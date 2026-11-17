# YAML Record Review: marine sediment bacterium BB0608_2216_7.1_19G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_7_1_19g0.yaml`
- Started UTC: 2026-10-04T09:33:52Z
- Finished UTC: 2026-10-04T09:35:01Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033429`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The full designation
BB0608_2216_7.1_19G0 distinguishes neighboring isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_7_1_19g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_7_1_19g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221063 and scientific-name row 30371 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033429&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033429)
confirm identity, species rank and parent 49928; EFetch confirms code 11.
The root-first lineage matches root (1), cellular organisms (131567),
Bacteria (2) and unclassified Bacteria (49928). Species rank does not prove
valid nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750292.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750292.1),
UID 333384639, a 460-base partial 16S rRNA gene. Its source names strain
BB0608_2216_7.1_19G0, taxon 1033429, coastal marine sediment, Australia:
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
All 40 matches were inspected: target backbone, scope and scientific name,
one unrelated ATB row and 36 BioProject collisions. Recursive structured
SOURCE.json searches found no matches. These checks do not establish
universal absence.

ATB SAMEA1033429, run ERR084556 and ENA analysis ERZ3068782 is
Staphylococcus aureus. Available FASTA and passing filters do not establish
target identity. The numeric BioSample suffix is not this NCBI taxon ID.

The other 36 rows match only BioProject PRJNA1033429: 18 BV-BRC and 18
GenBank entries with different taxon IDs and BCCIQ strain designations.
Structured native-object inspection checked organism, taxon, strain,
BioSample, project, assembly and supplied WGS/paired-assembly fields.
No object contains the BB0608 designation. Source locations:

- `data/bvbrc/bvbrc-0028.jsonl.gz`: rows 15413-15415 and 15417-15418; five Burkholderia cenocepacia, taxon 95486.
- `data/bvbrc/bvbrc-0015.jsonl.gz:41753`: Burkholderia gladioli BCCIQ06A, taxon 28095.
- `data/bvbrc/bvbrc-0027.jsonl.gz`: rows 44255-44260 and 44270; seven Burkholderia multivorans, taxon 87883.
- `data/bvbrc/bvbrc-0018.jsonl.gz`: rows 45645-45649; five Burkholderia sp. entries, each with explicit taxon_id 3090833. Genome IDs 3090833.3 through 3090837.3 are kept distinct from that field.
- `data/catalog/ncbi_genbank-0032.jsonl.gz`: rows 36847-36863; the five taxon-3090833 strains are named Burkholderia anthinoferrum here. `data/catalog/ncbi_genbank-0035.jsonl.gz:31779` supplies the eighteenth entry, B. multivorans BCCIQ03A, GCA_038067055.1, SAMN38033602, JBBULX000000000.1, with explicit identical pair GCF_038067055.1.

For example, BCCIQ07E maps within those sources to BV-BRC 95486.1028,
GCA_035064605.1, SAMN38033613 and JAWRLI000000000.1; GenBank explicitly
reports an identical GCF_035064605.1 pair. Such source-supported links
remain evidence for those Burkholderia strains, not this target. Neither
project suffixes nor sample suffixes establish target strain/genome links.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321415`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033429 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13512`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
