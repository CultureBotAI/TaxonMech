# YAML Record Review: Streptococcus didelphis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptococcus_didelphis.yaml`
- Started UTC: 2026-10-03T19:22:07Z
- Finished UTC: 2026-10-03T19:28:58Z
- Verdict: pass

## Target

Read all 918 lines of the generated `TaxonRecord` for
`NCBITaxon:102886`. Rank is `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:1301`, genetic code 11, grounding `EXACT` and mapping
status `SEEDED`. The record has nine lineage entries, one related
authority synonym, one LPSN nomenclature entry, one GTDB close mapping,
two xrefs, six source attestations and one embedded seed event.

One BacDive type-strain record is listed, with `classified_as` preserving
the child taxon `NCBITaxon:1123301`. Its 9 assembly assertions,
7 other genome-record assertions and 37 related-record assertions
are provenance-bearing relationships, not 53 distinct genomes.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptococcus_didelphis.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptococcus_didelphis.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured reads reproduced identity, all nine lineage objects,
  the authority synonym and the complete descendant subtree. The only
  descendant is DSM 15616, `NCBITaxon:1123301`; the complete BacDive
  inventory supplies exactly the one listed strain through that child.
- Complete field-by-field multiset comparison matched all 9 assembly
  assertions, all 6 non-ATB genome assertions and all 37 related
  assertions to the raw and StrainInfo tables. Nested StrainInfo
  evidence was parsed, not compared as opaque text. The ATB record's
  metadata, six sample assertions and five source-matched genome
  crosslinks were checked separately and agree.
- All 16 StrainInfo assertions were independently compared to the
  native record's own deposits, statuses, DOI, classifications and
  explicit same-deposit sequence membership. All checks passed.
- `just verify-corpus`: Not checked; full-corpus-only. The bounded
  comparisons above do not replace corpus reproduction. Full QC,
  global provenance/hash replay, rendered products and exports were
  not audited. Genome FASTAs and archive contents were not downloaded.
- Ignored-inclusive ID, label, slug and strain searches found no
  standalone target history entry. Strict validation checked the
  embedded event; standalone history validation had no target.
  Graph/product gates are not applicable: no graph is asserted.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18157` supports the species identity,
code, authority synonym and 2026-09-13 snapshot. The chain is root,
cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli,
Lactobacillales, Streptococcaceae and Streptococcus. The child row at
line 243025 supports the strain-level classification and parentage.
The complete scientific-name and authority objects at
`data/catalog/ncbi_names-0000.jsonl.gz:38162` and line 38163, and the
child scientific-name object at `ncbi_names-0006.jsonl.gz:7049`, agree.

Inspected live
[NCBI EFetch taxonomy for both taxa](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=102886,1123301&retmode=xml)
confirms both identities, their ranks, codes and parent chains. The
species authority is correctly related, not an exact synonym for a
different species. Type-material designations are not species synonyms.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/102886)
also confirms all nine ancestor identifiers, including root, and the
sole child. Exact grounding and the bacterial domain are supported.

[LPSN record 781317](https://lpsn.dsmz.de/species/streptococcus-didelphis)
confirms the name, authorship, valid publication, correct-name status,
four listed culture-collection deposits and AF176103. The local
nomenclature fields match `data/raw/lpsn_names.tsv:20079`, including
the source legitimacy flag, publications and sequence identifier.
The xrefs do not assert assembly equivalence or replace the NCBI lineage.

## Evidence

**Nomenclature and type identity.** The full primary BacDive projection
at `data/bacdive/records.jsonl.gz:14642` and the inspected
[BacDive 14814 page](https://bacdive.dsmz.de/strain/14814) support
designation 94-11374-1, the five carried culture/alias values, species
102886, child strain 1123301 and type status. Four deposits intersect
the LPSN type list. `data/raw/bacdive_strains.tsv:14643` reproduces
the listing. The count is one source strain record, not five strains.

The full
[PubMed XML for PMID 10758886](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10758886&retmode=xml)
links DOI 10.1099/00207713-50-2-759 to the original 2000 species
description and identifies ATCC 700828 as the type. Its accession list
includes AF176103. Inspected
[Crossref metadata](https://api.crossref.org/works/10.1099/00207713-50-3-951)
identifies the other DOI as the IJSEM notification list, volume 50,
issue 3, pages 951-953. LPSN explicitly associates that list with
this name. Publisher full texts were not available through the web
tool; no quotation or experimental claim was inferred from them.

**GTDB and NCBI assemblies.** The three complete GTDB native objects
are `gtdb_genomes-0000.jsonl.gz:4531`, line 8799, and
`gtdb_genomes-0001.jsonl.gz:2175`. They support the species mapping
and count 3 in `data/raw/gtdb_mappings.tsv:1245` and
`gtdb_species.tsv:168762`. Only `RS_GCF_000380005.1` names the
eligible DSM 15616 deposit; the other two are LBVP100/21 and
LBVP101/21 source isolates. The species count is not a genome count
for every deposit and need not equal a newer NCBI species-wide count.

The complete primary NCBI objects at
`data/catalog/ncbi_genbank-0000.jsonl.gz:10751` and
`ncbi_refseq-0000.jsonl.gz:9413` explicitly supply GCA_000380005.1,
GCF_000380005.1, DSM 15616, taxon 1123301, SAMN02256413 and their
source-specific projects PRJNA165435 and PRJNA224116. The manifest
at `data/raw/MANIFEST.yaml:79` and line 86 identifies the named
GenBank/RefSeq snapshot inputs. Live
[NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000380005.1/dataset_report)
confirms the current GenBank accession, explicit RefSeq partner, scaffold
level, strain, BioSample and GenBank project. Pairing comes from NCBI,
not prefix replacement or co-occurrence. Unversioned GCA_000380005
from BacDive and StrainInfo remains unversioned.

**BV-BRC, IMG and GOLD.** The complete BV-BRC object at
`data/bvbrc/bvbrc-0000.jsonl.gz:13221` explicitly links DSM 15616
to genome 1123301.3, GCA_000380005.1, SAMN02256413 and PRJNA165435.
BacDive's native genome row retains reference 66792 and independently
supplies the unversioned GenBank accession, BV-BRC 1123301.3 and
IMG 2515154028. These are source assertions, not an experimental
demonstration that every deposit or database entry has identical sequence.

All relevant GOLD objects were read in full. Organism
Go0013342 (`data/gold/organisms.jsonl.gz:11763`) explicitly names
DSM 15616 in both supported culture fields. Project Gp0013342
(`projects.jsonl.gz:11590`) names that organism, BioSample and
BioProject. Analysis Ga0025241 (`analyses.jsonl.gz:16096`) references
that project and explicitly supplies GCA_000380005.1 and IMG 2515154028.
Its direct organism field is empty, not conflicting; the sole project
resolves the chain. Two source culture fields legitimately yield separate
provenance assertions. Go0626930 and Go0626931 at organism lines
457516 and 457517 support CCUG 45419 and ATCC 700828 related records,
without invented projects or genomes.

**StrainInfo.** The full native object at
`data/straininfo/records.jsonl.gz:32332` agrees with the inspected
[live SI-ID44160 API response](https://api.straininfo.dsmz.de/v2/data/strain/max/44160).
The record-version DOI is 10.60712/SI-ID44160.3, the strain is published,
and the four matched deposits are available, nondeprecated and have
nonerroneous relations. They are ATCC 700828 / SI-DP118550,
CCUG 45419 / SI-DP118552, DSM 15616 / SI-DP303882 and
CIP 106980 / SI-DP305423. All four match the pinned CAFI authority
and full accession templates. Source BacDive ID 14814 agrees.

Each sequence explicitly names its own matched deposit:

| Deposit | Explicit sequence evidence |
|---|---|
| ATCC 700828 | AY123727, cpn60; DQ303185, 16S rRNA |
| DSM 15616 | GCA_000380005, genome; DQ118677, 16S rRNA |
| CIP 106980 | DQ232447, rpoB; DQ232545, sodA; EU003638, groEL; EU003790, gyrB |
| CCUG 45419 | Deposit/strain context only; no transferred sequence |

Inspected
[NCBI nucleotide metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AF176103,AY123727,DQ118677,DQ232447,DQ232545,DQ303185,EU003638,EU003790&rettype=gb&retmode=xml)
confirms all eight cited markers, their definitions, taxon, strains and
gene/rRNA feature annotations. AF176103 names the original W94-11374-1
type. Live versions were not substituted for source-unversioned IDs.
The seven imported StrainInfo markers remain nucleotide related records,
not genome assemblies or phenotype assertions. Sequence annotations
were inspected; no sequence alignment or experimental validation was run.

**AllTheBacteria.** The entire matching native metadata row at
`data/catalog/allthebacteria.tsv.xz:1018055` equals the overlap row
at `data/atb/assemblies.tsv:2468`. It supplies SAMN02256413,
SRR3947696, ERZ4066122, available FASTA, PASS assembly/HQ filters,
dataset 661k, the exact SeqKit sum, source species and supplied
download/archive metadata. Release 2025-05 and snapshot-scoped
`atb.assembly:202505.SAMN02256413` remain distinct from the BioSample.

`data/atb/strain_links.tsv:2102` contains six original sample assertions,
each equal to its YAML BIOSAMPLE related record. Genome links at
`data/atb/genome_links.tsv:8896` through line 8900 preserve five typed
genome IDs and explicit source-matched evidence pairs. These assert
`shares_biosample`, not sequence equivalence. Live
[ENA analysis ERZ4066122](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ4066122)
explicitly names the same BioSample and run;
[ENA run SRR3947696](https://www.ebi.ac.uk/ena/browser/api/xml/SRR3947696)
confirms its public DSM 15616 context. The ENA file MD5 is not the ATB
SeqKit sum. No FASTA/archive availability or checksum replay is claimed.

**Attestations and audit.** Counts agree with maintained inputs:
NCBI 1 NAME; LPSN 1 NAME; GTDB 3 GENOME; BacDive 1 STRAIN;
GOLD 4 direct ORGANISM (`gold_organisms.tsv:356`); Madin 2 direct
TRAIT_ASSERTION (`madin_taxa.tsv:541`). The child-only MediaDive
count 2 and Madin count 4 are correctly not promoted to the species.
Madin's count is coverage metadata, not two asserted biological traits.

`data/taxa/PATHS.tsv:11419` pins this slug. Scope line 21027 admits
the species on 2026-09-12. The embedded 2026-09-13T17:54:04Z event
correctly carries seed_from_sources, SEEDED_FROM_SOURCES, the six
generated source names and the exact retained five-source scope reason.
The latter is historical scope text, not a recalculated total that must
include the descendant BacDive contribution. `SEEDED` remains appropriate.

## Completeness

Absence and candidate checks included ignored files. Complete ID, label,
slug and local-strain searches covered `data/raw/`, `curation/` and
`history/`; no additional unexamined source file or standalone history
event was returned. Full structured reads covered the backbone subtree,
seven source inventories, raw assembly/genome/related tables and the
StrainInfo/ATB overlays. Full-source JSONL searches covered catalog,
BacDive, BV-BRC, GOLD, SeqCode and StrainInfo, with additional deposit
and explicit taxon-field searches. Ten NCBITaxon prefix hits denoted
1028860-1028869, not 102886; their complete name objects were read and
rejected. Source spelling and typed identity, not substring membership,
controlled the decision.

The whole native species-name result set was read. It includes the
SeqCode name index object at `data/seqcode/names.jsonl.gz:19681`,
all three GTDB genomes, eleven GenBank/RefSeq pairs and five BV-BRC
genome objects. Other species isolates, including LBVP100/21,
LBVP101/21, SS1648, SS1649, PS110_23, B69_22, B65_22, Z1073A,
PS30_22 and Z845, have no inspected qualifying deposit match to this
BacDive strain. Their shared species is not sufficient. Literature
PMIDs appearing only on those unlinked objects were not used as target
evidence or independently reviewed.

GOLD Go0106477 / Gp0106477 names GTC 02045, not a deposit in the
local BacDive inventory. Go0626929 names WADDL 94-11374-1 without
an eligible culture authority. Both remain part of the direct GOLD
organism census, not imported strain-genome links. No culture chain was
invented for them. The full ATB catalog also has three other same-species
samples, SAMD00009235, SAMEA103957228 and SAMN11268216; the inspected
strain has no eligible prior BIOSAMPLE assertion for these samples.

The live LPSN type list additionally names W94-11374-1 and WADDL
94-11374-1. The schema at `src/taxonmech/schema/taxonmech.yaml:391`
defines the nomenclature slot as culture-collection numbers. NCBI
identifies these extra labels as personal/strain designations, and neither
passes the pinned CAFI collection matcher. WADDL is already preserved
as a BacDive alias. Their absence from the four collection-number
nomenclature entries is not treated as a defect or license to use them
as genome-join keys.

StrainInfo also has LMG 21595 / SI-DP378998 and three associated
markers. The local BacDive culture inventory does not contain that
deposit; StrainInfo grouping alone cannot introduce it or transfer its
sequences. These are possible future source-enrichment candidates, not
missing eligible imports under the current contract.

The structured iModulonDB runner was found in the local
culturebotai-claw checkout. `kg-microbe-sources imodulondb datasets`
succeeded after network escalation and returned no S. didelphis dataset.
S. pneumoniae and S. pyogenes datasets are not transferable. iModulonDB
is therefore not applicable to these deposit-specific marker references;
absence is not negative biological evidence. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Retain the supported species/child distinction, source
counts, typed identifiers, unversioned accessions, deposit-specific
sequence evidence, explicit GOLD chain and ATB sample evidence.

Any future enrichment of aliases or collection deposits belongs in the
maintained source pipelines and inventories. Nomenclature flows through
`src/taxonmech/extract.py:420` from kg-microbe LPSN inputs to
`data/raw/lpsn_names.tsv`, then `src/taxonmech/seed.py:405`.
Do not patch generated YAML, infer new join keys from personal aliases,
or import LMG sequences without an authorized eligible deposit path.

## Follow-up Checks

No corrective check is required. An authorized source refresh should
recheck whole culture identifiers, source-specific counts, explicit
organism/project chains and same-deposit sequence evidence; rebuild
affected overlays through their documented workflows and rerun both
focused validators. Corpus-wide reproduction and publication claims
additionally require `just verify-corpus` and full QC, not run here.

## Additional Notes

Browser retrieval of GTDB, GOLD, DSMZ and StrainInfo pages failed.
Inspected pinned primary projections support the relevant database
assertions; live StrainInfo, NCBI and ENA APIs supplied independent
checks where noted. Live status of every external database page was
not proved. NCBI/PubMed browser responses and publisher DOI retrieval
were incomplete, so the XML and Crossref results above were used.

Local runner discovery encountered permission-denied directories outside
this repository. After the runner was located, both discovery processes
were explicitly terminated and confirmed terminal; no global filesystem
absence was inferred. All record searches and validators completed.
No full primary-archive or global provenance replay was performed.

The only manual write is this new report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or review
status was changed. No generator, refresh, paid research, GitHub action
or cross-repository edit occurred. Eukaryota was not re-reviewed.
