# YAML Record Review: Photobacterium sp. squidInt_08

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_squidint_08.yaml`
- Started UTC: 2026-10-07T01:24:08Z
- Finished UTC: 2026-10-07T01:25:13Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035399`, label `Photobacterium sp. squidInt_08`. It contains SPECIES rank, BACTERIA domain, parent 2628852, genetic code 11, EXACT grounding, SEEDED mapping status, zero associated strain records, a single NCBITAXON NAME attestation, and one seed event. No synonym, nomenclature, taxonomy-mapping, culture-deposit, genome, literature, phenotype, or causal-graph claims are present.

This generated YAML is read-only. Future changes belong in maintained source inventories or upstream transforms, the seeder, or the scope input, depending on ownership. Only this review report is added.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_squidint_08.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_squidint_08.yaml --out /private/tmp/psqi08-strict.tsv`: exit 0, one file scanned, zero ERROR rows. Read the actual TSV, which is header-only.
- Compared the target's own source, backbone, lineage, scope, and path-index rows. These bounded checks passed; they are not a substitute for a corpus reproduction gate.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, provenance hashes, generated-site drift, and the complete test suite. No invented focused corpus verifier or inferred corpus-wide pass is reported.
- Not checked: corpus-wide `just validate-products` and `just validate-history`. This target has no curator-grounded graph nodes; no target external history artifact matched the bounded search. The inline seed event was schema-checked and inspected. No history artifact or status promotion was created.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222061` agrees with the identifier, exact label, rank, parent `NCBITaxon:2628852`, genetic code 11, empty synonym fields, and 2026-09-13 snapshot. Read the complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31541`; it retains the exact identity.

Inspected complete current responses from [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035399&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035399). They agree on exact label and species rank; the XML confirms parent and code. The ten-entry root-first chain agrees in identifiers, labels, and ranks with the pinned backbone and YAML: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Vibrionales, Vibrionaceae, Photobacterium, unclassified Photobacterium. Datasets includes root explicitly.

The isolate-style designation does not authorize a named-species synonym or rank change. EXACT refers to the taxon identifier match, not formal nomenclatural standing, culture-deposit equivalence, or genome identity. The inspected XML has no alternate-name or type-material assertion. Exact target checks of pinned type-material, merged-ID, and dropped inventories returned no rows.

## Evidence

- `data/taxa/PATHS.tsv:14552` records this slug. `curation/seed_scope.tsv:322332` records the 2026-09-13 addition and NCBI attestation reason reproduced in the seed event.
- The sole NCBITAXON attestation correctly carries the source identifier, label, count 1, unit NAME, and snapshot. Exact target rows in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories are empty. No child taxon was found in the pinned backbone. Zero associated strain records is not a denial that squidInt_08 is an isolate designation.
- The manifest timestamp fields and maximum-selection code at `src/taxonmech/seed.py:139` were inspected earlier this turn. Raw is 2026-09-13T17:50:44Z, AllTheBacteria 17:54:04Z, and StrainInfo 17:29:00Z; their maximum matches the seed event at 2026-09-13T17:54:04Z. Source hashes were not recomputed.
- Exact `txid1035399[Organism:noexp]` searches returned zero Assembly records, with a phrase-not-found warning, and one nucleotide UID, 333798002. Read the full returned nucleotide metadata, references, and features, excluding sequence bases. [JF792720.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792720.1) is a 1,251-base partial 16S rRNA sequence explicitly linked to squidInt_08 and taxon 1035399, not a genome or assembly.
- The sequence source gives host `Nototodarus gouldi` verbatim and locality `New Zealand: North Island, Auckland Fish Market`. It does not explicitly name an anatomical isolation site. The inspected metadata contains no BioSample, BioProject, assembly, or culture-deposit accession.
- Its Wollenberg/Rainey/Ruby research reference is marked Unpublished and provides no DOI or PMID. The separate Wollenberg/Ruby direct submission is dated 07-APR-2011 at the University of Wisconsin, Madison. The bioluminescence-related title does not itself establish an experimental phenotype for this isolate.
- An independent [NCBI genome Datasets query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035399/dataset_report) returned an empty object. No supported target assembly link was identified in the checked sources. This does not prove the absence of all genomes under other names or classifications.
- Reused the successful iModulonDB inventory queried earlier this turn for squidInt_04, before this target's web search. All 28 rows were inspected and none covers Photobacterium; the Vibrio natriegens datasets are not transferable. The command was `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`; a sandbox DNS failure was followed by a successful network-authorized retry. iModulonDB is not applicable, not negative biological evidence.
- Open-web discovery covered the exact label, hyphenated and space-separated designations, author/designation combinations, JF792720, genome/strain terms, and bioluminescence. Returned taxonomy listings did not establish new biological claims. No inspected exact-isolate experiment supplied a missing required assertion. This is not an exhaustive literature census, and neighboring isolates' accessions or findings were not transferred.

## Completeness

The bounded local search used `rg --no-ignore --hidden -n -z -i` for the taxon ID, label, slug, and designation variants within `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed contents were included. All three matching rows were read: backbone, scope, and native scientific name.

All five SOURCE.json files were separately parsed in full, and history filenames were checked without ignore filtering; no target match was found in those checks. The accession/version search for JF792720 over the same roots returned zero matching content lines; separate metadata and history-filename checks also returned none. These bounds do not encompass all external repositories or every downloadable source snapshot. An ignored-inclusive review-directory filename check found no earlier report for this target before this report was added.

The empty optional nomenclature, mapping, deposit, genome, phenotype, and graph slots fit the inspected evidence. The marker sequence and host/locality qualifiers could support future typed enrichment, but are not required missing genome assertions. Do not infer an anatomical site from Int, silently change the source's host spelling, or equate this isolate with other squid-associated records.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the stated individual-review bounds. Identity, carried NCBI lineage, source count, attestation, and seed event are supported. Pass does not certify corpus-wide reproducibility or globally exhaustive source coverage.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED lifecycle status.

Optional future JF792720.1 representation requires an owned maintained input and a supported typed field preserving exact linkage and nucleotide-marker identity, outside genome counts. Phenotype or habitat enrichment must rest on inspected isolate-specific evidence, not an abbreviation, title, or neighboring accession.

## Follow-up Checks

Following any upstream input change, verify taxon, strain/deposit, and sequence identities separately at their authorities. Rerun this target's schema and strict validation and run documented full-corpus reproduction and QC before claiming corpus-wide correctness. Route fixes to the owning transform, seeder, or scope input with focused regression coverage.

No unresolved blocker was identified. Any future experimental assertion requires primary evidence with its actual strain scope, conditions, and measured result; coverage remains bounded by the sources searched here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The other session is closed; the existing checkout was retained. No YAML, inventory, prior report, generated output, history artifact, GitHub item, or Eukaryota record was changed. No paid research or external contact occurred.
