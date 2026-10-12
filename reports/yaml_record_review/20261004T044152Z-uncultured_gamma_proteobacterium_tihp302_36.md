# YAML Record Review: uncultured gamma proteobacterium TIHP302-36

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_36.yaml`
- Started UTC: 2026-10-04T04:41:10Z
- Finished UTC: 2026-10-04T04:41:52Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103291`, uncultured gamma proteobacterium TIHP302-36: rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:50423`, seven root-first ancestors and code 11. Grounding is `EXACT`, status `SEEDED`, strain_count zero. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained upstream transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_36.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_36.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity/lineage/code, source attestation, scope/PATHS registration and seed text. Evidence audits do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone row `data/raw/ncbitaxon_taxa.tsv:18400`, name-catalog shard 0000 row 38418, PATHS row 13337 and scope row 144060 agree on this exact clone-named taxon. Live NCBI EFetch and Datasets confirm its preferred label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The final ancestor is the environmental-samples grouping beneath Gammaproteobacteria, not a genus. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103291&retmode=xml)

The source species rank supports repository inclusion, not a claim of valid nomenclatural publication, cultivation or type-strain status. No extra synonym or formal binomial identity is asserted.

## Evidence

The pinned backbone/name row and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869716; its source qualifiers and reference metadata were inspected. AB031622.1 is an 871 bp partial 16S rRNA sequence with explicit taxon:103291, clone TIHP302-36, environmental_sample and coastal-marine-sediment qualifiers. It is not an assembly or deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031622.1)

Reference metadata names Urakawa, Yoshida, Nishimura and Ohwada for an unpublished coastal-community study using 16S and quinone profiling, plus a separate direct submission dated 1999-08-25. The entries supply no DOI/PMID, and the YAML cites no publication. This study context does not prove a clone-specific phenotype.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded live query agrees with marker-only evidence; it is not a universal genome-absence claim.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 103291, TIHP302-36/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 25 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned; two BacDive request matches concern its own identifier namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

Excluded collisions include BacDive 103291, Agromyces sp. ST001893/51513; CIP 103291, Haemophilus parainfluenzae HK 22/729, BacDive 137242, NCTC 11607, GOLD Go0172050 and StrainInfo SI-ID 68815/own deposit 151543; and SI-DP 103291, Escherichia coli ATCC 23849 in SI-ID 38263. These are not the environmental clone.

CP103291 belongs to an NS1 source record with taxid 450367/GCA_024758165.1; KY103291 occurs in Debaryomyces fabryi SI-ID 63548. Muribaculum MGBC103291/GCA_948607555.1, Escherichia coli PNUSAE103291/GCA_023759175.1 and Photobacterium chitinilyticum MarMAG_103291/GCA_977594285.1 are also distinct. ATB DRR103291 belongs to Escherichia coli sample SAMD00077699.

No gene, pathway, resistance, transcriptomics or causal-graph assertion is present. iModulonDB is not applicable rather than negative evidence, and marker context alone does not justify functional enrichment.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertions and source scope.

## Recommended Edits

None required. Future enrichment must preserve the environmental-clone identity and treat AB031622.1 only as marker evidence with exact source qualifiers. Do not import unrelated culture/genome links by numeric substring or infer phenotype from the community-study title.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103291 --force`, inspect the result and repeat both focused validators. No canary ran here. Reconfirm exact marker/taxon provenance before adding sequence evidence, and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Source/reference metadata were inspected without claiming access to unpublished study results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
