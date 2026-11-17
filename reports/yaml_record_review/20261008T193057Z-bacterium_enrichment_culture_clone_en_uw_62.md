# YAML Record Review: bacterium enrichment culture clone En_UW_62

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_62.yaml`
- Started UTC: 2026-10-08T19:27:33Z
- Finished UTC: 2026-10-08T19:30:57Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036448`, bacterium enrichment culture clone En_UW_62. It asserts species rank, Bacteria domain, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and zero represented strains. One NCBITAXON name attestation and one seed event are present. Synonyms, nomenclature, other taxonomy mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no previous report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_62.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_62.yaml --out /private/tmp/uw62-strict.tsv`: passed, one file and zero errors. The complete diagnostic TSV was header-only.
- Structured comparisons checked the full backbone row, all four ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide/protein XML parsing confirmed actual versus declared lengths and equality of the submitted CDS translation with its own protein. This is annotation consistency, not independent translation, alignment or an activity assay.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded seed event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused replacement was invented for a corpus-wide validator.

## Identity and Grounding

The full [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036448&retmode=xml) agrees with the identifier, name, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036448) confirms root-first ancestor IDs 1, 131567, 2 and 48479. All YAML ancestor labels and ranks match pinned rows. EFetch omits root from its displayed lineage while Datasets includes it; that is not a conflict.

This is an environmental clone taxon at NCBI species rank, not a formally named species or demonstrated pure isolate. Exact grounding refers to the identifier. EFetch provides no other names, and pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222450`: identity, rank, parent, code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31994`: exact scientific-name object and empty unique-name field.
- `data/taxa/PATHS.tsv:14957`: identifier and slug.
- `curation/seed_scope.tsv:322697`: admission date and one-source reason matching the seed event.

The assertion unit is `NAME`, not strain, assembly or experiment. Complete exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows, consistent with the represented strain count and single source attestation.

The additional local numeric match was read in full: `data/catalog/ncbi_genbank-0059.jsonl.gz:40682` describes `GCA_947484335.1`, Nitrosomonadaceae bacterium isolate RH-9nov16-7, with taxon and species ID `2026767`. Its genome-size fields equal `1036448`; those values are lengths, not the target identifier. This metagenome-derived assembly, sample `SAMEA112176035` and project `PRJEB35770` must not be linked to En_UW_62.

Exact non-expanded Nuccore query `txid1036448[Organism:noexp]` returned one record, UID 336092440. The complete [HQ630186.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630186.1) assigns a 346-base partial `nosZ` CDS to the same taxon and clone. It supplies an anode-biofilm source, environmental-sample status and H2S-supplemented mineral medium. Both CDS ends are partial, codon start is 3 and translation table is 11; no strain, culture-deposit or geographic qualifier is provided.

The complete linked [AEI00844.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00844.1) reciprocally identifies HQ630186.1 and the same clone/taxon. It contains a 115-residue conceptual translation and a PRK02888/CDD:235082 region through residue 109. Actual lengths agree with declared lengths, and the submitted translation equals the linked protein sequence. No non-ACGT DNA or ambiguous amino-acid symbols were found. Both records cite an unpublished enrichment study and a 17-NOV-2010 direct submission, without a PMID or DOI for that study. Submitted fragment provenance does not establish measured enzyme activity, culture purity, a complete pathway or organism-level phenotype.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, places HQ630186 within the enrichment-derived nosZ range HQ630075-HQ630210. Page 92 cautions that one DGGE band does not prove purity. Both pages were read completely. Exact accession/clone searches across all 164 pages of extractable text returned no match. This is study context, not a clone-specific species assignment; raster and supplementary content were not exhaustively searched.

The clone-label web query excluding the already checked NCBI Taxonomy site and separate HQ630186/AEI00844 queries returned no results. Exact accession/clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matching text. These bounded searches do not establish literature absence. No community-level result was transferred to this clone.

## Completeness

Complete enough for the supported taxonomy seed. Empty optional nomenclature, synonyms, mappings, deposits, genomes and graphs are appropriate without an explicit identity chain. An external partial gene is not an assembly or a required taxonomy-record slot.

Expanded searches used `rg --no-ignore --hidden -n -z -i` across ignored and compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Patterns included taxid, slug, clone-label variants, own sequence/protein accessions, unpublished study title and PLOS DOI. Exactly four rows matched: backbone, scientific name, scope and the unrelated assembly-length collision; all were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match, and history filenames were independently inventoried. Absence claims are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning, not universal genome absence. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: the YAML asserts no gene, regulator or expression claim, and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. An unrelated numeric match and limited biological characterization of an external environmental fragment are not defects in this taxonomy seed.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status. Do not import the unrelated assembly, or transfer a neighboring clone's sequence accession, isolate identity, species assignment or phenotype.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with a regression test; scope changes belong in `curation/seed_scope.tsv`. Optional sequence provenance needs supported maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up is required. Optional biological enrichment first requires primary evidence explicitly linking this clone to the proposed isolate, genome or experiment.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036448`, inspect emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command was run by this review.

## Additional Notes

The single-record skill was reread; the local checklist, ownership guidance and documented validators governed this review. Own source rows and accession records were inspected independently. Before/after YAML SHA-256 was `13f7a0c9d5525e01bd59aa72e233ccf1e1582f533bca45a67b603ee4b8b57e9b`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.

