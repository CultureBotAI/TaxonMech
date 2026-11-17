# YAML Record Review: bacterium enrichment culture clone En_UW_59

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_59.yaml`
- Started UTC: 2026-10-08T19:06:06Z
- Finished UTC: 2026-10-08T19:13:11Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036445`, bacterium enrichment culture clone En_UW_59. It records species rank, Bacteria domain, parent `NCBITaxon:48479`, genetic code 11, exact grounding, seeded mapping status and zero represented strains. Its one name attestation and one seed event assert no isolate, assembly, phenotype or causal graph.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no existing report for this stem. The generated YAML is not the maintained surface for corrections.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_59.yaml`: passed, no issues.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_59.yaml --out /private/tmp/uw59-strict.tsv`: passed, one file and zero errors. The full diagnostic TSV contained only its header.
- Structured source comparisons checked the full target backbone row, all four ancestors, seven supplementary raw inventories, PATHS, scope, type-material, merged-ID and dropped tables. Identity, lineage, attestation and seed wording agree.
- Complete submitted nucleotide/protein XML parsing confirmed actual lengths and exact equality of the submitted CDS translation with its own protein sequence. This tests annotation consistency, not independent translation, alignment or enzyme function.

Not checked: `just verify-corpus`, full-corpus schema validation, global provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded seed event was inspected; bounded searches found no separate target history artifact. `just validate-products` is not applicable without graph nodes. No focused substitute was invented for a corpus-wide gate.

## Identity and Grounding

The full [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036445&retmode=xml) agrees with the target ID, label, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036445) confirms ancestor IDs 1, 131567, 2 and 48479. All YAML ancestor labels and ranks agree with pinned source rows. EFetch omits root from its displayed lineage, whereas Datasets includes it; this is not a conflict.

This is an environmental clone assigned NCBI species rank, not a formally named species or demonstrated pure isolate. `EXACT` describes identifier grounding, not biological characterization. Live EFetch supplies no other names, and pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

The complete source chain was inspected:

- `data/raw/ncbitaxon_taxa.tsv:222447`: exact identity, rank, parent, genetic code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31991`: exact scientific-name object and empty unique-name field.
- `data/taxa/PATHS.tsv:14954`: identifier and slug.
- `curation/seed_scope.tsv:322694`: admission date and one-source reason agreeing with the embedded seed event.

The assertion unit is `NAME`, not strain, genome or experiment. Complete exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Zero represented strains and no additional source attestations are consistent with these inputs.

One extra local numeric match was inspected in full: `data/catalog/ncbi_genbank-0063.jsonl.gz:44276` describes assembly `GCA_964786765.1`, a Rickettsiaceae bacterium with taxon and species ID `2023360`. Both genome-size fields equal `1036445`; they are lengths, not the target taxon identifier. Its sample `SAMEA117430856`, project `PRJEB75477` and metagenome assembly must not be attached to En_UW_59.

Exact non-expanded Nuccore query `txid1036445[Organism:noexp]` returned one record, UID 336092434. The complete [HQ630183.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630183.1) identifies the same taxon and clone. It contains a 340-base partial `nosZ` CDS, anode-biofilm source, environmental-sample status and H2S-supplemented mineral medium. Both CDS ends are partial, codon start is 3 and translation table is 11. It supplies no strain, culture-deposit or geographic qualifier.

The full reciprocal [AEI00841.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00841.1) identifies HQ630183.1 and the same clone/taxon. Its conceptual translation has 112 residues, with a PRK02888/CDD:235082 region through residue 112. Actual lengths equal declared lengths, its sequence exactly matches the submitted CDS translation, and neither non-ACGT DNA nor ambiguous amino-acid symbols were found. The records cite an unpublished enrichment study and a 17-NOV-2010 submission, with no PMID or DOI for that unpublished reference. Submitted fragment provenance does not establish enzyme activity, culture purity, a complete pathway or organism-level phenotype.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, places HQ630183 within the enrichment-derived nosZ range HQ630075-HQ630210. Page 92 explains why one DGGE band cannot establish culture purity. Both pages were read completely. Exact accession/clone searches across all 164 pages of extractable text returned no match. This provides study context, not a clone-specific species assignment; raster and supplementary content were not exhaustively searched.

The clone-label web query excluding the already checked NCBI Taxonomy site returned no results, as did own-accession discovery queries for HQ630183 and AEI00841. Exact accession/clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matching text. These bounded searches do not establish literature absence, and no community-level result was assigned to the clone.

## Completeness

The supported taxonomy seed is complete enough for its scope. Optional nomenclature, synonyms, mappings, strain deposits, assemblies and graphs are appropriately unfilled without an explicit identity chain. A partial external gene is not an assembly and is not a mandatory taxonomy-record field.

Expanded searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored and compressed files. Expressions covered taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. Exactly four rows matched: backbone, scientific name, scope and the unrelated assembly-length collision. All were read completely. Five source `SOURCE.json` files were separately parsed in full without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

The exact non-expanded Assembly query returned zero with a phrase-not-found warning, not proof that no genome exists anywhere. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: the YAML asserts no gene, regulator or expression claim, and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. Limited characterization of an external environmental fragment and an unrelated numeric search match are not defects in this taxonomy seed.

## Recommended Edits

None required. Preserve the generated YAML and its `SEEDED` status. Do not import the unrelated assembly or transfer neighboring clones' accessions, species assignments, isolate identities or phenotypes.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A demonstrated projection defect belongs in `src/taxonmech/seed.py` with a regression test; a scope correction belongs in `curation/seed_scope.tsv`. Optional sequence provenance requires supported maintained input and appropriate model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up is required. Before optional biological enrichment, inspect primary evidence explicitly linking this clone to the proposed isolate, genome or experiment. Recheck authority records when a later snapshot changes identity or lineage.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036445`, inspect the generated YAML, rerun both individual validators and `just verify-corpus`, then perform full publication QC. This review ran no generation command.

## Additional Notes

The single-record review skill, local checklist, ownership guidance and documented validators governed this review. Own source rows and accession records were inspected independently. Before/after YAML SHA-256 was `ca32436ee35b963426723ee3d480d43f13d2b3e3eb522f6bd9ac6b1530202702`.

Only this timestamped report was written for the target. No source, record, history, status, generated page or GitHub object was changed. Existing worktrees and all Eukaryota records remained untouched.

