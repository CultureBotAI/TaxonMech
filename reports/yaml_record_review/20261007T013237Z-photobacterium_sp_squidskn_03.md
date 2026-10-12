# YAML Record Review: Photobacterium sp. squidSkn_03

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_squidskn_03.yaml`
- Started UTC: 2026-10-07T01:31:35Z
- Finished UTC: 2026-10-07T01:32:37Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035402`, label `Photobacterium sp. squidSkn_03`. It contains SPECIES rank, BACTERIA domain, parent 2628852, genetic code 11, EXACT grounding, SEEDED mapping status, zero associated strain records, one NCBITAXON NAME attestation, and one seed event. No synonym, nomenclature, taxonomy-mapping, deposit, genome, literature, phenotype, or causal-graph assertions are present.

The YAML is generated and read-only. Future fixes belong in maintained source inventories or upstream transforms, the seeder, or `curation/seed_scope.tsv`, according to ownership. This review creates only this report.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_squidskn_03.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_squidskn_03.yaml --out /private/tmp/psqs03-strict.tsv`: exit 0, one file scanned, zero ERROR rows. Read the actual TSV; it is header-only.
- Target-specific backbone, parent-chain, source, scope, and path-index comparisons passed. These bounded comparisons are not corpus reproduction.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, provenance hashes, generated-site drift, and the full test suite. No invented focused corpus gate or inferred corpus-wide result is claimed.
- Not checked: corpus-wide `just validate-products` and `just validate-history`. This target has no curator-grounded graph nodes, and no external target history artifact matched the bounded search. Its inline event was schema-checked and inspected. No external history entry or status promotion was written.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222064` agrees with the exact identifier and label, rank, parent `NCBITaxon:2628852`, code, empty synonym fields, and 2026-09-13 snapshot. Read the complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31544`; it independently retains the same name.

Inspected full current [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035402&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035402) responses. They agree on exact identity and species rank; the XML verifies parent and code. The ten-entry root-first lineage agrees with the pinned source and YAML: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Vibrionales, Vibrionaceae, Photobacterium, unclassified Photobacterium. Datasets includes root explicitly.

The isolate-style designation does not justify changing NCBI's rank, assigning a named-species synonym, or asserting culture-deposit equivalence. EXACT denotes the taxon match, not formal nomenclatural standing or genome identity. The inspected XML supplies no alternate name or type designation. Exact target lookups in pinned type-material, merged-ID, and dropped inventories returned no rows.

## Evidence

- `data/taxa/PATHS.tsv:14555` maps this identifier to its slug. `curation/seed_scope.tsv:322335` supplies the 2026-09-13 addition and NCBI attestation reason retained in the event.
- The single NCBITAXON attestation correctly carries its identifier, exact label, count 1, unit NAME, and snapshot. Exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories are empty. No child taxon occurs in the pinned backbone. Zero associated strain records does not deny the isolate designation.
- Manifest timestamp fields and `src/taxonmech/seed.py:139` were inspected earlier this turn: raw 2026-09-13T17:50:44Z, AllTheBacteria 17:54:04Z, StrainInfo 17:29:00Z. The maximum-selection rule explains this target's seed event at 2026-09-13T17:54:04Z. Hashes were not recomputed.
- Exact `txid1035402[Organism:noexp]` searches returned zero Assembly records, with a phrase-not-found warning, and one nucleotide UID, 333798005. Read the complete nucleotide metadata, references, and features, excluding sequence bases. [JF792723.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792723.1) is a 1,251-base partial 16S rRNA sequence explicitly linked to squidSkn_03 and taxon 1035402. It is not a genome or assembly.
- Its source qualifiers give host `Nototodarus gouldi` verbatim and locality `New Zealand: North Island, Auckland Fish Market`. They do not explicitly identify an anatomical isolation site; Skn in the strain label is not itself evidence of skin isolation. No BioSample, BioProject, assembly, or culture-deposit accession appears in the inspected metadata.
- The Wollenberg/Rainey/Ruby research reference is marked Unpublished and provides no DOI or PMID. Its separate Wollenberg/Ruby direct submission is dated 07-APR-2011 at the University of Wisconsin, Madison. A title about bioluminescence variation is not a measured phenotype result for this isolate.
- The independent [NCBI genome Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035402/dataset_report) was an empty object. No supported target genome link was found in the checked sources. This does not establish that no genome exists elsewhere under a different identity.
- Reused the successful current-turn iModulonDB inventory queried for squidInt_09 before this target's web search: `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`. All 28 rows were inspected; none covers Photobacterium, and Vibrio natriegens datasets are not transferable. iModulonDB is not applicable, not negative biological evidence.
- Bounded web discovery used exact label/designation variants, authors, JF792723, genome/strain terms, and bioluminescence. Results were taxonomy listings; no inspected exact-isolate experiment supplied a missing biological assertion. This is not a global literature census, and no neighboring isolate's evidence was transferred.

## Completeness

Used `rg --no-ignore --hidden -n -z -i` for the identifier, label, slug, and designation variants in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed contents were included. All three matching rows were read: backbone, scope, and native scientific name.

All five SOURCE.json files were separately parsed in full and history filenames checked without ignore filtering; neither yielded a target match. A second accession/version search for JF792723 over the same roots returned zero matching content lines; separate metadata and history-filename searches returned none. Bounds exclude arbitrary external repositories and every downloadable source snapshot. An ignored-inclusive review-directory filename check found no earlier report for this target before this report was added.

The empty optional nomenclature, mappings, deposits, genomes, and graph fit the inspected source support. The marker and source qualifiers are possible future typed enrichment, not required missing genome assertions. Do not silently normalize host spelling or infer tissue from Skn without separate evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this individual review's evidence bounds. Identity, carried lineage, source count, attestation, and seed event are supported. Pass does not certify corpus-wide reproduction or globally exhaustive evidence.

## Recommended Edits

None required. Leave the generated YAML and SEEDED lifecycle status unchanged.

Optional JF792723.1 enrichment needs a maintained owner and supported typed representation that preserves its nucleotide-marker identity and exact taxon linkage, outside genome counts. Future phenotype, tissue, or habitat assertions require inspected isolate-level evidence.

## Follow-up Checks

For any maintained-input change, verify exact taxon, strain/deposit, and sequence identities at their authorities, rerun target schema and strict validation, and run documented full-corpus reproduction and QC gates before asserting corpus-wide correctness. Route transform or seeder corrections through their owning modules with focused regression tests.

Any future experimental assertion needs a primary source with the exact isolate, experimental conditions, and measured result, not an abbreviation or study title. No unresolved blocker was identified.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The other session is closed; the existing checkout was retained. No YAML, inventory, prior report, generated output, history artifact, GitHub item, or Eukaryota record was changed. No paid research or external contact occurred.
