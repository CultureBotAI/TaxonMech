# YAML Record Review: Saccharothrix sp. NRRL B-16108

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/saccharothrix_sp_nrrl_b_16108.yaml`
- Started UTC: 2026-10-09T22:53:40Z
- Finished UTC: 2026-10-09T22:56:24Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read. `NCBITaxon:103727` denotes Saccharothrix sp. NRRL B-16108, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2593673` (unclassified Saccharothrix), code 11, grounding `EXACT`, status `SEEDED`. All ten ancestors, the sole attestation and complete seed event were inspected. There are no asserted synonyms, taxonomy mappings, identity xrefs, nomenclature, nested strains, definition, functional evidence or graph. Zero represented BacDive strains does not imply absence of the culture or sequence evidence.

HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; YAML SHA-256 `e23e7aaf18d87a38e7ef28002a2804bfda7126d99af16ee5ec90e251e318ec2f`. Ignored-inclusive filename resolution found exactly one target and no prior report. Guidance, schema, implementation and history remained unchanged from prior complete reads and the checklist inspected during this turn.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/saccharothrix_sp_nrrl_b_16108.yaml`: passed.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/saccharothrix_sp_nrrl_b_16108.yaml --out /private/tmp/taxonmech-saccharothrix-16108-20261009-validation.tsv --workers 1`: one file, zero errors; header-only output TSV read.
- `uv run --offline python scripts/validate_history.py history`: earlier in this same turn, 17 valid records and zero invalid links. History and validator were confirmed unchanged before reusing that result; no second run is claimed.
- Complete own-row inventory, ten-ancestor, type/status, attestation, scope and slug checks passed. These bounded comparisons do not certify full-corpus reproduction.
- NCBI EFetch and Datasets taxonomy, genome-index, exact-taxid nucleotide search and sequence-metadata reads succeeded. Taxonomy browser access failed. PubMed bibliography and abstract were read; full article and supplementary data were not.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18553`, native scientific name `data/catalog/ncbi_names-0000.jsonl.gz:38590`, slug `data/taxa/PATHS.tsv:15252` and scope `curation/seed_scope.tsv:144194` agree. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103727&retmode=xml) independently confirms the exact name, species rank, parent and code. [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103727) confirms all ten ancestor IDs including root.

The complete root-first chain matches the pinned backbone in labels and ranks: root; cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; Pseudonocardiales; Pseudonocardiaceae; Saccharothrix; unclassified Saccharothrix. A deposit designation in an unnamed species-level placeholder does not justify changing NCBI's `SPECIES` rank to `STRAIN`. This record does not claim that the placeholder is a validly published species name.

Complete backbone/status scans found no own child, type-material, merged-ID or dropped-ID row. The current source does not assert type-strain status. The inspected authority places the taxon in Pseudonocardiaceae; older phylogenetic literature is not silently used to replace that lineage.

## Evidence

NCBITAXON 1 NAME and the 2026-09-13 snapshot note match the complete backbone. Exact own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row, and no child contributes BacDive coverage. The full seed sentence matches the sole NCBITAXON source and exact admission reason, dated 2026-09-13. Source manifests inspected this turn contain raw extraction 17:50:44Z, StrainInfo 17:29:00Z and ATB 17:54:04Z on that date. The inspected `_seed_timestamp` implementation uses the latest, supporting `2026-09-13T17:54:04Z`. `SEEDED` describes generation, not human approval.

The [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103727/dataset_report) returned an empty object. The [exact-taxid nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid103727%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one record, GI 5915970. Its [GenBank entry AF114810.1](https://www.ncbi.nlm.nih.gov/nuccore/AF114810.1) explicitly gives organism Saccharothrix sp. NRRL B-16108, strain NRRL B-16108 and `taxon:103727`. It is a 1,512-base partial 16S ribosomal RNA sequence, not a genome assembly. Complete features and bibliography were read; declared and returned nucleotide lengths agree, alphabet is acgt, and the returned lowercase sequence SHA-256 is `330b634c972daaa07539ae8944042a81be1729eead9cb78448f827e57c318a54`. The record was created 1999-09-21 and updated 2013-11-14. No type-status or genome-equivalence assertion is inferred from the marker.

The marker cites Labeda and Kroppenstedt's [Phylogenetic analysis of Saccharothrix and related taxa: proposal for Actinosynnemataceae fam. nov.](https://pubmed.ncbi.nlm.nih.gov/10826820/), IJSEM, January 2000, PMID 10826820, DOI `10.1099/00207713-50-1-331`. The inspected abstract describes comparative partial 16S analysis and a historical family proposal. It does not independently establish every phenotype or modern family placement for this individual culture. Its Actinosynnemataceae proposal is preserved as historical context, not reconciled into current NCBI's Pseudonocardiaceae lineage. Full text and supplements were not inspected.

## Completeness

An initial `rg --no-ignore --hidden -n -z -i` substring search across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history` returned 650 addresses. To separate the taxon number from longer numbers, the same complete ignored/hidden/compressed search was repeated with `(^|[^0-9])103727([^0-9]|$)|NRRL[ _-]*B[ _-]*16108|saccharothrix_sp_nrrl_b_16108`. All 54 resulting rows were read completely, including lossless common-field/delta views. The 596 substring-only rows excluded by the numeric boundary were not all read and are not cited as biological evidence; all complete designation and slug matches remained eligible.

Five SOURCE.json files were separately parsed. The numeric match in BacDive SOURCE.json response 279 is a requested BacDive identifier, not an NCBI identity: the complete matching BacDive row identifies Rhodococcus sp. ST000912, taxon 194249. No own history filename was found. A separate ignored/hidden/compressed search for AF114810 found zero rows in the same ten roots; the five metadata files and history filenames were also checked for that accession with no match. This is a bounded local-inventory result, not a statement that the live marker is absent from NCBI.

Complete false-positive source checks included:

- BacDive 103727 at row 27847 and raw strain row 27848 are Rhodococcus ST000912, not this Saccharothrix.
- CIP 103727 is BacDive 139098 and StrainInfo 42768, deposit 148607, linked to Arcobacter butzleri taxon 28197. GOLD Go0242495 instead calls that deposit Aliarcobacter cryaerophilus, taxon 28198. This cross-source conflict was preserved; neither identity is Saccharothrix. All corresponding raw, native and StrainInfo related/link rows were read.
- DSM 103727 is BacDive 158368 and StrainInfo 399363, deposit 906144, Glycomyces sediminimaris taxon 1761452, also GOLD Go0620729 and LPSN 796410. Its type-material designations, KU174196 marker and collection aliases belong to that Glycomyces, not NRRL B-16108.
- StrainInfo deposit number 103727 is ATCC 25191, Stigmatella erecta taxon 83460, within StrainInfo 38403. The complete record and sequence-deposit links preserve DQ768128 for ATCC 25191 separately from DSM 16858-linked sequences and unversioned GCA_900111745. None establishes a Saccharothrix association.
- CP103727 in two BV-BRC rows and GOLD Ga0608842 belongs to Klebsiella pneumoniae 2289, GCA_024918835.1. MGBC103727 belongs to uncultured Prevotella, GCA_948911605.1, with suppressed historical RefSeq GCF_948911605.1. ASM103727v1 belongs to Pseudomonas aeruginosa, GCA/GCF_001037275.1. PNUSAS103727 and 2024LABP103727.R32G belong to other organisms. Their source identities and statuses were not transferred to this target.
- Ten complete GTDB hits contain those unrelated identifiers or assembly-contiguity statistics equal to 103727, not NCBI taxon 103727. The remaining ATB hit, row 2956859, is Salmonella Infantis, run SRR29339963, sample SAMN41769994, assembly ERZ26812183; the digits occur in its checksum. Its FASTA is available and filters pass, but it has no NRRL B-16108 link.

No eligible BacDive/whole-deposit chain or required missing representation was established. The direct marker association is useful future enrichment evidence but does not require inventing a BacDive strain entry or an assembly. Optional nomenclature, definitions, functional evidence and graphs may remain empty. iModulonDB is inapplicable because the YAML asserts no gene, regulator, pathway, functional trait or expression dataset; a marker discovered during review does not create such a YAML assertion. All absence statements are bounded to inspected roots, snapshots, query keys and responses.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The represented identity, species rank, lineage, attestation and generation history are supported. This pass does not certify all possible biological knowledge or full-corpus reproduction.

## Recommended Edits

None required for the represented claims. If marker enrichment is later authorized, preserve AF114810.1 as partial 16S evidence for the explicit NRRL B-16108/taxon association, not as a genome or type-strain claim. Establish a maintained source transform or curation input and regenerate through the validated writer; do not directly patch this generated YAML or create a BacDive strain from an unrelated numeric identifier.

## Follow-up Checks

For future enrichment, independently verify whole-deposit identity and any source-native sequence link. Re-run schema and strict validation, history validation when history changes, then `just verify-corpus` and `just qc` after maintained inputs change. Retry taxonomy browser access when available; successful authority APIs already support the current identity. No unresolved blocker remains for this review.

## Additional Notes

Only NCBITaxon:103727 is judged using its complete YAML and independently inspected evidence. No prior Saccharothrix verdict was inherited. Eukaryota YAMLs were not reopened. This new report is the only repository write for this target; YAMLs, sources, inventories, scope, history, status, branches, worktrees and GitHub remain unchanged. No paid research was used.
