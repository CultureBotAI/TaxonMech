# YAML Record Review: Duganella sp. LT17CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_lt17cd.yaml`
- Started UTC: 2026-10-06T01:19:29Z
- Finished UTC: 2026-10-06T01:21:10Z
- Verdict: pass

## Target

Read the entire 56-line generated `TaxonRecord`: `NCBITaxon:1034914`, Duganella sp. LT17CD, `SPECIES`, `BACTERIA`, parent `NCBITaxon:2636909` (unclassified Duganella). The record contains eleven root-first lineage entries, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBITAXON NAME attestation at snapshot `2026-09-13`, and one `SEEDED_FROM_SOURCES` event dated `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strains, evidence objects, discussions and causal graph are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_lt17cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_lt17cd.yaml --out /private/tmp/lt17cd-validation.tsv`: exit 0, one file scanned, zero ERROR rows. The complete TSV was read and contains only its header.
- Structured source comparisons verified every target backbone field and ancestor ID/label/rank, the unique PATHS mapping, scope row, source attestation and inline event description. The backbone scan returned no children. These checks are bounded comparisons, not corpus reproduction.
- Exact-ID scans of the complete `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` returned no matching row. Seven supplementary source inventories returned no exact target-ID match.
- Read complete live NCBI Taxonomy EFetch and Datasets responses, exact non-expanding Assembly/Nuccore search results, and complete metadata, references and feature annotations of the sole nucleotide hit. No sequence-base reanalysis was performed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. This report-only review does not claim those full gates. Inline-event inspection is not a history-schema validation run.
- `just validate-products` and iModulonDB were not applicable: no curator-added graph grounding, gene, regulator, expression module or transcriptomic claim is asserted. No target LPSN or GTDB assertion required an authority-page check.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221742` agrees with the YAML. The inspected [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034914&retmode=xml) confirms exact ID/label, species rank, parent, bacterial division and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034914) confirms the target and the complete ordered ancestor-ID chain, including root.

The eleven ancestors are root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group, Duganella and unclassified Duganella. All labels and ranks agree with the pinned inventory and inspected taxonomy evidence. Telluria group (`NCBITaxon:2895353`) is a no-rank ancestor, not a target synonym or alternate genus assertion. GenBank's abbreviated lineage omits the final unclassified intermediate; the dedicated taxonomy endpoints confirm that parent.

`data/taxa/PATHS.tsv:14212` uniquely assigns the ID to `duganella_sp_lt17cd`; `curation/seed_scope.tsv:322044` gives the one-source NCBI inclusion rule. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31145` identifies the same taxon. No alternate target name is supplied by the inspected taxonomy evidence. NCBI species rank for this provisional isolate-labelled entity does not establish formal nomenclatural validity or equivalence with another LT-labelled isolate.

## Evidence

The record's NCBI name/lineage claim is supported at the stated snapshot. Its exact source ID, label, count of one and NAME unit agree with the inventory; this count is not a strain or genome total. No phenotype, growth condition, ecological mechanism, type strain or genome claim is present in the YAML.

The exact Nuccore query returned UID 333496498. The complete [JF778667.1 record](https://www.ncbi.nlm.nih.gov/nuccore/JF778667.1) describes a 940-base partial 16S rRNA gene, partial at both ends, with source qualifiers Duganella sp. LT17CD, strain LT17CD, freshwater lake and `taxon:1034914`. Its only reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter's Bellerophon-screening comment was not independently tested here. No culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID occurs in the inspected metadata. This is a marker, not a genome or a culture-deposit identifier.

[Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4), whose main text was inspected, lists JF778652-JF778667. The accession and matching authors support a Lake Tawani(P), East Antarctica study association, not LT17CD-specific physiology or a deposit relationship. Study conditions do not establish growth optima. Supplements and figure images were not inspected.

Exact Assembly search returned zero, with the phrase-not-found warning for `txid1034914[Organism:noexp]`. That bounded result does not prove universal genome absence under other identifiers or taxa.

## Completeness

Ignored-inclusive hidden/compressed searches used `rg --no-ignore --hidden -n -z -i`, excluding `SOURCE.json` manifests, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The ID digits, full label and slug query returned 18 lines. Backbone and scope rows were read structurally; all other four native JSON objects and twelve complete header-aware AllTheBacteria rows were inspected. Address reconciliation found no unread or truncated candidate.

Three rows identify LT17CD: backbone, scope and native scientific name. Fifteen other matches contain coincident numeric identifiers for unrelated organisms:

- BV-BRC `1773.20363` is Mycobacterium tuberculosis ERR1034914, taxon 1773, with no GenBank accession in that object. The AllTheBacteria row for run `ERR1034914` is Mycobacterium tuberculosis sample `SAMEA3558447`, analysis `ERZ3501194`.
- GenBank `GCA_058711685.1` is Streptococcus pneumoniae, taxon 1313, with isolate value `1034914`, sample `SAMEA120831636` and project `PRJNA514245`. Even an exact match to those digits in an isolate field is not a match to the target NCBI taxonomy identifier. This full object explicitly identifies a different organism.
- GenBank `GCA_027162825.1` is Staphylococcus aureus 8-299-029, taxon 1280, sample `SAMEA1034914`, project `PRJNA514245`. Its AllTheBacteria sample match is also Staphylococcus aureus, analysis `ERZ3070315`, run `ERR086067`.
- Ten AllTheBacteria entries identify Shigella sonnei samples `SAMEA110349140` through `SAMEA110349149`.

A second ignored-inclusive search across the same ten roots for `JF778667|LT[ -]?17[ -]?CD` found only the same three target rows. Exact-ID structured comparisons in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no target row. These bounded retained sources do not support a missing eligible culture/deposit/genome relationship. Zero represented strains is an inventory statement, not denial of the named isolate's existence.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem search for the target review filename, found no previous target report or history match before this report. No required missing synonym, nomenclature, mapping, causal-graph or evidence object was established. Optional literature enrichment is not required for a taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record's identity, carried lineage, source count, provenance and seeded status are supported. The Streptococcus isolate-field collision and other unrelated identifiers must not be turned into LT17CD genome links.

## Recommended Edits

None. Keep the generated YAML and `SEEDED` status unchanged.

Future taxonomy corrections belong at NCBI, then the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction in `scripts/extract_source_inventory.py`. Harmonization changes belong in `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`; scope policy belongs in `curation/seed_scope.tsv`. A future study-context extension first needs a maintained input and explicit target-specific support. Do not patch generated YAML, infer culture deposits from a bare strain name or count the rRNA marker as a genome.

## Follow-up Checks

No blocking follow-up remains for this verdict. Any future deposit/genome candidate requires full source-native inspection and an explicit identity/linkage chain. After an authorized implementation, rerun focused schema/strict validation plus the documented reproduction, provenance, history and relevant corpus gates. Refresh the live taxonomy check when changing the pinned dump. Independent sequence placement and chimera analysis remain outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, existing worktree; the other session was reported closed and no extra worktree was created. This target review adds only this report, with diagnostics under `/private/tmp`. Records, source inventories, scope, history, statuses, prior reports and generated pages were preserved. No commits, GitHub mutations, external contacts or paid research occurred. Eukaryota was left untouched.
