# YAML Record Review: uncultured gamma proteobacterium TIHP368-33

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_33.yaml`
- Started UTC: 2026-10-04T05:12:35Z
- Finished UTC: 2026-10-04T05:13:20Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103307`, uncultured gamma proteobacterium TIHP368-33. It carries species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. NCBITAXON is the sole attestation, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_33.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_33.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18416`, name-catalog shard 0000 row 38434, PATHS row 13355 and scope row 144076 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103307&retmode=xml)

The full clone designation is retained without extra synonyms, a formal binomial, cultivation or type-material claims. Source species rank supports inclusion without implying nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869742. Its inspected qualifiers identify AB031648.1, a 748 bp partial 16S rRNA sequence, with taxon:103307, clone TIHP368-33, environmental_sample and coastal marine sediment. This directly resolved marker is not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031648.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML supply a DOI/PMID. Study context is not clone-specific phenotype evidence.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103307, TIHP368-33/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 32 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned, yielding two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103307 concerns Lactobacillus kefiranofaciens subsp. kefiranofaciens WT-2B, BacDive 6622, strain taxid 1423827, subspecies 190905 and species 267818. LPSN 777331/777332, GOLD organism Go0279589 and NCBI type-material rows concern that culture. SI-ID 3321 owns deposit 152138; the strain has subspecies context, while the inspected own-deposit taxon field is absent. These scopes were retained without filling that gap from another source.

AJ575259 is a marker in the unrelated LPSN culture context. StrainInfo related records FR775933 and FR775946 describe partial pheS and rpoA genes from CIP 103307T. These are not TIHP368-33 sequences, genome assemblies or evidence for this clone's functional traits. Type material, nomenclature and publication references attached to that Lactobacillus culture remain excluded.

Other excluded matches include BacDive 103307, Agromyces sp. ST027927/51513; CP103307 in Pseudomonas aeruginosa PLL01/287, GCA_024760445.1; uncultured bacterium MGBC103307/GCA_948659785.1; Salmonella enterica PNUSAS103307/GCA_008824685.1; Pseudomonas aeruginosa PSA-BAB-IMI-103307/GCA_023905105.1; and Shigella flexneri PNUSAE103307/GCA_024110655.1. ATB DRR103307 belongs to E. coli sample SAMD00077715; a Mycobacterium SeqKit-checksum substring is unrelated. Source-specific labels and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion is present in the target. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031648.1 only as directly sourced marker evidence. Do not infer neighboring accessions or transfer culture, genome, nomenclature or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103307 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence source qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
