# YAML Record Review: Planktothrix cf. suspensa FEM_DD592

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/planktothrix_cf_suspensa_fem_dd592.yaml`
- Started UTC: 2026-10-06T23:59:23Z
- Finished UTC: 2026-10-07T00:01:35Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read before judgment:
`NCBITaxon:1035354`, Planktothrix cf. suspensa FEM_DD592,
`STRAIN`, `BACTERIA`, parent `NCBITaxon:1035353`, genetic code 11,
`grounding_status: EXACT`, and `mapping_status: SEEDED`. It contains a
12-entry ancestor chain, zero BacDive strains, one NCBITAXON NAME attestation,
and one seed event. No synonym, nomenclature, taxonomy mapping, genome link,
definition, literature evidence, discussion or causal graph is asserted.

This target is the qualified strain concept, not its species parent
Planktothrix suspensa, SAG 5.81, or another FEM_DD strain. The PATHS entry
uniquely resolves the filename. An ignored-inclusive filename search found
no prior report for this stem.

The record is generated from source inventories and scope. No YAML, source
inventory, generator, page, prior report, history entry or lifecycle status
was changed.

## Validation

Commands used the existing environment and
`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/planktothrix_cf_suspensa_fem_dd592.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/planktothrix_cf_suspensa_fem_dd592.yaml --out /private/tmp/p592-strict.tsv`: exit 0, exactly one file scanned, zero ERROR rows. The actual output TSV was read and is header-only.
- Read-only parsed comparisons checked the exact pinned backbone row, full
  root-first lineage, synonym fields, seven non-NCBI source inventories,
  PATHS, scope, attestation and seed-event wording.
- Exact-taxonomy scans of type-material, merged-ID and dropped-ID inventories
  found no row for this target. The pinned backbone has no children below
  this taxon.

Not checked: full-corpus `just verify-corpus`, `just qc`,
`just validate-all`, `just validate-history`, `just validate-products`,
provenance hashes, tests, generated-site drift and publication-size gates.
No target-only replacement for a corpus gate was invented. There are no
curator-added graph nodes or new history references to validate in this
record. Passing schema checks establishes shape, not biological truth.

## Identity and Grounding

The exact row `data/raw/ncbitaxon_taxa.tsv:222039` agrees with the record's
ID, full qualified label, strain rank, parent, genetic code and 2026-09-13
snapshot. `data/catalog/ncbi_names-0005.jsonl.gz:31517` is its scientific
name, not a synonym or a culture-deposit assertion.
`data/taxa/PATHS.tsv:14530` and `curation/seed_scope.tsv:322311` agree
on the target and inclusion reason.

The lineage, including rank and label for every ancestor, is:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 1783272 Bacillati / KINGDOM; 1798711 Cyanobacteriota/Melainabacteria group / CLADE; 1117 Cyanobacteriota / PHYLUM; 3028117 Cyanophyceae / CLASS; 1301283 Oscillatoriophycideae / SUBCLASS; 1150 Oscillatoriales / ORDER; 1892252 Microcoleaceae / FAMILY; 54304 Planktothrix / GENUS; 1035353 Planktothrix suspensa / SPECIES`.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035354&retmode=xml)
and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035354)
were inspected. They retain the exact label and rank and agree with the
parent and ancestor IDs. XML additionally confirms genetic code 11;
Datasets explicitly includes the root. No other name or type material is
asserted by the live XML.

The `cf.` qualification is material and is preserved. EXACT describes
resolution to this precise NCBI concept; it does not convert a provisional
species identification into a definitive one or equate FEM_DD592 with a
species type culture.

## Evidence

The attestation's ID, label, NAME unit, count 1 and snapshot date trace to
the pinned NCBI inventory. The seed event matches the exact scope reason and
NCBITAXON source list. Its timestamp 2026-09-13T17:54:04Z matches the newest
source manifest, as implemented by
`src/taxonmech/seed.py::_seed_timestamp`. The manifests were parsed during
this review turn: raw 17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z,
all on 2026-09-13. This event is provenance, not human review.

The complete exact-taxonomy nuccore result set contained two records.
Both were inspected in full metadata form, including source qualifiers,
references, gene/CDS features and protein IDs:

| Record | Sequence scope | Source-provided protein identifiers |
|---|---|---|
| [HQ288044.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ288044.1) | 641 bases; partial rpoC1 coding sequence, annotated DNA-dependent RNA polymerase | AEF98440.1 |
| [HQ288045.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ288045.1) | 879 bases; partial rbcL and complete rbcX coding sequences | AEF98441.1; AEF98442.1 |

Both explicitly name FEM_DD592 and taxon 1035354, with an Italian freshwater
sample collected 28 April 2010. They were directly submitted on 22 September
2010 by D'Alelio, Gandolfi and Salmaso from Fondazione Edmund Mach.
Their research reference still says Unpublished and uses a longer working
title. Neither record supplies a BioSample, assembly, BioProject or registered
culture-collection deposit. The protein IDs are retained as source feature
annotations; their protein records were not independently fetched and no
experimental protein-function claim is inferred.

The relevant primary paper is D'Alelio and Salmaso (2011), Phycologia
50(4):379-383, [DOI 10.2216/10-73.1](https://doi.org/10.2216/10-73.1).
The publisher and institutional-repository fetches returned HTTP 403; their
search snippets were treated only as leads. The
[author-uploaded article text](https://www.researchgate.net/publication/237201260_Occurrence_of_an_uncommon_Planktothrix_Cyanoprokaryota_Oscillatoriales_in_a_deep_lake_south_of_the_Alps)
was opened and its methods, results and Table 1 inspected. Table 1 directly
pairs FEM_DD592 with HQ288044 and HQ288045. The authors provisionally assigned
the Lake Idro strains using morphology and the two gene regions; the
qualification is therefore supported, not a label defect. Their historical
statement about culture-collection coverage is not evidence of today's
availability. No toxin phenotype, universal species trait or genome
equivalence is transferred from the paper.

An exact non-expanded Assembly search returned zero, with a
phrase-not-found warning. The
[Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035354/dataset_report)
returned an empty object. These observations are bounded to the queries and
date checked; they do not prove that no assembly exists anywhere under
another classification. The two short coding-region records are not whole
genome assemblies, even though one includes a complete CDS.

The structured iModulonDB dataset inventory was read before open web research
via `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
Its 28 rows contain no matching Planktothrix organism/dataset. The adapter was
not applicable, and its lack of coverage is not negative biological evidence.

## Completeness

A completed `rg --no-ignore --hidden -n -z -i` discovery search used
`1035354|FEM[-_ ]*DD592|planktothrix_cf_suspensa_fem_dd592` over
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`. All 21 matching rows were read losslessly
using their native JSON or TSV structure, including compressed files.
The five SOURCE.json files were separately parsed in full and history
filenames checked independently of gitignore.

Three rows are this target's backbone, scientific name and scope. The other
18 comprise one Mesorhizobium assembly, one Campylobacter assembly, ten
Klebsiella GenBank assemblies, five suppressed Klebsiella RefSeq assemblies
and an ATB M. tuberculosis run. Their numeric substring hits are not taxon
or strain matches; identifiers are detailed below.

A second ignored-inclusive search for HQ288044, HQ288045 and
`10.2216/10-73.1` completed with zero matches in the same ten roots.
Its separate structured metadata and history-filename checks also found
nothing. These are bounded local findings, not claims of absence from the
literature or public sequence archives.

Parsed exact-taxonomy scans found no BacDive, LPSN, GTDB, GOLD, MediaDive,
Madin or BactoTraits inventory row. With no descendants, the zero BacDive
strain count is supported. It does not deny the existence of the study's
laboratory strain. No supported whole-culture-deposit chain or genome link
was found to add. The optional nomenclature, mappings, evidence, definition
and causal-graph fields can remain empty. The paper and markers are useful
future enrichment leads, not missing required fields.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity and source assertions agree, and the qualified name
preserves the unresolved species-level identification. The unpublished
sequence-reference label does not invalidate the subsequently inspected
article or create a citation defect in a YAML that cites no publication.

## Recommended Edits

None required. Do not hand-edit the generated YAML.

For later authorized literature enrichment, use a maintained evidence
mechanism in `src/taxonmech/seed.py` with tests, or an explicitly designed
curator overlay that survives regeneration. Do not invent an existing
overlay path. Any future culture-deposit mapping belongs in its primary
source/importer and must satisfy the whole-identifier and own-deposit rules.
If marker accessions are represented later, retain them as typed nucleotide
related records, not assembly or genome identifiers.

## Follow-up Checks

- Preserve FEM_DD592 and `cf.` in all future mappings; investigate an
  authority-backed reclassification before changing either.
- Before adding a deposit or sequence join, inspect a primary source that
  explicitly associates that same strain with the exact culture accession.
  Do not transfer SAG 5.81 or NIES-3736 from the species parent.
- If a whole genome is later reported, verify its assembly record,
  classification, source strain and explicit sample/deposit chain. Marker
  similarity is not sufficient.
- After an authorized maintained-input change, follow the appropriate source
  refresh, seed dry run, canary and actual-file inspection; rerun the two
  target validators and full `just verify-corpus` and `just qc`.
  No such curation was performed here.

## Additional Notes

Rejected numeric substring candidates, all inspected in their complete
native rows:

- `data/catalog/ncbi_genbank-0003.jsonl.gz:39484` is Mesorhizobium sp.
  M2D.F.Ca.ET.145.01.1.1, taxon 2563933, GCA_004792335.1,
  SAMN09232685, PRJNA453501. Its ungapped genome size 10353541
  contains the target digit string; its organism does not match.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6510` is Campylobacter jejuni
  PNUSAC013446, taxon 197, GCA_010353545.1, SAMN13327410,
  PRJNA239251. The assembly accession is not a taxon identifier.
- The ten current GenBank rows at
  `data/catalog/ncbi_genbank-0015.jsonl.gz:13534` through physical line
  13543 are Klebsiella pneumoniae, taxon 573, PRJNA503173.
  Their five historical RefSeq partners at
  `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:37908` through
  physical line 37912 are suppressed, with non-live date 2021-01-28
  and source BioProject PRJNA224116. Current GenBank partner fields do not
  make those historical RefSeq rows current.
- `data/catalog/allthebacteria.tsv.xz:569824` is M. tuberculosis,
  SAMEA3558887 / ERR1035354 / ERZ9334544, with available FASTA,
  assembly PASS and SYLPH_RESULTS_FAIL high-quality context. A run number
  containing 1035354 does not identify this cyanobacterium.

| Klebsiella BioSample | Strain | GenBank assembly | Suppressed RefSeq partner inspected |
|---|---|---|---|
| SAMN10353540 | 13HN-132 | GCA_016755555.1 | None in this candidate set |
| SAMN10353541 | 13HN-244 | GCA_016755595.1 | None in this candidate set |
| SAMN10353542 | 14HN-106 | GCA_016755575.1 | None in this candidate set |
| SAMN10353543 | 14HN-121 | GCA_016755515.1 | None in this candidate set |
| SAMN10353544 | 14HN-13 | GCA_016755535.1 | GCF_016755535.1 |
| SAMN10353545 | 14HN-130 | GCA_016755475.1 | GCF_016755475.1 |
| SAMN10353546 | 14HN-136 | GCA_016755485.1 | GCF_016755485.1 |
| SAMN10353547 | 14HN-137 | GCA_016755445.1 | None in this candidate set |
| SAMN10353548 | 14HN-15 | GCA_016755415.1 | GCF_016755415.1 |
| SAMN10353549 | 14HN-17 | GCA_016755435.1 | GCF_016755435.1 |

No paid research, genome download, external contact, GitHub mutation,
history append or status promotion was performed. Eukaryota remains outside
this review's target scope.
