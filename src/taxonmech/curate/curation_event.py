"""Standard helper for appending CurationEvent entries to a TaxonRecord.

Every script that mutates a record YAML should call ``record_curation_event``
to leave an audit trail. Centralising here means timestamps are ISO-8601 UTC,
the ``curation_history`` slot is created on demand, idempotent re-runs can
short-circuit (``skip_if_recent``), and the CurationEvent field names live in
one place.

Usage::

    from taxonmech.curate.curation_event import record_curation_event

    record_curation_event(
        doc,
        curator="claude",
        action="CURATED_NOMENCLATURE",
        changes="Confirmed the LPSN correct name and type strain",
        llm_assisted=True,
    )

Ported from HabitatMech / CellStructureMech ``curate/curation_event.py``.
"""

from __future__ import annotations

import datetime
from typing import Any

__all__ = ["record_curation_event", "now_iso"]


def now_iso() -> str:
    """Current UTC timestamp, whole-second precision with a ``Z`` suffix."""
    iso = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    return iso.replace("+00:00", "Z")


def record_curation_event(
    doc: dict[str, Any],
    *,
    curator: str,
    action: str,
    changes: str,
    llm_assisted: bool = False,
    timestamp: str | None = None,
    skip_if_recent: bool = False,
) -> dict[str, Any]:
    """Append a CurationEvent to ``doc['curation_history']`` and return it.

    ``llm_assisted`` is emitted only when True, so consumers can tell
    "explicitly not LLM" from "written before this field existed".
    """
    history = doc.setdefault("curation_history", [])
    if history is None:
        doc["curation_history"] = history = []

    if skip_if_recent and history:
        last = history[-1]
        if isinstance(last, dict) and last.get("curator") == curator and last.get("action") == action:
            return last

    event: dict[str, Any] = {
        "timestamp": timestamp or now_iso(),
        "curator": curator,
        "action": action,
    }
    event["changes"] = changes
    if llm_assisted:
        event["llm_assisted"] = True

    history.append(event)
    return event
