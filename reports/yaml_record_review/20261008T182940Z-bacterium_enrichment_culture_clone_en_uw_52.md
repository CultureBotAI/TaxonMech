# YAML Record Review: bacterium enrichment culture clone En_UW_52

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_52.yaml`
- Started UTC: 2026-10-08T18:25:33Z
- Finished UTC: 2026-10-08T18:29:40Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036438`, bacterium enrichment culture clone En_UW_52. It records `SPECIES`, `BACTERIA`, parent `NCBITaxon:48479`, code 11, `EXACT` grounding, `SEEDED` mapping status and zero strains. One NCBITAXON name attestation and one seed event are present. No optional synonym, nomenclature, taxonomy mapping, strain, genome or causal-graph claims are stored.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved exactly this YAML and no previous report for the stem. The record is generated from maintained inventories and scope, not a directly editable curation surface.

## Validation

Commands ran with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_52.yaml`: passed, no issues.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_52.yaml --out /private/tmp/uw52-strict.tsv`: passed, one file and zero error rows. The complete TSV contained only its header.
- Structured comparisons scanned the complete pinned backbone, relevant ancestors, seven supplementary raw inventories, PATHS, scope, type-material, merged-ID and dropped tables. The recorded identity, lineage, attestation and seed-event wording agree with their source rows.
- Full nucleotide/protein XML parsing confirmed declared versus actual sequence lengths and exact agreement of the submitted CDS translation with its own protein record. This is annotation consistency, not an independent translation or functional assay.

Not checked: `just verify-corpus`, full-corpus schema validation, global provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual source comparisons are not corpus-reproduction proof. The embedded seed history was inspected; no separate target history artifact was found in the bounded searches below. `just validate-products` is not applicable because there are no graph nodes. No invented focused replacement for a corpus-wide validator was used.

## Identity and Grounding

The full [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036438&retmode=xml) confirms the exact label, species rank, parent 48479 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036438) supplies ancestor IDs 1, 131567, 2 and 48479. The pinned ancestor rows agree with all YAML names and ranks: root, cellular organisms, Bacteria and environmental samples. Root is included by Datasets although omitted from EFetch's displayed lineage; this is not a conflict.

This is an environmental clone taxon at NCBI species rank, not a demonstrated pure culture or formally named species. `EXACT` correctly describes identifier grounding. Live EFetch supplies no other names; pinned synonym fields are empty. Exact scans found no target type material, merged-ID or dropped row, and no children in the complete backbone.

## Evidence

The complete inspected source rows were:

- `data/raw/ncbitaxon_taxa.tsv:222440`: identity, parent, rank, code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31984`: the exact scientific name and an empty unique-name qualifier.
- `data/taxa/PATHS.tsv:14947`: identifier-to-slug mapping.
- `curation/seed_scope.tsv:322687`: admission date and reason matching the seed event.

One `NAME` assertion is not one isolate, genome or experimental observation. Exact-target scans of the complete BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no rows; the represented zero-strain count and lack of additional attestations are consistent with those inputs.

One extra numeric search candidate was fully read: `data/catalog/ncbi_genbank-0064.jsonl.gz:15729`, assembly `GCA_965310235.1`. Its organism is Clostridia bacterium with both taxid and species taxid 2044939. The number 1036438 occurs only as `genome_size_ungapped`; total genome size is 1037271. This is a genome-length collision, not target identity evidence. Its BioSample `SAMEA118409537`, project `PRJEB89408` and assembly must not be attached to this clone.

Exact non-expanded Nuccore search `txid1036438[Organism:noexp]` returned one record, UID 336092420. The complete [HQ630176.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630176.1) identifies this taxon and En_UW_52 clone, a 340-base partial `nosZ` CDS, an anode-biofilm source, environmental-sample status and H2S-supplemented mineral medium. Both CDS ends are partial; codon start is 3 and translation table is 11. No strain, collection deposit or geographic qualifier is supplied.

Its complete linked [AEI00834.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00834.1) reciprocally identifies HQ630176.1 and the same taxon/clone. The 112-residue conceptual translation carries a PRK02888/CDD:235082 region through residue 112. Both actual lengths match their annotations, the submitted translation exactly matches the protein, and no non-ACGT DNA symbols or ambiguous amino-acid symbols were found. These are partial-sequence annotations, not measured enzyme activity or whole-organism phenotype evidence.

Both records cite an unpublished enrichment study and a direct submission dated 17-NOV-2010. Neither provides a PMID or DOI for that unpublished reference. Source medium and biofilm provenance cannot establish purity, a complete denitrification pathway or performance of an isolated organism.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, lists enrichment nosZ accessions HQ630075-HQ630210, which includes HQ630176. Page 92 cautions that a single DGGE band does not prove purity. Both pages were read completely. Exact accession/clone searches across all 164 pages of extractable text found no match. This is study context, not a clone-specific species assignment; raster and supplementary material were not exhaustively audited.

The exact HQ630176 web query and clone-label query excluding the already checked NCBI Taxonomy site returned no results. Searching unversioned AEI00834 produced an implant-catalog search lead, which was not used as biological evidence; refined AEI00834.1 and AEI00834 plus nosZ queries returned no results. Exact accession and clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matches. These bounded searches do not establish literature absence.

## Completeness

Complete enough for the stored taxonomy seed. Optional mappings, nomenclature, deposits, genome links, synonyms and graphs need not be invented. A partial gene fragment is not an assembly and is not a required taxonomy-record slot.

Expanded `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored and compressed files. Expressions included taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. Four rows matched: backbone, scientific name, scope and the rejected assembly-length collision above. All were read completely. Five source `SOURCE.json` files were separately parsed in full without a target identity match, and history filenames were separately inventoried. Absence claims are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning, not proof that a genome cannot exist elsewhere. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: the YAML has no gene, regulator or expression claim, and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. The numeric catalog collision was rejected, and the limited characterization of an external environmental fragment does not make this taxonomy seed unsupported.

## Recommended Edits

None required. Preserve the YAML and its `SEEDED` status. Do not add the unrelated assembly or infer isolate/phenotype links from medium, study membership or a neighboring clone.

Any future taxonomy correction belongs first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A demonstrated projection defect belongs in `src/taxonmech/seed.py` with a regression test; a scope change belongs in `curation/seed_scope.tsv`. Optional sequence provenance needs supported maintained input and appropriate model/seeder handling, not hand edits to `data/taxa/`.

## Follow-up Checks

No corrective follow-up is required. Before optional biological enrichment, establish an explicit target-to-isolate, target-to-genome or target-to-experiment chain from primary evidence. Check typed source fields so a numerical metric cannot become an identifier join.

For an authorized future source/seeder correction, run the focused regression test, `just seed-canary NCBITaxon:1036438`, inspect its emitted YAML, rerun both record validators and `just verify-corpus`, then use full publication QC. No regeneration command was run by this review.

## Additional Notes

The review followed the single-record skill, local checklist, ownership boundaries and documented validators. Its own source and accession records were inspected independently. Before/after YAML SHA-256 was `6815a84a0da9287ad2d116df76e57b66cca1e58edfdd831fe621c033e66a43e8`.

Only this new timestamped report was written for this target. No YAML, inventory, history, status, generated page or GitHub object was changed. Eukaryota and existing worktrees remained untouched.
