# YAML Record Review: uncultured gamma proteobacterium TIHP368-13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_13.yaml`
- Started UTC: 2026-10-04T04:54:42Z
- Finished UTC: 2026-10-04T04:55:47Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103298`, uncultured gamma proteobacterium TIHP368-13. It has species rank, domain BACTERIA, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for scope changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_13.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_13.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched the complete backbone identity, lineage and code, attestation, scope/PATHS registration and seed text. These checks are not corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18407`, name-catalog shard 0000 row 38425, PATHS row 13344 and scope row 144067 agree. Live NCBI taxonomy EFetch and Datasets confirm the label, rank, parent, genetic code and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is an environmental-samples grouping beneath Gammaproteobacteria, not a named genus. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103298&retmode=xml)

The complete TIHP368-13 clone designation is retained without synonyms or formal-binomial claims. Source species rank supports inclusion; it does not establish valid nomenclatural publication, cultivation or type material.

## Evidence

Pinned and live taxonomy support the exact NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869730. Its inspected source qualifiers identify AB031636.1, a 663 bp partial 16S rRNA sequence, with taxon:103298, clone TIHP368-13, environmental_sample and coastal marine sediment. This is marker evidence, not a genome assembly or culture deposit. The accession was resolved directly. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031636.1)

Reference metadata names Urakawa, Yoshida, Nishimura and Ohwada for an unpublished coastal-community study using 16S and quinone profiling, and a separate direct submission dated 1999-08-25. No DOI or PMID is supplied there or cited by the YAML. Study context does not prove a clone-specific phenotype.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This is a bounded query result, not proof of universal genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Empty optional strains, nomenclature, mappings and functional fields are appropriate. Zero strain_count follows the BacDive-subtree definition.

An ignored-inclusive `rg --no-ignore --hidden -n -z -i` search covered bounded 103298, TIHP368-13/underscore spelling and the record stem in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 32 matched lines and structured contexts were inspected. A separate SOURCE.json scan found two BacDive request matches in its own identifier namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103298 is Pseudomonas mucidolens strain 37, BacDive 13145, strain taxid 1215111/species 46679, LPSN 784727 and GOLD organism Go0599514. SI-ID 14308 owns CIP deposit 154294 in that species context. The culture's NCBI type material, LPSN publication and D84017 marker evidence do not belong to TIHP368-13.

Other excluded matches include BacDive 103298, Agromyces sp. STI07742/51513; DSM 103298, Escherichia phage vB_EcoS_HASG4 deposit 905717 in SI-ID 398961; and CP103298 in strain PS125/taxid 1234144, GCA_025562715.2. Genome collisions include Escherichia coli fosA_Ecoli_2/GCA_901521585.1 with historical GCF_901521585.1, uncultured Prevotella sp. MGBC103298/GCA_948623995.1 with historical GCF_948623995.1, and Shigella flexneri PNUSAE103298/GCA_023758385.1. ATB DRR103298 belongs to E. coli sample SAMD00077706. Assembly statistics and a Campylobacter SeqKit-checksum substring are not identity evidence. Source-specific accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment must preserve exact clone identity and represent AB031636.1 only as directly sourced marker evidence. Do not infer accessions from numbering or transfer culture, genome or phenotype claims from numeric collisions or study context.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103298 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence source qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished study results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
