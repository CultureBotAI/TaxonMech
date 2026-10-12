# YAML Record Review: uncultured gamma proteobacterium TIHP368-24

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_24.yaml`
- Started UTC: 2026-10-04T05:03:17Z
- Finished UTC: 2026-10-04T05:04:05Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103302`, uncultured gamma proteobacterium TIHP368-24. It carries species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. The sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Maintained owners for future corrections are source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_24.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_24.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18411`, name-catalog shard 0000 row 38429, PATHS row 13350 and scope row 144071 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria, not a named genus. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103302&retmode=xml)

The complete clone designation is retained without extra synonyms, a formal binomial, cultivation or type-material claims. Source species rank supports inclusion without implying nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869737. Its inspected source qualifiers identify AB031643.1, a 799 bp partial 16S rRNA sequence, with taxon:103302, clone TIHP368-24, environmental_sample and coastal marine sediment. This directly resolved marker is not a genome assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031643.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. No DOI/PMID is supplied by these entries or the YAML. Study context is not clone-specific phenotype evidence.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This is a bounded query result, not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103302, TIHP368-24/underscore spelling and the complete stem in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 39 matching lines and structured contexts were inspected. SOURCE.json files were separately scanned, yielding two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103302 belongs to BacDive 2888/taxid 12917 and SI-ID 136's own deposit 148005. BacDive, StrainInfo and LPSN 772601 label that culture Acidovorax facilis; the inspected NCBI type-material row uses Pseudomonas facilis, also represented by LPSN synonym 780015. These source names were preserved rather than reconciled. Their type material, nomenclature, references and AF078765 marker do not concern TIHP368-24. DSM 103302 is Serratia marcescens PH1a/615, BacDive 131927 and SI-ID 397620's own deposit 904260, not CIP 103302 or this target.

Other excluded matches include BacDive 103302, Agromyces sp. ST027886/51513; KY103302 in Brettanomyces anomalus SI-ID 179506; and CP103302 in Klebsiella pneumoniae Kpn1695/573, GCA_025723265.1. Genome collisions include uncultured Muribaculaceae bacterium MGBC103302/GCA_948634165.1, Shigella flexneri PNUSAE103302/GCA_023670525.1, Listeria monocytogenes FLAG-103302/GCA_050884925.1, Streptococcus pneumoniae strain 103302/GCA_035984315.1 and Acidaminobacteraceae bacterium MarMAG_103302/GCA_977587785.1. ATB DRR103302 belongs to E. coli sample SAMD00077710. Unrelated assembly statistics and Salmonella/E. coli SeqKit-checksum substrings are not identity evidence. Source-specific names and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal claim occurs. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should retain exact environmental-clone identity and represent AB031643.1 only as directly sourced marker evidence. Do not infer neighboring accessions or transfer culture, genome, nomenclature or phenotype claims by numeric coincidence.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103302 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm source qualifiers before sequence enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The source-name differences for the unrelated CIP culture are not findings against this clone.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
