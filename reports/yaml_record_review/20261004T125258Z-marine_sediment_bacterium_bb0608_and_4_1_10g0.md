# YAML Record Review: marine sediment bacterium BB0608_AND_4.1_10G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_1_10g0.yaml`
- Started UTC: 2026-10-04T12:51:59Z
- Finished UTC: 2026-10-04T12:52:58Z
- Verdict: pass

## Target

Full generated `TaxonRecord` read: `NCBITaxon:1033528`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. BB0608_AND_4.1_10G0
distinguishes this record from neighboring AND_4.1 and AND_3.2 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_1_10g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_1_10g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221162 and scientific-name row 30470 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033528&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033528)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank alone does not establish
valid nomenclatural publication or finer placement.

## Evidence

Exact Nuccore search returned one sequence, [JF750074.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750074.1),
UID 333384421, a 248-base partial 16S rRNA gene. Its source explicitly names
strain BB0608_AND_4.1_10G0, taxon 1033528, coastal marine sediment,
Australia: Gulf of Carpentaria and June 2008 collection. The qualifier is
strain, not clone or environmental sample. This short locus is not an
assembly, culture deposit or independent taxonomic classification.

Both references were read: Cornall, Beyer, Streten-Joyce, McGuinness, Parry
and Gibb's marine-sediment cryopreservation study marked unpublished, and
Cornall's direct submission dated 2011-04-01. Neither supplies a DOI or
PMID. Full manuscript text was not obtained; no phenotype was inferred
from the title. Exact Assembly search returned zero with phrase-not-found
and no-items warnings. The NAME attestation and 2026-09-13 snapshot match
the inventory; the count is not independent experiments.

## Completeness

Complete exact-ID scans found no rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional slots reflect
bounded coverage; zero inventoried strains does not mean never cultured.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
numeric ID and complete label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All six matches were inspected: target scope, backbone and scientific name,
two unrelated ATB rows and one unrelated GenBank row. Recursive structured
SOURCE.json scans found no matches. These checks do not prove universal absence.

- ATB row 64884 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033528, run ERR068087, analysis ERZ3068928; scientific name and both Sylph fields are Streptococcus pneumoniae. Only the BioSample suffix matches.
- ATB row 1013292: SAMN01907439, run SRR1033528, analysis ERZ3639960; scientific name is Salmonella enterica subsp. enterica serovar Tennessee and both Sylph fields are Salmonella enterica. Only the run suffix matches.
- Full native row 38387 in `data/catalog/ncbi_genbank-0040.jsonl.gz`: GCA_044359035.1, taxon/species 1869227, organism bacterium, isolate ME2014-09-13_3300035665_group5_bin114, SAMN43898781, PRJNA1158976, JBIKMX000000000.1. It is metagenome-derived, 88 contigs, with no RefSeq pair. Only total and ungapped genome lengths, both 1033528, match the numeric search. The unrelated row's PMID 38370794 was not retrieved or used as target evidence.

Both ATB FASTAs are available, assembly/Sylph/HQ filters PASS, prior-HQ T;
column meanings were rechecked against the actual header. Exclusions are
identity-based, not quality-based. None supplies a target strain/deposit/genome chain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321514`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033528 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13611`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.
