# YAML Record Review: Ralstonia solanacearum Po82

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/ralstonia_solanacearum_po82.yaml`
- Started UTC: 2026-10-03T08:41:04Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:42:28Z
- Verdict: needs curation

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1031711` denotes
Ralstonia solanacearum Po82, beneath species `NCBITaxon:305`. The record
declares `STRAIN`, `BACTERIA`, `EXACT` grounding and `SEEDED` mapping status.
It contains eleven ancestors, one GTDB mapping, three exact synonyms, one
GTDB xref, code 11, zero attached strains, three attestations and one
2026-09-13 seed event. Its index entry is `data/taxa/PATHS.tsv:13124`.

## Validation

- `just validate data/taxa/bacteria/ralstonia_solanacearum_po82.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/ralstonia_solanacearum_po82.yaml`:
  passed, one file scanned and zero errors.
- Structured YAML/TSV comparisons confirmed identity, stored rank, parent,
  code and all eleven ancestor labels, ranks and parent links. A complete
  taxonomy-inventory scan found zero direct children.
- The native GTDB species scan found 333 members across thirteen NCBI taxa;
  one member is assigned to 1031711. The mapping inventory has thirteen
  targets for this cluster: twelve closeMatch and one broadMatch.
- `just verify-corpus` was not rerun because it is full-corpus-only. These
  focused checks are not a reproduction pass. Full source hashes/censuses
  and generated pages were not revalidated.
- `just validate-products` is not applicable without causal-graph nodes.
  `just validate-history` was not run: an ignored-file-inclusive target
  search found no separate history artifact. The embedded event was inspected
  and covered by strict validation.
- `git diff --exit-code -- data/taxa/bacteria/ralstonia_solanacearum_po82.yaml`
  passed. The target and its maintained sources were not modified.

## Identity and Grounding

The inspected [NCBI Po82 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1031711)
agrees on identifier, label, two strain-name equivalents, code 11 and
lineage, including the Ralstonia solanacearum species-complex ancestor.
Its rank is `no rank`, unlike the pinned inventory's `STRAIN`. Identity,
parentage and eligibility below species are supported despite that discrepancy.

The GTDB species concept is broader than the Po82 taxon. The species-only
exact synonym and equivalence-style xref overstate what the inspected
metadata support. The genome count describes the cluster, not Po82 alone.

## Evidence

| Claim group | Inspected evidence and interpretation |
| --- | --- |
| NCBI identity and lineage | `data/raw/ncbitaxon_taxa.tsv:220780` matches all stored target fields; ancestor rows were checked individually by ID. `data/catalog/ncbi_names-0005.jsonl.gz:29965` and its following two rows support the scientific name and the `str. Po82`/`strain Po82` equivalent names. |
| GTDB mapping and count | `data/raw/gtdb_mappings.tsv:1316` supplies closeMatch and count 333; `data/raw/gtdb_species.tsv:152908` supplies the same species total. Of the native cluster's 333 genomes, 318 have species taxon 305, one has Po82 taxon 1031711, and fourteen span eleven other taxa. |
| Po82 member | `RS_GCF_000215325.1` has taxon 1031711, bare strain designation Po82, GenBank GCA_000215325.1, BioSample SAMN02603411 and project PRJNA224116. It is not the representative. |
| Representative | `RS_GCF_002251695.1` is the representative, assigned to K60 taxon 1091042, not Po82. This supplies an explicit counterexample to strain-level equivalence. |
| Native assemblies | Current GenBank GCA_000215325.1 and RefSeq GCF_000215325.1 rows have latest status, taxon 1031711, species taxon 305, strain Po82, sample SAMN02603411 and reciprocal paired-assembly accessions. Their projects are PRJNA66837 and PRJNA224116 respectively. |
| BV-BRC | `data/bvbrc/bvbrc-0000.jsonl.gz:3094` and the next row identify 1031711.10 as a plasmid record and 1031711.3 as complete. Both refer to the same assembly/sample/project. The complete record retains CP002819 and CP002820; these are not two distinct assemblies. |
| GOLD | Native organism Go0011247 has taxon 1031711, strain Po82 and an empty culture-collection field. Project Gp0011247 points to that organism, PRJNA66837 and SAMN02603411. Analysis Ga0030056 points to Gp0011247, IMG 651053062, and both nucleotide accessions associated with GCA_000215325.1. Organism/project IDs are not genome IDs. |
| Attestations and history | `data/raw/madin_taxa.tsv:586` supports four trait-assertion rows, not four independently verified phenotypes. The NCBI count is one name assertion. `curation/seed_scope.tsv:36136` supports the 2026-09-12 three-source rationale retained by the seed event. GTDB's count requires the same cluster-scope qualification as its mapping. |

The NCBI-linked [Po82 genome paper, PMID 21685279](https://pubmed.ncbi.nlm.nih.gov/21685279/)
was inspected at its abstract and associated-data sections. It corroborates
that Po82 was sequenced and associates CP002819/CP002820 with the report;
the bibliographic entry identifies DOI 10.1128/JB.05384-11. This is supplementary
identity/genome evidence, not justification to expand the YAML's phenotype
claims. The target itself cites no paper or LPSN name.

## Completeness

The exact identifier, name and slug were searched with
`rg --no-ignore --hidden` in review reports, history, curation, raw, ATB and
StrainInfo uncompressed inventories. Only taxonomy, GTDB mapping, Madin,
seed-scope and legacy-page rows matched before this report. No prior target
review or separate history artifact was found in those surfaces. Compressed
JSONL.GZ/TSV.GZ catalogs under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/` and `data/straininfo/` were searched with decompression for the
exact taxonomy fields, name variants and slug. The eleven native matches
were inspected; none was a BacDive or StrainInfo target record.

An additional case-insensitive standalone Po82/exact-taxid search in the
BacDive and culture-collection inventories returned no matches, including
ignored files. The NCBI-linked [BacDive 2083 page](https://bacdive.dsmz.de/strain/2083)
instead identifies type strain K60/60-1, taxon 1091042, with deposits including
DSM 9544 and ATCC 11696. A species-level type-strain link-out does not transfer
those deposits to Po82. The LPSN inventory entry `lpsn:780321` at
`data/raw/lpsn_names.tsv:19472` maps to parent species 305, not Po82.

Zero attached strains is consistent with the current requirement for
supported BacDive strain identities and eligible deposit evidence. Bare
Po82 does not meet that requirement. Native genome associations exist and
must not be described as absent merely because this array is empty.
Exposing taxon-to-genome associations directly is a separate representation
question. GOLD attestations originate in the maintained KGX inventory;
an omitted attestation is not evidence of absence from the native workbook.

## Findings

- **Blocker:** None found in primary identity or file structure.
- **Major (1): Species membership promoted to exact strain identity.**
  The closeMatch is imported from the kg-microbe GTDB transform through
  `src/taxonmech/extract.py:extract_gtdb`. In
  `src/taxonmech/seed.py:build_document`, line 451 treats it as identity,
  and lines 467-469 create a species-only exact synonym and xref. The native
  cluster includes K60 and many other taxa; it cannot be identical to Po82.
  The upstream predicate and local promotion rule are the maintained owners
  of the scope problem, not this generated YAML.
- **Minor (1): Unresolved source-rank discrepancy.** The accessible NCBI
  browser reports `no rank`; the pinned inventory says `STRAIN`.
  `src/taxonmech/ncbi_taxdump.py` normalizes source rank rather than inferring
  strain status. The original archive pinned in `conf/ncbi_taxdump.yaml`
  is unavailable in this checkout; source-version divergence versus importer
  error remains unproven. Identity and scope are unaffected.

## Recommended Edits

1. In a separately authorized correction, prevent
   `src/taxonmech/seed.py:build_document` from treating a species-cluster
   association as an exact synonym/equivalence xref of an infraspecific
   taxon solely because it is closeMatch. Retain the supported NCBI synonyms.
2. Review the owning kg-microbe mapping rule with Po82, determine supported
   scope/direction and re-extract as needed. Do not mechanically change
   closeMatch to another predicate or replace the species total 333 with one.
3. Add a focused `tests/test_seed.py` regression for species-cluster mappings
   on strain/unranked children, preserving supported species-level behavior.
4. Inspect the hash-verified pinned NCBI rank before modifying inputs or
   importer behavior. Do not assign K60 deposits to Po82 or hand-edit lineage.

## Follow-up Checks

- Run the new and existing seeder tests; confirm 1031711 retains parent 305
  and its two NCBI synonyms without the unsupported species-only equivalence.
- Recheck the native cluster count of 333, its thirteen NCBI targets and the
  single Po82 member. Keep plasmid, assembly, sample and project IDs distinct.
- Recover the taxonomy archive pinned by `conf/ncbi_taxdump.yaml`, SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`,
  and inspect the original `nodes.dmp` row for 1031711.
- After an authorized fix, run the normal extraction/seeding workflow,
  `just seed-canary NCBITaxon:1031711`, both target validators and the full
  `just verify-corpus`.

## Additional Notes

The live GTDB tree request failed; native RS232 metadata support the cluster
finding. NCBI's accessible response was cached six months earlier, so it is
not proof that the pinned inventory's rank was imported incorrectly. The
ignored-file-inclusive taxdump filename search in this session found no
archive or `nodes.dmp` within the checkout. No claim is made about external
copies. The compressed ATB full TSV.XZ and full source hashes were not checked.

iModulonDB is not applicable to this taxonomy/count-only record; no specific
gene or regulator is asserted. No paid research, outbound messages, GitHub
mutation, curation-history entry or human-review-status promotion occurred.
