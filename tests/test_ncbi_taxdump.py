"""Primary taxonomy completeness and retirement evidence boundaries."""

import hashlib
import io
import tarfile

import pytest

from taxonmech.ncbi_taxdump import load_taxdump, prokaryote_taxa


def archive(tmp_path, *, nodes=None, names=None, omit=()):
    rows = nodes or [
        (1, 1, "no rank"),
        (2, 1, "domain"),
        (2157, 1, "domain"),
        (5, 2, "species"),
        (6, 5, "strain"),
        (7, 2157, "species"),
        (8, 1, "species"),
    ]
    node_rows = [
        [str(tid), str(parent), rank, "", "0", "0", "11", "0", "0", "0", "0", "0", ""]
        for tid, parent, rank in rows
    ]
    name_rows = (
        names
        if names is not None
        else [[str(tid), f"Taxon {tid}", "", "scientific name"] for tid, _, _ in rows]
    )
    tables = {
        "nodes.dmp": node_rows,
        "names.dmp": name_rows,
        "merged.dmp": [["99", "5"]],
        "typematerial.dmp": [["5", "Taxon 5", "type strain", "DSM 1"]],
        "excludedfromtype.dmp": [["5", "Taxon 5", "not considered type", "DSM 2"]],
    }
    path = tmp_path / "taxonomy.tar.gz"
    with tarfile.open(path, "w:gz") as handle:
        for name, values in tables.items():
            if name in omit:
                continue
            payload = "".join("\t|\t".join(row) + "\t|\n" for row in values).encode()
            info = tarfile.TarInfo(name)
            info.size = len(payload)
            handle.addfile(info, io.BytesIO(payload))
    return path


def test_complete_domain_selection_keeps_species_and_strains_without_other_sources(tmp_path):
    path = archive(tmp_path)
    nodes, parents, ranks, _, redirects, material = load_taxdump(
        path, expected_sha256=hashlib.sha256(path.read_bytes()).hexdigest()
    )
    assert prokaryote_taxa(parents, nodes) == {
        "NCBITaxon:2",
        "NCBITaxon:2157",
        "NCBITaxon:5",
        "NCBITaxon:6",
        "NCBITaxon:7",
    }
    assert ranks["NCBITaxon:6"] == "STRAIN"
    assert redirects == {"NCBITaxon:99": "NCBITaxon:5"}
    assert {row["source_field"] for row in material} == {"typematerial.dmp", "excludedfromtype.dmp"}
    assert material[1]["type"] == "not considered type"


def test_source_hash_and_required_archive_members_fail_closed(tmp_path):
    with pytest.raises(ValueError, match="SHA256"):
        load_taxdump(archive(tmp_path), expected_sha256="0" * 64)
    with pytest.raises(ValueError, match="required members"):
        load_taxdump(archive(tmp_path, omit=("names.dmp",)))


@pytest.mark.parametrize(
    "nodes",
    [
        [(1, 1, "no rank"), (5, 6, "species"), (6, 5, "strain")],
        [(1, 1, "no rank"), (5, 6, "species")],
        [(1, 1, "no rank"), (5, 5, "species")],
        [(1, 1, "no rank"), (2, 5, "domain"), (5, 2, "species")],
        [(1, 1, "no rank"), (2157, 5, "domain"), (5, 2157, "species")],
        [(1, 2, "no rank"), (2, 1, "domain")],
    ],
)
def test_broken_or_cyclic_lineage_never_yields_a_partial_inventory(tmp_path, nodes):
    with pytest.raises(ValueError):
        load_taxdump(archive(tmp_path, nodes=nodes))


def test_scientific_names_are_required_and_unique(tmp_path):
    with pytest.raises(ValueError, match="scientific names"):
        load_taxdump(archive(tmp_path, names=[]))
    with pytest.raises(ValueError, match="duplicate NCBI scientific name"):
        load_taxdump(archive(tmp_path, names=[["1", "root", "", "scientific name"]] * 2))
