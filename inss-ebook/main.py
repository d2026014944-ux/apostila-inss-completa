"""Ponto de entrada — gera o ebook INSS completo."""

import sys
import os

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generator import gerar_pdf

if __name__ == '__main__':
    print('=' * 60)
    print('  APOSTILA COMPLETA INSS — TÉCNICO DO SEGURO SOCIAL')
    print('  Gerando PDF profissional...')
    print('=' * 60)

    try:
        nome = gerar_pdf('Apostila_INSS_Completa.pdf')
        tamanho = os.path.getsize(nome) / 1024
        print(f'\n📄 Arquivo: {nome}')
        print(f'📦 Tamanho: {tamanho:.1f} KB')
        print(f'✅ Concluído com sucesso!')
    except Exception as e:
        print(f'\n❌ Erro: {e}')
        import traceback
        traceback.print_exc()
