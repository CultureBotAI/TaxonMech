# YAML Record Review: bacterium enrichment culture clone En_UW_42

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_42.yaml`
- Started UTC: 2026-10-08T17:20:48Z
- Finished UTC: 2026-10-08T17:25:50Z
- Verdict: pass

## Target

Exactly one generated `TaxonRecord` was resolved and read in full: `NCBITaxon:1036428`, bacterium enrichment culture clone En_UW_42. Its fields are `SPECIES`, `BACTERIA`, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and zero associated strain records. NCBI's species rank does not establish a formally named species or pure isolate.

The ignored-inclusive filename search across `data/taxa/`, `reports/yaml_record_review/` and `history/` found only the target YAML for the identifier/label/slug pattern, with no prior report for this stem. This review leaves generated records, source inventories, scope, status and history unchanged.

## Validation

Focused commands ran with the existing environment and `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`, `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_42.yaml`: pass, no issues found.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_42.yaml --out /private/tmp/uw42-strict.tsv`: pass, one file scanned, zero files with errors and zero error rows. The full TSV was inspected and contained only the header.
- Structured comparisons of the complete target with its pinned backbone, all four ancestors, attestation, scope, path index and embedded seed event: pass.
- Live primary taxonomy, nucleotide and linked protein inspections: completed as described below.

Not checked: full-corpus `just verify-corpus`, `just provenance-check`, `just validate-history`, `just qc`, `just test`, vendored synchronization, generated-site drift and global statistics gates. A focused comparison is not corpus reproduction. No undocumented per-record reproduction/history gate was invented. The seed event was manually checked against its source and scope evidence; no matching standalone history artifact was found in the bounded search.

Graph grounding validation is not applicable because there is no curator-added graph. iModulonDB was not run: this YAML has no gene, regulator, pathway or expression-module claim and the environmental clone has not been resolved to a covered strain/dataset. That is not a claim of database absence.

## Identity and Grounding

Complete evidence rows were inspected at `data/raw/ncbitaxon_taxa.tsv:222430`, `data/catalog/ncbi_names-0005.jsonl.gz:31974`, `data/taxa/PATHS.tsv:14937` and `curation/seed_scope.tsv:322677`. The identifier, scientific name, rank, parent, genetic code and 2026-09-13 snapshot agree. The backbone and YAML both carry no synonyms. The complete root-first lineage matches root, cellular organisms, Bacteria and environmental samples, with the corresponding ranks. The full backbone scan found no direct children.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036428&retmode=xml) agrees with the clone name, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036428) confirms all four ancestor IDs, including root. EFetch omits root from its lineage representation and supplies an environmental-samples division; neither is a conflict with the generated root-first bacterial lineage. No additional names appear in the taxonomy response.

Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target rows. The grounding is exact to the supported NCBI name/identifier, not to a cultured species inferred from a similar fragment. No neighboring clone, accession, taxon, strain or deposit is treated as equivalent.

## Evidence

The scientific-name row supports the one `NCBITAXON` attestation with assertion unit `NAME`. This counts a source assertion, not organisms, strains or genomes. The snapshot note matches the backbone, and the 2026-09-13 embedded seed event reproduces the maintained scope reason. Retaining `SEEDED` is appropriate; this report is not a human-approved status promotion.

The exact Nuccore query `txid1036428[Organism:noexp]` returned UID 336092270. The complete [HQ630101.1 GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=336092270&rettype=gb&retmode=xml), including all features and sequence, identifies this taxon and En_UW_42. It contains 347 bases of a partial `nosZ` CDS, with both ends partial, codon start 3 and translation table 11. Source qualifiers specify an anode biofilm, environmental sample and Na2S2O3-supplemented mineral medium. No strain, culture-deposit or geographic source qualifier is supplied. The linked study remains marked unpublished and the direct submission is dated 17 November 2010. Those annotations describe the submitted clone fragment, not a purified isolate, experimentally measured enzyme activity or whole-genome phenotype.

The explicitly linked [AEI00759.1 protein XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AEI00759.1&rettype=gb&retmode=xml) was opened and read in full. It carries 115 amino acids, the same taxon and clone, and a partial CDS link back to HQ630101.1. Declared and actual nucleotide/protein lengths match; the submitted translation exactly matches the protein sequence. No non-ACGT nucleotide or X/B/Z/J amino-acid ambiguity was detected. This is annotation consistency, not independent translation or experimental verification. Its computational PRK02888/CDD:235082 region spans residues less-than-1 through 109, not the entire 115-residue fragment; that annotation does not prove measured reductase activity in this clone.

The cached 164-page [Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), dated 2015, was searched for HQ630101 and the clone label, with no extracted-text hit. Printed pages 54 and 92 were read in full again. Page 54 identifies an enrichment-sequence accession range containing HQ630101; page 92 cautions that a single DGGE band does not prove culture purity. This establishes study context, not a clone-to-species identification. The search does not cover all rasterized text or supplements.

Exact target-accession and clone searches in the main HTML of the related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) returned no matching text. This is not a supplement audit. Exact web queries for HQ630101 and AEI00759, plus the clone query excluding NCBI's already inspected taxonomy listing, returned no results. No community-level performance result, nearby-clone protein archive or inferred taxonomic assignment was imported from those searches.

## Completeness

No consequential gap was identified within the supported taxonomy-seed scope. Optional nomenclature, synonyms, mappings, strains, deposits, genome links, traits and graph fields need not be invented to fill the record. Zero associated strains agrees with the available source evidence, not a claim that the organism is intrinsically unculturable.

Exact identifier scans of the seven raw inventories for BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits found no target rows. The broader compressed-content search used `rg --no-ignore --hidden -n -z -i` over `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. Identifier, slug and clone-label patterns returned three rows: the backbone, scientific name and scope evidence above. All three complete rows were read.

An expanded search adding HQ630101, AEI00759, the submitted study title and the related PLOS DOI returned the same three rows. All five applicable `SOURCE.json` metadata files, excluded from the content scan, were separately read without finding a target identity match. The ignored-independent history filename search found no target artifact. These absence statements apply only to the named local surfaces and exact search patterns.

The exact NCBI Assembly query returned zero items with a phrase-not-found warning. This result does not prove that no relevant assembly exists under any identifier. No supported culture-deposit or whole-genome association emerged from the inspected evidence, and no fragment was misclassified as a genome.

## Findings

None found in the YAML's supported claims.

Counts: 0 blocker, 0 major, 0 minor.

The unresolved organism-level identity of an environmental clone and the limited scope of its partial-gene annotations are evidence boundaries, not contradictions in the present taxonomy record. No invalid field, broken stored reference, unsupported trait or status inflation was identified.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status.

If future identity evidence requires correction, NCBI is the authority; pinned ingestion is maintained in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Seeder defects belong in `src/taxonmech/seed.py` with focused tests, and scope changes in `curation/seed_scope.tsv`. These are ownership routes, not proposed edits. Do not hand-edit generated records, add a graph, or infer traits from the medium note, gene annotation or a neighboring clone.

## Follow-up Checks

No unresolved blocker remains for this individual verdict. Any future phenotype or strain enrichment needs explicit clone-to-organism/deposit evidence and claim-specific experimental support, preserving the partial-sequence qualifiers. Supplementary-material searches are optional discovery work, not a prerequisite for this taxonomy seed.

After an authorized maintained-input change, use the documented canary workflow, inspect the generated record, rerun the focused schema and strict validators, and execute the applicable reproduction, provenance, history and corpus QC gates. This read-only review did not run generation or claim those global gates passed.

## Additional Notes

This report completes one sequential individual review. Eukaryota, other records and existing worktrees were untouched. No history entry, status promotion, source refresh, generated product, paid research, outbound communication or GitHub mutation was performed.

The record SHA-256 remained `60c94dee67b9bdb2989d7f3d0e3784cc2a54e40c04c4dec1f6216755966225c1` before and after the review. One new timestamped Markdown report is the only repository write for this target. No absence statement here is a universal census of external knowledge.
