# YAML Record Review: Photobacterium sp. squidInt_09

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_squidint_09.yaml`
- Started UTC: 2026-10-07T01:27:03Z
- Finished UTC: 2026-10-07T01:28:36Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035400`, label `Photobacterium sp. squidInt_09`. It carries SPECIES rank, BACTERIA domain, parent 2628852, genetic code 11, EXACT grounding, SEEDED mapping status, zero associated strain records, one NCBITAXON NAME attestation, and one seed event. No synonym, nomenclature, taxonomy-mapping, deposit, genome, literature, phenotype, or causal-graph assertions are present.

Generated YAML is read-only. Future changes belong in maintained source inventories or their upstream transforms, the seeder, or `curation/seed_scope.tsv`, according to ownership. This review adds only this report.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_squidint_09.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_squidint_09.yaml --out /private/tmp/psqi09-strict.tsv`: exit 0, one file scanned, zero ERROR rows. Read the actual TSV; it is header-only.
- Compared the target's complete backbone row, parent chain, source rows, scope, and index entry. These bounded checks passed and are not a corpus reproduction gate.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, provenance hashes, generated-site drift, and the full test suite. No focused substitute or corpus-wide result is claimed.
- Not checked: corpus-wide `just validate-products` and `just validate-history`. This target has no curator-grounded graph nodes and no external history artifact matched the bounded search. The inline event was schema-checked and inspected; no history artifact or lifecycle promotion was created.

## Identity and Grounding

The full row at `data/raw/ncbitaxon_taxa.tsv:222062` agrees with identifier, exact label, SPECIES rank, parent `NCBITaxon:2628852`, genetic code 11, empty synonym fields, and snapshot 2026-09-13. Read the complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31542`; it also retains the exact identity.

Inspected full current responses from [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035400&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035400). The name, species rank, parent, bacterial domain, and genetic code agree. All ten lineage entries agree with the pinned parent chain: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Vibrionales, Vibrionaceae, Photobacterium, and unclassified Photobacterium. Datasets explicitly includes root.

The isolate-style label does not justify replacing NCBI's rank, inferring a named-species synonym, or assigning culture-deposit equivalence. EXACT denotes this identifier match, not formal nomenclatural standing or genome identity. The inspected XML supplies no alternate name or type designation. Exact-target checks of pinned type-material, merged-ID, and dropped inventories returned no rows.

## Evidence

- `data/taxa/PATHS.tsv:14553` maps the identifier to this slug; `curation/seed_scope.tsv:322333` supplies the 2026-09-13 scope addition and attestation reason retained in the event.
- The single NCBITAXON attestation has the correct source identifier, exact label, count 1, unit NAME, and snapshot. Exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories are empty. No child taxon was found in the pinned backbone. Zero associated strain records does not deny the isolate's strain designation.
- Read the three manifest timestamp fields and `src/taxonmech/seed.py:139` timestamp-selection logic this turn. Raw is 2026-09-13T17:50:44Z, AllTheBacteria 17:54:04Z, and StrainInfo 17:29:00Z. Their maximum matches the target's 2026-09-13T17:54:04Z seed event. Source hashes were not recomputed.
- Exact `txid1035400[Organism:noexp]` searches returned zero Assembly records, with a phrase-not-found warning, and one nucleotide UID, 333798003. Read the complete returned nucleotide metadata, references, and features, excluding sequence bases. [JF792721.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792721.1) is a 1,251-base partial 16S rRNA sequence explicitly assigned to squidInt_09 and taxon 1035400, not a genome or assembly.
- Sequence source qualifiers state host `Nototodarus gouldi` verbatim and locality `New Zealand: North Island, Auckland Fish Market`. No explicit anatomical isolation site is supplied. No BioSample, BioProject, assembly, or culture-deposit accession appears in this metadata.
- The Wollenberg/Rainey/Ruby research reference is marked Unpublished and supplies no DOI or PMID. Its separate Wollenberg/Ruby direct submission is dated 07-APR-2011 at the University of Wisconsin, Madison. The bioluminescence-related research title is not an isolate-level measurement or phenotype result.
- The independent [NCBI genome Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035400/dataset_report) was an empty object. No supported target genome link was identified in the checked sources. This is not proof that no genome exists elsewhere under a different identity.
- Before open-web discovery, successfully ran `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` with read-only network access and inspected all 28 rows. No Photobacterium dataset was listed; Vibrio natriegens datasets are not transferable. iModulonDB is not applicable, not negative biological evidence.
- Bounded web discovery covered the exact name, hyphenated and space-separated designations, authors, JF792721, genome/strain terms, and the sequence research title. Results were taxonomy listings or unrelated leads. No inspected exact-isolate publication supplied a missing experimental claim. This is not an exhaustive literature census, and neighboring isolates' evidence was not transferred.

## Completeness

Used `rg --no-ignore --hidden -n -z -i` for the taxon ID, exact label, slug, and designation variants within `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed contents were included. All three matching rows were read: backbone, scope, and native scientific name.

All five SOURCE.json metadata files were separately parsed in full, and history filenames were checked without ignore filtering; no target match was found there. A second search for JF792721 and its version over the same roots returned zero matching content lines; metadata and history-filename checks likewise returned none. These bounds do not encompass all external repositories or every downloadable source snapshot. An ignored-inclusive review-directory filename check found no earlier report for this target before this report was added.

The empty optional nomenclature, mapping, strain/deposit, genome, and graph slots fit the inspected evidence. The partial marker and host/locality qualifiers could support future typed enrichment, but are not missing required genome assertions. Do not infer an anatomical site from Int or silently correct the source's host spelling without separate authority evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the stated individual-review bounds. The identity, carried NCBI lineage, source count, attestation, and seed event are supported. Pass does not certify globally exhaustive evidence or corpus-wide reproducibility.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED lifecycle status.

Optional JF792721.1 enrichment needs an owned maintained input and a supported typed representation preserving nucleotide-marker identity and exact linkage, outside genome counts. New phenotype or habitat claims require inspected isolate-specific evidence, not an abbreviation, research title, or another strain's result.

## Follow-up Checks

After a maintained-input change, verify taxon, strain/deposit, and sequence identities at their authorities; rerun target schema and strict validation; then run documented full-corpus reproduction and QC before asserting corpus-wide correctness. Route transform or seeder fixes through their owning modules with focused regression coverage.

Any future experimental assertion needs a primary source documenting this isolate, conditions, and measured result. No unresolved blocker was identified; the stated source-coverage bounds remain.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The other session is closed and the existing checkout was retained. No YAML, inventory, prior report, generated output, history artifact, GitHub item, or Eukaryota record was changed. No paid research or external contact occurred.
