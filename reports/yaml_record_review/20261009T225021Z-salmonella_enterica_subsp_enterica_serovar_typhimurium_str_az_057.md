# YAML Record Review: Salmonella enterica subsp. enterica serovar Typhimurium str. AZ 057

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_az_057.yaml`
- Started UTC: 2026-10-09T22:48:23Z
- Finished UTC: 2026-10-09T22:50:21Z
- Verdict: needs curation

## Target

Entire generated `TaxonRecord` inspected: `NCBITaxon:1037262`, Typhimurium strain AZ 057, `STRAIN`, `BACTERIA`, parent `NCBITaxon:90371`, code 11, grounding `EXACT`, status `SEEDED`. All twelve ancestors, two synonyms, one mapping, three attestations and the seed event were read. `strain_count: 0` counts represented BacDive strains, not sequencing coverage. No nomenclature, nested strains, definition, functional evidence or graph is asserted.

HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; YAML SHA-256 `cbfdba1cf387eff506a6d24b2a1e906c6831191236e3fab565b65bf9c1f787e5`. Ignored-inclusive filename resolution found exactly one target and no prior report. Guidance, schema and implementation remained unchanged from prior complete reads; the local checklist was freshly read.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_az_057.yaml`: passed.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_az_057.yaml --out /private/tmp/taxonmech-sal-typhimurium-az057-20261009-validation.tsv --workers 1`: one file, zero errors; header-only TSV inspected.
- `uv run --offline python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Complete own-row inventory, ancestor, type/status, source-attestation, scope and slug comparisons passed. These bounded checks do not establish full-corpus reproduction or mapping semantics.
- NCBI taxonomy API and focused assembly identity checks succeeded. NCBI taxonomy and GTDB genome browser opens failed; native GTDB metadata was read completely. PubMed bibliography and abstract were inspected, not full text or supplements.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:222712`, native names `data/catalog/ncbi_names-0005.jsonl.gz:32316` and `:32317`, slug `data/taxa/PATHS.tsv:15250`, scope `curation/seed_scope.tsv:36184` and legacy page row 913 agree. The NCBI equivalent name expands `str.` to `strain` while retaining AZ 057. The YAML line wrap does not alter that name.

All twelve ancestor IDs, labels and ranks match the pinned backbone: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Salmonella; Salmonella enterica; Salmonella enterica subsp. enterica; serovar Typhimurium. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037262&retmode=xml) confirms strain identity, rank, parent, code and named ancestors. [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037262) confirms `STRAIN`, all twelve ancestor IDs including root, and one assembly. Complete backbone/status scans found no own child, type-material, merger or dropped-ID row.

The main NCBI identity is correct. GTDB species-cluster membership does not support the exact species-name synonym applied to this strain; see M1.

## Evidence

`data/raw/gtdb_mappings.tsv:1478` supplies closeMatch to `GTDB:s__Salmonella_enterica` and count 21,527. Freshly inspected `data/raw/gtdb_species.tsv:163163` supports the count as source-species volume. The schema at `src/taxonmech/schema/taxonmech.yaml:431` describes closeMatch as the same species, from the source taxon's side; `genome_count` describes assemblies under that source taxon. The count is not independently defective and must not be interpreted as 21,527 genomes of AZ 057. No native-cluster recount was performed.

Complete GTDB row `data/catalog/gtdb_genomes-0013.jsonl.gz:24231` places non-representative `RS_GCF_000486105.1` in S. enterica while separately retaining NCBI strain taxon 1037262, species taxon 28901 and strain identifier AZ 057. This directly supports species membership, not strain/species equivalence.

Complete GenBank row `data/catalog/ncbi_genbank-0000.jsonl.gz:15601` and RefSeq row `data/catalog/ncbi_refseq-0000.jsonl.gz:13060` identify paired GCA_000486105.1/GCF_000486105.1, ASM48610v1, Contig, 87 contigs, 4,917,909 bases, AOXC00000000.1 and SAMN01823743. Both are latest with identical paired assemblies. The native GenBank project is PRJNA67437; native RefSeq and GTDB retain PRJNA224116. Their annotation counts and dates are source-specific, not competing taxon identities. [Live GenBank](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000486105.1/dataset_report) and [live RefSeq](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000486105.1/dataset_report) both confirm current status, the exact strain, sample and PRJNA67437. Neither is suppressed.

Live BioSample metadata additionally names CFSAN001156 and SRS472223. These sample identifiers were not treated as culture deposits, used for genome-equivalence joins or separately searched locally; the completeness conclusions remain bounded accordingly.

Complete BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:3423` identifies PATRIC 1037262.4, GCA_000486105.1, PRJNA67437, SAMN01823743 and AZ 057, with an empty culture collection and a dash in its RefSeq field. That older source row's RefSeq field does not negate the verified current RefSeq assembly. GOLD rows `data/gold/organisms.jsonl.gz:39732`, `projects.jsonl.gz:33698` and `analyses.jsonl.gz:33411` trace `Go0048561 -> Gp0048561 -> Ga0051786`, IMG 2579778567 and GCA_000486105.1. The analysis identifies the organism through its explicit project link; its direct organism field is empty. No culture collection is supplied. `data/raw/gold_organisms.tsv:517` correctly counts one organism. These chains do not independently establish an eligible BacDive/deposit link.

Assembly PMID 24158624 resolves to [Phylogenetic diversity of the enteric pathogen Salmonella enterica subsp. enterica inferred from genome-wide reference-free SNP characters](https://pubmed.ncbi.nlm.nih.gov/24158624/), Genome Biology and Evolution, 2013, DOI `10.1093/gbe/evt159`. Its abstract describes a genome-wide analysis of 156 isolates representing 78 serovars. It does not alone demonstrate an experimental phenotype for AZ 057. No such phenotype is asserted here or in the YAML; full text and supplements were not inspected.

NCBITAXON 1 NAME and GOLD 1 ORGANISM agree with inventories. GTDB 21,527 GENOME is supported as source-species volume with M1's scope qualification. Complete own-ID inventory scans found no BacDive, LPSN, MediaDive, Madin or BactoTraits row, and no descendant contributes BacDive coverage. The full seed sentence matches the three-source set and scope. Fresh manifest extraction times are raw 2026-09-13T17:50:44Z, StrainInfo 17:29:00Z and ATB 17:54:04Z; `_seed_timestamp` therefore supports the recorded 17:54:04Z event. `SEEDED` does not claim human review.

## Completeness

`rg --no-ignore --hidden -n -z -i` searched `1037262|AZ[ _-]?057|salmonella_enterica_subsp_enterica_serovar_typhimurium_str_az_057` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. All 30 hits were completely read, including lossless common-field/delta representations of native rows. Five SOURCE.json documents and history filenames were separately checked with no own match.

False-positive source hits were explicitly distinguished: backbone rows 16430 and 19681 contain fungal AZ057-prefix names; GOLD Go0454022 and projects Gp0322168/Gp0345663 concern Nemania serpens AZ0576; GenBank row `data/catalog/ncbi_genbank-0009.jsonl.gz:7440` concerns Anatum strain FSIS1607715, GCA_010372625.1, taxon 58712. None denotes AZ 057. These incidental source reads did not reopen any Eukaryota YAML review.

Ten ATB rows, 171021, 171041, 171050, 171060, 171195, 171198, 171213, 171219, 171293 and 171305, concern Campylobacter jejuni runs ERR10372620-29. Their full assembly, sample, checksum, availability and status fields were read: all have available FASTAs and passing source filters. Matching run digits establish no AZ 057 link.

No eligible whole-deposit association or missing required representation was established. Known assemblies do not justify inventing a BacDive entry or converting a bare strain name into a collection accession. Optional definitions, nomenclature, functional evidence and graphs may remain empty. iModulonDB is inapplicable because the YAML asserts no gene, regulator, pathway, functional trait or expression dataset; an assembly's publication does not create such a claim. All absence conclusions are bounded to inspected snapshots, roots and responses.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Broader GTDB species is promoted to exact strain identity.** The GTDB `taxonomy_mappings` closeMatch, GTDB `EXACT_SYNONYM`, identity xref and corresponding attestation conflate species membership with equivalence to AZ 057. This record's own GTDB row separates strain taxon 1037262 from species taxon 28901, and NCBI independently confirms the narrower strain rank. The species name cannot substitute for the individual strain's name. These derived assertions are one connected scope-inflation defect, not multiple independent findings. The species-wide count is not itself wrong.

Maintained owners are upstream kg-microbe's GTDB mapping, imported by `src/taxonmech/extract.py:501`, and the rank-unaware identity promotion in `src/taxonmech/seed.py:452` and `:468`. The inspected seeder treats closeMatch as identity and emits an exact synonym without testing target scope. Structural validators cannot establish this biological equivalence. No blocker is assigned because the main NCBI identity and lineage are correct.

## Recommended Edits

1. Correct or qualify the maintained upstream GTDB relation, preserve provenance and re-extract. Check direction from the source taxon's side; do not blindly substitute broadMatch, which assumes the record is broader than the source.
2. Make `src/taxonmech/seed.py` scope-aware before deriving exact strain synonyms and identity xrefs from a broader source species. Retain the true NCBI strain synonym and defensible species-membership evidence, with counts explicitly source-scoped.
3. Add a STRAIN-to-broader-GTDB-species regression and a valid same-species positive case in `tests/test_seed.py`, then regenerate through the validated writer. Do not hand-edit generated YAML, pages or an assumed overlay.

## Follow-up Checks

Run targeted seeder tests, schema and strict validation, `just verify-corpus` and `just qc`. Confirm the emitted AZ 057 record retains its correct NCBI identity without the exact species-name synonym or unqualified identity relation. Retry live GTDB authority access. Any future strain/genome enrichment must independently establish a whole-deposit identity and explicit source chain; shared names, taxonomy and samples alone are insufficient.

## Additional Notes

Only NCBITaxon:1037262 is judged, using its own complete YAML and source evidence. No neighboring verdict or assembly status was inherited. Eukaryota YAMLs were not reopened. This report is the only repository write for this target: records, source inventories, scope, history, status, branches, worktrees and GitHub remain unchanged. No paid research was used.
