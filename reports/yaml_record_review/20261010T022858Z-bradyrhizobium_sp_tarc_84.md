# YAML Record Review: Bradyrhizobium sp. TARC 84

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bradyrhizobium_sp_tarc_84.yaml`
- Started UTC: 2026-10-10T02:26:29Z
- Finished UTC: 2026-10-10T02:28:58Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:103740` denotes Bradyrhizobium sp. TARC 84, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2631580`, genetic code 11, grounding `EXACT`, mapping status `SEEDED`.

It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. This is TARC 84, not the separately indexed TARC 64. No nomenclature, cultured deposit, genome, physiological trait or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bradyrhizobium_sp_tarc_84.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bradyrhizobium_sp_tarc_84.yaml --out /private/tmp/taxonmech-bradyrhizobium-tarc84-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, complete lineage, code, empty synonyms, own source inventories, unique index/scope resolution, attestation and exact seed reason. Complete backbone scanning found no immediate child. Own type-material, merged-ID and dropped-record inventories had no rows.
- The native NCBI name row, all relevant TSV candidate rows and the two ambiguous GOLD project/analysis rows were read completely. Other native search candidates were inspected for identity and every matching field. Live taxonomy and the single exact-taxonomy nucleotide record were inspected, including complete annotations and sequence length/alphabet/hash checks.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, source replay, rendering and publication gates. The graph ID/label gate `just validate-products` is inapplicable without a graph. Focused checks do not establish corpus reproduction.
- NCBI browser and DOI landing pages failed through the web reader. EFetch/Datasets and the full PubMed abstract/bibliographic response were available. The cited article's full text was not read; no independent phylogenetic or experimental reanalysis was performed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18566`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103740&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103740) agree on the exact label, species rank and lineage; EFetch confirms parent 2631580 and code 11.

All stored ancestor IDs, labels and ranks agree with the backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Nitrobacteraceae, Bradyrhizobium and unclassified Bradyrhizobium. EFetch confirms the chain below root and Datasets includes root 1. Retain the unclassified `NO_RANK` parent rather than replacing it with the genus.

The complete native name row `data/catalog/ncbi_names-0000.jsonl.gz:38625` is a scientific name with an empty unique-name qualifier. EFetch supplies no alternate names. This informal strain-labelled NCBI species is not automatically a validly published ICNP species name or a synonym of B. japonicum or B. elkanii.

`EXACT` describes identifier grounding. The attestation correctly records one NAME from the 2026-09-13 NCBI snapshot, not a count of independent experiments or public culture deposits.

## Evidence

The live query `txid103740[Organism:exp]` returned one nucleotide record: [D85405.1](https://www.ncbi.nlm.nih.gov/nuccore/D85405.1), a 264-base partial 16S ribosomal RNA sequence. Its source explicitly identifies TARC 84 and taxon 103740. Declared and actual lengths agree, with an A/C/G/T alphabet. The rRNA feature has a non-experimental inference qualifier. No host or location qualifier is present in the inspected source block.

The record cites [PMID:10528395](https://pubmed.ncbi.nlm.nih.gov/10528395/), DOI `10.1139/w99-061`, verified through PubMed, and a 1996 direct submission. The 1999 paper's abstract describes Thai soybean-nodulating Bradyrhizobium isolates compared with USDA strains using nifDK RFLP and partial 16S sequences. It reports shared partial-marker sequences among some isolates and USDA strains, alongside genetic distinctions. The abstract does not name TARC 84; do not turn study-level context into a strain-specific trait, host-range claim or formal species reassignment.

D85405.1 is not a genome and does not supply a public culture-deposit accession. The Datasets taxonomy response omits an assembly-count field; that omission is not an explicit zero-assembly result. No functional nodulation-gene evidence from another TARC isolate is transferred to this record.

The current YAML makes no unsupported mechanistic claim and contains no citation that misrepresents the inspected literature. The marker and paper are bounded review context rather than missing required YAML fields.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded taxon ID, label, slug and TARC 84 variants. The initial search returned 48 lines.

Identity and matched-field inspection excluded unrelated numerical collisions: BacDive 103740 is Rhodococcus ST002182; DSM 103740 belongs to Sphingomonas D2_1; CIP 103740 belongs to E. coli B-96. CP103740, MGBC103740, other numbered strain labels and assembly statistics are not TARC 84 identity evidence. A StrainInfo KY103740 hit concerns Kluyveromyces lactis; no Eukaryota YAML was opened.

The full GOLD rows `Gp0791991` and `Ga0635413` describe NPDC103740_432_B10. They provide no organism identifier or GenBank accession connecting that culture to TARC 84; a shared numeric substring is insufficient for a join. Their unresolved biological identity is not resolved by guessing.

All six ATB candidate rows were read in full. The initial match at `data/catalog/allthebacteria.tsv.xz:2646741` is Klebsiella pneumoniae sample SAMN36519382, assembly ERZ26533620. Five follow-up D85405 hits are checksum substrings in rows for Mycobacterium tuberculosis, Staphylococcus pseudintermedius, Salmonella, Enterococcus faecium and Legionella pneumophila. None is an accession link to this marker or a supported TARC 84 genome.

Complete structured scans found no own-taxonomy BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. Five independently enumerated SOURCE.json files were parsed; the metadata hit for requested BacDive 103740 refers to the unrelated Rhodococcus record. Ignored-independent filename enumeration found exactly one target YAML and no prior target report; history filenames had no target-specific match.

These searches establish bounded repository coverage, not global absence of biological evidence. `strain_count: 0` measures inventory coverage, not absence of the TARC 84 isolate. Empty optional synonyms, nomenclature, mappings, deposits, definitions and graphs are appropriate. iModulonDB is not applicable to the taxonomy/name assertions or partial ribosomal marker here.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertion scope. The record preserves its own NCBI identity and complete lineage without importing adjacent-isolate evidence or unrelated numerical matches.

## Recommended Edits

None required. Leave the generated YAML, seed status and curation history unchanged.

Any separately authorized enrichment belongs in maintained source inventories or a supported extraction/harmonization extension before regeneration. Do not hand-add a marker as a genome, treat a number shared across namespaces as identity, or merge TARC isolates on partial-sequence similarity.

## Follow-up Checks

For future host, phenotype or mechanism enrichment, inspect the primary paper's full strain-level evidence and resolve the exact accession/strain chain. Keep TARC 84 evidence distinct from other TARC and USDA isolates and preserve the sequence version.

After maintained inputs change, rerun the documented canary, schema/strict/history checks and full-corpus reproduction/QC gates. No correction is required merely to retain this supported NCBI-only record.

## Additional Notes

- YAML SHA-256: `ff64593df694e6dd6c52bb6735e9168c66790841fc1b01549082ca98c9e073a9`.
- `data/taxa/PATHS.tsv:15293` and `curation/seed_scope.tsv:144200` uniquely resolve the target. The seed event retains 2026-09-13T17:54:04Z and its exact single-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No tracked record, source input, schema, history, page, branch, worktree or GitHub state changed. No review status was promoted.
