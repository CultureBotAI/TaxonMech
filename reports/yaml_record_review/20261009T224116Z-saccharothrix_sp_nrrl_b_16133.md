# YAML Record Review: Saccharothrix sp. NRRL B-16133

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/saccharothrix_sp_nrrl_b_16133.yaml`
- Started UTC: 2026-10-09T22:38:30Z
- Finished UTC: 2026-10-09T22:41:16Z
- Verdict: pass

## Target

Entire 54-line generated `TaxonRecord` read. `NCBITaxon:103726` denotes NCBI's species-ranked placeholder Saccharothrix sp. NRRL B-16133, domain `BACTERIA`, parent `NCBITaxon:2593673`, genetic code 11, grounding `EXACT`, status `SEEDED`. Ten ancestors, one NCBITAXON attestation and the complete seed event were inspected. No synonyms, nomenclature, taxonomy mappings, nested strain entries, definition, functional evidence or graph are asserted. Zero represented BacDive strains describes source coverage, not absence of a biological strain.

HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. YAML SHA-256: `bbf03af502aabc7fd308df0428ae57aa6ad0ff2e94ad797b78f3816d32cf6b11`. Ignored-inclusive filename resolution found one target and no prior report for this stem.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/saccharothrix_sp_nrrl_b_16133.yaml`: passed.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/saccharothrix_sp_nrrl_b_16133.yaml --out /private/tmp/taxonmech-sacch-16133-20261009-validation.tsv --workers 1`: one file, zero errors; output TSV read and header-only.
- `uv run --offline python scripts/validate_history.py history`: reused this turn's 17 valid records, zero invalid links after a fresh empty diff for schema, history and validator.
- Complete own-row, lineage, source, type/status, scope and slug comparisons passed. These focused comparisons do not certify full-corpus reproduction or raw-provenance replay.
- Public NCBI taxonomy, nucleotide search, sequence annotation and genome discovery reads succeeded. The taxonomy browser failed, so complete structured authority responses were inspected. PubMed bibliography and abstract were read, not full text or supplements.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18552`, native scientific name `data/catalog/ncbi_names-0000.jsonl.gz:38589`, slug `data/taxa/PATHS.tsv:15248` and scope `curation/seed_scope.tsv:144193` agree. The complete backbone supports identity, species rank, parent, code, empty synonym fields and the 2026-09-13 snapshot.

All ten ancestor IDs, labels and ranks match the pinned chain: root; cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; Pseudonocardiales; Pseudonocardiaceae; Saccharothrix; unclassified Saccharothrix. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103726&retmode=xml) confirms the target, rank, parent, code and named ancestors; [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103726) confirms all ancestor IDs including root. Neither response supplies a successor or synonym. Complete backbone/type/status scans found no own child, type-material, merged-ID or dropped row.

`EXACT` grounds the NCBI node, not formal species nomenclature. The culture-style name does not authorize changing the NCBI species rank to STRAIN or inventing type status. Current NCBI lineage is carried, not reconciled with historical family proposals.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME. Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. No descendant supplies BacDive coverage. The full seed sentence matches the sole source and scope addition on 2026-09-13. This turn's inspected `_seed_timestamp` implementation and raw/ATB/StrainInfo extraction times, freshly confirmed unchanged, support `2026-09-13T17:54:04Z`, the latest extraction timestamp. The event denotes generation, not human review.

The [exact non-expanded nucleotide search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid103726%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one sequence, GI 5915971. Complete annotations and bibliography for [AF114811.1](https://www.ncbi.nlm.nih.gov/nuccore/AF114811.1) identify a partial 16S rRNA gene, organism Saccharothrix sp. NRRL B-16133, strain NRRL B-16133 and `taxon:103726`. Declared and actual lengths are both 1,510 bases; lowercase sequence alphabet is `acgt`, SHA-256 `7f6eb9d920f2768c059f2c45739a723d71072c45618b4cb4b7589cee0495c738`. Its direct-submission reference dates to 18 December 1998. This is marker identity evidence, not a whole genome or a validated chain to additional deposits.

The sequence's publication resolves to [PubMed 10826820](https://pubmed.ncbi.nlm.nih.gov/10826820/), Labeda and Kroppenstedt, January 2000, DOI `10.1099/00207713-50-1-331`, pages 331-336. The abstract describes comparative partial-16S phylogeny and proposes Actinosynnemataceae for a group including Saccharothrix. That historical proposal is not a reason to overwrite today's carried NCBI Pseudonocardiaceae lineage or to attribute all comparative chemotaxonomic observations to this isolate. No full-text or strain-specific phenotypic conclusion was inferred.

The [NCBI genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103726/dataset_report?page_size=100) returned `{}`. This supplies no positive assembly evidence in that response, not proof of worldwide genome absence. An ignored-, hidden- and compression-inclusive search for AF114811 across the same ten local roots returned no match. The marker was not silently promoted into a required genome link or a new source attestation.

## Completeness

`rg --no-ignore --hidden -n -z -i` searched bounded numeric identity, scientific-name/strain spellings and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 90 matching rows were read completely or in lossless common-field/delta representations. Five SOURCE.json files and history filenames were separately checked. No own history entry was established.

Whole-identifier false matches were distinguished rather than treated as taxon evidence:

- BacDive 103726 is Rhodococcus sp. ST000904, taxon 194249. Its native record, raw row and the complete response-279 metadata object confirm that the matching SOURCE.json request is for a BacDive ID, not NCBI taxon 103726. That object names records-0278.json.gz and hash `594181e6d0d9950e7c778c27296a1607cc6a599f118ed1895784a3d0cc08437a`.
- CIP 103726 is Campylobacter jejuni, BacDive 138459, StrainInfo 45258, deposit 149621 and GOLD Go0168162. Its source-specific species/subspecies taxon IDs 197 and 32022 do not implicate Saccharothrix.
- NBRC 103726 is Teredinibacter sp. F316, BacDive 140442, associated with DSM 21037 and StrainInfo 396907. Native source classification uses taxon 2294030 or genus 2425. It is not NRRL B-16133.
- DSM 103726 is Pseudokineococcus basanitobsidens SKC1-2, taxon 1926649, BacDive 141047, LPSN 796011, StrainInfo 406412 and deposit 913711. Its native and transformed chains support GCA/GCF_037482545.1, PATRIC 1926649.3, IMG 8124691089 and GOLD Go0620725/Gp0828711/Ga0674328. All matching assembly, genome-record, related-record, type-material and collection rows belong to that other organism.
- MGBC103726 is an uncultured Muribaculaceae sample/assembly GCA_949004235.1, not this NCBI taxon. Enterobacter hormaechei 3131 matches plasmid CP103726 within GCA_024918795.1. A Pseudomonas aeruginosa Pae_CF67.06p assembly matches the name ASM103726v1, and unrelated Salmonella and Campylobacter entries match bare strain/isolate digits.
- Other GTDB hits are contig/scaffold N50/N75/N90 values equal to 103726 in Streptomyces, Oscillospiraceae, Clostridium, Saccharibacteria, Pseudomonas, Doudnabacteria and Cupriavidus records. Their complete metadata identifies unrelated taxa; statistics are not taxon links.

No additional supported synonym, required nomenclature or mapping, successor, eligible whole-deposit genome chain or missing required representation was established. Optional definitions, evidence and graphs may remain absent. iModulonDB is inapplicable because the YAML asserts no gene function, regulator, pathway, phenotype or transcriptomics dataset. A ribosomal marker used for identity does not create such a claim. All absence conclusions are bounded to the inspected roots, snapshots and responses, not every possible external collection or publication.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. NCBI identity, lineage, source coverage, lifecycle and provenance agree. The single 16S record supports the named taxon, while the numerous numeric catalog hits do not supply missing Saccharothrix associations.

## Recommended Edits

None required. Preserve the NCBI placeholder, rank, lineage and SEEDED status. Future enrichment must verify actual NRRL B-16133 collection evidence and explicit source-specific links rather than repurpose DSM/CIP/NBRC numbers or numeric catalog statistics. Supported changes belong in maintained source transforms or `src/taxonmech/seed.py`, with tests and regeneration; do not hand-edit the generated YAML or assume an existing curator overlay.

## Follow-up Checks

No corrective validation is required by a finding. Before regenerated publication run `just verify-corpus` and `just qc`. Any later taxonomic revision belongs upstream and must distinguish this placeholder from formally named species; any genome addition requires supported deposit identity and explicit source-chain evidence. Historical 16S phylogeny alone is insufficient for either action.

## Additional Notes

Only NCBITaxon:103726 is judged. No neighboring YAML or Eukaryota review was reopened. No YAML, source, inventory, scope, history, status, branch, worktree or GitHub item changed. This new report is the only repository write for the target. No paid research was used.
