"""Metadados editoriais da edicao publicada."""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class EditionMetadata:
    """Contrato minimo que deve acompanhar cada PDF distribuido."""

    product_name: str
    edition: str
    status: str
    reference_date: str
    target_role: str
    official_notice: str | None
    update_policy: str
    disclaimer: str


EDITION = EditionMetadata(
    product_name="Apostila INSS - Tecnico do Seguro Social",
    edition="0.1.0-auditoria",
    status="pre-edital",
    reference_date=date.today().isoformat(),
    target_role="Tecnico do Seguro Social",
    official_notice=None,
    update_policy=(
        "Edicao de validacao editorial. Nao inclui promessa de atualizacoes "
        "comerciais ate a publicacao de uma politica especifica."
    ),
    disclaimer=(
        "Material educacional independente. Consulte sempre o edital e as "
        "fontes oficiais vigentes. Este material nao garante aprovacao e nao "
        "substitui a legislacao, atos oficiais ou orientacao profissional."
    ),
)


def edition_label() -> str:
    """Retorna um rotulo curto para capa, rodape e nome de arquivo."""
    return f"Edicao {EDITION.edition} | {EDITION.status} | corte {EDITION.reference_date}"
