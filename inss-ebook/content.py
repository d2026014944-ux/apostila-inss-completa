"""Conteúdo completo das disciplinas do concurso INSS."""

DISCIPLINAS = [
    # =====================================================
    # 1. LÍNGUA PORTUGUESA (~18% da prova)
    # =====================================================
    {
        'nome': 'Língua Portuguesa',
        'chave': 'portugues',
        'peso': '18%',
        'descricao': 'Interpretação de texto, gramática normativa, redação oficial e ortografia.',
        'topicos': [
            {
                'titulo': 'Interpretação de Texto',
                'conteudo': """A interpretação de texto é a habilidade de compreender, analisar e inferir informações a partir de um texto apresentado. No concurso INSS, é o tipo de questão mais recorrente.

**Tipos de texto cobrados:**
• Textos narrativos, dissertativos e injuntivos
• Textos jornalísticos e opinativos
• Textos técnicos e administrativos
• Charges, tirinhas e textos multimodais

**Habilidades exigidas:**
• Identificar tema central e ideias principais
• Distinguir fato de opinião
• Reconhecer ironia, sarcasmo e figuras de linguagem
• Inferir informações implícitas
• Identificar a intenção do autor
• Relacionar o texto com seu contexto de produção

**Estratégia para resolver:**
1. Leia o texto completo antes de ver as alternativas
2. Identifique o tema e a tese defendida
3. Volte ao texto para cada questão — nunca responda de memória
4. Elimine alternativas absurdas primeiro
5. Cuidado com palavras absolutas ("sempre", "nunca", "todos")""",
                'dica': 'A banca Cebraspe adora cobrar detalhes sutis do texto. Leia cada palavra com atenção.'
            },
            {
                'titulo': 'Gêneros Textuais',
                'conteudo': """Os gêneros textuais são formas padronizadas de comunicação que circulam socialmente.

**Gêneros mais cobrados no INSS:**
• **Ofício:** comunicação formal entre órgãos públicos
• **Memorando:** comunicação interna entre setores
• **Portaria:** ato administrativo de autoridade
• **Edital:** convocação pública
• **Relatório:** descrição de fatos ou atividades
• **Notícia:** relato jornalístico de fatos
• **Artigo de opinião:** texto argumentativo

**Estrutura do Ofício:**
1. Brasão + nome do órgão
2. Local e data
3. Destinatário (cargo + nome)
4. Assunto
5. Saudação protocolar
6. Corpo do texto (introdução, desenvolvimento, fechamento)
7. Despedida protocolar
8. Assinatura + cargo

**Estrutura do Memorando:**
1. Nome do órgão
2. Memorando Nº
3. De: (setor remetente)
4. Para: (setor destinatário)
5. Assunto
6. Data
7. Corpo do texto
8. Assinatura""",
                'dica': 'Cebraspe cobra bastante a estrutura formal dos documentos públicos. Memorize os campos obrigatórios.'
            },
            {
                'titulo': 'Ortografia e Acentuação',
                'conteudo': """**Regras de acentuação (Novo Acordo Ortográfico):**

**Tonicidade:**
• Oxítona: acentua se terminar em a, e, o, u, â, ê, ô (ex: café, sofá, papéis)
• Paroxítona: acentua se NÃO terminar em a, e, o, u, i, l, r, n, s, x (ex: lâmpada, música)
• Proparoxítona: SEMPRE se acentua (ex: médico, psicólogo)

**Ditongos abertos (ei, oi) — acentua apenas na sílaba tônica:**
• Paroxítonas: jiboia, assembleia, plateia
• Oxítonas: herói, dói, anzol

**Hiatos tônico:**
• a + a → saara, charuto (não acentua mais pelo Novo Acordo)
• e + e → veem, leem (acentua: vêem, lêem — para distinguir de "veem" do verbo ver)
• o + o → voo (mantém acento)

**Regras de uso do "s", "ss", "x", "z":**
• "ss" entre vogais: sempre som de "s" (ex: professor, ação)
• "s" entre vogais: som de "z" (ex: casa, asa)
• "x" entre vogais: som de "sh" (ex: caixa, feixe)
• "z" no final: palavras oxítonas terminadas em "iz" (ex: rapaz, juiz)""",
                'dica': 'O Novo Acordo Ortográfico eliminou o acento diferencial de "pára" (verbo parar) e "para" (preposição). Cuidado com questões armadilha!'
            },
            {
                'titulo': 'Morfologia: Classes de Palavras',
                'conteudo': """**Substantivo:**
• Próprio (João) / Comum (menino)
• Concreto (mesa) / Abstrato (amor)
• Simples (casa) / Composto (guarda-chuva)
• Coletivo (rebanho, matilha)

**Verbo:**
• Tempos: presente, pretérito, futuro
• Modos: indicativo, subjuntivo, imperativo
• Conjugação: 1ª (-ar), 2ª (-er), 3ª (-ir)

**Conjugação composta (tempos):**
• Pretérito perfeito composto: tenho cantado
• Pretérito mais-que-perfeito composto: tinha cantado
• Futuro do presente composto: terei cantado

**Advérbios:**
• De lugar: aqui, ali, acolá
• De tempo: hoje, ontem, amanhã
• De modo: bem, mal, assim
• De intensidade: muito, pouco, bastante
• De afirmação: sim, certamente
• De negação: não, jamais, nunca

**Preposições essenciais:**
• a, ante, após, até, com, contra, de, desde, em, entre, para, perante, por, sem, sob, sobre, trás""",
                'dica': 'Foco na conjugação dos verbos "ser", "estar", "ter", "haver" e "ir" — são os mais cobrados em questões de concordância.'
            },
            {
                'titulo': 'Sintaxe: Período Simples',
                'conteudo': """**Termos essenciais (obrigatórios):**
• **Sujeito:** quem pratica ou sofre a ação
  - Simples: Um único núcleo (O aluno estudou.)
  - Composto: Mais de um núcleo (João e Maria saíram.)
  - Indeterminado: Não se sabe ou não se quer dizer (Bateu à porta.)
  - Oração sem sujeito: Fenômenos da natureza (Choveu ontem.)

• **Predicado:** o que se afirma sobre o sujeito
  - Verbal: núcleo é verbo intransitivo (O sol nasceu.)
  - Nominal: núcleo é nome + cópula (Ela é bonita.)
  - Verbo-nominal: verbo + nome (Ele correu depressa.)

**Termos integrantes:**
• **Objeto direto:** sem preposição (Li o livro.)
• **Objeto indireto:** com preposição (Gosto de chocolate.)
• **Predicativo do objeto:** qualifica o objeto (Considero-o inteligente.)
• **Complemento nominal:** completar nome (Fome de justiça.)""",
                'dica': 'Para identificar o sujeito, pergunte: "Quem faz a ação?" Para o OD: "O quê?" + verbo. Para o OI: "De quê?" / "Em quê?" + verbo.'
            },
            {
                'titulo': 'Sintaxe: Período Composto',
                'conteudo': """**Coordenação (orações independentes):**
• Aditiva: e, nem, como também (Estudou e passou.)
• Adversativa: mas, porém, contudo (Estudou, mas não passou.)
• Alternativa: ou, ora...ora (Ou chove ou faz sol.)
• Conclusiva: logo, portanto, pois (Estudou, portanto passou.)
• Explicativa: porque, pois, que (Não saiu, porque chovia.)

**Subordinação (oração dependente):**
• Substantiva: funciona como substantivo (Quero que você estude.)
• Adjetiva: funciona como adjetivo (O livro que li é bom.)
• Adverbial: funciona como advérbio
  - Causal: porque, visto que
  - Condicional: se, caso, desde que
  - Concessiva: embora, ainda que
  - Temporal: quando, enquanto
  - Final: para que, a fim de
  - Consecutiva: tão...que, tanto...que
  - Comparativa: como, do que, quanto

**Ponto e vírgula:**
• Separar orações coordenadas longas
• Separar itens de enumeração
• Antes de "porém", "portanto", "contudo" no meio da frase""",
                'dica': 'Cebraspe adora cobrar crase antes de "ela" e pronomes relativos. Revise: "à qual", "àquela", "às quais".'
            },
            {
                'titulo': 'Concordância Verbal e Nominal',
                'conteudo': """**Concordância verbal — casos especiais:**

• Sujeito posposto: concorda com o núcleo (Chegaram os alunos / Chegou os alunos — errado)
• Sujeito composto antes do verbo: plural (João e Maria saíram.)
• Sujeito composto após o verbo: pode concordar com o mais próximo (Saíram ou saiu João e Maria — ambas aceitas)
• Expressões partitivas: "a maioria dos alunos aprovou/aprovaram" (ambas aceitas)
• Verbo "haver" (sentido existir): IMPERSONAL — sempre singular (Havia muitos alunos.)
• Verbo "fazer" (tempo decorrido): IMPERSONAL (Faz/Fazia dois anos.)
• Verbo "ser": concorda com o predicativo (O problema são/sou eu — ambas aceitas)

**Concordância nominal:**
• Geralmente obrigatória (Boas vindas / Boas vindas — aceita)
• Numeral + substantivo: pode flexionar (Dois/Duas horas)
• Meia (substantivo) vs. Meio (advérbio) — "Meia hora" vs. "Meio dia"

**Crase:**
• Obrigatória: preposição "a" + artigo "a" (Fui à escola.)
• Proibida: antes de verbos, pronome possessivo feminino, "uma"
• Facultativa: antes de nomes próprios femininos
• Regra: substitua por "ele" — se couber, tem crase""",
                'dica': 'O erro mais comum em provas: "Houveram muitos acidentes" — ERRADO. "Haver" no sentido de existir é IMPERSONAL.'
            },
            {
                'titulo': 'Pontuação',
                'conteudo': """**Vírgula — regras principais:**
1. Separar vocativo (Venha cá, João.)
2. Separar aposto (Brasília, capital do Brasil,)
3. Separar oração adjetiva explicativa (Meu pai, que é médico,)
4. Isolar adjunto adverbial deslocado (Ontem, fui ao cinema.)
5. Separar termos repetidos (Ele, ele mesmo, fez isso.)
6. Antes de "e", "mas", "porém" quando há troca de sujeito

**Ponto e vírgula:**
• Orações coordenadas longas
• Enumerações complexas
• Antes de conectivos adversativos

**Dois-pontos:**
• Ante de citação
• Antes de enumeração
• Antes de explicação ou esclarecimento
• Em diálogos

**Ponto de interrogação e exclamação:**
• Encerram orações interrogativas e exclamativas
• Cuidado com orações indiretas (Perguntou se viria. — sem "?")""",
                'dica': 'A vírgula antes de "que" introduzindo oração substantiva é proibida: "Eu acho, que ele vem" — ERRADO.'
            },
            {
                'titulo': 'Figuras de Linguagem',
                'conteudo': """**Principais figuras cobradas:**

• **Metáfora:** comparação implícita (Ele é um leão.)
• **Comparação/Símile:** comparação explícita (Ele forte como um leão.)
• **Metonímia:** substituição por relação de proximidade (Leu Machado de Assis = leu as obras)
• **Antítese:** ideias opostas (O amor e o ódio.)
• **Ironia:** dizer o contrário do que se pensa
• **Eufemismo:** suavizar expressão (Ele faleceu = morreu.)
• **Hipérbole:** exagero (Morri de rir.)
• **Personificação:** atribuir qualidades humanas (O sol sorriu.)
• **Onomatopeia:** reproduzir sons (Miau, au-au.)
• **Pleonasmo:** repetição intencional (Eu vi com meus próprios olhos.)

**Figuras de som:**
• **Aliteração:** repetição de consoantes (Riso ruim, rápido, raro.)
• **Assonância:** repetição de vogais (O teu amor é flor.)""",
                'dica': 'Cebraspe cobra a identificação da figura em trechos de poemas e letras de música. Memorize as definições.'
            },
            {
                'titulo': 'Coesão e Coerência Textual',
                'conteudo': """**Coesão referencial:**
• Pronomes pessoais (ele, ela, eles)
• Pronomes demonstrativos (este, esse, aquele)
• Pronomes relativos (que, o qual, cujo)
• Substituição lexical (sinônimos, hiperônimos)

**Coesão sequencial:**
• **Adição:** e, além disso, ainda, também
• **Adversação:** mas, porém, contudo, entretanto
• **Consequência:** portanto, logo, assim, por isso
• **Causa:** porque, pois, uma vez que
• **Tempo:** depois, em seguida, então, enquanto
• **Conclusão:** enfim, em suma, em resumo

**Coerência:**
• Progressão temática (o texto deve avançar)
• Não-contradição (sem afirmações conflitantes)
• Relevância (informações pertinentes ao tema)
• Conectividade (relação lógica entre as partes)""",
                'dica': 'Questões de coesão pedem para trocar ou inserir conectivos. Leia a frase inteira para entender a relação lógica.'
            },
        ],
        'exercicios': [
            {
                'enunciado': 'Assinale a alternativa em que há erro de concordância verbal.',
                'alternativas': [
                    'A) Chegaram os meninos atrasados.',
                    'B) Haviam muitos candidatos na sala.',
                    'C) Faz dois anos que ele partiu.',
                    'D) A maioria dos alunos aprovou o teste.',
                ],
                'resposta': 'B',
                'comentario': 'O verbo "haver" no sentido de existir é IMPERSONAL — sempre singular. O correto é "Havia muitos candidatos".'
            },
            {
                'enunciado': 'Em qual alternativa a vírgula está sendo usada para isolar um aposto?',
                'alternativas': [
                    'A) Brasília, capital do Brasil, é uma cidade planejada.',
                    'B) Venha cá, João, preciso falar com você.',
                    'C) Ontem, fui ao cinema com meus amigos.',
                    'D) Ele, cansado, deitou-se no sofá.',
                ],
                'resposta': 'A',
                'comentario': 'O aposto é um termo que explica ou resume outro. "Capital do Brasil" explica "Brasília".'
            },
        ],
    },

    # =====================================================
    # 2. RACIOCÍNIO LÓGICO-MATEMÁTICO (~10% da prova)
    # =====================================================
    {
        'nome': 'Raciocínio Lógico-Matemático',
        'chave': 'raciocinio',
        'peso': '10%',
        'descricao': 'Lógica proposicional, sequências, problemas de lógica e matemática básica.',
        'topicos': [
            {
                'titulo': 'Lógica Proposicional',
                'conteudo': """**Proposições:**
Uma proposição é uma frase que pode ser classificada como verdadeira (V) ou falsa (F).
• "O céu é azul" → proposição (V ou F)
• "Que horas são?" → NÃO é proposição
• "Feche a porta" → NÃO é proposição

**Conectivos lógicos:**
• **Negação (¬p):** inverte o valor de verdade
  ¬V = F, ¬F = V

• **Conjunção (p ∧ q) — "e":** só é V quando ambas são V
  V ∧ V = V | V ∧ F = F | F ∧ V = F | F ∧ F = F

• **Disjunção (p ∨ q) — "ou":** só é F quando ambas são F
  V ∨ V = V | V ∨ F = V | F ∨ V = V | F ∨ F = F

• **Condicional (p → q) — "se...então":** só é F quando V → F
  V → V = V | V → F = F | F → V = V | F → F = V

• **Bicondicional (p ↔ q) — "se e somente se":** V quando ambas iguais
  V ↔ V = V | V ↔ F = F | F ↔ V = F | F ↔ F = V

**Tautologia:** proposição sempre verdadeira (p ∨ ¬p)
**Contradição:** proposição sempre falsa (p ∧ ¬p)""",
                'dica': 'A regra do condicional (→) é a mais cobrada: "Se chover, fico em casa" é VERDADEIRO mesmo quando não chove (premissa falsa).'
            },
            {
                'titulo': 'Tabelas-Verdade',
                'conteudo': """**Como montar uma tabela-verdade:**
1. Identifique as proposições simples (p, q, r...)
2. Crie colunas para cada proposição (2^n linhas)
3. Calcule o valor de verdade para cada combinação

**Exemplo: (p ∧ q) → p**
| p | q | p ∧ q | (p ∧ q) → p |
|---|---|-------|-------------|
| V | V |   V   |      V      |
| V | F |   F   |      V      |
| F | V |   F   |      V      |
| F | F |   F   |      V      |
→ Tautologia (sempre V)

**Equivalências importantes:**
• p → q ≡ ¬p ∨ q (condicional como disjunção)
• ¬(p ∧ q) ≡ ¬p ∨ ¬q (Lei de De Morgan)
• ¬(p ∨ q) ≡ ¬p ∧ ¬q (Lei de De Morgan)
• p → q ≡ ¬q → ¬p (contrapositiva)""",
                'dica': 'Pratique montar tabelas-verdade rapidamente. Cebraspe cobra 2-3 questões disso por prova.'
            },
            {
                'titulo': 'Argumentação Lógica',
                'conteudo': """**Estrutura de um argumento:**
• **Premissas:** informações dadas como verdadeiras
• **Conclusão:** o que se deduz das premissas
• **Validade:** a conclusão decorre das premissas (não depende do conteúdo)

**Modus Ponens:**
Premissa 1: Se chove, a rua molha (p → q)
Premissa 2: Choveu (p)
Conclusão: A rua molhou (q) ✓

**Modus Tollens:**
Premissa 1: Se chove, a rua molha (p → q)
Premissa 2: A rua não molhou (¬q)
Conclusão: Não choveu (¬p) ✓

**Falácia da afirmação do consequente:**
Premissa 1: Se chove, a rua molha (p → q)
Premissa 2: A rua molhou (q)
Conclusão: Choveu (p) ✗ (Pode ter sido um cano estourado!)

**Falácia da negação do antecedente:**
Premissa 1: Se chove, a rua molha (p → q)
Premissa 2: Não choveu (¬p)
Conclusão: A rua não molhou (¬q) ✗ (Pode ter molhado por outro motivo!)""",
                'dica': 'Cebraspe adora cobrar falácias lógicas. Memorize: afirmar consequente e negar antecedente são SEMPRE inválidos.'
            },
            {
                'titulo': 'Sequências e Padrões',
                'conteudo': """**Tipos de progressão:**

**PA (Progressão Aritmética):**
• Razão constante entre termos consecutivos
• aₙ = a₁ + (n-1)·r
• Soma: S = n·(a₁ + aₙ)/2
• Exemplo: 2, 5, 8, 11, 14... (r = 3)

**PG (Progressão Geométrica):**
• Razão constante de multiplicação
• aₙ = a₁ · r^(n-1)
• Soma: S = a₁ · (r^n - 1)/(r - 1)
• Exemplo: 2, 6, 18, 54... (r = 3)

**Sequências especiais:**
• Fibonacci: 1, 1, 2, 3, 5, 8, 13... (soma dos 2 anteriores)
• Quadrados: 1, 4, 9, 16, 25... (n²)
• Cubos: 1, 8, 27, 64... (n³)
• Primos: 2, 3, 5, 7, 11, 13...
• Triangulares: 1, 3, 6, 10, 15...

**Dica para identificar:**
1. Calcule as diferenças entre termos consecutivos
2. Se as diferenças forem iguais → PA
3. Se as razões forem iguais → PG
4. Se as diferenças das diferenças forem iguais → PA do 2º grau""",
                'dica': 'Se a sequência não é PA nem PG, tente: diferenças das diferenças, alternância de sinais, ou padrões agrupados.'
            },
            {
                'titulo': 'Problemas de Lógica',
                'conteudo': """**Diagramas lógicos:**
Use tabelas ou diagramas para organizar informações.

**Tipo 1 — Agrupamento:**
"A, B, C, D e E estão em uma fila. A está antes de B. C está depois de D. B está ao lado de D."
→ Monte o diagrama passo a passo.

**Tipo 2 — Verdadeiro/Falso:**
"João diz que Maria mente. Maria diz que Pedro é honesto. Pedro diz que João fala a verdade."
→ Teste cada combinação até encontrar consistência.

**Tipo 3 — Eliminação:**
"Dos 5 suspeitos, apenas um é culpado. As pistas eliminam 3 deles."
→ Monte tabela com eliminações.

**Princípios:**
1. Organize todas as informações em tabela
2. Use ✔ (verdadeiro) e ✗ (falso)
3. Comece pelas informações mais restritivas
4. Use eliminação quando não houver certeza direta""",
                'dica': 'Em questões de fila, desenhe posições: 1ª _ 2ª _ 3ª _ 4ª _ 5ª. Vá preenchendo conforme as pistas.'
            },
            {
                'titulo': 'Probabilidade e Combinação',
                'conteudo': """**Probabilidade básica:**
P(evento) = casos favoráveis / casos possíveis
• Exemplo: jogar um dado e tirar 3 → P = 1/6

**Probabilidade do complementar:**
P(A não ocorrer) = 1 - P(A ocorrer)
• Exemplo: não tirar 3 no dado → P = 1 - 1/6 = 5/6

**Princípio multiplicativo:** "E" → MULTIPLICA
• Jogar dado E tirar cara → (1/6) × (1/2) = 1/12

**Princípio aditivo:** "OU" → SOMA (se eventos excludentes)
• Tirar 3 OU 5 no dado → 1/6 + 1/6 = 2/6 = 1/3

**Fatorial:**
n! = n × (n-1) × ... × 2 × 1
5! = 120, 0! = 1

**Arranjo (importa a ordem):**
A(n,p) = n! / (n-p)!
Ex: 5 pessoas em 3 cadeiras = A(5,3) = 60

**Combinação (não importa a ordem):**
C(n,p) = n! / [p! × (n-p)!]
Ex: Escolher 3 de 5 = C(5,3) = 10""",
                'dica': 'Pergunte: "A ordem importa?" Se sim → arranjo. Se não → combinação. Se é "E" → multiplica. Se é "OU" → soma.'
            },
        ],
        'exercicios': [
            {
                'enunciado': 'Se "p → q" é falso, qual é o valor de verdade de "¬p ∨ q"?',
                'alternativas': [
                    'A) Verdadeiro',
                    'B) Falso',
                    'C) Depende de p',
                    'D) Depende de q',
                ],
                'resposta': 'B',
                'comentario': 'p → q ≡ ¬p ∨ q. Se p → q é falso, então ¬p ∨ q também é falso.'
            },
            {
                'enunciado': 'Em uma PA de razão 5, o primeiro termo é 3. Qual é o 10º termo?',
                'alternativas': [
                    'A) 48',
                    'B) 50',
                    'C) 53',
                    'D) 45',
                ],
                'resposta': 'A',
                'comentario': 'a₁₀ = a₁ + (10-1)·5 = 3 + 45 = 48.'
            },
        ],
    },

    # =====================================================
    # 3. DIREITO CONSTITUCIONAL (~12% da prova)
    # =====================================================
    {
        'nome': 'Direito Constitucional',
        'chave': 'constitucional',
        'peso': '12%',
        'descricao': 'Constituição Federal de 1988, direitos fundamentais, organização do Estado.',
        'topicos': [
            {
                'titulo': 'Princípios Fundamentais (Art. 1-4, CF/88)',
                'conteudo': """**Art. 1° — Fundamentos da República:**
I — Soberania
II — Cidadania
III — Dignidade da pessoa humana
IV — Valores sociais do trabalho e da livre iniciativa
V — Pluralismo político

**Art. 2° — Poderes:**
Legislativo, Executivo e Judiciário — independentes e harmônicos entre si.

**Art. 3° — Objetivos da República:**
I — Construir uma sociedade livre, justa e solidária
II — Garantir o desenvolvimento nacional
III — Erradicar a pobreza e a marginalização
IV — Promover o bem de todos, sem preconceitos

**Art. 4° — Princípios das Relações Internacionais:**
• Independência nacional
• Prevalência dos direitos humanos
• Autodeterminação dos povos
• Não intervenção
• Igualdade entre os Estados
• Defesa da paz
• Solução pacífica dos conflitos
• Repúdio ao terrorismo e ao racismo
• Cooperação entre os povos
• Concessão de asilo político""",
                'dica': 'Memorize os 5 fundamentos (Art. 1°) e os 4 objetivos (Art. 3°) — caem em toda prova de Direito Constitucional.'
            },
            {
                'titulo': 'Direitos e Garantias Fundamentais (Art. 5°)',
                'conteudo': """**Princípio da igualdade (Art. 5°, caput):**
• Igualdade formal: todos são iguais perante a lei
• Igualdade material: tratamento desigual aos desiguais

**Direitos individuais mais cobrados:**
• I — Igualdade perante a lei (sem distinção de qualquer natureza)
• II — Direito à vida, liberdade, igualdade, segurança e propriedade
• IV — Liberdade de pensamento (livre manifestação)
• V — Direito de resposta e indenização
• VI — Liberdade de consciência e crença
• VIII — Vedação de tortura e tratamento desumano
• IX — Liberdade de expressão (atividade intelectual, artística, científica)
• X — Inviolabilidade da intimidade, vida privada, honra e imagem
• XLII — Racismo é crime inafiançável e imprescritível
• XLIV — Ação de grupos armados é crime inafiançável

**Cláusulas pétreas (Art. 60, §4°):**
• Forma federativa de Estado
• Voto direto, secreto, universal e periódico
• Separação dos Poderes
• Direitos e garantias individuais""",
                'dica': 'O Art. 5° tem 78 incisos. Foque nos mais cobrados: I, II, IV, V, VI, IX, X, XLII, XLIV.'
            },
            {
                'titulo': 'Direitos Sociais (Art. 6° a 11)',
                'conteudo': """**Art. 6° — Direitos Sociais:**
Educação, saúde, alimentação, trabalho, moradia, transporte, lazer, segurança, previdência social, proteção à maternidade e à infância, assistência aos desamparados.

**Obs: Moradia foi incluída pela EC 26/2000 e Alimentação pela EC 64/2010.**

**Direitos dos trabalhadores urbanos e rurais (Art. 7°):**
• Salário mínimo (vedada vinculação)
• Irredutibilidade salarial
• 13° salário
• Repouso semanal remunerado
• Férias anuais remuneradas (+ 1/3)
• Licença-maternidade (120 dias)
• Licença-paternidade (5 dias)
• Aviso prévio proporcional
• FGTS
• Seguro-desemprego
• Hora extra com adicional mínimo de 50%

**Direitos da criança e do adolescente (Art. 227):**
• Prioridade absoluta
• Direito à vida, saúde, educação, lazer
• Proteção contra exploração e violência""",
                'dica': 'O Art. 7° tem 34 incisos. Foque nos que envolvem números: 13°, 120 dias, 5 dias, 50%.'
            },
            {
                'titulo': 'Organização do Estado (Art. 18-32)',
                'conteudo': """**Forma de Estado:** República Federativa
• União (art. 20 e 21)
• Estados (art. 25 a 28)
• Municípios (art. 29 a 31)
• DF (art. 32)

**Competências da União (Art. 22):**
• Exclusiva: legislar sobre direito civil, penal, processual, eleitoral, trabalhista, etc.
• Privativa: legislar sobre normas gerais (concorrente)

**Competências concorrentes (Art. 24):**
• União: normas gerais
• Estados: normas suplementares
• DF: competências legislativas dos Estados e Municípios

**Competências dos Municípios (Art. 30):**
• Legislar sobre assuntos de interesse local
• Suplementar legislação federal/estadual
• Organizar e prestar serviços públicos
• Promover o adequado ordenamento territorial

**Entes descentralizados:**
• Autarquias (ex: INSS)
• Fundações públicas
• Sociedades de economia mista
• Empresas públicas""",
                'dica': 'INSS é autarquia federal. Entenda a diferença entre autarquia (patrimônio próprio, personalidade jurídica) e órgão (sem personalidade).'
            },
            {
                'titulo': 'Poder Legislativo (Art. 44-75)',
                'conteudo': """**Estrutura: Congresso Nacional = Senado + Câmara dos Deputados**

**Senado Federal (Art. 46):**
• 81 senadores (3 por Estado + DF)
• Mandato de 8 anos
• Renovação: 1/3 e 2/3 a cada 4 anos

**Câmara dos Deputados (Art. 45):**
• Proporcional à população (mín. 8, máx. 70 por Estado + DF)
• Mandato de 4 anos

**Competências exclusivas do Senado:**
• Processar e julgar o Presidente (infrações penais)
• Aprovar escolha de Ministros do STF, PGR, etc.
• Autorizar operações externas

**Competências exclusivas da Câmara:**
• Autorizar instauração de processo contra Presidente
• Elaborar regimento interno
• Fixar subsídios de autoridades

**Processo Legislativo (Art. 59-69):**
• Emendas constitucionais (3/5 dos votos + 2 turnos em cada casa)
• Leis complementares (maioria absoluta)
• Leis ordinárias (maoria simples)
• Medidas provisórias (vigência 60 dias, prorrogável)""",
                'dica': 'Diferença crucial: emenda constitucional (2/3) vs. lei complementar (maioria absoluta) vs. lei ordinária (maioria simples).'
            },
            {
                'titulo': 'Poder Judiciário (Art. 92-126)',
                'conteudo': """**Órgãos do Judiciário:**
• STF — Supremo Tribunal Federal (11 ministros)
• STJ — Superior Tribunal de Justiça (33 ministros)
• TRFs — Tribunais Regionais Federais
• TST, TSE, STM
• Tribunais de Justiça (Estados)
• Juízes de primeiro grau

**STF (Art. 102) — Guardião da Constituição:**
• Ação Direta de Inconstitucionalidade (ADI)
• Ação Declaratória de Constitucionalidade (ADC)
• Arguição de Descumprimento de Preceito Fundamental (ADPF)
• Recurso Extraordinário (RE)

**STJ (Art. 105) — Uniformização da lei federal:**
• Recurso Especial (REsp)
• Conflitos de competência
• Habeas corpus em casos específicos

**Princípios do Judiciário (Art. 93, Lei Orgânica):**
• Vitaliciedade (após 2 anos de estágio)
• Inamovibilidade
• Irredutibilidade de subsídio""",
                'dica': 'STF = Constituição (controle de constitucionalidade). STJ = lei federal (interpretação uniforme). Nunca troque um pelo outro.'
            },
        ],
        'exercicios': [
            {
                'enunciado': 'Sobre os fundamentos da República Federativa do Brasil, é CORRETO afirmar que NÃO é fundamento:',
                'alternativas': [
                    'A) A soberania.',
                    'B) A cidadania.',
                    'C) A separação dos Poderes.',
                    'D) A dignidade da pessoa humana.',
                ],
                'resposta': 'C',
                'comentario': 'Separação dos Poderes (Art. 2°) é princípio estruturante, NÃO fundamento (Art. 1°). Fundamentos: soberania, cidadania, dignidade, valores sociais do trabalho, pluralismo político.'
            },
        ],
    },

    # =====================================================
    # 4. DIREITO ADMINISTRATIVO (~12% da prova)
    # =====================================================
    {
        'nome': 'Direito Administrativo',
        'chave': 'administrativo',
        'peso': '12%',
        'descricao': 'Lei 8.112/90 (Regime Jurídico dos Servidores), atos administrativos, processos administrativos.',
        'topicos': [
            {
                'titulo': 'Princípios da Administração Pública',
                'conteudo': """**Art. 37, caput, CF/88 — LIMPE:**
• **Legalidade:** a administração só pode fazer o que a lei permite
• **Impessoalidade:** igualdade de tratamento, vedação ao nepotismo
• **Moralidade:** ética e probidade administrativa
• **Publicidade:** transparência dos atos (salvo sigilo)
• **Eficiência:** qualidade e presteza no serviço público

**Princípios adicionais (L. 9.784/99):**
• Ampla defesa e contraditório
• Motivação
• Proporcionalidade
• Razoabilidade
• Segurança jurídica
• Interesse público

**Legalidade vs. Legitimidade:**
• Legalidade: conformidade com a lei
• Legitimidade: conformidade com a moral e o interesse público
• Um ato pode ser legal mas ilegítimo""",
                'dica': 'LIMPE é a sigla mais cobrada em Direito Administrativo. Memorize: Legalidade, Impessoalidade, Moralidade, Publicidade, Eficiência.'
            },
            {
                'titulo': 'Atos Administrativos',
                'conteudo': """**Atributos dos atos administrativos:**
• **Presunção de legitimidade:** presume-se válido até prova em contrário
• **Imperatividade:** impõe obrigações mesmo sem consentimento
• **Autoexecutoriedade:** administração pode executar sem autorização judicial
• **Tipicidade:** deve corresponder a tipo previsto em lei

**Requisitos de validade:**
• Competência (agente competente)
• Finalidade (interesse público)
• Forma (escrita, geralmente)
• Motivo (causa do ato)
• Objeto (conteúdo lícito e possível)

**Vícios dos atos administrativos:**
• **Nulo:** vício grave → anulação (retroativa)
• **Anulável:** vício leve → pode ser convalidado
• **Inexistente:** não produz efeitos

**Classificação:**
• Quanto ao conteúdo: simples, complexo, composto
• Quanto aos destinatários: geral, individual
• Quanto à discricionariedade: vinculado, discricionário""",
                'dica': 'Ato discricionário = administração tem liberdade de escolha. Ato vinculado = a lei determina exatamente o que fazer.'
            },
            {
                'titulo': 'Regime Jurídico dos Servidores — Lei 8.112/90',
                'conteudo': """**Provimento do cargo público:**
• Nomeação (concurso público)
• Promoção (merecimento ou antiguidade)
• Readaptação (inaptidão para funções)
• Reversão (aposentado volta ao cargo)
• Aproveitamento (servidor em disponibilidade)
• Reintegração (anulação de demissão)
• Recondução (retorno de estágio probatório)

**Estágio probatório (Art. 20):**
• Duração: 3 anos
• Avaliação: desempenho, assiduidade, disciplina, iniciativa
• Pode ser dispensado por insuficiência (com ampla defesa)

**Direitos dos servidores:**
• Remuneração / subsídio
• Férias (30 dias)
• Licença-maternidade (120 dias)
• Licença-paternidade (5 dias)
• Licença para tratamento de saúde
• Licença para atividade política
• Aposentadoria

**Deveres:**
• Assiduidade e pontualidade
• Obediência ao superior
• Sigilo profissional
• Zelo pelo patrimônio público""",
                'dica': 'Cebraspe cobra muito as diferenças entre provimento, reintegração, recondução e reversão. Memorize cada um.'
            },
            {
                'titulo': 'Processo Administrativo Federal — Lei 9.784/99',
                'conteudo': """**Princípios do processo (Art. 2°):**
• Igualdade entre as partes
• Defesa do interesse público
• Objetividade e imparcialidade
• Ampla defesa e contraditório

**Requisitos da petição inicial:**
• Autoridade dirigida
• Identificação do interessado
• Objeto do pedido
• Fundamentos
• Provas

**Prazos relevantes:**
• Interposição de recurso: 10 dias (Art. 59)
• Manifestação do interessado: 10 dias, salvo prazo especifico (Art. 44)
• Decisão após concluída a instrução: 30 dias, prorrogáveis por igual período com motivação (Art. 49)

**Decisão administrativa (Art. 48):**
• Deve ser fundamentada
• Indicar recursos cabíveis
• Prazo geral para decisão: 30 dias, prorrogável por igual período com motivação (Art. 49)

**Recursos:**
• Hierárquico (para autoridade superior)
• De ofício (pela própria administração)
• Efeito: devolutivo (sempre) + suspensivo (quando previsto)

**Revisão administrativa:**
• Pela própria administração
• De ofício ou por provocação
• Sem prazo decadencial""",
                'dica': 'O recurso administrativo tem prazo geral de 10 dias; a decisão tem prazo geral de 30 dias após a instrução, prorrogável uma vez com motivação.'
            },
            {
                'titulo': 'Improbidade Administrativa — Lei 8.429/92',
                'conteudo': """**A Lei no 8.429/1992 exige leitura conforme a redacao vigente e o elemento subjetivo do dolo.**

**1. Enriquecimento ilicito (Art. 9°):**
• Auferir vantagem patrimonial indevida em razao do cargo
• A conduta deve ser dolosa
• As sancoes devem ser conferidas no Art. 12, I, conforme a edicao vigente

**2. Prejuizo ao erario (Art. 10°):**
• Causar dano efetivo ao patrimonio publico por conduta dolosa
• Nao basta mera irregularidade ou presuncao de dano
• As sancoes devem ser conferidas no Art. 12, II, conforme a edicao vigente

**3. Atentado aos principios (Art. 11°):**
• Praticar dolosamente uma das condutas tipificadas no artigo
• A lista legal e taxativa; nao basta afirmar genericamente que houve falta etica
• As sancoes devem ser conferidas no Art. 12, III, conforme a edicao vigente

**Sancoes e legitimidade:**
• Variam conforme o inciso do Art. 12 e nao podem ser resumidas em uma lista unica
• A acao de improbidade deve seguir o Art. 17 e a interpretacao constitucional vigente
• Nao atribuir legitimidade a qualquer cidadao sem base legal especifica

**Legitimidade ativa:**
• Conferir o Art. 17 e os entendimentos vinculantes do STF na data de corte
• Nao confundir representacao por qualquer pessoa com legitimidade para propor a acao""",
                'dica': 'Diferencie: Art. 9 = vantagem patrimonial indevida; Art. 10 = dano efetivo ao erario; Art. 11 = conduta dolosa tipificada contra principios.'
            },
        ],
        'exercicios': [
            {
                'enunciado': 'Qual dos seguintes NÃO é princípio da Administração Pública previsto no art. 37 da CF/88?',
                'alternativas': [
                    'A) Legalidade.',
                    'B) Moralidade.',
                    'C) Proporcionalidade.',
                    'D) Publicidade.',
                ],
                'resposta': 'C',
                'comentario': 'Proporcionalidade não está no art. 37 (LIMPE). Está na Lei 9.784/99 como princípio do processo administrativo.'
            },
        ],
    },

    # =====================================================
    # 5. DIREITO PREVIDENCIÁRIO (~25% da prova) — O MAIS IMPORTANTE
    # =====================================================
    {
        'nome': 'Direito Previdenciário',
        'chave': 'previdenciario',
        'peso': '25%',
        'descricao': 'Legislação do RGPS — Lei 8.213/91, Decreto 3.048/99, EC 103/2019. A disciplina de maior peso no INSS.',
        'topicos': [
            {
                'titulo': 'Seguridade Social — Conceito e Estrutura',
                'conteudo': """**Art. 194, CF/88 — Seguridade Social:**
Conjunto integrado de ações de iniciativa dos Poderes Públicos e da sociedade destinadas a assegurar:
• Saúde
• Previdência Social
• Assistência Social

**Financiamento (Art. 195, CF):**
• Empresas: folha de salários, faturamento, lucro
• Trabalhadores: salários
• Receita de concursos de prognósticos
• Orçamento da União

**Princípios (Lei 8.212/91, Art. 2°):**
• Universalidade da cobertura
• Uniformidade e equivalência dos benefícios
• Seletividade e distributividade
• Irredutibilidade do valor dos benefícios
• Equidade no custeio
• Diversidade da base de financiamento
• Caráter democrático

**Orgãos:**
• MPS — Ministério da Previdência Social
• INSS — Instituto Nacional do Seguro Social (executor)
• CNPS — Conselho Nacional de Previdência Social
• DATAPREV — Empresa de Tecnologia""",
                'dica': 'INSS é autarquia federal vinculada ao MPS. Entenda a diferença: MPS formula política, INSS executa.'
            },
            {
                'titulo': 'Plano de Custeio — Lei 8.212/91',
                'conteudo': """**Contribuição do empregador (Art. 22):**
• 20% sobre folha de salários
• 20% sobre remuneração de diretores

**Contribuição do trabalhador (Art. 28):**
• Tabela progressiva (alíquota variável conforme faixa salarial)
• 7,5% a 14% (após Reforma — EC 103/2019)

**Contribuição do segurado facultativo:**
• 20% sobre salário mínimo (plano normal)
• 11% sobre salário mínimo (plano simplificado)
• 5% sobre salário mínimo para facultativo de baixa renda, observados os requisitos legais; isso não é contribuição para o BPC/LOAS

**Terceiros (Art. 3°):**
• Cooperativas, condomínios, templos, partidos, sindicatos
• 20% sobre folha

**SAT — Seguro de Acidente de Trabalho:**
• 1%, 2% ou 3% conforme atividade
• FAP (Fator Acidentário de Previdência): multiplicador

**Recolhimento:**
• Empresas: até o dia 20 do mês seguinte
• Contribuintes individuais: até o último dia do mês seguinte""",
                'dica': 'A tabela progressiva de contribuição do trabalhador (7,5% a 14%) é muito cobrada. Memorize as faixas.'
            },
            {
                'titulo': 'Qualidade de Segurado e Carência',
                'conteudo': """**Segurados obrigatórios (Lei 8.213/91, Art. 11):**
• Empregado (CLT, doméstico, temporário)
• Empregado doméstico
• Trabalhador avulso
• Contribuinte individual (autônomo, prestador)
• Segurado especial (rural)

**Segurados facultativos (Art. 13):**
• Dona de casa
• Estudante
• Desempregado
• Presidiário não remunerado
• Bolsista (pesquisa, formação)

**Qualidade de segurado:**
• Adquire com a primeira contribuição
• Mantém durante 12 meses após última contribuição (período de graça)
• Pode haver extensão de 12 meses por desemprego comprovado
• Pode haver outra extensão de 12 meses quando preenchido o requisito legal de contribuições sem perda da qualidade
• O segurado detido ou recluso possui hipótese própria no Art. 15, IV
• A perda ocorre após o fim do período de graça, observadas as regras legais

**Carência (Art. 24):**
• Número mínimo de contribuições mensais
• Aposentadoria por idade: 180 meses (15 anos)
• Aposentadoria por tempo: 180 meses (15 anos) — antes da Reforma
• Auxílio-doença: 12 contribuições
• Aposentadoria por invalidez: 12 contribuições
• Salário-maternidade: sem carência para empregadas""",
                'dica': 'O periodo de graca exige identificar a categoria do segurado e as extensoes condicionais do Art. 15; nao memorize uma formula fixa.'
            },
            {
                'titulo': 'Benefícios Previdenciários — Visão Geral',
                'conteudo': """**Benefícios previdenciários (Art. 18, Lei 8.213):**

**Aposentadorias:**
1. Por idade (urbana/rural)
2. Por tempo de contribuição (extinta pela Reforma — regra de transição)
3. Por invalidez
4. Especial

**Outros benefícios:**
5. Auxílio-doença → Auxílio por incapacidade temporária (Reforma)
6. Salário-maternidade
7. Salário-família
8. Auxílio-reclusão
9. Pensão por morte

**Benefícios assistenciais (não previdenciários):**
• LOAS/BPC: benefício de 1 salário mínimo para idosos (65+) e deficientes

**Renda mensal:**
• 1 salário mínimo (benefício mínimo)
• Até o teto do RGPS (R$ 7.786,02 em 2024)
• Atualização: INPC

**Cálculo do salário de benefício (após Reforma):**
• Média de TODAS as contribuições (desde julho/1994)
• Antes: 80% maiores contribuições (descartava 20% menores)
• Após Reforma: 60% + 2% por ano que exceder 20 anos de contribuição (homem) ou 15 anos (mulher)""",
                'dica': 'A fórmula 60% + 2% é crucial. Para homem com 30 anos: 60% + 2%(10) = 80%. Para mulher com 25 anos: 60% + 2%(10) = 80%.'
            },
            {
                'titulo': 'Aposentadoria por Idade',
                'conteudo': """**Regra permanente (após Reforma — EC 103/2019):**

**Urbana:**
• Homem: 65 anos + 20 anos de contribuição
• Mulher: 62 anos + 15 anos de contribuição

**Rural (segurado especial):**
• Homem: 60 anos + 15 anos de atividade rural
• Mulher: 55 anos + 15 anos de atividade rural

**Regra de transição — Idade Progressiva:**
• Homem: 65 anos + 15 anos de contribuição (já completava 15 em 19/11/2019)
• Mulher: 62 anos + 15 anos de contribuição (já completava 15 em 19/11/2019)
• +6 meses por ano a partir de 2020 até atingir 20 anos (homem) e 15 anos (mulher)

**Cálculo (Regra Permanente):**
• Média de todas as contribuições
• 60% + 2% por ano que exceder:
  - Homem: 20 anos de contribuição
  - Mulher: 15 anos de contribuição

**Exemplo (homem, 30 anos contribuição):**
60% + 2% × (30-20) = 60% + 20% = 80% da média""",
                'dica': 'Aposentadoria rural: idade inferior (60/55) mas mesmo tempo de contribuição (15 anos). Muito cobrada no INSS.'
            },
            {
                'titulo': 'Aposentadoria por Tempo de Contribuição — Regras de Transição',
                'conteudo': """**Aposentadoria por tempo de contribuição foi EXTINTA pela Reforma (EC 103/2019).**

**Regras de transição:**

**1. Pedágio de 50% (Art. 17):**
• Quem faltava até 2 anos em 13/11/2019
• Tempo restante + 50% do tempo faltante
• Idade mínima: não exigida

**2. Pedágio de 100% (Art. 18):**
• Idade mínima: 57 (M) / 60 (H)
• Tempo mínimo: 30 (M) / 35 (H)
• Paga pedágio de 100% do tempo faltante em 13/11/2019
• Cálculo: média de todas as contribuições (sem descartar)

**3. Pontos (Art. 15):**
• Idade + tempo de contribuição = pontos
• Homem: 96 pontos + 35 anos contribuição
• Mulher: 86 pontos + 30 anos contribuição
• +1 ponto por ano até atingir 105 (H) / 100 (M)

**4. Idade mínima progressiva (Art. 16):**
• 56 anos (M) / 61 anos (H) em 2019
• +6 meses por ano até atingir 62 (M) / 65 (H)
• Tempo: 30 (M) / 35 (H)""",
                'dica': 'Regra de pontos: some idade + tempo. Se homem com 60 anos e 36 de contribuição = 96 pontos. Precisa de 96 (2019). ✅'
            },
            {
                'titulo': 'Aposentadoria por Invalidez',
                'conteudo': """**Requisitos (Art. 42):**
• Incapacidade total e permanente para o trabalho
• Sem possibilidade de reabilitação
• Carência: 12 contribuições (salvo acidente/doença grave)
• Qualidade de segurado

**Conversão:**
• Pode converter para aposentadoria por idade (se atingir idade)

**Não pode recolher:**
• Não pode exercer atividade remunerada
• Se voltar a trabalhar → benefício cessa

**Perícia médica:**
• Obrigatória para concessão
• Periodicidade: a cada 2 anos (pode ser dispensada >60 anos)

**Revisão:**
• Se houver recuperação → cessação ou redução
• Recuperação parcial → redução do benefício
• Recuperação total → cessação imediata

**Renda mensal:**
• 60% da média + 2% por ano que exceder 20 anos (H) / 15 anos (M)
• Mínimo: 1 salário mínimo""",
                'dica': 'Aposentadoria por invalidez exige incapacidade TOTAL e PERMANENTE. Se for temporária → auxílio-doença.'
            },
            {
                'titulo': 'Aposentadoria Especial',
                'conteudo': """**Requisitos (Art. 57):**
• Exposição a agentes nocivos (físicos, químicos, biológicos)
• Tempo: 15, 20 ou 25 anos conforme o agente
• Carência: 180 contribuições

**Agentes e tempos:**
• 15 anos: mineração subterrânea
• 20 anos: amianto/asbesto
• 25 anos: ruído, calor, frio, pressão, químicos, biológicos

**Após Reforma (EC 103/2019):**
• Idade mínima obrigatória:
  - 15 anos: 55 anos de idade
  - 20 anos: 58 anos de idade
  - 25 anos: 60 anos de idade

**Comprovação:**
• PPP (Perfil Profissiográfico Previdenciário)
• LTCAT (Laudo Técnico das Condições do Ambiente de Trabalho)
• DIRBEN 8030 / SB-40 (formulários antigos)

**Renda mensal:**
• Integralidade (sem redutor)
• Média de todas as contribuições""",
                'dica': 'PPP é o documento-chave. Sem ele, não comprova a especialidade. Exija do empregador.'
            },
            {
                'titulo': 'Auxílio-doença (Auxílio por Incapacidade Temporária)',
                'conteudo': """**Requisitos (Art. 59):**
• Incapacidade para o trabalho (temporária)
• Carência: 12 contribuições
• Qualidade de segurado

**Início do benefício:**
• Dia do afastamento (empregado)
• 1° dia do mês seguinte (demais)

**Perícia médica:**
• Obrigatória para concessão
• Pode ser agendada pelo Meu INSS

**Cessação:**
• Recuperação da capacidade
• Retorno voluntário ao trabalho
• Aposentadoria por invalidez
• Morte

**Renda mensal:**
• 91% do salário de benefício
• Sem o redutor de 60%/2%

**B91 — Auxílio-doença comum vs. B92 — Acidente de trabalho:**
• B91: doença comum (12 meses carência)
• B92: acidente/doença ocupacional (sem carência)""",
                'dica': 'Auxílio-doença = 91% do SB. Aposentadoria por invalidez = 60%+2%. O auxílio pode ser MAIOR que a aposentadoria por invalidez!'
            },
            {
                'titulo': 'Pensão por Morte',
                'conteudo': """**Requisitos (Art. 74):**
• Morte do segurado
• Qualidade de segurado do falecido
• Carência: não exigida

**Dependentes (Art. 16):**
• Classe I: cônjuge/companheiro + filhos < 21 anos ou inválidos
• Classe II: pais
• Classe III: irmãos < 21 anos ou inválidos
• Exclusão: classe anterior exclui a posterior

**Após Reforma (EC 103/2019):**
• Cônjuge/companheiro: cota de 50% + 10% por dependente
• Limite: 100% do salário de benefício
• Duração: vitalícia se > 44 anos ou invalidez; caso contrário, temporária
• Temporária: 4 meses (até 21 anos) ou 3-5 anos (cônjuge)

**Renda mensal (nova regra):**
• 50% do SB + 10% por dependente (máx. 100%)
• Exemplo: 2 dependentes → 50% + 20% = 70%

**Cota individual:**
• Cada dependente recebe cota individual
• Órfão: cota individual = SB × cota / número de dependentes""",
                'dica': 'Antes da Reforma: 100% para 1 dependente. Depois: 50% + 10% por dependente. A regra mudou drasticamente.'
            },
            {
                'titulo': 'Salário-maternidade e Salário-família',
                'conteudo': """**Salário-maternidade (Art. 71-73):**
• Parto: 120 dias
• Aborto espontâneo: 14 dias
• Adoção: 120 dias
• Empregada: empregador paga (recolhe depois)
• Demais: INSS paga diretamente

**Carência:**
• Empregada, doméstica, avulsa: SEM carência
• Contribuinte individual e facultativa: 10 contribuições

**Renda mensal:**
• 1 salário de benefício (integral)
• Sem redutor

**Salário-família (Art. 65-70):**
• Apenas para empregado (CLT) e trabalhador avulso
• Renda ≤ teto (atualizar anualmente)
• Valor por filho < 14 anos ou inválido (qualquer idade)
• Não é pago pelo INSS — é pago pelo empregador

**Conversão em aposentadoria:**
• Salário-maternidade NÃO se converte em aposentadoria""",
                'dica': 'Salário-maternidade: 120 dias, sem carência para empregadas, valor integral. É um dos benefícios mais "generosos" do RGPS.'
            },
            {
                'titulo': 'Reforma da Previdência — EC 103/2019',
                'conteudo': """**Principais mudanças:**

**1. Idade mínima:**
• Homem: 65 anos (era sem idade mínima)
• Mulher: 62 anos (era sem idade mínima)

**2. Tempo mínimo de contribuição:**
• Homem: 20 anos (era 35)
• Mulher: 15 anos (era 30)

**3. Fórmula de cálculo:**
• Antes: 80% maiores contribuições → 100% do SB
• Depois: média de todas → 60% + 2% por ano acima de 20 (H) / 15 (M)

**4. Aposentadoria por tempo extinta:**
• Regras de transição (pedágio, pontos, idade progressiva)

**5. Professor:**
• Antes: 30 (M) / 25 (H) anos de magistério
• Depois: 57 (M) / 60 (H) anos + 25 anos de magistério + 100 pontos (M) / 92 pontos (H)

**6. Policial:**
• Antes: 30 anos de atividade policial
• Depois: 55 anos + 25 anos de atividade + 75 pontos

**7. Pensão por morte:**
• 50% + 10% por dependente (era 100%)

**8. Benefício de prestação continuada (BPC/LOAS):**
• Inalterado: 1 salário mínimo para idosos 65+ e deficientes""",
                'dica': 'A Reforma é a mudança mais importante. Foque nas mudanças de cálculo (60%+2%) e idade mínima (65/62).'
            },
        ],
        'exercicios': [
            {
                'enunciado': 'Considerando a regra geral do segurado que deixou de exercer atividade remunerada, sem outra extensão já demonstrada, é CORRETO afirmar que:',
                'alternativas': [
                    'A) 6 meses após a última contribuição, independentemente da situação.',
                    'B) Mantém a qualidade por 12 meses após a última contribuição, podendo haver extensão por mais 12 se comprovar desemprego involuntário.',
                    'C) 24 meses após a última contribuição, sem possibilidade de extensão.',
                    'D) 12 meses após a última contribuição, sem possibilidade de extensão.',
                ],
                'resposta': 'B',
                'comentario': 'A regra geral é de 12 meses. A extensão por desemprego depende de comprovação; outras hipóteses e requisitos devem ser conferidos no Art. 15 da Lei 8.213/91.'
            },
            {
                'enunciado': 'Na hipótese de aposentadoria programada do RGPS sujeita à regra geral de cálculo da EC 103/2019, para homem com 30 anos de contribuição, o percentual inicial sobre a média será:',
                'alternativas': [
                    'A) 100% da média de todas as contribuições.',
                    'B) 80% das maiores contribuições.',
                    'C) 60% da média + 2% por ano que exceder 20 anos = 80%.',
                    'D) 70% da média + 2% por ano que exceder 25 anos = 80%.',
                ],
                'resposta': 'C',
                'comentario': 'Na hipótese indicada, 60% + 2% × (30-20) = 80% da média. O cálculo depende do benefício, do histórico de filiação e das regras de transição aplicáveis.'
            },
        ],
    },

    # =====================================================
    # 6. ÉTICA NO SERVIÇO PÚBLICO (~8% da prova)
    # =====================================================
    {
        'nome': 'Ética no Serviço Público',
        'chave': 'etica',
        'peso': '8%',
        'descricao': 'Decreto 1.171/94 (Código de Ética), Lei 8.429/92 (Improbidade), Lei 8.112/90 (infrações).',
        'topicos': [
            {
                'titulo': 'Código de Ética do Servidor — Decreto 1.171/94',
                'conteudo': """**Princípios fundamentais:**
• Dignidade, decoro, zelo e eficiência
• Cortesia no atendimento
• Sigilo sobre informações privilegiadas
• Imparcialidade e isonomia
• Lealdade e boa-fé

**Deveres do servidor (Anexo, Seção II):**
I — Desempenhar com zelo e dedicação as atribuições
II — Observar normas legais e regulamentares
III — Ser assíduo e pontual
IV — Tratar com respeito e educação
V — Manter conduta compatível com a moral pública
VI — Respeitar o sigilo funcional
VII — Representar contra ilegalidade ou abuso de poder

**Vedações (Anexo, Seção III):**
I — Usar cargo para obter vantagens
II — Favorecer pessoas com informações privilegiadas
III — Revelar informações sigilosas
IV — Usar equipamentos para fins particulares
V — Ausentar-se durante o expediente
VI — Valer-se do cargo para obter favores

**Comissao de etica:**
• O Codigo preve a aplicacao da pena de censura etica
• Advertencia, suspensao e demissao pertencem ao regime disciplinar aplicavel e nao devem ser atribuidas automaticamente ao Decreto no 1.171/1994""",
                'dica': 'O Decreto 1.171/94 estabelece o Código de Ética. É diferente da Lei 8.429/92 (Improbidade). Memorize ambos.'
            },
            {
                'titulo': 'Improbidade Administrativa — Lei 8.429/92 (Detalhamento)',
                'conteudo': """**Art. 9° — Enrichhecimento ilícito:**
• Receber, para si ou para outrem, dinheiro, bens ou qualquer vantagem
• Aceitar promessa de vantagem
• Desviar bens, rendas ou verbas públicas
• As sancoes devem ser conferidas no Art. 12, I, conforme a edicao vigente

**Art. 10° — Lesão ao erário:**
• Facilitar ou permitir lesão ao patrimônio público
• Permite ou facilita a ação de terceiros
• A conduta exige dolo, conforme a redacao vigente
• As sancoes devem ser conferidas no Art. 12, II

**Art. 11° — Atentado aos princípios:**
• Praticar ato visando fim proibido ou não vedado por lei
• Praticar ato com excesso de poder
• Deixar de prestar contas quando obrigatório
• As sancoes devem ser conferidas no Art. 12, III, conforme a edicao vigente

**Prescricao:**
• Conferir o Art. 23 na redacao vigente e a jurisprudencia aplicavel

**Legitimidade ativa:**
• MP (obrigatório)
• Poder Público lesado
• Nao atribuir legitimidade a qualquer cidadao sem base legal especifica""",
                'dica': 'Art. 9 = vantagem patrimonial indevida; Art. 10 = dano efetivo ao erario; Art. 11 = conduta dolosa tipificada.'
            },
        ],
        'exercicios': [
            {
                'enunciado': 'Considerando que a vantagem pessoal seja uma vantagem patrimonial indevida obtida em razão do cargo, a conduta pode caracterizar:',
                'alternativas': [
                    'A) Apenas infração disciplinar.',
                    'B) Improbidade administrativa por atentado aos princípios.',
                    'C) Improbidade administrativa por enriquecimento ilícito.',
                    'D) Apenas violação do Código de Ética.',
                ],
                'resposta': 'C',
                'comentario': 'Com vantagem patrimonial indevida e dolo, a hipótese se aproxima do Art. 9° da Lei 8.429/92. A classificação exige análise dos fatos e não decorre automaticamente da expressão vantagem pessoal.'
            },
        ],
    },

    # =====================================================
    # 7. INFORMÁTICA (~8% da prova)
    # =====================================================
    {
        'nome': 'Informática',
        'chave': 'informatica',
        'peso': '8%',
        'descricao': 'Windows, Office 365, internet, redes, segurança da informação.',
        'topicos': [
            {
                'titulo': 'Sistema Operacional Windows',
                'conteudo': """**Conceitos básicos:**
• Sistema operacional: gerencia hardware e software
• Windows 10/11: versões mais cobradas
• Desktop: área de trabalho
• Barra de tarefas: atalhos e notificações

**Gerenciador de Arquivos (Explorador):**
• Hierarquia: Disco > Pastas > Arquivos
• Extensões: .docx, .xlsx, .pdf, .exe, .jpg
• Atalhos: Ctrl+C (copiar), Ctrl+V (colar), Ctrl+X (recortar), Ctrl+Z (desfazer)
• Windows+E: abrir Explorador
• Windows+L: bloquear computador
• Alt+Tab: alternar janelas
• Alt+F4: fechar janela

**Painel de Controle:**
• Programas e Recursos
• Contas de Usuário
• Segurança e Manutenção
• Rede e Internet

**Gerenciador de Tarefas:**
• Ctrl+Shift+Esc: abrir direto
• Ctrl+Alt+Del: opções de segurança
• Monitora processos, desempenho, rede""",
                'dica': 'Cebraspe adora cobrar atalhos de teclado. Memorize pelo menos os 10 mais usados.'
            },
            {
                'titulo': 'Microsoft Word (Office 365)',
                'conteudo': """**Conceitos fundamentais:**
• Processador de textos
• Formatação de caracteres (fonte, tamanho, cor, estilo)
• Formatação de parágrafos (alinhamento, espaçamento, recuo)
• Estilos (Título 1, Título 2, Normal)

**Recursos avançados:**
• Cabeçalho e rodapé
• Numeração de páginas
• Sumário automático
• Caixa de texto
• Tabelas
• Imagens e formas
• WordArt

**Atalhos essenciais:**
• Ctrl+S: salvar
• Ctrl+P: imprimir
• Ctrl+F: localizar
• Ctrl+H: localizar e substituir
• Ctrl+A: selecionar tudo
• Ctrl+B: negrito
• Ctrl+I: itálico
• Ctrl+U: sublinhado
• Ctrl+Enter: quebra de página

**Referências:**
• Notas de rodapé
• Citações e bibliografia
• Índice remissivo
• Legendas de figuras e tabelas""",
                'dica': 'Foco em sumário automático, cabeçalho/rodapé e estilos — são os recursos mais cobrados em provas de Informática.'
            },
            {
                'titulo': 'Microsoft Excel (Office 365)',
                'conteudo': """**Conceitos:**
• Planilha eletrônica
• Célula: interseção de linha e coluna (ex: A1)
• Intervalo: conjunto de células (ex: A1:C5)
• Aba / Planilha / Pasta de trabalho

**Fórmulas e funções:**
• Soma: =SOMA(A1:A10)
• Média: =MÉDIA(A1:A10)
• Contagem: =CONT.VAL(A1:A10)
• Máximo: =MÁXIMO(A1:A10)
• Mínimo: =MÍNIMO(A1:A10)
• Se: =SE(condição;verdadeiro;falso)
• Procv: =PROCV(valor;intervalo;coluna;falso)

**Formatação:**
• Número: casas decimais, separador de milhar
• Moeda: R$ com 2 casas decimais
• Data: dd/mm/aaaa
• Condicional: formatação baseada em valores

**Gráficos:**
• Colunas, linhas, pizza, barras
• Título, legenda, rótulos de dados

**Outros:**
• Filtro e ordenação
• Tabela dinâmica (conceito)
• Impressão: área de impressão, cabeçalho/rodapé""",
                'dica': '=SE() e =PROCV() são as funções mais cobradas em concursos. Pratique exemplos práticos.'
            },
            {
                'titulo': 'Internet e Redes',
                'conteudo': """**Conceitos de rede:**
• LAN: rede local (prédio, casa)
• WAN: rede de longa alcance (internet)
• WLAN: rede sem fio (Wi-Fi)
• IP: endereço único do computador
• DNS: converte nome em IP (google.com → 142.250.x.x)

**Navegadores:**
• Chrome, Firefox, Edge
• Abas, favoritos, histórico
• Modo anônimo/privado
• Extensões

**Protocolos:**
• HTTP/HTTPS: navegação web (S = seguro)
• FTP: transferência de arquivos
• SMTP/POP3/IMAP: e-mail
• TCP/IP: protocolo base da internet

**E-mail:**
• Caixa de entrada, enviados, rascunho
• Anexos
• CC (cópia) e CCO (cópia oculta)
• Responder, encaminhar
• Spam: lixo eletrônico
• Phishing: golpe por e-mail

**Segurança:**
• Firewall: barreira de segurança
• Antivírus: proteção contra malware
• HTTPS: comunicação criptografada
• Autenticação de dois fatores (2FA)""",
                'dica': 'Diferença entre HTTP e HTTPS, e entre CC e CCO, são cobradas frequentemente.'
            },
            {
                'titulo': 'Segurança da Informação',
                'conteudo': """**Tríade CIA:**
• **Confidencialidade:** acesso apenas a autorizados
• **Integridade:** dados não alterados indevidamente
• **Disponibilidade:** dados acessíveis quando necessário

**Tipos de ameaças:**
• **Vírus:** programa que se replica e danifica
• **Worm:** se espalha automaticamente pela rede
• **Trojan:** disfarçado de programa legítimo
• **Ransomware:** criptografa dados e pede resgate
• **Spyware:** coleta informações sem consentimento
• **Phishing:** golpe por e-mail/site falso
• **Engenharia social:** manipulação psicológica

**Boas práticas:**
• Senhas fortes (8+ caracteres, maiúsculas, minúsculas, números, símbolos)
• Não clicar em links suspeitos
• Atualizar sistema e programas
• Backup regular
• Autenticação de dois fatores (2FA)
• Não usar Wi-Fi público para operações sensíveis
• Verificar URL antes de inserir dados""",
                'dica': 'Phishing é o ataque mais cobrado. Entenda: e-mail/site falso que imita instituição para roubar dados.'
            },
            {
                'titulo': 'Computação em Nuvem (Cloud)',
                'conteudo': """**Conceito:**
• Serviços de TI pela internet
• Não precisa de infraestrutura local
• Paga pelo uso (modelo pay-as-you-go)

**Modelos de serviço:**
• **IaaS:** infraestrutura como serviço (servidores virtuais)
• **PaaS:** plataforma como serviço (ambiente de desenvolvimento)
• **SaaS:** software como serviço (Office 365, Gmail)

**Modelos de implantação:**
• **Público:** disponível para todos (AWS, Azure, Google Cloud)
• **Privado:** uso exclusivo de uma organização
• **Híbrido:** combinação de público e privado

**Vantagens:**
• Escalabilidade
• Redução de custos
• Acessibilidade remota
• Atualização automática

**Exemplos no governo:**
• Gov.br: serviços públicos digitais
• Nuvem.gov.br: nuvem governamental
• Office 365 Gouverno""",
                'dica': 'Diferença entre IaaS, PaaS e SaaS é muito cobrada. SaaS = usa software. PaaS = desenvolve. IaaS = gerencia infraestrutura.'
            },
        ],
        'exercicios': [
            {
                'enunciado': 'No Excel, qual função retorna o maior valor de um intervalo de células?',
                'alternativas': [
                    'A) =MÍNIMO(A1:A10)',
                    'B) =MÁXIMO(A1:A10)',
                    'C) =MÉDIA(A1:A10)',
                    'D) =SOMA(A1:A10)',
                ],
                'resposta': 'B',
                'comentario': '=MÁXIMO() retorna o maior valor. =MÍNIMO() retorna o menor. =MÉDIA() retorna a média. =SOMA() retorna a soma.'
            },
        ],
    },

    # =====================================================
    # 8. NOÇÕES DE CONTABILIDADE (~4% da prova)
    # =====================================================
    {
        'nome': 'Noções de Contabilidade',
        'chave': 'contabilidade',
        'peso': '4%',
        'descricao': 'Princípios contábeis, demonstrações financeiras, conceitos básicos.',
        'topicos': [
            {
                'titulo': 'Conceitos Fundamentais',
                'conteudo': """**Patrimônio:**
• Conjunto de bens, direitos e obrigações
• **Ativo:** bens e direitos (o que a empresa tem)
• **Passivo:** obrigações (o que a empresa deve)
• **Patrimônio Líquido:** Ativo - Passivo

**Equação fundamental:**
**Ativo = Passivo + Patrimônio Líquido**

**Classificação do Ativo:**
• **Ativo Circulante:** curto prazo (caixa, bancos, estoques)
• **Ativo Não Circulante:** longo prazo (imóveis, equipamentos)

**Classificação do Passivo:**
• **Passivo Circulante:** curto prazo (fornecedores, salários)
• **Passivo Não Circulante:** longo prazo (empréstimos de longo prazo)
• **Patrimônio Líquido:** capital social, reservas, lucros

**Contas:**
• T-Conta: débito (esquerda) e crédito (direita)
• Regra: Ativo ↑ = débito / Passivo ↑ = crédito
• Despesa = débito / Receita = crédito""",
                'dica': 'Ativo = Passivo + PL. Ativo cresce com débito. Passivo e PL crescem com crédito.'
            },
            {
                'titulo': 'Princípios Contábeis',
                'conteudo': """**CPC (Comitê de Pronunciamentos Contábeis):**

**1. Princípio da Entidade:**
• Patrimônio da empresa ≠ patrimônio dos sócios

**2. Princípio da Continuidade:**
• Empresa presume-se em funcionamento por prazo indeterminado

**3. Princípio da Oportunidade:**
• Registro no momento da ocorrência (competência)

**4. Princípio do Registro pelo Valor Original:**
• Ativos registrados pelo custo de aquisição

**5. Princípio da Competência:**
• Receitas e despesas no período em que ocorrem (não quando recebidas/pagas)

**6. Princípio da Prudência (Conservadorismo):**
• Antecipar perdas, não lucros
• Na dúvida, registrar o menor valor de ativo ou maior de passivo

**NBC (Normas Brasileiras de Contabilidade):**
• NBC TG 1000: Contabilidade para Pequenas Empresas
• NBC TG 01: Redução ao Valor Recuperável de Ativos""",
                'dica': 'Competência vs. Caixa: competência = quando ocorre. Caixa = quando recebe/paga. O INSS usa competência.'
            },
            {
                'titulo': 'Demonstrações Contábeis',
                'conteudo': """**1. Balanço Patrimonial:**
• Fotografia do patrimônio em uma data
• Ativo = Passivo + PL
• Publicado anualmente

**2. Demonstração do Resultado (DRE):**
• Receitas - Despesas = Lucro/Prejuízo
• Período (geralmente 1 ano)

**3. Demonstração do Fluxo de Caixa (DFC):**
• Entradas e saídas de caixa
• Operacional, investimento, financiamento

**4. Demonstração das Mutações do PL (DMPL):**
• Variações no patrimônio líquido

**5. Notas Explicativas:**
• Informações complementares
• Políticas contábeis adotadas

**Análise de balanço (indicadores):**
• Liquidez corrente = Ativo Circulante / Passivo Circulante
• Liquidez seca = (AC - Estoques) / PC
• Endividamento = Passivo Total / Ativo Total""",
                'dica': 'Liquidez corrente > 1 = empresa pode pagar suas dívidas de curto prazo. É o indicador mais cobrado.'
            },
        ],
        'exercicios': [
            {
                'enunciado': 'De acordo com o Princípio da Competência, uma despesa deve ser registrada:',
                'alternativas': [
                    'A) No momento em que é paga.',
                    'B) No momento em que é incorrida.',
                    'C) No início do exercício seguinte.',
                    'D) Quando o fornecedor emite a nota fiscal.',
                ],
                'resposta': 'B',
                'comentario': 'Competência: registra quando ocorre (incorre), não quando paga. Se paga depois, registra primeiro como "a pagar".'
            },
        ],
    },

    # =====================================================
    # 9. ATUALIDADES (~3% da prova)
    # =====================================================
    {
        'nome': 'Atualidades',
        'chave': 'atualidades',
        'peso': '3%',
        'descricao': 'Temas de política, economia, tecnologia e sociedade relevantes para o contexto atual.',
        'topicos': [
            {
                'titulo': 'Temas Políticos Relevantes',
                'conteudo': """**Estrutura política do Brasil:**
• República Federativa Presidencialista
• 3 Poderes: Executivo, Legislativo, Judiciário
• 26 Estados + DF + 5.570 Municípios

**Temas recorrentes:**
• Reforma da Previdência (EC 103/2019)
• Reforma Tributária (EC 132/2023)
• PEC da Reforma Administrativa
• Privatizações e concessões
• Transição energética
• Sustentabilidade e ESG

**Organismos internacionais:**
• ONU: Organização das Nações Unidas
• OMS: Organização Mundial da Saúde
• FMI: Fundo Monetário Internacional
• Banco Mundial
• OMC: Organização Mundial do Comércio
• BRICS: Brasil, Rússia, Índia, China, África do Sul""",
                'dica': 'Cebraspe cobra temas atuais mas com foco em conceitos, não em opinião. Estude os fatos, não as posições.'
            },
            {
                'titulo': 'Temas Econômicos',
                'conteudo': """**Indicadores econômicos:**
• PIB: Produto Interno Bruto (riqueza produzida)
• IPCA: Índice de Preços ao Consumidor Amplo (inflação)
• SELIC: taxa básica de juros
• Câmbio: valor do real frente ao dólar
• Dívida pública: relação dívida/PIB

**Política monetária:**
• Banco Central (BCB): controla inflação
• SELIC: instrumento principal
• Meta de inflação: piso, centro e teto

**Política fiscal:**
• Orçamento da União: LOA, PPA, LDO
• Superávit/déficit primário
• Teto de gastos (EC 95/2016) → novo arcabouço fiscal

**Temas globais:**
• Guerra Rússia-Ucrânia
• Conflito Israel-Palestina
• Mudanças climáticas
• Transição energética
• Inteligência artificial""",
                'dica': 'IPCA (inflação) e SELIC (juros) são os indicadores mais cobrados. Saiba o conceito de cada um.'
            },
            {
                'titulo': 'Temas Tecnológicos e Sociais',
                'conteudo': """**Inteligência Artificial (IA):**
• ChatGPT, automação, machine learning
• Impacto no mercado de trabalho
• Regulamentação da IA
• Ética e vieses algorítmicos

**Transformação Digital:**
• Governo digital (gov.br)
• Assinatura digital
• Processo eletrônico
• Lei Geral de Proteção de Dados (LGPD)

**LGPD — Lei 13.709/2018:**
• Proteção de dados pessoais
• Consentimento do titular
• Direitos: acesso, correção, eliminação
• ANPD: Autoridade Nacional de Proteção de Dados

**Temas sociais:**
• Desigualdade social
• Inclusão digital
• Saúde pública (SUS)
• Educação básica
• Segurança pública""",
                'dica': 'LGPD é tema quente em concursos. Saiba: consentimento, direitos do titular, ANPD, e dados sensíveis.'
            },
        ],
        'exercicios': [
            {
                'enunciado': 'No regime de metas para a inflação, qual taxa é utilizada como principal referência da política monetária do Banco Central do Brasil?',
                'alternativas': [
                    'A) A taxa SELIC.',
                    'B) O câmbio flutuante.',
                    'C) O controle de preços.',
                    'D) A emissão de moeda.',
                ],
                'resposta': 'A',
                'comentario': 'A taxa Selic é a taxa básica e a principal referência da política monetária. A transmissão para a inflação depende das condições econômicas; não é correto tratar o efeito como automático.'
            },
        ],
    },
]
