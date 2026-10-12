# YAML Record Review: uncultured gamma proteobacterium TIHP368-30

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_30.yaml`
- Started UTC: 2026-10-04T05:09:13Z
- Finished UTC: 2026-10-04T05:10:10Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103305`, uncultured gamma proteobacterium TIHP368-30. It has species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. NCBITAXON is the sole attestation, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_30.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_30.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18414`, name-catalog shard 0000 row 38432, PATHS row 13353 and scope row 144074 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is an environmental-samples grouping beneath Gammaproteobacteria, not a named genus. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103305&retmode=xml)

The complete clone designation is retained without extra synonyms, a formal binomial, cultivation or type-material claims. Source species rank supports inclusion without implying nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869740. Its inspected qualifiers identify AB031646.1, a 735 bp partial 16S rRNA sequence, with taxon:103305, clone TIHP368-30, environmental_sample and coastal marine sediment. This directly resolved marker is not an assembly or deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031646.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. No DOI/PMID is supplied by these entries or the YAML. Study context does not prove clone-specific functional traits.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This is a bounded query result, not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103305, TIHP368-30/underscore spelling and the complete stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 35 matching lines and structured contexts were inspected. Separately scanned SOURCE.json files yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103305 belongs to Phenylobacterium immobile strain E/21, BacDive 2339, LPSN 779460 and SI-ID 3827's own deposit 16224. Its type material, nomenclature, publication and Y18216 marker do not support this clone. The related designation E CIP103305 remains scoped to that culture, not to taxon 103305.

Other excluded matches include BacDive 103305, Agromyces sp. ST027920/51513; SI-DP 103305, Bacillus subtilis ATCC 23856 in SI-ID 46630; KY103305 in Brettanomyces anomalus SI-ID 119099; and CP103305 in strain PLX03/taxid 1034015, GCA_024760425.1. Genome collisions include Lactiplantibacillus plantarum SRCM 103305/GCA/GCF_004055415.1, uncultured Dubosiella sp. MGBC103305/GCA_948621315.1, Shigella flexneri PNUSAE103305/GCA_023758425.1, Salmonella enterica PNUSAS103305/GCA_016240035.1, Listeria monocytogenes FLAG-103305/GCA_050885005.1, Pseudomonas aeruginosa PSA-BAB-IMI-103305/GCA_023906045.1 and uncultured bacterium MarMAG_103305/GCA_977609845.1. ATB DRR103305 belongs to E. coli sample SAMD00077713. Assembly statistics and a Moraxella SeqKit-checksum substring do not establish identity. Source-specific labels, spacing and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031646.1 only as directly sourced marker evidence. Do not infer adjacent accessions or transfer culture, genome, nomenclature or phenotype claims by numeric coincidence.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103305 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence source qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
