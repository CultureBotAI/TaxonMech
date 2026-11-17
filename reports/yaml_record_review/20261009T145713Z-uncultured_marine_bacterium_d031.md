# YAML Record Review: uncultured marine bacterium D031

- Repository: TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d031.yaml`
- Started UTC: 2026-10-09T14:53:15Z
- Finished UTC: 2026-10-09T14:57:13Z
- Verdict: pass

## Target

Reviewed the entire generated `TaxonRecord` for `NCBITaxon:103678`, uncultured marine bacterium D031. It is a bacterial species-rank environmental taxonomy node, not a named cultured species or culture-collection deposit. The record has `grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11, zero inventoried strains, one NCBITAXON NAME attestation, and one inline seed event.

HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Target SHA-256: `6be627d9eae8d77fc8bc8a43086aec6d7174072bfa4999fe6f5de9bf9bedc496`.

## Validation

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d031.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d031.yaml --workers 1 --out /private/tmp/taxonmech-d031-20261009-validation.tsv
```

Both commands exited 0. Open validation reported no issues; strict validation scanned one file with zero errors. Its TSV was read and contains only the header.

Read-only structured comparisons confirmed the full root-first lineage, target identity fields, NCBI attestation, unique PATHS/scope rows, and inline event's exact scope reason. Complete type-material, merged-ID, dropped-record, and child-row scans found no own entries. These checks are not a replacement for full-corpus reproduction.

Not run: full-corpus `verify-corpus`, provenance, render/docs, test-suite, and `qc` gates. The OAK `validate-products` configuration covers causal-graph groundings, which this record does not contain; it does not validate ordinary NCBI identity. No target external history file was found in the ignored-inclusive bounded searches, so no separate history instance was validated. Review-only work must not create such an event or promote the record status.

## Identity and Grounding

The complete native backbone row `data/raw/ncbitaxon_taxa.tsv:18543` and scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38559` agree on ID 103678, label, species rank, parent 150608, genetic code 11, and no synonyms. Fresh NCBI EFetch XML confirms those fields. NCBI Datasets independently supplies the same label/rank and all five ancestor IDs, including root. Sources: [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103678&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103678).

The exact lineage is root (1), cellular organisms (131567), Bacteria (2), environmental samples (48479), and marine bacteria D ensemble (150608). Ranks match, including CELLULAR_ROOT and the two NO_RANK environmental groupings. Sparse environmental placement is the authoritative NCBI chain, not a missing inferred phylum/genus. SPECIES and EXACT describe taxonomy rank and grounding; neither asserts valid nomenclatural publication or a cultured biological species.

## Evidence

The sole attestation is exactly the native row's NCBITAXON source, own identifier and label, count 1, unit NAME, and snapshot 2026-09-13. Empty BacDive inventory support justifies `strain_count: 0`; it is not a universal statement that no D031-related biological material exists.

A fresh exact-taxonomy Nuccore query, `txid103678[Organism:noexp]`, returned one sequence, UID 5882280, accession AF177565.1. The complete GenBank record confirms clone D031, taxonomy cross-reference 103678, environmental-sample status, a surface-associated uncultured marine source, and a partial 16S rRNA gene. The sequence has 584 actual bases, matching its declared length; the alphabet includes the deposited ambiguity code S. Its sequence SHA-256 is `af4ded6bc777bfceb1776662e8b733df58250405856f80a23f4f4202e7f17b51`. Source: [AF177565 GenBank record](https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AF177565&db=nuccore&report=genbank&retmode=text).

The sequence cites Dang and Lovell's 2000 study, PMID 10653705, DOI 10.1128/AEM.66.2.467-475.2000. PubMed's complete abstract and the paper's clone-specific results were inspected. The paper explicitly groups D031 with D029 in the gamma-proteobacterial Alteromonas group, and reports D031 among clones recovered during early surface colonization but no longer recovered after 72 hours. This is experimental clone-library context, not a species-wide growth, metabolic, or survival claim. The paper's predominant Roseobacter finding concerns other clones and must not be assigned to D031. Sources: [PubMed record](https://pubmed.ncbi.nlm.nih.gov/10653705/), [primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC91850/).

The marker is neither an assembly nor a culture deposit. Its discovery does not authorize inventing a strain container to hold a `related_records` link. No record field claims a phenotype or mechanism requiring this paper to be embedded. The NCBI-only YAML does not miscite or overstate the study.

## Completeness

Before judging omissions, ignored-inclusive compressed searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Searches covered the taxon number, full label/slug variants, bounded D031 token, and then AF177565/5882280. All 48 initial candidates and five expanded-search candidates were read in full; the five SOURCE metadata documents were also parsed. Filename inventory included ignored files under `data/taxa`, `reports/yaml_record_review`, and `history`.

Only the own NCBI backbone/name and scope entries support this target. Cross-source numeric collisions were distinguished by native identifiers: BacDive 103678 denotes Rhodococcus ST000651; CIP 103678 denotes Aeromonas; DSM 103678 denotes Streptococcus azizii; NBRC 103678 denotes Actinoallomurus caesius; StrainInfo deposit 103678 denotes Mycobacterium xenopi. KY103678 is a fungal marker, CP103678 a Klebsiella sequence, and DRR103678 an unrelated ATB run. GTDB hits include unrelated assembly statistics and MGBC103678; none supplies a D031 genome. Expanded UID hits were unrelated accession/sample/size substrings, not AF177565 crosswalks. Inspecting a fungal collision was disambiguation only, not a new Eukaryota record review.

Complete structured scans of the BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin, and BactoTraits inventory tables found no row mapped to this exact NCBI identifier. Consequently no missing supported nomenclature, type strain, cross-source mapping, medium, trait, or genome assertion was identified within these checked inputs. No assertion is made about all undiscovered external data.

`data/taxa/PATHS.tsv:15147` uniquely resolves the target slug. `curation/seed_scope.tsv:144187` includes this species-rank node through the one-source attestation rule. The seed event at 2026-09-13T17:54:04Z reproduces that reason exactly. Ignored-inclusive searches in `conf`, `curation`, `history`, `src`, and `tests` found no own corrective overlay or history entry; longer neighboring taxon IDs were not treated as matches.

iModulonDB is not applicable: this record names no regulatory gene, protein, functional trait, or transcriptomic dataset, and its discovered marker is a taxonomic 16S fragment rather than expression-module evidence. No functional inference was made from absent optional fields.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The YAML faithfully represents its scoped NCBI evidence and does not overstate the independently inspected environmental-clone literature.

## Recommended Edits

None required. Do not hand-edit the generated record, add a cultured strain, substitute an inferred lineage, or promote SEEDED status as a result of this review.

An optional future taxon-level marker/literature enrichment would require an authorized maintained schema/import/seeder design with source provenance; it should not be implemented by placing AF177565 in a fabricated BacDive strain. Scope changes belong in `curation/seed_scope.tsv`; primary taxonomy changes belong in the maintained NCBI inventory import and pin.

## Follow-up Checks

- After an authorized taxonomy refresh, recheck the full ID/label/parent chain and rerun the two focused validators above.
- If marker enrichment is commissioned, retain clone D031, AF177565.1, its exact taxonomy reference, and the paper's clone-specific limits; distinguish marker sequences from genome assemblies.
- Run full provenance, corpus-reproduction, and publication gates after any authorized source/generator change. They were not run for this read-only review.

## Additional Notes

The web-reader taxonomy page and PMC article initially returned unavailable/browser-challenge responses; NCBI XML/Datasets and a direct read of the correct PMC article supplied the evidence. A Europe PMC full-text XML request returned HTTP 500; the successful direct HTML read recovered the clone-specific results. General web-search near misses were not evidence.

All source/record files, status, external history, and existing worktrees were left unchanged. Only this independent report was added. Eukaryota remains excluded from new record reviews.
