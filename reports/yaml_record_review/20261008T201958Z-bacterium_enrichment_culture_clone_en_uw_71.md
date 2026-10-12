# YAML Record Review: bacterium enrichment culture clone En_UW_71

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_71.yaml`
- Started UTC: 2026-10-08T20:16:41Z
- Finished UTC: 2026-10-08T20:19:58Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036457`, bacterium enrichment culture clone En_UW_71. It asserts species rank, Bacteria domain, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented strains, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_71.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_71.yaml --out /private/tmp/uw71-strict.tsv`: passed, one file and zero errors. Complete diagnostic TSV was header-only.
- Structured comparisons checked the full backbone row, four ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Own nucleotide/protein XML parsing confirmed declared versus actual lengths and equality of the submitted CDS translation with the linked protein sequence. This is annotation consistency, not independent translation, alignment or experimental validation.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused replacement was invented for a corpus-wide gate.

## Identity and Grounding

The complete [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036457&retmode=xml) agrees with the ID, label, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036457) confirms root-first ancestor IDs 1, 131567, 2 and 48479. All ancestor labels and ranks match pinned rows. EFetch's displayed lineage omits root while Datasets includes it; this is not a conflict.

NCBI species rank does not establish a formally named species or pure isolate. Exact grounding denotes identity with this environmental clone taxon. Live EFetch supplies no other names, and pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete native source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222459`: identity, rank, parent, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32003`: exact scientific-name object, empty unique-name field.
- `data/taxa/PATHS.tsv:14966`: ID and slug.
- `curation/seed_scope.tsv:322706`: date and one-source admission reason matching the seed event.

The attestation unit is `NAME`, not strain, assembly or experiment. Full exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows, consistent with one attestation and zero represented strains.

An additional complete native object at `data/catalog/ncbi_genbank-0066.jsonl.gz:27119` is an incidental numeric match, not identity evidence. Assembly `GCA_982663585.1` represents uncultured Candidatus Poseidoniales archaeon, with taxid and species_taxid 274854. Its `genome_size` is 1036457; ungapped size is 1035797. The matched number is not its taxon ID. Do not attach this archaeal assembly, BioSample `SAMEA122230397` or BioProject `PRJEB72923` to the bacterial clone.

Exact non-expanded Nuccore query `txid1036457[Organism:noexp]` returned one record, UID 336092458. The complete [HQ630195.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630195.1) assigns a 347-base partial `nosZ` CDS to this clone and taxon. Source qualifiers describe an anode-biofilm environmental sample and H2S-supplemented mineral medium. Both CDS ends are partial; codon start is 3 and translation table is 11. No strain, culture-deposit or geographic qualifier is supplied.

The full linked [AEI00853.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00853.1) reciprocally identifies HQ630195.1 and the same clone/taxon. Its 115-residue conceptual translation carries a PRK02888/CDD:235082 region through residue 109. Actual lengths match declarations; the submitted CDS translation matches the protein sequence exactly. No non-ACGT DNA or ambiguous amino-acid symbols were found. Both records cite an unpublished enrichment study and a 17-NOV-2010 direct submission, without a PMID or DOI for that study. Fragment annotation is not a clone-specific enzyme assay, complete pathway, culture-purity result or whole-organism phenotype.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, places HQ630195 within the enrichment-derived nosZ range HQ630075-HQ630210. Page 92 cautions that a single DGGE band does not prove purity. Both pages were read fully. Exact accession/clone searches across all 164 pages of extractable text found no match. This provides study context, not clone-specific species identification; raster and supplementary content were not exhaustively searched.

The clone-label web query excluding the already checked NCBI Taxonomy site and separate HQ630195/AEI00853 queries returned no results. Exact accession/clone finds in the [PLOS main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) returned no matching text. These bounded checks do not establish literature absence. No community-level performance claim was assigned to the clone.

## Completeness

Complete enough for its supported taxonomy-seed scope. Optional nomenclature, synonyms, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. An external partial gene is neither an assembly nor a required taxonomy-record slot.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. Four rows matched: backbone, scientific name, scope and the excluded assembly object above. All were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning, not universal genome absence. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: the YAML has no gene, regulator or expression claim, and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. The unrelated catalog match is not present in the YAML and does not constitute a record defect. Limited external characterization does not make the taxonomy seed unsupported.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not turn the numeric catalog match into a genome link or transfer neighboring clones' accessions, isolate identities, species assignments or phenotypes.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence provenance requires maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Before optional enrichment, inspect primary evidence explicitly linking this exact clone to the proposed isolate, genome or experiment. Match typed taxon-ID fields, not arbitrary numeric fields.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036457`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The single-record skill and checklist were reread in this continuing review session; unchanged local ownership guidance and validators governed the review. Own source rows and accessions were inspected independently. Before/after YAML SHA-256 was `4f036d85ffe28051a8859f255ff6eb80438e805601d0c70fba0676e2f599943d`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.

