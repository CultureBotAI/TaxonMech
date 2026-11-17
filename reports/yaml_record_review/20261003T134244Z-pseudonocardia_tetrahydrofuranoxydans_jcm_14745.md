# YAML Record Review: Pseudonocardia tetrahydrofuranoxydans JCM 14745

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudonocardia_tetrahydrofuranoxydans_jcm_14745.yaml`
- Started UTC: 2026-10-03T13:39:36Z
- Finished UTC: 2026-10-03T13:42:44Z
- Verdict: pass

## Target

- Class `TaxonRecord`; identifier `NCBITaxon:1303679`; label
  Pseudonocardia tetrahydrofuranoxydans JCM 14745; rank `STRAIN`;
  domain `BACTERIA`; parent species `NCBITaxon:102884`.
- Read all 681 YAML lines. Grounding is `EXACT`; mapping status is `SEEDED`.
- Generated from maintained inventories by `src/taxonmech/seed.py`.
  The only manual write for this review is this new report.
- One directly classified BacDive strain, `bacdive:13395`, designation K1,
  carries four deposits, seven assembly assertions, six other genome
  assertions, and 32 related-record assertions.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudonocardia_tetrahydrofuranoxydans_jcm_14745.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudonocardia_tetrahydrofuranoxydans_jcm_14745.yaml`:
  PASS; one file scanned, zero errors. The standard diagnostic output is
  `reports/instance_validation_failures.tsv`.
- Structured identity, all ten ancestors, parent-chain order, genetic code,
  empty synonym inventory, complete subtree, BacDive count and deposits: PASS.
- Exact multiset comparisons of all populated fields for all 45 link
  assertions against raw and StrainInfo inventories: PASS. Nested serialized
  StrainInfo evidence was parsed before comparison.
- All four culture CURIEs and each explicit source-field match passed the
  repository's CAFI-aware `culture_curie_key` and normalization checks.
- All thirteen StrainInfo assertions passed native own-deposit, source status,
  relation, DOI, and sequence-to-deposit checks.
- An initial ad hoc taxonomy check used incorrect inventory column names and
  stopped with `KeyError`; it made no changes. The corrected check used the
  inspected headers (`taxon_id`, `parent_id`, `taxon_ids`) and passed.
- `just verify-corpus`: Not checked; the documented command is full-corpus,
  not a focused record validator. No corpus reproduction claim is made.
- Standalone history validation was not run: no matching standalone entry
  was found in the ignored-inclusive search of `history/`. The embedded
  seed event passed strict schema validation.
- Causal-graph gates are not applicable; no graph is asserted. Generated
  pages, exports, and global product validation were not audited.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308105` and
`data/catalog/ncbi_names-0007.jsonl.gz:30641` support the exact taxon name.
All ten lineage entries match the complete raw inventory and its parent
chain. The target subtree contains only taxon 1303679.

The [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1303679)
agrees on name, identifier, lineage and genetic code 11 but displays
`no rank`. This source-surface disagreement was investigated rather than
silently harmonized: live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303679&retmode=xml)
returns `strain` and parent 102884, while
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303679)
returns `STRAIN` and exactly the ten lineage identifiers in the YAML.
Both structured authorities support the pinned rank. No rank edit is needed.

[JCM's own catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=14745)
connects JCM 14745 to CIP 109050, DSM 44239, CCUG 52126, K1, BacDive 13395,
and assembly GCA_001313405. The strain and species taxon remain distinct.
Neither a species-level LPSN xref nor an exact species-name synonym has been
promoted onto this strain record.

## Evidence

The following maintained rows were read and checked for this target:

| Input | Row or lines | Supported content |
| --- | --- | --- |
| `data/raw/ncbitaxon_taxa.tsv` | 308105 | Name, rank, parent, code, source list |
| `data/raw/bacdive_strains.tsv` | 13232 | Direct classification, K1, four deposits |
| `data/raw/mediadive_taxa.tsv` | 2809 | Three direct media: 553, 65, J57 |
| `data/raw/bactotraits_taxa.tsv` | 2275 | Sixteen direct trait assertions |
| `curation/seed_scope.tsv` | 22453 | Scope and four-source admission reason |
| `data/raw/strain_assemblies.tsv` | 33267-33272 | Six assembly provenance paths |
| `data/straininfo/assemblies.tsv` | 2543 | One deposit-specific assembly path |
| `data/raw/strain_genome_records.tsv` | 26129-26134 | Six IMG/BV-BRC paths |
| `data/raw/strain_related_records.tsv` | 89343-89362 | Twenty source relationships |
| `data/straininfo/related_records.tsv.gz` | 38424-38435 | Twelve deposit/strain/gene paths |

The complete native [BacDive](https://bacdive.dsmz.de/strain/13395) projection
at `data/bacdive/records.jsonl.gz:13231` supports source references 11614
and 66792, both NCBI classifications, the designation and deposits, and
the unversioned assembly, IMG and BV-BRC assertions. The live page agrees.
The raw strain medium count is zero; the separate taxon MediaDive count
is three. These inventories encode different relationships, not a claimed
absence of all growth-medium information.

The complete native GenBank row at
`data/catalog/ncbi_genbank-0000.jsonl.gz:49276` and BV-BRC row at
`data/bvbrc/bvbrc-0001.jsonl.gz:23804` agree on JCM 14745, taxon 1303679,
`GCA_001313405.1`, `PRJDB936`, and `SAMD00016936`.
GenBank identifies ASM131340v1 as contig-level; its fragmented-assembly
RefSeq exclusion and 1,947 contigs do not contradict a source-association
record that makes no complete/high-quality genome claim. BV-BRC retains
both its strain and culture-collection match routes to `patric:1303679.3`.
The external original GenBank download was not reread; the native catalog
projection and maintained source-reference metadata supply this audit.

All five relevant GOLD native objects were reread:

- `data/gold/organisms.jsonl.gz:55145`: `Go0094255`, JCM 14745.
- `data/gold/projects.jsonl.gz:55650`: `Gp0094255` explicitly names
  `Go0094255`, PRJDB936, and SAMD00016936.
- `data/gold/analyses.jsonl.gz:74790`: `Ga0128428` explicitly names
  `Gp0094255`, GCA_001313405.1, and IMG 2734481945. Its blank organism
  field does not introduce a conflicting assignment.
- `data/gold/organisms.jsonl.gz:24231` and `:439742` identify
  `Go0028501` (DSM 44239) and `Go0608774` (CIP 109050). Their retained
  assertions are organism relationships, not transferred JCM assemblies.

The live [BioProject result](https://www.ncbi.nlm.nih.gov/bioproject/?term=txid1303679%5BOrganism:noexp%5D)
links the assembly, sample, GOLD project, and IMG identifier to the JCM taxon.
The complete [SAMD00016936 page](https://www.ncbi.nlm.nih.gov/biosample/SAMD00016936)
explicitly supplies strain JCM 14745, culture collection JCM: 14745,
project PRJDB936, and species type-material context. This independently
verifies the sample association, not just its presence in multiple caches.

The complete native StrainInfo object at
`data/straininfo/records.jsonl.gz:79230` supports SI-ID113658 and its
version-3 DOI. Eligible deposit IDs are DSM 340748, CIP 690288,
CCUG 703098, and JCM 792172. All are available, in nondeprecated collections,
and have nonerroneous relations. The genome sequence explicitly names JCM
792172; the four partial-gene sequences explicitly name DSM 340748.
Every YAML sequence retains that exact deposit boundary.
[DataCite](https://api.datacite.org/dois/10.60712/si-id113658.3) independently
resolved the DOI to the findable version-3 StrainInfo record. This is a
source-record version identifier, not a publication or a deposit DOI.

Live [NCBI nucleotide XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=EU722544,EU722578,EU722600,EU722633&rettype=gb&retmode=xml)
verified EU722544.1/fusA (783 bp), EU722578.1/gyrB (1229 bp),
EU722600.1/lepA (966 bp), and EU722633.1/rpoB (798 bp), all partial
CDS records for DSM 44239 and taxon 102884. Source species classification
is retained on these assertions without replacing the taxon record's identity.
The unversioned YAML accessions preserve the asserting source's syntax.

The local claw adapter's `imodulondb datasets` command was attempted using
`uv run --no-sync --project .../culturebotai-claw kg-microbe-sources`.
Sandbox DNS failed, but an approved public read-only request to the official
[datasets API](https://imodulondb.org/api/datasets) succeeded. Its complete
20-organism response contained no Pseudonocardia dataset. iModulonDB is
not applicable; unrelated organisms' housekeeping-gene hits are not evidence.

## Completeness

- One strain matches the complete BacDive subtree census. Because it is filed
  directly under this record, omission of `classified_as` is correct.
- Counts and units agree: one NCBI name, one BacDive strain, three MediaDive
  media, and sixteen BactoTraits assertions. No cross-source total is implied.
- Seven assembly entries are provenance assertions over two accession strings;
  six genome-record entries refer to two database identifiers. These counts
  do not measure distinct biological genomes.
- No LPSN name maps directly to this strain in the searched inventory. The
  parent species owns name 780187 and its type designations. Under the
  documented same-taxon derivation, the optional `is_type_strain` flag is not
  emitted here; its absence does not assert that JCM 14745 is not type material.
  The live JCM, BacDive, and BioSample sources affirm the type context.
- GOLD workbook links do not require a GOLD KGX taxon attestation. The raw
  aggregate inventories contain GOLD and Madin rows for the parent species,
  not this strain; no species counts were incorrectly inherited.
- Ignored/hidden-inclusive compressed searches covered `data/catalog/`,
  `data/bvbrc/`, and `data/gold/` using the species name, assembly, sample,
  and four whole culture-deposit patterns. Matching files were the inspected
  NCBI name/GenBank, BV-BRC, and GOLD files. No matching native GTDB or
  RefSeq object was found in this bounded search.
- Ignored-inclusive searches of `history/`, `data/atb/`, and the complete
  compressed ATB catalog covered target ID/name/slug, BacDive ID, assembly,
  and both live project sample accessions. No target history or eligible
  ATB overlap was found. Numeric substring hits for unrelated Salmonella
  accessions were rejected after inspection.
- The additional live [sample SAMD00012248](https://www.ncbi.nlm.nih.gov/biosample/2731198)
  belongs to the same project but is distinct from SAMD00016936. Its ATB
  catalog row at `data/catalog/allthebacteria.tsv.xz:936` is `NOT_PROCESSED`,
  with no FASTA URL or assembly accession. It cannot supply an eligible ATB
  assembly, nor does project co-membership establish assembly equivalence.
- Optional phenotype and causal-graph fields are not required for this seeded
  taxon record. No unsupported phenotype or regulatory claim was added.

## Findings

None found: 0 blocker, 0 major, 0 minor findings for the YAML record.
The browser rank discrepancy is preserved above and resolved for this verdict
by two agreeing live structured NCBI authorities and the pinned inventory.

## Recommended Edits

None required to this record. Preserve the original accession versions,
source-field provenance, typed relationships, and deposit-scoped sequences.
Future source corrections belong in maintained `data/raw/` or
`data/straininfo/` inputs and their transforms, then `src/taxonmech/seed.py`,
not direct edits to the generated YAML.

## Follow-up Checks

- Rerun focused schema/strict validation and exact source/deposit comparisons
  after any relevant source refresh.
- Run `just verify-corpus` before claiming corpus-wide reproducibility.
- Keep future sample or ATB expansion tied to explicit deposit/source paths
  and availability; the unprocessed sample does not justify a genome link.
- Product rendering and the external original snapshot bytes remain outside
  this completed record audit.

## Additional Notes

Correction to the adjacent species report
`20261003T133741Z-pseudonocardia_tetrahydrofuranoxydans.md`: its completeness
statement that a target/child search found no MediaDive or BactoTraits rows
was inaccurate. That search tested bare numeric taxon fields, but those
inventories contain `NCBITaxon:` CURIEs. The corrected ignored-inclusive
search found the child rows at MediaDive line 2809 and BactoTraits line 2275;
there is no species-direct row in those two inventories. This report
supersedes that negative search statement. The species record's omission of
those child counts remains consistent with documented direct-only counting.
The earlier report is retained unchanged as an append-only review artifact.

No taxon YAML, maintained source, generated product, curation event, review
status, or GitHub object was modified. The seeded lifecycle state was retained.
