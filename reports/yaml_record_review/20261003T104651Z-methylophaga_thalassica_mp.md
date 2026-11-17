# YAML Record Review: Methylophaga thalassica MP

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylophaga_thalassica_mp.yaml`
- Started UTC: 2026-10-03T10:44:39Z
- Finished UTC: 2026-10-03T10:46:51Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1026882`, Methylophaga thalassica MP,
rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:40223`. The entire YAML
was read. Grounding is EXACT; mapping status is SEEDED. The record has one
GTDB mapping, three synonyms, no listed BacDive strains, four source
attestations and an embedded seed event.

This is a strain-level record review, not a review of the parent species or
the BacDive record mentioned as completeness context below.

## Validation

| Command or check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/methylophaga_thalassica_mp.yaml` | PASS, no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/methylophaga_thalassica_mp.yaml` | PASS, one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: documented full-corpus comparison, with no focused target selector. The checks below do not replace it. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive identifier/label/slug search of `history/` found no target entry. Embedded history was covered by strict validation. |

Read-only structured checks verified every ancestor label/rank and the parent
chain against the pinned taxonomy table. Full-table descendant traversal
found only this taxon in its subtree. Scanning the complete BacDive inventory
found no classified strain in that subtree. All ten native GTDB cluster
members were inspected. These checks establish source agreement, not
biological correctness or full-corpus reproducibility.

## Identity and Grounding

The ID, current name, parent, genetic code 11 and lineage agree with
`data/raw/ncbitaxon_taxa.tsv` row 218769. The
[NCBI authority page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1026882)
supports the current name and lists Methylophaga aminisulfidivorans MP and
Methylophaga aminisulfidivorans SK1 as equivalent names. The latter is described
as a co-identical strain. The two NCBI exact synonyms are therefore supported.

The inspected NCBI page reports `no rank`, whereas the pinned table and YAML
report STRAIN. The configured 2026-09-13 taxdump archive is not present at
`data/source_snapshots/ncbi-new-taxdump-2026-09-13.tar.gz`; its original
nodes row could not be replayed. The importer simply normalizes supplied
rank text. This snapshot/browser discrepancy is unresolved, not proof that
the importer inferred a rank or that the record denotes another organism.

The GTDB species name is not an exact name for strain MP. The mapping and
synonym issue is detailed under finding M1. The NCBI grounding itself is
not the wrong identity.

## Evidence

**Pinned NCBI identity.** Native `ncbi_names-0005.jsonl.gz` rows 27754-27756
contain exactly the two equivalent names and the scientific name on this
taxon. The ten lineage entries, including the species parent, agree with
the raw taxonomy chain. The scope entry is row 26048 of
`curation/seed_scope.tsv`, naming four sources. The embedded 2026-09-13 seed
event describes those same sources and does not claim human review.

**GTDB cluster, not strain identity.** Raw `gtdb_mappings.tsv` row 1205
supplies closeMatch and count 10. Native compressed GTDB catalogs contain
these exact terminal-cluster members:

| Genome accession | NCBI taxid | Source strain designation |
| --- | --- | --- |
| RS_GCF_015659015.1 | 230105 | SZUA-1124 |
| RS_GCF_030149465.1 | 230105 | BWSM_101 |
| RS_GCF_030159795.1 | 40223 | NBRC 102424 |
| RS_GCF_002335235.1 | 1946870 | UBA2012 |
| RS_GCF_042661685.1 | 40223 | NBRC 102424 |
| RS_GCF_000214595.1 | 1026882 | MP |
| RS_GCF_012963145.1 | 2024840 | UWMA-0155 |
| RS_GCF_048269145.1 | 230105 | ET25-06 |
| RS_GCF_036324325.1 | 40223 | IOM01 |
| GB_GCA_036155435.1 | 1977087 | XB_MAG545 |

Thus 10 is the cluster-wide count; one member has taxid 1026882. The MP
metadata link its RefSeq genome to GCA_000214595.2, SAMN02469574 and the
older aminisulfidivorans name. That older source taxonomy is retained as
provenance, not substituted for the current NCBI lineage.
The [live GTDB taxon page](https://gtdb.ecogenomic.org/taxon_search?s=al&q=s__Methylophaga%20thalassica)
could not be retrieved; the native snapshot supports the count and scope
comparison independently.

**BacDive boundary.** Both the exact native object and
[BacDive 134269](https://bacdive.dsmz.de/strain/134269) identify designation
MP, culture accessions JCM 14647, KCTC 12909 and the source's VKM values.
Its classification field is species taxid 40223, not strain taxid 1026882.
Its genome section separately points to MP's GCA_000214595, IMG 651324072
and BV-BRC 1026882.3. These different field roles explain why the target
has `strain_count: 0` despite relevant genome evidence existing elsewhere.

The raw strain rows and the parent species YAML retain BacDive 134269 and
its links. They are not absent from the repository. No culture identifiers
were transferred to this target by matching the bare designation MP, and
no equivalence between all genomes co-occurring on a BacDive page is implied.

**GOLD.** `gold_organisms.tsv` row 326 has count 1. A complete native-organism
scan also found exactly one directly classified object, Go0011120, carrying
taxid 1026882, KCTC 12909 and the older MP name. Native Gp0011120 explicitly
links that organism to PRJNA66315 and SAMN02469574. Ga0029400 explicitly links
the project to unversioned GCA_000214595 and IMG 651324072. These corroborate
the attestation and the existing parent-record links; they do not authorize
fabricating a strain entry in this record.

**Assembly-version context.** Native current NCBI assembly summaries carry
GCA_000214595.2 and GCF_000214595.1 under the current name and species 40223.
The historical summary marks GCA_000214595.1 suppressed. The distinction
matters for any later link curation: source-unversioned GCA_000214595 must
not be silently expanded to the suppressed version. No assembly accession
is asserted in the reviewed YAML itself.

**Nomenclature context.** The current
[LPSN thalassica page](https://lpsn.dsmz.de/species/methylophaga-thalassica)
describes a species, with a type distinct from MP. The
[aminisulfidivorans page](https://lpsn.dsmz.de/species/methylophaga-aminisulfidivorans)
lists MP/JCM 14647/KCTC 12909 as its type and records the later heterotypic
synonym relationship to thalassica. This supports preserving strain
distinctions even when species classifications change. Neither species-level
LPSN record is directly mapped to this strain in the inspected inventory.

**Other assertions.** `madin_taxa.tsv` row 503 reproduces the count of three
trait assertions. No individual phenotype is asserted in this YAML; this
is a source-inventory count, not three experimentally established traits.
The NCBI attestation is one name. Counts across these sources are not summed.

## Completeness

No required causal graph, definition or record-level evidence slot is
missing. The record relies on source attestations, as permitted for seeded
records. No gene, expression module or mechanism claim makes iModulonDB
applicable here.

The search for target identifier, current label, old MP/SK1 names and slug
included ignored files in `data/raw/`, `curation/` and `history/`. Native
compressed NCBI and GTDB catalogs and relevant GOLD/BacDive objects were
also inspected without gitignore filtering. Exact report filenames were
checked independently of gitignore; none existed before this report.
No repository-wide absence of genome evidence is claimed.

The rank discrepancy needs a pinned-node replay. It does not justify
altering the generated YAML based on a potentially differently dated web
page. Original taxdump replay and live GTDB verification remain unavailable.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **M1 - Major: a GTDB species classification is promoted to strain identity.**
   The species-wide closeMatch is used to emit `Methylophaga thalassica` as
   an `EXACT_SYNONYM` and the GTDB species as an identity xref for strain MP.
   The ten-member native cluster includes distinct culture strains and six
   NCBI taxids. It cannot denote MP alone. The cluster-wide genome count is
   numerically correct but is not a count of MP genomes. The inherited
   species-to-strain closeMatch also needs an explicit scope review.

   Maintained owners: `src/taxonmech/seed.py` lines 438-474 currently treats
   every closeMatch as identity without checking strain/species scope and
   emits exact synonyms and xrefs; KG-Microbe owns the upstream mapping
   predicate. The consumed row is `data/raw/gtdb_mappings.tsv` row 1205,
   not a manually editable correction surface. Do not fix this by editing
   the generated YAML or by relabeling MP as the species.

## Recommended Edits

1. Add a tested rank/scope guard to GTDB identity promotion in the seeder.
   Retain the supported species-classification evidence, but suppress the
   species-derived exact synonym and identity promotion on this strain.
   Preserve both NCBI equivalent names.
2. Review the upstream strain-to-species mapping semantics in KG-Microbe.
   Use a documented classification relationship or appropriately directed
   broader mapping; do not mechanically substitute a predicate without
   checking its direction and intended contract.
3. Label any retained count explicitly as GTDB cluster membership, rather
   than implying ten genomes from MP. Keep the native count of ten.

No recommended change was performed in this read-only review.

## Follow-up Checks

- Add focused seeder regressions contrasting this strain with its species
  parent: classification retained, no species exact synonym on MP, NCBI
  aliases unchanged, cluster count clearly scoped.
- Re-extract and regenerate only under an authorized curation change, then
  run both record validators and `just verify-corpus` at its full scope.
- Recover the configured taxdump with its pinned checksum and inspect
  the original nodes row to resolve STRAIN versus browser no rank.
- Retry live GTDB verification; retain snapshot dates and historical
  assembly versions when investigating MP's older classification.

## Additional Notes

Schema success does not detect the identity-scope error. No source data,
record, history, mapping status, branch or GitHub state was mutated.
The strict validator wrote its normal report TSV. This timestamped Markdown
is the only manually authored artifact from this review.
