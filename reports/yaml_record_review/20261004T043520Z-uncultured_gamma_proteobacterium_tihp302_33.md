# YAML Record Review: uncultured gamma proteobacterium TIHP302-33

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_33.yaml`
- Started UTC: 2026-10-04T04:34:36Z
- Finished UTC: 2026-10-04T04:35:20Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` denotes `NCBITaxon:103287`, uncultured gamma proteobacterium TIHP302-33. It has rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:50423`, seven root-first ancestors, code 11, `EXACT` grounding, `SEEDED` status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_33.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_33.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched identity, complete backbone lineage/code, source attestation, scope/PATHS registration and seed text. Source and live API audits are not substitutes for corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18396`, `data/catalog/ncbi_names-0000.jsonl.gz:38414`, PATHS row 13333 and scope row 144056 agree on the exact target. Live NCBI EFetch and Datasets confirm the species-rank environmental taxon, preferred label, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The final ancestor is the environmental-samples grouping beneath Gammaproteobacteria, not a named genus. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103287&retmode=xml)

NCBI's species rank supports repository inclusion; it does not imply a validly published binomial or a cultured type strain. No extra synonym or nomenclatural identity is asserted. Other TIHP302 clones remain separate taxa.

## Evidence

The pinned backbone and name row support the single NCBITAXON NAME attestation. Current exact-taxid Nuccore ESearch returned one entry, UID 5869712, and its full source qualifiers and reference metadata were inspected. AB031618.1 is a 294 bp partial 16S rRNA sequence, explicitly names clone TIHP302-33 and taxon 103287, and carries environmental_sample and coastal-marine-sediment source context. It is not a genome assembly or culture-deposit identifier. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031618.1)

Its reference metadata names Urakawa, Yoshida, Nishimura and Ohwada for an unpublished community study using 16S and quinone profiling; a separate direct-submission entry is dated 1999-08-25. No PMID/DOI is supplied by those entries, and the YAML cites no publication. The broad study context does not establish a clone-specific metabolic or quinone phenotype.

Exact-taxid Assembly ESearch returned zero entries, with a phrase-not-found/no-items warning. This is a bounded live-query result, not proof that no assembly could exist under another identifier. It is consistent with the inspected marker-only context and does not require inventing genome links.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Empty optional strains, mappings, nomenclature and functional fields are appropriate. Zero strain_count is the BacDive-subtree count, not a universal absence claim.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 103287, TIHP302-33/underscore spelling and the target stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 20 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned; their two BacDive request matches refer to BacDive's own numeric identifier. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within those bounds.

Namespace and substring collisions were excluded:

- BacDive 103287 is Agromyces sp. ST000949, taxid 51513, not NCBITaxon:103287.
- DSM 103287 belongs to Escherichia phage vB_EcoM_WFC, taxid 2508193, in StrainInfo SI-ID 399325 with own deposit 906104.
- Strain SRCM103287 belongs to Lactiplantibacillus plantarum 1590, with GCA/GCF_004054305.1; MGBC103287 belongs to Muribaculaceae 2301481, with GCA_948731535.1.
- CP103287 is associated with Parabacteroides distasonis BFG-574/GCA_024760285.1, and KY103287 occurs in the Debaryomyces robertsiae StrainInfo record SI-ID 180424. Neither is this clone's accession.
- ATB run DRR103287 belongs to sample SAMD00077695 classified as Escherichia coli; assembly-statistic values and SeqKit checksum substrings containing the same digits are not identity evidence.

There is no gene, pathway, resistance, transcriptomics or causal-graph assertion. iModulonDB is not applicable, not negative evidence; marker context alone does not require functional enrichment.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Any later source enrichment should preserve the environmental-clone identity and represent AB031618.1 only as a marker sequence with direct provenance, never as an assembly or deposit. Do not add cultured-strain or functional claims from numeric collisions or the community-study title.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103287 --force`, inspect the output and repeat both focused validators. No canary ran here. Verify exact accession/taxon/source qualifiers before adding marker evidence, and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Sequence-source and reference metadata were inspected without inferring results from the unpublished study.

No YAML, maintained input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, preserving prior reports.
