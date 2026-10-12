# YAML Record Review: uncultured gamma proteobacterium TIHP368-01

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_01.yaml`
- Started UTC: 2026-10-04T04:47:23Z
- Finished UTC: 2026-10-04T04:48:07Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` denotes `NCBITaxon:103295`, uncultured gamma proteobacterium TIHP368-01: rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:50423`, seven root-first ancestors and code 11. Grounding is `EXACT`, status `SEEDED`, strain_count zero. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future fixes belong to maintained source transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, if inclusion changes, `curation/seed_scope.tsv`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_01.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_01.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity/lineage/code, source attestation, scope/PATHS registration and seed text. Evidence audits do not substitute for corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18404`, name-catalog shard 0000 row 38422, PATHS row 13341 and scope row 144064 agree on this exact target. Live NCBI EFetch and Datasets confirm the preferred label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The final ancestor is the environmental-samples grouping beneath Gammaproteobacteria, not a genus. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103295&retmode=xml)

The source species rank supports inclusion without claiming valid nomenclatural publication, cultivation or a type strain. No extra synonym or formal binomial is asserted. TIHP368-01 is not interchangeable with a TIHP302 clone or another TIHP368 suffix.

## Evidence

The pinned backbone/name row and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869721; its source qualifiers and reference metadata were inspected. AB031627.1 is a 783 bp partial 16S rRNA sequence with explicit taxon:103295, clone TIHP368-01, environmental_sample and coastal-marine-sediment qualifiers. It is a marker, not an assembly or culture deposit. The accession was resolved directly, not inferred from neighboring numbers. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031627.1)

Reference metadata names Urakawa, Yoshida, Nishimura and Ohwada for an unpublished coastal-community study using 16S and quinone profiling, with a separate direct submission dated 1999-08-25. The entries supply no DOI/PMID, and the YAML cites no publication. The community-study context does not prove a clone-specific phenotype.

Exact-taxid Assembly ESearch returned zero entries with a phrase-not-found/no-items warning. This bounded result agrees with the inspected marker-only context; it is not a universal genome-absence claim.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Empty optional strains, nomenclature, mappings and functional fields are appropriate. Zero strain_count follows the BacDive-subtree definition.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 103295, TIHP368-01/underscore spelling and the complete stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 40 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned; their two BacDive request matches refer to that source's own identifier. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103295 is an excluded culture collision. BacDive 13158 labels it Pseudomonas chlororaphis subsp. aureofaciens EIII.9.25.1/L8, with strain taxid 1215095 and subspecies 587851. GOLD Go0264509 instead uses name Pseudomonas chlororaphis and taxid 587753. StrainInfo SI-ID 3935 has the latter taxon context and owns deposit 154215, CIP 103295, whose deposit taxon field is absent. These source-scope differences were preserved, not reconciled or transferred to the environmental clone.

Other excluded matches include BacDive 103295, Agromyces sp. ST027489(HKI), GT20044005/51513; DSM 103295, phage deposit 914392 in SI-ID 407047; KY103295 in Debaryomyces subglobosus SI-ID 63638; and CP103295 in Escherichia coli 2e/GCA_024760205.1 context. Genome collisions include Lactiplantibacillus plantarum SRCM103295/GCA/GCF_004087995.1, uncultured bacterium MGBC103295/GCA_948714845.1, Vibrio brasiliensis MarMAG_103295/GCA/GCF_977587835.1, Listeria FLAG-103295/GCA_050885345.1, Shigella sonnei PNUSAE103295/GCA_023873045.1 and Shigella flexneri isolate 103295/GCA_026021695.1. ATB DRR103295 belongs to Escherichia coli sample SAMD00077703; unrelated GTDB assembly-statistic values are not taxon-ID assertions.

No gene, resistance, pathway, expression-module or causal-graph claim is present. iModulonDB is not applicable, not negative evidence; marker context alone does not require functional enrichment.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed assertions and source scope.

## Recommended Edits

None required. Future enrichment should preserve the exact environmental-clone identity and represent AB031627.1 only as marker evidence with its source qualifiers. Do not infer accessions from numbering, attach unrelated culture/genome links by numeric substring or infer phenotype from study metadata.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103295 --force`, inspect the result and repeat both focused validators. No canary ran here. Reconfirm the exact marker/taxon/source qualifiers before adding sequence evidence, and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished study results.

No YAML, maintained input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; previous reports were preserved.
