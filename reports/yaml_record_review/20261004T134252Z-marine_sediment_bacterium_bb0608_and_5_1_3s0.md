# YAML Record Review: marine sediment bacterium BB0608_AND_5.1_3S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_5_1_3s0.yaml`
- Started UTC: 2026-10-04T13:42:01Z
- Finished UTC: 2026-10-04T13:42:52Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033554`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. BB0608_AND_5.1_3S0
distinguishes this record from neighboring AND_5.1 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_5_1_3s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_5_1_3s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221188 and scientific-name row 30496 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033554&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033554)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not establish valid
nomenclatural publication or finer taxonomic placement.

## Evidence

Exact Nuccore search returned one sequence, [JF750100.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750100.1),
UID 333384447, a 472-base partial 16S rRNA gene. Source qualifiers name
strain BB0608_AND_5.1_3S0, taxon 1033554, coastal marine sediment,
Australia: Gulf of Carpentaria and June 2008 collection. The qualifier is
strain, not clone or environmental sample. This locus is not a genome,
culture deposit or independent taxonomic classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither supplies a DOI
or PMID. Full manuscript text was not obtained; no phenotype was inferred
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

- ATB row 64910 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033554, run ERR068141, analysis ERZ3068952; scientific name Streptococcus pneumoniae, both Sylph names unknown. FASTA available, assembly filter PASS, prior-HQ F, Sylph/HQ filters SYLPH_RESULTS_FAIL. Only the BioSample suffix matches.
- ATB row 1020323: SAMN02335409, run SRR1033554, analysis ERZ4068978; scientific name Salmonella enterica subsp. enterica serovar Javiana, earlier Sylph name Salmonella enterica, current Sylph name unknown. FASTA available, assembly filter PASS, prior-HQ T, current Sylph/HQ filters SYLPH_RESULTS_FAIL. Only the run suffix matches.

Exclusions are identity-based, not quality-based. Non-HQ or failed Sylph
classification alone does not make an available FASTA ineligible. Neither
row supports a target strain/deposit/genome chain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321540`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033554 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13637`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.

