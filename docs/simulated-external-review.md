# Simulacao de revisao externa

## Natureza do documento

Esta e uma simulacao interna de revisao tecnica, feita em 19/08/2026 a partir do conteudo do repositorio. Nao e parecer juridico, nao substitui revisao por advogado ou professor especializado e nao autoriza comercializacao.

## Decisao simulada

**NAO APROVAR PARA VENDA.**

Motivos: existem afirmacoes juridicas que exigem correcao ou verificacao em fonte oficial, as questoes ainda nao possuem confirmacao de autoria/licenca e nenhum revisor externo independente assinou o material.

## Correcoes aplicadas apos a simulacao

Em 19/08/2026, foram corrigidos os pontos de maior risco no conteudo: referencias do Codigo de Etica foram direcionadas ao anexo e suas secoes; Improbidade deixou de usar sanções, prescricao e legitimidade apresentadas como regras antigas; periodo de graca passou a indicar extensoes condicionais; e as questoes previdenciarias, de Etica e de Atualidades foram reescritas com hipoteses e ressalvas.

Essas mudancas reduzem os achados conhecidos, mas exigem nova conferencia artigo a artigo por revisor externo antes de qualquer aprovacao.

## Achados criticos

### CRITICO-01 - Codigo de Etica

O conteudo atribui deveres e proibicoes aos “Art. 11” e “Art. 12” do Decreto no 1.171/1994. O Codigo de Etica esta no anexo do decreto e deve ser citado pela secao, item ou alinea correspondente, nao por essa numeracao generica de artigos. **Acao:** revisar toda a secao de Etica diretamente no texto oficial e substituir as referencias.

### CRITICO-02 - Improbidade administrativa

O conteudo mistura classificacoes e sancoes que precisam ser revistas conforme a Lei no 8.429/1992 com as alteracoes da Lei no 14.230/2021. A redacao sobre culpa grave, legitimidade ativa, prescricao e duracao das sancoes nao pode permanecer sem conferencia artigo a artigo. **Acao:** reescrever os tres tipos de ato, elemento subjetivo, sancoes e prescricao usando a redacao vigente.

### CRITICO-03 - Previdenciario

As secoes de periodo de graca, contribuicoes, aposentadorias, pensao por morte, salario de beneficio e regras de transicao usam formulas resumidas sem explicitar segurado, marco temporal, excecoes e requisitos. **Acao:** revisar cada regra na Lei no 8.213/1991, Lei no 8.212/1991, Decreto no 3.048/1999 e EC no 103/2019, com artigo e data de corte.

### CRITICO-04 - Escopo do edital

Pesos, disciplinas, banca e dados de concurso nao podem ser tratados como oficiais enquanto nao houver edital ou comunicado oficial aplicavel. A edicao deve permanecer marcada como `pre-edital`.

## Revisao simulada das questoes

| ID | Resultado simulado | Pendencia principal |
|---|---|---|
| portugues-q01 | corrigir/confirmar | Gabarito plausivel, mas deve receber fonte didatica e revisao de formulacao. |
| portugues-q02 | corrigir/confirmar | Resposta A parece adequada; conferir se a alternativa D nao cria ambiguidade sintatica. |
| raciocinio-q01 | aprovado condicional | Equivalencia logica esta adequada; falta fonte/autoria e revisao independente. |
| raciocinio-q02 | aprovado condicional | Calculo da PA esta adequado; falta fonte/autoria e revisao independente. |
| constitucional-q01 | aprovado condicional | Gabarito C esta coerente com a separacao entre Arts. 1 e 2; citar CF, Arts. 1 e 2. |
| administrativo-q01 | aprovado condicional | Resposta C e coerente com o caput do Art. 37, mas a explicacao deve distinguir CF e Lei 9.784/1999. |
| previdenciario-q01 | corrigir/confirmar | Periodo de graca depende de requisitos e extensoes especificas; comentario esta simplificado demais. |
| previdenciario-q02 | corrigir/confirmar | Formula apresentada depende do beneficio e do regime aplicavel; nao usar “salario de beneficio” como sinonimo automatico da renda. |
| etica-q01 | corrigir | “Vantagem pessoal” e amplo demais para concluir automaticamente Art. 9; separar enriquecimento ilicito, violacao de principios e eventual infração disciplinar. |
| informatica-q01 | aprovado condicional | Funcao MÁXIMO esta correta; registrar versao/localizacao da funcao e autoria. |
| contabilidade-q01 | aprovado condicional | Resposta B e coerente com competencia; registrar fonte contabil e autoria. |
| atualidades-q01 | corrigir/atualizar | “Principal instrumento” exige formulacao temporal e fonte do Banco Central; atualidades deve ter data de corte. |

## Achados de produto e direitos

- As 12 questoes estao marcadas como `internal-draft`, mas isso ainda nao prova autoria exclusiva.
- `license_status` permanece pendente em [question_review.yaml](../inss-ebook/question_review.yaml).
- A matriz de fontes tem URLs e data de catalogacao, mas ainda nao tem conferencia juridica externa.
- O acesso ao Planalto nao foi confirmado no ambiente de execucao; os portais INSS e Cebraspe responderam.
- O PDF foi gerado e inspecionado, mas qualidade visual nao substitui revisao de conteudo.

## Plano de correcao exigido

1. Revisar integralmente Etica, Improbidade e Previdenciario em fonte oficial.
2. Criar uma linha de fonte e dispositivo para cada afirmacao juridica de risco.
3. Corrigir ou reescrever as questoes classificadas como `corrigir`.
4. Confirmar autoria ou obter licenca para cada questao.
5. Fazer segunda leitura por revisor pedagogico.
6. Obter nome, qualificacao, data e assinatura do revisor juridico externo.
7. Rodar novamente `python3 inss-ebook/main.py --validate --strict`.
8. Somente liberar a edicao quando nao houver pendencias criticas, juridicas ou de direitos autorais.

## Conclusao

A simulacao confirma que a infraestrutura de publicacao esta funcional, mas o produto ainda e uma edicao de auditoria. A decisao profissional simulada e **bloqueio de comercializacao** ate a correcao dos achados e a assinatura de revisores independentes.
