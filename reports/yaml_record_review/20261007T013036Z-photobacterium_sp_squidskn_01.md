# YAML Record Review: Photobacterium sp. squidSkn_01

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_squidskn_01.yaml`
- Started UTC: 2026-10-07T01:29:31Z
- Finished UTC: 2026-10-07T01:30:36Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035401`, label `Photobacterium sp. squidSkn_01`. Its SPECIES rank, BACTERIA domain, parent 2628852, genetic code 11, EXACT grounding, SEEDED mapping status, zero associated strain records, one NCBITAXON NAME attestation, and one seed event were reviewed individually. It asserts no synonyms, nomenclature, taxonomy mappings, deposits, genomes, literature, phenotypes, or causal graph.

The YAML is generated and read-only. A future correction belongs in its maintained source inventory or upstream transform, the seeder, or `curation/seed_scope.tsv`, as appropriate. Only this report is added.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_squidskn_01.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_squidskn_01.yaml --out /private/tmp/psqs01-strict.tsv`: exit 0, one file scanned, zero ERROR rows. Read the actual header-only TSV.
- Complete target-specific backbone, lineage, source, scope, and path-index comparisons passed. These bounded comparisons are not corpus reproduction.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, source hashes, generated-site drift, and the full test suite. No invented focused corpus gate or inferred corpus-wide pass is claimed.
- Not checked: corpus-wide `just validate-products` and `just validate-history`. This target has no curator-grounded graph nodes; no external target history artifact matched the bounded search. Its inline event was schema-checked and inspected. No history artifact or lifecycle promotion was written.

## Identity and Grounding

The entire row at `data/raw/ncbitaxon_taxa.tsv:222063` agrees with the target's identifier, label, rank, parent `NCBITaxon:2628852`, code, empty synonym fields, and 2026-09-13 snapshot. Read the complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31543`.

Full current [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035401&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035401) responses agree on the exact name and species rank; the XML verifies parent and code. The ten-entry root-first lineage agrees with the pinned backbone and YAML in identifiers, labels, and ranks: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Vibrionales, Vibrionaceae, Photobacterium, unclassified Photobacterium. Datasets includes root explicitly.

The isolate-style designation does not justify changing NCBI rank or assigning a named-species synonym. EXACT is a match to this taxon identity, not formal nomenclatural standing or deposit/genome equivalence. No alternate name or type designation appears in the inspected XML. Exact target lookups in pinned type-material, merged-ID, and dropped inventories returned no rows.

## Evidence

- `data/taxa/PATHS.tsv:14554` identifies this slug. `curation/seed_scope.tsv:322334` supplies the 2026-09-13 addition and attestation reason reproduced in the seed event.
- The sole NCBITAXON attestation correctly retains count 1, unit NAME, exact identifier and label, and snapshot. Exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories are empty. The pinned backbone contains no child taxon. Zero associated strain records is not a biological denial of the strain designation.
- The manifest timestamp fields and selection code at `src/taxonmech/seed.py:139` were inspected earlier this turn: raw 2026-09-13T17:50:44Z, AllTheBacteria 17:54:04Z, StrainInfo 17:29:00Z. Their maximum explains this target's 2026-09-13T17:54:04Z seed event. Source hashes were not recomputed.
- Exact `txid1035401[Organism:noexp]` searches returned zero Assembly records, with a phrase-not-found warning, and one nucleotide UID, 333798004. Read all returned nucleotide metadata, references, and features, excluding sequence bases. [JF792722.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792722.1) is a 1,251-base partial 16S rRNA sequence explicitly linked to squidSkn_01 and taxon 1035401. It is not a genome or assembly.
- The source qualifiers retain host `Nototodarus gouldi` verbatim and locality `New Zealand: North Island, Auckland Fish Market`. They provide no explicit anatomical isolation site. In particular, Skn in the designation is not itself evidence of skin isolation. No BioSample, BioProject, assembly, or culture-deposit accession appears in the inspected metadata.
- The research reference names Wollenberg, Rainey, and Ruby, is marked Unpublished, and provides no DOI or PMID. The separate Wollenberg/Ruby direct submission is dated 07-APR-2011 at the University of Wisconsin, Madison. A bioluminescence-related study title is not proof of an isolate-level phenotype.
- The independent [genome Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035401/dataset_report) was an empty object. The checked sources supplied no supported target genome link; this does not prove that no genome exists elsewhere under another identity.
- Reused the successful current-turn iModulonDB inventory queried for squidInt_09 before this target's web discovery. The command was `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`. All 28 dataset rows were inspected, with no Photobacterium coverage. Vibrio natriegens datasets are not transferable. iModulonDB is not applicable, not negative evidence.
- Bounded web queries covered exact label/designation variants, authors, JF792722, genome/strain terms, and bioluminescence. Results were taxonomy listings; no inspected exact-isolate experimental publication supplied a missing biological assertion. This is not a global literature census. Other isolates' accessions, patent mentions, or phenotypes were not transferred.

## Completeness

Used `rg --no-ignore --hidden -n -z -i` for the target ID, label, slug, and designation variants in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed contents were included. All three matching rows were read: backbone, scope, and native scientific name.

All five SOURCE.json files were separately parsed in full and history filenames checked without ignore filtering; neither yielded a target match. A second accession/version search for JF792722 over the same roots returned zero content matches, with no metadata or history-filename matches. These bounds exclude arbitrary external repositories and every downloadable source snapshot. An ignored-inclusive review-directory filename check found no earlier report for this target before this report was added.

Empty optional nomenclature, mapping, strain/deposit, genome, and graph slots are consistent with the inspected sources. The marker and source qualifiers could support future typed enrichment, but are not missing required genome assertions. Preserve the source's host spelling unless separately resolved; do not derive a tissue claim from Skn.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the individual review's evidence bounds. Identity, carried lineage, source count, attestation, and event provenance are supported. Pass does not certify full-corpus reproduction or globally exhaustive evidence.

## Recommended Edits

None required. Keep generated YAML and SEEDED status unchanged.

Optional JF792722.1 enrichment needs a maintained owner and supported typed representation preserving nucleotide-marker identity and exact taxon linkage, outside genome counts. Future anatomy, phenotype, or habitat claims need inspected source evidence at the isolate level.

## Follow-up Checks

For any maintained-input change, reverify exact taxon, strain/deposit, and sequence identities, rerun target schema and strict validation, and run documented full-corpus reproduction and QC gates before asserting corpus-wide correctness. Changes to a transform or seeder need focused regression tests in the owning module.

A future tissue or phenotype assertion needs an explicit primary-source statement or measured result, not the isolate abbreviation or study title. No unresolved blocker was identified.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The other session is closed; the existing checkout was retained. No YAML, inventory, prior report, generated product, history artifact, GitHub item, or Eukaryota record was changed. No paid research or external contact occurred.
