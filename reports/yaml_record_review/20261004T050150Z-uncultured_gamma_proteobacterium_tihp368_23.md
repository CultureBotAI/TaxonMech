# YAML Record Review: uncultured gamma proteobacterium TIHP368-23

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_23.yaml`
- Started UTC: 2026-10-04T04:59:55Z
- Finished UTC: 2026-10-04T05:01:50Z
- Verdict: pass

## Target

The full generated `TaxonRecord` denotes `NCBITaxon:103301`, uncultured gamma proteobacterium TIHP368-23. It carries species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. NCBITAXON is its sole attestation, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Any future correction belongs to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_23.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_23.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text; these are not a replacement for corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18410`, name-catalog shard 0000 row 38428, PATHS row 13348 and scope row 144070 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103301&retmode=xml)

The full clone designation is retained without extra synonyms, formal-binomial, cultivation or type-material claims. NCBI species rank supports inclusion, not an inference of nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869736. Its inspected qualifiers identify AB031642.1, a 783 bp partial 16S rRNA sequence, taxon:103301, clone TIHP368-23, environmental_sample and coastal marine sediment. This directly resolved marker is not a genome assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031642.1)

The inspected references describe an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML supply a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This is a bounded query result, not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

An ignored-inclusive `rg --no-ignore --hidden -n -z -i` search covered bounded 103301, TIHP368-23/underscore spelling and the complete stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 38 matching lines and structured contexts were inspected. Separately scanned SOURCE.json files yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103301 belongs to Sphingomonas echinoides, BacDive 14200, strain taxid 1112212/species 59803 and SI-ID 4046's own deposit 17275. LPSN 781007 and the synonym records Parasphingomonas echinoides/65502 and Pseudomonas echinoides/780009 carry that designation and marker AB021370. Their type material, nomenclature and references do not support this clone. DSM 103301 is Pseudomonas aeruginosa H1l/287, BacDive 131886 and SI-ID 401200's own deposit 908114; it is distinct from CIP 103301 and the target taxon.

Other excluded matches include BacDive 103301, Agromyces sp. STI07747/51513; CP103301 in Klebsiella pneumoniae Kpn1695/573, GCA_025723265.1; uncultured Duncaniella sp. MGBC103301/GCA_948689545.1; Shigella flexneri PNUSAE103301/GCA_023758465.1; Listeria monocytogenes FLAG-103301/GCA_050884945.1; uncultured bacterium MarMAG_103301/GCA_977587345.1; and uncultured Bacillota bacterium ERR15992690_bin_103301/GCA_982230225.1. ATB DRR103301 belongs to E. coli sample SAMD00077709. Assembly-statistic matches do not establish identity. Source-specific names and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031642.1 only as directly sourced marker evidence. Do not infer adjacent accessions or transfer culture, genome, nomenclature or phenotype claims through numeric coincidences.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103301 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm sequence source qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, preserving all prior reports.
