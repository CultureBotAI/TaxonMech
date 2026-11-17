# YAML Record Review: Verrucosispora sp. M1Z33

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/verrucosispora_sp_m1z33.yaml`
- Started UTC: 2026-10-09T03:23:38Z
- Finished UTC: 2026-10-09T03:26:24Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036536`: species rank, Bacteria, parent `NCBITaxon:2617518`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/verrucosispora_sp_m1z33.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/verrucosispora_sp_m1z33.yaml --out /private/tmp/taxonmech-m1z33-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched backbone, all ancestors, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared/actual length 1383, submitted rRNA transcription equals DNA and no non-ACGT symbols. This checks annotation, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036536&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036536) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching labels/ranks while omitting root from its displayed chain.

Importantly, NCBI retains the scientific name Verrucosispora sp. M1Z33 while placing it under Micromonospora and unclassified Micromonospora. The record faithfully carries that same combination, including Micromonosporales and Micromonosporaceae. This is not a locally inferred lineage or demonstrated projection bug. No renamed Micromonospora label or exact synonym should be invented to make the strings agree.

EFetch has no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for an unnamed strain-associated concept does not establish formal nomenclatural standing. Exact grounding identifies this NCBI concept, not a nearest named species.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222536`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32080`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15043`: identifier/slug.
- `curation/seed_scope.tsv:322783`: admission date/reason matching the seed event.

One `NAME` attestation counts a source name, not a genome or experiment. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries, not every external strain designation.

Exact Nuccore query `txid1036536[Organism:noexp]` returned only UID 334361387. Complete [JF806642.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806642.1) XML was read, including references, every feature and sequence. This 1383-base 16S marker is partial at both ends. Its four source qualifiers identify Verrucosispora sp. M1Z33, genomic DNA, strain M1Z33 and taxon 1036536. Its taxonomy also includes Micromonospora. Only source and rRNA features occur; no host, isolation-source, geographic, culture-deposit or assembly qualifier is supplied.

The marker names Chen, Wu and Li, an unpublished seagrass-associated study and a 13-APR-2011 direct submission from the South China Sea Institute of Oceanology, without DOI or PMID. It is neither a genome nor a phenotype assay.

[Wu et al. (2012), Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii), compares M1Z33 with Verrucosispora sediminis at 99.21%; PKS-I is negative, PKS-II and NRPS positive. This row has no tree-inclusion star. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981. Neither synonymy nor metabolite production follows. GenBank does not explicitly cite this DOI.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit identity/evidence chains. An external marker does not require inventing a BacDive strain.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms included word-bounded taxid 1036536, label/slug and M1Z33 with optional hyphen, space or underscore before 33. Expansion added JF806642 and word-bounded UID 334361387. Both returned the same three fully inspected taxonomy/name/scope rows and no additional candidate. Five SOURCE.json files were fully parsed separately for both term sets without matches; history filenames were independently inventoried. Absence statements are bounded to these roots and terms.

Unfiltered Nuccore query `M1Z33[All Fields]` returned only the own marker, so this check did not depend on selecting Verrucosispora versus Micromonospora as a genus filter. Exact non-expanded Assembly search returned zero with missing-phrase/no-items diagnostics. PubMed queries `M1Z33[All Fields]` and `JF806642[All Fields]` returned zero with missing-phrase diagnostics. Exact-accession web search returned no results. Label searches found the primary paper, secondary review leads and unrelated product-code matches; the primary table, not secondary species wording, supports the interpretation above. Indexed misses do not prove universal genome or literature absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. The differing genus string in the label is preserved from NCBI, not silently reconciled. No unsupported genome, phenotype or species reassignment is asserted.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit generated names or lineage based on apparent genus-string mismatch or nearest-species comparison.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment requires explicit strain/accession/deposit linkage. Relevant primary text, table headings and footnote were inspected; original PDF figures were not visually verified. No complete experiment audit or independent alignment is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036536`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, complete marker and relevant primary text were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `6e58fa800ee401f4e7958c61bb71739e22bb9213a03781419978439827568826`. Only this new report was written for the target. YAML, sources, history, status, pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
