"""Scope growth includes every eligible candidate without changing rank rules."""

import csv
from io import StringIO

import pytest

from scripts import propose_scope
from taxonmech import seed
from tests.test_seed import _inventory


@pytest.fixture
def many_taxa(monkeypatch, tmp_path):
    inv = _inventory()
    for number in range(1000, 1120):
        tid = f"NCBITaxon:{number}"
        inv.taxa[tid] = dict(inv.taxa["NCBITaxon:562"], taxon_id=tid, label=f"Species {number}")
    inv.taxa["NCBITaxon:2"]["attested_by"] = "bacdive"
    inv.taxa["NCBITaxon:9000"] = dict(inv.taxa["NCBITaxon:83333"], taxon_id="NCBITaxon:9000",
                                    rank="NO_RANK")
    inv.taxa["NCBITaxon:9001"] = dict(inv.taxa["NCBITaxon:562"], taxon_id="NCBITaxon:9001",
                                    attested_by="")
    monkeypatch.setattr(propose_scope, "load_inventory", lambda: inv)
    scope = tmp_path / "scope.tsv"
    scope.write_text("identifier\tadded\treason\nNCBITaxon:562\t2026-09-10\toriginal\n")
    monkeypatch.setattr(propose_scope, "SCOPE_PATH", scope)
    monkeypatch.setattr(propose_scope, "load_scope", lambda: seed.load_scope(scope))
    return inv, scope


def test_all_candidates_and_append_are_complete(many_taxa, capsys):
    _, scope = many_taxa
    before = scope.read_bytes()
    assert propose_scope.main(["--rule", "attested", "--rank", "", "--all", "--date", "2026-09-12"]) == 0
    output = capsys.readouterr()
    rows = list(csv.DictReader(StringIO(output.out), delimiter="\t"))
    ids = {row["identifier"] for row in rows}
    assert len(rows) == len(ids) == 123
    assert {"NCBITaxon:562", "NCBITaxon:83333", "NCBITaxon:9000"} <= ids
    assert not {"NCBITaxon:2", "NCBITaxon:9001"} & ids
    assert "123 of 123" in output.err
    assert all(row["added"] == "2026-09-12" for row in rows)
    assert propose_scope.main(["--rule", "attested", "--rank", "", "--all", "--append"]) == 0
    appended = capsys.readouterr().out.splitlines()
    assert len(appended) == 122 and not any(line.startswith("NCBITaxon:562\t") for line in appended)
    assert scope.read_bytes() == before


def test_default_limit_and_species_filter_remain_explicit(many_taxa, capsys):
    assert propose_scope.main(["--rule", "attested"]) == 0
    output = capsys.readouterr()
    assert len(list(csv.DictReader(StringIO(output.out), delimiter="\t"))) == 100
    assert "100 of 121" in output.err
    assert propose_scope.main(["--rule", "attested", "--all"]) == 0
    assert "121 of 121" in capsys.readouterr().err


@pytest.mark.parametrize("args", [["--all", "--top", "1"], ["--top", "0"], ["--top", "-1"]])
def test_invalid_limits_are_rejected(args):
    with pytest.raises(SystemExit) as exc:
        propose_scope.main(args)
    assert exc.value.code == 2


def test_scope_covers_all_attested_species_or_below(repo_root):
    with (repo_root / "data/raw/ncbitaxon_taxa.tsv").open() as handle:
        taxa = {row["taxon_id"]: row for row in csv.DictReader(handle, delimiter="\t")}
    eligible = set()
    for identifier, row in taxa.items():
        if not row["attested_by"]:
            continue
        if row["rank"] in seed.RECORD_RANKS:
            eligible.add(identifier)
        elif row["rank"] in seed.ANCESTRY_DEPENDENT_RANKS:
            parent, seen = row["parent_id"], {identifier}
            while parent in taxa and parent not in seen:
                seen.add(parent)
                if taxa[parent]["rank"] == "SPECIES":
                    eligible.add(identifier)
                    break
                parent = taxa[parent]["parent_id"]
    assert set(seed.load_scope()) == eligible
