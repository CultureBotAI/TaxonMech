# YAML Record Review: Salmonella enterica subsp. enterica serovar Typhimurium str. AZ 033

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_az_033.yaml`
- Started UTC: 2026-10-09T22:51:22Z
- Finished UTC: 2026-10-09T22:52:47Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1037263`, Salmonella Typhimurium strain AZ 033, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:90371`, genetic code 11, grounding `EXACT`, status `SEEDED`. All twelve ancestors, the single NCBI synonym, single attestation and full seed event were inspected. `strain_count: 0` concerns represented BacDive strains, not the existence of organisms or genomes. No GTDB mapping, identity xref, nomenclature, nested strains, definition, functional evidence or graph is asserted.

HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; YAML SHA-256 `73ec598a80a9917dfe7ecf883a0df95cf1bd98518abb2d5b2b56c9b026220592`. Ignored-inclusive filename resolution found exactly one target and no prior report. Relevant guidance, schema, implementation and history files were confirmed unchanged; prior complete reads and the freshly inspected local checklist remain applicable.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_az_033.yaml`: passed.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_az_033.yaml --out /private/tmp/taxonmech-sal-typhimurium-az033-20261009-validation.tsv --workers 1`: one file, zero errors; output TSV inspected and header-only.
- `uv run --offline python scripts/validate_history.py history`: earlier in this same turn, 17 valid records and zero invalid links. History and validator were rechecked unchanged before reuse; no second run is claimed.
- Complete own-row inventory, ancestor, type/status, attestation, scope and slug comparisons passed. These bounded checks do not certify full-corpus reproduction.
- Live NCBI EFetch and Datasets taxonomy reads succeeded. The taxonomy browser open failed. Genome and exact-taxid nucleotide queries returned no records, with the nucleotide query also reporting an unmatched phrase; limitations are preserved below.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:222713`, native NCBI names `data/catalog/ncbi_names-0005.jsonl.gz:32318` and `:32319`, slug `data/taxa/PATHS.tsv:15251` and scope `curation/seed_scope.tsv:322940` agree. The native names classify the longer `strain AZ 033` form as an equivalent name and the `str. AZ 033` form as the scientific name. The YAML's line wrap preserves the complete equivalent name; it is not a synonym for a different strain or for the species as a whole.

All twelve ancestors match the pinned backbone in ID, label and rank: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Salmonella; Salmonella enterica; Salmonella enterica subsp. enterica; serovar Typhimurium. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037263&retmode=xml) independently confirms strain identity, rank, parent, code and named ancestors. [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037263) confirms all twelve ancestor IDs including root and rank `STRAIN`.

Complete backbone/status scans found no own child, type-material, merged-ID or dropped-ID row. No claim of type status is made. The source's creation, update and publication dates were not substituted for the recorded snapshot or interpreted as nomenclatural dates.

## Evidence

NCBITAXON 1 NAME is supported by the full backbone and source names. The 2026-09-13 snapshot agrees with the attestation note. Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. No descendant contributes BacDive coverage. The record correctly lacks a broad species mapping or derived species-name exact synonym; a neighboring strain's GTDB membership cannot be transferred to AZ 033.

The full seed sentence matches the sole NCBITAXON attestation and exact scope reason. Scope admission occurred on 2026-09-13. The source manifests inspected during this turn contain raw extraction 2026-09-13T17:50:44Z, StrainInfo 17:29:00Z and ATB 17:54:04Z; the inspected `_seed_timestamp` implementation uses the latest, supporting the event at 17:54:04Z. `SEEDED` does not imply human approval. No citation or evidence snippet is asserted, so no citation-placement defect was found.

The [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1037263/dataset_report) returned an empty object. The [exact-taxid nucleotide search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1037263%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned count zero and an empty ID list, with `phrasesnotfound` naming the exact organism query and a no-items warning. These are bounded index responses, not proof that no AZ 033 sequence exists under another submission identity or in another database. No marker or assembly was assigned on that basis.

## Completeness

`rg --no-ignore --hidden -n -z -i` searched `1037263|AZ[ _-]?033|salmonella_enterica_subsp_enterica_serovar_typhimurium_str_az_033` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. All 27 matching rows were read completely, including lossless common-field/delta views. Five SOURCE.json documents and history filenames were separately checked with no own match. These searches establish no source-backed enrichment candidate for the Salmonella target within the inspected material.

Important false positives were separated by complete source identity:

- `Enterococcus sp. AZ033`, taxon 2774777, occurs in backbone row 553706, scope row 102375, names shard 0013 row 10529, GenBank shard 0047 row 37142, RefSeq shard 0007 row 39681 and GTDB shard 0003 row 49186. Its GCA_051715165.1/GCF_051715165.1, SAMN16255505, 3,145,482-base assembly and GTDB Enterococcus_B pernyi placement belong to that Enterococcus, not Salmonella AZ 033.
- `data/catalog/ncbi_genbank-0002.jsonl.gz:10545` is Candidatus Pacebacteria bacterium CG_4_10_14_0_8_um_filter_43_12, taxon 1974760, GCA_002784585.1. The numeric hit is its ungapped genome size of 1,037,263 bases, not the target taxon ID.
- Backbone rows 16430 and 20882 contain fungal AZ033-prefix synonyms. GOLD organisms Go0109990 and Go0632610, with projects Gp0110461 and Gp0649224, concern Brachypodium distachyon 21-3 NAZ033 and Xylaria flabelliformis AZ0336A. These incidental source reads did not reopen Eukaryota YAML reviews.
- Ten ATB rows, 171048, 171070, 171099, 171171, 171173, 171209, 171210, 171257, 171273 and 171298, concern Campylobacter jejuni runs ERR10372630-39. All complete assembly, sample, checksum, availability and filter fields were inspected; all retain available FASTAs and passing source filters. Matching run digits do not establish a Salmonella association.

No eligible whole-deposit association, required missing representation or demonstrated unsupported claim was found. Optional nomenclature, definitions, functional evidence and graphs may remain empty. Do not invent a culture accession from a bare strain name or import an adjacent taxon's assembly. iModulonDB is inapplicable: the YAML names no gene, regulator, pathway, functional trait or expression dataset. Absence conclusions are bounded to the listed snapshots, roots and public responses.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The represented NCBI identity, lineage, equivalent name, attestation and generated status are supported. This pass does not certify all possible biological knowledge about the strain or full-corpus reproduction.

## Recommended Edits

None required for the represented claims. Do not add Enterococcus AZ033 assemblies, the Pacebacteria numerical hit, fungal prefix matches or another Salmonella strain's GTDB membership. If new evidence emerges, its maintained source transform or explicit curation input must establish the target identity before `src/taxonmech/extract.py` and `src/taxonmech/seed.py` regenerate the record through the validated writer. Do not directly patch generated YAML or pages.

## Follow-up Checks

For any future enrichment, independently verify whole-deposit identity and source-native links rather than joining on AZ033 alone. Re-run schema and strict validation, history validation when history changes, and the appropriate `just verify-corpus` and `just qc` gates after maintained inputs change. Retry the NCBI taxonomy browser when accessible; the successful authority API checks already support the current identity. No unresolved blocker remains for this review.

## Additional Notes

Only NCBITaxon:1037263 is judged using its complete YAML and its own evidence. No neighboring finding was inherited. Eukaryota YAMLs were not reopened. This new report is the only repository write for this target; record YAMLs, sources, inventories, scope, history, status, branches, worktrees and GitHub remain unchanged. No paid research was used.
