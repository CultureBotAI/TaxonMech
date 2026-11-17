# YAML Record Review: uncultured gamma proteobacterium TIHP368-66

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_66.yaml`
- Started UTC: 2026-10-04T05:27:40Z
- Finished UTC: 2026-10-04T05:28:36Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103314`, uncultured gamma proteobacterium TIHP368-66: species rank, BACTERIA, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. The sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion decisions, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_66.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_66.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, genetic code, attestation, PATHS/scope registration and seed text. These checks are not corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18423`, name-catalog shard 0000 row 38441, PATHS row 13362 and scope row 144083 agree. Live NCBI Taxonomy EFetch and Datasets confirm exact label, species rank, parent 50423, genetic code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103314&retmode=xml)

The full clone designation is retained without invented synonyms, a formal binomial, cultivation claims or type-material status. NCBI species rank does not imply nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869750. Inspected accession AB031656.1 is a 716 bp partial 16S rRNA sequence with taxon:103314, clone TIHP368-66, environmental_sample and coastal marine sediment. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031656.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML provide a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result does not prove universal genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strain, nomenclature, mapping and functional fields are appropriately empty. Zero strain_count agrees with the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103314, TIHP368-66/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 31 matched lines and their structured contexts were inspected. Separate SOURCE.json scans found two BacDive request matches, an unrelated SeqCode timestamp and a StrainInfo byte count. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103314 denotes Staphylococcus aureus Becker, BacDive 136195/taxid 1280, explicitly non-type, also represented by GOLD Go0154876. SI-ID 70227 owns SI-DP 155291, but both strain and own-deposit taxon fields are absent in the inspected StrainInfo record. Taxonomy from BacDive/GOLD was not imputed into those missing fields. This culture is not TIHP368-66.

Other excluded collisions include BacDive 103314, Agromyces sp. ST031447/51513; KY103314 in Brettanomyces bruxellensis SI-ID 178011; and CP103314 in a GOLD analysis named Mycolicibacterium crocinum JCM 16369. Genome collisions include uncultured Prevotellamassilia sp. MGBC103314/GCA_948763625.1, uncultured bacterium MarMAG_103314/GCA_977610945.1, Pseudomonas aeruginosa PSA-BAB-IMI-103314/GCA_033091655.1, Shigella sonnei PNUSAE103314/GCA_023697165.1, Salmonella enterica PNUSAS103314/GCA_016240075.1 and Listeria monocytogenes FLAG-103314/GCA_050886165.1. ATB DRR103314 belongs to E. coli sample SAMD00077722. Unrelated assembly statistics are not identity evidence. GOLD object identifiers were not counted as assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031656.1 only as directly sourced marker evidence. Do not infer neighboring accessions or transfer culture, genome, type-material or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103314 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. A local search-helper concatenation syntax error was corrected and the complete search rerun successfully before judgement.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
