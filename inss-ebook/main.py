"""Ponto de entrada para validacao e geracao da edicao."""

import sys
import os
import argparse

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from metadata import EDITION
from validate_content import validate_content


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--validate', action='store_true', help='valida a estrutura editorial')
    parser.add_argument('--strict', action='store_true', help='trata avisos editoriais como erros')
    parser.add_argument('--output', default='Apostila_INSS_Completa.pdf', help='caminho do PDF de saida')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.validate:
        erros, avisos = validate_content(strict=args.strict)
        for aviso in avisos:
            print(f'AVISO: {aviso}')
        for erro in erros:
            print(f'ERRO: {erro}')
        print(f'Edicao: {EDITION.edition} ({EDITION.status})')
        sys.exit(1 if erros else 0)

    from generator import gerar_pdf

    print('=' * 60)
    print('  APOSTILA COMPLETA INSS — TÉCNICO DO SEGURO SOCIAL')
    print('  Gerando PDF profissional...')
    print('=' * 60)

    try:
        nome = gerar_pdf(args.output)
        tamanho = os.path.getsize(nome) / 1024
        print(f'\n📄 Arquivo: {nome}')
        print(f'📦 Tamanho: {tamanho:.1f} KB')
        print(f'✅ Concluído com sucesso!')
    except Exception as e:
        print(f'\n❌ Erro: {e}')
        import traceback
        traceback.print_exc()
