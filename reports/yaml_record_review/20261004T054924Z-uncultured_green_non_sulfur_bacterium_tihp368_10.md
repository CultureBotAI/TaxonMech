# YAML Record Review: uncultured green non-sulfur bacterium TIHP368-10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_green_non_sulfur_bacterium_tihp368_10.yaml`
- Started UTC: 2026-10-04T05:48:45Z
- Finished UTC: 2026-10-04T05:49:24Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103323`, uncultured green non-sulfur bacterium TIHP368-10: species rank, BACTERIA, parent 58229, six root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. The sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_green_non_sulfur_bacterium_tihp368_10.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_green_non_sulfur_bacterium_tihp368_10.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18432`, name-catalog shard 0000 row 38450, PATHS row 13374 and scope row 144092 agree. Live NCBI EFetch and Datasets confirm exact label, species rank, parent 58229, code 11 and the complete lineage: 1/root, 131567/cellular organisms, 2/Bacteria, 1783272/Bacillati, 200795/Chloroflexota and 58229/environmental samples. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103323&retmode=xml)

The complete environmental-clone designation is retained without invented synonyms, a formal binomial, cultivation or type-material status. Green non-sulfur is source naming, not independent proof of photosynthesis or sulfur metabolism. NCBI species rank does not imply nomenclatural publication.

## Evidence

Pinned and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869726. Directly resolved AB031632.1 is a 759 bp partial 16S rRNA sequence whose qualifiers identify taxon:103323, clone TIHP368-10, environmental_sample and coastal marine sediment. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031632.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML provide a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103323, TIHP368-10/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 33 matching lines and their structured contexts were inspected. Separate SOURCE.json scans yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103323 concerns Yersinia bercovieri, BacDive 5226, species taxid 634 and strain taxid 349968, with LPSN 785220 and GOLD Go0630225. NCBI type-material and native BacDive support type status for that culture, whereas the extracted BacDive inventory has type flag 0. SI-ID 45179 owns SI-DP 147663, with species taxid 634 on strain and own deposit. This unrelated discrepancy and the species/strain scopes were preserved, not resolved or transferred to the target. LPSN KJ606905 and publication metadata are excluded culture evidence.

BacDive 103323 itself is Agromyces sp. ST018421/51513. CP103323 belongs to Klebsiella pneumoniae hvKP12/GCA_024762135.1, represented by two BV-BRC records. Other excluded genome collisions include uncultured Duncaniella sp. MGBC103323/GCA_948680895.1, uncultured bacterium MarMAG_103323/GCA_977587665.1, Pseudomonas aeruginosa PSA-BAB-IMI-103323/GCA_033091155.1, Shigella sonnei PNUSAE103323/GCA_023697725.1 and Salmonella enterica PNUSAS103323/GCA_008814735.1. Unrelated assembly statistics and ATB SeqKit-checksum substrings for Campylobacter-labelled sample SAMN11175931 and Mycobacterium-labelled sample SAMN37527098 do not establish identity; their source classification/QC fields were not promoted into target claims. GOLD object identifiers were not counted as assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required for this target. Future enrichment should preserve exact environmental-clone identity and represent AB031632.1 only as directly sourced marker evidence. Do not convert source naming into experimental phenotype evidence or transfer culture, genome or type-material claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103323 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated culture's type-flag discrepancy is outside this record's scope; any future correction belongs to its maintained source/extraction inputs, not this YAML.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
