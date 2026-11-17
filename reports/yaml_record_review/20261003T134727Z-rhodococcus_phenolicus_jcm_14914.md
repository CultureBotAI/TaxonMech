# YAML Record Review: Rhodococcus phenolicus JCM 14914

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhodococcus_phenolicus_jcm_14914.yaml`
- Started UTC: 2026-10-03T13:44:09Z
- Finished UTC: 2026-10-03T13:47:27Z
- Verdict: pass

## Target

- Class `TaxonRecord`; identifier `NCBITaxon:1303680`; rank `STRAIN`;
  domain `BACTERIA`; parent species `NCBITaxon:263849`.
- Read all 1,157 YAML lines, rereading the middle section after initial tool
  output truncation. Grounding is `EXACT`; mapping status is `SEEDED`.
- One directly classified strain, `bacdive:11042`, designation G2P, has four
  deposits, 17 assembly assertions, 13 other genome assertions, and 56
  related-record assertions. All 86 assertions were reviewed.
- This is generated YAML owned by maintained inventories and
  `src/taxonmech/seed.py`. Only this new review report was manually written.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/rhodococcus_phenolicus_jcm_14914.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/rhodococcus_phenolicus_jcm_14914.yaml`:
  PASS; one file scanned, zero errors. The command writes the normal
  `reports/instance_validation_failures.tsv` diagnostic.
- Structured checks of identity, rank, parent, code, all ten ancestors,
  root-first parent-chain order, empty synonyms, complete target subtree,
  BacDive count and deposits: PASS.
- Exact multiset comparisons of every populated field in all 86 assertions
  against the raw and StrainInfo inventories: PASS. Nested evidence JSON was
  parsed before comparison, not compared as an opaque string.
- All four culture identifiers and every explicit source-field match passed
  the repository's CAFI-aware culture-key and normalization helpers.
- All eighteen StrainInfo assertions passed native deposit eligibility,
  relation/status, record DOI, and exact sequence-deposit checks.
- `just verify-corpus`: Not checked; it is full-corpus-only, not a documented
  focused validator. No corpus-wide reproduction claim is made.
- Standalone history validation was not applicable to a matching external
  history entry: none was found in the ignored-inclusive search of `history/`.
  The embedded seed event passed strict validation.
- No causal graph is asserted, so graph-specific gates are not applicable.
  Generated pages, exports, and global product validation were not audited.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308106` identifies the target strain;
`:53951` identifies its parent species. The native scientific-name object
at `data/catalog/ncbi_names-0007.jsonl.gz:30642` agrees. The complete target
subtree contains only taxon 1303680, and its ten ancestors match the YAML.

The live [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1303680)
agrees on identity, lineage and genetic code 11, but displays `no rank`.
Approved read-only requests to [Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303680&retmode=xml)
and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303680)
returned `strain`/`STRAIN`, parent 263849, and the exact ten lineage IDs.
This preserves the browser/API discrepancy while supporting the pinned
strain rank; no YAML rank change is indicated.

[JCM's catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=14914)
supports G2P and the JCM 14914, DSM 44812, CIP 109148, and NRRL B-24323
deposit relationships. [LPSN](https://lpsn.dsmz.de/species/rhodococcus-phenolicus)
places name 780465 and its type designations at species level. It also
documents historical NRRL-number typographical errors; the YAML retains
the supported B-24323 accession, not an erroneous number from older prose.
No species-level LPSN name or GTDB species xref is incorrectly promoted
onto the strain record.

## Evidence

Maintained evidence was checked at these locations:

| Input | Row or lines | Verified scope |
| --- | --- | --- |
| `data/raw/bacdive_strains.tsv` | 10896 | G2P, direct classification, four deposits |
| `data/raw/mediadive_taxa.tsv` | 2810 | Two direct media: 535 and J43 |
| `data/raw/bactotraits_taxa.tsv` | 2276 | One direct trait assertion |
| `curation/seed_scope.tsv` | 22454 | Four-source admission reason |
| `data/raw/strain_assemblies.tsv` | 3461-3475 | Fifteen source assembly paths |
| `data/straininfo/assemblies.tsv` | 398-399 | Two deposit-specific assembly paths |
| `data/raw/strain_genome_records.tsv` | 2704-2716 | Thirteen non-NCBI genome paths |
| `data/raw/strain_related_records.tsv` | 10645-10684 | Forty source relationships |
| `data/straininfo/related_records.tsv.gz` | 7890-7905 | Sixteen deposit/strain/sequence paths |

The complete native BacDive object at `data/bacdive/records.jsonl.gz:10895`
and the inspected [BacDive page](https://bacdive.dsmz.de/strain/11042) support
the source strain and four deposits. Genome reference 66792 supplies the
JCM contig assembly, IMG 2675903364, and BV-BRC 1303680.3; reference 67770
supplies the DSM scaffold assembly, IMG 2744054614, and BV-BRC 263849.4.
The separate source references and classifications are preserved.

Complete native genome objects establish two distinct deposit paths:

- JCM: `data/catalog/ncbi_genbank-0000.jsonl.gz:49277` and
  `data/bvbrc/bvbrc-0001.jsonl.gz:23805` support GCA_001313425.1,
  ASM131342v1, taxon 1303680, PRJDB937, SAMD00016937, and
  WGS BBFV00000000.1 (unversioned in BV-BRC).
- DSM: `data/catalog/ncbi_genbank-0001.jsonl.gz:13852`,
  `data/catalog/ncbi_refseq-0001.jsonl.gz:3448`, and
  `data/bvbrc/bvbrc-0015.jsonl.gz:3940` support GCA_001646785.1 /
  GCF_001646785.1, ASM164678v1, taxon 263849, and SAMN04357313.
  GenBank/BV-BRC name PRJNA306614; RefSeq names PRJNA224116.
  The NCBI rows explicitly pair the DSM assemblies. No such pairing is
  inferred between the JCM and DSM assemblies.

The native GTDB object at `data/catalog/gtdb_genomes-0011.jsonl.gz:11451`
supports `gtdb.genome:RS_GCF_001646785.1`, the whole DSM 44812 culture
identifier, both NCBI assembly identifiers, sample, and RefSeq project.
Its GTDB family is Mycobacteriaceae while its NCBI family is Nocardiaceae;
the YAML correctly retains the NCBI lineage instead of harmonizing them.
The live GTDB genome page could not be retrieved. Verification of the
GTDB-specific assertions therefore rests on the complete pinned native row,
not a claim about today's live GTDB release.

Native GOLD objects preserve separate organism/project/analysis chains:

| Deposit | Organism | Project | Analysis | NCBI assembly / IMG |
| --- | --- | --- | --- | --- |
| JCM 14914 | Go0094256 | Gp0094256 | Ga0128429 | GCA_001313425.1 / 2675903364 |
| DSM 44812 | Go0026060 | Gp0150351 | Ga0132898 | GCA_001646785.1 / 2744054614 |

The organism rows are `data/gold/organisms.jsonl.gz:55146` and `:22076`;
project rows are `data/gold/projects.jsonl.gz:55651` and `:95399`;
analysis rows are `data/gold/analyses.jsonl.gz:74791` and `:78911`.
Both analyses name their respective project explicitly. Their blank
analysis-level organism fields do not conflict with those project chains.
`Go0607082` (CIP; organism line 438066) and `Go0607084` (NRRL; line 438068)
remain typed organism relationships. `Go0607083` (line 438067) supplies only
bare G2P and no culture-collection identifier; it correctly supplies no join.

The live [JCM BioProject result](https://www.ncbi.nlm.nih.gov/bioproject/?term=txid1303680%5BOrganism:noexp%5D)
and [SAMD00016937 page](https://www.ncbi.nlm.nih.gov/biosample/SAMD00016937)
independently verify the JCM assembly, sample, deposit, project, GOLD project
and IMG relationships. Official [BioSample EFetch XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=4151249,4357313&retmode=xml)
also verifies SAMN04357313 as DSM 44812, with culture collection DSM:44812
and species taxon 263849.

Official [PRJNA306614 XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=306614&retmode=xml)
identifies a multispecies Rhodococcus sequencing project and explicitly
pairs GCA_001646785 with SAMN04357313 in a locus-tag entry. The live
[PRJNA224116 page](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA224116)
identifies NCBI's RefSeq annotation project. Their differing project IDs
are supported source context, not a wrong-strain association. Failed web
requests for the DSM sample/project were resolved by these XML requests.

The complete native StrainInfo object at
`data/straininfo/records.jsonl.gz:225808` supports SI-ID291003,
BacDive 11042, and DOI 10.60712/SI-ID291003.3. Its deposits are
DSM 677526, NRRL 677528, CIP 690685, and JCM 801692. All are available,
belong to nondeprecated collections, and have nonerroneous relations.
The JCM assembly names deposit 801692; the DSM assembly and all eight
nucleotide sequences name deposit 677526. No sequence transfers through
shared strain grouping. [DataCite](https://api.datacite.org/dois/10.60712/si-id291003.3)
independently confirms the findable version-3 strain-record DOI.

Official [NCBI nucleotide XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AM933579,KF410354,KF410390,KF410426,KF410462,KF410498,KF410534,KF410570&rettype=gb&retmode=xml)
was fetched and parsed for every asserted nucleotide reference:

| Resolved accession | Identity | Length |
| --- | --- | --- |
| AM933579.1 | Partial 16S rRNA | 1511 bp |
| KF410354.1 | Partial 16S rRNA | 1379 bp |
| KF410390.1 | rpsA, partial CDS | 888 bp |
| KF410426.1 | pnp, partial CDS | 840 bp |
| KF410462.1 | purF, partial CDS | 660 bp |
| KF410498.1 | purL, partial CDS | 1278 bp |
| KF410534.1 | rpoC, partial CDS | 1419 bp |
| KF410570.1 | secY, partial CDS | 666 bp |

All eight source features identify DSM 44812 and species taxon 263849.
The YAML correctly preserves unversioned asserting-source accessions.
The source category `rrnaop` is retained for the two partial 16S references;
the record names do not claim complete operons or genomes.

The same-session structured-source coverage check resolved the local claw
runner and attempted `kg-microbe-sources imodulondb datasets`; sandbox DNS
failed. An approved request to the official
[datasets API](https://imodulondb.org/api/datasets) succeeded and its complete
20-organism list contained no Rhodococcus dataset. iModulonDB is not
applicable; that absence is not evidence against these gene annotations.

## Completeness

- The full target subtree yields exactly one BacDive strain. All four
  culture deposits are retained, and `classified_as` is correctly omitted
  for a strain directly classified under the target.
- Attestations agree with the inventories: one NCBI name, one BacDive strain,
  two MediaDive media, and one BactoTraits assertion. The raw per-strain
  medium count is zero; it is distinct from the taxon-level medium count.
- LPSN, GTDB species mapping, GOLD aggregate, and Madin aggregate rows were
  found for the parent species, not this strain. Their absence as strain-level
  nomenclature, equivalence, or source counts is correct under the model.
  Optional `is_type_strain` follows same-taxon LPSN derivation; its omission
  here does not negate the source-supported species type-material context.
- Seventeen assembly assertions contain five distinct source accession strings;
  thirteen other genome assertions contain five distinct database identifiers.
  Neither count denotes independent biological genomes.
- Ignored/hidden-inclusive compressed searches of `data/catalog/`,
  `data/bvbrc/`, and `data/gold/` covered the species, assemblies, GOLD IDs,
  and all four whole culture-deposit patterns. Matches were the inspected
  native objects; no additional matching historical assembly was found.
- Ignored-inclusive searches of `history/`, `data/atb/`, and the complete
  compressed ATB catalog covered the taxon ID/name/slug, BacDive ID, assemblies,
  and asserted sample IDs. No matching standalone history or ATB overlap
  was found for those asserted identifiers.
- The additional live [SAMD00006289 sample](https://www.ncbi.nlm.nih.gov/biosample/2731199)
  is a separate SRA-associated sample in PRJDB937, not SAMD00016937.
  A further ignored-inclusive search found its ATB catalog row at
  `data/catalog/allthebacteria.tsv.xz:383`: `NOT_PROCESSED`, without a
  FASTA URL or assembly accession. It supplies no eligible ATB genome link.
- No experimental phenotype, regulatory claim, or causal graph is asserted.
  Optional fields were not populated merely because source pages offer
  broader biological context.

## Findings

None found: 0 blocker, 0 major, 0 minor findings within the reviewed scope.
The live GTDB limitation does not demonstrate a defective pinned assertion.
This verdict is not a full-corpus or assembly-quality certification.

## Recommended Edits

None required. Preserve deposit-specific paths, independent source fields,
the GenBank/RefSeq project distinction, and source accession versions.
Future corrections belong in maintained `data/raw/` or `data/straininfo/`
inputs and their owning transforms, followed by `src/taxonmech/seed.py`,
not a hand edit of this generated YAML.

## Follow-up Checks

- Rerun schema/strict validators and exact source/deposit checks after a
  relevant source refresh; specifically prevent JCM/DSM sequence transfer.
- Recheck the live GTDB genome page when available if a current-release
  classification claim is required.
- Run `just verify-corpus` before claiming corpus-wide reproducibility.
- Assess current assembly quality separately before selecting a genome for
  downstream biological analysis; a source association is not a quality gate.

## Additional Notes

The JCM GenBank row reports 2,757 contigs and RefSeq exclusion reasons
including fragmentation, frameshifted proteins, and not being used as type.
The DSM row has 235 contigs in 232 scaffolds and an explicit paired RefSeq
assembly. These source quality differences were not hidden by treating the
two deposit-linked assemblies as interchangeable.

The JCM catalog lists an LRRH WGS link alongside its JCM assembly link;
these co-listed identifiers were not used to merge the two native paths.
NCBI's explicit BBFV/JCM and LRRH/DSM assembly chains remain the evidence.
The configured NCBI source-reference filenames were checked in
`conf/ncbi_assemblies.yaml`; original external snapshot downloads were not
reread. No source refresh, generation, history event, lifecycle promotion,
taxon YAML edit, or GitHub mutation was performed.
