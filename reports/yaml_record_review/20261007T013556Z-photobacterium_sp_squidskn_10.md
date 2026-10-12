# YAML Record Review: Photobacterium sp. squidSkn_10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_squidskn_10.yaml`
- Started UTC: 2026-10-07T01:34:16Z
- Finished UTC: 2026-10-07T01:35:56Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035403`, label `Photobacterium sp. squidSkn_10`. It carries SPECIES rank, BACTERIA domain, parent 2628852, genetic code 11, EXACT grounding, SEEDED mapping status, zero associated strain records, one NCBITAXON NAME attestation, and one seed event. It has no synonym, nomenclature, taxonomy-mapping, deposit, genome, literature, phenotype, or causal-graph assertions.

Generated YAML is read-only. Future changes belong in maintained source inventories or upstream transforms, the seeder, or `curation/seed_scope.tsv`, according to ownership. Only this report is added.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_squidskn_10.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_squidskn_10.yaml --out /private/tmp/psqs10-strict.tsv`: exit 0, one file scanned and zero ERROR rows. Read the actual header-only TSV.
- Complete target-specific backbone, lineage, source, scope, and index comparisons passed. These bounded comparisons are not corpus reproduction.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, source hashes, generated-site drift, and the full test suite. No focused substitute or inferred corpus-wide pass is claimed.
- Not checked: corpus-wide `just validate-products` and `just validate-history`. There are no curator-grounded graph nodes in this target; bounded history searches found no external target artifact. The inline event was schema-checked and inspected. No history artifact or status promotion was created.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:222065` agrees with identifier, exact label, rank, parent `NCBITaxon:2628852`, code, empty synonym fields, and 2026-09-13 snapshot. The full native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31545` independently retains the same identity.

Inspected complete current [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035403&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035403) responses. The exact name and species rank agree; XML verifies parent and code. All ten lineage entries agree with the pinned source and YAML: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Vibrionales, Vibrionaceae, Photobacterium, unclassified Photobacterium. Datasets includes root explicitly.

An isolate-style designation does not authorize changing NCBI rank, assigning a named-species synonym, or inferring culture-deposit identity. EXACT denotes this taxon match, not formal nomenclatural standing or genome equivalence. The inspected XML has no alternate-name or type-material assertion. Exact target lookups in pinned type-material, merged-ID, and dropped inventories returned no rows.

## Evidence

- `data/taxa/PATHS.tsv:14556` supplies the slug; `curation/seed_scope.tsv:322336` supplies the 2026-09-13 addition and NCBI attestation reason retained in the seed event.
- The sole NCBITAXON attestation has the correct identifier, exact label, count 1, unit NAME, and snapshot. Exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories are empty. No child taxon occurs in the pinned backbone. Zero associated strain records does not deny the isolate designation.
- Read the three manifest timestamp fields and the maximum-selection logic at `src/taxonmech/seed.py:139` this turn. Raw is 2026-09-13T17:50:44Z, AllTheBacteria 17:54:04Z, and StrainInfo 17:29:00Z. Their maximum matches this target's 2026-09-13T17:54:04Z event. Hashes were not recomputed.
- Exact `txid1035403[Organism:noexp]` searches returned zero Assembly records, with a phrase-not-found warning, and one nucleotide UID, 333798011. Read all its returned metadata, references, and features, excluding sequence bases. [JF792729.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792729.1) is a 1,251-base partial 16S rRNA sequence explicitly linked to squidSkn_10 and taxon 1035403. The accession was read from this response, not inferred from nearby isolates. It is not a genome or assembly.
- Source qualifiers give host `Nototodarus gouldi` verbatim and locality `New Zealand: North Island, Auckland Fish Market`. No explicit anatomical isolation site is supplied; Skn is not itself evidence of skin isolation. No BioSample, BioProject, assembly, or culture-deposit accession occurs in the inspected sequence metadata.
- The Wollenberg/Rainey/Ruby research reference is marked Unpublished and has no DOI or PMID. Its separate Wollenberg/Ruby direct submission is dated 07-APR-2011 at the University of Wisconsin, Madison. A bioluminescence-related title is not a measured phenotype result for this isolate.
- The independent [genome Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035403/dataset_report) was an empty object. No supported target genome link emerged within the checked sources. This is not proof that no genome exists elsewhere under a different identity.
- Before open-web discovery, successfully ran `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` with read-only network access. Inspected all 28 dataset rows; none covers Photobacterium, and Vibrio natriegens datasets are not transferable. iModulonDB is not applicable, not negative biological evidence.
- Bounded web queries covered exact label/designation variants, authors, JF792729, genome/strain terms, and the research title. Results were taxonomy listings or unrelated leads; no inspected exact-isolate experimental publication supplied a missing biological assertion. This is not an exhaustive literature census, and neighboring isolates' evidence was not transferred.

## Completeness

Used `rg --no-ignore --hidden -n -z -i` for the identifier, label, slug, and designation variants within `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed contents were included. All three matches were read: backbone, scope, and native scientific name.

All five SOURCE.json files were separately parsed in full and history filenames checked without ignore filtering; neither yielded a target match. A second accession/version search for JF792729 over the same roots returned zero content matches, with no metadata or history-filename matches. Bounds exclude arbitrary external repositories and every downloadable source snapshot. An ignored-inclusive review-directory filename check found no earlier report for this target before this report was added.

The empty optional nomenclature, mapping, strain/deposit, genome, and graph slots fit the inspected support. The partial marker and host/locality qualifiers are possible future typed enrichment, not required missing genomes. Preserve the source's host spelling unless separately resolved, and do not infer anatomy from Skn.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the individual review's evidence bounds. Identity, carried lineage, count, attestation, and event provenance are supported. Pass does not certify corpus-wide reproduction or globally exhaustive evidence.

## Recommended Edits

None required. Leave generated YAML and SEEDED lifecycle status unchanged.

Optional JF792729.1 enrichment needs an owned maintained input and supported typed representation preserving exact taxon linkage and nucleotide-marker identity, outside genome counts. Anatomy, phenotype, or habitat assertions require explicit isolate-level evidence.

## Follow-up Checks

After any maintained-input change, verify taxon, strain/deposit, and sequence identities at their authorities, rerun target schema and strict validation, and run documented full-corpus reproduction and QC before asserting corpus-wide correctness. Route transform or seeder changes through their owning modules with focused regression tests.

A future experimental assertion needs the exact isolate, conditions, and measured result from an inspected primary source, not an abbreviation or study title. No unresolved blocker was identified.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The other session is closed; the existing checkout was retained. No YAML, inventory, prior report, generated output, history artifact, GitHub item, or Eukaryota record was changed. No paid research or external contact occurred.
