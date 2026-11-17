# YAML Record Review: Extensimonas vulgaris

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/extensimonas_vulgaris.yaml`
- Started UTC: 2026-10-03; exact start time not captured, source/validation checkpoint recorded at 08:12:03Z
- Finished UTC: 2026-10-03T08:18:33Z
- Verdict: pass with minor issues

## Target

The entire 1,109-line generated `TaxonRecord` was inspected. It denotes
`NCBITaxon:1031594`, Extensimonas vulgaris, rank `SPECIES`, domain `BACTERIA`.
Grounding is `EXACT`; mapping status remains `SEEDED`. The record contains one
LPSN name, one GTDB mapping, two related synonyms, one BacDive strain, eight
source attestations, and one seeding event. This is the deferred target at
`data/taxa/PATHS.tsv:13104`, not a new pass over Eukaryota.

The strain contains 19 assembly assertions, 16 other genome assertions
(including two AllTheBacteria records), and 42 related-record assertions.
These are evidence rows, not counts of distinct biological genomes.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/extensimonas_vulgaris.yaml` | Passed; no issues found. |
| `just validate-strict data/taxa/bacteria/extensimonas_vulgaris.yaml` | Passed; one file scanned, zero errors. `reports/instance_validation_failures.tsv` contains only its header. |
| Structured YAML/TSV/JSON comparisons using `.venv/bin/python` | All 19 assembly rows equal 18 raw inventory rows plus one StrainInfo overlay row. All 14 non-ATB genome rows equal the raw inventory. All 42 related rows equal 40 raw rows plus two StrainInfo rows, including nested evidence. Comparisons preserve multiplicity and omit only empty TSV fields and the containing strain key. |
| Read-only `taxonmech.atb.genome_records()` conversion | Both ATB rows exactly match the YAML, including six and seven sample-link assertions respectively. The two assembly metadata rows also match the inspected compressed native catalog rows. |
| Identity, lineage and source references | Manually checked against inventories, native snapshots and the source pages detailed below. No universal per-record external-accession validator is exposed by the documented recipes. |
| `just verify-corpus` | Not rerun in this review. This is a full-corpus reproduction check, not a focused validator; the row comparisons above are not a substitute or a claim that it passed now. |
| `just validate-products` | Not run: the documented OAK gate covers curator-added causal-graph nodes; this record has no causal graph. |
| `just validate-history` | Not run: the ignored-file-inclusive target search in `history/` found no matching history artifact. The embedded seeding event was inspected and covered by strict validation. No history was created or status promoted. |
| Full source-catalog hash/census validation and rendered-site checks | Not rerun. No source data, generator or page was changed. |
| Final target diff | `git diff --exit-code -- data/taxa/bacteria/extensimonas_vulgaris.yaml reports/instance_validation_failures.tsv` passed before report creation. |

An initial `uv run python` ad hoc comparison could not read the external uv
cache. The existing `.venv/bin/python` completed the comparisons. An initial
comparison used the wrong source enum and taxonomy column name; it was
corrected to `ALLTHEBACTERIA` and `taxon_id` before drawing conclusions.

## Identity and Grounding

The [NCBI taxon page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1031594)
supports the species identity, type-strain aliases, genetic code 11 and
displayed lineage. Each of the nine ancestor IDs, labels, ranks and parent
links agrees with `data/raw/ncbitaxon_taxa.tsv`, including the root and cellular
root entries. The parent is `NCBITaxon:1434001`, Extensimonas. The two synonyms
retain NCBI's related-synonym treatment rather than asserting exact equivalence.

[LPSN record 790859](https://lpsn.dsmz.de/species/extensimonas-vulgaris)
agrees on name, authority, species rank, valid publication, current-name status
and marker accession. The stored legitimacy flag comes from the pinned LPSN
API-derived status line; the public page was not treated as an independent
authenticated API check of that flag. See the minor designation gap below.

The GTDB species mapping and count of three agree with
`data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv` and three inspected
RS232 native genome rows. The `skos:closeMatch` predicate preserves a separate
taxonomy assertion. GTDB's Gammaproteobacteria/Burkholderiaceae_C classification
differs from the NCBI lineage; it was not substituted into the NCBI lineage or
treated as proof of exact taxonomic equivalence. The live GTDB page could not
be retrieved.

## Evidence

| Claim group | Inspected support and scope |
| --- | --- |
| Nomenclature and literature | `data/raw/lpsn_names.tsv:27770` contains the name, status, publications and `INSDC:HQ596491`. The [original article](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.038158-0) identifies S4 as the type strain and explicitly relates CGMCC 1.10977 and JCM 17803. The [notification article](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.055343-0) resolves with the expected bibliographic identity; its full list was not independently inspected. LPSN associates that list with this name. NCBI and BacDive link PMID:23064351 to the original description, but direct PubMed content was unavailable. |
| Strain identity and deposits | `data/raw/bacdive_strains.tsv:53572`, the native `data/bacdive/records.jsonl.gz` entry, and [BacDive 131261](https://bacdive.dsmz.de/strain/131261) support S4, the species ID and all three culture deposits. [DSM 100911](https://www.dsmz.de/collection/catalogue/details/culture/DSM-100911) and [JCM 17803](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=17803) independently support the deposit relationships and type status. |
| Direct BacDive sequences | The native entry explicitly supplies unversioned GCA_003337425, GCA_007830535 and GCA_007996985, BV-BRC 1031594.3/.4/.5, and IMG 2770939495/2596583579. Source reference IDs 67770 and 66792 and their field placement agree with the record. Its 16S entry identifies HQ596491 as the S4 marker; that marker is not promoted to a genome assembly. |
| GTDB and NCBI assemblies | Native `data/catalog/gtdb_genomes-*.jsonl.gz`, `ncbi_genbank-*.jsonl.gz` and `ncbi_refseq-*.jsonl.gz` rows support the versioned 003337425.1/007830535.1 accessions, exact DSM/CGMCC deposit fields, assembly names and levels, BioSamples and BioProjects. The third GTDB genome is RS_GCF_007996985.1 with bare designation S4. Its contribution to the species count does not authorize a culture-deposit join. |
| BV-BRC | Three native `data/bvbrc/bvbrc-*.jsonl.gz` rows were inspected. DSM 100911 and CGMCC 1.10977 provide explicit deposit evidence for the attached rows. The separate S4 row is not used to infer an additional deposit-based association. |
| GOLD | Native organism, project and analysis JSONL rows establish Go0093898 -> Gp0093898 -> Ga0040927 for CGMCC and Go0402697 -> Gp0290596 -> Ga0244581 for DSM. The analyses explicitly supply the assembly and IMG accessions. Go0619564 supplies the JCM organism relation. Go0711997 is a fourth species-attested organism but has only bare designation S4, so it does not supply an inferred deposit-based link. |
| StrainInfo | The complete native SI-ID 406481 entry in `data/straininfo/records.jsonl.gz` supports its DOI version `10.60712/SI-ID406481.3`, BacDive and taxon references, published status, available own deposit SI-DP 913787 (DSM 100911), and GCA_003337425 sequence attached to that same deposit. The YAML preserves strain, deposit and sequence-deposit roles separately; related designations CGMCC/JCM are not treated as own deposits. |
| AllTheBacteria | Native `data/catalog/allthebacteria.tsv.xz:1058605` and `:1397225`, the two `data/atb/assemblies.tsv` rows, and `data/atb/strain_links.tsv` support release 2025-05 records for SAMN02927936 and SAMN09074687. Runs SRR4128928/SRR7174984, ENA analyses ERZ3988558/ERZ26866085, sequence checksums, filters, dataset, archive and download URLs agree. These remain sample-derived ATB assemblies, not equivalence assertions to every assembly on the strain. |

The two attached BioSamples are supported separately by BV-BRC, GOLD, GTDB
and NCBI metadata. PRJNA255578 and PRJNA463372 are the source projects;
PRJNA224116 remains the explicitly reported RefSeq project, not a newly inferred
strain-specific project. The 13 nested ATB sample assertions preserve these
source distinctions and match the maintained inventory.

All eight attestations match their inventory counts and units: NCBI 1 name,
LPSN 1 name, GTDB 3 genomes, BacDive 1 strain, MediaDive 2 media, GOLD 4
organisms, Madin 10 trait assertions and BactoTraits 25 trait assertions.
The relevant inventory files are `ncbitaxon_taxa.tsv`, `lpsn_names.tsv`,
`gtdb_mappings.tsv`, `bacdive_strains.tsv`, `mediadive_taxa.tsv`,
`gold_organisms.tsv`, `madin_taxa.tsv` and `bactotraits_taxa.tsv` under
`data/raw/`. Counts are not summed into a biological evidence score. The trait
attestations do not assert particular phenotypes; underlying trait studies were
not newly reviewed. MediaDive's species count does not imply a nonzero
strain-level `medium_count` in the source inventory.

## Completeness

The one-strain listing is complete for its maintained BacDive inventory row.
Assembly and related-record lists preserve all attached inventory assertions;
repeated identifiers with distinct source fields are provenance, not erroneous
biological duplicates. Missing deposit-based links for bare S4 source rows are
consistent with `docs/STRAIN_GENOMES.md`, not evidence that S4 lacks a genome.
No phenotype expansion or causal graph is required for this seeded taxon.

The consequential bounded gap is the LPSN-specific CGMCC designation in the
next section. S4 itself is a local designation, not a culture-collection CURIE.

Searches included ignored and hidden files. Identifier, label and slug were
searched in `history/` and `curation/`; the seed-scope and legacy-page rows
were found, with no target history match. The target stem was searched among
all review-report filenames before writing; no previous report was found.
Target identifiers, label, slug, BacDive/StrainInfo keys and both sample IDs
were searched in the ATB and StrainInfo exclusion TSVs with no matching row.
These are bounded results, not claims about every file or external database.
Compressed native catalogs were decompressed for inspection, not searched as
opaque binary files.

## Findings

- **Blocker:** None found within the checked scope.
- **Major:** None found within the checked scope.
- **Minor (1): Incomplete LPSN type-strain designation list.** The YAML at
  `nomenclature[0].type_strain_designations` contains DSM-100911 and JCM-17803
  but omits `kgmicrobe.strain:CGMCC-1.10977`. The inspected LPSN page and
  original description both support the CGMCC designation. The BacDive strain
  already retains it, so this is a bounded provenance/completeness gap, not
  wrong strain identity. `data/raw/lpsn_names.tsv` has the same omission;
  therefore the seeder faithfully reproduces the current inventory. The
  correction belongs to the maintained kg-microbe LPSN source/transform feeding
  that inventory, with `src/taxonmech/extract.py:extract_lpsn` as the local
  extraction boundary. The configured upstream transform paths were unavailable
  at inspection, so the exact upstream implementation cause and module were
  not established. Do not patch the generated YAML or invent a source edge.

## Recommended Edits

1. Reconcile LPSN record 790859 against the pinned kg-microbe LPSN transform
   inputs named in `data/raw/MANIFEST.yaml`. Confirm why the supported CGMCC
   culture identifier is omitted, then correct or refresh the maintained
   upstream input/transform. Inspect `src/taxonmech/extract.py:extract_lpsn`
   if the corrected source edge still fails to reach `type_strain_ids`.
2. In a separately authorized curation change, re-extract the inventory and
   regenerate this record through the normal seeder. Add a focused extraction
   regression test if transformation logic is the cause. Preserve all three
   registered deposits, retain S4 as a designation, and leave the evidence
   roles and taxonomy mapping predicates intact.

No data edits, regeneration, history event or review-status promotion were
performed by this review.

## Follow-up Checks

- Inspect the original LPSN source edge(s) and compare them to
  `data/raw/lpsn_names.tsv` before choosing the correction layer. The manifest
  attributes extraction to `kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd`;
  the current public page is additional evidence, not a byte-identical replay
  of that upstream snapshot.
- After an authorized input correction, use `just extract-inventory-dry`,
  the normal extraction workflow and
  `just seed-canary NCBITaxon:1031594`; confirm that the LPSN list now includes
  CGMCC-1.10977 without losing the existing deposits.
- Run `just validate data/taxa/bacteria/extensimonas_vulgaris.yaml`,
  `just validate-strict data/taxa/bacteria/extensimonas_vulgaris.yaml` and
  the full `just verify-corpus` after regeneration. Run relevant extraction
  tests for any code change. Validate any new curation-history artifact in
  that later change, not by creating one in this read-only review.
- Retry live GTDB, StrainInfo/DOI, PubMed and INSDC accession resolution when
  those endpoints are accessible. Snapshot-supported claims remain distinct
  from successful live authority checks.

## Additional Notes

Live NCBI Taxonomy was accessible through the source link despite direct-open
failures. GTDB requests failed; StrainInfo's page exposed only its JavaScript
shell and its API/DOI requests failed; PubMed and direct nucleotide access
did not expose usable records. NCBI Datasets exposed only a page shell for
GCA_007996985.1. These were not counted as successful content checks.
Native committed snapshots provided the genome and StrainInfo evidence above.
Live GOLD, BV-BRC and ATB archive payloads were not independently fetched;
genome FASTAs were not downloaded and source checksums were not recalculated
from live sequence data. Complete catalog hashes were not revalidated.

iModulonDB is not applicable: this record makes no gene, regulator or
transcriptomic-module claim. The absence of that check is not biological
negative evidence. No provider credits, GitHub mutations or external messages
were used.
