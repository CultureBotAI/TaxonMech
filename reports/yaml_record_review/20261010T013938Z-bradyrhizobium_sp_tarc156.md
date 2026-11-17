# YAML Record Review: Bradyrhizobium sp. TARC156

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bradyrhizobium_sp_tarc156.yaml`
- Started UTC: 2026-10-10T01:34:08Z
- Finished UTC: 2026-10-10T01:39:38Z
- Verdict: pass

## Target

The complete 58-line generated `TaxonRecord` was read. `NCBITaxon:103737` denotes Bradyrhizobium sp. TARC156, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2631580`, genetic code 11, grounding `EXACT`, status `SEEDED`.

The record carries ten ancestors, one NCBI synonym, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. A strain-bearing authority name does not turn the taxon concept into a culture-collection accession or change its authority rank.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bradyrhizobium_sp_tarc156.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bradyrhizobium_sp_tarc156.yaml --out /private/tmp/taxonmech-tarc156-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified own identity, every ancestor, code, synonym source columns, attestation, index/scope entries and seed reason. Complete backbone scanning found no direct child. Exact own-ID type-material, merged-ID and dropped scans found none.
- Both native name rows, complete live taxonomy responses, the sole exact-taxonomy nucleotide annotation and the cited publication's PubMed abstract and identifiers were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused source agreement is not corpus reproduction. No causal graph is asserted, so `just validate-products` has no applicable nodes.
- Not checked: primary article full text, independent sequence alignment, phylogeny, genome comparison or experimental reanalysis. Publisher requests for DOI 10.1139/w99-061 and a secondary literature lead, DOI 10.1080/00380768.1999.10409366, returned HTTP 403. Search snippets were not treated as inspected evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18563`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103737&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103737) agree on exact scientific name, species rank, parent and code.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Nitrobacteraceae, Bradyrhizobium and unclassified Bradyrhizobium. Every stored ancestor ID, label and rank matches the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1. No alternate hierarchy is imposed.

`data/catalog/ncbi_names-0000.jsonl.gz:38621` is the own scientific-name row; line 38622 is the synonym Bradyrhizobium sp. TARC 156. The pinned synonym and live EFetch agree. The spacing variant supports the stored `EXACT_SYNONYM` with source NCBITaxon. `EXACT` concerns this NCBI concept, not valid publication of a species name or equivalence to B. japonicum or B. elkanii.

## Evidence

The sole NCBITAXON attestation has the exact own ID and label, count 1, unit `NAME`, snapshot 2026-09-13. It counts a source name assertion, not strains, deposits, sequences or genomes.

A live exact nucleotide query, `txid103737[Organism:exp]`, returned one entry, UID 5881552. Its complete annotation identifies [D85402.1](https://www.ncbi.nlm.nih.gov/nuccore/D85402.1), a 264-base partial 16S rRNA sequence, organism Bradyrhizobium sp. TARC156, strain TARC 156, `taxon:103737`. Declared and actual lengths agree and the sequence uses A/C/G/T. The rRNA feature has partial endpoints and a non-experimental annotation-inference qualifier. This is marker evidence, not a genome assembly or proof of a functional phenotype. The query is not a global sequence census.

The annotation explicitly cites [Ando and Yokoyama, PMID 10528395](https://pubmed.ncbi.nlm.nih.gov/10528395/), DOI 10.1139/w99-061, Canadian Journal of Microbiology 45:639-645 (1999). The inspected abstract describes partial 16S sequencing and nifDK-probe RFLP comparisons of Thai soybean bradyrhizobia with USDA strains. Several distinct study strains shared a partial 16S sequence. That observation does not establish strain equivalence, a common deposit, or identical genomes. The accession's explicit bibliography supports the publication link; the abstract alone does not assign every experimental result or geographic detail to TARC156.

The YAML asserts taxonomy and provenance only. No soybean-nodulation mechanism, nitrogen-fixation phenotype, antibiotic response or causal graph is inferred from the paper title, genus or marker annotation.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 103737, TARC156 with optional space/underscore/hyphen, and the target slug. Identity and matching fields of all 95 matching lines were inspected; own native name rows and ambiguous LPSN, culture-collection and ATB rows were additionally read in full.

The broad numeric matches are not missing target links:

- BacDive 23777 and CIP 103737 concern Bartonella henselae, including NCBITaxon:38323/283166. LPSN 783485 and 784812 concern Bartonella henselae and its Rochalimaea name, not Bradyrhizobium. BacDive record 103737 concerns Rhodococcus sp. ST002174, NCBITaxon:194249; its record number is not this taxon ID.
- BacDive 131683, DSM 103737, NCBITaxon:1348468, GCA_014196925.1, GCF_014196925.1, BV-BRC 1348468.3 and GOLD Go0511028/Gp0401082/Ga0373271 concern Chelatococcus caeni. The five ATB genome links and one strain link inspected in full use BacDive 131683 and BioSample SAMN13172972 with explicit Chelatococcus source evidence. None supports a TARC156 join.
- Other genome candidates contain Salmonella strain 103737, PNUSAS103737, Eubacteriales MGBC103737, Klebsiella component CP103737, or an N50 value of 103737. StrainInfo candidates contain a Nitrosospira deposit SI-DP 103737, the Bartonella/Chelatococcus deposits, Kluyveromyces sequence KY103737, or Rigidoporus designation 103737-S. Their identity fields exclude the target; no eukaryotic taxon YAML was opened.

A follow-up ignored/compressed-inclusive search for D85402, PMID 10528395 and DOI 10.1139/w99-061 returned five unrelated rows, all read in full: four ATB SeqKit sums containing the accession substring and Salmonella assembly GCA_010528395.1 containing the PMID digits. These are not marker or bibliography links. Five SOURCE.json files were separately parsed; the only broad numeric match was the BacDive 103737 request metadata already distinguished above.

Gitignore-independent filename enumeration under the taxon corpus and report directory found only this target YAML and no prior matching report. History filename inspection found no target-specific filename. Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. These are bounded repository findings, not global absence claims.

Zero correctly counts inventoried BacDive strains, not the existence of the named isolate or its public marker. No source-supported target culture-deposit/genome chain was established. Optional definitions, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable to the taxonomy-only claims; no adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, synonym, provenance, count semantics and seeded status are supported. Unavailable article full texts and skipped corpus checks remain explicit review limitations.

## Recommended Edits

None required. Preserve the authority label/rank, exact spacing synonym and zero BacDive count. Do not transfer unrelated culture accessions, count the 16S marker as a genome, or treat identical short markers as strain equivalence.

Future authorized corrections belong in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect requires a change here; generated YAML must not be hand-edited.

## Follow-up Checks

Future phenotype enrichment requires the original experiment and a target-specific assignment, not title-level attribution. New deposit/genome links require explicit source-supported identity chains and full culture accessions. Preserve sequence accession versions as supplied; no version should be invented for an unversioned imported accession.

After an authorized source refresh, rerun schema/strict/history validation and documented full-corpus reproduction/QC gates. Focused matching does not replace those checks.

## Additional Notes

- YAML SHA-256: `41b663a76012d76f842ec7fb1c47f55f1aab2d5610f8c0c5f7f05f000f99682b`.
- `data/taxa/PATHS.tsv:15284` and `curation/seed_scope.tsv:144197` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and the exact one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
