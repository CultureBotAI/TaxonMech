# YAML Record Review: Bradyrhizobium sp. TARC124

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bradyrhizobium_sp_tarc124.yaml`
- Started UTC: 2026-10-10T00:46:37Z
- Finished UTC: 2026-10-10T00:50:42Z
- Verdict: pass

## Target

The complete 58-line generated `TaxonRecord` was read. `NCBITaxon:103736` denotes Bradyrhizobium sp. TARC124, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2631580` (unclassified Bradyrhizobium), genetic code 11, grounding `EXACT`, status `SEEDED`.

It carries ten ancestors, one NCBI exact synonym, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. The strain-like designation does not override the authority's species rank.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bradyrhizobium_sp_tarc124.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bradyrhizobium_sp_tarc124.yaml --out /private/tmp/taxonmech-tarc124-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured scans matched identity, full lineage, code, synonym, own attestation, index/scope entries and seed-event text. Complete backbone scanning found no direct child; exact own-ID type-material, merged-ID and dropped scans found none.
- All 83 local search candidate lines were parsed for identity and matching fields. The two own native NCBI name rows were read completely. Live taxonomy responses, complete primary nucleotide annotation apart from the summarized sequence, and the complete linked PubMed abstract/identifiers were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused agreement is not corpus reproduction. No causal graph is asserted, so `just validate-products` has no applicable nodes.
- Full experimental papers, strain-specific phenotype tables, independent phylogeny and genome comparisons were not audited. Publisher requests for DOI 10.1139/w99-061 and DOI 10.1080/00380768.1999.10409366 returned HTTP 403. PubMed's web page returned a browser check, but its public EFetch API supplied the complete abstract and identifiers. Search snippets were not used as experimental proof.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18562` agrees with [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103736&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103736): Bradyrhizobium sp. TARC124, species rank, parent 2631580 and code 11.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Nitrobacteraceae, Bradyrhizobium and unclassified Bradyrhizobium. Every stored ancestor ID, label and rank matches the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1.

`data/catalog/ncbi_names-0000.jsonl.gz:38619` is the scientific-name row and line 38620 is the synonym Bradyrhizobium sp. TARC 124. The pinned exact-synonym column and live authority agree. The record correctly preserves the spelling variant, its source and exact-synonym classification.

Exact grounding identifies this NCBI concept; it does not establish formal nomenclatural validity, identity with a named Bradyrhizobium species or equivalence to USDA 124.

## Evidence

The sole NCBITAXON attestation has exact own ID/label, count 1, unit `NAME`, snapshot 2026-09-13. It is not a count of genomes, culture deposits or experiments.

A live NCBI nucleotide query for `txid103736[Organism:exp]` returned one entry. Complete [D85401 metadata](https://www.ncbi.nlm.nih.gov/nuccore/D85401) identifies D85401.1, a 264-base partial 16S rRNA sequence, explicitly organism Bradyrhizobium sp. TARC124, strain TARC 124 and `taxon:103736`. The rRNA feature has partial endpoints and a non-experimental inference qualifier. This sequence is a marker, not a genome or a culture-collection accession. It is supplementary identity evidence, not currently a YAML sequence assertion. The nucleotide query is not a global sequence census.

The marker bibliography explicitly links [Ando and Yokoyama, PMID 10528395](https://pubmed.ncbi.nlm.nih.gov/10528395/), DOI 10.1139/w99-061, Canadian Journal of Microbiology 45:639-645 (1999). The inspected abstract describes RFLP and partial-16S comparisons of Thai soybean bradyrhizobia and USDA reference strains, with relatedness and distinctions depending on the comparison. It does not name TARC124 individually; the marker bibliography supplies that connection.

A short shared marker and study-level relationships do not authorize renaming the taxon as B. japonicum or B. elkanii. The YAML makes no nodulation, nitrogen-fixation, antibiotic-resistance, gene-function or habitat assertion, and none was inferred from the abstract.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 103736, TARC124 with optional space/hyphen/underscore separators, and the slug. All 83 candidate lines were resolved using structured identity and matching-field inspection.

The principal unrelated matches were:

- BacDive 103736 is Rhodococcus sp. ST002173, taxon 194249. Its DOI and fetch-request metadata use a BacDive namespace, not NCBI taxon 103736.
- DSM 103736 belongs to Enterobacillus tribolii, taxon 1487935, BacDive 132219. Its GenBank/RefSeq GCA/GCF_003363015.1, GTDB, BV-BRC, GOLD and derived ATB associations do not belong to TARC124. GOLD Go0389919, Gp0251931 and Ga0215724 remain organism/project/analysis references, not this target's genomes.
- CIP 103736 is associated with BacDive 138487 and StrainInfo SI-ID 69003, taxon 57037; native sources use Lactobacillus/Lacticaseibacillus zeae. These culture deposits and the derived SI rows are unrelated to TARC124, regardless of their shared numeric portion.
- Other assembly candidates matched a scaffold/contig statistic, a strain/isolate containing 103736, or CP103736 in the Klebsiella pneumoniae 913 assembly GCA_024918875.1. SI-ID 178675's KY103736 is also an accession in an unrelated source record. None supplies the target's identity.

A follow-up D85401 search over the same ignored/compressed-inclusive roots returned six ATB catalog lines. Their only matching fields were hexadecimal substrings in SeqKit sums for unrelated organisms. No candidate was a D85401 sequence link; SeqKit sums are neither sequence accessions nor MD5 evidence.

Five SOURCE.json files were separately parsed; the only target-number matches were BacDive 103736's fetch request. Gitignore-independent filename enumeration under the taxon corpus and report directory found the target YAML and four unrelated report timestamps containing 103736, but no prior report for this slug. History filename inspection found no target-specific filename. These are bounded repository checks, not global absence claims.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. No immediate backbone child supplies descendant inventory. Zero correctly counts inventoried BacDive strains, not whether an isolate was studied. No repository-supported culture-deposit/genome chain for TARC124 was established.

Optional definition, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable to this taxonomy-only YAML; gene-probe language in a contextual abstract does not create a gene or transcriptomics claim. No adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, synonym, provenance, source-count semantics and seeded status are supported. Skipped corpus checks and uninspected strain-level experimental details remain limitations.

## Recommended Edits

None required. Preserve the authority species rank, unclassified placement, source synonym and zero BacDive count. Do not import DSM 103736, CIP 103736, BacDive 103736 or CP103736 by numeric resemblance, treat D85401 as a genome, or infer a named-species reassignment from partial 16S similarity.

Any future authorized correction belongs in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect requires a change here; generated YAML must not be hand-edited.

## Follow-up Checks

Before phenotype or mechanism enrichment, inspect the full papers and strain-specific experimental evidence, keeping TARC124 distinct from USDA 124 and other TARC strains. New genome/deposit links require an explicit source-supported identity chain and whole authority-qualified accessions.

After an authorized source refresh, rerun schema/strict/history validation and documented full-corpus reproduction/QC gates. Focused matching does not replace those checks.

## Additional Notes

- YAML SHA-256: `30ad1ae7e694dae32d7f4248372ec54483f06c88bbd268223a343533a147125c`.
- `data/taxa/PATHS.tsv:15273` and `curation/seed_scope.tsv:144196` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and the exact one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
