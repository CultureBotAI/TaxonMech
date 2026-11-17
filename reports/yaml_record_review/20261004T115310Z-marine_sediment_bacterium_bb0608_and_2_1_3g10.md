# YAML Record Review: marine sediment bacterium BB0608_AND_2.1_3G10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_2_1_3g10.yaml`
- Started UTC: 2026-10-04T11:49:21Z
- Finished UTC: 2026-10-04T11:53:10Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033499`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The full designation
BB0608_AND_2.1_3G10 distinguishes neighboring isolates, including 3G0.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_2_1_3g10.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_2_1_3g10.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221133 and scientific-name row 30441 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033499&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033499)
confirm identity and species rank; EFetch also confirms parent 49928 and
code 11. The root-first lineage matches root (1), cellular organisms
(131567), Bacteria (2) and unclassified Bacteria (49928). Species rank
does not prove valid nomenclatural publication or a finer placement.

## Evidence

Exact Nuccore search returned one entry, [JF750049.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750049.1),
UID 333384396, a 588-base partial 16S rRNA gene. Its source names strain
BB0608_AND_2.1_3G10, taxon 1033499, coastal marine sediment, Australia:
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
All six matches were inspected: target backbone, scope and scientific name,
two unrelated ATB rows and one GTDB contig-N50 collision. Recursive structured
SOURCE.json searches found no matches. These checks do not establish
universal absence.

- ATB row 64855 in `data/catalog/allthebacteria.tsv.xz` identifies SAMEA1033499, run ERR084547 and ENA analysis ERZ3068882 as Staphylococcus aureus in the scientific-name and both Sylph fields. Its BioSample suffix is not this taxon ID. FASTA is available; assembly/Sylph/HQ filters pass, with prior-HQ status T.
- ATB row 1021040 identifies SAMN02345238, run SRR1033499 and ENA analysis ERZ4069951. Its scientific name is Salmonella enterica subsp. enterica serovar Typhimurium; both Sylph species fields are Salmonella enterica. FASTA is available; assembly/Sylph/HQ filters pass, with prior-HQ status T. Only the run accession suffix matches the numeric search. Exclusion is identity, not quality.
- The full native row `data/catalog/gtdb_genomes-0015.jsonl.gz:1771` identifies GB_GCA_963810185.1 / GCA_963810185.1, uncultured Gemmatimonadales bacterium, taxon and species taxon 412054, isolate MFD02979.bin.2.2, BioSample SAMEA114813682, project PRJEB58634 and WGS CAWEMJ000000000.1. Only contig N50, 1033499, matches. This metagenome-derived assembly has 13 contigs and total/ungapped length 2835719; GTDB places it in SPDF01 sp963810185 within Gemmatimonadota. Neither this genome nor its classification belongs to the reviewed taxon.

No target strain/deposit/genome chain is supported by these unrelated rows.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321485`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033499 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13582`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
