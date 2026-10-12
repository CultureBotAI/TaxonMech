# YAML Record Review: uncultured gamma proteobacterium TIHP302-35b

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_35b.yaml`
- Started UTC: 2026-10-04T04:39:42Z
- Finished UTC: 2026-10-04T04:40:26Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103290`, uncultured gamma proteobacterium TIHP302-35b. It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:50423`, seven root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status and zero BacDive strains. The sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13. Its seed event is dated 2026-09-13T17:54:04Z.

Future fixes belong to maintained upstream transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, if inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_35b.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_35b.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity/lineage/code, source attestation, scope/PATHS registration and seed text. Evidence audits are not corpus-reproduction gates.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18399`, `data/catalog/ncbi_names-0000.jsonl.gz:38417`, PATHS row 13336 and scope row 144059 agree on this exact taxon. Live NCBI EFetch and Datasets confirm its preferred label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The final ancestor is the environmental-samples grouping beneath Gammaproteobacteria, not a named genus. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103290&retmode=xml)

Species rank supports repository inclusion without asserting a validly published binomial, culture availability or type-strain status. The full clone suffix 35b is significant and is not interchangeable with 35a. No unsupported synonym or nomenclature is asserted.

## Evidence

The complete pinned backbone/name record and current taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869715; its source qualifiers and reference metadata were inspected. AB031621.1 is a 315 bp partial 16S rRNA sequence, explicitly linked to taxon:103290 and clone TIHP302-35b, with environmental_sample and coastal-marine-sediment qualifiers. It is a marker, not an assembly or deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031621.1)

The reference metadata names Urakawa, Yoshida, Nishimura and Ohwada for an unpublished coastal-community study using 16S and quinone profiling; a separate direct submission is dated 1999-08-25. No DOI/PMID is supplied by those entries, and the YAML cites no publication. The study context does not establish clone-specific quinone activity or another phenotype.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query is consistent with marker-only evidence, not proof that no genome could exist under another identifier.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Empty optional strains, mappings and nomenclature are appropriate. Zero strain_count is the BacDive-subtree count, not a universal biological absence claim.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 103290, TIHP302-35b/underscore spelling and the full target stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 43 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned; two BacDive request matches concern that database's identifier namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

Excluded collisions include:

- BacDive 103290 is Agromyces sp. ST000942, taxid 51513.
- CIP 103290 belongs to Haemophilus haemolyticus AQ/3273, taxid 726, BacDive 135242, LPSN 783939 and GOLD Go0205442. StrainInfo SI-ID 40473/own SI-DP 135975 also concerns that culture. Its DQ005618 sodA and JN175335, LC752364 and NR_104930 rRNA references are not TIHP302-35b evidence.
- Limosilactobacillus fermentum SRCM 103290 has GCA/GCF_004063635.1; Ruminococcus MGBC103290 has GCA_948694695.1; Escherichia coli PNUSAE103290 has GCA_023758895.2 and an earlier .1 catalog entry; Campylobacter jejuni strain 103290 has GCA_013292715.1.
- CP103290 appears in an NS2 source record, taxid 1452, GCA_024757965.1. ATB DRR103290 belongs to Escherichia coli sample SAMD00077698. Unrelated GTDB assembly statistics containing 103290 are not identity assertions.

No functional, resistance, pathway, expression-module or causal-graph claim is present. iModulonDB is not applicable, not negative evidence; marker context does not require functional enrichment.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve the exact environmental-clone identity and represent AB031621.1 only as marker evidence with direct provenance. Do not transfer cultured-strain, genome or phenotype claims through matching digits or the community-study title.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103290 --force`, inspect the result and repeat both focused validators. No canary ran here. Reconfirm the exact marker/taxon/source qualifiers before adding sequence evidence, and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Source/reference metadata were inspected without claiming access to unpublished study results.

No YAML, maintained input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
