# YAML Record Review: Wolbachia endosymbiont of Accinctapubes albifasciata

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_accinctapubes_albifasciata.yaml`
- Started UTC: 2026-10-07T14:24:13Z
- Finished UTC: 2026-10-07T14:26:33Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035962`,
Wolbachia endosymbiont of Accinctapubes albifasciata.
It is a species-rank bacterial NCBI node with `EXACT` grounding,
`SEEDED` lifecycle, genetic code 11, 11 root-first ancestors,
zero inventoried BacDive strains, one NCBITAXON name attestation,
and one inline seed event. There are no synonym, nomenclature,
mapping, strain/genome, citation, phenotype, or causal-graph objects.
Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_accinctapubes_albifasciata.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_accinctapubes_albifasciata.yaml --out /private/tmp/wol-aalbi-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source checks passed for identity, every ancestor label/rank/link, synonyms, attestation, unique path/scope rows, and seed-event wording. These are bounded checks, not corpus reproduction.
- Live NCBI EFetch/Datasets confirmed the target and the distinct DHJ03 near-match. Assembly/Nuccore index queries were inspected with their warnings.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxon identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite. No corpus-wide acceptance claim is made.
- NCBI's browser page was unavailable through the web tool; authoritative EFetch XML and Datasets JSON were available.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035962&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035962)
agree on the active taxid, exact label, species rank, Bacteria
domain, code 11, and parent `NCBITaxon:2640676`
(unclassified Wolbachia). EFetch lists no other names.

All 11 ancestors match the pinned backbone, including
Pseudomonadota, Alphaproteobacteria, Rickettsiales, Anaplasmataceae,
Wolbachieae, and Wolbachia. Datasets supplies root and EFetch
the remaining labeled chain. The record denotes the bacterium,
not the named host, and does not claim that all members of that
host species carry the same Wolbachia strain.

Complete rows agree at `data/raw/ncbitaxon_taxa.tsv:222221`,
`data/catalog/ncbi_names-0005.jsonl.gz:31729`,
`data/taxa/PATHS.tsv:14719`, and
`curation/seed_scope.tsv:322478`.
Synonym columns and `retired_into` are empty; the snapshot
is 2026-09-13. Parsed backbone/status inventories contain no
target child, type-material, merged-ID, or dropped row.

The similarly named
[DHJ03 endosymbiont](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1084937&retmode=xml)
is a separate active taxid, `NCBITaxon:1084937`, with the
scientific name ending albifasciataDHJ03 and synonym
Wolbachia sp. Accinctapubes albifasciataDHJ03.
Live taxonomy and full pinned rows agree. Shared parent and
overlapping host-name text do not establish equivalence.

## Evidence

The attestation counts one `NAME`, not a culture, specimen,
infection, sequence, or genome. Exact-target raw BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin, and BactoTraits scans found no
applicable rows. With no backbone descendants, zero inventoried
BacDive strains agrees with the inputs.

The seed wording matches scope/inventories.
Its timestamp `2026-09-13T17:54:04Z` equals the latest extraction
timestamp among the inspected raw, ATB, and StrainInfo YAML
manifests, as specified by `src/taxonmech/seed.py::_seed_timestamp`.

Exact Assembly and Nuccore searches
`txid1035962[Organism:noexp]` each returned zero with
phrase-not-found/no-items warnings. A separate exact scientific-name
Nuccore query also returned zero, with incorrect-translation and
quoted-phrase-not-found diagnostics. These are bounded indexing
results, not proof of global or historical sequence absence.
They do not invalidate the independently resolving taxonomy node.

No sequence accession or primary paper is asserted in the YAML.
A bounded web search supplied the nearby DHJ03 name as a lead;
the authority checks resolved it as a separate taxon.
No sibling sequence, host trait, reproductive phenotype,
strain identity, or experimental claim is transferred.

## Completeness

Complete enough for an NCBI-only generated identity record.
Optional fields are appropriately empty without applicable
supported objects. `strain_count: 0` is an inventory count,
not a biological assertion that infections or isolates do not exist.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Ignored, hidden, and compressed content was included.
Patterns covered the target taxid, host-qualified label, and slug.
All 19 returned candidate rows were read completely:

- Three rows describe the target backbone, scope, and scientific name.
- Four describe the distinct DHJ03 endosymbiont: backbone, scope, scientific name, and synonym.
- GOLD project `Gp0780712` describes Teratosphaeria destructans CMW44962; `SAMN10359629` is a numeric substring collision. No Eukaryota YAML was re-reviewed.
- GenBank `GCA_010359625.1` describes Campylobacter jejuni PNUSAC014942, taxid 197; the assembly digits are a collision.
- Ten AllTheBacteria rows describe Escherichia coli samples `SAMEA110359620` through `SAMEA110359629`, not this Wolbachia.

Five native `SOURCE.json` files were parsed completely,
and history filenames were searched independently.
No additional applicable local source assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within those bounded roots. No global absence claim is made.

iModulonDB is not applicable: this record names no regulator,
mechanistic gene, expression module, or transcriptomic dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, attestation units, zero BacDive
count, optional omissions, and seed provenance are supported.

## Recommended Edits

None required. Keep generated YAML and `mapping_status: SEEDED`
unchanged. A read-only review does not authorize status promotion
or a history event.

Future source corrections belong to maintained inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope corrections belong to `curation/seed_scope.tsv`.
Any enrichment must resolve this exact taxid and its evidence,
not borrow from the DHJ03 sibling or host-name resemblance.

## Follow-up Checks

No corrective follow-up is required. Before optional sequence
enrichment, establish an authoritative accession-to-taxid link;
retain indexing warnings and distinguish current availability
from historical submission status.

After authorized input changes, rerun appropriate extraction/seeding,
schema, strict, reproduction, provenance, and QC checks;
validate products/history if introduced.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- The complete YAML was reread byte-identical before report creation.
- Only this new report is written; no YAML, source, history, generated product, GitHub object, branch, or worktree is changed.
- Eukaryota remains fully covered and was not re-reviewed.
