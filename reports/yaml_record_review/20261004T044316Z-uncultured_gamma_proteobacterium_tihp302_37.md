# YAML Record Review: uncultured gamma proteobacterium TIHP302-37

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_37.yaml`
- Started UTC: 2026-10-04T04:42:34Z
- Finished UTC: 2026-10-04T04:43:16Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` denotes `NCBITaxon:103292`, uncultured gamma proteobacterium TIHP302-37. It has rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:50423`, seven root-first ancestors, code 11, `EXACT` grounding, `SEEDED` status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future correction owners are maintained upstream transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, if inclusion changes, `curation/seed_scope.tsv`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_37.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_37.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity/lineage/code, source attestation, scope/PATHS registration and seed text. Evidence audits do not substitute for corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18401`, name-catalog shard 0000 row 38419, PATHS row 13338 and scope row 144061 agree on the exact target. Live NCBI EFetch and Datasets confirm the label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The final ancestor is the environmental-samples grouping below Gammaproteobacteria, not a genus. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103292&retmode=xml)

The source species rank supports repository inclusion without asserting nomenclatural publication, cultivation or a type strain. No synonym, formal binomial or broader identity is inferred.

## Evidence

The pinned backbone/name row and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869717; its source qualifiers and reference metadata were inspected. AB031623.1 is an 861 bp partial 16S rRNA sequence, explicitly linked to taxon:103292 and clone TIHP302-37, with environmental_sample and coastal-marine-sediment qualifiers. It is a marker, not a genome assembly or deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031623.1)

Its reference metadata names Urakawa, Yoshida, Nishimura and Ohwada for an unpublished coastal-community study using 16S and quinone profiling, and a separate direct submission dated 1999-08-25. No PMID/DOI is supplied by those entries; none is claimed in the YAML. The community-study context does not establish a clone-specific phenotype.

Exact-taxid Assembly ESearch returned zero entries with a phrase-not-found/no-items warning. This bounded query supports the inspected marker-only context, not a universal genome-absence claim.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory entry, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Empty optional strains, mappings, nomenclature and functional fields are appropriate. Zero strain_count follows the BacDive-subtree definition.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 103292, TIHP302-37/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 42 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned; their two BacDive request matches use that resource's own ID namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

The main excluded culture collision is CIP 103292, Aggregatibacter segnis HK316/ATCC 33393. BacDive 11755 and the backbone place its strain at 888057 under species 739; GOLD Go0610005 and StrainInfo SI-ID 47018/own deposit 151566 use species 739. LPSN 785426 and historical Haemophilus segnis 795963, type-material rows for 739 and the DQ005625 sodA reference concern that culture, not TIHP302-37. This species/strain source-scope difference does not create any link to taxon 103292.

Other excluded matches are BacDive 103292, Agromyces sp. ST001922/51513; DSM 103292, phage deposit 904161 in SI-ID 397527; KY103292 in Debaryomyces subglobosus SI-ID 177821; and CP103292 in BV-BRC strain JKL2022/taxid 1685. Genome collisions include Lactiplantibacillus plantarum SRCM 103292/GCA/GCF_004055435.1, Treponema MGBC103292/GCA_948687105.1, Escherichia coli PNUSAE103292/GCA_023758795.1 and Photobacterium chitinilyticum MarMAG_103292/GCA_977601415.1. ATB DRR103292 belongs to Escherichia coli sample SAMD00077700; assembly-statistic and SeqKit checksum substrings are not identity evidence.

No gene, pathway, resistance, expression-module or causal-graph claim is present. iModulonDB is not applicable, not negative evidence; marker context alone does not require functional enrichment.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve the environmental-clone identity and represent AB031623.1 only as directly sourced marker evidence. Do not import unrelated culture/type-strain/genome links by matching digits or infer phenotype from community-study metadata.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103292 --force`, inspect the result and repeat both focused validators. No canary ran here. Reconfirm exact marker/taxon/source qualifiers before adding sequence evidence, and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished study results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, preserving previous reports.
