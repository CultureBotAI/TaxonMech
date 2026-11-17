# YAML Record Review: bacterium enrichment culture clone En_UW_56

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_56.yaml`
- Started UTC: 2026-10-08T18:50:05Z
- Finished UTC: 2026-10-08T18:53:25Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036442`, bacterium enrichment culture clone En_UW_56. It records species rank, bacterial domain, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and zero strains. One NCBITAXON name attestation and one seed event are present. No synonyms, nomenclature, taxonomy mappings, strain/genome links or causal graph are asserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior report for the stem. The generated record remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_56.yaml`: passed, no issues.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_56.yaml --out /private/tmp/uw56-strict.tsv`: passed, one file, zero errors. The complete TSV contained only its header.
- Structured scans compared the complete backbone and all four ancestors, seven supplementary raw inventories, PATHS, scope, type-material, merged-ID and dropped tables. Recorded identity, lineage, attestation and seed-event wording agree with their source rows.
- Full nucleotide/protein XML parsing confirmed actual versus declared lengths and exact equality of the submitted CDS translation with its own protein sequence. This is annotation consistency, not independent translation, alignment or functional validation.

Not checked: `just verify-corpus`, full-corpus schema validation, global provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual comparisons are not proof of corpus reproduction. The embedded seed event was inspected; no separate target history artifact was found in the searches below. `just validate-products` is not applicable because no graph nodes are present. No invented focused replacement was used for a corpus-wide gate.

## Identity and Grounding

The full [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036442&retmode=xml) agrees with the exact identifier, label, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036442) confirms root-first ancestor IDs 1, 131567, 2 and 48479. All YAML ancestor names and ranks agree with pinned rows: root, cellular organisms, Bacteria and environmental samples. EFetch omits root from its displayed lineage; Datasets includes it. That is not a conflict.

The environmental clone has species rank in NCBI; this does not identify a formally named species or establish a pure isolate. `EXACT` appropriately describes identifier grounding. Live EFetch supplies no other names and pinned synonyms are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

The source chain was read completely:

- `data/raw/ncbitaxon_taxa.tsv:222444`: identity, rank, parent, code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31988`: exact scientific-name object with an empty unique-name field.
- `data/taxa/PATHS.tsv:14951`: exact identifier and slug.
- `curation/seed_scope.tsv:322691`: admission date and one-source reason matching the seed event.

The count of one has unit `NAME`, not organism, strain, assembly or experiment. Complete exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Zero represented strains and no additional source attestations are consistent with those inputs.

Exact non-expanded Nuccore search `txid1036442[Organism:noexp]` returned one record, UID 336092428. Its complete [HQ630180.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630180.1) assigns a 340-base partial `nosZ` CDS to this taxon and clone En_UW_56. It supplies an anode-biofilm source, environmental-sample status and H2S-supplemented mineral medium. Both CDS ends are partial, codon start is 3 and translation table is 11. No strain, culture deposit or geographic qualifier is supplied.

The complete linked [AEI00838.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00838.1) reciprocally identifies HQ630180.1 and the same taxon/clone. Its 112-residue conceptual translation carries a PRK02888/CDD:235082 region through residue 112. Actual lengths equal declared lengths, the submitted translation matches its protein exactly, and no non-ACGT DNA or ambiguous amino-acid symbols were found. Both records cite an unpublished enrichment study and a 17-NOV-2010 direct submission, without a PMID or DOI for the unpublished reference. These annotations support submitted fragment provenance, not enzyme activity, culture purity, a complete pathway or whole-organism phenotype.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, lists enrichment-derived nosZ accessions HQ630075-HQ630210, including HQ630180. Page 92 cautions that one DGGE band cannot establish purity. Both pages were read completely. Searching all 164 pages of extractable text for the exact accession/clone returned no match. This is study context, not clone-specific species identification; raster and supplementary content were not exhaustively searched.

Exact HQ630180 and AEI00838 web searches returned no results; the clone-label query excluding the already checked NCBI Taxonomy site also returned none. Exact accession/clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matching text. No community-level experimental result was transferred to this clone. These are bounded searches, not proof of literature absence.

## Completeness

Complete enough for the supported taxonomy seed. Optional synonyms, nomenclature, mappings, deposits, genomes and graphs should remain empty without an explicit supporting identity chain. An external partial gene fragment is not an assembly and is not a mandatory taxonomy-record field.

Expanded searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored and compressed files. Patterns covered taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. Only backbone, native name and scope rows matched, and all were read completely. Five source `SOURCE.json` files were separately parsed in full without a target identity match; history filenames were separately inventoried. Absence claims are bounded to those roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning, not universal genome absence. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: the record has no gene, regulator or expression claim, and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. The limited biological characterization of an environmental sequence fragment is not a defect in this taxonomy-only record.

## Recommended Edits

None required. Preserve the generated YAML and its `SEEDED` status. Do not transfer a neighboring clone's accessions, isolate identity, medium, species assignment or phenotype.

Future taxonomy corrections belong first at NCBI and then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A demonstrated projection defect belongs in `src/taxonmech/seed.py` with a regression test; a scope decision belongs in `curation/seed_scope.tsv`. Optional sequence provenance needs supported maintained input and appropriate model/seeder handling, not direct YAML edits.

## Follow-up Checks

No corrective follow-up is required. Before optional biological enrichment, inspect primary evidence explicitly linking this exact clone to an isolate, genome or experiment. Shared study, medium or sequence annotation is insufficient.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036442`, inspect the emitted YAML, rerun both record validators and `just verify-corpus`, then use full publication QC. No generation command was run for this review.

## Additional Notes

The single-record skill, local checklist, ownership guidance and documented validators governed the review. Its own source and accession records were inspected independently. Before/after YAML SHA-256 was `4d957702f1b15e3ec8dcccddd93f3dcd1072f4a0e596f35e691d12965b884937`.

Only this new timestamped report was written for this target. No record, source, history, status, generated page or GitHub object was changed. Existing worktrees and Eukaryota remained untouched.
