# YAML Record Review: bacterium enrichment culture clone En_UW_79

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_79.yaml`
- Started UTC: 2026-10-08T21:06:36Z
- Finished UTC: 2026-10-08T21:10:11Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036465`, bacterium enrichment culture clone En_UW_79. It asserts species rank, Bacteria domain, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` status, zero represented strains, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_79.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_79.yaml --out /private/tmp/uw79-strict.tsv`: passed, one file and zero errors; complete diagnostic TSV was header-only.
- Structured comparisons checked the full backbone row, four ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Own nucleotide/protein XML parsing confirmed actual lengths equal declarations and submitted CDS translation equals the linked protein. This is annotation consistency, not independent translation, alignment or experimental validation.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. These individual checks do not prove corpus reproduction. The embedded event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused replacement was invented for a corpus-wide gate.

## Identity and Grounding

The complete [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036465&retmode=xml) agrees with the ID, label, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036465) confirms root-first ancestor IDs 1, 131567, 2 and 48479. Ancestor labels and ranks match pinned rows. EFetch's displayed lineage omits root while Datasets includes it; this is not a conflict.

Species rank does not establish a formally named species or pure isolate. Exact grounding denotes this environmental clone taxon. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete native source rows were read:

- `data/raw/ncbitaxon_taxa.tsv:222467`: identity, rank, parent, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32011`: exact scientific name, empty unique-name field.
- `data/taxa/PATHS.tsv:14974`: ID and slug.
- `curation/seed_scope.tsv:322714`: date and one-source admission reason matching the seed event.

The attestation unit is `NAME`, not strain, assembly or experiment. Full exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows, consistent with one attestation and zero represented strains.

Two additional complete search candidates, `data/catalog/gtdb_genomes-0017.jsonl.gz:41215` and `data/catalog/ncbi_genbank-0063.jsonl.gz:25971`, both concern GCA_964514585.1, Candidatus Woesearchaeota archaeon, taxid/species taxid 2026803. Their ungapped length is 1036465 and total length 1036865. The search hit is a numeric collision, not this bacterial clone's identity. Do not attach that archaeal metagenome-derived assembly, SAMEA117383917, PRJEB82487 or CAZETU000000000.1 to this record.

Exact non-expanded Nuccore query `txid1036465[Organism:noexp]` returned UID 336092474 only. The full [HQ630203.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630203.1) links a 341-base partial `nosZ` CDS to this clone/taxon, an anode-biofilm environmental sample and H2S-supplemented mineral medium. Both CDS ends are partial; codon start is 3 and translation table 11. No strain, culture-deposit or geographic qualifier is supplied.

The full [AEI00861.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00861.1) reciprocally links HQ630203.1 and this clone/taxon. It is a 113-residue conceptual translation with a PRK02888/CDD:235082 region through residue 113. Actual lengths and submitted CDS translation agree; no non-ACGT bases or ambiguous amino-acid symbols were found. Both records cite an unpublished enrichment study and 17-NOV-2010 direct submission without a study PMID or DOI. This fragment is not evidence of a clone-specific enzyme assay, complete pathway, pure isolate or whole-organism phenotype.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, places HQ630203 within enrichment-derived nosZ accessions HQ630075-HQ630210. Page 92 cautions that one DGGE band does not prove purity. Both pages were read fully. Exact accession/clone searches across all 164 pages of extractable text found no match. This is study context, not clone-specific identification; raster and supplementary content were not exhaustively searched.

The clone-label web query excluding the already checked NCBI Taxonomy site returned no results. HQ630203/AEI00861 queries and versioned/gene-qualified refinements surfaced unrelated vehicle-part catalog leads, including a [headlamp-part listing](https://partsouq.com/shop/product/HQ630203-hyundai-kia-bezel-assy-h-lamp-lh/15387108), not verified biological evidence. Those searches were not empty. Exact accession/clone finds in the [PLOS main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) returned no matching text. These bounded searches do not establish literature absence; community-level performance was not assigned to this clone.

## Completeness

Complete enough for its supported taxonomy-seed scope. Optional nomenclature, synonyms, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. A partial gene is not an assembly or a required taxonomy-record slot.

Expanded `rg --no-ignore --hidden -n -z -i` searches covered ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. The five matches were the backbone, name, scope and two unrelated assembly rows above; all were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning, not universal genome absence. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: the YAML has no gene, regulator or expression claim and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. External characterization limits and unrelated search collisions do not make this taxonomy seed unsupported.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not transfer neighboring clones' accessions, species assignments, isolate identities or phenotypes from shared medium or study membership.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence provenance needs maintained input and suitable model/seeder handling, not generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Optional enrichment requires primary evidence explicitly linking this exact clone to an isolate, genome or experiment.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036465`, inspect emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The single-record skill and checklist were reread; unchanged local ownership guidance and documented validators governed the review. Own source rows and accessions were inspected independently. Before/after YAML SHA-256 was `41a45f30a61954d4fe98b4751863a252616a8ddcec9c1aeffced9f7efd8d6bfc`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
