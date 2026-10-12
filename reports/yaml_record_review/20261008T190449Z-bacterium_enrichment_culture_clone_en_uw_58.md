# YAML Record Review: bacterium enrichment culture clone En_UW_58

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_58.yaml`
- Started UTC: 2026-10-08T19:01:09Z
- Finished UTC: 2026-10-08T19:04:49Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord` for `NCBITaxon:1036444`, bacterium enrichment culture clone En_UW_58. It records `SPECIES`, `BACTERIA`, parent `NCBITaxon:48479`, code 11, `EXACT` grounding, `SEEDED` mapping status and zero strains. One NCBITAXON name attestation and one seed event are present; no synonyms, nomenclature, taxonomy mappings, strain/genome links or causal graph are asserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no previous report for its stem. Generated YAML is not the maintained surface for a future correction.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_58.yaml`: passed, no issues.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_58.yaml --out /private/tmp/uw58-strict.tsv`: passed, one file and zero errors. The complete TSV contained only its header.
- Structured scans compared the complete backbone and all four ancestors, seven supplementary raw inventories, PATHS, scope, type-material, merged-ID and dropped tables. Recorded identity, lineage, attestation and seed-event wording agree with their source rows.
- Complete nucleotide/protein XML parsing confirmed declared versus actual lengths and exact equality of the submitted CDS translation with its own protein sequence. This is annotation consistency, not independent translation, alignment or an experimental assay.

Not checked: `just verify-corpus`, full-corpus schema validation, global provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. The individual checks do not prove corpus reproduction. The embedded seed event was inspected; no separate target history artifact was found in the bounded searches below. `just validate-products` is not applicable because no graph nodes are present. No invented focused replacement was used for a corpus-wide validator.

## Identity and Grounding

The complete [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036444&retmode=xml) agrees with the exact identifier, label, species rank, parent 48479 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036444) confirms root-first ancestor IDs 1, 131567, 2 and 48479. All YAML ancestor labels and ranks match pinned rows: root, cellular organisms, Bacteria and environmental samples. EFetch omits root from its displayed lineage while Datasets includes it; that is not a contradiction.

This is an environmental clone taxon at NCBI species rank, not a formally named species or demonstrated pure isolate. `EXACT` refers to identifier grounding. Live EFetch provides no other names, and pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

The source chain was read completely:

- `data/raw/ncbitaxon_taxa.tsv:222446`: identity, rank, parent, code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31990`: exact scientific-name object, with an empty unique-name field.
- `data/taxa/PATHS.tsv:14953`: exact identifier and slug.
- `curation/seed_scope.tsv:322693`: admission date and one-source reason matching the seed event.

The single assertion has unit `NAME`, not organism, strain, assembly or experiment. Complete exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Zero represented strains and no additional source attestations are consistent with those inputs.

Exact non-expanded Nuccore query `txid1036444[Organism:noexp]` returned one record, UID 336092432. Its complete [HQ630182.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630182.1) assigns a 340-base partial `nosZ` CDS to this taxon and clone En_UW_58. It supplies an anode-biofilm source, environmental-sample status and H2S-supplemented mineral medium. Both CDS ends are partial, codon start is 3 and translation table is 11. No strain, culture deposit or geographic qualifier is supplied.

The complete linked [AEI00840.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00840.1) reciprocally identifies HQ630182.1 and the same taxon/clone. Its 112-residue conceptual translation carries a PRK02888/CDD:235082 region through residue 112. Actual lengths agree with declared lengths, the submitted CDS translation exactly matches its protein, and no non-ACGT DNA or ambiguous amino-acid symbols were found. Both records cite an unpublished enrichment study and a 17-NOV-2010 direct submission, without a PMID or DOI for the unpublished reference. These support submitted fragment provenance, not measured enzyme activity, culture purity, a complete pathway or whole-organism phenotype.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, lists enrichment-derived nosZ accessions HQ630075-HQ630210, including HQ630182. Page 92 cautions that one DGGE band does not establish purity. Both pages were read completely. Exact accession/clone searches across all 164 pages of extractable text returned no match. This is study context, not a clone-specific species assignment; raster and supplementary content were not exhaustively searched.

The clone-label web query excluding the already checked NCBI Taxonomy site returned no results. Discovery queries for HQ630182, AEI00840.1 and AEI00840 with nosZ supplied no additional verified biological source; an implant-catalog search lead was not used as evidence. Exact accession/clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matching text. No community-level result was transferred to this clone. These bounded searches do not prove literature absence.

## Completeness

Complete enough for the supported taxonomy seed. Empty optional nomenclature, mappings, deposits, genomes, synonyms and graphs are appropriate without an explicit identity chain. An external partial gene is not an assembly and is not a mandatory taxonomy-record slot.

Expanded searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored and compressed files. Patterns covered taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. Only backbone, scientific-name and scope rows matched; all were read completely. Five source `SOURCE.json` files were separately parsed in full without a target identity match; history filenames were separately inventoried. Absence claims are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning, not universal genome absence. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: the record contains no gene, regulator or expression claim, and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. The external environmental fragment's limited biological characterization does not make the taxonomy seed unsupported.

## Recommended Edits

None required. Preserve the generated record and its `SEEDED` status. Do not transfer a neighboring clone's accessions, isolate identity, species assignment or phenotype, or infer those from medium and shared study membership.

Future taxonomy corrections belong first at NCBI and then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A demonstrated projection defect belongs in `src/taxonmech/seed.py` with a regression test; a scope decision belongs in `curation/seed_scope.tsv`. Optional sequence provenance needs supported maintained input and appropriate model/seeder handling, not direct YAML edits.

## Follow-up Checks

No corrective follow-up is required. Before optional biological enrichment, inspect primary evidence explicitly connecting this exact clone to the asserted isolate, genome or experiment. Recheck the exact authority records if a later snapshot changes identity or lineage.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036444`, inspect the emitted YAML, rerun both record validators and `just verify-corpus`, then use full publication QC. No generation command was run by this review.

## Additional Notes

The single-record skill was reread; the local checklist, ownership guidance and documented validators governed the review. Its own source rows and accession records were inspected independently. Before/after YAML SHA-256 was `24b74ef48935b46970cef02ec1460f96e6a23643382ad82e379bc23757e744c3`.

Only this new timestamped report was written for this target. No record, source, history, status, generated page or GitHub object was changed. Existing worktrees and Eukaryota remained untouched.
