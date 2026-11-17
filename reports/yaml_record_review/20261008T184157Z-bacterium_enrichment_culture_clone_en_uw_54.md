# YAML Record Review: bacterium enrichment culture clone En_UW_54

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_54.yaml`
- Started UTC: 2026-10-08T18:37:44Z
- Finished UTC: 2026-10-08T18:41:57Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036440`, bacterium enrichment culture clone En_UW_54. It records `SPECIES`, `BACTERIA`, parent `NCBITaxon:48479`, code 11, `EXACT` grounding, `SEEDED` mapping status and zero strains. One NCBITAXON name attestation and one seed event are present; no synonyms, nomenclature, mappings, strain/genome links or causal graph are asserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no earlier report for the stem. The generated record remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_54.yaml`: passed, no issues.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_54.yaml --out /private/tmp/uw54-strict.tsv`: passed, one file and zero errors. The full TSV contained only its header.
- Structured scans compared the complete pinned backbone and four ancestors, seven supplementary raw inventories, PATHS, scope, type-material, merged-ID and dropped tables. Stored identity, lineage, attestation and seed-event values agree with their source rows.
- Complete nucleotide/protein XML parsing confirmed actual lengths against declared lengths and the submitted CDS translation against its own protein sequence. A separate structured comparison confirmed the entire UniParc sequence equals the NCBI protein, with matching length and target-specific cross-references.

Not checked: `just verify-corpus`, full-corpus schema validation, global provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual source checks are not corpus-reproduction proof. The embedded seed event was inspected; no separate target history artifact was found in the bounded searches below. Graph validation is not applicable because no graph nodes are present. No undocumented single-record gate was substituted for a full-corpus check. Sequence comparisons establish annotation consistency, not independent translation, alignment or experimental function.

## Identity and Grounding

The complete [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036440&retmode=xml) agrees with the identifier, label, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036440) confirms root-first ancestor IDs 1, 131567, 2 and 48479. Pinned ancestor rows agree with all YAML labels and ranks: root, cellular organisms, Bacteria and environmental samples. EFetch omits root from its displayed lineage while Datasets includes it; this is not a contradiction.

The target is an environmental clone taxon at NCBI species rank, not an identified pure culture or formally named species. `EXACT` refers to identifier grounding. Live EFetch provides no other names and pinned synonym fields are empty. Complete scans found no target type-material, merged-ID or dropped row and no children in the backbone.

## Evidence

The complete local source rows inspected were:

- `data/raw/ncbitaxon_taxa.tsv:222442`: identity, rank, parent, code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31986`: exact scientific-name object, with an empty unique-name field.
- `data/taxa/PATHS.tsv:14949`: exact ID-to-slug assignment.
- `curation/seed_scope.tsv:322689`: admission date and one-source reason matching the seed event.

The attestation count is one `NAME`, not a strain, assembly or experimental observation. Complete exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Zero represented strains and no extra source attestations agree with those inputs.

Exact non-expanded Nuccore query `txid1036440[Organism:noexp]` returned one record, UID 336092424. The complete [HQ630178.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630178.1) identifies this taxon and clone, a 346-base partial `nosZ` CDS, an anode-biofilm source, environmental-sample status and H2S-supplemented mineral medium. Both CDS ends are partial, codon start is 3 and translation table is 11. No strain, culture deposit or geographic qualifier is supplied.

The complete linked [AEI00836.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00836.1) reciprocally identifies HQ630178.1 and the same clone/taxon. Its 115-residue conceptual translation carries a PRK02888/CDD:235082 region through residue 109. Declared and actual lengths agree, the submitted translation exactly matches the protein, and no non-ACGT DNA symbols or ambiguous amino-acid symbols were found. Both sequence records cite an unpublished enrichment study and a 17-NOV-2010 direct submission without a PMID or DOI for the unpublished reference. These support submitted sequence provenance, not measured enzyme activity, isolate purity or a complete pathway.

A [CNGB search lead](https://db.cngb.org/data_resources/protein/F8SJ03) identified F8SJ03 and older unreviewed UniProt metadata. It was used only for discovery. The complete primary [UniProt response](https://rest.uniprot.org/uniprotkb/F8SJ03.json) now marks F8SJ03 inactive/deleted because it is not part of a reference proteome and points to UPI0002130F3F. The older search lead must not be described as the current UniProt entry state.

The complete [UniParc archive](https://rest.uniprot.org/uniparc/UPI0002130F3F.json) contains exactly two cross-references: inactive UniProtKB/TrEMBL F8SJ03 and active EMBL AEI00836 version 1, both naming taxon 1036440 and En_UW_54. Its entire 115-residue sequence exactly matches AEI00836.1. The archive also carries computational domain-family annotations; these are not an enzyme assay or proof of organism-level traits. This establishes bounded historical protein provenance. The YAML does not cite F8SJ03, so its deletion is not a broken record reference or a required-field defect.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, places HQ630075-HQ630210 among enrichment-derived nosZ accessions; HQ630178 falls within this range. Page 92 cautions that one DGGE band cannot establish purity. Both pages were read completely. Exact accession/clone searches across all 164 pages of extractable text returned no match. This supports study context, not a clone-specific species assignment; raster and supplementary content were not exhaustively searched.

Exact HQ630178 and AEI00836 web queries returned no results. Exact accession/clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matches. No community-level result was assigned to this clone. These bounded searches do not demonstrate literature absence.

## Completeness

Complete enough for the stored taxonomy seed. Optional mappings, nomenclature, deposits, genomes, synonyms and graphs need not be invented. The external partial gene/protein and deleted UniProt accession are not required taxonomic-record slots; a gene fragment is not an assembly.

Expanded `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored and compressed files. Patterns included taxid, slug, clone variants, own nucleotide/protein, F8SJ03, UPI0002130F3F, unpublished study title and PLOS DOI. Only backbone, scientific-name and scope rows matched; all were read completely. Five source `SOURCE.json` files were separately parsed in full without a target identity match, and history filenames were separately inventoried. Absence claims are bounded to those roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning, not universal genome absence. No pure-isolate identity or covered expression dataset was established. iModulonDB was not run: the YAML makes no gene, regulator or transcriptomics claim and no covered strain/dataset was identified. This is not negative evidence about that database.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. The current UniProt deletion and limited characterization of an environmental fragment are documented evidence boundaries, not unsupported assertions in this YAML.

## Recommended Edits

None required. Preserve the generated record and its `SEEDED` status. Do not present F8SJ03 as an active UniProtKB entry or convert sequence annotation and enrichment conditions into isolate or phenotype claims.

Future taxonomy corrections belong first at NCBI and then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A demonstrated projection defect belongs in `src/taxonmech/seed.py` with a regression test; a scope decision belongs in `curation/seed_scope.tsv`. Optional sequence/archive provenance needs supported maintained input and model/seeder handling, not direct YAML edits.

## Follow-up Checks

No corrective follow-up is required. Before optional sequence enrichment, retain the archive's exact target cross-reference and current inactive/active distinction, and recheck its full sequence against AEI00836.1. Biological enrichment requires explicit clone-to-isolate, clone-to-genome or clone-to-experiment evidence, not merely archive membership or a partial domain annotation.

After an authorized upstream/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036440`, inspect the emitted YAML, rerun both record validators and `just verify-corpus`, then use the full publication QC gates. This review ran no regeneration command.

## Additional Notes

The single-record skill, local checklist, write boundaries and documented validators governed the review. This target's records and archive were inspected independently. Before/after YAML SHA-256 was `f7527c116abbc7e3da923d87689a6eb7f20fbbe555adcb3904aa5bae2d47adf2`.

Only this new report was written for this target. No YAML, source, history, status, generated page or GitHub object was changed. Existing worktrees and Eukaryota remained untouched.
