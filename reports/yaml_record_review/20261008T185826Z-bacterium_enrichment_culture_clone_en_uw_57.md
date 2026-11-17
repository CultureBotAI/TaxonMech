# YAML Record Review: bacterium enrichment culture clone En_UW_57

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_57.yaml`
- Started UTC: 2026-10-08T18:54:44Z
- Finished UTC: 2026-10-08T18:58:26Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036443`, bacterium enrichment culture clone En_UW_57. It records `SPECIES`, `BACTERIA`, parent `NCBITaxon:48479`, code 11, `EXACT` grounding, `SEEDED` mapping status and zero strains. One NCBITAXON name attestation and one seed event are present. Optional synonym, nomenclature, taxonomy mapping, strain/genome and graph claims are not stored.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no previous report for the stem. Generated YAML is not the maintained edit surface for a future correction.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_57.yaml`: passed, no issues.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_57.yaml --out /private/tmp/uw57-strict.tsv`: passed, one file scanned and zero errors. The full TSV contained only its header.
- Structured comparisons scanned the complete backbone, all four ancestors, seven supplementary raw inventories, PATHS, scope, type-material, merged-ID and dropped tables. Stored identity, lineage, attestation and seed-event wording agree with the source rows.
- Full nucleotide/protein XML parsing confirmed actual versus declared lengths and exact equality of the submitted CDS translation with its own protein sequence. This is annotation consistency, not independent translation, alignment or experimental function.

Not checked: `just verify-corpus`, full-corpus schema validation, global provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual comparisons are not proof of corpus reproduction. The embedded seed event was inspected; no separate target history artifact was found within the bounded searches below. `just validate-products` is not applicable because no graph nodes are present. No invented single-record replacement was used for a corpus-wide gate.

## Identity and Grounding

The full [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036443&retmode=xml) agrees with the exact identifier, label, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036443) confirms root-first ancestor IDs 1, 131567, 2 and 48479. Pinned ancestor rows agree with all YAML names and ranks: root, cellular organisms, Bacteria and environmental samples. EFetch omits root from its displayed lineage while Datasets includes it; this is not a contradiction.

The record denotes an environmental clone taxon at NCBI species rank, not a formally named species or demonstrated pure isolate. `EXACT` correctly describes identifier grounding. Live EFetch supplies no other names and pinned synonym fields are empty. Complete scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

The complete source rows inspected were:

- `data/raw/ncbitaxon_taxa.tsv:222445`: identity, rank, parent, code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31989`: exact scientific-name object with an empty unique-name field.
- `data/taxa/PATHS.tsv:14952`: exact identifier and slug.
- `curation/seed_scope.tsv:322692`: admission date and one-source reason matching the seed event.

One assertion with unit `NAME` is not one isolate, assembly or experiment. Complete exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Zero represented strains and no extra source attestations agree with those inputs.

The additional candidate `data/catalog/ncbi_genbank-0064.jsonl.gz:18137` was read in full. It is assembly `GCA_965334525.1`, Acutalibacteraceae bacterium isolate rk3_bin_269, with taxid and species taxid 3077420. The target number 1036443 appears in `genome_size` and `genome_size_ungapped`, not in a taxonomic identifier field. This numeric collision does not link the assembly, BioSample `SAMEA118407512` or project `PRJEB89408` to En_UW_57.

Exact non-expanded Nuccore query `txid1036443[Organism:noexp]` returned one result, UID 336092430. The complete [HQ630181.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630181.1) assigns a 346-base partial `nosZ` CDS to this taxon and clone En_UW_57. It supplies an anode-biofilm source, environmental-sample status and H2S-supplemented mineral medium. Both CDS ends are partial, codon start is 3 and translation table is 11. No strain, culture deposit or geographic qualifier is supplied.

The complete linked [AEI00839.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00839.1) reciprocally identifies HQ630181.1 and the same taxon/clone. Its 114-residue conceptual translation carries a PRK02888/CDD:235082 region through residue 108. Actual lengths equal declared lengths, the submitted CDS translation exactly matches this protein, and no non-ACGT DNA or ambiguous amino-acid symbols were found. Both records cite an unpublished enrichment study and a 17-NOV-2010 direct submission, without a PMID or DOI for the unpublished reference. These annotations support submitted fragment provenance, not measured enzyme activity, purity, a complete pathway or whole-organism phenotype.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, lists enrichment-derived nosZ accessions HQ630075-HQ630210, including HQ630181. Page 92 cautions that a single DGGE band cannot establish purity. Both pages were read completely. Exact accession/clone searches across all 164 pages of extractable text returned no match. This supports study context, not clone-specific species identification; raster and supplementary content were not exhaustively searched.

Exact HQ630181 and AEI00839 web queries returned no results; the clone-label query excluding the already checked NCBI Taxonomy site also returned none. Exact accession/clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matching text. No community-level experimental result was transferred to this clone. These are bounded searches, not proof of literature absence.

## Completeness

Complete enough for the supported taxonomy seed. Empty optional synonyms, nomenclature, mappings, deposits, genome links and graphs are appropriate without explicit identity evidence. An external partial gene fragment is not an assembly and is not a mandatory taxonomy-record field.

Expanded searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored and compressed files. Patterns covered taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. Four rows matched: backbone, native name, scope and the rejected genome-size collision. All were read completely. Five source `SOURCE.json` files were separately parsed in full without a target identity match; history filenames were separately inventoried. Absence claims apply only to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning, not universal genome absence. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: no gene, regulator or expression claim is stored and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. The unrelated assembly was excluded, and limited characterization of an external environmental fragment does not make the taxonomy seed unsupported.

## Recommended Edits

None required. Preserve the generated YAML and its `SEEDED` status. Do not add the unrelated assembly or infer isolate identity, phenotype or taxonomy from neighboring clones, medium or study membership.

Future taxonomy corrections belong first at NCBI and then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A demonstrated projection defect belongs in `src/taxonmech/seed.py` with a regression test; a scope decision belongs in `curation/seed_scope.tsv`. Optional sequence provenance needs supported maintained input and model/seeder handling, not direct YAML edits.

## Follow-up Checks

No corrective follow-up is required. Before optional genome or trait enrichment, inspect primary evidence explicitly linking this clone to the asserted entity or experiment. Use typed identifiers so a genome-length metric cannot become an identity join.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036443`, inspect the emitted YAML, rerun both record validators and `just verify-corpus`, then use full publication QC. No generation command was run by this review.

## Additional Notes

The single-record skill, local checklist, ownership guidance and documented validators governed the review. Its own source rows and accession records were inspected independently. Before/after YAML SHA-256 was `5d840645959b73363dadf2690d17aacc87081c4a870f88c39f580dfa6b47c813`.

Only this new timestamped report was written for this target. No record, source, history, status, generated page or GitHub object was changed. Existing worktrees and Eukaryota remained untouched.
