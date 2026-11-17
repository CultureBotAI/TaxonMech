# YAML Record Review: White Point filamentous bacterium

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/white_point_filamentous_bacterium.yaml`
- Started UTC: 2026-10-10T00:13:46Z
- Finished UTC: 2026-10-10T00:15:16Z
- Verdict: pass

## Target

The entire 58-line generated `TaxonRecord` was read. `NCBITaxon:1037349` denotes White Point filamentous bacterium, rank `ISOLATE`, domain `BACTERIA`, parent `NCBITaxon:991901` (Candidatus Marithrix sessilis), genetic code 11, grounding `EXACT`, status `SEEDED`.

It carries ten ancestors, one WP-qualified NCBI exact synonym, zero BacDive strains, one NCBITAXON name attestation and the seed event. This review concerns the White Point isolate, not the parent species or its Juan de Fuca and Escanaba Trough siblings.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/white_point_filamentous_bacterium.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/white_point_filamentous_bacterium.yaml --out /private/tmp/taxonmech-white-point-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons matched identity, complete pinned lineage, synonym, genetic code, source attestation, scope/index entries and seed text. Complete backbone scanning found no child. Exact own-ID scans found no type-material, merged-ID or dropped row.
- Every one of the 14 source-search candidate lines was read completely. Live NCBI taxonomy APIs and marker metadata were inspected independently of the generated inventory. The relevant primary-study abstract and bibliography were retrieved.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused checks are not full-corpus reproducibility evidence. `just validate-products` has no applicable causal-graph nodes.
- The NCBI taxonomy browser returned a tool access error; EFetch and Datasets succeeded. The full experimental paper was not audited and no genome-sequence comparison was performed. The verdict does not depend on uninspected experimental claims.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222717` matches [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037349&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037349): White Point filamentous bacterium, isolate 1037349, parent 991901, genetic code 11.

The root-first chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Thiotrichales, Thiotrichaceae, Candidatus Marithrix and Candidatus Marithrix sessilis. All identifiers, labels and ranks agree with the pinned backbone; live taxonomy independently confirms the chain, including root ID 1 in Datasets.

`data/catalog/ncbi_names-0005.jsonl.gz:32327` supplies Candidatus Marithrix sessilis (WP) as a synonym and row 32328 supplies the scientific name. The exact synonym keeps WP, rather than substituting the broader unqualified species name. The source rows also distinguish Juan de Fuca/1037347 and Escanaba Trough/1037348 from this target. An isolate under a species is eligible under repository scope rules.

## Evidence

The sole source attestation is NCBITAXON, ID 1037349, one `NAME`, snapshot 2026-09-13. Its label and provenance match the backbone. This is a taxon identity assertion, not cultivation, genome or phenotype evidence.

Live [AY496953 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AY496953) identifies AY496953.1, a 1,463-base partial 16S sequence, with organism White Point filamentous bacterium, isolate White Point and explicit `taxon:1037349`. Its source specifies an intertidal hydrothermal sulfidic vent at White Point, California. These qualifiers support the target identity without turning a marker into a genome or culture-deposit identifier. The accession is additional review context, not a field asserted by the YAML.

The marker reference matches [PMID 15574952](https://pubmed.ncbi.nlm.nih.gov/15574952/), Kalanetra, Huston and Nelson, DOI 10.1128/AEM.70.12.7487-7496.2004. The complete abstract and bibliography were inspected through both PubMed and EFetch. It connects the 16S sequence to wider White Point filaments through FISH and distinguishes observations about nitrate storage from possible oxygen-storage or buoyancy functions. The latter are hypotheses, not demonstrated mechanisms. None of these experimental or proposed-function claims is asserted in the seeded record.

The inspected [parent LPSN species](https://lpsn.dsmz.de/species/marithrix-sessilis) names JdF, not WP, as type. Its alternative classification must not replace the carried NCBI lineage.

The prior-in-turn primary classification abstract, [PMID 21498017](https://pubmed.ncbi.nlm.nih.gov/21498017/), DOI 10.1016/j.syapm.2011.02.001, supplies historical context only. Likewise, Juan de Fuca/AY883933 and Escanaba/AY883934 are separate accession-to-isolate relationships, not aliases of AY496953. Parent-species membership cannot transfer a sibling's type, deposit, genome or ecological result.

## Completeness

An ignored-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It used bounded ID 1037349, spaced/slug variants of the target label, Marithrix sessilis and AY496953.

The 14 matches consisted of seven native NCBI name rows, four backbone rows, two scope rows and one unrelated GenBank assembly. Every candidate was read in full. `data/catalog/ncbi_genbank-0051.jsonl.gz:19521` is GCA_055615235.1, Streptococcus pneumoniae, taxon 1313, BioSample SAMEA120831703. Its isolate field happens to be 1037349; that number is not an NCBI taxonomy match. It must not be attached to White Point.

Separate complete structured scans found no direct own-ID BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. The complete backbone contains no child to contribute descendant strains. The zero strain count therefore accurately denotes zero inventoried BacDive entries, not absence of a biological isolate, literature or sequence.

Five SOURCE.json files were parsed without a target match. Gitignore-independent filename searching found this YAML and no prior target report; history filename inspection found no target-specific filename. No own marker-bearing or eligible genome/deposit evidence was found within the searched source roots. These are bounded repository results, not global database-absence claims.

No required representation is demonstrably missing. Optional definition, record-level evidence, nomenclature, mappings and causal graph should not be invented from contextual literature. iModulonDB searches were not applicable because the YAML asserts no gene, regulator, pathway or transcriptomics result; no adapter run or dataset-absence claim is made. No Eukaryota YAML was opened.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and source scope. Identity, WP-qualified synonym, lineage, provenance, count semantics and seed status agree with the inspected sources. Unrun corpus gates remain limitations.

## Recommended Edits

None required. Keep the exact isolate distinct from its species and siblings. Do not attach the numeric-collision assembly, promote the marker to a genome, transfer JdF type status, or turn suggested vacuole functions into established mechanisms.

Future authorized source/harmonization corrections belong in maintained inputs or `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and `curation/seed_scope.tsv`, as appropriate, followed by documented extraction/seeding. No such correction is established here, and generated YAML must not be hand-edited.

## Follow-up Checks

Future literature enrichment should preserve White Point collection scope and distinguish measurements from hypotheses. Any deposit or assembly proposal requires its own primary identity evidence, not a shared taxon name or numerical substring.

After an authorized source refresh, repeat schema/strict/history checks and the documented full-corpus reproduction/QC gates. A full experimental-paper review would be needed before introducing detailed biological claims.

## Additional Notes

- SHA-256: `f4b3084b3eb291caef82f558322b912d0d3c5c105d44640d76cea694d02e363e`.
- `data/taxa/PATHS.tsv:15263` and `curation/seed_scope.tsv:322943` uniquely identify the target. The seed remains 2026-09-13T17:54:04Z with its matching one-source scope reason.
- Supporting rows include parent backbone 206576, sibling backbone rows 222715-222716, parent native names 14247-14249 and sibling synonym rows 32323/32325 in NCBI names shard 0005.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. This is the only new report for this target. No YAML, source input, schema, history, page, branch, worktree or GitHub state was changed. All ten worktrees were preserved and no status promotion occurred.
