# Apostila INSS - Tecnico do Seguro Social

> **Status atual:** edicao `0.1.0-auditoria`, em fase de curadoria e pre-edital. Este repositorio ainda nao representa uma edicao aprovada para comercializacao.

O projeto gera um PDF educacional independente. Nenhuma informacao sobre vagas, salario, banca ou edital futuro deve ser tratada como confirmada sem publicacao oficial.

Apostila de estudo completa para o concurso do **INSS (Instituto Nacional do Seguro Social)**, cargo de **Técnico do Seguro Social**, cobrindo **todas as 9 disciplinas** do edital.

## 📋 Disciplinas Cobertas

| # | Disciplina | Peso na Prova | Tópicos | Status |
|---|---|---|---|---|
| 1 | 🛡️ Direito Previdenciário | **~25%** | 12 tópicos | ✅ Completo |
| 2 | 📖 Língua Portuguesa | ~18% | 10 tópicos | ✅ Completo |
| 3 | ⚖️ Direito Constitucional | ~12% | 6 tópicos | ✅ Completo |
| 4 | 🏛️ Direito Administrativo | ~12% | 5 tópicos | ✅ Completo |
| 5 | 🧮 Raciocínio Lógico-Matemático | ~10% | 6 tópicos | ✅ Completo |
| 6 | 🤝 Ética no Serviço Público | ~8% | 2 tópicos | ✅ Completo |
| 7 | 💻 Informática | ~8% | 6 tópicos | ✅ Completo |
| 8 | 📊 Noções de Contabilidade | ~4% | 3 tópicos | ✅ Completo |
| 9 | 🌍 Atualidades | ~3% | 3 tópicos | ✅ Completo |

## Estrutura do Projeto

```
apostila-inss-completa/
├── README.md                    # Este arquivo
├── .gitignore                   # Arquivos ignorados
├── inss-ebook/
│   ├── Apostila_INSS_Completa.pdf  # 📄 PDF final (119 KB)
│   ├── main.py                  # Ponto de entrada
│   ├── generator.py             # Gerador PDF (reportlab)
│   ├── content.py               # Conteúdo das 9 disciplinas
│   └── styles.py                # Configurações de estilo e cores
│   ├── metadata.py               # Versao, status e data de corte
│   ├── sources.yaml              # Matriz inicial de fontes oficiais
│   ├── question_review.yaml      # Manifesto das 12 questoes para revisao
│   └── validate_content.py       # Gate editorial antes do build
├── docs/
│   └── editorial-policy.md       # Politica de fontes, revisao e lancamento
│   └── simulated-external-review.md # Simulacao interna do parecer
├── requirements.txt              # Dependencias do gerador
├── memory/
│   └── 2025-08-19-apostila-inss.md  # Registro de progresso
└── AGENTS.md                    # Configuração do assistente IA
```

## 🎨 Design do PDF

O ebook foi gerado com diagramação profissional usando **ReportLab**:

- **Capa principal** com cores institucionais (azul + dourado)
- **9 capas de disciplina**, cada uma com cor e ícone próprios
- **Sumário navegável** com pesos de cada disciplina
- **Boxes de destaque** com dicas da prova (🎯)
- **Exercícios comentados** por disciplina com gabarito
- **Página de estratégia** com cronograma de estudos

## Como validar e gerar o PDF

```bash
pip install -r requirements.txt
cd inss-ebook
python3 main.py --validate
python3 main.py --output Apostila_INSS_Completa.pdf
```

O comando `--validate` verifica a estrutura minima e exibe pendencias editoriais. Use `--strict` para bloquear tambem os avisos. Uma validacao estrutural bem-sucedida nao substitui revisao juridica, pedagogica ou checagem de direitos autorais.

## 📖 Fontes de Pesquisa

- **Edital INSS 2022** (Cebraspe) — conteúdo programático oficial
- **Estratégia Concursos** — análise de disciplinas e pesos
- **JR Concursos** — material gratuito por disciplina
- **SPES Edu** — conteúdo programático INSS 2026
- **Lei 8.213/91** — Planos de Benefícios da Previdência Social
- **Decreto 3.048/99** — Regulamento da Previdência Social
- **EC 103/2019** — Reforma da Previdência
- **CF/88** — Constituição Federal
- **Lei 8.112/90** — Regime Jurídico dos Servidores

## 📊 Dados do Concurso

| Item | Informação |
|---|---|
| **Cargo** | Técnico do Seguro Social (TSS) |
| **Nível** | Médio |
| **Salário inicial** | R$ 5.905,79 (40h semanais) |
| **Banca prevista** | Cebraspe (CESPE/UnB) |
| **Formato da prova** | Certo/Errado (com penalidade) |
| **Vagas previstas** | 3.000+ (edital 2026) |
| **Edital esperado** | 2º semestre 2026 |

## 🎯 Estratégia de Estudos

1. **Meses 1-2:** Português + Raciocínio Lógico (base)
2. **Meses 3-4:** Direito Previdenciário a fundo (25% da prova!)
3. **Meses 5-6:** Direito Constitucional + Administrativo + Ética
4. **Meses 7-8:** Informática + Contabilidade + Revisão geral

> **Dica:** Direito Previdenciário é a disciplina com maior peso (~25%). Estude a Lei 8.213/91 linha por linha e resolva 500+ questões antes da prova.

---

**Edicao atual:** 0.1.0-auditoria  
**Data de corte:** 19/08/2026  
**Material educacional independente - nao aprovado para comercializacao**

O PDF de auditoria gerado em `inss-ebook/Apostila_INSS_Auditoria.pdf` foi inspecionado visualmente e possui 72 paginas. A matriz de fontes e o manifesto de questoes ainda aguardam revisao juridica externa, confirmacao de autoria/licenca e assinatura do revisor.

A simulacao de revisao esta em `docs/simulated-external-review.md` e conclui pelo bloqueio de comercializacao ate a correcao dos achados.
