# YAML Record Review: bacterium enrichment culture clone En_UW_64

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_64.yaml`
- Started UTC: 2026-10-08T19:37:40Z
- Finished UTC: 2026-10-08T19:40:34Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036450`, bacterium enrichment culture clone En_UW_64. It records species rank, Bacteria domain, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and zero represented strains. One NCBITAXON name attestation and one seed event are present; nomenclature, synonyms, additional taxonomy mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_64.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_64.yaml --out /private/tmp/uw64-strict.tsv`: passed, one file and zero errors. The complete TSV was header-only.
- Structured comparisons verified the full backbone row, all four ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide/protein XML parsing confirmed declared versus actual lengths and equality of the submitted CDS translation with its own protein. This is annotation consistency, not independent translation, alignment or an activity assay.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded seed event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused substitute was invented for a corpus-wide validator.

## Identity and Grounding

The complete [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036450&retmode=xml) agrees with the exact identifier, label, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036450) confirms root-first ancestor IDs 1, 131567, 2 and 48479. All ancestor labels and ranks match pinned rows. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

This is an environmental clone taxon at NCBI species rank, not a formally named species or demonstrated pure isolate. Exact grounding refers to identifier identity. EFetch provides no other names; pinned synonym fields are empty. Full pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222452`: identity, rank, parent, code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31996`: exact scientific-name object and empty unique name.
- `data/taxa/PATHS.tsv:14959`: identifier and slug.
- `curation/seed_scope.tsv:322699`: admission date and one-source reason matching the embedded seed event.

The attestation unit is `NAME`, not strain, assembly or experiment. Complete exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows, consistent with zero represented strains and one source attestation.

Exact non-expanded Nuccore query `txid1036450[Organism:noexp]` returned one record, UID 336092444. The complete [HQ630188.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630188.1) assigns a 346-base partial `nosZ` CDS to the same clone and taxon. Qualifiers describe an anode-biofilm environmental sample and H2S-supplemented mineral medium. Both CDS ends are partial, codon start is 3 and translation table is 11; no strain, culture-deposit or geographic qualifier is supplied.

The complete linked [AEI00846.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00846.1) reciprocally identifies HQ630188.1 and the same clone/taxon. Its 114-residue conceptual translation carries a PRK02888/CDD:235082 region through residue 108. Declared and actual lengths agree, and the submitted translation equals the protein sequence. No non-ACGT DNA or ambiguous amino-acid symbols were found. Both records cite an unpublished enrichment study and a 17-NOV-2010 submission, without a PMID or DOI for that study. These annotations support fragment provenance, not measured enzyme activity, culture purity, a complete pathway or whole-organism phenotype.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, includes HQ630188 in the enrichment-derived nosZ range HQ630075-HQ630210. Page 92 cautions that one DGGE band does not establish purity. Both pages were read completely. Exact accession/clone searches across all 164 pages of extractable text returned no match. This is study context, not clone-specific species identification; raster and supplementary content were not exhaustively searched.

The clone-label web query excluding the already checked NCBI Taxonomy site and separate HQ630188/AEI00846 queries returned no results. Exact accession/clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matching text. These bounded searches do not prove literature absence. No community-level result was assigned to this clone.

## Completeness

Complete enough for the supported taxonomy seed. Optional nomenclature, synonyms, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. An external partial gene is not an assembly or a required taxonomy-record slot.

Expanded searches used `rg --no-ignore --hidden -n -z -i` across ignored and compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. Only backbone, scientific-name and scope rows matched; all were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence claims are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning, not universal genome absence. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: the record contains no gene, regulator or expression claim, and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. Limited characterization of the external environmental fragment is not a defect in this taxonomy seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not transfer a neighboring clone's accessions, species assignment, isolate identity or phenotype, or infer these from medium and study membership.

Future taxonomy corrections belong first at NCBI and then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with a regression test; scope changes belong in `curation/seed_scope.tsv`. Optional sequence provenance requires supported maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up is required. Before optional biological enrichment, inspect primary evidence explicitly linking this exact clone to the proposed isolate, genome or experiment.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036450`, inspect emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. This review ran no generation command.

## Additional Notes

The single-record skill, local checklist, ownership guidance and documented validators governed this review. Own source rows and accession records were inspected independently. Before/after YAML SHA-256 was `e6459fa3918ef92e0eb98d3d1b415f799e86c48f3c256c6a0c26ead76d7b2321`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.

