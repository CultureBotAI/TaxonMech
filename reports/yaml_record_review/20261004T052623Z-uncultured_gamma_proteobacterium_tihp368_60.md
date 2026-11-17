# YAML Record Review: uncultured gamma proteobacterium TIHP368-60

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_60.yaml`
- Started UTC: 2026-10-04T05:23:18Z
- Finished UTC: 2026-10-04T05:26:23Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103313`, uncultured gamma proteobacterium TIHP368-60. It has species rank, BACTERIA domain, parent 50423, seven root-first ancestors, genetic code 11, EXACT grounding, SEEDED status and zero BacDive strains. The sole source attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13. Its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion decisions, `curation/seed_scope.tsv`. The generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_60.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_60.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured source comparisons matched the complete backbone identity, lineage, code, source attestation, PATHS/scope registration and seed text. They do not substitute for full-corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18422`, name-catalog shard 0000 row 38440, PATHS row 13361 and scope row 144082 agree with the record. Live NCBI Taxonomy EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103313&retmode=xml)

The clone designation is retained without inventing a formal binomial, synonym, cultivation claim or type-material status. Source species rank does not imply nomenclatural publication.

## Evidence

Pinned and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869749. Its inspected source qualifiers identify AB031655.1, a 728 bp partial 16S rRNA sequence, taxon:103313, clone TIHP368-60, environmental_sample and coastal marine sediment. This directly resolved marker is neither an assembly nor a culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031655.1)

Reference metadata identifies an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither the inspected references nor the YAML provide a DOI/PMID. This study context does not support clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This is a bounded query result, not universal proof of genome absence.

## Completeness

Complete exact-ID source scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strain, nomenclature, mapping and functional fields are appropriately empty. Zero strain_count agrees with the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103313, TIHP368-60/underscore spelling and the full record stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 33 matching lines and their structured contexts were inspected. SOURCE.json manifests were separately searched, yielding two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103313 denotes Staphylococcus aureus Reynolds, BacDive 138441/taxid 1280, explicitly non-type; GOLD Go0154875 carries that culture context. SI-ID 70226 owns SI-DP 155290, but both the strain and own-deposit taxon fields are absent in the inspected StrainInfo record. The BacDive/GOLD taxonomy was not imputed into those missing fields. This culture is not TIHP368-60.

Other excluded namespace collisions include BacDive 103313, Agromyces sp. ST031443/51513; SI-DP 103313, Bacillus subtilis ATCC 23859 under SI-ID 38270/taxid 1423; KY103313 in Brettanomyces bruxellensis SI-ID 90478; and CP103313 in a GOLD analysis named Mycolicibacterium rufum JCM 16372. Genome collisions include uncultured Eubacteriales bacterium MGBC103313/GCA_948691865.1, uncultured bacterium MarMAG_103313/GCA_977609835.1, Pseudomonas aeruginosa PSA-BAB-IMI-103313/GCA_033091795.1, Shigella sonnei PNUSAE103313/GCA_023697325.1, Salmonella enterica PNUSAS103313/GCA_008789345.1 and Listeria monocytogenes FLAG-103313/GCA_050885105.1. ATB DRR103313 belongs to E. coli sample SAMD00077721. Unrelated assembly statistics and Streptococcus pneumoniae/Mycobacterium tuberculosis SeqKit-checksum substrings do not establish target identity. GOLD object identifiers were not treated as assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031655.1 only as directly sourced marker evidence. Do not infer neighboring accessions or transfer culture, genome, type-material or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103313 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. Source-specific missing taxon fields in an unrelated culture are excluded context, not findings against this clone.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; existing reports were preserved.
