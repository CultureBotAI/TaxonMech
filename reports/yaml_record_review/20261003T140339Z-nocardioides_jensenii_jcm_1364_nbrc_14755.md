# YAML Record Review: Nocardioides jensenii JCM 1364 = NBRC 14755

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardioides_jensenii_jcm_1364_nbrc_14755.yaml`
- Started UTC: 2026-10-03T13:59:08Z
- Finished UTC: 2026-10-03T14:03:39Z
- Verdict: needs curation

## Target

- Class `TaxonRecord`; identifier `NCBITaxon:1303683`; rank `STRAIN`;
  domain `BACTERIA`; parent species `NCBITaxon:1843`.
- Read all 1,437 YAML lines in three untruncated sections. Grounding is
  `EXACT`; mapping status is `SEEDED`.
- One directly classified strain, `bacdive:11099`, has 17 retained culture
  identifiers or aliases, 17 assembly assertions, 11 other genome
  assertions, and 68 related-record assertions. All 96 were reviewed.
- Generated YAML is owned by maintained source inventories and
  `src/taxonmech/seed.py`. Only this new review report was manually written.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/nocardioides_jensenii_jcm_1364_nbrc_14755.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/nocardioides_jensenii_jcm_1364_nbrc_14755.yaml`:
  PASS; one file scanned, zero errors. The normal diagnostic is
  `reports/instance_validation_failures.tsv`.
- Structured identity, rank, parent, genetic code, ten ancestor labels and
  ranks, root-first chain, three NCBI synonyms, complete target subtree,
  BacDive count, and all 17 retained identifiers: PASS.
- Exact multiset comparisons of every populated field in all 96 assertions
  against source inventories: PASS. Nested evidence was parsed as JSON.
  Every populated culture-match path passed the repository's CAFI-aware
  normalization checks; unsupported aliases are retained without joins.
- Native StrainInfo reconstruction in memory reproduced 13 own-deposit
  matches, four assembly assertions, and 31 related assertions exactly.
  No output files or source inventories were regenerated.
- Complete scans of the native StrainInfo archive and nineteen GTDB genome
  shards checked deposit coverage and exact species-cluster membership.
- `just verify-corpus`: Not checked; full-corpus-only, not a documented
  focused validator. No full-corpus reproducibility claim is made.
- Ignored-inclusive `history/` searches found no matching external entry;
  standalone history validation had no target. The embedded event passed
  strict validation. No history entry was created.
- Causal-graph gates are not applicable. Pages, exports, global product
  validation, and full-corpus QC were not audited.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308108` identifies the strain; row 1447
identifies its parent species. The complete target subtree contains only
1303683. Its ten ancestors match the root-first NCBI chain in the YAML.
Native names at `data/catalog/ncbi_names-0007.jsonl.gz:30647` through 30650
include the scientific name, two synonyms, and the equivalent name with
NBRC/JCM ordering reversed. All three NCBI exact synonyms are supported.

The inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1303683)
agrees on identity, lineage, and code 11, but displays `no rank`. Approved
read-only requests to [Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303683&retmode=xml)
and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303683)
return `strain`/`STRAIN`, parent 1843, the exact label, and all ten lineage
IDs. The browser/API discrepancy does not warrant a YAML rank change.

[JCM 1364](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=1364)
supports the deposit relationships and the CNF 091 history. The inspected
[BacDive record](https://bacdive.dsmz.de/strain/11099) agrees on ID 11099,
the strain/species taxon distinction, and the culture collection list.
CNF 091 and IMSNU 22036 remain source-retained values, not registered
genome-join keys under the pinned CAFI templates.

[LPSN](https://lpsn.dsmz.de/species/nocardioides-jensenii) identifies
Nocardioides jensenii as the validly published correct species name and
Pimelobacter jensenii as its homotypic synonym. The raw name row at
`data/raw/lpsn_names.tsv:18670` concerns species 1843, not strain 1303683.
The lack of a strain-level nomenclature block or same-taxon LPSN-derived
type flag is not a missing required representation. The parent species'
name must not become this strain's exact synonym merely because the
culture is a type strain; that scope error occurs for GTDB in M1.

## Evidence

Maintained input checks:

| Input | Row or lines | Supported scope |
| --- | --- | --- |
| `data/raw/bacdive_strains.tsv` | 10952 | Direct classification, 17 identifiers, empty designation, medium count zero |
| `data/raw/mediadive_taxa.tsv` | 2812 | Two media, 92 and J40 |
| `data/raw/madin_taxa.tsv` | 11824 | One direct trait assertion |
| `data/raw/bactotraits_taxa.tsv` | 2278 | Five direct trait assertions |
| `curation/seed_scope.tsv` | 12068 | Six-source admission reason |
| `data/raw/gtdb_species.tsv` | 127777 | Exact species cluster, one genome |
| `data/raw/gtdb_mappings.tsv` | 17459 | Strain-targeted closeMatch, one genome |
| `data/raw/strain_assemblies.tsv` | 3918-3930 | Thirteen source assembly paths |
| `data/straininfo/assemblies.tsv` | 429-432 | Four explicit sequence-deposit paths |
| `data/raw/strain_genome_records.tsv` | 3019-3029 | Eleven other genome paths |
| `data/raw/strain_related_records.tsv` | 11885-11921 | Thirty-seven qualified relationships |
| `data/straininfo/related_records.tsv.gz` | 8484-8514 | Thirty-one deposit/strain/nucleotide paths |

The complete BacDive object at `data/bacdive/records.jsonl.gz:10951`
supports two separate native genome families. Reference 66792 supplies
unversioned GCA_001313485, IMG 2734481948, and BV-BRC 1303683.6;
reference 67770 supplies GCA_001552535, IMG 2731957589, and 1303683.4.
The corresponding live BacDive genome table agrees. Accessions, references,
and source taxon classifications are preserved without inventing versions.

Complete native assembly and genome objects establish the two paths:

- JCM: `data/catalog/ncbi_genbank-0000.jsonl.gz:49280` and
  `data/bvbrc/bvbrc-0001.jsonl.gz:23810` support GCA_001313485.1,
  ASM131348v1, PRJDB940, SAMD00016933, and WGS BBFY00000000.1
  (unversioned in BV-BRC). NCBI reports 2,354 contigs, 3,673,495 bp,
  and exclusion from RefSeq for fragmentation/not being used as type.
  The association is supported; it is not a genome-quality endorsement.
- NBRC: `data/catalog/ncbi_genbank-0001.jsonl.gz:9848`,
  `data/catalog/ncbi_refseq-0001.jsonl.gz:163`, and
  `data/bvbrc/bvbrc-0001.jsonl.gz:23809` support GCA_001552535.1 /
  GCF_001552535.1, ASM155253v1, SAMD00046513, and WGS
  BCRJ00000000.1. NCBI explicitly pairs these assemblies as identical,
  with 187 contigs and 5,102,139 bp. GenBank/BV-BRC use sequencing project
  PRJDB1327; RefSeq uses annotation project PRJNA224116.

The complete GTDB object at `data/catalog/gtdb_genomes-0003.jsonl.gz:27071`
supports RS_GCF_001552535.1, explicit NBRC 14755, both NCBI assembly
identifiers, the sample, and RefSeq project. The full nineteen-shard exact
terminal-taxonomy scan found this as the sole member of
`s__Nocardioides jensenii`. Its representative/type metadata support this
culture's membership; a singleton source snapshot does not turn a species
concept into a strain concept.

Native GOLD objects preserve the evidence chains:

- `data/gold/organisms.jsonl.gz:47163` is Go0075746. Its explicit culture
  field is JCM 1364; its strain field is bare CNF091. Only the former
  supplies the match, even though the organism name also mentions NBRC.
- `data/gold/projects.jsonl.gz:46186` and 55645 identify Gp0075746 and
  Gp0094250, both pointing to Go0075746, with the NBRC and JCM
  project/sample pairs respectively.
- `data/gold/analyses.jsonl.gz:74903` and 74794 identify Ga0128541 and
  Ga0128432, each pointing to its corresponding project. Their GenBank
  payloads and IMG identifiers support the assembly/genome links. Blank
  analysis organism fields do not contradict the explicit project chain.
- Organism rows 432019-432024 support Go0601000 through Go0601005 and
  the ATCC, DSM, IAM, IFO, IMET, and NCIB deposits. Those organism
  references do not transfer the JCM genome paths onto those deposits.

The full StrainInfo object at `data/straininfo/records.jsonl.gz:9324`
is SI-ID 9324, BacDive 11099, published online, with fourteen own deposits.
Thirteen match eligible culture keys and have available status,
nondeprecated collections, and nonerroneous relations. Each source
sequence names its exact matched SI-DP. Both unversioned assemblies
explicitly name both JCM deposit 37104 and NBRC deposit 332648; all four
assertions are therefore supported, not inferred cross-deposit transfers.

The remaining own deposit is 114870, designation `NCIB9770`. It lacks
the separator required by the pinned culture-key parser, so it does not
join the retained `NCIB-9770` identifier. PCM 2328 and IMSNU 22036 occur
only among this snapshot's alternative designations, not own deposit
objects. No extra link is licensed by those mentions or group membership.

[DataCite](https://api.datacite.org/dois/10.60712/si-id9324.3) confirms
findable DOI 10.60712/SI-ID9324.3, version 3, and the StrainInfo destination.
Approved [nucleotide EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AF005006,AF017491,AF110038,X53214,Z78210&rettype=gb&retmode=xml)
checks confirm all five accessions and source strains:

| Accession | Deposit | Source sequence description | Length |
| --- | --- | --- | --- |
| AF005006.1 | KCTC 9134 | Partial 16S rRNA | 1473 bp |
| AF017491.1 | KCTC 9134 | Complete 16S-23S ITS | 344 bp |
| AF110038.1 | KCTC 9134 | Partial RNase P RNA gene | 326 bp |
| X53214.1 | DSM 20641 | Partial 16S rRNA | 1452 bp |
| Z78210.1 | DSM 20641 | 16S rRNA gene | 1467 bp |

All classify under species 1843 in the sequence source. The YAML preserves
StrainInfo's unversioned forms and its `gene`/`rrnaop` source categories;
these references are not genomes, phenotypes, or complete operon claims.

After four web-page opens failed, approved NCBI ESearch/EFetch requests
verified [SAMD00016933](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=4151245&retmode=xml)
as JCM 1364 and [SAMD00046513](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=4447879&retmode=xml)
as NBRC 14755, both taxon 1303683, linked respectively to PRJDB940 and
PRJDB1327. The project XML independently verifies
[PRJDB940](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=245961&retmode=xml),
[PRJDB1327](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=231384&retmode=xml),
and the separate [RefSeq annotation project](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=224116&retmode=xml).

Six attestations reproduce the pinned inventories: NCBI one NAME, GTDB
one cluster GENOME, BacDive one STRAIN, MediaDive two MEDIUM records,
Madin one and BactoTraits five TRAIT_ASSERTION records. GOLD's six direct
species organisms at `data/raw/gold_organisms.tsv:16359` are not a direct
strain attestation. Native genome enrichment and KGX attestation counts
are distinct inputs. The seed event's six-source reason agrees.

## Completeness

- All 96 populated assertions retain supported source-specific paths.
  Repeated identifiers preserve distinct provider/field/deposit evidence.
- A complete ignored-inclusive scan of native StrainInfo own deposits
  found only SI-ID 9324 matching this record's eligible culture keys.
  Its thirteen eligible deposits and seven sequence objects are accounted
  for by the four assembly and 31 related assertions.
- Ignored-inclusive, decompression-aware searches of `history/`,
  `data/atb/`, and the full compressed ATB catalog for target ID, label,
  slug, BacDive strain ID, both assembly families, and both whole BioSample
  accessions returned no matches. This is bounded local-source coverage,
  not a claim that no raw sequencing reads exist elsewhere.
- The iModulonDB runner resolved, but its dataset request failed DNS.
  An approved direct read of the official
  [dataset API](https://imodulondb.org/api/datasets) returned the complete
  organism list without Nocardioides coverage. Component searches were
  not applicable; absence is not biological negative evidence.
- Optional phenotype graphs, definitions, and experimental evidence are
  not required. The consequential issue is GTDB species identity scope,
  not optional empty slots, source quality differences, or excluded aliases.

## Findings

**M1 - Major: GTDB species identity is promoted onto an individual strain.**

YAML lines 46-49 make Nocardioides jensenii an `EXACT_SYNONYM` of the
JCM/NBRC strain, and line 60 places `GTDB:s__Nocardioides_jensenii` in
equivalence xrefs. The raw closeMatch at lines 39-44 is the source of
this promotion, but the mapped concept is a species and the target is a
strain under NCBI species 1843. The schema explicitly reserves xrefs for
true equivalences. One sequenced representative in the pinned GTDB
snapshot does not establish equivalence between these biological scopes.

**Maintained owner:** `src/taxonmech/seed.py:451` treats any closeMatch
as identity without a compatible-rank check, then lines 466-469 generate
the xref and exact synonym. Upstream predicate semantics belong to the
kg-microbe GTDB transform identified by `conf/sources.yaml`; generated
`data/raw/gtdb_mappings.tsv` is an input artifact, not a hand-edit target.

Finding counts: zero blockers, one major, zero minor. No additional finding
is warranted for the NCBI synonyms, explicit genome links, or source-only
assembly quality metadata.

## Recommended Edits

1. Make GTDB identity promotion rank/scope-aware in `src/taxonmech/seed.py`.
   Remove this species' exact synonym and equivalence xref from the strain
   through regeneration, while preserving defensible source classification
   provenance. Add strain and valid species cases in `tests/test_seed.py`.
2. Review the upstream GTDB predicate derivation before changing the
   mapping itself. Do not invent a replacement broad/narrow predicate or
   manually rewrite the generated inventory. The singleton count remains
   a species-cluster count, not proof of strain identity.
3. Preserve the NCBI identity and three NCBI synonyms, all 17 retained
   identifiers, all 96 qualified links, accession versions, and exact SI-DP
   evidence. Do not normalize `NCIB9770` or unsupported aliases beyond
   the maintained matching contract as an incidental fix.
4. After authorized maintained changes, use the documented extraction and
   seed-canary workflow before any wider regeneration. Do not hand-edit
   generated YAML or promote review status from this report alone.

## Follow-up Checks

- Run focused seed regression tests for the singleton GTDB strain case
  and valid same-species equivalences; shape validation cannot detect M1.
- Inspect the regenerated target for removal of species equivalence claims
  while preserving bounded GTDB provenance and source-scoped counts.
- Repeat the full 96-assertion comparison and native StrainInfo replay,
  ensuring that both sequences' explicit JCM/NBRC paths survive.
- Rerun the two focused validators above. After an authorized broad
  regeneration, run full `just verify-corpus` and documented product gates.
- Recheck the live GTDB page when available if future curation depends on
  current release membership, rather than the inspected pinned snapshot.

## Additional Notes

The GTDB species page was unavailable in the web tool. Its count and scope
were checked from pinned native metadata and a complete cluster scan.
The first ad hoc comparison used a singular BacDive column name and failed;
the corrected `taxon_ids` comparison completed successfully. Initial broad
numeric searches also returned unrelated IDs and were not treated as target
matches; structured exact comparisons and bounded absence searches supplied
the conclusions above.

Review findings do not mutate the generated record or confer human-reviewed
status. No paid research, source refresh, GitHub mutation, curation event,
or generated-page rebuild was performed. Eukaryota was excluded from new
target selection as requested.
