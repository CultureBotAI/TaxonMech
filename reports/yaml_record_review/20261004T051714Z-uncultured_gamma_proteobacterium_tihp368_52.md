# YAML Record Review: uncultured gamma proteobacterium TIHP368-52

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_52.yaml`
- Started UTC: 2026-10-04T05:16:29Z
- Finished UTC: 2026-10-04T05:17:14Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103309`, uncultured gamma proteobacterium TIHP368-52. It carries species rank, BACTERIA domain, parent 744997, nine root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. NCBITAXON is its sole attestation, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_52.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_52.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18418`, name-catalog shard 0000 row 38436, PATHS row 13357 and scope row 144078 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 744997, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 1706369, 1706372, 744997. Cellvibrionales is order 1706369, Halieaceae is family 1706372, and the immediate parent is that family's environmental-samples grouping. This is not parent 50423, used by several adjacent clone records. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103309&retmode=xml)

The more specific carried lineage is supported independently, not inferred from the label or neighboring records. The complete clone designation is retained without extra synonyms, a formal binomial, cultivation or type-material claims. Source species rank supports inclusion without implying nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869745. Its inspected qualifiers identify AB031651.1, a 794 bp partial 16S rRNA sequence, with taxon:103309, clone TIHP368-52, environmental_sample and coastal marine sediment. This directly resolved marker is not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031651.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither those entries nor the YAML supply a DOI/PMID. Study context does not prove clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103309, TIHP368-52/underscore spelling and the full stem in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 42 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned, yielding two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103309 belongs to Clostridium butyricum Rowett, BacDive 2563, strain taxid 1316931/species 1492, LPSN 774842, GOLD organism Go0292750 and SI-ID 92601's own deposit 149939. Its type material, nomenclature, publication and AB595129 marker do not support this environmental clone.

Other excluded matches include BacDive 103309, Agromyces sp. ST027930/51513; KY103309 in Brettanomyces bruxellensis SI-ID 177880; and CP103309 in RL-GZ01/taxid 103816, GCA_024760325.1. Genome collisions include E. coli PNUSAE103309/GCA_023674305.2 with historical version .1, Pseudomonas aeruginosa PSA-BAB-IMI-103309/GCA_033091615.1, uncultured Candidatus Saccharibacteria bacterium MGBC103309/GCA_948623715.1, Listeria monocytogenes FLAG-103309/GCA_050885065.1, Salmonella enterica PNUSAS103309/GCA_008791705.1 and uncultured bacterium MarMAG_103309/GCA_977609815.1. ATB DRR103309 belongs to E. coli sample SAMD00077717. Unrelated assembly statistics and a Staphylococcus SeqKit-checksum substring do not establish identity. Source-specific labels and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion occurs. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment must preserve the independently supported Halieaceae lineage and exact clone identity, and represent AB031651.1 only as directly sourced marker evidence. Do not copy neighboring lineages/accessions or transfer culture, genome or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103309 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact source lineage and sequence qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
