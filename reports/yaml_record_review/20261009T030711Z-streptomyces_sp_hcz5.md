# YAML Record Review: Streptomyces sp. HCZ5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_hcz5.yaml`
- Started UTC: 2026-10-09T03:04:23Z
- Finished UTC: 2026-10-09T03:07:11Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036533`: species rank, Bacteria, parent `NCBITaxon:2593676`, ten root-first ancestors, code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_sp_hcz5.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptomyces_sp_hcz5.yaml --out /private/tmp/taxonmech-hcz5-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched backbone, all ancestors, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared/actual length 1419, submitted rRNA transcription equals DNA and no non-ACGT symbols. This checks annotation, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036533&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036533) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching labels/ranks while omitting root from its displayed chain.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch has no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for an unnamed strain-associated concept does not establish formal nomenclatural standing. Exact grounding identifies this NCBI concept, not a nearest named species or any similarly designated isolate.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222533`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32077`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15040`: identifier/slug.
- `curation/seed_scope.tsv:322780`: admission date/reason matching the seed event.

One `NAME` attestation counts a source name, not a genome or experiment. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries, not every external strain designation.

Exact Nuccore query `txid1036533[Organism:noexp]` returned only UID 334361396. Complete [JF806651.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806651.1) XML was read, including references, every feature and sequence. This 1419-base 16S marker is partial at both ends. Four source qualifiers identify Streptomyces sp. HCZ5, genomic DNA, strain HCZ5 and taxon 1036533. Only source and rRNA features occur; no host, isolation-source, geographic, culture-deposit or assembly qualifier is supplied.

The marker names Chen, Wu and Li, an unpublished seagrass-associated study and a 13-APR-2011 direct submission from the South China Sea Institute of Oceanology, without DOI or PMID. It is neither a genome nor a phenotype assay.

[Wu et al. (2012), Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii), compares HCZ5 with Streptomyces drozdowiczii at 99.65%; all three PKS-I/PKS-II/NRPS screens are positive. Its star denotes tree inclusion. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981. This is not synonymy or metabolite-production evidence. GenBank does not explicitly cite the DOI.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit identity/evidence chains. An external marker does not require inventing a BacDive strain.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms included word-bounded taxid 1036533, label/slug and HCZ5 with optional hyphen, space or underscore. Expansion added JF806651 and word-bounded UID 334361396. Both returned the same three fully inspected taxonomy/name/scope rows and no additional candidate. Five SOURCE.json files were fully parsed separately for both term sets without matches; history filenames were independently inventoried. Absence statements are bounded to these roots and terms.

`HCZ5[All Fields] AND Streptomyces[Organism]` returned only the own marker; the translation stack also counted one unfiltered HCZ5 hit. Exact non-expanded Assembly search returned zero with missing-phrase/no-items diagnostics. PubMed queries `HCZ5[All Fields] AND Streptomyces[All Fields]` and `JF806651[All Fields]` returned zero with missing-phrase diagnostics. Exact-accession web search returned no results; label search found the independently inspected primary paper. A secondary CNGB taxonomy mirror was only a search lead. Indexed misses do not prove universal genome or literature absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. No unsupported genome, phenotype or species reassignment is asserted.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit generated output based on a nearest-species comparison.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment requires explicit strain/accession/deposit linkage. Relevant table text, headings and footnote were inspected; original PDF figures were not visually verified. No complete experiment audit or independent alignment is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036533`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, complete marker and relevant primary text were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `1e2ed046226dc4597a7612739aa0150742b43565c934fa958eb00d6acda9f396`. Only this new report was written for the target. YAML, sources, history, status, pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
