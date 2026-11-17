# YAML Record Review: marine sediment bacterium BB0608_AND_4.1_1G10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_1_1g10.yaml`
- Started UTC: 2026-10-04T12:55:21Z
- Finished UTC: 2026-10-04T12:56:14Z
- Verdict: pass

## Target

Full generated `TaxonRecord` read: `NCBITaxon:1033530`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The complete designation
BB0608_AND_4.1_1G10 distinguishes AND_4.1_1G0 and other adjacent isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_1_1g10.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_1_1g10.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221164 and scientific-name row 30472 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033530&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033530)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not establish valid
nomenclatural publication or finer classification.

## Evidence

Exact Nuccore search returned one sequence, [JF750088.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750088.1),
UID 333384435, a 264-base partial 16S rRNA gene. Source qualifiers explicitly
name strain BB0608_AND_4.1_1G10, taxon 1033530, coastal marine sediment,
Australia: Gulf of Carpentaria and June 2008 collection. The qualifier is
strain, not clone or environmental sample. This short locus is not a genome,
culture deposit or independent taxonomic classification.

Both references were read: Cornall, Beyer, Streten-Joyce, McGuinness, Parry
and Gibb's marine-sediment cryopreservation study marked unpublished, and
Cornall's direct submission dated 2011-04-01. Neither supplies a DOI or
PMID. Full manuscript text was not obtained; no phenotype was inferred
from the title. Exact Assembly search returned zero with phrase-not-found
and no-items warnings. The NAME attestation and 2026-09-13 snapshot match
the inventory; the count is not independent experiments.

## Completeness

Complete exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional slots reflect
bounded coverage; zero inventoried strains does not mean never cultured.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
numeric ID and complete label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All five matches were inspected: target scope, backbone and scientific
name, plus two unrelated ATB rows. Recursive structured SOURCE.json scans
found no matches. These checks do not establish universal absence.

- ATB row 64886 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033530, run ERR064763, analysis ERZ3068919; scientific name and both Sylph fields are Streptococcus pneumoniae. Only the BioSample suffix matches this taxon's number.
- ATB row 1021264: SAMN02345466, run SRR1033530, analysis ERZ4070340; scientific name and both Sylph fields are Salmonella enterica. Only the run suffix matches.

Both FASTAs are available, assembly/Sylph/HQ filters PASS, prior-HQ T.
Exclusions are identity-based, not quality-based. Neither unrelated row
supports a target strain/deposit/genome chain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321516`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033530 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13613`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.
