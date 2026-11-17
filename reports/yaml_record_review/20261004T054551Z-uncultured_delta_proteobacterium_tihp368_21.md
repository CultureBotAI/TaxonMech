# YAML Record Review: uncultured delta proteobacterium TIHP368-21

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_delta_proteobacterium_tihp368_21.yaml`
- Started UTC: 2026-10-04T05:45:10Z
- Finished UTC: 2026-10-04T05:45:51Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103321`, uncultured delta proteobacterium TIHP368-21: species rank, BACTERIA, parent 34033, six root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_delta_proteobacterium_tihp368_21.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_delta_proteobacterium_tihp368_21.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18430`, name-catalog shard 0000 row 38448, PATHS row 13372 and scope row 144090 agree. Live NCBI Taxonomy EFetch and Datasets confirm exact label, species rank, parent 34033, genetic code 11 and all six lineage entries: 1/root, 131567/cellular organisms, 2/Bacteria, 68525/delta/epsilon subdivisions, 28221/Deltaproteobacteria and 34033/environmental samples. The delta/epsilon entry has clade rank. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103321&retmode=xml)

No kingdom or phylum placement is inferred to fill the source chain. The full clone designation is retained without invented synonyms, a formal binomial, cultivation or type-material claims. NCBI species rank does not imply nomenclatural publication.

## Evidence

Pinned and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869735. Directly resolved AB031641.1 is a 762 bp partial 16S rRNA sequence whose source qualifiers identify taxon:103321, clone TIHP368-21, environmental_sample and coastal marine sediment. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031641.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML supply a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103321, TIHP368-21/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 24 matching lines and their structured contexts were inspected. Separate SOURCE.json searches yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103321 and CLIP 14014 concern Listeria grayi, BacDive 136197/taxid 1641, explicitly non-type. SI-ID 9806 owns SI-DP 38562, with Listeria grayi/LPSN 777586/taxid 1641 on the strain and own deposit. This culture is not TIHP368-21. BacDive 103321 itself denotes Agromyces sp. ST018417/51513.

CP103321 belongs to Klebsiella pneumoniae hvKP12/GCA_024762135.1, represented by two BV-BRC records. MGBC103321/GCA_948680975.1 has taxid 1906137: GenBank and GTDB label it Candidatus Gastranaerophilus phascolarcticola, while BV-BRC uses Candidatus Gastranaerophilus phascolarctosicola. Both source-specific spellings are preserved as excluded context, not silently reconciled or attributed to this clone.

Other excluded genome collisions include uncultured bacterium MarMAG_103321/GCA_977601515.1, Pseudomonas aeruginosa PSA-BAB-IMI-103321/GCA_033091135.1, Shigella sonnei PNUSAE103321/GCA_023696905.1 and Salmonella enterica PNUSAS103321/GCA_008792885.1. ATB DRR103321 belongs to E. coli sample SAMD00077729. Numeric similarity does not establish taxon, strain or genome equivalence. GOLD object identifiers were not counted as assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present in the target. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031641.1 only as directly sourced marker evidence. Do not infer a missing taxonomic rank or transfer culture, genome, type-material or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103321 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated genome's source-specific spelling difference is excluded context, not a finding against this clone.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
