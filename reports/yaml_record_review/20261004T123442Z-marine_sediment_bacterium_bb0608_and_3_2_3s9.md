# YAML Record Review: marine sediment bacterium BB0608_AND_3.2_3S9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_3_2_3s9.yaml`
- Started UTC: 2026-10-04T12:33:46Z
- Finished UTC: 2026-10-04T12:34:42Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033520`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. BB0608_AND_3.2_3S9 is
distinct from neighboring isolates, including AND_3.2_3S10.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_3_2_3s9.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_3_2_3s9.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221154 and scientific-name row 30462 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033520&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033520)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
The root-first lineage matches root (1), cellular organisms (131567),
Bacteria (2) and unclassified Bacteria (49928). Species rank does not prove
valid nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750071.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750071.1),
UID 333384418, a 325-base partial 16S rRNA gene. Its source names strain
BB0608_AND_3.2_3S9, taxon 1033520, coastal marine sediment, Australia:
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
All five matches were inspected: target backbone, scope and scientific
name, and two unrelated ATB rows. Recursive structured SOURCE.json
searches found no matches. These checks do not establish universal absence.

- ATB row 64876 in `data/catalog/allthebacteria.tsv.xz` identifies SAMEA1033520, run ERR068166 and ENA analysis ERZ3068909. Its scientific name is Streptococcus pneumoniae; both Sylph species fields are unknown. FASTA is available, the assembly filter passes, prior-HQ status is F, the Sylph filter is SYLPH_RESULTS_FAIL, and the HQ filter is CHECKM2_MAX_CONTAM,SYLPH_RESULTS_FAIL. Its BioSample suffix is not this taxon ID. Non-HQ status alone does not disqualify an available FASTA; exclusion is identity, not quality.
- ATB row 1021310 identifies SAMN02345512, run SRR1033520 and ENA analysis ERZ4070408. Its scientific name is Salmonella enterica subsp. enterica; both Sylph species fields are Salmonella enterica. FASTA is available; assembly/Sylph/HQ filters pass, with prior-HQ status T. Only the run suffix matches the numeric search.

No target strain/deposit/genome chain is supported by these unrelated rows.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321506`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033520 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13603`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
