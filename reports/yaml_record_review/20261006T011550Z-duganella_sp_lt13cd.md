# YAML Record Review: Duganella sp. LT13CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_lt13cd.yaml`
- Started UTC: 2026-10-06T01:14:05Z
- Finished UTC: 2026-10-06T01:15:50Z
- Verdict: pass

## Target

Read the complete 56-line generated `TaxonRecord` for `NCBITaxon:1034912`, Duganella sp. LT13CD. It is a `SPECIES` in `BACTERIA`, parent `NCBITaxon:2636909` (unclassified Duganella), with eleven root-first lineage entries, genetic code 11, `EXACT` grounding and `SEEDED` mapping status. It represents zero source-backed strain entries and one NCBITAXON NAME assertion at snapshot `2026-09-13`. Its sole inline history event is `SEEDED_FROM_SOURCES` at `2026-09-13T17:54:04Z`. Optional synonym, nomenclature, taxonomy-mapping, strain, evidence, discussion and causal-graph sections are not populated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_lt13cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_lt13cd.yaml --out /private/tmp/lt13cd-validation.tsv`: exit 0, one file, zero ERROR rows; the full output TSV contains only its header.
- Read the complete matching backbone, scope and source-native name rows. Structured comparisons verified every lineage ID/label/rank, the target fields, unique PATHS entry, attestation and inline seed-event scope description. No child row was returned from the backbone. These bounded comparisons do not prove full corpus reproduction.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no matching row. Seven supplementary inventories also returned no exact taxon match, as detailed below.
- Read complete live NCBI Taxonomy EFetch and Datasets responses. Read both exact, non-expanding Assembly/Nuccore search results and the complete metadata, references and features for the sole nucleotide hit; bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, source-provenance hashes, rendered-site drift, README statistics, publication-size budget and vendored synchronization. No such gate is claimed by this bounded report-only review. Inline-event inspection is not history-schema validation.
- `just validate-products` and iModulonDB were not applicable: no curator-added graph grounding, gene, regulator, transcriptomic module or expression claim exists. No LPSN/GTDB mapping on the target required an authority-page check.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221740`, the [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034912&retmode=xml), and the [NCBI Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034912) agree on the target ID, label, rank and parent. EFetch supplies code 11 and bacterial division; Datasets supplies the ordered ancestor IDs including root. All eleven YAML ancestors match the pinned chain, with the same labels and ranks in the inspected taxonomy evidence.

The chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group, Duganella and unclassified Duganella. Telluria group (`NCBITaxon:2895353`) is a carried no-rank ancestor, not a synonym or alternate genus assignment for LT13CD. The abbreviated GenBank lineage omits the final unclassified intermediate; dedicated taxonomy responses explicitly confirm it.

`data/taxa/PATHS.tsv:14210` uniquely maps the ID to `duganella_sp_lt13cd`; `curation/seed_scope.tsv:322042` records the one-source NCBI inclusion rule. The complete `data/catalog/ncbi_names-0005.jsonl.gz:31143` object is the matching scientific name, without an alternate name. Species rank denotes this provisional isolate-labelled NCBI taxon and does not establish valid publication of a formal species name. Nearby LT12CD and LT14CD labels do not establish strain equivalence.

## Evidence

The sole record-level assertion is its source-backed NCBI name and taxonomy. The source ID, label, snapshot and single NAME unit agree with the pinned inventory. This count is not a strain or genome count. No phenotype, growth requirement, ecological mechanism, genome or type-strain claim is made in the YAML.

The exact Nuccore query returned one UID, 333496494. Its complete [JF778663.1 record](https://www.ncbi.nlm.nih.gov/nuccore/JF778663.1) describes a 970-base partial 16S rRNA gene, partial at both ends, explicitly linked to Duganella sp. LT13CD, strain LT13CD, freshwater-lake isolation source and `taxon:1034912`. The only reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter reports Bellerophon chimera screening; this review did not independently repeat it. There is no culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID in the inspected sequence metadata. A partial rRNA marker and bare strain designation are not an eligible culture-deposit/genome chain.

The inspected main text of [Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4) includes JF778663 within its submitted range JF778652-JF778667. The matching authors and accession range support association with the Lake Tawani(P), East Antarctica study. Community results and culture-workflow conditions do not prove LT13CD-specific physiology, growth optima or a culture deposit. Supplements and figure images were not inspected.

The exact Assembly query returned zero, with a phrase-not-found warning for `txid1034912[Organism:noexp]`. This result is bounded to that query; it is not proof that no genome exists under any other identifier.

## Completeness

Ignored-inclusive hidden/compressed searches used `rg --no-ignore --hidden -n -z -i`, excluding `SOURCE.json` manifests, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searching `1034912`, the full label and the slug yielded 19 lines. Backbone and scope rows were read structurally; all other five native JSON objects and twelve header-aware AllTheBacteria rows were read completely. Address reconciliation found no unread or truncated candidate.

Only the backbone, scope and native scientific-name row identify LT13CD. The sixteen other matches are numeric collisions:

- BV-BRC `1773.20365` is Mycobacterium tuberculosis ERR1034912, taxon 1773, with no GenBank accession in that object. The AllTheBacteria row using run `ERR1034912` is likewise Mycobacterium tuberculosis, sample `SAMEA3558445`, analysis `ERZ3501178`.
- GenBank `GCA_010349125.1` is Campylobacter jejuni PNUSAC013794, taxon 197, sample `SAMN13428625`, project `PRJNA239251`. The digits occur in the assembly accession, not its taxonomy.
- GenBank `GCA_048499015.1` is Hyphomicrobiaceae bacterium PROT-2, taxon 2015799, sample `SAMN31034912`, project `PRJNA884640`, derived from a metagenome.
- GenBank `GCA_027162265.1` is Staphylococcus aureus 8-327-026, taxon 1280, sample `SAMEA1034912`, project `PRJNA514245`. The corresponding AllTheBacteria sample row is Staphylococcus aureus, analysis `ERZ3070319`, run `ERR086096`.
- Ten AllTheBacteria rows are Shigella sonnei samples `SAMEA110349120` through `SAMEA110349129`, not Duganella cultures.

A separate ignored-inclusive scan of the same ten roots for `JF778663|LT[ -]?13[ -]?CD` returned only the same three target rows. Exact-ID comparisons of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no target row. No eligible missing strain/deposit/genome association is supported within these retained sources. `strain_count: 0` describes represented inventory evidence, not whether the named isolate exists biologically.

Ignored-inclusive searches of `reports` and `history` for the target ID, label and slug, plus a filesystem search for the target review filename, found no previous report/history match before this report. No required optional synonym, nomenclature, mapping, graph or literature object was identified as missing. Study-context enrichment is possible future curation, not a prerequisite for this taxonomy-only record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record's asserted identity, carried lineage, count semantics, provenance and seeded status are supported. Neither unrelated accession substrings nor the partial marker justify adding a genome or deposit relationship.

## Recommended Edits

None. Preserve the generated YAML, prior reports and `SEEDED` status.

Any future primary taxonomy correction belongs at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization changes belong in `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`; scope changes belong in `curation/seed_scope.tsv`. An optional study-context addition requires a maintained source representation with target-specific support. Do not hand-edit generated YAML or treat the rRNA marker as a genome.

## Follow-up Checks

No blocking follow-up remains for this verdict. New deposit or genome evidence would require full source-native identity and linkage verification before any authorized regeneration. Then rerun the focused schema and strict validators and the documented reproduction, provenance, history and relevant corpus gates. Recheck live taxonomy after a pinned refresh. Sequence-based placement and independent chimera assessment remain outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; guidance and relevant tracked files had no diff at baseline. One existing worktree was listed, with the other session reported closed; no extra worktree was created. Only this new report was written, with validator diagnostics under `/private/tmp`. No records, source inputs, scope, history, statuses, prior reports or generated pages were changed. No commits, GitHub mutations, external contacts or paid research were performed. Eukaryota was left untouched.
