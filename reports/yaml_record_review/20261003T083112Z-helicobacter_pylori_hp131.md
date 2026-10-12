# YAML Record Review: Helicobacter pylori HP131

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_hp131.yaml`
- Started UTC: 2026-10-03T08:30:39Z
- Finished UTC: 2026-10-03T08:31:12Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:103171` denotes
Helicobacter pylori HP131 beneath species `NCBITaxon:210`. It declares
`STRAIN`, `BACTERIA`, `EXACT` grounding and `SEEDED` mapping status, ten
root-first lineage entries, genetic code 11, zero attached BacDive strains,
one NCBI name attestation and one 2026-09-13 seeding event. The target is at
`data/taxa/PATHS.tsv:13122`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_hp131.yaml`: passed,
  no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_hp131.yaml`:
  passed, one file scanned and zero errors. The diagnostic TSV has only its
  header.
- Structured YAML/TSV comparison confirmed the target ID, name, stored rank,
  parent and genetic code, and all ten ancestor IDs, labels, ranks and parent
  links. A complete taxonomy-inventory scan found zero direct children.
- `just verify-corpus` was not rerun: the documented recipe is full-corpus-only;
  focused comparisons are not a new reproduction pass. Full source-catalog
  hashes/censuses and rendered pages were not revalidated.
- `just validate-products` was not run because the record has no causal graph.
  `just validate-history` was not run because the bounded target search found
  no separate history artifact. The embedded event was inspected and covered
  by strict validation. No history artifact was created.

## Identity and Grounding

The inspected [NCBI HP131 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103171&lvl=&mode=node)
supports ID, scientific name, genetic code 11 and the displayed ancestry
through Helicobacter pylori. The species tree lists HP131 separately from
HP112 and HP125. The exact grounding identifies the infraspecific taxon,
not the whole species and not unrelated isolates sharing the designation.

The browser reports `no rank`, whereas the pinned inventory and YAML declare
`STRAIN`. This discrepancy is unresolved; no rank was inferred from the label
to reconcile it. Either rank remains eligible under the repository scope
because the immediate parent is a species.

## Evidence

| Assertion | Inspected support |
| --- | --- |
| Identity and stored taxonomy | `data/raw/ncbitaxon_taxa.tsv:18338` supplies the matching ID, name, STRAIN rank, parent 210, code 11 and snapshot 2026-09-13. All ancestor rows were individually compared. |
| Scientific name | `data/catalog/ncbi_names-0000.jsonl.gz:38351` contains the exact scientific-name assertion. |
| Attestation | The taxonomy row has `attested_by=ncbitaxon`; the YAML correctly retains one `NAME` assertion for this target. |
| Inclusion and event | `curation/seed_scope.tsv:143999` supplies the 2026-09-13 inclusion and one-source rationale retained by the embedded seed event. This is generation provenance, not human review approval. |

The record contains no DOI/PMID, LPSN name, GTDB mapping, BacDive deposit,
assembly accession or causal edge to resolve. It does not inherit species-level
nomenclature, phenotypes or another strain's genome.

## Completeness

Identifier, full label and slug were searched with `rg --no-ignore --hidden`
in TSV/YAML/Markdown files under `data/raw/`, `data/atb/`, `data/straininfo/`,
`curation/`, `history/` and `reports/yaml_record_review/`. Only the taxonomy
and scope rows matched; no previous target report or separate history artifact
was found.

Ignored-file-inclusive `rg -z` searches covered JSONL.GZ, TSV.GZ and TSV.XZ
files under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/` and
`data/straininfo/`, including exact numeric taxonomy fields and the standalone
designation HP131. The target-specific hit was the NCBI scientific-name row.
The broader designation search also found these inspected, rejected near matches:

- GOLD `Go0278046` and StrainInfo `SI-ID 361512` describe Vibrio harveyi
  (`NCBITaxon:669`), designation Gomez-Gil HP131, with LMG 22895 in StrainInfo.
  They do not refer to Helicobacter pylori HP131.
- `data/catalog/ncbi_genbank-0018.jsonl.gz:37116` describes
  `GCA_020362225.1`, strain HP131 of Escherichia coli (`NCBITaxon:562`).
  The shared bare designation does not establish identity with taxon 103171.

These searches include ignored files but are limited to the specified source
surfaces. No supported attached BacDive strain or descendant aggregation was
found for the target. Zero attached strains is not a claim that HP131 lacks
biological material or sequence evidence outside these sources. No optional
definition, phenotype or causal graph needs to be invented.

## Findings

- **Blocker:** None found.
- **Major:** None found.
- **Minor (1): Unresolved NCBI rank discrepancy.** The accessible browser says
  `no rank`; the pinned inventory and generated record say `STRAIN`.
  `src/taxonmech/ncbi_taxdump.py:load_taxdump` reads and normalizes the source
  rank rather than inferring it from a name. The original archive pinned by
  `conf/ncbi_taxdump.yaml` is unavailable locally, so source-version divergence
  versus import error remains unresolved. Ownership is the pinned NCBI
  input/configuration and importer, not the generated YAML. Identity and
  parent placement are unaffected.

## Recommended Edits

Do not change the YAML now. Compare taxon 103171 in the hash-verified original
`nodes.dmp` against a dated current NCBI source. If the pinned rank is `strain`,
retain it until an authorized source refresh. If it is `no rank`, correct the
owning extraction/inventory integration with a regression test, then regenerate.
Do not add the Vibrio or Escherichia genome/deposit candidates based on HP131
name similarity.

## Follow-up Checks

1. Recover the archive in `conf/ncbi_taxdump.yaml` with SHA256
   `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`
   and inspect the exact source rank for 103171.
2. For a separately authorized correction, run relevant
   `tests/test_ncbi_taxdump.py` tests, re-extract, use
   `just seed-canary NCBITaxon:103171`, repeat both target validators and run
   the full `just verify-corpus`.
3. Any future HP131 strain/genome association must resolve its full source
   identity and biological scope, not just the repeated short designation.

## Additional Notes

The authority page was reached from NCBI's species-tree link. Earlier in this
same review session, an ignored-file-inclusive repository filename search for
taxdump/nodes artifacts found the configuration, importer, test and bytecode
but no archive or `nodes.dmp`; the configured snapshot directory was unavailable.
No assertion is made about archives outside the checkout.

iModulonDB is not applicable: this is a taxonomy-only record without a gene
or transcriptomic claim. No generated record, source inventory, page, history
or review status was changed. No paid research, external messages or GitHub
mutation was performed.
