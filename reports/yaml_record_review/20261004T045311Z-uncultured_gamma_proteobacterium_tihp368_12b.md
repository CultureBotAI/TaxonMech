# YAML Record Review: uncultured gamma proteobacterium TIHP368-12b

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_12b.yaml`
- Started UTC: 2026-10-04T04:50:26Z
- Finished UTC: 2026-10-04T04:53:11Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103297`, uncultured gamma proteobacterium TIHP368-12b. It has rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:50423`, seven root-first ancestors, code 11, `EXACT` grounding, `SEEDED` status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained upstream transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, if inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_12b.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_12b.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity/lineage/code, source attestation, scope/PATHS registration and seed text. Evidence audits do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone row `data/raw/ncbitaxon_taxa.tsv:18406`, name-catalog shard 0000 row 38424, PATHS row 13343 and scope row 144066 agree on this exact target. Live NCBI EFetch and Datasets confirm the preferred label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The final ancestor is the environmental-samples grouping beneath Gammaproteobacteria, not a named genus. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103297&retmode=xml)

The source species rank supports inclusion without claiming valid nomenclatural publication, cultivation or type-strain status. The complete clone designation is preserved; it is not interchangeable with another TIHP368 suffix. No extra synonym or formal binomial is asserted.

## Evidence

The pinned backbone/name row and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869729; its source qualifiers and reference metadata were inspected. AB031635.1 is a 496 bp partial 16S rRNA sequence with explicit taxon:103297, clone TIHP368-12b, environmental_sample and coastal-marine-sediment qualifiers. It is a marker, not an assembly or deposit. Its accession was resolved directly, not inferred from adjacent records. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031635.1)

Reference metadata names Urakawa, Yoshida, Nishimura and Ohwada for an unpublished coastal-community study using 16S and quinone profiling, plus a separate direct submission dated 1999-08-25. These entries supply no DOI/PMID, and the YAML cites no publication. The study context does not prove clone-specific phenotype assertions.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result agrees with the inspected marker-only context, not a universal genome-absence claim.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Empty optional strains, nomenclature, mappings and functional fields are appropriate. Zero strain_count follows the BacDive-subtree definition.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 103297, TIHP368-12b/underscore spelling and the complete stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 37 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned; two BacDive request matches concern that resource's own identifier namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103297 is an excluded culture collision: Curvibacter lanceolatus strain 192, BacDive 138785, with source strain taxid 1265504 and species taxid 86182. LPSN 783716 and the historical Pseudomonas lanceolata name 784725 include this deposit and marker AB021390; the NCBI type-material rows concern species 86182. StrainInfo SI-ID 277604 owns CIP deposit 154276 in the Curvibacter species context. These type-material, nomenclature, publication and marker assertions do not concern TIHP368-12b.

Other excluded matches include BacDive 103297, Agromyces sp. STI07737/51513; SI-DP 103297, Escherichia coli ATCC 23851 in SI-ID 38265; DSM 103297, Escherichia phage vB_EcoS-WFI deposit 910239 in SI-ID 403182; KY103297 in Debaryomyces vietnamensis SI-ID 368220; and CP103297 in Escherichia coli 2e/GCA_024760205.1. These identifiers occupy distinct namespaces.

Genome collisions include Lactiplantibacillus plantarum SRCM103297/GCA/GCF_004141755.1, uncultured Oscillospiraceae bacterium MGBC103297/GCA_948626135.1, Shigella flexneri PNUSAE103297/GCA_023670445.1 and Escherichia coli fosA_Ecoli_1/GCA_901521665.1 with historical RefSeq GCF_901521665.1. ATB DRR103297 belongs to Escherichia coli sample SAMD00077705; unrelated assembly-statistic substrings do not assert this taxon identity. Source-specific names and accession versions were retained rather than transferred to the target.

No gene, resistance, pathway, expression-module or causal-graph assertion is present. iModulonDB is not applicable, not negative evidence; marker context does not require functional enrichment.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve the exact environmental-clone identity and represent AB031635.1 only as directly sourced marker evidence. Do not infer accessions from numbering, transfer unrelated culture/genome evidence by numeric substring or infer phenotype from the study title.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103297 --force`, inspect the result and repeat both focused validators. No canary ran here. Reconfirm exact marker/taxon/source qualifiers before adding sequence evidence, and run corpus-wide gates before broader release.

## Additional Notes

The browser web tool was unavailable; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished study results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, preserving earlier reports.
