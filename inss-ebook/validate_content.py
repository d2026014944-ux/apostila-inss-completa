"""Valida requisitos editoriais minimos antes da geracao do PDF."""

import argparse
import sys
from pathlib import Path

from content import DISCIPLINAS
from metadata import EDITION


REQUIRED_SOURCE_IDS = {
    "constituicao-federal",
    "lei-8212",
    "lei-8213",
    "decreto-3048",
    "ec-103",
    "lei-8112",
    "lei-9784",
    "lei-8429",
    "decreto-1171",
    "lei-lgpd",
}


def validate_content(strict=False):
    """Retorna erros bloqueantes e avisos da edicao atual."""
    errors = []
    warnings = []

    if not EDITION.edition or not EDITION.reference_date:
        errors.append("metadados de edicao incompletos")
    if EDITION.status not in {"pre-edital", "edital-confirmado"}:
        errors.append("status de edital invalido")
    if not DISCIPLINAS:
        errors.append("nenhuma disciplina cadastrada")

    seen_keys = set()
    for discipline in DISCIPLINAS:
        key = discipline.get("chave")
        name = discipline.get("nome", "disciplina sem nome")
        if not key or key in seen_keys:
            errors.append(f"chave ausente ou duplicada: {name}")
        seen_keys.add(key)
        topics = discipline.get("topicos", [])
        if not topics:
            errors.append(f"disciplina sem topicos: {name}")
        for topic in topics:
            if not topic.get("titulo") or not topic.get("conteudo"):
                errors.append(f"topico incompleto em {name}")
        for exercise in discipline.get("exercicios", []):
            if not exercise.get("enunciado") or not exercise.get("resposta"):
                errors.append(f"questao incompleta em {name}")

    source_file = Path(__file__).with_name("sources.yaml")
    source_text = source_file.read_text(encoding="utf-8") if source_file.exists() else ""
    for source_id in sorted(REQUIRED_SOURCE_IDS):
        if f"id: {source_id}" not in source_text:
            errors.append(f"fonte obrigatoria ausente: {source_id}")
    if "checked_at: null" in source_text:
        warnings.append("a matriz de fontes ainda possui itens sem data de consulta")
    elif source_text:
        warnings.append("fontes catalogadas aguardam conferencia juridica externa")

    question_file = Path(__file__).with_name("question_review.yaml")
    question_text = question_file.read_text(encoding="utf-8") if question_file.exists() else ""
    question_count = sum(len(discipline.get("exercicios", [])) for discipline in DISCIPLINAS)
    manifest_count = question_text.count("  - id:")
    if manifest_count != question_count:
        errors.append(
            f"manifesto de questoes inconsistente: {manifest_count} registros para {question_count} questoes"
        )
    if "license_status: pending_confirmation" in question_text:
        warnings.append("questoes aguardam confirmacao de licenca ou autoria")
    if "review_status: pending_external_review" in question_text:
        warnings.append("questoes aguardam revisao independente de gabarito e comentario")

    if strict:
        errors.extend(warnings)

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="trata avisos como erros")
    args = parser.parse_args()
    errors, warnings = validate_content(strict=args.strict)

    print(f"Edicao: {EDITION.edition} ({EDITION.status})")
    print(f"Disciplinas: {len(DISCIPLINAS)}")
    for warning in warnings:
        print(f"AVISO: {warning}")
    for error in errors:
        print(f"ERRO: {error}")

    if errors:
        return 1
    print("OK: estrutura minima validada")
    return 0


if __name__ == "__main__":
    sys.exit(main())
