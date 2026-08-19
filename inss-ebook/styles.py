"""Configurações de estilo e cores para o ebook INSS."""

# === PALETA DE CORES ===
CORES = {
    'primaria': (0, 51, 102),        # Azul escuro institucional
    'secundaria': (0, 102, 178),      # Azul médio
    'destaque': (255, 153, 0),        # Laranja/Amarelo destaque
    'sucesso': (0, 128, 0),           # Verde
    'alerta': (204, 0, 0),            # Vermelho
    'fundo_box': (230, 240, 250),     # Azul claro fundo
    'fundo_dica': (255, 248, 220),    # Amarelo claro
    'fundo_exercicio': (220, 245, 220),  # Verde claro
    'fundo_alerta': (255, 230, 230),  # Vermelho claro
    'cinza_escuro': (51, 51, 51),
    'cinza_medio': (102, 102, 102),
    'cinza_claro': (200, 200, 200),
    'branco': (255, 255, 255),
    'preto': (0, 0, 0),
}

# === CORES POR DISCIPLINA ===
CORES_DISCIPLINA = {
    'portugues': (0, 102, 178),       # Azul
    'raciocinio': (102, 0, 153),      # Roxo
    'constitucional': (0, 128, 0),    # Verde
    'administrativo': (178, 102, 0),  # Dourado
    'previdenciario': (204, 0, 0),    # Vermelho
    'etica': (0, 128, 128),           # Teal
    'informatica': (0, 51, 102),      # Azul escuro
    'contabilidade': (102, 51, 0),    # Marrom
    'atualidades': (153, 0, 153),     # Magenta
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
