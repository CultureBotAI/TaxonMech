# YAML Record Review: Sphingomonas sp. TS-001

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sphingomonas_sp_ts_001.yaml`
- Started UTC: 2026-10-03T08:24:06Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:25:10Z
- Verdict: pass

## Target

The full generated `TaxonRecord` was read. It denotes `NCBITaxon:1031697`,
Sphingomonas sp. TS-001, rank `SPECIES`, domain `BACTERIA`, with immediate
parent `NCBITaxon:196159`, unclassified Sphingomonas. Grounding is `EXACT`;
mapping status is `SEEDED`. It carries ten lineage entries, genetic code 11,
zero attached BacDive strains, one NCBI name attestation and one seeding event.
The target is at `data/taxa/PATHS.tsv:13119`.

## Validation

- `just validate data/taxa/bacteria/sphingomonas_sp_ts_001.yaml`: passed,
  no issues found.
- `just validate-strict data/taxa/bacteria/sphingomonas_sp_ts_001.yaml`:
  passed, one file scanned and zero errors.
- Structured YAML/TSV comparison: identity, rank, parent, genetic code and
  all ten ancestor IDs, labels, ranks and parent links match the maintained
  taxonomy inventory. A complete inventory scan found zero direct children.
- `just verify-corpus` was not rerun; the documented recipe is full-corpus-only,
  and these focused checks are not a substitute for a reproduction pass.
- `just validate-products` was not run because this record has no causal
  graph. `just validate-history` was not run because the bounded target search
  found no separate history artifact. The embedded seed event was inspected
  and covered by strict validation. No history record was created.
- Full source-catalog hash/census checks and rendered-site checks were not
  rerun. No source, record or page was modified.

## Identity and Grounding

The inspected [NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1031697&lvl=&mode=node)
agrees on taxon ID, scientific name, species rank, genetic code and displayed
lineage. The parent is an unclassified grouping below Sphingomonas, not an
identified named species. The exact taxon grounding does not claim an ICNP
validly published species name or a culture-deposit identity.

## Evidence

| Assertion | Inspected support |
| --- | --- |
| Identity and taxonomy | `data/raw/ncbitaxon_taxa.tsv:220777` contains the same ID, label, rank, parent, code and 2026-09-13 snapshot. Each ancestor was separately compared with its inventory row. |
| Scientific name | `data/catalog/ncbi_names-0005.jsonl.gz:29958` contains the exact scientific-name assertion. |
| Attestation | The taxonomy row has `attested_by=ncbitaxon`; the YAML retains one `NAME` assertion for the exact target. |
| Inclusion and seed event | `curation/seed_scope.tsv:321181` contains the 2026-09-13 one-source rationale retained by the embedded seed event. No human review approval is implied. |

The record makes no phenotype, mechanism, culture-medium, LPSN nomenclature,
GTDB mapping or genome assertion. It has no DOI/PMID or assembly reference
that requires additional resolution. NCBI's nucleotide-link count was not
mistaken for a curated genome association or an absent biological sequence.

## Completeness

Identifier, label and slug were searched with `rg --no-ignore --hidden` in
the TSV/YAML inventories under `data/raw/`, `data/atb/` and `data/straininfo/`,
and in `curation/`, `history/` and `reports/yaml_record_review/`. Only the
taxonomy and seed-scope rows matched; no previous target report or separate
history artifact was found.

Additional ignored-file-inclusive `rg -z` searches covered JSONL.GZ, TSV.GZ
and TSV.XZ files under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/` and `data/straininfo/`, using the ID, exact label, slug, numeric
taxonomy-field forms and standalone designation TS-001. Only the NCBI
scientific-name row matched. These are bounded searches of maintained source
surfaces, not a claim that no external evidence exists.

No descendant aggregation was missed in the checked inventory. Zero attached
BacDive strains and omitted optional source-specific fields are therefore
consistent with the maintained evidence. Definition, evidence and causal-graph
fields need not be populated merely to make this seeded record look fuller.

## Findings

- **Blocker:** None found.
- **Major:** None found.
- **Minor:** None found within the inspected snapshot and source scope.

## Recommended Edits

None. Preserve the exact placeholder name and the NCBI lineage. Do not attach
a nearby named species, strain deposit or genome through label similarity.
Any future source enrichment belongs in the maintained source/import path
and normal seeder workflow, never a hand edit to this generated YAML.

## Follow-up Checks

No corrective check is required for a finding. After a future authorized
source refresh, repeat the live NCBI identity check, both target validators
and the full `just verify-corpus`. Any new strain/genome link must carry its
own exact source and deposit/sample evidence.

## Additional Notes

Direct target URL opens failed, but following the target link from NCBI's
unclassified-Sphingomonas tree exposed the usable target page. The original
pinned taxdump archive was not independently replayed in this review; source
and lineage checks used committed inventories and the accessible authority
page. LPSN, GTDB and BacDive pages are not cited assertions of this record.
iModulonDB is not applicable to this taxonomy-only record. No paid research,
external messages, GitHub changes, history additions or status promotion were
performed.
