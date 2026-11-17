# YAML Record Review: marine sediment bacterium BB0608_2216_5.2_12G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_5_2_12g0.yaml`
- Started UTC: 2026-10-04T08:46:49Z
- Finished UTC: 2026-10-04T08:47:37Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033405`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The complete designation
BB0608_2216_5.2_12G0 distinguishes neighboring isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_5_2_12g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_5_2_12g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221039 and scientific-name row 30347 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033405&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033405)
confirm the identifier, label, species rank and parent 49928; EFetch also
confirms code 11. The root-first lineage matches root (1), cellular organisms
(131567), Bacteria (2) and unclassified Bacteria (49928). Species rank does
not establish valid nomenclatural publication or a finer placement.

## Evidence

Exact Nuccore search returned one entry, [JF750268.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750268.1),
UID 333384615, a 472-base partial 16S rRNA gene. The source names strain
BB0608_2216_5.2_12G0 and taxon 1033405, coastal marine sediment, Australia:
Gulf of Carpentaria, collected June 2008. It uses a strain qualifier, not a
clone or environmental-sample qualifier. This locus is neither a genome nor
an independent classification or culture-deposit link.

Both sequence references were inspected: the Cornall, Beyer, Streten-Joyce,
McGuinness, Parry and Gibb marine-sediment cryopreservation study marked
unpublished, and Cornall's direct submission dated 2011-04-01. Neither
supplies a DOI or PMID. Full manuscript text was not obtained; no phenotype
was inferred from the title. Exact Assembly search returned zero with
phrase-not-found and no-items warnings. The NAME attestation, source label,
count and 2026-09-13 snapshot agree with the inventory, not an experiment count.

## Completeness

Complete exact-ID scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and
BactoTraits inventories found no rows. Empty optional slots reflect bounded
source coverage; zero inventoried strains does not mean never cultured.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
numeric ID and complete label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All six matches were inspected: target backbone, scope and scientific name,
and three unrelated source rows. Recursive structured SOURCE.json searches
found no matches. These checks do not establish universal absence.

- ATB SAMEA1033405, run ERR084555, ENA analysis ERZ3068748 is Staphylococcus aureus. Available FASTA and passing filters do not establish target identity.
- Full native rows `data/catalog/ncbi_genbank-0038.jsonl.gz:6426` and `data/catalog/gtdb_genomes-0006.jsonl.gz:17713` identify GCA_041660885.1 / GB_GCA_041660885.1 as Patescibacteria group bacterium, taxon 2052139, isolate SO_2017_GW1_252, BioSample SAMN39904824, project PRJNA823399 and WGS JBAZVM000000000.1. GTDB calls it JBAZVM01 sp041660885. The matched total/ungapped length is 1033405 bases; this is not a target identity or strain/deposit/genome relationship.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321391`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033405 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13488`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
