# YAML Record Review: Agarivorans sp. 1-Cc-9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/agarivorans_sp_1_cc_9.yaml`
- Started UTC: 2026-10-07T09:35:29Z
- Finished UTC: 2026-10-07T09:40:27Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035759`, Agarivorans sp. 1-Cc-9, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2636026` (unclassified Agarivorans), ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and `strain_count: 0`. One NCBI name attestation and one embedded seed event are present.

No synonyms, nomenclature, mappings, deposits, genomes, definition, literature evidence, discussions, replacement or causal graph are asserted. This NCBI species-rank concept has a laboratory strain-like label; it does not assert a registered deposit or a formally named species. Generated YAML is read-only. Maintained extraction inputs and `src/taxonmech/seed.py` own future source/harmonization changes; `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` own scope and slug decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/agarivorans_sp_1_cc_9.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/agarivorans_sp_1_cc_9.yaml --out /private/tmp/agarivorans9-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/agarivorans9-strict.tsv` | Actual TSV inspected; header only. |
| Structured backbone, full lineage, seven inventories, scope/path and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI EFetch and Datasets | Identity and all ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1; complete marker metadata read. |
| Related primary paper | Relevant complete pages read; Figure 8 and its caption visually inspected. Attribution is to another strain. |
| Entire target reread | Byte-identical to the initial read. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons are not substitutes for these gates.

`just validate-products` was not run: no curator-added graph nodes are present, and configured OAK targets exclude NCBI taxonomy. No YAML literature/internal evidence references require a separate citation check. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact within the bounded scope below.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222163` agrees on ID, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete native row at `data/catalog/ncbi_names-0005.jsonl.gz:31647` identifies the exact scientific name. Unique path and scope rows are `data/taxa/PATHS.tsv:14663` and `curation/seed_scope.tsv:322429`.

Every ancestor's ID, label, rank and order agrees: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Alteromonadaceae, Agarivorans and unclassified Agarivorans. Live taxonomy EFetch confirms species rank, parent 2636026, code 11, no alternate names and all non-root ancestors; Datasets includes root. The inspected lifecycle sources contain no target type-material, merged or dropped row. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035759&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035759)

The unclassified parent is a carried NCBI node, not a missing species assignment. `EXACT` means agreement with the NCBI concept, not nomenclatural validity. Preserve case, hyphens and the pinned lowercase filename. Neighboring isolate 1-Cc-12 is a distinct taxon, not a synonym.

## Evidence

The sole `NCBITAXON` attestation matches the identifier, label, count 1, unit `NAME` and snapshot note. It counts a source name, not genomes or deposits. Full backbone scanning found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore search returned UID 333974690, accession `JF502833.1`: a 1,352-nt partial 16S rRNA record, with strain 1-Cc-9 and explicit `taxon:1035759`. Source qualifiers give host Clathrina clathrus, France, November 2007, collectors/identifiers M. Roue and I. Domart-Coulon, and primers 27F/1385R. Submission was 6 March 2011; creation 30 May and update 3 June 2011. All metadata were read, excluding only nucleotide/translation/transcription payloads. No culture-collection, assembly, BioSample, BioProject, DOI or PMID link is supplied in these metadata. [GenBank JF502833.1](https://www.ncbi.nlm.nih.gov/nuccore/JF502833.1)

GenBank's unpublished reference by Roue, Domart-Coulon, Jovet and Bourguet-Kondracki concerns glycerolipids from C. clathrus and Pseudoalteromonas-associated bacteria. This submission context does not show production by Agarivorans 1-Cc-9. Host metadata do not establish persistent symbiosis, a deposit or a phenotype.

A related primary article, DOI `10.6119/JMST-013-0718-2`, was inspected from the authors' institutional repository. The title page verifies the 2014 article identity. Complete printed pages 40, 45 and 46 were read; Figure 8 and its caption were visually checked in a rendered page. The methods, culture results and caption attribute glycerolipid production to Pseudoalteromonas strain 1-Cc-11, not this target. Exact case-insensitive searches of all 14 pages' extracted text found no JF502833, 1-Cc-9 or Agarivorans. This is a bounded attribution check, not an exhaustive supplement/literature review or independent chemistry assessment. Do not transfer activity based on a shared host or adjacent numbering. [Primary paper, pp. 40, 45-46](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17-06/010070108.pdf)

All local candidate rows were read fully before exclusion:

| Source address | Actual identity and reason for exclusion |
| --- | --- |
| `data/gold/organisms.jsonl.gz:243118` | Go0314453, Salmonella enterica enterica sv. Typhi strain 1035759, taxid 90370. |
| `data/gold/projects.jsonl.gz:104271` | Gp0162928, same Salmonella organism, SAMEA1969886 and PRJEB3215. |
| `data/gold/analyses.jsonl.gz:86714` | Ga0142587, project Gp0162928, GCA_001358575.1 and CFAW00000000, same strain. |
| `data/catalog/gtdb_genomes-0016.jsonl.gz:10541` | GB_GCA_001358575.1, Salmonella enterica, nonrepresentative, taxid 90370 and strain 1035759. |
| `data/bvbrc/bvbrc-0027.jsonl.gz:47416` | 90370.1121, GCF_001358575.1, same Salmonella sample/project and lineage. |
| `data/catalog/ncbi_genbank-0001.jsonl.gz:1506` | Current GCA_001358575.1, same Salmonella taxid/strain/sample. |
| `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:10835` | GCF_001358575.1, same non-target taxid/strain/sample, suppressed 2021-01-18. |
| `data/catalog/allthebacteria.tsv.xz:546914` | Staphylococcus aureus, SAMEA3322968, ERR1035759, ERZ3253640. Digits occur in a run accession, not target taxonomy. |

The seven Salmonella rows consistently describe a strain whose designation happens to equal this target's taxid digits. Their accession chain is not an Agarivorans association.

The seed event's scope reason and NCBI-only attestation agree. Its 2026-09-13T17:54:04Z timestamp is the latest extracted-at value among raw, ATB and StrainInfo manifests, as `src/taxonmech/seed.py:_seed_timestamp` specifies; it does not imply an ATB association for every taxon. The manifests give raw 17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z that day.

iModulonDB is not applicable: neither this YAML nor its taxonomic 16S provenance asserts a regulator, pathway, stress response, functional trait or expression module. Findings about another strain do not create a target claim.

## Completeness

No consequential gap was found. `strain_count: 0` counts BacDive source entries in this source scope, not all named laboratory strains. A partial marker is not a genome, and a laboratory designation is not a verified deposit. Empty optional fields are appropriate. The exact-taxid Assembly search returned zero with a phrase-not-found warning; it does not prove that no assembly exists under another classification.

Both search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed at both stages; history filenames were independently traversed.

The initial complete-digit taxid/label/slug search returned 11 rows: three target rows, seven Salmonella rows and one Staphylococcus row. The expanded JF502833 with optional .1 and bare 1-Cc-9 separator/case variant search returned only the same three target rows. Every matched row was inspected. No marker-accession hit, matching metadata value or target history filename was found in these searches. All negative statements are limited to those roots and terms and include ignored files.

Web searches used the exact label, accession and glycerolipid/designation terms. No additional target-specific primary publication was verified. Exhaustive literature retrieval, sequence similarity/phylogenetic reanalysis and the related paper's other figures/supplements were not checked.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML within the inspected scope. Identity, lineage, attestation, zero BacDive strain count and seed event agree. Sparse optional enrichment is not a curation defect.

## Recommended Edits

None required. Do not merge adjacent isolate labels, infer a formally named species, count JF502833.1 as a genome, create a deposit from the laboratory designation, import unrelated numerical matches, transfer Pseudoalteromonas compound findings or promote `SEEDED` to `REVIEWED`.

Future exact-strain evidence should enter through maintained source extraction/overlay inputs and the normal seeder workflow, not hand edits to generated YAML or pages.

## Follow-up Checks

On a controlled source refresh, repeat exact NCBI identity/lineage and Assembly/nuccore queries and compare updated inventories. Additional associations must explicitly identify 1-Cc-9 or a verified accession/deposit chain; shared hosts, neighboring labels and bare numerical matches are insufficient.

If maintained inputs change, use `just seed`, an authorized `just seed-canary NCBITaxon:1035759`, full emitted-file inspection, focused schema/strict validation, `just verify-corpus` and `just qc`. These are future curation checks, not regeneration performed by this review.

## Additional Notes

Reviewed on branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The complete YAML was reread and remained byte-identical. This new timestamped report is the only repository write for this review. Strict output and paper artifacts are temporary files. No source record, inventory, old report, status, history, generated page, worktree or GitHub item was changed.
