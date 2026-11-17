# YAML Record Review: Pseudoalteromonas sp. 1-Cc-11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_1_cc_11.yaml`
- Started UTC: 2026-10-07T09:42:58Z
- Finished UTC: 2026-10-07T09:46:08Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035760`, Pseudoalteromonas sp. 1-Cc-11, `SPECIES`, `BACTERIA`, parent `NCBITaxon:194690` (unclassified Pseudoalteromonas), ten root-first ancestors, code 11, `EXACT`, `SEEDED` and `strain_count: 0`. One NCBI name attestation and one seed event are present.

There are no synonyms, nomenclature, taxonomy mappings, deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graph assertions. The strain-like label identifies a species-rank NCBI concept, not a formal species name or culture-collection deposit. Generated YAML is read-only; maintained extraction inputs and `src/taxonmech/seed.py` own future source/harmonization changes, and `curation/seed_scope.tsv` plus `data/taxa/PATHS.tsv` own scope and slug decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoalteromonas_sp_1_cc_11.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_1_cc_11.yaml --out /private/tmp/pseudoCc11-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/pseudoCc11-strict.tsv` | Actual TSV inspected; header only. |
| Structured backbone, full lineage, seven inventories, scope/path and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI EFetch and Datasets | Identity, rank, parent, code and ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1; complete marker metadata inspected. |
| Primary publication and thesis abstract | Exact strain designation inspected; source scope distinguished from taxonomic identity. |
| Entire target reread | Byte-identical to initial read. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove corpus reproduction.

`just validate-products` was not run because no curator-added graph nodes are present and configured OAK targets exclude NCBI taxonomy. No YAML citation/internal evidence references require separate checking. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact within the scope below.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222164` agrees on ID, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31648` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14664` and `curation/seed_scope.tsv:322430`.

All ancestor IDs, labels, ranks and ordering agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Pseudoalteromonadaceae, Pseudoalteromonas and unclassified Pseudoalteromonas. Live taxonomy EFetch confirms the non-root chain, species rank, parent 194690, code 11 and no alternate names; Datasets also includes root. The inspected lifecycle inventories contain no target retirement, merge or type-material entry. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035760&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035760)

The paper's species-affiliation wording, discussed below, is not authority to rewrite this carried NCBI label/lineage. No inspected NCBI source supplies P. citrea as this target's synonym. `EXACT` means exact NCBI grounding, not an inferred species identification.

## Evidence

The sole `NCBITAXON` attestation matches ID, label, count 1, unit `NAME` and snapshot note. It counts a source name, not deposits or genomes. Full backbone scanning found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nucleotide search returned UID 333974686, `JF502829.1`: a 1,203-nt partial 16S rRNA record, partial at both ends, with strain 1-Cc-11 and `taxon:1035760`. Source qualifiers give host Clathrina clathrus, France, November 2007, collectors/identifiers M. Roue and I. Domart-Coulon, and primers 27F/1385R. Submission was 5 March 2011; creation 30 May and update 3 June 2011. All metadata were read except sequence/translation/transcription payloads. They provide no culture-collection, assembly, BioSample, BioProject, DOI or PMID link. [GenBank JF502829.1](https://www.ncbi.nlm.nih.gov/nuccore/JF502829.1)

GenBank lists an unpublished glycerolipid study by Roue, Domart-Coulon, Jovet and Bourguet-Kondracki, plus the direct submission. That title alone is not experimental evidence.

The 2014 article DOI `10.6119/JMST-013-0718-2` explicitly studies Pseudoalteromonas 1-Cc-11. Its identity/title page and relevant complete printed pages 39-40 and 44-47 were inspected, with rendered checks of the species-affiliation text and Figures 8-9/captions. It reports monopalmitin and monostearin from this strain's cultures, while warning that their occurrence in the host does not establish an exclusive bacterial origin. The affiliation section describes partial-16S similarity to both P. citrea and P. aurantia reference strains. Thus the paper's P. citrea wording is not a basis for a new exact synonym or deposit association. Its other isolated compounds did not explain the reported antimicrobial activities. The chemical and ecological conclusions remain bounded to the experiments; neither host-wide metabolism nor genus-wide activity follows. [Primary article](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17-06/010070108.pdf)

The PDF's extracted text contains 1-Cc-11 but not JF502829. Association of the paper with this record is an inference supported by the exact designation, genus, host and overlapping authorship, not an explicit accession cross-citation. A 2011 Roue thesis abstract independently names this isolate and discusses its chemical investigation and a possible feeding relationship. Only the official thesis metadata and abstract were inspected, not the full thesis. [Thesis 2011PA066107](https://theses.fr/2011PA066107?domaine=theses)

All local source candidates were read fully before exclusion:

| Source address | Actual identity and reason for exclusion |
| --- | --- |
| `data/catalog/gtdb_genomes-0017.jsonl.gz:49693` | GB_GCA_038828535.1, Nitrososphaerota archaeon, taxid 2026795, isolate GXS_202007_bins_58, SAMN36039018. The matched number 1035760 is genome length, not taxonomy. |
| `data/catalog/ncbi_genbank-0035.jsonl.gz:47050` | GCA_038828535.1 for that same archaeal metagenome-derived assembly; same numerical length match. |
| `data/catalog/allthebacteria.tsv.xz:546916` | Staphylococcus aureus, SAMEA3322970, ERR1035760, ERZ3253641. The digits occur in a run accession. |
| `data/catalog/ncbi_genbank-0000.jsonl.gz:31253` | Capnocytophaga canimorsus Cc11, taxid 28188, GCA_000827575.1, SAMEA3180108. Cc11 is not 1-Cc-11. |
| `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:7716` | Its suppressed GCF_000827575.1 counterpart, same unrelated strain and taxid. |

The broad designation pattern matched `.1_Cc11` in assembly FTP paths. These are substring matches, not biological joins.

The seed event agrees with the scope reason and NCBI-only source list. `src/taxonmech/seed.py:_seed_timestamp` selects the newest manifest extraction time. Raw, ATB and StrainInfo timestamps are respectively 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z; the record correctly uses 17:54:04Z without asserting a target ATB link.

iModulonDB is not applicable: no regulator, gene function, expression module or transcriptomics claim is asserted. A taxonomic 16S record and chemical-isolation study do not require an expression-module lookup.

## Completeness

No consequential gap was found. `strain_count: 0` counts BacDive records classified in this subtree, not all laboratory strains. The marker is not a genome, and the isolate designation is not a registered deposit. The exact-taxid Assembly search returned zero with a phrase-not-found warning; this cannot rule out assemblies under another classification.

Both local search stages included ignored/hidden files and compressed catalogs using `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed at each stage, and history filenames were independently traversed.

The initial whole-digit taxid and label/slug search returned six rows: three target rows, two archaeal length matches and one unrelated ATB run. The expanded JF502829 with optional .1 and bare 1-Cc-11 separator/case variants returned five rows: the same three target rows and two Capnocytophaga assembly rows. All were read. No marker-accession hit, matching metadata value or target history filename was found in this bounded search, including ignored files.

Web searches used exact label/accession, designation/author and genome/culture-collection terms. They supplied the primary article and thesis abstract, not a verified deposit or assembly. Optional record-level literature is not required for seeded provenance. Habitat, growth medium and phenotype curation belong to the relevant sibling repositories; this review does not authorize cross-repository writes. Exhaustive literature retrieval, full-thesis review, independent chemistry and phylogenetic reanalysis were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML within the inspected scope. The taxonomic/source assertions are supported; absence of optional biological enrichment is not a defect.

## Recommended Edits

None required. Preserve the NCBI label and lineage, `SEEDED` status and distinct meaning of marker, genome and deposit identifiers. Do not import the unrelated numerical/substring matches or infer species equivalence from the paper's affiliation terminology.

Optional literature enrichment would need an authorized persistent curation mechanism or seeder change with tests, not a hand edit to the generated YAML. Any later biological curation must retain experimental and taxonomic uncertainty.

## Follow-up Checks

During a controlled source refresh, repeat NCBI identity/lineage and exact-taxid Assembly/nuccore queries and compare inventories. Accept a new strain/genome association only with explicit own-deposit or accession-chain evidence.

For changed maintained inputs, run `just seed`, an authorized `just seed-canary NCBITaxon:1035760`, inspect the entire output, repeat focused schema/strict validation and run `just verify-corpus` plus `just qc`. These are future curation checks, not operations performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The full target was reread and remained byte-identical. This new timestamped report is the only repository write for this record review. Validation TSV and PDF artifacts are temporary. No YAML, inventory, old report, status/history, generated page, worktree or GitHub item was changed.
