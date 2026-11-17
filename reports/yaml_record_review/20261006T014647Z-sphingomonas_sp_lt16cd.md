# YAML Record Review: Sphingomonas sp. LT16CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sphingomonas_sp_lt16cd.yaml`
- Started UTC: 2026-10-06T01:44:49Z
- Finished UTC: 2026-10-06T01:46:47Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1034920`, Sphingomonas sp. LT16CD. It is a `SPECIES` in `BACTERIA`, parent `NCBITaxon:196159` (unclassified Sphingomonas), with ten root-first ancestors and genetic code 11. It has `EXACT` grounding, `SEEDED` mapping status, zero represented strains, one NCBITAXON NAME assertion from snapshot `2026-09-13`, and one inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strains, evidence, discussions and causal graphs are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/sphingomonas_sp_lt16cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/sphingomonas_sp_lt16cd.yaml --out /private/tmp/lt16cd-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the complete header-only TSV.
- Structured comparisons checked the full target backbone and scope rows, every ancestor ID/label/rank, unique PATHS entry, NCBI attestation and inline seed-event description. The backbone scan returned no children. These bounded comparisons are not full-corpus reproduction.
- Exact-ID scans of complete `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` returned no match. Seven supplementary source inventories likewise returned no exact target-ID match.
- Read complete live NCBI Taxonomy EFetch/Datasets responses, exact non-expanding Assembly/Nuccore responses, and full marker metadata, references and feature annotations. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. These full gates remain outside this bounded report-only review. Inline-event inspection is not history-schema validation.
- `just validate-products` and iModulonDB were not applicable without curator-added graph grounding, genes, regulators, modules or transcriptomic assertions. The record has no LPSN/GTDB assertion requiring an authority-page check.

## Identity and Grounding

The complete `data/raw/ncbitaxon_taxa.tsv:221748` row agrees with the YAML. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034920&retmode=xml) confirms exact ID/label, species rank, parent, bacterial division and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034920) confirms all ten ordered ancestor IDs, including root.

The lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Sphingomonadales, Sphingomonadaceae, Sphingomonas and unclassified Sphingomonas. All ancestor labels and ranks agree with the pinned backbone and dedicated taxonomy evidence. The marker's abbreviated GenBank lineage ends at Sphingomonas; it does not override the more complete taxonomy chain.

`data/taxa/PATHS.tsv:14219` uniquely maps the target to `sphingomonas_sp_lt16cd`; `curation/seed_scope.tsv:322050` gives its one-source inclusion rule. The complete scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31151` identifies the same target. No alternate target name is supplied by the inspected taxonomy evidence. NCBI species rank for this isolate-labelled taxon does not establish formal nomenclatural validity or equivalence with similarly named isolates.

## Evidence

Source ID, label, snapshot, count of one and NAME unit match the retained inventory. The YAML asserts identity and carried lineage, not a culture deposit, genome, phenotype, medium or mechanism. A source-name count must not be interpreted as a biological strain or genome count.

Exact Nuccore search returned UID 333496497. The complete [JF778666.1 record metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF778666.1) identify a 993-base partial 16S rRNA gene, partial at both ends, from Sphingomonas sp. LT16CD, with strain LT16CD, freshwater-lake isolation source and `taxon:1034920` qualifiers. The sole reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter's Bellerophon-screening comment was not independently tested. The metadata contain no culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID. A bare strain name plus a partial marker does not supply a culture-deposit/genome chain.

The inspected main text of [Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4) places JF778666 within its explicit JF778652-JF778667 submission range. That range and matching authors support association with the Lake Tawani(P), East Antarctica study, not LT16CD-specific physiology, growth optima or deposit identity. Supplements and figure images were not inspected.

Exact Assembly search returned zero with a phrase-not-found warning for `txid1034920[Organism:noexp]`. This bounded result does not exclude genomes under other identifiers or classifications.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered hidden/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. Searching the ID digits, full label and slug yielded 39 lines. Backbone and scope rows were read structurally, then all thirteen remaining native JSON objects and twenty-four complete header-aware AllTheBacteria rows were read. Reconciliation found no unread or truncated candidate.

Three rows identify LT16CD: backbone, scope and native scientific name. The remaining 36 are unrelated numeric collisions:

- Thirteen objects concern three Escherichia coli isolates. Each has BV-BRC, current GenBank, replaced GenBank and ATB sample records: PNUSAE019161 has `562.36441`, `GCA_003754325.1`/`.2`, `SAMN10349202` and `ERZ9092482`; PNUSAE017612 has `562.36553`, `GCA_003764205.1`/`.2`, `SAMN10349208` and `ERZ9092488`; PNUSAE019159 has `562.36573`, `GCA_003765665.1`/`.2`, `SAMN10349204` and `ERZ9092487`. All three GenBank records name taxon 562 and project `PRJNA218110`. The thirteenth object is GOLD project `Gp0386986`, organism `Go0502709`, explicitly naming E. coli PNUSAE019161 and sample `SAMN10349202`. GOLD project/organism identifiers are not genome identifiers.
- GenBank `GCA_027162365.1` is Staphylococcus aureus 8-320-043, taxon 1280, sample `SAMEA1034920`, project `PRJNA514245`. Its ATB sample row is also Staphylococcus aureus, analysis `ERZ3070316`, run `ERR086090`.
- BV-BRC `1773.20360` is Mycobacterium tuberculosis ERR1034920, taxon 1773. Its ATB run row names sample `SAMEA3558453`, analysis `ERZ3501211`, and Mycobacterium tuberculosis.
- Ten ATB rows name Shigella sonnei samples `SAMEA110349200` through `SAMEA110349209`; their sylph species field says Escherichia coli. Neither classification identifies Sphingomonas.
- Nine further ATB rows match runs `SRR10349201` through `SRR10349209`: one is E. coli sample `SAMN13117268`, analysis `ERZ25673581`; eight are Salmonella enterica samples `SAMN13117270`, `SAMN13117274`, `SAMN13117275`, `SAMN13117276`, `SAMN13117277`, `SAMN13117279`, `SAMN13117280` and `SAMN13117281`. Their full source rows supply no LT16CD association.

All candidate source-native objects were inspected, not merely snippets. Digit overlap in sample, run or accession strings is not identity evidence, and a shared sample alone would not establish genome equivalence.

A second ignored-inclusive search of the same ten roots for `JF778666|LT[ -]?16[ -]?CD` returned only the same three target rows. Exact-ID scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Within these bounded sources, no eligible missing strain/deposit/genome association was established. Zero represented strains describes inventory coverage, not the biological absence of the named isolate.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No required missing synonym, nomenclature, mapping, graph or evidence representation was established. Optional study-context enrichment is not required for a taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, carried lineage, provenance, source-count semantics and seeded status are supported. The marker and unrelated genome catalogs do not establish an omitted LT16CD genome or deposit link.

## Recommended Edits

None. Preserve the generated YAML and `SEEDED` status.

Future primary taxonomy corrections belong at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization belongs in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope policy belongs in `curation/seed_scope.tsv`. A study-context extension needs a maintained input and explicit target-specific evidence. Do not hand-edit generated YAML or count the marker as a genome.

## Follow-up Checks

No blocking follow-up remains. Future deposit/genome candidates require full source-native inspection and an explicit identity/linkage chain before authorized regeneration. Rerun focused schema/strict validation and the documented reproduction, provenance, history and relevant full gates after implementation. Recheck live taxonomy when refreshing the pinned dump. Independent sequence placement and chimera analysis were outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, existing worktree. The other session was reported closed; no additional worktree was created. This target review adds only this report, with diagnostics under `/private/tmp`. Records, inventories, scope, history, statuses, prior reports and generated pages were preserved. No commits, GitHub mutations, external contacts or paid research occurred. Eukaryota was left untouched.
