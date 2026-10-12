# YAML Record Review: marine sediment bacterium BB0608_2216_8.1_2G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_8_1_2g0.yaml`
- Started UTC: 2026-10-04T10:09:52Z
- Finished UTC: 2026-10-04T10:10:59Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033448`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The full designation
BB0608_2216_8.1_2G0 distinguishes neighboring isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_8_1_2g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_8_1_2g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221082 and scientific-name row 30390 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033448&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033448)
confirm identity, species rank and parent 49928; EFetch confirms code 11.
The root-first lineage matches root (1), cellular organisms (131567),
Bacteria (2) and unclassified Bacteria (49928). Species rank does not prove
valid nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750311.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750311.1),
UID 333384658, a 539-base partial 16S rRNA gene. Its source names strain
BB0608_2216_8.1_2G0, taxon 1033448, coastal marine sediment, Australia:
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
All 26 matches were inspected: target backbone, scope and scientific name,
one unrelated ATB row and 22 BioProject collisions. Recursive structured
SOURCE.json searches found no matches. These checks do not establish
universal absence.

ATB SAMEA1033448, run ERR084728 and ENA analysis ERZ3068799 is
Staphylococcus aureus. Available FASTA and passing filters do not establish
target identity; the BioSample suffix is not this taxon ID.

All 22 other rows are in `data/catalog/ncbi_genbank-0056.jsonl.gz` and
match only PRJNA1033448. Structured native-object inspection checked
organism, taxon, strain, assembly, BioSample, WGS and paired-assembly fields.
No object contains BB0608 or the target taxon ID:

- Six Bifidobacterium pseudocatenulatum, taxon 28026: rows 10436, 10437, 10440, 11906, 11928 and 11929; strains Bp-Xy-13, Bp-Xy-2, Bp-Tc-1, Bp-Tc-10, Bp-St-4 and Bp-St-1.
- Six Bifidobacterium longum, taxon 216816: rows 11952, 11954, 11975, 11978, 11999 and 12001; strains YIT12812, YIT12811, YIT12762, LO-Cw098-B4, Blo-Em-3 and Blo-Em-1.
- Ten Bifidobacterium breve, taxon 1685: rows 10441, 12022, 12024, 12046, 12047, 12069, 12070, 12092, 12093 and 12113; strains Bb-Em-3, BR-Cw104-C2, BR-Cw104-A1, Bb-Em-7, Bb-Em-8, Bb-Em-6, Bb-Em-5, Bb-Em-2, Bb-Em-4 and Bb-Em-1.

Each row supplies an explicit identical RefSeq pair, but for its own
Bifidobacterium assembly. For example, Bp-Xy-13 is GCA_060677005.1 paired
with GCF_060677005.1, BioSample SAMN43055307 and WGS JBGGIB000000000.1.
The project suffix does not transfer those links to this target; none
supports a target strain/deposit/genome chain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321434`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033448 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13531`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
