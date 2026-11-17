# YAML Record Review: Wolbachia endosymbiont of Microplitis sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_microplitis_sp.yaml`
- Started UTC: 2026-10-09T15:15:40Z
- Finished UTC: 2026-10-09T15:17:46Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036782` was read. The exact label is Wolbachia endosymbiont of Microplitis sp.; rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), grounding `EXACT`, status `SEEDED`, genetic code 11, zero inventoried strains and one NCBITAXON name attestation.

An ignored-inclusive filename inventory resolved only this target YAML and no own prior report. SHA-256: `e7f2d14fcaeae72e2cbe17b593ed4b8faa17b51908de32e40129e4eb4f396e7c`. This review concerns the bacterial source taxon, not a host, bracovirus or a different Microplitis-associated Wolbachia.

## Validation

Commands used the existing offline environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_microplitis_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_microplitis_sp.yaml --workers 1 --out /private/tmp/taxonmech-wmic-20261009-validation.tsv`: passed, one file, zero errors. The TSV was read and contains only its header.
- `uv run --offline python scripts/validate_history.py history` passed earlier in this review turn: 17 valid records, zero invalid links. No history file was changed thereafter. The target's history absence and generated event were checked separately.
- Own-row structured checks passed for identity, the complete ancestor chain, sole attestation, PATHS/scope entries and seeding-event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site-drift gates were not rerun for this record. `just verify-corpus` has no focused record selector. Bounded source comparisons are not a replacement for that gate.
- Not applicable: OAK curator-added graph-node checks and iModulonDB gene/component checks. The YAML has no causal graph, gene, regulator, pathway, trait or transcriptomic assertion.
- The web Taxonomy browser was inaccessible, but both direct live NCBI EFetch and Datasets taxonomy responses were successfully inspected. Exact-taxon nucleotide and genome queries also completed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222622` agrees with every identity field and the single NCBITAXON source. `data/catalog/ncbi_names-0005.jsonl.gz:32200` is the own scientific-name entry. Neither source supplies an own synonym requiring representation.

Live [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036782&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036782) confirm the ID, exact label, species rank, parent and bacterial placement; EFetch also confirms genetic code 11.

The complete 11-entry root-first chain agrees with the inventory and live authority: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. The tribe and unranked parent are correctly preserved.

This species-rank NCBI node is not a claim of a validly published species name, type strain or identified host species. `EXACT` describes the grounding of this record to its NCBI ID, not a reconciliation of all Wolbachia associated with the same host genus.

## Evidence

The only material source assertion is one NCBI name from the 2026-09-13 snapshot. Its ID, label, unit, count and date match the backbone. `strain_count: 0` matches the absence of own BacDive strain rows and does not assert biological absence of bacterial cells or strains.

The own [non-expanded nucleotide search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036782%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned zero IDs, with a phrase-not-found message; the [genome report query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036782/dataset_report) returned an empty object. These establish no positive currently indexed accession evidence through these queries. They do not establish global sequence absence, explain why the node was created, or invalidate a live taxonomy node. No marker accession from a neighboring record was borrowed.

The broad Microplitis source search returned distinct entities, all read as source context rather than additional review targets:

- Other NCBI nodes 1094258 (Microplitis jft02), 1366276 (Microplitis mediator) and 1366277 (Microplitis tuberculifer) have their own names and scope rows. The own record has no merge row connecting them. Shared genus/parent does not establish equivalence.
- GOLD `Go0081174 -> Gp0081174 -> Ga0055777` belongs to Microplitis demolitor bracovirus, NCBI 53988, not this bacterial taxon.
- GOLD `Go0089939 -> Gp0089939 -> Ga0129742` belongs to Microplitis demolitor, NCBI 69319, including host assembly `GCA_000572035.2`. Host identity does not transfer its genome to an endosymbiont.
- Twelve other paired GOLD project/analysis rows describe viral-community metatranscriptomes under PRJNA437008, with no organism GOLD ID or assembly accession establishing an own Wolbachia link.
- BV-BRC `patric:303.1302` and NCBI `GCA_039634515.1` are Pseudomonas putida NY11286. The incidental digits occur in their BioProject, `PRJNA1036782`, not the taxonomy field.
- GTDB/native NCBI `GCA_000992395.1` is Parcubacteria group bacterium GW2011_GWA2_38_13, NCBI 1618811; `GCA_053536075.1` is Candidatus Iainarchaeum sp., NCBI 3101447. Their sequence length of 1,036,782 bp is a numeric collision, not a taxon match.

The YAML correctly does not import these nearby or incidental references. No primary publication, phenotype, mechanism or genome relationship is asserted by this record that requires an additional literature citation.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The bounded taxon ID, exact label and broader Microplitis name yielded 47 rows. Every returned JSON/TSV row was read fully; source metadata in all five `SOURCE.json` files was parsed. History content and filenames were also checked with ignored-inclusive searches.

Complete own-ID inventory scans found no LPSN, GTDB, BacDive, GOLD, MediaDive, Madin or BactoTraits assertion, type material, merge mapping, dropped row or child node. The broader source candidates above did not establish an eligible own strain, assembly, ATB sample link or StrainInfo deposit. These findings are bounded to the inspected snapshots and queries, not all possible external data.

Optional synonyms, nomenclature, xrefs, mappings, strains, genomes, experimental evidence and causal graphs are correctly left unpopulated. Absence of a formal name or a positive nucleotide query does not require deletion of a live source-taxonomy record.

`data/taxa/PATHS.tsv:15150` matches the filename. `curation/seed_scope.tsv:322855` records the 2026-09-13 one-source inclusion. The sole 2026-09-13T17:54:04Z seeding event exactly reproduces source/scope wording. No target-specific external history entry was found. No review status or human sign-off is implied by this report.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this target and the inspected evidence. The lack of a positive live sequence query remains an observation, not a demonstrated data defect.

## Recommended Edits

None required. Do not merge similarly named Wolbachia nodes or transfer host, virus, BioProject-number or sequence-length matches into this record.

Any future authorized correction belongs in the maintained source/extractor/seeder or scope input that owns the affected field. Do not patch generated YAML or pages to add speculative evidence.

## Follow-up Checks

Before future regeneration, run the documented corpus reproduction, provenance, strict-schema, test and publication gates. Any proposed accession enrichment should resolve its own current NCBI taxonomy and explicit sample/deposit relationship. No defect-specific repair is required on present evidence.

## Additional Notes

This independent report is the only repository write for this target. Source-context reads did not re-review or modify Eukaryota records. Records, source snapshots, scope, history, generated products, branches and all existing worktrees remain untouched. No paid provider or GitHub mutation was used.

