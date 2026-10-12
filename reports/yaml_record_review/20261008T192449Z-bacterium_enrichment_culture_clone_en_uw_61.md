# YAML Record Review: bacterium enrichment culture clone En_UW_61

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_61.yaml`
- Started UTC: 2026-10-08T19:21:14Z
- Finished UTC: 2026-10-08T19:24:49Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord` for `NCBITaxon:1036447`, bacterium enrichment culture clone En_UW_61. It asserts species rank, Bacteria domain, parent `NCBITaxon:48479`, code 11, exact grounding, seeded mapping status and zero represented strains. One NCBITAXON name attestation and one seed event are present; nomenclature, synonyms, other taxonomy mappings, strain/genome links and graphs are unasserted.

An ignored-inclusive filename search of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no previous report for its stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_61.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_61.yaml --out /private/tmp/uw61-strict.tsv`: passed, one file and zero errors. The full diagnostic TSV contained only its header.
- Structured comparisons confirmed identity, all four ancestors, source attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Declared nucleotide/protein lengths matched actual lengths; submitted CDS translation exactly matched the linked protein. This is annotation consistency, not independent translation, alignment or experimental validation.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. These individual checks do not demonstrate corpus reproduction. The embedded seed event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused substitute was invented for a corpus-wide gate.

## Identity and Grounding

The full [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036447&retmode=xml) agrees with the ID, label, species rank, parent 48479 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036447) confirms root-first ancestor IDs 1, 131567, 2 and 48479. Pinned ancestor labels and ranks agree with the YAML. EFetch's displayed lineage omits root while Datasets includes it; this is not a contradiction.

The record denotes an environmental clone taxon at NCBI species rank, not a formally named species or demonstrated pure isolate. `EXACT` describes identifier grounding. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

The complete local source chain was inspected:

- `data/raw/ncbitaxon_taxa.tsv:222449`: identity, rank, parent, code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31993`: exact scientific-name object, with empty unique name.
- `data/taxa/PATHS.tsv:14956`: identifier and slug.
- `curation/seed_scope.tsv:322696`: admission date and one-source reason matching the embedded event.

The assertion unit is `NAME`, not organism, strain, assembly or experiment. Exact scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no target rows. Zero represented strains and one source attestation are consistent with these inputs.

Exact non-expanded Nuccore query `txid1036447[Organism:noexp]` returned one record, UID 336092438. The complete [HQ630185.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630185.1) assigns a 346-base partial `nosZ` CDS to the same clone and taxon. Its qualifiers describe an anode-biofilm environmental sample and H2S-supplemented mineral medium. Both CDS ends are partial, codon start is 3 and translation table is 11. No strain, culture-deposit or geographic qualifier is supplied.

The complete linked [AEI00843.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00843.1) reciprocally identifies HQ630185.1 and the same clone/taxon. Its 114-residue conceptual translation carries a PRK02888/CDD:235082 region through residue 109. Actual lengths agree with declared lengths; the submitted CDS translation equals its own protein sequence. No non-ACGT DNA or ambiguous amino-acid symbols were found. Both records cite an unpublished enrichment study and a 17-NOV-2010 direct submission, with no PMID or DOI for that study. These establish submitted fragment provenance, not measured enzyme activity, culture purity, a complete pathway or whole-organism phenotype.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, includes HQ630185 in the enrichment-derived nosZ range HQ630075-HQ630210. Page 92 cautions that a single DGGE band does not establish purity. Both pages were read completely. Exact accession/clone searches over all 164 pages of extractable text returned no match. This is study context, not clone-specific species identification; raster and supplementary content were not exhaustively searched.

The clone-label web query excluding the already checked NCBI Taxonomy site and separate HQ630185/AEI00843 queries returned no results. Exact accession/clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matching text. These bounded searches do not prove literature absence. No community-level result was assigned to the clone.

## Completeness

Complete enough for the supported taxonomy-seed scope. Optional nomenclature, mappings, synonyms, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. A partial external gene is not an assembly or a required taxonomy-record field.

Expanded searches used `rg --no-ignore --hidden -n -z -i` across ignored and compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. Only backbone, scientific-name and scope rows matched; all were read in full. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence claims are bounded to these roots and expressions.

The exact non-expanded Assembly query returned zero with a phrase-not-found warning, not universal genome absence. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: the YAML asserts no gene, regulator or expression claim, and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. Limited characterization of the external environmental fragment does not make the taxonomy seed unsupported.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status. Do not transfer neighboring clones' accessions, isolate identities, species assignments or phenotypes, or infer them from medium and common study membership.

Future taxonomy corrections belong first at NCBI and then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with a regression test; scope changes belong in `curation/seed_scope.tsv`. Optional sequence provenance needs supported maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up is required. Optional biological enrichment requires primary evidence explicitly linking this exact clone to the proposed isolate, genome or experiment.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036447`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. This review ran no generation command.

## Additional Notes

The single-record skill, local checklist, ownership guidance and documented validators governed the review. Own source rows and accession records were inspected independently. Before/after YAML SHA-256 was `8a7e1f90d6142c50a9b8ba639c1c42f1a8c16c4026eaa4bb4a1bcf4498c676de`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.

