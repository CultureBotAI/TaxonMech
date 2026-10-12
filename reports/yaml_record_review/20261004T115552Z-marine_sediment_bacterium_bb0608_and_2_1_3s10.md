# YAML Record Review: marine sediment bacterium BB0608_AND_2.1_3S10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_2_1_3s10.yaml`
- Started UTC: 2026-10-04T11:54:58Z
- Finished UTC: 2026-10-04T11:55:52Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033500`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. BB0608_AND_2.1_3S10 is
distinct from the neighboring 3G10 and other AND_2.1 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_2_1_3s10.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_2_1_3s10.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221134 and scientific-name row 30442 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033500&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033500)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
The root-first lineage matches root (1), cellular organisms (131567),
Bacteria (2) and unclassified Bacteria (49928). Species rank does not prove
valid nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750050.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750050.1),
UID 333384397, a 491-base partial 16S rRNA gene. Its source names strain
BB0608_AND_2.1_3S10, taxon 1033500, coastal marine sediment, Australia:
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
All seven matches were inspected: target backbone, scope and scientific
name, two unrelated ATB rows and two native genome-length collisions.
Recursive structured SOURCE.json searches found no matches. These checks
do not establish universal absence.

- ATB row 64856 in `data/catalog/allthebacteria.tsv.xz` identifies SAMEA1033500, run ERR068165 and ENA analysis ERZ3068881. The scientific name is Streptococcus pneumoniae; both Sylph species fields are unknown. FASTA is available, the assembly filter passes, prior-HQ status is F, and Sylph/HQ filters are SYLPH_RESULTS_FAIL. Non-HQ status alone does not disqualify available FASTA; exclusion is identity, not quality. Its BioSample suffix is not this taxon ID.
- ATB row 1013300 identifies SAMN01907447, run SRR1033500 and ENA analysis ERZ3639978. Its scientific name is Salmonella enterica subsp. enterica serovar Montevideo; both Sylph species fields are Salmonella enterica. FASTA is available; assembly/Sylph/HQ filters pass, with prior-HQ status T. Only the run suffix matches the numeric search.
- Full native rows `data/catalog/gtdb_genomes-0009.jsonl.gz:36341` and `data/catalog/ncbi_genbank-0045.jsonl.gz:32018` identify GB_GCA_049459265.1 / GCA_049459265.1, Methylophilaceae bacterium, taxon and species taxon 2030816, isolate Tbon_V8_S27_100percent_par_Tbon_V8_S27_metabat.10_sub, BioSample SAMN45206811, project PRJNA1171802 and WGS JBMUDG000000000.1. Only total/ungapped length 1033500 matches. The metagenome-derived assembly has 132 contigs and no paired RefSeq assembly. GTDB places it in BACL14 sp017852315; neither this genome nor its classification belongs to the reviewed taxon.

No target strain/deposit/genome chain is supported by these unrelated rows.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321486`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033500 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13583`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
