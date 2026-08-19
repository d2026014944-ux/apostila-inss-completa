"""Gerador de PDF profissional para o ebook INSS."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, Color, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Flowable, Frame, PageTemplate, BaseDocTemplate
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import re

from styles import CORES, CORES_DISCIPLINA, ICONES, PESOS
from content import DISCIPLINAS

# =====================================================
# CONSTANTES
# =====================================================
LARGURA, ALTURA = A4
MARGEM = 2 * cm
LARGURA_UTIL = LARGURA - 2 * MARGEM

# =====================================================
# CORES HEX
# =====================================================
def hex_cor(rgb_tuple):
    return '#{:02x}{:02x}{:02x}'.format(*rgb_tuple)

C_PRIMARIA = hex_cor(CORES['primaria'])
C_SECUNDARIA = hex_cor(CORES['secundaria'])
C_DESTAQUE = hex_cor(CORES['destaque'])
C_SUCESSO = hex_cor(CORES['sucesso'])
C_FUNDO_BOX = hex_cor(CORES['fundo_box'])
C_FUNDO_DICA = hex_cor(CORES['fundo_dica'])
C_FUNDO_EXERCICIO = hex_cor(CORES['fundo_exercicio'])
C_FUNDO_ALERTA = hex_cor(CORES['fundo_alerta'])
C_CINZA = hex_cor(CORES['cinza_medio'])
C_BRANCO = '#ffffff'
C_PRETO = '#000000'

# =====================================================
# ESTILOS
# =====================================================
styles = getSampleStyleSheet()

# Estilo para título da disciplina
style_disciplina = ParagraphStyle(
    'Disciplina',
    parent=styles['Heading1'],
    fontSize=26,
    leading=32,
    textColor=HexColor(C_BRANCO),
    alignment=TA_LEFT,
    spaceAfter=6*mm,
    fontName='Helvetica-Bold',
)

# Estilo para subtítulo da disciplina
style_subtitulo_disciplina = ParagraphStyle(
    'SubtituloDisciplina',
    parent=styles['Normal'],
    fontSize=13,
    leading=18,
    textColor=HexColor('#e0e0e0'),
    alignment=TA_LEFT,
    fontName='Helvetica',
)

# Estilo para tópico
style_topico = ParagraphStyle(
    'Topico',
    parent=styles['Heading2'],
    fontSize=17,
    leading=22,
    textColor=HexColor(C_PRIMARIA),
    spaceBefore=8*mm,
    spaceAfter=4*mm,
    fontName='Helvetica-Bold',
)

# Estilo para conteúdo
style_conteudo = ParagraphStyle(
    'Conteudo',
    parent=styles['Normal'],
    fontSize=10.5,
    leading=16,
    textColor=HexColor('#333333'),
    alignment=TA_JUSTIFY,
    spaceAfter=3*mm,
    fontName='Helvetica',
)

# Estilo para listas
style_lista = ParagraphStyle(
    'Lista',
    parent=style_conteudo,
    leftIndent=8*mm,
    bulletIndent=3*mm,
    spaceAfter=1.5*mm,
)

# Estilo para dica
style_dica = ParagraphStyle(
    'Dica',
    parent=styles['Normal'],
    fontSize=10,
    leading=15,
    textColor=HexColor('#8B6914'),
    alignment=TA_LEFT,
    fontName='Helvetica-Oblique',
    leftIndent=4*mm,
)

# Estilo para exercício
style_exercicio = ParagraphStyle(
    'Exercicio',
    parent=styles['Normal'],
    fontSize=10.5,
    leading=16,
    textColor=HexColor('#333333'),
    alignment=TA_LEFT,
    fontName='Helvetica',
    spaceAfter=2*mm,
)

# Estilo para alternativa
style_alternativa = ParagraphStyle(
    'Alternativa',
    parent=styles['Normal'],
    fontSize=10.5,
    leading=15,
    textColor=HexColor('#333333'),
    alignment=TA_LEFT,
    fontName='Helvetica',
    leftIndent=8*mm,
    spaceAfter=1*mm,
)

# Estilo para resposta
style_resposta = ParagraphStyle(
    'Resposta',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    textColor=HexColor(C_SUCESSO),
    alignment=TA_LEFT,
    fontName='Helvetica-Bold',
    spaceBefore=2*mm,
)

# Estilo para comentário
style_comentario = ParagraphStyle(
    'Comentario',
    parent=styles['Normal'],
    fontSize=9.5,
    leading=14,
    textColor=HexColor(C_CINZA),
    alignment=TA_LEFT,
    fontName='Helvetica-Oblique',
    leftIndent=8*mm,
)

# Estilo do sumário
style_sumario_titulo = ParagraphStyle(
    'SumarioTitulo',
    parent=styles['Heading1'],
    fontSize=22,
    textColor=HexColor(C_PRIMARIA),
    alignment=TA_CENTER,
    spaceAfter=10*mm,
    fontName='Helvetica-Bold',
)

style_sumario_item = ParagraphStyle(
    'SumarioItem',
    parent=styles['Normal'],
    fontSize=12,
    leading=20,
    textColor=HexColor('#333333'),
    fontName='Helvetica',
    leftIndent=5*mm,
)

style_sumario_peso = ParagraphStyle(
    'SumarioPeso',
    parent=styles['Normal'],
    fontSize=11,
    leading=20,
    textColor=HexColor(C_DESTAQUE),
    fontName='Helvetica-Bold',
    alignment=TA_RIGHT,
)

# =====================================================
# COMPONENTES CUSTOMIZADOS
# =====================================================

class BordaColorida(Flowable):
    """Linha horizontal colorida decorativa."""
    def __init__(self, width, height=2, color=C_PRIMARIA):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.canv.setFillColor(HexColor(self.color))
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)


class BoxDestaque(Flowable):
    """Caixa colorida com conteúdo (dica, alerta, etc)."""
    def __init__(self, text, largura, cor_fundo, cor_borda, icone='💡', style=None):
        Flowable.__init__(self)
        self.text = text
        self.largura = largura
        self.cor_fundo = cor_fundo
        self.cor_borda = cor_borda
        self.icone = icone
        self.style = style or style_dica
        self._para = Paragraph(f'{icone} {text}', self.style)
        self._w, self._h = self._para.wrap(largura - 12*mm, 1000*cm)

    def wrap(self, availWidth, availHeight):
        return self.largura, self._h + 10*mm

    def draw(self):
        self.canv.setFillColor(HexColor(self.cor_fundo))
        self.canv.setStrokeColor(HexColor(self.cor_borda))
        self.canv.setLineWidth(2)
        self.canv.roundRect(0, 0, self.largura, self._h + 10*mm, 4, fill=1, stroke=1)
        # Barra lateral
        self.canv.setFillColor(HexColor(self.cor_borda))
        self.canv.rect(0, 0, 4, self._h + 10*mm, fill=1, stroke=0)
        self._para.drawOn(self.canv, 8*mm, 4*mm)


class CapaDisciplina(Flowable):
    """Capa colorida para cada disciplina."""
    def __init__(self, nome, chave, peso, descricao, largura, altura_pagina):
        Flowable.__init__(self)
        self.nome = nome
        self.chave = chave
        self.peso = peso
        self.descricao = descricao
        self.largura = largura
        self.altura_pagina = altura_pagina
        self.cor = hex_cor(CORES_DISCIPLINA.get(chave, CORES['primaria']))
        self.icone = ICONES.get(chave, '📘')

    def wrap(self, availWidth, availHeight):
        return self.largura, self.altura_pagina - 4*cm

    def draw(self):
        w = self.largura
        h = self.altura_pagina - 4*cm
        # Fundo
        self.canv.setFillColor(HexColor(self.cor))
        self.canv.roundRect(0, 0, w, h, 8, fill=1, stroke=0)
        # Borda inferior
        self.canv.setFillColor(HexColor(C_DESTAQUE))
        self.canv.rect(0, 0, w, 6, fill=1, stroke=0)
        # Ícone
        self.canv.setFont('Helvetica', 60)
        self.canv.setFillColor(HexColor(C_BRANCO))
        self.canv.drawString(15*mm, h - 35*mm, self.icone)
        # Nome
        self.canv.setFont('Helvetica-Bold', 30)
        self.canv.setFillColor(HexColor(C_BRANCO))
        self.canv.drawString(15*mm, h - 55*mm, self.nome)
        # Peso
        self.canv.setFont('Helvetica-Bold', 16)
        self.canv.setFillColor(HexColor(C_DESTAQUE))
        self.canv.drawString(15*mm, h - 70*mm, f'Peso na prova: {self.peso}')
        # Descrição
        self.canv.setFont('Helvetica', 12)
        self.canv.setFillColor(HexColor('#e0e0e0'))
        # Word wrap manual
        palavras = self.descricao.split()
        linha = ''
        y = h - 90*mm
        for p in palavras:
            teste = linha + ' ' + p if linha else p
            if self.canv.stringWidth(teste, 'Helvetica', 12) < w - 30*mm:
                linha = teste
            else:
                self.canv.drawString(15*mm, y, linha)
                y -= 16
                linha = p
        if linha:
            self.canv.drawString(15*mm, y, linha)


# =====================================================
# TEMPLATE DE PÁGINA
# =====================================================

def cabecalho_rodape(canvas, doc):
    """Adiciona cabeçalho e rodapé em cada página."""
    canvas.saveState()
    # Cabeçalho
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(HexColor(C_CINZA))
    canvas.drawString(MARGEM, ALTURA - 1.2*cm, 'Apostila Completa INSS — Técnico do Seguro Social')
    canvas.drawRightString(LARGURA - MARGEM, ALTURA - 1.2*cm, f'Página {doc.page}')
    # Linha separadora
    canvas.setStrokeColor(HexColor('#cccccc'))
    canvas.setLineWidth(0.5)
    canvas.line(MARGEM, ALTURA - 1.4*cm, LARGURA - MARGEM, ALTURA - 1.4*cm)
    # Rodapé
    canvas.setFont('Helvetica', 7)
    canvas.setFillColor(HexColor(C_CINZA))
    canvas.drawCentredString(LARGURA/2, 1*cm, 'Material de estudo para concurso INSS — Uso pessoal — Todos os direitos reservados')
    canvas.restoreState()


def capa_rodape(canvas, doc):
    """Sem cabeçalho/rodapé na capa."""
    pass


# =====================================================
# FUNÇÕES DE CONTEÚDO
# =====================================================

def processar_texto(texto, cor_disciplina=C_PRIMARIA):
    """Converte markdown simples em Paragraphs do ReportLab."""
    elementos = []
    linhas = texto.strip().split('\n')

    for linha in linhas:
        linha = linha.strip()
        if not linha:
            elementos.append(Spacer(1, 2*mm))
            continue

        # Negrito
        linha = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', linha)
        # Itálico
        linha = re.sub(r'\*(.*?)\*', r'<i>\1</i>', linha)

        if linha.startswith('•'):
            texto_item = linha[1:].strip()
            elementos.append(Paragraph(
                f'<bullet>&bull;</bullet>{texto_item}',
                style_lista
            ))
        elif linha.startswith(('I ', 'II ', 'III ', 'IV ', 'V ', 'VI ', 'VII ', 'VIII ', 'IX ', 'X ')):
            elementos.append(Paragraph(
                f'<bullet>{linha[:linha.index(" ")+1]}</bullet>{linha[linha.index(" ")+1:].strip()}',
                style_lista
            ))
        else:
            elementos.append(Paragraph(linha, style_conteudo))

    return elementos


def criar_sumario():
    """Cria a página de sumário."""
    elementos = []
    elementos.append(Spacer(1, 15*mm))
    elementos.append(Paragraph('SUMÁRIO', style_sumario_titulo))
    elementos.append(BordaColorida(LARGURA_UTIL, 3, C_PRIMARIA))
    elementos.append(Spacer(1, 8*mm))

    for i, disc in enumerate(DISCIPLINAS):
        nome = disc['nome']
        chave = disc['chave']
        peso = disc['peso']
        icone = ICONES.get(chave, '📘')
        cor = hex_cor(CORES_DISCIPLINA.get(chave, CORES['primaria']))

        # Linha do sumário com tabela
        num = f'{i+1:02d}'
        t = Table(
            [[Paragraph(f'{icone}  {num}. {nome}', style_sumario_item),
              Paragraph(f'{peso}', style_sumario_peso)]],
            colWidths=[LARGURA_UTIL * 0.75, LARGURA_UTIL * 0.25],
            rowHeights=[10*mm]
        )
        t.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LINEBELOW', (0,0), (-1,-1), 0.5, HexColor('#eeeeee')),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ]))
        elementos.append(t)

    elementos.append(Spacer(1, 10*mm))
    elementos.append(BordaColorida(LARGURA_UTIL, 1, C_CINZA))
    elementos.append(Spacer(1, 5*mm))
    elementos.append(Paragraph(
        '<i>Total de 9 disciplinas • Conteúdo baseado nos últimos editais INSS (2022/2025)</i>',
        ParagraphStyle('Nota', parent=style_conteudo, fontSize=9, textColor=HexColor(C_CINZA), alignment=TA_CENTER)
    ))

    return elementos


def criar_capa_principal():
    """Cria a capa principal do ebook."""
    elementos = []
    elementos.append(Spacer(1, 25*mm))

    # Título principal
    elementos.append(Paragraph(
        '<font color="#ffffff"><b>APOSTILA COMPLETA</b></font>',
        ParagraphStyle('T1', parent=styles['Title'], fontSize=36, textColor=white, alignment=TA_CENTER, fontName='Helvetica-Bold')
    ))
    elementos.append(Spacer(1, 5*mm))
    elementos.append(Paragraph(
        '<font color="#ffffff"><b>CONCURSO INSS</b></font>',
        ParagraphStyle('T2', parent=styles['Title'], fontSize=42, textColor=HexColor(C_DESTAQUE), alignment=TA_CENTER, fontName='Helvetica-Bold')
    ))
    elementos.append(Spacer(1, 8*mm))
    elementos.append(Paragraph(
        '<font color="#ffffff">Técnico do Seguro Social</font>',
        ParagraphStyle('T3', parent=styles['Title'], fontSize=18, textColor=HexColor('#e0e0e0'), alignment=TA_CENTER, fontName='Helvetica')
    ))
    elementos.append(Spacer(1, 15*mm))
    elementos.append(BordaColorida(LARGURA_UTIL * 0.6, 3, C_DESTAQUE))
    elementos.append(Spacer(1, 15*mm))

    # Disciplinas
    disciplinas_texto = ' • '.join([d['nome'] for d in DISCIPLINAS])
    elementos.append(Paragraph(
        f'<font color="#cccccc">{disciplinas_texto}</font>',
        ParagraphStyle('Disc', parent=style_conteudo, fontSize=10, textColor=HexColor('#cccccc'), alignment=TA_CENTER)
    ))

    elementos.append(Spacer(1, 30*mm))
    elementos.append(Paragraph(
        '<font color="#999999">Material de estudo completo • Todas as 9 disciplinas do edital</font>',
        ParagraphStyle('Sub', parent=style_conteudo, fontSize=11, textColor=HexColor('#999999'), alignment=TA_CENTER)
    ))
    elementos.append(Spacer(1, 5*mm))
    elementos.append(Paragraph(
        '<font color="#999999">2026</font>',
        ParagraphStyle('Ano', parent=style_conteudo, fontSize=14, textColor=HexColor(C_DESTAQUE), alignment=TA_CENTER, fontName='Helvetica-Bold')
    ))

    return elementos


def criar_pagina_disciplina(disc, idx):
    """Cria todas as páginas de uma disciplina."""
    elementos = []
    nome = disc['nome']
    chave = disc['chave']
    peso = disc['peso']
    descricao = disc['descricao']
    topicos = disc['topicos']
    exercicios = disc.get('exercicios', [])
    cor = hex_cor(CORES_DISCIPLINA.get(chave, CORES['primaria']))
    icone = ICONES.get(chave, '📘')

    # Capa da disciplina
    elementos.append(CapaDisciplina(nome, chave, peso, descricao, LARGURA_UTIL, ALTURA))
    elementos.append(PageBreak())

    # Tópicos
    for j, topico in enumerate(topicos):
        titulo = topico['titulo']
        conteudo = topico['conteudo']
        dica = topico.get('dica', '')

        # Título do tópico
        elementos.append(Paragraph(
            f'{icone} {titulo}',
            ParagraphStyle('TopicoColor', parent=style_topico, textColor=HexColor(cor))
        ))
        elementos.append(BordaColorida(LARGURA_UTIL, 2, cor))
        elementos.append(Spacer(1, 3*mm))

        # Conteúdo
        elementos.extend(processar_texto(conteudo, cor))

        # Dica
        if dica:
            elementos.append(Spacer(1, 3*mm))
            elementos.append(BoxDestaque(
                f'<b>Dica da prova:</b> {dica}',
                LARGURA_UTIL,
                C_FUNDO_DICA,
                C_DESTAQUE,
                '🎯'
            ))

        elementos.append(Spacer(1, 8*mm))

    # Exercícios
    if exercicios:
        elementos.append(PageBreak())
        elementos.append(Paragraph(
            f'📝 Exercícios — {nome}',
            ParagraphStyle('ExTitulo', parent=style_topico, textColor=HexColor(cor), fontSize=20)
        ))
        elementos.append(BordaColorida(LARGURA_UTIL, 3, cor))
        elementos.append(Spacer(1, 5*mm))

        for k, ex in enumerate(exercicios):
            elementos.append(BoxDestaque(
                f'<b>Questão {k+1}:</b> {ex["enunciado"]}',
                LARGURA_UTIL,
                C_FUNDO_BOX,
                cor,
                '❓'
            ))
            elementos.append(Spacer(1, 3*mm))

            for alt in ex['alternativas']:
                elementos.append(Paragraph(alt, style_alternativa))

            elementos.append(Spacer(1, 2*mm))
            elementos.append(Paragraph(
                f'✅ Resposta: {ex["resposta"]}',
                style_resposta
            ))
            elementos.append(Paragraph(
                f'💬 {ex["comentario"]}',
                style_comentario
            ))
            elementos.append(Spacer(1, 6*mm))

    return elementos


def criar_pagina_estrategia():
    """Cria página de estratégia de estudos."""
    elementos = []
    elementos.append(PageBreak())

    elementos.append(Paragraph(
        '🎯 Estratégia de Estudos para o INSS',
        ParagraphStyle('EstTitulo', parent=style_topico, fontSize=22, textColor=HexColor(C_PRIMARIA))
    ))
    elementos.append(BordaColorida(LARGURA_UTIL, 3, C_DESTAQUE))
    elementos.append(Spacer(1, 8*mm))

    estrategias = [
        ('📅 Cronograma (6-8 meses)', 'Meses 1-2: Português + Raciocínio Lógico (base). Meses 3-4: Direito Previdenciário (a fundo). Meses 5-6: Direito Constitucional + Administrativo + Ética. Meses 7-8: Informática + Contabilidade + Revisão geral.'),
        ('⚖️ Direito Previdenciário é o jogo', '25% da prova! Estude Lei 8.213/91 e Decreto 3.048/99 linha por linha. Resolva 500+ questões de Previdenciário. É o que separa aprovados de reprovados.'),
        ('📋 Formato Cebraspe: Certo ou Errado', 'A banca usa formato único com penalidade por erro. Se não tem CERTEZA, não marque. Errar tira ponto. Treine milhares de questões Cebraspe.'),
        ('🔄 Revisão por flashcards', 'Previdenciário tem muitos números: prazos, idades, valores. Use Anki ou flashcards físicos para fixar dados numéricos.'),
        ('📝 Caderno de erros', 'Toda questão errada → anotação. Revisar o caderno semanalmente é o que separa 70% de 85% de acerto.'),
        ('🏃 Simulados completos', 'Faça 10+ simulados completos no formato Cebraspe antes da prova. Treine resistência mental (prova de 4h+).'),
        ('📚 Material recomendado', 'Lei 8.213/91 (texto integral). Decreto 3.048/99 (regulamento). Constituição Federal (Arts. 1-32). Lei 8.112/90 (regime jurídico). Decreto 1.171/94 (ética).'),
    ]

    for titulo, texto in estrategias:
        elementos.append(Paragraph(titulo, ParagraphStyle('EstTit', parent=style_topico, fontSize=14, textColor=HexColor(C_SECUNDARIA), spaceBefore=5*mm)))
        elementos.append(Paragraph(texto, style_conteudo))

    return elementos


# =====================================================
# GERAÇÃO DO PDF
# =====================================================

def gerar_pdf(nome_arquivo='Apostila_INSS_Completa.pdf'):
    """Gera o PDF completo."""
    doc = BaseDocTemplate(
        nome_arquivo,
        pagesize=A4,
        leftMargin=MARGEM,
        rightMargin=MARGEM,
        topMargin=2*cm,
        bottomMargin=1.5*cm,
        title='Apostila Completa INSS — Técnico do Seguro Social',
        author='Material de Estudo',
    )

    # Frames e templates
    frame = Frame(MARGEM, 1.5*cm, LARGURA_UTIL, ALTURA - 3.5*cm, id='normal')
    frame_capa = Frame(MARGEM, 1.5*cm, LARGURA_UTIL, ALTURA - 3.5*cm, id='capa')

    doc.addPageTemplates([
        PageTemplate(id='capa', frames=frame_capa, onPage=capa_rodape),
        PageTemplate(id='normal', frames=frame, onPage=cabecalho_rodape),
    ])

    # Construir story
    story = []

    # === CAPA PRINCIPAL ===
    story.extend(criar_capa_principal())
    story.append(PageBreak())

    # === SUMÁRIO ===
    story.extend(criar_sumario())
    story.append(PageBreak())

    # === DISCIPLINAS ===
    for i, disc in enumerate(DISCIPLINAS):
        story.extend(criar_pagina_disciplina(disc, i))
        if i < len(DISCIPLINAS) - 1:
            story.append(PageBreak())

    # === ESTRATÉGIA ===
    story.extend(criar_pagina_estrategia())

    # Gerar PDF
    doc.build(story)
    print(f'✅ PDF gerado com sucesso: {nome_arquivo}')
    return nome_arquivo


if __name__ == '__main__':
    gerar_pdf()
