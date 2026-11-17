# YAML Record Review: uncultured gamma proteobacterium TIHP368-74a

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_74a.yaml`
- Started UTC: 2026-10-04T05:29:30Z
- Finished UTC: 2026-10-04T05:30:14Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103315`, uncultured gamma proteobacterium TIHP368-74a. It carries species rank, BACTERIA domain, parent 50423, seven root-first ancestors, genetic code 11, EXACT grounding, SEEDED status and zero BacDive strains. The sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_74a.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_74a.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched the complete backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18424`, name-catalog shard 0000 row 38442, PATHS row 13363 and scope row 144084 agree. Live NCBI EFetch and Datasets confirm exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103315&retmode=xml)

The full designation, including suffix a, is retained without invented synonyms, a formal binomial, cultivation or type-material claims. Source species rank does not imply nomenclatural publication.

## Evidence

Pinned and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869753. The directly resolved AB031659.1 is a 585 bp partial 16S rRNA sequence whose source qualifiers identify taxon:103315, clone TIHP368-74a, environmental_sample and coastal marine sediment. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031659.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither those entries nor the YAML supply a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This is a bounded query result, not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103315, TIHP368-74a/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 47 matching lines and their structured contexts were inspected. Separate SOURCE.json searches yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103315 is Leuconostoc citreum B2399, BacDive 6828/taxid 33964, LPSN 777537, GOLD Go0293283 and SI-ID 3489 with own SI-DP 152410. Native BacDive says type strain yes; NCBI type-material and LPSN support that culture designation, while the extracted BacDive inventory has type flag 0. This unrelated source discrepancy is preserved, not resolved or transferred to TIHP368-74a. LPSN's AF111948 and publication metadata concern that culture, not the target.

SI-DP 103315 instead belongs to Actinomyces gerencseriae ATCC 23860, SI-ID 38271, BacDive 159/taxid 52769. Its explicitly deposit-linked EU647585, EU647589, EU647591 and EU647597 are partial gene records, not target genomes. BacDive 103315 itself denotes Agromyces sp. ST031449/51513. KY103315 is in Brettanomyces bruxellensis SI-ID 178214. CP103315 belongs to Klebsiella pneumoniae hvKP12/GCA_024762135.1, with two BV-BRC records; NPDC103315_429_C01 appears as an unrelated GOLD culture project/analysis label.

Other excluded genome collisions are Bifidobacterium pseudolongum subsp. globosum MGBC103315/GCA_948682835.1, uncultured bacterium MarMAG_103315/GCA_977597905.1, Pseudomonas aeruginosa PSA-BAB-IMI-103315/GCA_033091535.1, Shigella sonnei PNUSAE103315/GCA_023758265.1, Salmonella enterica PNUSAS103315/GCA_008789225.1, Listeria monocytogenes FLAG-103315/GCA_050885125.1, E. coli strain 103315/GCA_059797115.1 and Shigella flexneri isolate 103315/GCA_026021335.1. ATB DRR103315 belongs to E. coli sample SAMD00077723. Unrelated assembly statistics do not establish identity; GOLD object identifiers are not assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present in the target. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required for this target. Future enrichment should preserve exact environmental-clone identity and use AB031659.1 only as directly sourced marker evidence. Do not infer neighboring accessions or transfer culture, genome, type-material or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103315 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated Leuconostoc type-flag discrepancy is outside this record's scope; any later correction would belong to its maintained source/extraction inputs, not this YAML.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
