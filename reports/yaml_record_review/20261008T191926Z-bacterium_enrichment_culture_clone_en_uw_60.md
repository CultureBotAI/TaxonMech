# YAML Record Review: bacterium enrichment culture clone En_UW_60

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_60.yaml`
- Started UTC: 2026-10-08T19:15:48Z
- Finished UTC: 2026-10-08T19:19:26Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord` for `NCBITaxon:1036446`, bacterium enrichment culture clone En_UW_60. It asserts species rank, Bacteria domain, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and zero represented strains. It contains one NCBITAXON name attestation and one seed event, without synonyms, nomenclature, other taxonomy mappings, strain/genome links or a graph.

An ignored-inclusive filename search of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no previous report for its stem. This generated YAML is not the maintained correction surface.

## Validation

Commands ran with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_60.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_60.yaml --out /private/tmp/uw60-strict.tsv`: passed, one file and zero errors; the complete diagnostic TSV was header-only.
- Structured comparisons confirmed the full target backbone row, all four ancestors, source attestation, PATHS and scope rows, and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Submitted nucleotide/protein lengths and CDS-translation equality passed. This checks annotation consistency, not independent translation, alignment or experimental activity.

Not checked: corpus reproduction via `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. The embedded history event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused replacement was invented for a corpus-wide gate.

## Identity and Grounding

The complete [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036446&retmode=xml) agrees with ID, name, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036446) confirms root-first ancestor IDs 1, 131567, 2 and 48479. All ancestor labels and ranks match pinned rows. EFetch's displayed lineage omits root while Datasets includes it; this is not a conflict.

The identifier denotes an environmental clone taxon, not a formally named species or proven pure isolate. Exact grounding is an identifier assertion. EFetch supplies no other names; pinned synonym fields are empty. Full pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete source rows were read:

- `data/raw/ncbitaxon_taxa.tsv:222448`: identity, rank, parent, code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31992`: exact scientific-name object, empty unique name.
- `data/taxa/PATHS.tsv:14955`: identifier and slug.
- `curation/seed_scope.tsv:322695`: admission date and one-source reason matching the seed event.

The assertion unit is `NAME`, not strain, assembly or experiment. Exact scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no target rows, consistent with the represented strain count and single source attestation.

Exact non-expanded query `txid1036446[Organism:noexp]` returned one Nuccore record, UID 336092436. Its complete [HQ630184.1 record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630184.1) assigns a 340-base partial `nosZ` CDS to the same taxon and clone. Qualifiers identify an anode-biofilm environmental sample and H2S-supplemented mineral medium. Both ends are partial, codon start is 3 and translation table is 11; no strain, deposit or geographic qualifier is provided.

The complete linked [AEI00842.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00842.1) reciprocally identifies HQ630184.1 and the same clone/taxon. Its 112-residue conceptual translation includes a PRK02888/CDD:235082 region through residue 112. Declared and actual lengths agree; the submitted translation equals the protein sequence. No non-ACGT DNA or ambiguous amino-acid symbols were found. The records cite an unpublished enrichment study and a 17-NOV-2010 submission, without a PMID or DOI for that study. These annotations establish fragment provenance, not culture purity, measured enzyme activity, a complete pathway or whole-organism phenotype.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, includes HQ630184 in its enrichment-derived nosZ range HQ630075-HQ630210. Page 92 cautions that a single DGGE band does not prove purity. Both pages were read completely. Exact accession/clone searches across all 164 pages of extractable text returned no match. This is study context, not clone-specific species identification; raster and supplemental content were not exhaustively searched.

The clone-label web query excluding the already checked NCBI Taxonomy site and separate HQ630184/AEI00842 queries returned no results. Exact accession/clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matching text. These searches do not prove literature absence. No community-level result was transferred to this clone.

## Completeness

The taxonomy seed is complete enough for its supported scope. Optional nomenclature, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. An external partial gene is neither an assembly nor a required taxonomy-record field.

Expanded `rg --no-ignore --hidden -n -z -i` searches covered ignored and compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions included taxid, slug, clone variants, own sequence/protein accessions, unpublished study title and PLOS DOI. Only the backbone, scientific-name and scope rows matched; all were fully inspected. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence claims are bounded to these roots and expressions.

The exact non-expanded Assembly query returned zero with a phrase-not-found warning, not universal genome absence. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: the YAML has no gene/regulator/expression claim, and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. Limited characterization of an environmental fragment is not itself a defect in the taxonomy seed.

## Recommended Edits

None required. Preserve the generated record and `SEEDED` status. Do not infer species, isolate identity or phenotype from shared study membership, medium or neighboring clones.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with a regression test; scope changes belong in `curation/seed_scope.tsv`. Optional sequence provenance needs supported maintained input and suitable model/seeder handling, not direct YAML edits.

## Follow-up Checks

No corrective follow-up is required. Optional biological enrichment first needs primary evidence explicitly linking this clone to the proposed isolate, genome or experiment.

After an authorized upstream/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036446`, inspect emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. This review ran no generation command.

## Additional Notes

The review skill, local checklist, ownership guidance and documented validators governed this individual review. Own accession records and source rows were inspected independently. Before/after YAML SHA-256 was `fe9b492c2711b80ceb1b6ec33da2a78a3e23ab88b760269d05e7b69d66323ed0`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.

