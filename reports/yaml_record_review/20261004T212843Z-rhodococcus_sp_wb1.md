# YAML Record Review: Rhodococcus sp. WB1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhodococcus_sp_wb1.yaml`
- Started UTC: 2026-10-04T21:23:19Z
- Finished UTC: 2026-10-04T21:28:43Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033922`,
Rhodococcus sp. WB1. It asserts SPECIES, BACTERIA, parent
`NCBITaxon:192944`, ten root-first ancestors, code 11, EXACT grounding,
SEEDED status, one GTDB mapping and source-scoped synonym/xref, zero
inventoried BacDive strains, two attestations and one inline seed event.
No YAML, code, source input, status or history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/rhodococcus_sp_wb1.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/rhodococcus_sp_wb1.yaml`; one file, zero errors. This implements `just validate-strict`, producing `reports/instance_validation_failures.tsv`.
- Bounded identity, lineage, mapped-source, scope, filename and inline-event comparisons passed. A complete pinned GTDB genome-catalog scan independently checked cluster membership and count.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` caps diagnostics, not scope. Bounded comparisons are not byte-level reproduction. Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`; the YAML has no curator graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. The inline event was inspected.
- Unavailable: live GTDB genome and taxon-tree pages returned inaccessible results through the web reader. GTDB conclusions below are pinned-snapshot conclusions, not a claim that the current live release was verified.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221356`, full native scientific-name
object `data/catalog/ncbi_names-0005.jsonl.gz:30696`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033922&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033922)
agree on identifier, label, species rank, bacterial domain, parent and
code 11. All ten lineage IDs match, including root; expanded labels and
ranks agree where supplied. The chain includes Bacillati, Actinomycetota,
Actinomycetes, Mycobacteriales, Nocardiaceae, Rhodococcus and its
unclassified parent. SPECIES is NCBI's placeholder rank, not proof of a
formally named species.

Complete exact-ID type-material, merged-ID and dropped-taxon scans
returned no rows. Live taxonomy supplies no formal synonym, replacement
or type designation requiring a change. WB1 is a laboratory strain
designation, not by itself a registered culture-collection accession.

## Evidence

The NCBITAXON attestation matches the exact identifier, label, one NAME
assertion and snapshot `2026-09-13`. Complete mapped BacDive, LPSN,
GOLD, MediaDive, Madin and BactoTraits inventory scans found no direct
target rows. The backbone scan found no children. Native genome catalogs
described below are distinct from those mapped taxon-attestation tables.

The GTDB mapping exactly matches `data/raw/gtdb_mappings.tsv:1384`:
`GTDB:s__Rhodococcus_aetherivorans`, `skos:closeMatch`, count 37.
`data/raw/gtdb_species.tsv:154134` also gives 37. A full scan of 901,341
pinned GTDB genome rows found 37 unique members of this species cluster,
spanning 16 NCBI taxon IDs. Selected identity, strain, sample, taxonomy,
type and representative metadata were inspected for every member.

Only one cluster member is assigned to NCBI taxon 1033922:
`RS_GCF_001700945.1`, WB1, at
`data/catalog/gtdb_genomes-0007.jsonl.gz:32415`; this native object was
read in full. The representative is `RS_GCF_011058165.1`, DSM 44752,
NCBI taxon 191292, not WB1. WB1 is neither a representative nor a type
genome in this snapshot. Accordingly, 37 is the GTDB cluster count,
not 37 WB1 genomes, strains or deposits. The GENOME attestation repeats
that source-scoped cluster count and does not sum it with the NAME unit.

The closeMatch is defensible as WB1's source-specific placement in this
GTDB species. `src/taxonmech/seed.py:439` and
`docs/HARMONIZATION.md` explain why closeMatch supplies the GTDB
synonym and xref. The source-scoped `Rhodococcus aetherivorans` synonym
is not an NCBI nomenclatural rename or equality of WB1 with every strain
in that species. GTDB places this cluster in Mycobacteriaceae whereas
the NCBI lineage uses Nocardiaceae; the YAML correctly retains the NCBI
backbone and a separate GTDB mapping.

The exact-taxonomy Assembly search returned one assembly:
[GCF_001700945.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_001700945.1/dataset_report),
paired identically with GCA_001700945.1, ASM170094v1, Complete Genome.
Native rows `data/catalog/ncbi_genbank-0001.jsonl.gz:16071` and
`data/catalog/ncbi_refseq-0001.jsonl.gz:5455` were read in full and
agree with live assembly identity. The current total is 6,148,559 bases,
comprising one chromosome and one plasmid. GenBank's project is
PRJNA317416; PRJNA224116 is the RefSeq umbrella, not another isolate.
The live ANI report names a best type-genome match to R. aetherivorans
at 99.19% ANI, while retaining the submitted WB1 taxonomy; this supports
the placement without authorizing a name replacement.

The complete [BioSample SAMN04606842](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN04606842)
object identifies WB1 and taxon 1033922, collected in 2009 from
PCB-contaminated soil in Zhejiang, China. It supplies no registered
culture deposit. Assembly/sequence comments say the organism is available
from the submitting institution; that is not a culture accession.

Exact-taxonomy nuccore search returned eight entries. Identity metadata,
references and source qualifiers were read for all eight, plus all
non-sequence feature qualifiers of the four short records. Genome-wide
gene features and nucleotide/protein strings were not inspected.

- [CP015529.1](https://www.ncbi.nlm.nih.gov/nuccore/CP015529.1) and NZ_CP015529.1: 5,924,026-base chromosome.
- [CP015530.1](https://www.ncbi.nlm.nih.gov/nuccore/CP015530.1) and NZ_CP015530.1: 224,533-base circular plasmid pWB1. RefSeq explicitly identifies its corresponding GenBank sequence.
- [JF775506.1](https://www.ncbi.nlm.nih.gov/nuccore/JF775506.1): 1,488-base partial 16S rRNA sequence, directly submitted April 1, 2011, with an unpublished reference.
- [KT921259.1](https://www.ncbi.nlm.nih.gov/nuccore/KT921259.1), [KT921260.1](https://www.ncbi.nlm.nih.gov/nuccore/KT921260.1) and [KT921261.1](https://www.ncbi.nlm.nih.gov/nuccore/KT921261.1): complete bphC1, bphC2 and bphC3 coding sequences of 945, 903 and 912 bases, respectively, with protein accessions AMB20702.1, AMB20703.1 and AMB20704.1. All explicitly identify WB1/taxon 1033922 and contain unpublished references plus October 15, 2015 submissions.

The full primary [genome announcement](https://pmc.ncbi.nlm.nih.gov/articles/PMC5064098/)
was inspected: PMID 27738025, DOI `10.1128/genomeA.00996-16`,
Xu, Yu and Shen, 2016. It explicitly connects WB1 to CP015529.1 and
CP015530.1 and its soil origin. It describes PCB degradation and
predicted catabolic functions; these are not assertions in this seed.
No phenotype, gene function or causal graph was imported or generalized
to the whole GTDB cluster.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
ID, label, slug and designation patterns included WB1/WB-1/WBI variants.
An initial 352-line search was output-truncated and is not claimed as
fully inspected. A completed refined search tightened designation-token
boundaries to exclude suffixed sample/bin names; all 113 matching
contexts were inspected.

The designation has many homonyms, including Acetobacterium woodii
DSM 1030, Thiomicrospira sp. WB1, Sphingobacterium faecium WB1,
Acinetobacter refrigeratoris and Thermogladius shockii. StrainInfo
WB1 aliases in unrelated taxa do not support a Rhodococcus deposit.
Numeric matches include SAMEA1033922 in Streptococcus pneumoniae and
Salmonella FDA isolate labels, not this taxon.

An independent accession-led search used the assembly, BioSample,
BioProject, eight nucleotide accessions, three protein accessions,
GOLD/IMG identifiers and publication identifiers. All eleven resulting
line contexts were inspected: eight target catalog objects and three
unrelated numeric matches to PMID digits in other sample/assembly IDs.
No target strain-crosswalk, eligible deposit, StrainInfo or
AllTheBacteria linkage was found within these ignored-inclusive roots.

All target native objects were read in full. BV-BRC
`data/bvbrc/bvbrc-0000.jsonl.gz:3252` and line 3253 describe
`1033922.4` (complete genome) and `1033922.6` (plasmid record).
They are not two independent biological isolates or a culture match.
The GOLD chain is explicit:
`data/gold/organisms.jsonl.gz:269644` (Go0364282),
`data/gold/projects.jsonl.gz:133078` (Gp0203386), and
`data/gold/analyses.jsonl.gz:114117` (Ga0176047, IMG 2718218326).
It links the same assembly/sample through the project, but its organism
culture-collection field is empty and its strain field is only WB1.

The registered-authority and full-accession rules in
`docs/HARMONIZATION.md` prevent a taxon/name-only join from creating a
BacDive strain or transferring another cluster member's deposits.
Consequently `strain_count: 0` is correct for the inventoried strain
model despite a real WB1 genome. Empty optional nomenclature, definition,
evidence and graph slots are not required omissions in this seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, source-scoped
mapping/synonym, counts, strain inventory, status and inline provenance
are supported. Live GTDB release verification remains unavailable, not
silently substituted by the pinned catalog.

## Recommended Edits

None. Preserve the generated YAML and SEEDED status. Do not turn the
GTDB representative's deposits into WB1 deposits or label all 37 cluster
members as WB1. Future mapping corrections belong in the maintained
kg-microbe/source transform and `src/taxonmech/extract.py`;
representation changes belong in `src/taxonmech/seed.py` with tests,
and scope changes in `curation/seed_scope.tsv`.

## Follow-up Checks

On source refresh, retry the live
[GTDB genome page](https://gtdb.ecogenomic.org/genome?gid=GCF_001700945.1)
and [species tree](https://gtdb.ecogenomic.org/tree?r=s__Rhodococcus%20aetherivorans),
then recompute the cluster count and WB1 membership. Recheck the exact
assembly/BioSample for a newly explicit culture deposit before creating
a strain join. After authorized input changes, regenerate and run
focused validators plus full `just verify-corpus`.
No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13812` locks the slug;
`curation/seed_scope.tsv:66003` supplies the September 13, 2026 date
and two-source reason. The event at `2026-09-13T17:54:04Z` exactly
reproduces the GTDB/NCBITAXON source list and reason. Ignored-inclusive
filename and history-content searches found no prior target report or
target-specific history artifact.

Source discrepancies outside the YAML were retained: the paper gives a
5,924,027-base chromosome versus 5,924,026 in the sequence records,
and HiSeq/PacBio RS sequencing versus MiSeq/PacBio in assembly metadata.
Its reported protein predictions also differ from the dated GenBank
and RefSeq annotation counts. These were not adjudicated as biological
claims or copied into the YAML. The sequence records still mark their
submission reference unpublished; the later paper independently supplies
the explicit accession link.

iModulonDB is not applicable: this YAML asserts no gene, regulator,
expression module or mechanism. No paid research, outside contact,
GitHub mutation, generator run, status promotion or history event occurred.

