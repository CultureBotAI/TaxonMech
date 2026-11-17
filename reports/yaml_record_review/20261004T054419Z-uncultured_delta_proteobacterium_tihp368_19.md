# YAML Record Review: uncultured delta proteobacterium TIHP368-19

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_delta_proteobacterium_tihp368_19.yaml`
- Started UTC: 2026-10-04T05:43:37Z
- Finished UTC: 2026-10-04T05:44:19Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103320`, uncultured delta proteobacterium TIHP368-19: species rank, BACTERIA, parent 34033, six root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. The sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_delta_proteobacterium_tihp368_19.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_delta_proteobacterium_tihp368_19.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched full backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18429`, name-catalog shard 0000 row 38447, PATHS row 13371 and scope row 144089 agree. Live NCBI EFetch and Datasets confirm exact label, species rank, parent 34033, code 11 and all six lineage entries: 1/root, 131567/cellular organisms, 2/Bacteria, 68525/delta/epsilon subdivisions, 28221/Deltaproteobacteria and 34033/environmental samples. The delta/epsilon entry has clade rank. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103320&retmode=xml)

No kingdom or phylum placement is inferred to fill the source chain. The full clone designation is retained without invented synonyms, a formal binomial, cultivation or type-material claims. NCBI species rank does not imply nomenclatural publication.

## Evidence

Pinned and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869732. Directly resolved AB031638.1 is a 750 bp partial 16S rRNA sequence whose qualifiers identify taxon:103320, clone TIHP368-19, environmental_sample and coastal marine sediment. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031638.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML supply a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103320, TIHP368-19/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 28 matching lines and their structured contexts were inspected. Separate SOURCE.json scans yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103320 is a Leuconostoc deposit, SI-DP 152464 under SI-ID 61416, with genus-level taxid 1243 on both strain and deposit. No species identity was inferred. SI-DP 103320 is a different object: ATCC 23862 under SI-ID 264292, BacDive 15126. Its source strain is Streptomyces diastatochromogenes/taxid 42236, while its own deposit is S. diastatochromogenes subsp. luteus/taxid 285494. The explicit deposit-linked assembly GCA_026913245 is retained without inventing a version suffix; it is evidence for that culture, not the target clone.

BacDive 103320 itself denotes Agromyces sp. ST018416/51513. CP103320 belongs to Klebsiella pneumoniae hvKP12/GCA_024762135.1, represented by two BV-BRC records. Other excluded genome collisions include uncultured bacterium MGBC103320/GCA_948709735.1 and MarMAG_103320/GCA_977612055.1, Pseudomonas aeruginosa PSA-BAB-IMI-103320/GCA_023905345.1, Shigella sonnei PNUSAE103320/GCA_023697705.1, Salmonella enterica PNUSAS103320/GCA_008793005.1 and Listeria monocytogenes FLAG-103320/GCA_050885225.1. ATB DRR103320 belongs to E. coli sample SAMD00077728. Unrelated assembly statistics and a Salmonella SeqKit-checksum substring do not establish identity. GOLD object identifiers were not counted as assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present in the target. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031638.1 only as directly sourced marker evidence. Do not infer a missing taxonomic rank or transfer culture, genome, type-material or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103320 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated StrainInfo strain/deposit taxonomic scopes and unversioned assembly were preserved at their source scope.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
