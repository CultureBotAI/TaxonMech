# YAML Record Review: Gordonia polyisoprenivorans HW436

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/gordonia_polyisoprenivorans_hw436.yaml`
- Started UTC: 2026-10-05T20:03:22Z
- Finished UTC: 2026-10-05T20:15:11Z
- Verdict: needs curation

## Target

The entire 79-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034768`, Gordonia polyisoprenivorans HW436, rank
`STRAIN`, domain `BACTERIA`, parent `NCBITaxon:84595`,
genetic code 11, `EXACT` grounding, `SEEDED` status, and
`strain_count: 0`. The primary identity is the HW436 strain,
not the parent species, its GTDB species cluster, or an assembly.

Owning source rows are `data/raw/ncbitaxon_taxa.tsv:221688`,
`data/raw/gtdb_mappings.tsv:1396`, and
`curation/seed_scope.tsv:66004`.
`data/taxa/PATHS.tsv:14158` agrees in identifier and slug.
The mapping and derived synonym need an upstream/rule correction;
this review changes no generated field.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/gordonia_polyisoprenivorans_hw436.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/gordonia_polyisoprenivorans_hw436.yaml --out /private/tmp/gph-strict-20261005.tsv`: exit 0; one file, zero error files and zero error rows. The output TSV was read and contains only its header.
- Structured comparisons checked the complete backbone row, ten ancestors, NCBI synonyms, PATHS, scope, source attestations, and seed event. Seven raw inventories and exact type-material, merged-ID, and dropped-record tables were checked.
- `rg --no-ignore --hidden -n -z -i` searched the target ID, slug, and HW436 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All 17 candidate rows were read fully: 13 target-relevant and four namespace collisions.
- A secondary accession/source-ID search across those roots returned 23 rows: seven already inspected and 16 additional rows, all read fully. One additional row is the target BioSample in AllTheBacteria; 15 are unrelated extended WGS-prefix matches. TSV headers and complete decoded JSON were used, not snippets.
- All seven mappings of the exact GTDB species and all 17 members of its pinned RS232 cluster were read. This is a complete check of that local species cluster, not an audit of GTDB generally.
- Separate ignored-inclusive content and filename searches in `reports` and `history` found no prior target report or separate target history artifact, including accession and source-ID matches, before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, Assembly ESummary, Datasets genome metadata, all six nucleotide records' metadata, the BioProject page, four PubMed queries, relevant publication metadata/abstracts, and the original genome paper were inspected.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused comparisons do not establish whole-corpus reproduction.
- iModulonDB and curator-added graph ID/label checks are inapplicable: the YAML asserts no gene, regulator, protein, phenotype, transcriptomic result, or causal graph. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

Live NCBI Taxonomy agrees with the exact strain ID/name, parent
species 84595, strain rank, genetic code, and full root-first lineage:
`1 > 131567 > 2 > 1783272 > 201174 > 1760 > 85007 > 85026 > 2053 > 84595`.
The corresponding labels/ranks are root, cellular organisms,
Bacteria, Bacillati, Actinomycetota, Actinomycetes, Mycobacteriales,
Gordoniaceae, Gordonia, and Gordonia polyisoprenivorans.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034768);
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034768).

The exact scientific-name and two equivalent-name rows are
`data/catalog/ncbi_names-0005.jsonl.gz:31076`,
`data/catalog/ncbi_names-0005.jsonl.gz:31077`, and
`data/catalog/ncbi_names-0005.jsonl.gz:31078`.
They support the two NCBI synonyms retaining "str. HW436" and
"strain HW436", but not the bare species name as an exact strain
synonym. The backbone has no target retirement value or direct
children; exact type-material, merged-ID, and dropped-record
checks found no target row.

The GTDB species `GTDB:s__Gordonia_polyisoprenivorans` is real,
but is broader than HW436. The pinned cluster has 17 assemblies
with seven distinct NCBI taxon IDs; only one member is assigned
to 1034768. Its representative is
`RS_GCF_000241325.1`, NBRC 16320, not HW436.
HW436 is not a representative or a type-material assembly in
the inspected GTDB/NCBI metadata. GTDB's Mycobacteriaceae family
placement and NCBI's Gordoniaceae placement are separate source
hierarchies, not grounds to overwrite the NCBI lineage.

The record's GTDB `skos:closeMatch`, bare-species
`EXACT_SYNONYM`, and identity-derived cross-reference therefore
conflate species classification with strain equivalence. This is
one major finding. The primary NCBI record identity remains sound.

## Evidence

The NCBITAXON attestation agrees in identifier, label, count 1,
unit `NAME`, and 2026-09-13 snapshot. The GTDB attestation
faithfully copies the raw mapping, including the problematic
predicate; copying a source does not establish equivalence.
Scope and the 2026-09-13T17:54:04Z `seed_from_sources` /
`SEEDED_FROM_SOURCES` event agree exactly.

The GTDB `genome_count: 17` matches
`data/raw/gtdb_species.tsv:70640` and the complete RS232 species
cluster. The schema defines this as a source-taxon count, not
the number of HW436 assemblies. It is not a separate count error.
The pinned catalog's RS232 provenance was read in
`data/catalog/PRIMARY.json:823`.
[GTDB RS232 release](https://data.gtdb.ecogenomic.org/releases/release232/232.0/).

All inspected cluster members are listed below. Shard/line is
relative to `data/catalog/gtdb_genomes-<shard>.jsonl.gz`;
designations are source-reported, not inferred deposit equivalences.

| GTDB accession | Strain/isolate | NCBI taxon | Shard:line |
|---|---|---|---|
| RS_GCF_000241325.1 | NBRC 16320 | 1077976 | 0013:7054 |
| RS_GCF_903833735.1 | MJ130916B_bin-104 | 198437 | 0013:24892 |
| RS_GCF_040538585.1 | GP2_1 | 84595 | 0013:26895 |
| RS_GCF_002043085.1 | i37 | 1961707 | 0013:36674 |
| RS_GCF_029269935.1 | N1V | 3034163 | 0000:43438 |
| RS_GCF_039600425.1 | GP2 | 84595 | 0007:44991 |
| RS_GCF_026016685.1 | B251 | 84595 | 0002:16977 |
| RS_GCF_018135605.1 | C | 84595 | 0002:33366 |
| RS_GCF_903862365.1 | MJ-time_bin-6433 | 198437 | 0002:47243 |
| GB_GCA_003524885.1 | UBA8180 | 84595 | 0005:32898 |
| RS_GCF_027947515.1 | 135 | 84595 | 0005:38378 |
| RS_GCF_040538615.1 | GP2_2 | 84595 | 0011:11017 |
| RS_GCF_051303105.1 | NBRC 16320 | 84595 | 0011:25534 |
| RS_GCF_002257745.1 | herm_1 | 84595 | 0001:24200 |
| RS_GCF_012396285.1 | ATCC BAA-14 | 84595 | 0001:46588 |
| RS_GCF_000385355.1 | HW436 | 1034768 | 0010:24070 |
| RS_GCF_000247715.1 | VH2 | 1112204 | 0006:5000 |

The raw species mappings occur at
`data/raw/gtdb_mappings.tsv:1396`, `data/raw/gtdb_mappings.tsv:2921`,
`data/raw/gtdb_mappings.tsv:3872`, `data/raw/gtdb_mappings.tsv:109688`,
`data/raw/gtdb_mappings.tsv:119157`, `data/raw/gtdb_mappings.tsv:249095`,
and `data/raw/gtdb_mappings.tsv:312328`.
They map the same source species to NCBI IDs 1034768, 1077976,
1112204, 1961707, 198437, 3034163, and 84595 respectively;
the 198437 and 84595 predicates are broadMatch, the other five
closeMatch. Thus the local input does not establish a one-to-one
species identity merely by emitting closeMatch.

The exact query `txid1034768[Organism:noexp]` returned one
Assembly item, UID 667558, and six Nuccore items. Assembly
ESummary and Datasets explicitly pair `GCA_000385355.1` and
`GCF_000385355.1` as identical GenBank/RefSeq counterparts,
assembly ASM38535v1, HW436, taxon 1034768, BioSample
`SAMN02256401`. This is a 6,328,722-base, one-contig assembly
at Contig level, not an asserted complete chromosome.
[NCBI assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000385355.1/).

The source BioProject `PRJNA165561` is mono-isolate and links
the same assembly/BioSample, GOLD project `Gp0015849`, and
IMG `2516493022`. The RefSeq umbrella `PRJNA224116` is not
a strain-unique identifier.
[BioProject PRJNA165561](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA165561).

Independent native inventory paths corroborate the explicit
assembly chain:

- `data/catalog/ncbi_genbank-0000.jsonl.gz:10998` and `data/catalog/ncbi_refseq-0000.jsonl.gz:9587`: paired versioned assemblies, exact strain/taxon and BioSample.
- `data/bvbrc/bvbrc-0000.jsonl.gz:3281`: genome `1034768.3`, HW436, `GCA_000385355.1`, `PRJNA165561`, `SAMN02256401`, and WGS `ARVZ00000000`.
- `data/gold/organisms.jsonl.gz:13565`: organism `Go0015849`, HW436, taxon 1034768, empty culture-collection field.
- `data/gold/projects.jsonl.gz:13157`: project `Gp0015849` explicitly points to that organism, project, and BioSample.
- `data/gold/analyses.jsonl.gz:17252`: analysis `Ga0026568` points to `Gp0015849`, IMG 2516493022, and decoded GenBank entries ARVZ00000000/GCA_000385355.1. Its own organism field is empty, so the project-to-organism join matters.
- `data/catalog/gtdb_genomes-0010.jsonl.gz:24070`: the exact HW436 RefSeq assembly in the species cluster.
- `data/catalog/allthebacteria.tsv.xz:1018045`: the exact BioSample, but `NOT_PROCESSED`, `asm_fasta_on_osf: 0`, unknown scientific name, and no assembly or run accession. It supplies no available ATB assembly or genome-download link.

The six inspected nucleotide records are four WGS records and
two tmRNA records:

| Versioned accession | Interpretation |
|---|---|
| ARVZ00000000.1 | GenBank WGS master; reported length 1 is a master placeholder |
| ARVZ01000001.1 | GenBank 6,328,722-base contig, source HW436/taxon 1034768 |
| NZ_ARVZ00000000.1 | RefSeq WGS master, not an additional strain genome |
| NZ_ARVZ01000001.1 | RefSeq contig explicitly identical to the GenBank contig |
| HG522412.1 | 375-base third-party tmRNA gene annotation, taxon 1034768 |
| HG784273.1 | 375-nucleotide third-party mature tmRNA, taxon 1034768 |

The tmRNA records explicitly derive from ARVZ01000001.1 and
use gene identifier Gordo_polyi_NBR163. That identifier does
not establish a culture deposit or equivalence to NBRC 16320.
Their PRJEB4570/RNAcentral context and citation to the 2004
tmRNA website paper, PMID 14681369, DOI
`10.1093/nar/gkh102`, are database/annotation provenance,
not a HW436 phenotype experiment.
[HG522412.1](https://www.ncbi.nlm.nih.gov/nuccore/HG522412.1);
[HG784273.1](https://www.ncbi.nlm.nih.gov/nuccore/HG784273.1);
[tmRNA database paper](https://pubmed.ncbi.nlm.nih.gov/14681369/).

Woo et al. (2017), DOI `10.1128/genomeA.00300-17`,
PMID 28473393, directly connects Gordonia sp. HW436 to
ARVZ00000000 in Table 1 and describes Puerto Rican forest-soil
isolation. The whole primary article was read. Its table gives
approximately 6.3 Mb for Gordonia, agreeing with the assembly;
a prose size ordering differs and should not override the
accession-backed assembly metadata. Its other isolates are
not HW436 aliases, and their properties must not be imported.
[Primary genome paper](https://journals.asm.org/doi/10.1128/genomea.00300-17).

The inspected abstract for Frantsuzova et al. (2024),
DOI `10.3390/biology13050339`, PMID 38785821, concerns
experiments on strain 135. Its full comparative table could
not be inspected through the blocked publisher/PMC pages,
so search snippets mentioning HW436 were only a lead to
the primary genome paper, not evidence adopted here.
[PubMed record](https://pubmed.ncbi.nlm.nih.gov/38785821/).

## Completeness

The six other raw enrichment inventories contain no exact target
row; the full native catalogs nevertheless contain the assembly
and source relationships above. Counts of zero in the normalized
inventory do not establish biological absence. In particular,
`strain_count: 0` counts modeled strain entries; it does not
deny that this strain taxon or its genome exists.

The verified assembly/BioSample chain is useful future enrichment,
but no eligible culture-deposit/BacDive-backed strain identity
was established by these bounded searches. Do not invent a
`kgmicrobe.strain:` identifier from the taxon, a bare HW436
designation, GOLD project, or BioSample just to populate a
`StrainEntry`. Any supported extension must preserve the
model's distinct strain, deposit, assembly, project, and sample
identities.

Missing optional record-level literature evidence, definition,
phenotype, and causal-graph slots are not independent defects in
a seeded record. The consequential gap is the rank-aware
interpretation of the existing GTDB mapping, not blanket
population of optional fields. NCBI grounding and the two
strain-specific NCBI aliases should be retained.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: species classification is promoted to strain equivalence.**
   The generated record's `taxonomy_mappings` closeMatch at
   line 43, bare-species exact synonym at lines 46-49,
   identity-derived xref at lines 56-57, and mirrored GTDB
   attestation predicate at line 70 all arise from the same
   scope error. NCBI identifies the target as a strain of
   species 84595; the inspected 17-member GTDB species
   cluster contains only one HW436 assembly and includes
   other named strains. `src/taxonmech/schema/taxonmech.yaml:429`
   describes closeMatch as same-species identity.
   `src/taxonmech/seed.py:451` treats every closeMatch as
   identity without checking rank, and
   `src/taxonmech/seed.py:467` generates the exact synonym/xref.
   `src/taxonmech/seed.py:579` propagates the mapping into
   source attestations. This is a mapping/seeding error,
   not a wrong primary NCBI identifier or a separate genome
   count error.

   Maintained owners: the upstream kg-microbe GTDB mapping
   transform configured by `conf/sources.yaml`, its local
   inventory adapter `src/taxonmech/extract.py:502`, and
   the rank/identity policy in `src/taxonmech/seed.py`.
   `docs/CURATION.md:54` routes source-mapping fixes upstream
   and harmonization-rule fixes to the seeder. Generated
   inventory rows and this YAML are not manual fix owners.

## Recommended Edits

1. Correct the upstream species-to-strain predicate/representation
   and add a rank-aware seeder guard so a broader GTDB species
   does not generate an exact synonym or identity xref for
   HW436. Preserve classification provenance with explicit
   non-equivalence semantics. Do not blindly substitute
   `skos:broadMatch`: the schema defines that direction as
   the record being broader than the source, the opposite
   of this species-to-strain case. Resolve the source mapping
   contract in the maintained transform/adapter and seeder.
2. Retain the exact NCBI identifier, lineage, code, and two
   HW436-specific aliases. Keep the verified count 17 scoped
   to the GTDB source species; do not replace it with one
   simply because only one cluster member is HW436.
3. Add a focused regression in `tests/test_seed.py` for a
   species-level GTDB mapping attached to a strain-level NCBI
   record, including alias preservation, non-equivalence,
   and source-species count semantics.
4. After an authorized upstream/rule fix, follow the documented
   extraction and seeding workflow: dry-run inventory extraction,
   re-extract corrected sources, dry-run the seed, then the
   single-record canary before broader regeneration. Do not
   patch this generated YAML, its source inventories, rendered
   pages, scope, or seed event as a shortcut.
5. Treat exact HW436 genome links as a separate, model-supported
   enrichment opportunity. An unprocessed ATB BioSample is not
   evidence of an available ATB assembly.

## Follow-up Checks

- Run `just test tests/test_seed.py` with the new rank-mismatch regression, then rerun focused schema and strict validation on this record.
- Reinspect the corrected maintained mapping and generated mapping, synonym, xref, and attestation together. Verify that the NCBI strain aliases survive and the species count remains explicitly species-scoped.
- Recheck the exact versioned GCA/GCF pair and explicit sample/project joins if genome enrichment is implemented. Do not infer culture-deposit equivalence from tmRNA names, source taxonomy, or the species representative.
- Run `just verify-corpus`, broader tests, QC, provenance/history checks as applicable, and generated-product checks after authorized regeneration. These were not run by this read-only review.
- Unresolved external-access limits: the live GTDB genome UI and the 2024 publisher/PMC full comparative table were unavailable. The major finding rests on inspected NCBI authorities, local full source rows, pinned RS232 members, and maintained local code, not those inaccessible pages.

## Additional Notes

The initial four rejected candidates are M. tuberculosis
ERR1034768 in `data/bvbrc/bvbrc-0006.jsonl.gz:6456` and
`data/catalog/allthebacteria.tsv.xz:569238`, and
Actinocorallia sp. A-T12471 with BioProject PRJNA1034768
in `data/bvbrc/bvbrc-0018.jsonl.gz:45626` and
`data/catalog/ncbi_genbank-0031.jsonl.gz:29091`.
Their taxon IDs are 1773 and 3089813, not 1034768.

The secondary WGS search intentionally overmatched extended
prefixes. All 15 additional non-target rows were read:
five JAARVZ Listeria seeligeri rows (BV-BRC 0004:40626,
GOLD analyses:371697, GTDB 0013:1991, GenBank 0012:42264,
RefSeq 0003:5181); AAARVZ L. monocytogenes
(GenBank 0003:27735); CAARVZ Streptococcus pneumoniae
(GenBank 0057:21704); DBARVZ Salmonella Typhimurium
(GenBank 0040:36260); DAARVZ Salmonella Ibadan
(GenBank 0009:14273); ABARVZ Salmonella enterica
(GenBank 0017:6168); JBARVZ Methylovirgula
(GenBank 0045:41039 and GTDB 0004:31471); JCARVZ
Enterococcus faecium (RefSeq 0009:9831 and GenBank
0055:19562); and ACARVZ Enterobacter hormaechei
(GenBank 0048:32605). None is the ARVZ HW436 project.

The PubMed HW436 query returned zero, but that is a bounded
index miss, not evidence of no publication. The ARVZ query's
single PMID 28373593 was inspected and rejected as an
unrelated medical article matching author initials. The two
DOI queries resolved the genome paper and the 2024 comparison
paper described above.

Sequence bases and non-source annotation features were not
audited; all six records' reference/comment/source metadata
were read. No gene-function or phenotype claim was inferred
from an annotation or sequencing-center address.
The upstream GTDB transform implementation was not audited;
the local adapter and seeder were. No YAML, inventory,
scope, history, status, generated product, or prior report was
changed. Eukaryota remains outside this review's work scope.
