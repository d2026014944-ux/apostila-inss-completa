"""Configurações de estilo e cores para o ebook INSS."""

# === PALETA DE CORES ===
CORES = {
    'primaria': (42, 45, 52),         # Grafite editorial
    'secundaria': (56, 111, 168),     # Azul discreto de destaque
    'destaque': (104, 146, 187),      # Azul claro de apoio
    'sucesso': (0, 128, 0),           # Verde
    'alerta': (204, 0, 0),            # Vermelho
    'fundo_box': (232, 234, 237),     # Cinza editorial
    'fundo_dica': (244, 245, 246),    # Cinza claro
    'fundo_exercicio': (232, 238, 244),  # Azul muito claro
    'fundo_alerta': (245, 235, 235),  # Vermelho claro
    'cinza_escuro': (51, 51, 51),
    'cinza_medio': (102, 102, 102),
    'cinza_claro': (200, 200, 200),
    'branco': (255, 255, 255),
    'preto': (0, 0, 0),
}

# === CORES POR DISCIPLINA ===
CORES_DISCIPLINA = {
    'portugues': (56, 111, 168),
    'raciocinio': (68, 103, 142),
    'constitucional': (80, 91, 104),
    'administrativo': (92, 112, 132),
    'previdenciario': (67, 92, 119),
    'etica': (83, 104, 119),
    'informatica': (47, 75, 105),
    'contabilidade': (94, 101, 109),
    'atualidades': (73, 113, 137),
}

# === MARCADORES ASCII POR DISCIPLINA ===
ICONES = {
    'portugues': 'PT',
    'raciocinio': 'RL',
    'constitucional': 'CF',
    'administrativo': 'DA',
    'previdenciario': 'DP',
    'etica': 'ET',
    'informatica': 'IT',
    'contabilidade': 'CT',
    'atualidades': 'AT',
}

# === PESOS DAS DISCIPLINAS ===
PESOS = {
    'Direito Previdenciário': 25,
    'Língua Portuguesa': 18,
    'Direito Constitucional': 12,
    'Direito Administrativo': 12,
    'Raciocínio Lógico-Matemático': 10,
    'Ética no Serviço Público': 8,
    'Informática': 8,
    'Noções de Contabilidade': 4,
    'Atualidades': 3,
}
