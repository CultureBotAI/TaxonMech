# YAML Record Review: Pseudomonas sp. StFLB209

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_stflb209.yaml`
- Started UTC: 2026-10-03T19:49:00Z
- Finished UTC: 2026-10-03T19:50:41Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1028989`,
Pseudomonas sp. StFLB209. Rank is `SPECIES`, domain `BACTERIA`,
parent `NCBITaxon:196821`, genetic code 11, grounding `EXACT`,
mapping status `SEEDED`. The record contains ten lineage entries,
one GTDB mapping, one GTDB-attributed synonym, one xref, zero
strains, two attestations and one embedded seed event. It asserts
no nomenclature, strain-linked genomes or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_stflb209.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_stflb209.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison matched identity, rank,
  parent, code and all ten lineage objects. No children were found.
  Complete source-inventory scans, scope/path rows, mapping/counts
  and embedded seed reason were checked and agree.
- `just verify-corpus`: Not checked; full-corpus-only. Bounded
  comparisons do not replace this gate. Full QC, global provenance/
  hash replay, rendered products and exports were not audited.
  Primary archives and genome FASTAs were not downloaded or verified.
- Ignored-inclusive ID, label and slug searches found no standalone
  target history event. Strict validation checked the embedded event;
  standalone history validation had no target. Graph/product gates
  are not applicable because no graph is asserted.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:219382` and the fully read native
scientific-name object at
`data/catalog/ncbi_names-0005.jsonl.gz:28450` support the exact
ID, name, species rank and 2026-09-13 taxonomy snapshot. Raw NCBI
exact, related and broad synonyms are empty, with no retirement
target. The YAML's Aquipseudomonas synonym is explicitly from GTDB,
not an NCBI equivalent name.

Inspected live
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1028989&retmode=xml)
and
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1028989)
confirm identity, species rank, code and parent. Datasets lists
all ten ancestor IDs, including root. The complete chain is root,
cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas and unclassified Pseudomonas. No alternate name was
supplied. Exact NCBI grounding and bacterial placement are supported.

NCBI's Pseudomonas placement and GTDB's Aquipseudomonas placement
are different source classifications. The record correctly preserves
NCBI lineage and presents GTDB separately, as required by
`docs/HARMONIZATION.md`; it does not silently reconcile the two.
The source species rank is retained despite the isolate-like label.

## Evidence

**GTDB membership and count.** `data/raw/gtdb_mappings.tsv:1248`
and `gtdb_species.tsv:11454` supply
`GTDB:s__Aquipseudomonas_sp000829415`, the corresponding label,
`skos:closeMatch` and count 4. An ignored-inclusive search across
the complete GTDB native catalog found exactly four cluster members,
all read fully:

| Native catalog location | GTDB accession | Source isolate / NCBI taxon |
|---|---|---|
| `gtdb_genomes-0006.jsonl.gz:1841` | RS_GCF_000829415.1 | StFLB209 / 1028989; representative |
| `gtdb_genomes-0015.jsonl.gz:38676` | RS_GCF_024129895.1 | 21LCFQ02 / 2957505 |
| `gtdb_genomes-0006.jsonl.gz:49227` | RS_GCF_024129905.1 | 21LCFQ010 / 2957506 |
| `gtdb_genomes-0008.jsonl.gz:13884` | RS_GCF_024584215.1 | LJDD11 / 2931984 |

All table paths are under `data/catalog/`. The target object
explicitly names StFLB209, taxon/species 1028989, GCA_000829415.1,
SAMD00019511 and the Aquipseudomonas cluster. The other three are
different isolates and samples, not additional StFLB209 genomes.
Thus count 4 is a species-cluster count and is not contradicted by
the live NCBI target assembly count of one.

The source close mapping supplies the GTDB-attributed synonym and
xref under `src/taxonmech/seed.py:437`. This preserves a source
classification, not identity equivalence among all four NCBI taxa
or all four assemblies. The supplied KGX predicate is retained;
no new cross-taxonomy reconciliation was inferred.

**NCBI assembly evidence.** Complete native objects at
`data/catalog/ncbi_genbank-0000.jsonl.gz:31340` and
`ncbi_refseq-0000.jsonl.gz:27147` supply GCA_000829415.1 and
GCF_000829415.1, explicitly paired, with StFLB209, taxon 1028989,
complete-genome level, SAMD00019511 and source-specific projects
PRJDB3085 and PRJNA224116. Annotation counts were not conflated
or promoted to taxon-wide biological claims.

Inspected live
[NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000829415.1/dataset_report)
confirms the current GenBank accession, explicit current RefSeq
partner, strain, assembly level, BioSample and GenBank project.
Pairing was not inferred by accession-prefix replacement. BioSample
environmental attributes and a nearest ANI match do not create
culture-deposit identity or authorize nomenclature transfer.
PMID 25323715 in native assembly metadata is not cited by the YAML
and was not used to assert literature or experimental findings.

**BV-BRC and GOLD context.** The full BV-BRC object at
`data/bvbrc/bvbrc-0000.jsonl.gz:3003` explicitly names genome
1028989.3, GCA_000829415.1, PRJDB3085, SAMD00019511 and
AP014637.1. These remain typed source identifiers; they do not
establish a qualifying culture-collection deposit.

Complete native GOLD objects at
`data/gold/organisms.jsonl.gz:59159`, `projects.jsonl.gz:60674`
and `analyses.jsonl.gz:43780` preserve
Go0106352 -> Gp0106352 -> Ga0069486. The organism supplies
StFLB209 and 1028989; the project supplies PRJDB3085 and
SAMD00019511; the analysis supplies GCA_000829415.1,
unversioned AP014637 and IMG 2636415557. The analysis's direct
organism field is empty but its sole explicit project resolves
to Go0106352. Source accession versions were not rewritten.

The organism's culture-collection field is empty. The pinned CAFI
matcher returns an empty normalized identifier for bare StFLB209,
and the complete BacDive inventory supplies no target or descendant
strain. The known native genome/project chain therefore does not
license adding strain-linked genomes to this YAML.

GOLD's taxon attestation comes from KGX, whereas its native workbook
supplies culture-linked relationships (`docs/HARMONIZATION.md:44`).
Native organism census presence is not by itself a missing
KGX-derived attestation under this pipeline.

**Attestations and audit.** The record correctly carries NCBITAXON
1 NAME with snapshot 2026-09-13 and GTDB 4 GENOME with the exact
source mapping. Units are not summed.
`data/taxa/PATHS.tsv:11556` pins the slug;
`curation/seed_scope.tsv:65997` admits the taxon on 2026-09-13
with the two-source reason. The event at 2026-09-13T17:54:04Z
correctly retains seed_from_sources, SEEDED_FROM_SOURCES, both
source names and the exact scope reason. Status remains `SEEDED`.

## Completeness

Absence checks included ignored files. Digit-bounded ID, label,
slug, StFLB209, GTDB species and BioSample searches covered raw
inventories, curation, history, native catalog/BacDive/BV-BRC/GOLD/
SeqCode/StrainInfo projections, ATB/StrainInfo TSV/compressed
overlays and the full ATB catalog. Eight target-native objects and
three additional GTDB cluster objects were read fully. Four foreign
numeric candidates were parsed and screened by typed identity and
matching key paths, not assigned foreign-record review verdicts.

Complete source-inventory scans found no target BacDive, LPSN,
GOLD KGX, MediaDive, Madin or BactoTraits entry. Further exact
assembly, sample and GOLD-ID searches found no target row in the
raw/ATB/StrainInfo relationship overlays. No standalone history
event was found within the ignored-inclusive history search.

The only full ATB candidate at
`data/catalog/allthebacteria.tsv.xz:57480` is Streptococcus
pneumoniae sample SAMEA1028989, run ERR064033. The same foreign
sample explains the four native numeric matches, whose organism
is S. pneumoniae / SMRU2528, not Pseudomonas. A BioSample numeric
suffix is not a taxon ID. No ATB entry matched StFLB209, its GTDB
species or target sample SAMD00019511. This describes the local
snapshot and does not claim that no public target genome exists.

No consequential missing eligible representation was identified.
Optional nomenclature and strain links should remain empty without
the required evidence. iModulonDB is not applicable: the record
names no gene, regulator, pathway, stress response, trait or
expression dataset. No graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Retain the visible NCBI/GTDB classification difference,
cluster-count scope and strict culture-deposit boundary. Future
enrichment belongs in maintained source and overlay pipelines before
`src/taxonmech/seed.py` emits links. GOLD attestation changes belong
in its KGX inventory pipeline. Do not hand-edit generated YAML or
infer culture/genome equivalence from a shared taxon or cluster.

## Follow-up Checks

No corrective check is required. An authorized refresh should recheck
the target identity, all GTDB cluster members, whole eligible culture
identifiers and explicit organism/project/assembly/sample chains,
then rerun both focused validators. Corpus-wide reproduction and
publication assurance additionally require `just verify-corpus` and
full QC, neither performed here.

## Additional Notes

The GTDB genome page was inaccessible through the web tool. The
complete pinned primary GTDB objects support the source classification;
live NCBI taxonomy and assembly responses supplied independent
identity checks. Live status of every external source record and
genome contents was not audited.

Only this new report was manually written. Strict validation wrote
its standard diagnostic. No YAML, source, prior report, history or
status was changed. No generator, refresh, paid research, GitHub
action or cross-repository edit occurred. Eukaryota was not re-reviewed.
