# YAML Record Review: uncultured delta proteobacterium TIHP368-09

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_delta_proteobacterium_tihp368_09.yaml`
- Started UTC: 2026-10-04T05:42:05Z
- Finished UTC: 2026-10-04T05:42:47Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103319`, uncultured delta proteobacterium TIHP368-09: species rank, BACTERIA, parent 34033, six root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_delta_proteobacterium_tihp368_09.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_delta_proteobacterium_tihp368_09.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18428`, name-catalog shard 0000 row 38446, PATHS row 13370 and scope row 144088 agree. Live NCBI EFetch and Datasets confirm exact label, species rank, parent 34033, code 11 and the complete lineage: 1/root, 131567/cellular organisms, 2/Bacteria, 68525/delta/epsilon subdivisions, 28221/Deltaproteobacteria and 34033/environmental samples. The delta/epsilon entry has clade rank. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103319&retmode=xml)

The leading zero in clone designation 09 is retained. No kingdom or phylum placement is inferred. No synonyms, formal binomial, cultivation or type-material claims are invented; species rank is the source's assignment, not nomenclatural publication evidence.

## Evidence

Pinned and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869725. Directly resolved AB031631.1 is a 742 bp partial 16S rRNA sequence whose source qualifiers identify taxon:103319, clone TIHP368-09, environmental_sample and coastal marine sediment. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031631.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML provide a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103319, TIHP368-09/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 36 matching lines and their structured contexts were inspected. Separate SOURCE.json scans yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103319 denotes Leuconostoc carnosum SML40, BacDive 6827, with species taxid 1252 and strain taxid 1046593. NCBI type-material and LPSN 777536 concern that culture. SI-ID 125691 owns SI-DP 14619, with species taxid 1252 on both strain and own deposit. Native BacDive says type strain yes while the extracted inventory has flag 0. This unrelated discrepancy and the species/strain distinction were preserved, not resolved or transferred to the clone. LPSN AB022925 and publication metadata are excluded culture evidence.

BacDive 103319 itself is Agromyces sp. ST031472/51513. CP103319 belongs to Klebsiella pneumoniae hvKP12/GCA_024762135.1, represented by two BV-BRC records. Other excluded genome collisions include uncultured Muribaculaceae bacterium MGBC103319/GCA_948635475.1, uncultured bacterium MarMAG_103319/GCA_977632645.1, Pseudomonas aeruginosa PSA-BAB-IMI-103319/GCA_033091575.1, Shigella sonnei PNUSAE103319/GCA_023691905.1, Salmonella enterica PNUSAS103319/GCA_008792845.1 and Listeria monocytogenes FLAG-103319/GCA_050885185.1. ATB DRR103319 belongs to E. coli sample SAMD00077727. Unrelated assembly statistics and Mycobacterium/Salmonella SeqKit-checksum substrings do not establish identity. GOLD object identifiers were not counted as assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present in the target. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required for this target. Future enrichment should preserve exact environmental-clone identity and represent AB031631.1 only as directly sourced marker evidence. Do not infer a missing taxonomic rank or transfer culture, genome, type-material or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103319 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated culture's flag discrepancy is outside this record's scope; any correction would belong to its maintained source/extraction inputs, not this YAML.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
