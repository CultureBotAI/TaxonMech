# YAML Record Review: Juan de Fuca filamentous bacterium

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/juan_de_fuca_filamentous_bacterium.yaml`
- Started UTC: 2026-10-10T00:08:07Z
- Finished UTC: 2026-10-10T00:10:24Z
- Verdict: pass

## Target

The entire 58-line generated `TaxonRecord` was read. `NCBITaxon:1037347` denotes Juan de Fuca filamentous bacterium, rank `ISOLATE`, domain `BACTERIA`, parent `NCBITaxon:991901` (Candidatus Marithrix sessilis), genetic code 11, grounding `EXACT`, status `SEEDED`.

It contains ten ancestors, one NCBI exact synonym, zero BacDive strains, one NCBITAXON name attestation and the seed event. This is the JdF isolate taxon, not the parent species, Escanaba Trough isolate or White Point isolate.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/juan_de_fuca_filamentous_bacterium.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/juan_de_fuca_filamentous_bacterium.yaml --out /private/tmp/taxonmech-juan-de-fuca-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons matched identity, complete pinned lineage, synonym, genetic code, source attestation, scope/index entries and seed-event text. Complete backbone scanning found no immediate child. Exact own-ID scans found no type-material, merged-ID or dropped row.
- Native NCBI name rows and all initial search candidates were read completely; additional numeric-collision candidates were checked by identity/matched fields or complete TSV rows. Live NCBI EFetch and Datasets independently agreed with the taxonomy.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. These focused comparisons are not a corpus reproduction result. `just validate-products` has no applicable causal-graph nodes.
- NCBI browser retrieval returned a tool error; taxonomy APIs succeeded. The PMC paper page presented a browser challenge, so the study abstract/bibliography were retrieved through NCBI EFetch. No full-paper experimental audit or genome-sequence comparison is claimed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222715` agrees with [live NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037347&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037347): isolate 1037347, exact label, parent 991901 and code 11.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Thiotrichales, Thiotrichaceae, Candidatus Marithrix and Candidatus Marithrix sessilis. Every label, identifier and rank matches the pinned backbone. Live EFetch supplies the same chain below root; Datasets includes root ID 1.

`data/catalog/ncbi_names-0005.jsonl.gz:32323` records Candidatus Marithrix sessilis (JdF) as an NCBI synonym; row 32324 supplies the scientific name. The exact synonym retains the isolate qualifier and is not collapsed to the species name.

The full parent and sibling backbone rows distinguish species 991901 from isolates 1037348 (Escanaba Trough, ET) and 1037349 (White Point, WP). The YAML's explicit infraspecific rank is eligible under repository scope rules and does not need promotion to species.

## Evidence

The sole attestation is `NCBITAXON`, source ID 1037347, count 1, unit `NAME`, snapshot 2026-09-13. Its label, count and note match the backbone. This is source identity evidence, not an experimental phenotype or a count of cultured strains.

Live [AY883933 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AY883933) identifies AY883933.1, a 1,461-base partial 16S sequence, with organism Juan de Fuca filamentous bacterium and explicit `taxon:1037347`. The source qualifier specifies the Endeavour Segment of the Juan de Fuca Ridge. The marker supports the isolate identity but is not an assembly or culture-deposit identifier. It is contextual evidence inspected during this review, not an accession asserted by this YAML.

The marker's reference matches [Kalanetra and Nelson, PMID 24391244](https://pubmed.ncbi.nlm.nih.gov/24391244/), DOI 10.1007/s00227-009-1362-3. The complete retrieved abstract distinguishes Juan de Fuca and Escanaba collections and compares them with White Point material. Its measurements and ecological results have collection-specific scope; no phenotype was transferred into the record.

The inspected [LPSN species authority](https://lpsn.dsmz.de/species/marithrix-sessilis), name 800539, lists JdF as nomenclatural type and AY883933 as marker. It concerns the parent Candidatus species and distinguishes not-validly-published status from pro-valid publication. It also places the genus in Beggiatoales/Beggiatoaceae, unlike NCBI's Thiotrichales/Thiotrichaceae. This is a preserved cross-source classification difference, not permission to rewrite the carried NCBI lineage or add a species-equivalence xref to the isolate.

The retrieved abstract of [Salman et al., PMID 21498017](https://pubmed.ncbi.nlm.nih.gov/21498017/), DOI 10.1016/j.syapm.2011.02.001, supports the historical classification context using 16S/ITS data and morphology. It does not establish a cultured deposit or an isolate genome. These papers are supplementary identity context; the seeded record relies on its explicit NCBI attestation.

## Completeness

An ignored-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded taxon ID 1037347, spaced/slug spellings of the label and Marithrix sessilis. Fourteen candidate lines consisted of seven NCBI name rows, four backbone rows, two scope rows and one unrelated assembly. All were read in full.

The unrelated assembly is `data/catalog/ncbi_genbank-0006.jsonl.gz:21028`, GCA_007483825.1, Salmonella enterica taxon 28901, with strain FDA1037347-C001-001. Digits inside that strain designation do not identify taxon 1037347.

A follow-up ignored-inclusive search over the same roots for AY883933 and bounded LPSN number 800539 returned three numeric collisions: E. coli isolate XH800539, an ATB E. coli run SRR800539, and SI-DP 800539 on a Porodaedalea pini source record. None supplies evidence for this isolate. No Eukaryota YAML was opened.

Complete structured scans of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits taxon inventories found no direct own-ID row. With no backbone children, there is also no descendant BacDive inventory to aggregate. Thus `strain_count: 0` means zero inventoried BacDive strains, not that the isolate has no literature or sequence record.

Five SOURCE.json files were parsed separately with no target match. Gitignore-independent filename searches found this YAML and no prior target report; history filename checks found no target-specific filename. These are bounded repository results, not global database absence claims.

No supported culture-deposit join, own genome assertion or omitted required representation was identified. A marker sequence, a species nomenclatural type label and an ecological sample are not substitutes for eligible BacDive/StrainInfo deposit evidence. Optional definition, record-level citations and causal graphs are not required for this seeded record.

iModulonDB gene/module searching was not applicable: the YAML asserts no gene, regulator, pathway or transcriptomics result. The adapter was not run; no dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, parentage, provenance, synonym scope, count semantics and seed status are consistent. Cross-source family/order differences and unavailable full-paper access are recorded without silently resolving them.

## Recommended Edits

None required. Preserve the isolate identity, JdF qualifier, NCBI lineage and zero BacDive count. Do not convert the marker into a genome link or the parent LPSN species into isolate equivalence.

A future authorized source or harmonization correction belongs in maintained extraction inputs/policies, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, as appropriate, followed by documented extraction/seeding. Do not hand-edit generated YAML. No such correction is established by this review.

## Follow-up Checks

Future enrichment should retain the exact isolate, accession and study/collection scope. Recheck any proposed culture-deposit or assembly link at its primary source before adding it.

After an authorized source refresh, rerun schema, strict and history validation and the documented corpus reproduction/QC gates. Full-paper access could strengthen experimental context, but no unverified experimental assertion is needed for the present verdict.

## Additional Notes

- SHA-256: `ac968bb0e826400efa6b61be1cf4f18b268691d0d087b270e6f4c4b9d38f6a0a`.
- `data/taxa/PATHS.tsv:15261` and `curation/seed_scope.tsv:322941` uniquely identify the target. The seed timestamp remains 2026-09-13T17:54:04Z; the one-source scope reason and seed wording match.
- Source context rows include parent backbone 206576, siblings 222716-222717, parent native names 14247-14249 and sibling synonym rows 32325 and 32327 in NCBI names shard 0005. These supporting rows do not constitute reviews of the sibling YAMLs.
- Read-only review against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new review report was added for this target. No YAML, history, schema, maintained source, page, branch, worktree or GitHub state was changed, and no review-status promotion occurred.
