# YAML Record Review: uncultured gamma proteobacterium TIHP368-77

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_77.yaml`
- Started UTC: 2026-10-04T05:32:46Z
- Finished UTC: 2026-10-04T05:33:30Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103317`, uncultured gamma proteobacterium TIHP368-77: species rank, BACTERIA, parent 50423, seven root-first ancestors, genetic code 11, EXACT grounding, SEEDED status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_77.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_77.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18426`, name-catalog shard 0000 row 38444, PATHS row 13365 and scope row 144086 agree. Live NCBI Taxonomy EFetch and Datasets confirm exact label, species rank, parent 50423, genetic code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103317&retmode=xml)

The complete clone designation is retained without invented synonyms, a formal binomial, cultivation or type-material claims. NCBI species rank does not imply nomenclatural publication.

## Evidence

Pinned and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869756. Directly resolved AB031662.1 is a 731 bp partial 16S rRNA sequence whose source qualifiers identify taxon:103317, clone TIHP368-77, environmental_sample and coastal marine sediment. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031662.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML supply a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This is a bounded query result, not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103317, TIHP368-77/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 45 matched lines and their structured contexts were inspected. Separate SOURCE.json searches yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103317 concerns Mycobacterium avium subsp. silvaticum strain 6409, BacDive 8445, with subspecies taxid 44282 and strain taxid 1401690. NCBI type-material and LPSN 778401 concern the subspecies; GOLD Go0190422 uses species taxid 1764 with a silvaticum label. SI-ID 42732 owns SI-DP 114974; the strain and deposit retain their respective source names at taxid 44282. Native BacDive says type strain yes while the extracted inventory has flag 0. These scopes and the unrelated flag discrepancy were preserved, not reconciled or transferred to TIHP368-77.

The culture's explicitly deposit-linked partial sequence records AF547810, AF547900, AY544804, AY544889, DQ480275, DQ986051 and EF686780 are gene/marker evidence, not target genomes. LPSN EF521891 and its publication metadata likewise concern that culture. BacDive 103317 itself is Agromyces sp. ST031458/51513; KY103317 occurs in Brettanomyces bruxellensis SI-ID 177677. CP103317 belongs to Klebsiella pneumoniae hvKP12/GCA_024762135.1, represented by two BV-BRC records. NPDC103317_431_E11 is an unrelated GOLD culture project/analysis label.

Other excluded genome collisions include uncultured Alistipes sp. MGBC103317/GCA_910576555.1, uncultured bacterium MarMAG_103317/GCA_977612125.1, Pseudomonas aeruginosa PSA-BAB-IMI-103317/GCA_023904955.1, Shigella sonnei PNUSAE103317/GCA_023697665.1, Salmonella enterica PNUSAS103317/GCA_008789725.1 and Listeria monocytogenes FLAG-103317/GCA_050885165.1. ATB DRR103317 belongs to E. coli sample SAMD00077725. Unrelated assembly statistics do not establish identity. GOLD object identifiers are not assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present in the target. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required for this target. Future enrichment should preserve exact environmental-clone identity and represent AB031662.1 only as directly sourced marker evidence. Do not infer neighboring accessions or transfer culture, genome, type-material or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103317 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated culture's type-flag discrepancy is outside this record's scope; any future correction belongs to its maintained source/extraction inputs, not this YAML.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
