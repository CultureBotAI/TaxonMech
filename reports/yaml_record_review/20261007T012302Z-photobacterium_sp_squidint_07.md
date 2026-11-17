# YAML Record Review: Photobacterium sp. squidInt_07

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_squidint_07.yaml`
- Started UTC: 2026-10-07T01:21:56Z
- Finished UTC: 2026-10-07T01:23:02Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035398`, label `Photobacterium sp. squidInt_07`. The record has SPECIES rank, BACTERIA domain, parent 2628852, code 11, EXACT grounding, SEEDED mapping status, zero associated strain records, one NCBITAXON NAME attestation, and one seed event. It has no synonym, nomenclature, taxonomy-mapping, culture-deposit, genome, literature, phenotype, or causal-graph assertions.

The YAML is generated and read-only. Future corrections belong in the maintained inventories or upstream transforms, seeder, or scope input as appropriate; this review creates only this report.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_squidint_07.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_squidint_07.yaml --out /private/tmp/psqi07-strict.tsv`: exit 0, one file scanned, zero ERROR rows. Read the actual header-only TSV.
- Individually compared this target's backbone, lineage, source, scope, and index rows. These bounded checks passed and are not a substitute for corpus reproduction.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, manifest hashes, generated-site drift, and the complete test suite. No focused corpus-reproduction result is claimed.
- Not checked: corpus-wide `just validate-products` and `just validate-history`. This target has no curator-grounded graph nodes and no target history artifact matched the bounded search. The inline seed event was schema-checked and inspected; no history entry or status promotion was made.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:222060` agrees with the identifier, exact name, rank, parent `NCBITaxon:2628852`, genetic code, empty synonym fields, and 2026-09-13 snapshot. The exact native scientific name is retained at `data/catalog/ncbi_names-0005.jsonl.gz:31540`; its complete row was read.

Inspected the full current [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035398&retmode=xml) and [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035398). The exact name, species rank, bacterial domain, parent, and code agree. All ten lineage entries agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Vibrionales, Vibrionaceae, Photobacterium, and unclassified Photobacterium. Datasets supplies root explicitly.

NCBI's species rank is preserved despite the isolate-style name; neither a named-species synonym nor culture-deposit identity can be inferred. EXACT describes the identifier match, not formal nomenclatural status or genome equivalence. No alternate name or type designation occurs in the inspected taxonomy XML. Exact target checks of the pinned type-material, merged-ID, and dropped inventories returned no rows.

## Evidence

- `data/taxa/PATHS.tsv:14551` gives this slug; `curation/seed_scope.tsv:322331` gives the 2026-09-13 addition and NCBI attestation reason recorded in the seed event.
- The NCBITAXON attestation has the exact source identifier and label, count 1, unit NAME, and correct snapshot. Exact target rows in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories are empty. No child taxon occurs in the pinned backbone. Zero associated strain records does not deny the isolate designation.
- The three manifest timestamp fields and `src/taxonmech/seed.py:139` timestamp-selection logic were inspected earlier in this same turn: raw 2026-09-13T17:50:44Z, AllTheBacteria 17:54:04Z, and StrainInfo 17:29:00Z. The maximum explains this target's 2026-09-13T17:54:04Z seed event. Manifest hashes were not recomputed.
- Exact `txid1035398[Organism:noexp]` searches returned zero Assembly records, with a phrase-not-found warning, and one nucleotide UID, 333798001. Read its complete metadata, references, and features, excluding sequence bases. [JF792719.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792719.1) is a 1,251-base partial 16S rRNA sequence explicitly linked to squidInt_07 and taxon 1035398. It is not a genome or assembly.
- Source qualifiers retain host `Nototodarus gouldi` verbatim and locality `New Zealand: North Island, Auckland Fish Market`. They do not explicitly supply an anatomical isolation site. This metadata contains no BioSample, BioProject, assembly, or culture-deposit accession. Its Wollenberg/Rainey/Ruby research reference is marked Unpublished and has no DOI or PMID. A separate Wollenberg/Ruby direct submission is dated 07-APR-2011 at the University of Wisconsin, Madison. The bioluminescence-related research title alone does not demonstrate an isolate phenotype.
- The independent [NCBI genome Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035398/dataset_report) was an empty object. No supported target genome link emerged within the checked sources. This is not a global assertion that no differently classified or named genome exists.
- Read and rejected the complete row at `data/catalog/gtdb_genomes-0004.jsonl.gz:34802`. `RS_GCF_948731065.1`, with GenBank accession `GCA_948731065.1`, belongs to an uncultured Alistipes taxon 538949, isolate MGBC123038, classified by GTDB as Alistipes muris. The number 1035398 occurs in `ncbi_scaffold_n50`, not its taxon fields. Neither this genome nor its sample/project links support the Photobacterium target.
- Reused the successful iModulonDB inventory queried earlier in this same turn for squidInt_04, before this target's web search. All 28 dataset rows were inspected; none covers Photobacterium, and Vibrio natriegens datasets are not transferable. The successful command was `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`; it followed a DNS failure in the sandbox and a network-authorized retry. iModulonDB is not applicable, not negative evidence.
- Targeted web queries covered exact label/designation variants, authors, JF792719, genome/strain terms, and bioluminescence. Results were taxonomy listings, not inspected isolate-specific experiments. No new biological claim was justified. This is a bounded discovery result, not an exhaustive literature census; findings for squidInt_04 or other nearby isolates were not transferred.

## Completeness

Used `rg --no-ignore --hidden -n -z -i` for the target ID, label, slug, and designation variants in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed contents were included. All four matched rows were read: backbone, scope, native name, and the rejected GTDB statistic collision.

All five SOURCE.json files were separately parsed in full and history filenames checked without ignore filtering; neither yielded a target match. A second search for JF792719 and its version across the same roots returned zero matching content lines, with no metadata or history-filename matches. Bounds exclude arbitrary external repositories and every downloadable source snapshot. An ignored-inclusive review-directory filename check found no earlier report for this target before this report was added.

The empty optional nomenclature, mapping, strain/deposit, genome, and graph slots match the inspected source support. The partial marker and host/locality qualifiers are potential future typed enrichment, not required missing genomes. Do not infer intestine from Int or silently normalize host spelling; those need separate evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the individual review's bounds. Identity, carried NCBI lineage, attestation, source count, and event provenance are supported. The pass does not certify globally exhaustive evidence coverage or corpus-wide reproducibility.

## Recommended Edits

None required. Leave the generated YAML and SEEDED status unchanged.

Optional future JF792719.1 representation must be owned by a maintained input and preserve exact taxon linkage and nucleotide-marker type, outside genome counts. Do not use a numerical catalog collision, study title, or another isolate's evidence as a join or biological assertion.

## Follow-up Checks

After any maintained-input change, verify exact taxon, strain/deposit, and sequence identities at their respective authorities, rerun this target's schema and strict validators, and run documented full-corpus reproduction and QC gates before claiming corpus-wide correctness. Generator or transform fixes need focused regression tests in their owning module.

A future phenotype or habitat assertion requires inspected isolate-level source evidence and its experimental scope. No unresolved blocker was identified; source-coverage limitations remain as stated above.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The other session is closed and the existing checkout was retained. No YAML, source inventory, prior report, generated product, history artifact, GitHub item, or Eukaryota record was changed. No paid research or external contact occurred.
