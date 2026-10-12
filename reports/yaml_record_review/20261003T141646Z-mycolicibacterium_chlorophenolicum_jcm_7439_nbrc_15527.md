# YAML Record Review: Mycolicibacterium chlorophenolicum JCM 7439 = NBRC 15527

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mycolicibacterium_chlorophenolicum_jcm_7439_nbrc_15527.yaml`
- Started UTC: 2026-10-03T14:09:09Z
- Finished UTC: 2026-10-03T14:16:46Z
- Verdict: needs curation

## Target

- Class `TaxonRecord`; identifier `NCBITaxon:1303685`; rank `STRAIN`;
  domain `BACTERIA`; parent `NCBITaxon:37916`.
- Read the entire 1,913-line YAML in four untruncated portions. Grounding
  is `EXACT`, mapping status `SEEDED`, genetic code 11, and strain count 1.
- The strain is `kgmicrobe.strain:bacdive_8364`, designation PCP-1, with
  13 retained culture identifiers, 27 assembly assertions, 19 other-genome
  assertions, and 86 related-record assertions. These are source-qualified
  assertions, not counts of distinct genomes or experiments.
- One GTDB mapping, five synonyms, one identity xref, six source
  attestations, and one seed event are present. There is no causal graph.
- This is generated YAML. No record, source, history, or status was edited.
  Only this report was manually written.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/mycolicibacterium_chlorophenolicum_jcm_7439_nbrc_15527.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/mycolicibacterium_chlorophenolicum_jcm_7439_nbrc_15527.yaml`:
  PASS; one file scanned, zero errors. The standard diagnostic is
  `reports/instance_validation_failures.tsv`.
- Structured identity, all ten ancestor labels/ranks and parent links,
  NCBI synonym classes, complete singleton subtree, and direct BacDive
  strain selection: PASS.
- Exact assertion comparisons: 22 raw plus five StrainInfo assembly
  assertions, 18 raw genome assertions, and 54 raw plus 32 StrainInfo
  related assertions all reproduce their YAML arrays. The one ATB genome
  assertion was checked separately, including every nested evidence field.
- In-memory `straininfo_links.build_links` replay: all 11 strain/deposit
  links, five assemblies, and 32 related assertions match; no exclusions.
- In-memory `atb_links.build_links` replay: one strain/sample link and
  five genome crosslinks match; no exclusions. Six complete sample-evidence
  objects and every explicit matched culture identifier also check out.
- `just verify-corpus`: Not checked; full-corpus-only. No focused substitute
  or claim of full-corpus reproduction is made. Global ATB digest replay,
  downloaded FASTA contents, pages, and exports were not audited.
- Ignored-inclusive target ID/name/slug searches of `history/` found no
  standalone history entry. Standalone history validation therefore had
  no target; the embedded event passed strict validation.
- Graph/product evidence gates are not applicable to this graph-free
  target. Validator success does not establish semantic rank equivalence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308110` supports the exact label, strain rank,
parent 37916, code 11, and four NCBI synonym entries. Parent row 4293 is
the species Mycolicibacterium chlorophenolicum. All ten root-first ancestors
match the complete pinned taxonomy parent chain. The complete target
subtree contains only 1303685.

Native scientific-name and synonym objects at
`data/catalog/ncbi_names-0007.jsonl.gz:30652` through 30656 distinguish
three old-genus synonyms from the reordered modern-genus `includes` name.
The latter is correctly `RELATED_SYNONYM`, not exact merely because the
two culture numbers appear in a different order.

The [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1303685)
agrees on identity but displays legacy `no rank`. Inspected
[Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303685&retmode=xml)
returns `strain`, parent 37916, the same synonyms, and code 11;
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303685)
independently returns `STRAIN` and all ten lineage IDs. The YAML rank is
supported; the browser display is not a reason to demote it.

[JCM 7439](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=7439)
supports the DSM 43826 deposit history and the culture equivalences.
[BacDive 8364](https://bacdive.dsmz.de/strain/8364) uses Mycobacterium
chlorophenolicum and PCP-1, while NCBI/JCM use Mycolicibacterium.
[LPSN](https://lpsn.dsmz.de/species/mycolicibacterium-chlorophenolicum)
classifies the Mycolicibacterium combination as a validly published synonym
and points to the Haggblom 1994 Mycobacterium combination as correct name.
These different genus treatments must remain source-qualified.

The LPSN inventory maps name 798171 to species 37916, not strain 1303685.
Names 778424 and 16956 distinguish the Haggblom and Briglia combinations;
the latter is illegitimate. They must not be collapsed by matching their
binomial strings. Missing strain-level nomenclature and a missing derived
type flag follow the current same-taxon LPSN rule, not evidence that this
culture is biologically non-type. No species-name claim should be promoted
to an exact synonym for the whole strain concept.

## Evidence

The six source attestations reproduce their inventories:

| Source | Inventory location | Count and unit |
| --- | --- | --- |
| NCBI | `data/raw/ncbitaxon_taxa.tsv:308110` | 1 NAME |
| GTDB | `data/raw/gtdb_mappings.tsv:17460` and `gtdb_species.tsv:122868` | 4 GENOME, species-cluster scope |
| BacDive | `data/raw/bacdive_strains.tsv:8233` | 1 STRAIN |
| MediaDive | `data/raw/mediadive_taxa.tsv:2813` | 4 MEDIUM: 645, 65, J26, J43 |
| GOLD | `data/raw/gold_organisms.tsv:7428` | 2 ORGANISM |
| Madin | `data/raw/madin_taxa.tsv:11825` | 4 TRAIT_ASSERTION |

`curation/seed_scope.tsv:12069` supplies the six-source admission reason.
The 2026-09-13T17:54:04Z event reproduces it and does not claim human
review. Units are not interchangeable. BacDive's raw medium count is zero
and is omitted; it is not the separate MediaDive inventory count.

**BacDive and culture identifiers.** The complete native object at
`data/bacdive/records.jsonl.gz:8232` supports the retained 13 identifiers
and all three direct assembly/BV-BRC/IMG groups. References 66792 and
67770 remain attached to their own genome objects, not the entire record.
The direct taxon association makes `classified_as` unnecessary.

Two retained numbers, NCIMB 12325 and NCIMB 123325, remain unresolved
source variants. Both occur in BacDive; JCM and the eligible StrainInfo
deposit support 12325, while native GOLD Go0605460 supplies 123325.
The primary NCIMB link for 12325 returned only a loading shell. Syntax
validation and source agreement do not prove the six-digit number denotes
the same deposit. Do not silently rewrite it, merge the keys, or transfer
12325's sequence evidence onto it. The YAML preserves their different
source assertions, so this uncertainty is not counted as an additional
unsupported transformation in this report.

**Three assembly families.** Native source objects were inspected in full:

| Deposit | NCBI assembly family | BioSample | Original BioProject | WGS |
| --- | --- | --- | --- | --- |
| DSM 43826 | GCA_001044235.1 / GCF_001044235.1 | SAMN03327461 | PRJNA274376 | JYNL00000000.1 |
| JCM 7439 | GCA_001313545.1, no RefSeq pair | SAMD00016952 | PRJDB943 | BBGB00000000.1 |
| NBRC 15527 | GCA_001552315.1 / GCF_001552315.1 | SAMD00046518 | PRJDB464 | BCQY00000000.1 |

- GenBank objects: `data/catalog/ncbi_genbank-0000.jsonl.gz:36354`
  and 49283, plus `ncbi_genbank-0001.jsonl.gz:9837`.
- RefSeq objects: `data/catalog/ncbi_refseq-0000.jsonl.gz:30723`
  and `ncbi_refseq-0001.jsonl.gz:153`. Their pinned BioProject field is
  PRJNA224116, distinct from each original submission project.
- BV-BRC objects: `data/bvbrc/bvbrc-0019.jsonl.gz:45231` for 37916.4;
  `bvbrc-0001.jsonl.gz:23812` for 1303685.4 and 23813 for 1303685.5.
  Explicit culture and strain fields are separate retained assertions.
- GTDB objects: `data/catalog/gtdb_genomes-0012.jsonl.gz:17502`
  for DSM 43826 and `gtdb_genomes-0008.jsonl.gz:24012` for NBRC 15527.
  The DSM genome is the cluster representative; NBRC is not.

Live [NCBI assembly reports](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_001044235.1,GCF_001044235.1,GCA_001313545.1,GCA_001552315.1,GCF_001552315.1/dataset_report)
confirm all five versioned accessions as current, their strains, pairs,
levels, samples, and original projects. The live API reports original
projects for RefSeq too; that does not erase the pinned umbrella-project
assertions. JCM's assembly is fragmented and not used as type. Its
association is not an endorsement of assembly quality. ENA sample XML
independently confirms [DSM](https://www.ebi.ac.uk/ena/browser/api/xml/SAMN03327461),
[JCM](https://www.ebi.ac.uk/ena/browser/api/xml/SAMD00016952), and
[NBRC](https://www.ebi.ac.uk/ena/browser/api/xml/SAMD00046518) deposit fields.

**GOLD chains.** Complete organism/project/analysis objects support:

- Go0116206 -> Gp0120608 -> Ga0080924 -> GCA_001044235.1,
  IMG 2630968674, DSM 43826.
- Go0094276 -> Gp0094276 -> Ga0128435 -> GCA_001313545.1,
  IMG 2734481951, JCM 7439.
- Go0024504 -> Gp0024504 -> Ga0128531 -> GCA_001552315.1,
  IMG 2731957580, NBRC 15527.

Organism source locations are `data/gold/organisms.jsonl.gz:65803`,
55166, and 20825; projects are `data/gold/projects.jsonl.gz:70227`,
55671, and 20318; analyses are `data/gold/analyses.jsonl.gz:51433`,
74797, and 74893. Go0094276's organism name mentions NBRC, but its explicit
culture field is JCM 7439; the join correctly follows that field.
Bare PCP-1 strain fields are not culture keys. Additional organism-only
Go0605458 through Go0605461 at rows 436453 through 436456 support ATCC,
JCM, NCIMB 123325, and NRRL relationships without invented assemblies.

**StrainInfo.** The complete native object at
`data/straininfo/records.jsonl.gz:30912` is SI-ID 42703, BacDive 8364,
published online. [DataCite](https://api.datacite.org/dois/10.60712/si-id42703.3)
confirms DOI 10.60712/SI-ID42703.3 as a findable version-3 source record,
not a publication or a deposit DOI. Eleven of its 12 own deposits match
retained culture identifiers and have eligible statuses. CCRC 13726 is
not rewritten into BCRC 13726. MTCC 2570 and NCIMB 123325 occur only as
relations in this pinned object and cannot supply own-deposit evidence.

Three genome sequence objects supply five exact deposit-specific assembly
assertions: GCA_001044235 for DSM deposit 114888; GCA_001313545 and
GCA_001552315 each for JCM 152978 and NBRC 335320. Their unversioned
accessions are preserved. The 32 related assertions comprise 11 source
strain references, 11 deposit references, and these ten nucleotide links:

| Deposit | Accessions and inspected sequence scope |
| --- | --- |
| IFO 15527 | AB014149, gyrB, 1,254 bp; AB426725, IM2-51/P450, 1,350 bp |
| CIP 104189 | AF547820, hsp65, 424 bp; AF547911, 16S, 540 bp; AY544900, rpoB, 398 bp; DQ480296, ssrA, 305 bp; DQ986108, tuf, 649 bp; EF686831, smpB, 302 bp |
| DSM 43826 | X79292, 16S, 1,466 bp |
| NCIMB 12325 | X81926, 16S, 1,317 bp |

Inspected [NCBI nucleotide EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB014149,AB426725,AF547820,AF547911,AY544900,DQ480296,DQ986108,EF686831,X79292,X81926&rettype=gb&retmode=xml)
resolves all ten to version .1 and corroborates lengths, annotations, and
deposit context. X79292 names DSM in its definition rather than a strain
qualifier; X81926 prints the type marker as NCIMB 12325T. These links use
explicit SI-DP evidence, not a new suffix-stripping identity rule. Genes
and rRNA are correctly outside assembly/genome counts.

**AllTheBacteria.** `atb.assembly:202505.SAMD00046518` reproduces
`data/atb/assemblies.tsv:144`, exactly matching the complete catalog row
at `data/catalog/allthebacteria.tsv.xz:4455`. Release 2025-05, dataset
661k, all filters, SeqKit sum, three runs, species classifier output,
FASTA URL, and archive URL/filename agree. The manifest and configuration
agree on the release, source URL, and metadata digest; their global files
were not rehashed in this focused review.

`data/atb/strain_links.tsv:5266` retains six explicit NBRC BioSample
assertions: two BV-BRC fields, GOLD, GTDB, GenBank, and RefSeq. The five
rows at `data/atb/genome_links.tsv:23094` through 23098 link only to
RS_GCF_001552315.1, IMG 2731957580, GCA_001552315.1,
GCF_001552315.1, and BV-BRC 1303685.4. Each relation is
`shares_biosample`, not genome identity. No DSM or JCM assembly family
is transferred merely because it belongs to the same BacDive strain.

[ENA ERZ2884845](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ2884845)
explicitly names sample SAMD00046518/DRS064730 and all three runs,
DRR064046, DRR064047, and DRR064048. Individual ENA run XML also resolves
them to the same sample context. An initial comma-separated portal query
returned an empty list; the successful individual and analysis lookups
resolve that retrieval limitation. ENA's reassembly study PRJEB45982 is
not the original sequencing project or evidence of assembly equivalence.

## Completeness

- Ignore-independent structured scans cover the complete taxonomy,
  BacDive classifications, relevant raw attestation/mapping tables, and
  native StrainInfo own deposits. Only SI-ID 42703 contains matching own
  deposits. No direct target LPSN mapping or BactoTraits attestation was
  found in their complete maintained inventories.
- Ignored-inclusive decompression-aware searches cover all 19 native
  GTDB shards and the full ATB catalog. The latter supplies only the NBRC
  sample among SAMD00046518, SAMD00016952, and SAMN03327461. This is
  bounded snapshot coverage, not a claim about all public sequencing data.
- Source-native searches and full target-object inspection cover NCBI
  names/assemblies, BacDive, BV-BRC, GOLD, StrainInfo, and ATB. The exact
  raw/SI/ATB comparisons found no lost represented assertion.
- The structured iModulonDB runner was resolved and attempted via
  `uv run --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`.
  Sandbox DNS failed. An approved read-only request to the official
  [datasets API](https://imodulondb.org/api/datasets) returned 20 organism
  entries, none matching chlorophenolicum. Mycobacterium tuberculosis
  is not a substitute. Component searches are not applicable, and absence
  supplies no negative biological evidence.
- Optional definitions, phenotypes, and causal mechanisms need not be
  invented. Extra native marker accession X79094 and species-level type
  information are not permission to broaden deposit-specific links or
  add fields outside the current import contract.

## Findings

**Major 1: A GTDB species cluster is promoted to strain identity.**

At target lines 39-49, the species-level mapping becomes an
`EXACT_SYNONYM` for this strain; lines 62-63 also place it in identity
xrefs. The source predicate is preserved correctly, but it does not prove
rank-compatible equivalence. A complete native cluster census contains:

| GTDB member | Native NCBI taxon | Strain/isolate | Native source location |
| --- | --- | --- | --- |
| RS_GCF_001552315.1 | 1303685 | NBRC 15527 | `gtdb_genomes-0008.jsonl.gz:24012` |
| RS_GCF_001044235.1 | 37916 | DSM 43826 | `gtdb_genomes-0012.jsonl.gz:17502` |
| GB_GCA_004216875.1 | 2512172 | BK558 | `gtdb_genomes-0005.jsonl.gz:14537` |
| GB_GCA_016219585.1 | 318424 | NC_groundwater_1897_Pr3_S2p5_69_21 | `gtdb_genomes-0005.jsonl.gz:19126` |

All paths in this table are beneath `data/catalog/`. The last member is
metagenome-derived and NCBI-classified as Mycolicibacterium rufum. Neither
it nor BK558 supplies evidence of identity with JCM 7439/NBRC 15527.
The four-genome count is correct for the species cluster, not four genomes
of this strain. Raw mapping rows 17460, 196511, 267646, and 284951 map
that cluster to several NCBI concepts, including parent species 37916.

Maintained owner: `src/taxonmech/seed.py:451` treats any `closeMatch` as
identity without checking rank and then adds the xref and exact synonym
at lines 466-468. `tests/test_seed.py` owns regression coverage. Upstream
mapping semantics belong to the kg-microbe GTDB transform identified by
`conf/sources.yaml`, not a hand edit to `data/raw/gtdb_mappings.tsv`.

Finding counts: zero blockers, one major, zero minor. The genus treatments
and NCIMB spelling conflict remain explicit uncertainties, not silently
resolved additional findings.

## Recommended Edits

1. In `src/taxonmech/seed.py`, require biological scope/rank-compatible
   evidence before generating GTDB identity xrefs or exact synonyms.
   Prevent this species-to-strain promotion and add a focused regression
   in `tests/test_seed.py`; retain the valid NCBI strain synonyms.
2. Review the upstream mapping predicate and local interpretation with
   the four-member counterexample. Preserve the source-qualified cluster
   relationship and count without asserting strain equivalence. Do not
   guess a replacement SKOS direction or automatically move everything
   onto the parent, which already has its own mapping.
3. Keep all supported deposit-qualified genome, sample, project, gene,
   and ATB links. Any later NCIMB-number reconciliation must start with
   collection/BacDive/GOLD source-owner evidence and refreshed maintained
   inputs, not normalization of generated YAML or relation-only SI text.

## Follow-up Checks

- Test this strain, its parent, and the BK558/metagenome counterexamples
  against the revised identity rule. Preserve genuine species mappings
  and explicitly supported strain synonyms.
- After an authorized implementation, use the documented targeted seed
  workflow and rerun both focused validators. Broad regeneration requires
  `just verify-corpus` and the documented product gates.
- Replay the exact raw, SI-DP, and ATB evidence comparisons. Keep marker
  genes out of genome counts, source versions intact, and ATB crosslinks
  limited to their explicit BioSample family.
- Resolve NCIMB 12325 versus 123325 with primary collection evidence
  before merging or deleting either retained source identifier.

## Additional Notes

The initial SI replay probe used the wrong top-level ID field, failed
without writing anything, and was rerun using native `strain.siID`.
Final structured comparisons and source replays succeeded. Public API
checks required approved read-only network escalation after sandbox DNS
failure. The unavailable GTDB tree page was supplemented by the complete
native four-member metadata census, not by a search-result inference.

This is a semantic review of one record, not a genome-quality assessment,
a source refresh, a correction of the NCIMB catalog, or certification of
the wider corpus. The report does not change `SEEDED` to `REVIEWED`.
