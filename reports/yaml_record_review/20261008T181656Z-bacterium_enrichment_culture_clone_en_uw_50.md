# YAML Record Review: bacterium enrichment culture clone En_UW_50

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_50.yaml`
- Started UTC: 2026-10-08T18:09:00Z
- Finished UTC: 2026-10-08T18:16:56Z
- Verdict: pass

## Target

Reviewed the entire generated `TaxonRecord` for `NCBITaxon:1036436`, bacterium enrichment culture clone En_UW_50. Its recorded rank is `SPECIES`, domain `BACTERIA`, grounding `EXACT`, mapping status `SEEDED`, genetic code 11 and strain count zero. One NCBITAXON name attestation and one seed event are present. No strain, genome, nomenclature, mapping, synonym or causal-graph claims are stored.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no earlier report for this stem. This review does not edit the generated record or promote its status.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_50.yaml`: passed, no issues.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_50.yaml --out /private/tmp/uw50-strict.tsv`: passed, one file, zero errors. The complete output TSV contained only its header.
- Structured comparisons against the complete pinned backbone, all four ancestor rows, seven supplementary raw inventories, PATHS, scope, type material, merged IDs and dropped rows: passed within the individual-record scope.
- Parsed the complete matched native scientific-name object and complete backbone/scope rows; all identity and provenance fields agree.
- Parsed both complete NCBI sequence XML records. Declared and actual lengths agree; the submitted CDS translation exactly matches its own protein sequence. No non-ACGT DNA symbols or ambiguous protein residues were found. This checks annotation consistency, not independent translation, alignment or experimental function.

Not checked: `just verify-corpus`, full-corpus schema validation, provenance/history gates, `just qc`, full tests, vendored synchronization, site drift and publication builds. This report does not claim corpus reproducibility. The embedded seed event was inspected, but no separate target history artifact was found in the bounded ignored-inclusive searches. `just validate-products` is not applicable: no curator-added graph nodes are present. No invented single-record substitute was used for a corpus-wide gate.

## Identity and Grounding

The full [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036436&retmode=xml) confirms the exact label, species rank, parent 48479 and code 11. The [NCBI Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036436) confirms root-first ancestor IDs 1, 131567, 2 and 48479. Their recorded names and ranks agree with the pinned backbone: root, cellular organisms, Bacteria and environmental samples. EFetch omits root from its displayed lineage; Datasets includes it. This is not a lineage conflict.

The record is an environmental clone taxon at NCBI's species rank, not an identified, formally named species or a demonstrated pure culture. `EXACT` correctly describes identifier grounding, not biological characterization. No other names were supplied by live EFetch; pinned synonym fields are empty. No exact target row appeared in pinned type-material, merged-ID or dropped inventories, and the complete backbone comparison found no children.

## Evidence

The individual source chain is:

- `data/raw/ncbitaxon_taxa.tsv:222438`: exact ID, label, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31982`: scientific-name object for this taxon, with no unique-name qualifier.
- `data/taxa/PATHS.tsv:14945`: exact identifier-to-slug assignment.
- `curation/seed_scope.tsv:322685`: 2026-09-13 admission and the same one-source reason carried by the seed event.

The single `NAME` attestation is one source assertion, not one isolate or experimental observation. The event timestamp and seeded state are internally consistent. Complete exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found no matching rows; zero represented strains is therefore supported within those inventories.

Exact non-expanded NCBI Nuccore search `txid1036436[Organism:noexp]` returned one record, UID 336092416. Its complete [HQ630174.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630174.1) identifies this taxon and clone, a 340-base partial `nosZ` CDS, an anode-biofilm source, environmental-sample status and H2S-supplemented mineral medium. Both CDS ends are partial, codon start is 3 and translation table is 11. No strain, collection deposit or geographic qualifier is supplied.

The complete [AEI00832.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00832.1) reciprocally references HQ630174.1 and the same clone/taxon. Its 112-residue conceptual translation has a PRK02888/CDD:235082 region annotated through residue 112. These annotations support the submitted partial-sequence identity, not measured enzyme activity, purity or whole-organism physiology. Both records cite an unpublished enrichment study and a 17-NOV-2010 direct submission; neither supplies a PMID or DOI for that unpublished reference.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, places HQ630075-HQ630210 among enrichment-derived nosZ accessions. Page 92 warns that a single DGGE band does not establish culture purity. HQ630174 falls within that range, but this is study context, not a clone-specific species assignment. Both pages were read completely. Searching extractable text across all 164 pages found neither the exact accession nor this clone label; raster content and every supplement were not exhaustively searched.

Exact accession/protein web searches returned no results; a clone-label search excluding the already checked NCBI Taxonomy site also returned none. Exact accession and clone searches within the inspected [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matches. No article-level community performance was attributed to this clone. These are bounded discovery checks, not claims of literature absence.

## Completeness

This record is complete enough for the supported taxonomy seed. Empty optional nomenclature, mappings, strain deposits, genome links, synonyms and graph fields do not require invented content. The external gene fragment is not a genome assembly and is not a mandatory taxonomic-record field.

An expanded `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored and compressed files. It used the taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. Only the three backbone, scientific-name and scope rows listed above matched. All were read completely. Five source `SOURCE.json` files were separately parsed in full and supplied no target identity match; history filenames were separately inventoried. The search is exhaustive only within these stated roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. This establishes no assembly hit under that exact query, not universal genome absence. No independent UniProt, pure-isolate or expression-dataset identity was established. iModulonDB was not run: the YAML makes no gene/regulator/expression claim and no covered strain/dataset was identified. This is not negative evidence about that database.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. The difference between a partial environmental sequence annotation and experimentally characterized biology is an evidence limit, not an unsupported claim made by this YAML.

## Recommended Edits

None required. Retain the current generated record, its `SEEDED` status and zero represented strains.

Any future taxonomy correction belongs first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. An established projection bug belongs in `src/taxonmech/seed.py` with a focused regression test; a scope decision belongs in `curation/seed_scope.tsv`. Optional sequence provenance would require a supported maintained input and schema/seeder handling, not hand-editing this YAML. Do not transfer a neighboring clone's accession, medium, strain, species assignment or phenotype.

## Follow-up Checks

No corrective follow-up is required for this pass. Before optional biological enrichment, establish an explicit clone-to-isolate or clone-to-genome chain and inspect the relevant primary experimental evidence. Recheck exact authority records if a later snapshot changes identity or lineage.

After an authorized upstream or seeder correction, run the focused regression test and documented `just seed-canary NCBITaxon:1036436`, inspect its emitted YAML, then rerun both record validators and `just verify-corpus`; use the full QC gates before publication. No generation command was run by this review.

## Additional Notes

Review guidance, curation boundaries, checklist and validator definitions were read. The source and public sequence checks were specific to En_UW_50; no verdict or accession was copied from a sibling record. SHA-256 before and after review was `54daada2bc9907a564094c5c25ca4a3efb8a23a9123a90f481f6fd620b91c27c`.

Only this new timestamped Markdown report was added. No record, source, history, status, generated page or GitHub object was changed. Eukaryota and existing worktrees were left untouched.
