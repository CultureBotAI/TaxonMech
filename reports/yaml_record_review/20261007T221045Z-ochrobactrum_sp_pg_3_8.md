# YAML Record Review: Ochrobactrum sp. PG-3-8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/ochrobactrum_sp_pg_3_8.yaml`
- Started UTC: 2026-10-07T22:07:53Z
- Finished UTC: 2026-10-07T22:10:45Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036153`, Ochrobactrum sp. PG-3-8, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read. It has eleven ancestors, genetic code 11, exact grounding, seeded status, one NCBI name attestation and `strain_count: 0`. No synonyms, nomenclature, mappings, strains, evidence objects, graph, discussion or dataset are asserted.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/ochrobactrum_sp_pg_3_8.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/ochrobactrum_sp_pg_3_8.yaml --out /private/tmp/opg38-strict.tsv`: exit 0, one file, zero errors. The diagnostic TSV was read and contains only its header.
- Structured comparisons passed for backbone identity, all eleven ancestors, attestation, unique path and scope reason. Exact pinned type-material, merged-ID and dropped-ID checks returned no target rows. The pinned backbone has no target descendants.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. Bounded comparisons do not reproduce the corpus. No graph is asserted and the bounded search found no standalone target history record, so specialized graph/history checks had no target.

## Identity and Grounding

Live Taxonomy EFetch agrees on ID, label, species rank, bacterial division, genetic code 11 and parent `NCBITaxon:239106`, unclassified Ochrobactrum. Datasets confirms all eleven ancestor IDs including root. Labels and ranks match through cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Brucellaceae, the unranked Brucella/Ochrobactrum group, Ochrobactrum and the unclassified parent. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036153), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036153).

Exact grounding identifies this NCBI node. PG-3-8 is a source strain designation, not an established culture-collection deposit; species rank does not establish a formally published species name. The group ancestor does not establish identity with a named Brucella species. Vibrio PG38, Bradyrhizobium dpg38 and Serratia IPG38 are distinct organisms.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222281` matches all seeded identity fields, empty synonyms, sole source and 2026-09-13 snapshot. The complete native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31799`.
- `data/taxa/PATHS.tsv:14784` uniquely maps the ID and slug; `curation/seed_scope.tsv:322535` matches the date and one-source reason.
- Exact-taxonomy Nucleotide search returned [JF820105.1](https://www.ncbi.nlm.nih.gov/nuccore/JF820105.1), a 1,335-base partial 16S rRNA sequence explicitly identifying PG-3-8/taxon 1036153. Complete non-sequence metadata describe soil from Puguang gas field, China. Submission was 14 April 2011 by Zhang, Li, Yang, Wang and Yuan at China Agricultural University; creation and update were 7 June 2011. No culture deposit, BioSample, BioProject, assembly or protein accession appears in the inspected metadata. The marker is not a genome.
- The sequence's unpublished survey title and author names match the 2012 publication represented by PMID 22452226. Previously fetched primary PubMed citation/full-abstract XML was reread. This association is bibliographic inference, not an explicit PMID link in GenBank. The abstract mentions Ochrobactrum in the Puguang survey but not PG-3-8-specific results. No functional phenotype or gene is inferred. [Primary survey abstract](https://pubmed.ncbi.nlm.nih.gov/22452226/).
- Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings, not proof of genome absence under every identifier.
- The attestation counts one NCBI `NAME`, not a culture or genome. The seed event agrees with the inventory and scope reason. Timestamp `2026-09-13T17:54:04Z` matches the latest extracted-at value among the raw, ATB and StrainInfo manifests, selected by `src/taxonmech/seed.py:139`.

## Completeness

The exact BacDive comparison and absence of classified descendants support the inventory-specific zero strain count, not a claim that PG-3-8 was never cultured. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons returned no target rows. Optional slots are appropriately empty for this seeded identity record.

Resolution searched ignored files in `data/taxa`, `reports`, `curation` and `history`. The two similarly named Vibrio and Bradyrhizobium YAMLs were read fully for collision resolution, not separately reviewed. The subsequent source search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, covering digit-bounded 1036153, PG-3-8 label/slug variants and JF820105. All fifteen candidates were read completely: eight JSON objects and seven TSV rows. Five SOURCE.json files were parsed separately and history filenames checked independently.

Three candidates are target backbone, native name and scope records. Twelve concern other taxa. No additional supported target culture/genome link, curation overlay or standalone history record was found in the bounded roots. No required representation was demonstrated missing. iModulonDB is not applicable: the YAML makes no gene, regulator, functional, transcriptomic or dataset claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, attestation, source-specific count and seeded provenance are supported. No phenotype or genome assertion is inferred from the marker or similar names.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Optional sequence enrichment belongs in maintained source/extractor inputs or a durable curator representation. Phenotype and isolation-context curation should follow ownership rules in `docs/CURATION.md` with direct strain-specific evidence. Do not join by bare strain designation or transfer assertions from the broader group ancestor.

## Follow-up Checks

Before adding a phenotype, inspect the survey's full methods and strain results with an explicit link to PG-3-8/JF820105.1. Require a direct source identity link before adding any deposit, genome or species reassignment. Regenerate future maintained-input changes through the documented pipeline and run focused schema/strict plus corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the target YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- Vibrio cholerae PG38 is taxon 693740, with GOLD Go0002299/Gp0002299 and PRJNA41841. Its backbone, name, scope and legacy-page row do not identify Ochrobactrum PG-3-8.
- Bradyrhizobium sp. dpg38 is taxon 1089510; its full backbone, name and scope rows are unrelated.
- Serratia marcescens IPG38 is taxon 615, GCA/GCF_028886045.1, SAMN32818148 and BV-BRC 615.2612. Complete BV-BRC and assembly catalog objects provide no link to this target.
- Name/accession web searches supplied no additional inspected target evidence. Search snippets were not used as claim evidence. No exhaustive literature-absence claim is made. The primary survey's full strain tables were not inspected; previously attempted full-text routes had timed out and were not retried.
- No sequence alignment, culture-availability assessment or taxonomic reassignment was performed. Only this new report was written; no YAML, source inventory, history/lifecycle or GitHub state changed.
