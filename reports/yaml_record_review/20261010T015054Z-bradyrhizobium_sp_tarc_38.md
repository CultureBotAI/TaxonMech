# YAML Record Review: Bradyrhizobium sp. TARC 38

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bradyrhizobium_sp_tarc_38.yaml`
- Started UTC: 2026-10-10T01:47:59Z
- Finished UTC: 2026-10-10T01:50:54Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:103738` denotes Bradyrhizobium sp. TARC 38, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2631580`, genetic code 11, grounding `EXACT`, status `SEEDED`.

It carries ten ancestors, no synonym list, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. The authority's strain-bearing species label does not by itself establish a culture-collection deposit or a genome link.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bradyrhizobium_sp_tarc_38.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bradyrhizobium_sp_tarc_38.yaml --out /private/tmp/taxonmech-tarc38-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links, run earlier this turn; history remains unchanged.
- Structured comparisons verified identity, every ancestor, code, empty synonym columns, attestation, index/scope entries and seed reason. Complete backbone scanning found no direct child. Exact own-ID type-material, merged-ID and dropped scans found none.
- The complete native name row, both live taxonomy responses, the sole exact-taxonomy nucleotide annotation and the cited PubMed abstract and identifiers were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused source agreement does not prove corpus reproduction. No causal graph is asserted, so `just validate-products` has no applicable nodes.
- Not checked: independent alignment, phylogeny, genome comparison, experimental reanalysis or primary article full text. Requests for the marker's publication, DOI 10.1139/w99-061, and a serology/antibiotic literature lead, DOI 10.1080/00380768.1999.10409366, returned HTTP 403. Search snippets and uninspected later papers were not used as experimental evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18564`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103738&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103738) agree on exact scientific name, species rank, parent and code.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Nitrobacteraceae, Bradyrhizobium and unclassified Bradyrhizobium. Every stored ancestor ID, label and rank matches the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1.

`data/catalog/ncbi_names-0000.jsonl.gz:38623` contains the exact scientific name and own taxon ID. The pinned synonym columns are empty and live EFetch supplies no OtherNames. `EXACT` concerns this NCBI concept, not identity with another TARC isolate or valid publication of a named Bradyrhizobium species.

## Evidence

The sole NCBITAXON attestation preserves the exact own ID and label, count 1, unit `NAME`, snapshot 2026-09-13. Its count is not a strain, deposit, sequence or genome count.

A live exact nucleotide query, `txid103738[Organism:exp]`, returned one entry, UID 5881553. [D85403.1](https://www.ncbi.nlm.nih.gov/nuccore/D85403.1) is a 264-base partial 16S rRNA sequence whose complete annotation explicitly gives organism Bradyrhizobium sp. TARC 38, strain TARC 38 and `taxon:103738`. Declared and actual sequence lengths agree; the alphabet is A/C/G/T. The rRNA has partial endpoints and a non-experimental annotation-inference qualifier. It is a marker, not a genome or a functional assay. The query is not a global sequence census.

The annotation explicitly cites [Ando and Yokoyama, PMID 10528395](https://pubmed.ncbi.nlm.nih.gov/10528395/), DOI 10.1139/w99-061, Canadian Journal of Microbiology 45:639-645 (1999). The inspected abstract describes partial 16S sequencing and nifDK-probe RFLP comparisons of Thai soybean bradyrhizobia with USDA strains, including shared partial 16S sequences among distinct study strains. This supports publication context without equating isolates, deposits or genomes. The accession's own bibliography establishes its paper connection; abstract-level group results do not assign every experimental result to TARC 38.

The YAML makes no soybean-nodulation mechanism, nitrogen-fixation, antibiotic-resistance or causal-graph claim. Near-strain literature leads mentioning TARC 64 or USDA 38 were not transferred to TARC 38. Geographic, serological and antibiotic details appearing only in search excerpts remain unverified here.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 103738, TARC 38 with optional separators, and the target slug. Identity and matched fields of all 112 matching lines were inspected. The own native name row, four LPSN candidate rows, two culture-collection rows and four ATB link rows were read in full.

The culture/source-number matches belong to other concepts:

- BacDive 103738 is Rhodococcus sp. ST002176, NCBITaxon:194249; its record number is not this taxon ID.
- CIP 103738 and BacDive 146145 belong to Bartonella vinsonii / subsp. vinsonii, NCBITaxon:33047/110577. Relevant LPSN names include Bartonella vinsonii, its nominal subspecies and the Rochalimaea synonym; relevant genomes include GCA/GCF_902825235.1 and BV-BRC 110577.3. Their StrainInfo record is SI-ID51909, not a TARC 38 link.
- DSM 103738 and BacDive 160556 belong to Palleniella intestinalis, NCBITaxon:2736291, also represented by older Prevotella source wording. Its StrainInfo record is SI-ID399379. The three ATB genome links and one strain link inspected in full use this BacDive ID and BioSample SAMN14906829, with explicit DSM 103738 evidence for GCA_013166595.1, BV-BRC 2736291.3 and IMG 2921969536. They do not support TARC 38.
- Additional numeric hits are unrelated assembly statistics, Pseudomonas assembly name ASM103738v1, Salmonella designations 103738/PNUSAS103738, Lachnospiraceae MGBC103738, an uncultured MarMAG_103738, a Campylobacter isolate code, or Klebsiella component CP103738. Names and source identity fields exclude the target.

A follow-up ignored/compressed-inclusive search for D85403 over the same roots returned two ATB catalog rows. Both were read in full: Escherichia coli sample SAMEA9334196 and Citrobacter rodentium sample SAMN31039852 contain the accession substring only inside SeqKit sums. These are not marker links.

Five SOURCE.json files were separately parsed; the broad numeric match was the BacDive 103738 request metadata already distinguished above. Gitignore-independent filename enumeration found only this target YAML and no prior matching report. History filename inspection found no target-specific filename. These are bounded repository checks, not global absence claims.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. No direct backbone child supplies descendant inventory. Zero correctly counts inventoried BacDive strains, not the existence of this named isolate or its marker. No supported target culture-deposit/genome chain was established.

Optional definitions, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable to the taxonomy-only record; the marker's bibliography does not create an expression-module assertion. No adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, provenance, source-count semantics and seeded status are supported. Unavailable primary full texts and skipped corpus checks remain limitations.

## Recommended Edits

None required. Preserve the authority label/rank, unclassified Bradyrhizobium placement and zero BacDive count. Do not turn a short marker into a genome, import CIP/DSM 103738 from unrelated taxa, or infer strain equivalence from a shared sequence segment.

Future authorized corrections belong in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect requires a change here; generated YAML must not be hand-edited.

## Follow-up Checks

Any future phenotype enrichment requires the original experiment and a precise target-specific assignment. New deposit/genome links require explicit source-supported identity chains and full culture accessions. Preserve supplied accession versions and source provenance.

After an authorized source refresh, rerun schema/strict/history validation and documented full-corpus reproduction/QC gates. Focused matching does not replace those checks.

## Additional Notes

- YAML SHA-256: `13715a1a3022874f64f669563ea25ec7e00072a23a134f79c1a142f2f531aa62`.
- `data/taxa/PATHS.tsv:15286` and `curation/seed_scope.tsv:144198` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and its exact one-source reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
