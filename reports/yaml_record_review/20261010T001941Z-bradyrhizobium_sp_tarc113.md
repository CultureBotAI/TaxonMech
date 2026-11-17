# YAML Record Review: Bradyrhizobium sp. TARC113

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bradyrhizobium_sp_tarc113.yaml`
- Started UTC: 2026-10-10T00:17:17Z
- Finished UTC: 2026-10-10T00:19:41Z
- Verdict: pass

## Target

The entire 58-line generated `TaxonRecord` was read. `NCBITaxon:103735` denotes Bradyrhizobium sp. TARC113, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2631580` (unclassified Bradyrhizobium), genetic code 11, grounding `EXACT`, status `SEEDED`.

It contains ten ancestors, one NCBI exact synonym, zero BacDive strains, one NCBITAXON name attestation and a seed event. The strain-like designation in the label is not a reason to override NCBI's species rank.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bradyrhizobium_sp_tarc113.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bradyrhizobium_sp_tarc113.yaml --out /private/tmp/taxonmech-tarc113-20261010-validation.tsv --workers 1`: one file, zero errors; the output was reread and contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured scans matched the pinned identity, full lineage, synonym, code, own attestation, scope/index rows and seed-event text. Complete backbone scanning found no immediate child; exact own-ID scans found no type-material, merged-ID or dropped entry.
- Own native NCBI name rows were read in full. Native/TSV candidate identities and matched fields were checked to distinguish numeric collisions. Live NCBI taxonomy APIs, primary marker metadata and the marker-linked publication abstract were independently inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused source agreement is not corpus reproduction. `just validate-products` has no applicable causal-graph nodes.
- NCBI taxonomy browser retrieval returned a tool error; EFetch and Datasets succeeded. The full experimental paper and any whole-genome sequence were not audited. Search snippets supplied leads only and were not used as experimental evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18561` agrees with [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103735&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103735): Bradyrhizobium sp. TARC113, species rank, parent 2631580 and code 11.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Nitrobacteraceae, Bradyrhizobium and unclassified Bradyrhizobium. Every stored ancestor ID, label and rank matches the pinned backbone; live EFetch confirms the chain below root and Datasets includes root ID 1.

`data/catalog/ncbi_names-0000.jsonl.gz:38617` supplies the scientific name and row 38618 supplies Bradyrhizobium sp. TARC 113 as an NCBI synonym. The space-bearing exact synonym is source-supported, not an invented alternative. `EXACT` grounds this NCBI concept; it does not claim formal species nomenclatural validation or identity with B. japonicum.

## Evidence

The sole attestation is NCBITAXON, source ID 103735, count 1 `NAME`, snapshot 2026-09-13. Its source label and provenance agree with the inventory. This does not imply one cultured deposit or one genome.

Live [D85400 metadata](https://www.ncbi.nlm.nih.gov/nuccore/D85400) identifies D85400.1, a 264-base partial 16S sequence, explicitly Bradyrhizobium sp. TARC113, strain TARC 113 and `taxon:103735`. The source's rRNA feature retains a non-experimental inference qualifier. The sequence is independent identity context, not a complete genome, a culture-deposit accession or a phenotype assay. It is not currently an asserted YAML field.

The marker bibliography matches [Ando and Yokoyama, PMID 10528395](https://pubmed.ncbi.nlm.nih.gov/10528395/), DOI 10.1139/w99-061, Canadian Journal of Microbiology 45:639-645 (1999). The complete EFetch abstract describes partial 16S and RFLP comparisons among Thai and USDA bradyrhizobia. A shared short marker segment does not establish whole-strain equivalence or authorize replacing the current NCBI label with B. japonicum or B. elkanii. Cohort-level nodulation/genetic results were not promoted to a new TARC113 mechanism or phenotype claim.

The publication and marker are supplementary review context. The record's actual claims remain its NCBI identity, lineage and inventory provenance; it cites no unsupported experimental paper or snippet.

## Completeness

An ignored-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded taxon number 103735, TARC113/TARC 113/TARC-113 spellings and the record slug. The 69 matching lines comprised 29 native JSON and 40 TSV rows. Their identities and matched fields were inspected; own source rows were read completely.

Material collisions include:

- BacDive 103735 is Rhodococcus sp. ST002172, NCBI taxon 194249, not this Bradyrhizobium taxon. The SOURCE.json request-ledger occurrence is the same unrelated BacDive identifier.
- CIP 103735 belongs to Streptococcus mutans, whereas DSM 103735 belongs to Rouxiella silvae, taxon 1646373. GOLD Go0620739 and the corresponding LPSN/type-material and strain links follow Rouxiella.
- SI-DP 103735 occurs in Nitrosospira multiformis, SI-ID 38407/BacDive 132056, taxon 1231; its multiple sequence links cannot be transferred by matching digits.
- MGBC103735, ASM103735v1, CP103735, numerical assembly statistics and several unrelated isolate names are not taxon identifiers.
- One fungal StrainInfo designation also contains 103735. Its native source identity was checked, but no Eukaryota YAML was opened.

A follow-up ignored-inclusive search for D85400 over the same roots returned nine ATB catalog hash-substring matches. Structured inspection showed unrelated organisms and SeqKit hashes, not the target marker or a supported BioSample chain. No own marker-bearing or eligible strain/genome assertion was found in the searched repository sources. This is not a global claim that no other sequence or genome exists.

Complete structured scans found no own-ID BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. With no backbone child, there is no descendant strain inventory to aggregate. Thus `strain_count: 0` correctly counts the inventoried BacDive entries, not the existence of TARC113 in research.

Five SOURCE.json files were parsed separately. Gitignore-independent filename searching found this target YAML and no prior report; history filename inspection found no target-specific filename. Optional definition, record-level evidence, nomenclature, mappings and causal graphs are not mandatory for this seeded record.

iModulonDB gene/module searches were not applicable: the YAML asserts no gene, regulator, pathway or transcriptomics result. Historical gene names in a contextual paper do not create new record claims. No adapter run or dataset absence is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, synonym, provenance, count semantics and seed status are supported. Skipped corpus checks and the uninspected full paper remain limitations.

## Recommended Edits

None required. Preserve the NCBI species rank and unclassified placement, the exact space-bearing synonym and the zero BacDive count. Do not attach numerically matching identifiers from other sources, infer a genome from D85400, or rename the record from a short-sequence comparison.

Future authorized changes belong in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No such correction is established here; generated YAML must not be hand-edited.

## Follow-up Checks

Any future genome/deposit enrichment needs an explicit primary-source identity chain. Detailed biological claims need TARC113-specific experimental support, not merely membership in a paper's cohort.

After an authorized source refresh, rerun schema/strict/history validation and the documented full-corpus reproduction/QC gates. The present marker evidence is insufficient by itself to reconcile species taxonomy.

## Additional Notes

- YAML SHA-256: `5b4d5b8100b15253f12d428bc291071bf7e663ed6f9c0855e6e10e180ae4b541`, unchanged on reread.
- `data/taxa/PATHS.tsv:15264` and `curation/seed_scope.tsv:144195` uniquely identify the target. The seed retains 2026-09-13T17:54:04Z and its matching one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed, and no status was promoted.
