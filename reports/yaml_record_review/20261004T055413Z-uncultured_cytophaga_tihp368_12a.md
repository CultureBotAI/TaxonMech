# YAML Record Review: uncultured cytophaga TIHP368-12a

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_cytophaga_tihp368_12a.yaml`
- Started UTC: 2026-10-04T05:53:29Z
- Finished UTC: 2026-10-04T05:54:13Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103326`, uncultured cytophaga TIHP368-12a: species rank, BACTERIA, parent 90877, twelve root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_cytophaga_tihp368_12a.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_cytophaga_tihp368_12a.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18435`, name-catalog shard 0000 row 38453, PATHS row 13380 and scope row 144095 agree. Live NCBI EFetch and Datasets confirm exact label, species rank, parent 90877, code 11 and all twelve lineage entries: 1/root, 131567/cellular organisms, 2/Bacteria, 3379134/Pseudomonadati, 1783270/FCB group, 68336/Bacteroidota/Chlorobiota group, 976/Bacteroidota, 768503/Cytophagia, 768507/Cytophagales, 89373/Cytophagaceae, 978/Cytophaga and 90877/environmental samples. Both group entries retain clade rank. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103326&retmode=xml)

Source spelling and suffix a are preserved as part of the clone's exact identity. No formal species binomial, synonym, cultivation or type-material status is invented. Placement and species rank are carried from NCBI, not independently re-established from the short marker or treated as nomenclatural publication evidence.

## Evidence

Pinned and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869728. Directly resolved AB031634.1 is a 223 bp partial 16S rRNA sequence whose qualifiers identify taxon:103326, clone TIHP368-12a, environmental_sample and coastal marine sediment. It is a short marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031634.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML provide a DOI/PMID. Study context does not establish clone-specific phenotype claims or a new taxonomic placement.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103326, TIHP368-12a/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 33 matched lines and their structured contexts were inspected. Separate SOURCE.json searches yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103326 denotes Leuconostoc citreum strain 5, BacDive 136184/taxid 33964, explicitly non-type, with GOLD Go0293737. SI-ID 3490 owns SI-DP 14629; both strain and own deposit carry taxid 33964/LPSN 777537. The culture's native NRRL : B-1142 designation and extracted normalized identifier do not identify the target clone. SI-DP 103326 instead denotes Planomonospora venezuelensis ATCC 23865, SI-ID 38274/BacDive 16577, with taxid 1999/LPSN 779677 on strain and deposit.

BacDive 103326 itself is Agromyces sp. ST018444/51513. KY103326 occurs in Derxomyces boninensis SI-ID 111505. CP103326 belongs to Lactiplantibacillus plantarum Ep-M17/GCA_032818175.1, BV-BRC 1590.4194. Other excluded genome collisions include uncultured Muribaculaceae bacterium MGBC103326/GCA_948698715.1, Pseudomonas aeruginosa PSA-BAB-IMI-103326/GCA_033091035.1, Shigella sonnei PNUSAE103326/GCA_023696145.1 and Salmonella enterica PNUSAS103326/GCA_008795655.1. Unrelated assembly statistics and ATB checksum substrings in Salmonella sample SAMN17129560 and Raoultella/Klebsiella-labelled sample SAMN42100757 do not establish identity. Source-specific labels were preserved, and GOLD object identifiers were not counted as assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present in the target. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Preserve exact clone identity and the source lineage. Future enrichment should represent AB031634.1 only as directly sourced marker evidence, without asserting biological equivalence to similarly named clones or transferring culture, genome, type-material or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103326 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. This review checks faithful taxonomy representation, not an independent phylogenetic reassessment from a 223 bp sequence.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
