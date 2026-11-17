# YAML Record Review: uncultured green non-sulfur bacterium TIHP302-40

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_green_non_sulfur_bacterium_tihp302_40.yaml`
- Started UTC: 2026-10-04T05:47:10Z
- Finished UTC: 2026-10-04T05:47:53Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103322`, uncultured green non-sulfur bacterium TIHP302-40: species rank, BACTERIA, parent 58229, six root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_green_non_sulfur_bacterium_tihp302_40.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_green_non_sulfur_bacterium_tihp302_40.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18431`, name-catalog shard 0000 row 38449, PATHS row 13373 and scope row 144091 agree. Live NCBI EFetch and Datasets confirm exact label, species rank, parent 58229, code 11 and the complete lineage: 1/root, 131567/cellular organisms, 2/Bacteria, 1783272/Bacillati, 200795/Chloroflexota and 58229/environmental samples. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103322&retmode=xml)

The full environmental-clone label is retained without inventing a formal binomial, synonyms, cultivation or type-material status. The words green non-sulfur are source naming, not independent proof of photosynthesis or sulfur metabolism. NCBI species rank does not imply nomenclatural publication.

## Evidence

Pinned and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869720. Directly resolved AB031626.1 is a 724 bp partial 16S rRNA sequence whose qualifiers identify taxon:103322, clone TIHP302-40, environmental_sample and coastal marine sediment. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031626.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML supply a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count agrees with the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103322, TIHP302-40/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 37 matching lines and their structured contexts were inspected. Separate SOURCE.json scans yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103322 and CLIP 10445 denote Listeria monocytogenes LL 347, BacDive 138784/taxid 1639, explicitly non-type, with GOLD Go0289627. SI-ID 69211 owns SI-DP 152546; both strain and own deposit use taxid 1639/LPSN 777590. This culture is not TIHP302-40. BacDive 103322 itself is Agromyces sp. ST018419/51513.

SI-DP 103322 instead denotes CCM 3013 under SI-ID 264292/BacDive 15126. Its source strain is Streptomyces diastatochromogenes/taxid 42236; its own deposit is S. diastatochromogenes subsp. luteus/taxid 285494. Strain grouping alone cannot transfer another deposit's assembly links to CCM 3013 or to this clone. KY103322 occurs in Brettanomyces bruxellensis SI-ID 177955. CP103322 belongs to Klebsiella pneumoniae hvKP12/GCA_024762135.1, represented by two BV-BRC records.

Other excluded genome collisions include uncultured Phocaeicola sp. MGBC103322/GCA_948712165.1, plus historical RefSeq GCF_948712165.1 also retained by GTDB; uncultured bacterium MarMAG_103322/GCA_977594795.1; Shigella sonnei PNUSAE103322/GCA_023696825.1; and Salmonella enterica PNUSAS103322/GCA_008792565.1. ATB DRR103322 belongs to E. coli sample SAMD00077730. Unrelated assembly statistics do not establish identity. GOLD object identifiers were not counted as assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031626.1 only as directly sourced marker evidence. Do not convert the source label into an experimentally established phenotype or transfer culture, genome or type-material claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103322 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. Source-specific strain/deposit taxonomy and accession versions were preserved for excluded matches.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
