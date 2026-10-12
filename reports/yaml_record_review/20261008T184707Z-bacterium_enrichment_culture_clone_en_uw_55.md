# YAML Record Review: bacterium enrichment culture clone En_UW_55

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_55.yaml`
- Started UTC: 2026-10-08T18:43:28Z
- Finished UTC: 2026-10-08T18:47:07Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036441`, bacterium enrichment culture clone En_UW_55. It carries species rank, bacterial domain, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and zero strains. One NCBITAXON name attestation and one seed event are present. It makes no synonym, nomenclature, mapping, strain/genome or causal-graph claims.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved exactly this YAML and no previous report for its stem. The generated record is not a direct curation-edit surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_55.yaml`: passed with no issues.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_55.yaml --out /private/tmp/uw55-strict.tsv`: passed, one file scanned and zero errors. The complete TSV contained only its header.
- Structured comparisons scanned the complete backbone and all four ancestors, seven supplementary raw inventories, PATHS, scope, type-material, merged-ID and dropped tables. Recorded identity, lineage, attestation and seed-event wording agree with the relevant input rows.
- Full nucleotide/protein XML parsing confirmed actual and declared lengths and exact equality of the submitted CDS translation with its own linked protein sequence. This was annotation consistency, not independent translation, alignment or experimental validation.

Not checked: `just verify-corpus`, full-corpus schema validation, global provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. The source checks are bounded individual comparisons, not corpus-reproduction proof. The embedded seed event was inspected; the searches below found no separate target history artifact. `just validate-products` is not applicable because there are no graph nodes. No invented focused gate was substituted for a global validator.

## Identity and Grounding

The complete [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036441&retmode=xml) agrees with the exact identifier, label, rank, parent 48479 and code 11. The [NCBI Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036441) confirms root-first lineage IDs 1, 131567, 2 and 48479. Pinned ancestor rows agree with all YAML names and ranks: root, cellular organisms, Bacteria and environmental samples. Datasets includes root while EFetch's displayed lineage omits it; this is not a conflict.

The label denotes an environmental clone taxon at NCBI species rank, not a demonstrated pure isolate or formally named species. `EXACT` describes identifier grounding. Live EFetch provides no other names; pinned synonym fields are empty. Complete scans found no exact target type-material, merged-ID or dropped row and no children in the backbone.

## Evidence

The source chain was read completely:

- `data/raw/ncbitaxon_taxa.tsv:222443`: identity, rank, parent, code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31987`: exact scientific-name object with an empty unique-name field.
- `data/taxa/PATHS.tsv:14950`: identifier-to-slug assignment.
- `curation/seed_scope.tsv:322690`: admission date and reason agreeing with the seed event.

The single attestation has unit `NAME`; it is not an isolate, assembly or experimental count. Complete exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Zero represented strains and no extra source attestations are consistent with those inputs.

Exact non-expanded Nuccore search `txid1036441[Organism:noexp]` returned one result, UID 336092426. The complete [HQ630179.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630179.1) assigns a 346-base partial `nosZ` CDS to this taxon and clone En_UW_55. It supplies an anode-biofilm source, environmental-sample status and H2S-supplemented mineral medium. Both CDS ends are partial, codon start is 3 and translation table is 11. No strain, collection deposit or geographic qualifier is supplied.

The complete linked [AEI00837.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00837.1) reciprocally identifies HQ630179.1 and the same taxon/clone. Its conceptual translation is 114 residues, with a PRK02888/CDD:235082 region through residue 109. Both actual lengths equal their declared values; the submitted CDS translation matches this protein exactly. No non-ACGT DNA symbols or ambiguous amino-acid symbols were found. The verified protein length is specific to this accession and was not inferred from adjacent clones.

Both records cite an unpublished enrichment study and a 17-NOV-2010 direct submission, with no PMID or DOI for the unpublished reference. These annotations support submitted fragment identity and provenance, not measured nitrous-oxide reduction, isolate purity, a complete pathway or whole-organism physiology. A medium qualifier does not provide those missing experimental claims.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, lists enrichment-derived nosZ accessions HQ630075-HQ630210, including HQ630179. Page 92 cautions that a single DGGE band cannot prove purity. Both pages were read completely. Searching all 164 pages of extractable text for the exact accession and clone returned no match. This supports study context, not clone-specific species identification; raster and supplementary content were not exhaustively searched.

The clone-label web query excluding the already checked NCBI Taxonomy site returned no results. Discovery searches for HQ630179, AEI00837.1 and AEI00837 with nosZ supplied no additional verified biological source; an implant-catalog search lead was not used as biological evidence. Exact accession/clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matching text. No community-level result was assigned to this clone. These are bounded searches, not proof of literature absence.

## Completeness

Complete enough for the supported taxonomy seed. Optional synonyms, nomenclature, mappings, deposits, genome links and graphs should remain empty without an explicit supporting identity chain. The external partial gene is not an assembly and is not a mandatory taxonomic-record slot.

Expanded searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored and compressed files. Patterns covered taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. Only backbone, native scientific name and scope rows matched; all were read completely. Five source `SOURCE.json` files were separately parsed in full without a target identity match; history filenames were separately inventoried. Absence claims apply only to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. This establishes no result under that exact query, not universal genome absence. No independent UniProt or pure-isolate identity was established; a sibling clone's UniProt/archive identity was not transferred. iModulonDB was not run because no gene, regulator or expression claim is stored and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. The environmental fragment's limited biological characterization does not make this correctly grounded taxonomy seed unsupported.

## Recommended Edits

None required. Preserve the generated YAML and its `SEEDED` status. Do not infer a strain, genome, UniProt accession or phenotype from a neighboring clone, medium or shared study.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A demonstrated projection defect belongs in `src/taxonmech/seed.py` with a regression test; a scope decision belongs in `curation/seed_scope.tsv`. Optional sequence provenance requires supported maintained input and appropriate schema/seeder handling, not hand-edited YAML.

## Follow-up Checks

No corrective follow-up is required. Before optional biological enrichment, inspect primary evidence explicitly linking this exact clone to the asserted isolate, genome or experiment. Recheck the exact authority records if a later snapshot changes identity or lineage.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036441`, inspect the emitted YAML, rerun both record validators and `just verify-corpus`, then use full publication QC. No regeneration command was run for this review.

## Additional Notes

The review followed the single-record skill, local checklist, ownership guidance and documented validators. Its source and accession evidence was inspected independently. Before/after YAML SHA-256 was `72788b7082ec9463a61dd81e875b3cf8b610936b4605169735edb1af3e9589e7`.

Only this new timestamped report was written for this target. No YAML, inventory, history, status, generated page or GitHub object was changed. Existing worktrees and the fully covered Eukaryota corpus remained untouched.
