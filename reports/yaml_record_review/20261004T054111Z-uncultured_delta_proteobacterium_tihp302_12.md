# YAML Record Review: uncultured delta proteobacterium TIHP302-12

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_delta_proteobacterium_tihp302_12.yaml`
- Started UTC: 2026-10-04T05:40:17Z
- Finished UTC: 2026-10-04T05:41:11Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103318`, uncultured delta proteobacterium TIHP302-12: species rank, BACTERIA, parent 34033, six root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. The sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_delta_proteobacterium_tihp302_12.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_delta_proteobacterium_tihp302_12.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched full backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18427`, name-catalog shard 0000 row 38445, PATHS row 13369 and scope row 144087 agree. Live NCBI EFetch and Datasets confirm exact label, species rank, parent 34033, code 11 and the complete lineage: 1/root, 131567/cellular organisms, 2/Bacteria, 68525/delta/epsilon subdivisions, 28221/Deltaproteobacteria and 34033/environmental samples. The delta/epsilon entry has clade rank. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103318&retmode=xml)

No kingdom or phylum placement is inferred to fill the source chain. The full clone designation is retained without invented synonyms, a formal binomial, cultivation or type-material claims. NCBI species rank does not imply nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869692. Directly resolved AB031598.1 is a 686 bp partial 16S rRNA sequence whose qualifiers identify taxon:103318, clone TIHP302-12, environmental_sample and coastal marine sediment. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031598.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither the inspected references nor the YAML provide a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count agrees with the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103318, TIHP302-12/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 37 matching lines and their structured contexts were inspected. Separate SOURCE.json scans yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103318 concerns Leuconostoc gelidum subsp. gelidum SML9, BacDive 6830, with species taxid 1244, subspecies taxid 1607839 and strain taxid 927691. NCBI type-material, LPSN 777546/791678 and GOLD Go0237724 concern that culture. Native BacDive says type strain yes while the extracted BacDive inventory has flag 0. SI-ID 3491 carries species taxid 1244 and owns SI-DP 152418, but the own-deposit taxon field is absent. These distinctions and the unrelated flag discrepancy were preserved; no strain-level taxonomy was imputed into the deposit or the target. LPSN AF175402 and publication metadata are excluded culture evidence.

BacDive 103318 itself denotes Agromyces sp. ST031462/51513; KY103318 occurs in Brettanomyces bruxellensis SI-ID 178165. CP103318 belongs to Klebsiella pneumoniae hvKP12/GCA_024762135.1, represented by two BV-BRC records. Other excluded genome collisions are Helicobacter rodentium MGBC103318/GCA_948698685.1 and GCF_948698685.1, uncultured bacterium MarMAG_103318/GCA_977622095.1, Pseudomonas aeruginosa PSA-BAB-IMI-103318/GCA_023904895.1, Shigella sonnei PNUSAE103318/GCA_023691765.1 and Salmonella enterica PNUSAS103318/GCA_008791525.1. ATB DRR103318 belongs to E. coli sample SAMD00077726. Unrelated assembly statistics do not establish identity. GOLD object identifiers are not assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present in the target. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required for this target. Future enrichment should preserve exact environmental-clone identity and represent AB031598.1 only as directly sourced marker evidence. Do not infer a missing taxonomic rank or transfer culture, genome, type-material or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103318 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated culture's flag discrepancy is outside this record's scope; any correction would belong to its maintained source/extraction inputs, not this YAML.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
