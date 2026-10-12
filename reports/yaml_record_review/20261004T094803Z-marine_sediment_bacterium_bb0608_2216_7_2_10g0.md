# YAML Record Review: marine sediment bacterium BB0608_2216_7.2_10G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_7_2_10g0.yaml`
- Started UTC: 2026-10-04T09:46:55Z
- Finished UTC: 2026-10-04T09:48:03Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033436`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The full designation
BB0608_2216_7.2_10G0 distinguishes neighboring isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_7_2_10g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_7_2_10g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221070 and scientific-name row 30378 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033436&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033436)
confirm identity, species rank and parent 49928; EFetch confirms code 11.
The root-first lineage matches root (1), cellular organisms (131567),
Bacteria (2) and unclassified Bacteria (49928). Species rank does not prove
valid nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750299.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750299.1),
UID 333384646, a 679-base partial 16S rRNA gene. Its source names strain
BB0608_2216_7.2_10G0, taxon 1033436, coastal marine sediment, Australia:
Gulf of Carpentaria, and June 2008 collection. The qualifier is strain,
not clone or environmental sample. This locus is not a genome, culture
deposit or independent taxonomic classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither supplies a DOI
or PMID. Full manuscript text was not obtained; no phenotype was inferred
from the title. Exact Assembly search returned zero with phrase-not-found
and no-items warnings. The NAME attestation and 2026-09-13 snapshot agree
with the inventory; the count is not a number of independent experiments.

## Completeness

Complete exact-ID scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and
BactoTraits inventories found no rows. Empty optional slots reflect bounded
source coverage; zero inventoried strains does not mean never cultured.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
numeric ID and complete label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All nine matches were inspected: target backbone, scope and scientific
name, plus six unrelated SAMEA1033436 source rows. Recursive structured
SOURCE.json searches found no matches. These checks do not establish
universal absence.

The five JSONL objects were read in full, and the ATB TSV fields inspected:

- `data/bvbrc/bvbrc-0001.jsonl.gz:493`: Staphylococcus aureus BSAR57, taxon 1280, genome 1280.3930, GCF_001203975.1, PRJEB2655, SAMEA1033436 and unversioned CSAX00000000.
- `data/gold/projects.jsonl.gz:77925`: Staphylococcus aureus BSAR57, project Gp0129884, organism Go0121988, PRJEB2655 and SAMEA1033436. GOLD organism/project IDs are not genome identifiers and supply no target deposit chain.
- `data/catalog/gtdb_genomes-0017.jsonl.gz:28041`: RS_GCF_001203975.1, GCA_001203975.1, Staphylococcus aureus, taxon 1280, raw strain BSAR57, SAMEA1033436, PRJNA224116 and CSAX00000000.1.
- `data/catalog/ncbi_refseq-0000.jsonl.gz:37017` and `data/catalog/ncbi_genbank-0000.jsonl.gz:44138`: GCF_001203975.1 / GCA_001203975.1, explicit identical pair, BSAR57, taxon 1280, SAMEA1033436 and CSAX00000000.1. RefSeq reports PRJNA224116 while GenBank reports PRJEB2655; both source values are retained.
- ATB SAMEA1033436, run ERR084771 and ENA analysis ERZ3068787: Staphylococcus aureus, FASTA available and filters passing. Sharing this BioSample does not establish assembly equivalence with the NCBI pair.

The numeric BioSample suffix is not the target taxon ID. None of these
objects supports a target strain/deposit/genome relationship.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321422`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033436 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13519`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
