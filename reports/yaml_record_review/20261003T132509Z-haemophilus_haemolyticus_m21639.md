# YAML Record Review: Haemophilus haemolyticus M21639

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/haemophilus_haemolyticus_m21639.yaml`
- Started UTC: 2026-10-03T13:23:15Z
- Finished UTC: 2026-10-03T13:25:09Z
- Verdict: needs curation

## Target

Generated `TaxonRecord`, `NCBITaxon:1028806`, Haemophilus haemolyticus
M21639; rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:726`.
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read all 84 YAML lines: ten ancestors, one GTDB mapping, three synonyms,
one GTDB xref, code 11, zero BacDive strains, three source attestations
and one embedded seed event. No publication or causal graph is asserted.

Read-only review: only this report was manually written. No YAML, source
inventory, history, status or generated page was changed. Eukaryota was
excluded.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/haemophilus_haemolyticus_m21639.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/haemophilus_haemolyticus_m21639.yaml` | PASS; one file, zero errors. |
| Complete raw identity, lineage and NCBI synonym comparison | PASS; all ten ancestors, rank, parent, label, code and both NCBI aliases agree. |
| Complete BacDive subtree membership | PASS; target is its only subtree member; zero classified BacDive rows. |
| GTDB source census | All 19 native genome shards inspected for exact terminal species; five members, only one assigned to taxid 1028806. |
| Source-count and scope comparison | Counts agree with inventories; the species-to-strain interpretation is defective. |
| `just verify-corpus` | Not run: full-corpus reproduction check, not a focused record validator. |
| `just validate-history` | Not run: ignored-inclusive target search found no standalone history. Strict validation checked the embedded event. |
| Graph and generated products | No graph asserted; graph gate not applicable. Pages and exports were not audited. |

Live NCBI Taxonomy, BioSample and BioProject pages were inspected. GTDB
search and genome pages were inaccessible through the web tool; the
committed RS232 native catalog supplies the bounded classification check.
Publication bodies and sequence payloads were not reassessed.

## Identity and Grounding

The [current NCBI summary](https://www.ncbi.nlm.nih.gov/taxonomy/1028806)
identifies M21639 as a strain. The
[legacy taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1028806&lvl=3&mode=node)
confirms the identifier, label, two equivalent strain names, lineage and
code 11, but displays `no rank`. Preserve this interface discrepancy;
the current summary and pinned inventory support `STRAIN`.

`data/raw/ncbitaxon_taxa.tsv:219211` matches the identity. Complete native
name objects at `data/catalog/ncbi_names-0005.jsonl.gz:28273` onward contain
one scientific name and two equivalent names. Both NCBI aliases retain
M21639 scope. In contrast, the GTDB exact synonym at YAML line 52 and xref
at line 57 denote a species cluster, not this strain.

## Evidence

**Source counts and audit.** `data/raw/madin_taxa.tsv:538` supports one
trait assertion, without asserting an unspecified phenotype. NCBI's count
of one is the scientific-name attestation, not a count of all names.
`curation/seed_scope.tsv:36104` agrees with the three-source selection.
The embedded seed event is dated 2026-09-13T17:54:04Z; the NCBI attestation
explicitly names the 2026-09-13 taxonomy snapshot.

**GTDB membership supports classification, not equivalence.**
`data/raw/gtdb_mappings.tsv:1243` supplies the target `skos:closeMatch`
and five-genome count. `data/raw/gtdb_species.tsv:72342` independently
contains that species count. The same mapping inventory also connects the
cluster to NCBITaxon:123834 with closeMatch at line 13692 and to
NCBITaxon:726 with broadMatch at line 305320. These are source assertions,
not a proof that all three NCBI concepts are identical.

Read all five complete native objects selected by the exact terminal
classification `s__Haemophilus quentini` across every GTDB genome shard:

| Native object in `data/catalog/` | Genome | Strain | NCBI taxid |
| --- | --- | --- | --- |
| `gtdb_genomes-0000.jsonl.gz:6369` | RS_GCF_013401805.1 | S32F2 | 726 |
| `gtdb_genomes-0001.jsonl.gz:30614` | GB_GCA_000222085.2 | M21639 | 1028806 |
| `gtdb_genomes-0001.jsonl.gz:38584` | RS_GCF_001702075.1 | MP1 | 123834 |
| `gtdb_genomes-0004.jsonl.gz:14421` | GB_GCA_001752465.1 | K068, representative | 123834 |
| `gtdb_genomes-0006.jsonl.gz:3950` | RS_GCF_001752475.1 | C860 | 123834 |

The five-genome count is correct for the cluster and must not be changed
to one as a repair. The target assembly's placement is supported; neither
cluster membership nor the raw closeMatch makes the species name an exact
alias for M21639. GTDB's Enterobacterales placement also differs from the
NCBI Pasteurellales lineage; the repository carries these classifications
separately and must not rewrite the NCBI ancestor chain.

The catalog manifest describes RS232. Attempts to inspect live
[GTDB search](https://gtdb.ecogenomic.org/searches?s=al&q=Haemophilus%20quentini)
and the [target genome page](https://gtdb.ecogenomic.org/genome?gid=GCA_000222085.2)
failed; no live-release equivalence claim is made.

**Native genome context.** Complete relevant source objects read:

| Source object | Checked evidence |
| --- | --- |
| `data/catalog/ncbi_genbank-0000.jsonl.gz:3845` | GCA_000222085.2, latest, Contig, 53 contigs, 2,328,161 bp, M21639, taxid 1028806, SAMN02952887, PRJNA66579 and AFQR00000000.1. |
| `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:1161` | GCA_000222085.1 suppressed, source not-live date 2012-01-29. |
| `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:1096` | GCF_000222085.1 suppressed, not-live date 2018-09-12, paired GCA_000222085.2, same sample, project PRJNA224116. |
| `data/bvbrc/bvbrc-0000.jsonl.gz:2995` | Genome 1028806.3, WGS, GCA_000222085.2, SAMN02952887, PRJNA66579 and AFQR00000000. |
| `data/gold/organisms.jsonl.gz:10577` | Go0012010, M21639, taxid 1028806; culture-collection field empty. |
| `data/gold/projects.jsonl.gz:10435` | Gp0012010 links Go0012010 to PRJNA66579 and SAMN02952887. |
| `data/gold/analyses.jsonl.gz:8818` | Ga0015258 links Gp0012010, IMG 2534681808 and unversioned GCA_000222085; isolate genome analysis. |

GenBank and historical RefSeq metadata report `genome length too large`
as the RefSeq exclusion reason. Do not turn the historical paired RefSeq
accession into a current assembly. A decompressed, ignored-inclusive
search across every current RefSeq shard using the taxid field, strain,
sample and assembly stem found no target match. Numeric genome-length
coincidences found by an initial broad search were not treated as taxid
matches.

The [BioSample page](https://www.ncbi.nlm.nih.gov/biosample/SAMN02952887)
confirms M21639, its WGS accession and PRJNA66579. The
[BioProject page](https://www.ncbi.nlm.nih.gov/bioproject/66579)
explicitly connects the target taxid, sample and GCA_000222085.2 at contig
level, and links GOLD Gp0012010 and IMG 2534681808. Its generic clinical
background was not converted into a strain-specific phenotype. The
project names the genome study identified by PMID 21952546 in native
GenBank metadata; its body was not used to infer additional claims.

## Completeness

Identity, NCBI lineage, code, strain-scoped NCBI synonyms and source counts
are supported. No other consequential required-field omission was found.
Zero BacDive strains means no classified BacDive entry in this subtree,
not that M21639 has no genome or has never been cultured.

Ignored-inclusive identifier, label, slug, strain-token, sample and
assembly-stem searches covered `history/`, `data/bacdive/`, `data/atb/`
and `data/straininfo/`, including compressed files. No target standalone
history, BacDive record or overlay match was found in those locations.
Ignored-inclusive searches of raw inventories found no target LPSN name
or GOLD taxon-count row. These are bounded local results, not worldwide
absence claims or a census of external collection catalogs.

The positive native GOLD workbook chain uses a different provenance route
from `data/raw/gold_organisms.tsv`, as documented in
`docs/HARMONIZATION.md`. Its empty culture field supplies no eligible
deposit join. Native GTDB's bare M21639 strain designation likewise does
not establish a registered culture accession. Under the current model,
these native genomes cannot justify inventing a BacDive strain entry.

No explicit trait, gene, regulator, transcriptomic dataset or causal graph
is asserted. iModulonDB and graph checks are not applicable. The absence
of optional nomenclature, publications or graph content is not a finding.

## Findings

**Major M1: species-cluster membership is promoted to exact strain identity.**
YAML lines 52-57 assert Haemophilus quentini and its GTDB species ID as
an exact synonym and equivalent identifier of M21639. The five native
cluster members include four other strain designations and two other
NCBI taxids. This contradicts the true-equivalence requirement at
`src/taxonmech/schema/taxonmech.yaml:180`. The source closeMatch at YAML
lines 43 and 70 does not establish same-species scope on a strain record.

The maintained local owner is `src/taxonmech/seed.py:451`: its identity
test accepts closeMatch without checking taxonomic scope, then writes
the xref and exact synonym at lines 467-469. The upstream predicate is
carried by `src/taxonmech/extract.py:519`; source mapping semantics need
review in kg-microbe as well. This is one connected major finding, not
separate counts for each generated manifestation.

Blocker: 0. Major: 1. Minor: 0.

## Recommended Edits

1. In `src/taxonmech/seed.py`, require defensible matching scope before
   promoting a GTDB species mapping into an exact synonym or xref.
   Preserve the evidenced species classification and its count separately.
2. Review the source predicate policy upstream in kg-microbe and document
   the accepted rank-aware interpretation in `docs/HARMONIZATION.md`.
   Do not guess a replacement mapping direction or patch raw inventories.
3. Add regression tests covering strain, subspecies and unranked
   below-species targets, singleton and multi-genome clusters, and genuine
   same-scope species equivalences. Regenerate only in a separately
   authorized curation change, never by hand-editing this YAML.

## Follow-up Checks

Run focused seeder tests and both target validators after an authorized
fix. A dry `just seed` and `just seed-canary NCBITaxon:1028806` should
show the exact identity claims removed or correctly constrained while
retaining the five-genome cluster count, NCBI identity and strain aliases.
Inspect the canary before a bulk write, then run full `just verify-corpus`.

Recheck the GTDB authority page when accessible, preserving the distinction
between the pinned release and a live refresh. Preserve current versus
historical NCBI statuses and accession versions in any future genome-link
expansion. None of these follow-ups was executed as a curation change.

## Additional Notes

The complete target was reviewed without sampling. No human-review
status or history event was added. Passing schema checks do not resolve
M1, and this report does not certify other records or full-corpus review
completion. All absence claims above name their local search boundaries.
