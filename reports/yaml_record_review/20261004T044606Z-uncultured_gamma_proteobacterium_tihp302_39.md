# YAML Record Review: uncultured gamma proteobacterium TIHP302-39

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_39.yaml`
- Started UTC: 2026-10-04T04:45:25Z
- Finished UTC: 2026-10-04T04:46:06Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` denotes `NCBITaxon:103294`, uncultured gamma proteobacterium TIHP302-39: rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:50423`, seven root-first ancestors and genetic code 11. Grounding is `EXACT`, status `SEEDED`, strain_count zero. NCBITAXON is the sole attestation, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained upstream transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_39.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_39.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity/lineage/code, source attestation, scope/PATHS registration and seed text. Source/API evidence audits do not substitute for corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18403`, name-catalog shard 0000 row 38421, PATHS row 13340 and scope row 144063 agree on this exact taxon. Live NCBI EFetch and Datasets confirm its preferred label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The final ancestor is the environmental-samples grouping below Gammaproteobacteria, not a genus. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103294&retmode=xml)

The carried species rank supports repository inclusion without claiming valid nomenclatural publication, cultivation or type-strain status. No synonym or formal binomial identity is asserted.

## Evidence

The pinned backbone/name row and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869719; its source qualifiers and reference metadata were inspected. AB031625.1 is a 762 bp partial 16S rRNA sequence with explicit taxon:103294, clone TIHP302-39, environmental_sample and coastal-marine-sediment qualifiers. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031625.1)

Reference metadata names Urakawa, Yoshida, Nishimura and Ohwada for an unpublished coastal-community study using 16S and quinone profiling, plus a separate direct submission dated 1999-08-25. The entries supply no DOI/PMID, and the YAML cites no publication. This community-study context does not establish clone-specific phenotype evidence.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. The bounded query agrees with the inspected marker-only context; it is not proof that no genome could exist under another identifier.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory entry, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Optional strains, mappings, nomenclature and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition, not a universal biological absence claim.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 103294, TIHP302-39/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 36 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned: two BacDive request matches use its ID namespace, and a StrainInfo response byte count happens to equal 103294. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within those bounds.

CIP 103294 is an excluded culture collision: Pasteurella canis 182, taxid 753, BacDive 11730, also ATCC 43326/DSM 22968/NCTC 11621. LPSN 779179, GOLD Go0612122 and StrainInfo SI-ID 46344/own deposit 153708 concern that culture, as do type-material rows and the AY702496 sodA reference. None identifies TIHP302-39.

Other excluded matches are BacDive 103294, Agromyces sp. ST027478(HKI), GT20044004/51513; SI-DP 103294, Escherichia coli ATCC 23850 in SI-ID 38264; DSM 103294, phage deposit 904393 in SI-ID 397738; and CP103294 in Limosilactobacillus fermentum LfU21 GOLD analysis context. Genome collisions include Muribaculaceae MGBC103294/GCA_910576965.1, Listeria monocytogenes FLAG-103294/GCA_050885325.1, Shigella sonnei PNUSAE103294/GCA_023798515.1 and Acidaminobacteraceae MarMAG_103294/GCA_977587635.1. ATB DRR103294 belongs to Escherichia coli sample SAMD00077702; unrelated assembly-statistic values containing these digits are not identity evidence.

No gene, resistance, pathway, expression-module or causal-graph assertion is present. iModulonDB is not applicable, not negative evidence; marker context alone does not require functional enrichment.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve the exact environmental-clone identity and represent AB031625.1 only as directly sourced marker evidence. Do not transfer type-strain, culture, genome or phenotype assertions through matching digits or a community-study title.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103294 --force`, inspect the result and repeat both focused validators. No canary ran here. Reconfirm exact marker/taxon/source qualifiers before adding sequence evidence, and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished study results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
