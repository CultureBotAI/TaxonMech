# YAML Record Review: uncultured gamma proteobacterium TIHP368-20a

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_20a.yaml`
- Started UTC: 2026-10-04T04:58:20Z
- Finished UTC: 2026-10-04T04:59:04Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` denotes `NCBITaxon:103300`, uncultured gamma proteobacterium TIHP368-20a. It carries species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. The sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Maintained owners for future corrections are source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_20a.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_20a.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text; they do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18409`, name-catalog shard 0000 row 38427, PATHS row 13346 and scope row 144069 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria, not a named genus. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103300&retmode=xml)

The full clone suffix is significant. No synonym, formal binomial, cultivation or type-material claim is asserted. Source species rank supports inclusion without implying nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869733. Its inspected source qualifiers identify AB031639.1, a 501 bp partial 16S rRNA sequence, taxon:103300, clone TIHP368-20a, environmental_sample and coastal marine sediment. This directly resolved accession is marker evidence, not a genome assembly or deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031639.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. No DOI/PMID appears in these entries or the YAML. Study context does not establish clone-specific functional traits.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result is not universal proof that no genome exists.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional slots are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103300, TIHP368-20a/underscore spelling and the full stem in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 52 matched lines and structured contexts were inspected. SOURCE.json was separately scanned, yielding two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103300 belongs to Pseudoalteromonas piscicida MB-1, BacDive 139570, strain taxid 1279016/species 43662, LPSN 784703 and SI-ID 36250's own deposit 142634. Its type material, publication and AB681918 marker evidence do not support this clone. DSM 103300 is Serratia fonticola H1n/47917, BacDive 131925 and SI-ID 405089's own deposit 912276. These two culture accessions are not interchangeable with each other or with taxon 103300.

Further excluded matches include BacDive 103300, Agromyces sp. STI07746/51513; SI-DP 103300, Salmonella enterica subsp. enterica ATCC 23854 in SI-ID 38266; Dactylosporangium sp. NAICONS 103300/3419230; KY103300 in Brettanomyces anomalus SI-ID 180639; and Wenling zhaovirus-like virus 1 WLJQ103300/1923551 GOLD records. CP103300 concerns Endozoicomonas euniceicola EF212/taxid 1234143, GCA_025562755.1.

Genome collisions include Lactiplantibacillus plantarum SRCM103300/GCA/GCF_004141875.1, uncultured Alphaproteobacteria bacterium MGBC103300/GCA_948691835.1, Shigella flexneri PNUSAE103300/GCA_023758405.1, Listeria monocytogenes FLAG-103300/GCA_050884985.1 and uncultured bacterium MarMAG_103300/GCA_977587555.1. ATB DRR103300 belongs to E. coli sample SAMD00077708. Assembly statistics and a Staphylococcus SeqKit-checksum substring are not identity evidence. Source-specific names and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Any future enrichment should retain exact environmental-clone identity and use AB031639.1 only as directly sourced marker evidence. Do not infer accessions from numbering or transfer culture, genome or functional claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103300 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, preserving earlier reports.
