# YAML Record Review: uncultured gamma proteobacterium TIHP368-18

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_18.yaml`
- Started UTC: 2026-10-04T04:56:31Z
- Finished UTC: 2026-10-04T04:57:31Z
- Verdict: pass

## Target

The full generated `TaxonRecord` denotes `NCBITaxon:103299`, uncultured gamma proteobacterium TIHP368-18. Its species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains were reviewed. NCBITAXON is the sole attestation, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Maintained owners for any future correction are source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Do not hand-edit generated YAML.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_18.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_18.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched the complete backbone identity, lineage and code, attestation, scope/PATHS registration and seed text. They do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18408`, name-catalog shard 0000 row 38426, PATHS row 13345 and scope row 144068 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103299&retmode=xml)

No extra synonym, binomial, cultivated isolate or type-material claim is made. Source species rank supports inclusion without implying nomenclatural publication. TIHP368-18 is not interchangeable with another clone suffix or an accession carrying the same digits.

## Evidence

Pinned and live taxonomy support the exact NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869731. Inspected source qualifiers identify AB031637.1, an 846 bp partial 16S rRNA sequence, with taxon:103299, clone TIHP368-18, environmental_sample and coastal marine sediment. This is marker evidence, not an assembly or culture deposit; its accession was directly resolved. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031637.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither those entries nor the YAML supply a DOI/PMID. The study context does not support clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Empty optional strains, nomenclature, mappings and functional slots are appropriate. Zero strain_count follows the BacDive-subtree definition.

The ignored-inclusive `rg --no-ignore --hidden -n -z -i` search covered bounded 103299, TIHP368-18/underscore spelling and the complete stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 39 matching lines and structured contexts were inspected. Separately scanned SOURCE.json files yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found in these bounds.

CIP 103299 belongs to Pseudomonas taetrolens/47884, BacDive 13148, LPSN 784738, GOLD organism Go0609661 and SI-ID 276625's own deposit 154392. Its type material, LPSN nomenclature and D84027 marker do not support TIHP368-18. A separate SI-ID 4592 record, classified as Stutzerimonas stutzeri/316, contains CIP 103299 only in `strain.relation.designation`; no own matching deposit was present. That related designation is not a deposit join or permission to transfer evidence between records.

Other excluded matches include BacDive 103299, Agromyces sp. STI07743/51513; Dactylosporangium sp. NAICONS 103299/3419229; KY103299 in Brettanomyces anomalus SI-ID 179798; and CP103299 in PS125/taxid 1234144, GCA_025562715.2. Genome collisions include Lacticaseibacillus paracasei SRCM103299/GCA/GCF_004141835.1, uncultured Alistipes sp. MGBC103299/GCA_948680765.1, Shigella flexneri PNUSAE103299/GCA_023758445.1, Listeria monocytogenes FLAG-103299/GCA_050885365.1 and uncultured bacterium MarMAG_103299/GCA_977627885.1. ATB DRR103299 belongs to E. coli sample SAMD00077707; an assembly statistic is also unrelated. Source-specific identity and versions were preserved.

No gene, resistance, pathway, expression-module or causal claim occurs. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Any future enrichment should retain exact clone identity and use AB031637.1 only as directly sourced marker evidence. Do not infer neighboring accessions, phenotype from a study title, or strain identity from related designations/numeric substrings.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103299 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm sequence source qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated StrainInfo grouping was preserved as context, not reported as a defect in this clone record.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, preserving all earlier reports.
