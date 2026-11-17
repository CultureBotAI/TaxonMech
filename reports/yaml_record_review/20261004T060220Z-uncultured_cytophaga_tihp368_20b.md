# YAML Record Review: uncultured cytophaga TIHP368-20b

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_cytophaga_tihp368_20b.yaml`
- Started UTC: 2026-10-04T06:01:29Z
- Finished UTC: 2026-10-04T06:02:20Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:103327`, rank
`SPECIES`, domain `BACTERIA`, grounding `EXACT`, status `SEEDED`, genetic
code 11, twelve lineage entries, zero strains and one NCBITAXON NAME
attestation. The record denotes an environmental clone, not a culture.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_cytophaga_tihp368_20b.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_cytophaga_tihp368_20b.yaml`: passed, one file, zero ERROR rows; refreshed the strict-validation TSV.
- Structured comparisons verified all twelve ancestors, parent, label,
  rank, code, empty synonyms, attestation, scope and seed-event text.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests,
  provenance/history/product gates, global term/reference checks and site
  rendering. The focused comparisons do not replace these gates.

## Identity and Grounding

Pinned backbone row 18436 and native scientific-name row 38454 in
`data/catalog/ncbi_names-0000.jsonl.gz` agree with the YAML. Live
[NCBI taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103327)
was verified through public EFetch and Datasets after the browser page was
inaccessible. It confirms the species label, parent 90877 and the complete
root-first chain through Pseudomonadati, FCB group, Bacteroidota/Chlorobiota
group, Bacteroidota, Cytophagia, Cytophagales, Cytophagaceae, Cytophaga and
environmental samples. No hierarchy was reconciled or inferred. The pinned
backbone has no direct children; exact merged-ID and dropped scans found no
target entry. A substring hit for retired 1033271 is not this taxon.

## Evidence

Exact NCBI Nuccore search returned one record: [AB031640.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031640.1),
279 bases of partial 16S rRNA gene, UID 5869734. Its source explicitly names
clone TIHP368-20b, taxon 103327, an environmental sample and coastal marine
sediment. Both references were inspected: the Urakawa, Yoshida, Nishimura
and Ohwada community study is marked unpublished, followed by Urakawa's
1999-08-25 direct submission. No DOI or PMID is supplied in those references;
no publication identifier was guessed. This locus is not a genome or proof
of a cultured strain, phenotype or independently reassessed taxonomy.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The single attestation counts one NCBI name, not strains, publications or
independent experiments. Its snapshot and the seed event remain 2026-09-13.

## Completeness

Complete exact-ID scans found no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin, BactoTraits or NCBI type-material row for
this target. Empty optional slots are supported by these bounded inventories.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched ID, label and
stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and
`history`: 117 matching lines. Separate recursive structured SOURCE.json
checks returned two BacDive request-list references, not target attestations.
Inspected false-positive contexts include:

- CIP 103327: Yersinia bercovieri, taxon 634, BacDive 138412, GOLD Go0299282,
  StrainInfo SI-ID 58346 and its own SI-DP 147666; not this clone.
- BacDive 103327: Agromyces sp. ST028538, taxon 51513.
- KY103327: Derxomyces huiaensis; AB103327: a Streptoalloteichus hindustanus
  biosynthetic locus. Source accession namespaces are not taxon IDs.
- CP103327 is associated with genome records for taxon 738, strain 1433,
  assembly GCA_024799765.1. MGBC103327 is a Lachnospiraceae bacterium with
  GCA_948625945.1; MarMAG_103327 has GCA_977587545.1. None identifies TIHP368-20b.
- Other matches are unrelated pathogen isolate names, assembly/sample/run
  accessions, sizes and checksums. ATB includes unrelated processed entries,
  E. coli RUN_REMOVED entries and unknown NOT_PROCESSED samples. None supplies
  the missing exact strain/BioSample chain. No link or assembly equivalence
  was inferred from a numeric substring or shared source grouping.

These searches establish local-source coverage, not universal absence of
additional biological information.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and stated checks.

## Recommended Edits

None. Preserve the carried NCBI lineage, clone identity and zero-strain state.
Any future supported source correction belongs in maintained source inputs
and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:144096`. Never hand-edit generated YAML.

## Follow-up Checks

After an authorized source change, inspect its exact identity evidence and
inventory delta, run `just seed-canary NCBITaxon:103327 --force`, both focused
validators and `just verify-corpus`, then remaining QC gates. No canary or
regeneration was performed in this read-only review.

## Additional Notes

`data/taxa/PATHS.tsv:13383` resolves the unique target. EFetch and Datasets
were the successful live taxonomy fallbacks. The 279-base locus was not used
to override the carried genus placement. iModulonDB was not applicable:
there is no gene-function, regulator or expression-module claim in the YAML.
No YAML, maintained input, scope, history, review status or GitHub state was
changed; only this new report and the documented validation TSV were written.
