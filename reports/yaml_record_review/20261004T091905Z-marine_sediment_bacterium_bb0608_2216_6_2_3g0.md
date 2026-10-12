# YAML Record Review: marine sediment bacterium BB0608_2216_6.2_3G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_6_2_3g0.yaml`
- Started UTC: 2026-10-04T09:18:10Z
- Finished UTC: 2026-10-04T09:19:05Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033422`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The full designation
BB0608_2216_6.2_3G0 distinguishes neighboring isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_6_2_3g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_6_2_3g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221056 and scientific-name row 30364 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033422&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033422)
confirm identity, species rank and parent 49928; EFetch confirms code 11.
The root-first lineage matches root (1), cellular organisms (131567),
Bacteria (2) and unclassified Bacteria (49928). Species rank does not prove
valid nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750285.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750285.1),
UID 333384632, a 518-base partial 16S rRNA gene. Its source names strain
BB0608_2216_6.2_3G0, taxon 1033422, coastal marine sediment, Australia:
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
All ten matches were inspected: target backbone, scope and scientific name,
six unrelated Staphylococcus source rows and one unrelated assembly-length
match. Recursive structured SOURCE.json searches found no matches. These
checks do not establish universal absence.

The six Staphylococcus hits contain BioSample SAMEA1033422, not the target
taxon. Full native objects were read for the five JSONL hits:

- `data/bvbrc/bvbrc-0001.jsonl.gz:307`: genome 1280.3894, Staphylococcus aureus strain BSAR77, taxon 1280, assembly GCF_001199875.1, project PRJEB2655, unversioned GenBank accession CSNI00000000.
- `data/gold/projects.jsonl.gz:77943`: Staphylococcus aureus BSAR77, project Gp0129902, organism Go0122006, BioProject PRJEB2655. Go/Gp are related organism/project identifiers, not genomes. No target GOLD organism-project-analysis chain is established by this row.
- `data/catalog/ncbi_refseq-0000.jsonl.gz:36833` and `data/catalog/ncbi_genbank-0000.jsonl.gz:43934`: GCF_001199875.1 and GCA_001199875.1, strain BSAR77, taxon 1280, explicitly paired as identical. RefSeq carries PRJNA224116 and GenBank PRJEB2655; both retain WGS CSNI00000000.1.
- `data/catalog/gtdb_genomes-0004.jsonl.gz:25240`: RS_GCF_001199875.1, GenBank GCA_001199875.1, Staphylococcus aureus, taxon 1280, raw strain identifier BSAR77, PRJNA224116 and CSNI00000000.1.
- ATB SAMEA1033422, run ERR084604, ENA analysis ERZ3068767 is Staphylococcus aureus. Its FASTA is available and filters pass. Shared BioSample does not establish equivalence between its assembly and the NCBI assembly pair, and none of these rows supports target identity.

Full native row `data/catalog/ncbi_genbank-0066.jsonl.gz:19465` identifies
GCA_982539075.1 as Allobrachymonas sp., taxon 1936292, isolate
ERS15409406-megahit_003, BioSample SAMEA121992080, project PRJEB104944 and
WGS CEWQKM000000000.1. Only total/ungapped length, 1033422 bases, matches;
this supplies no target strain/deposit/genome relationship.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321408`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033422 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13505`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
