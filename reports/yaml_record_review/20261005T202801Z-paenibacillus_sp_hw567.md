# YAML Record Review: Paenibacillus sp. HW567

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_hw567.yaml`
- Started UTC: 2026-10-05T20:19:37Z
- Finished UTC: 2026-10-05T20:28:01Z
- Verdict: pass

## Target

The entire 78-line generated `TaxonRecord` was read twice.
It denotes `NCBITaxon:1034769`, Paenibacillus sp. HW567,
rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:185978`, genetic code 11, `EXACT` grounding,
`SEEDED` status, and `strain_count: 0`. Its three sources
are NCBITAXON, GTDB, and MADIN.

Owning rows are `data/raw/ncbitaxon_taxa.tsv:221689`,
`data/raw/gtdb_mappings.tsv:1397`,
`data/raw/madin_taxa.tsv:651`, and
`curation/seed_scope.tsv:36160`.
`data/taxa/PATHS.tsv:14159` and
`curation/legacy_page_paths.tsv:841` agree with the target.
This review does not change any generated record.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/paenibacillus_sp_hw567.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/paenibacillus_sp_hw567.yaml --out /private/tmp/phw-strict-20261005.tsv`: exit 0; one file, zero error files and zero error rows. The TSV was read and contains only its header.
- Structured comparisons checked the complete backbone row, ten ancestors, synonyms, PATHS, scope, source attestations, and seed event. Seven raw enrichment inventories and exact type-material, merged-ID, and dropped-record tables were checked.
- `rg --no-ignore --hidden -n -z -i` searched the target ID, slug, and HW567 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All 21 candidates were read fully: 19 target/source-related rows and two unrelated run-identifier matches.
- A secondary search for the assembly/WGS/BioSample/GOLD/IMG identifiers, DSM 25994, StrainInfo IDs, and cmc22 returned 38 rows: 12 already seen and 26 additional rows. All additional rows were read with native TSV headers or full decoded JSON. Eight concern the deposit/sample or the separately named cmc22 taxon; 18 are namespace, substring, or numeric collisions.
- A further ignored-inclusive search for KB910518 and PD240497 across the same ten roots found no row. Separate ignored-inclusive content and filename searches in `reports` and `history`, covering the target and discovered accessions/aliases, found no prior target report or separate target history artifact before this report.
- The exact GTDB species row, its only raw mapping, and its entire one-member RS232 cluster were inspected. The complete relevant strain entry under the source-classifying record `data/taxa/bacteria/paenibacillus_sp.yaml` was read; this was a bounded cross-reference check, not a review of that entire separate record.
- Live NCBI Taxonomy EFetch/Datasets, Assembly ESummary/Datasets, exact nonexpanded Assembly/Nuccore searches, and metadata for all 15 nucleotide results were inspected. The separate cmc22 taxonomy identifier, live BacDive and DSMZ pages, the primary genome article, four PubMed searches, and three publications' metadata/abstracts were checked.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused comparisons do not establish whole-corpus reproduction.
- The configured upstream Madin edge file could not be opened, and an ignored-inclusive filename search in the configured kg-microbe `data` root found no matching Madin edge/CSV/TSV/ZIP input. The committed count was checked, but its original edge was not independently reproduced.
- iModulonDB and curator-added graph ID/label checks are inapplicable: the YAML asserts no gene, regulator, protein, phenotype, transcriptomic result, or causal graph. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

Live NCBI agrees with the exact scientific name, species rank,
parent 185978, genetic code 11, and the root-first lineage
`1 > 131567 > 2 > 1783272 > 1239 > 91061 > 1385 > 186822 > 44249 > 185978`.
All labels and normalized ranks match: root, cellular organisms,
Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales,
Paenibacillaceae, Paenibacillus, and unclassified Paenibacillus.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034769);
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034769).

The exact scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31079`.
The backbone contains no target synonyms, retirement target, or
direct children. Exact type-material, merged-ID, and dropped-record
checks found no target row. NCBI species rank for this provisional
isolate-named taxon does not imply a validly published binomial or
a type-strain designation.

The GTDB species `GTDB:s__Paenibacillus_AQ_sp000374185`
has exactly one local RS232 member,
`RS_GCF_000374185.1`, the HW567 representative. That row
explicitly supplies both NCBI taxon and species taxon 1034769.
The exact species source row,
`data/raw/gtdb_species.tsv:133520`, and its only mapping,
`data/raw/gtdb_mappings.tsv:1397`, agree on count 1.
This supports the species-level closeMatch in the inspected
snapshot. The source-attributed display synonym
"Paenibacillus AQ sp000374185" follows the seeder's label
normalization; it is not an independently published species name.

The complete member row is
`data/catalog/gtdb_genomes-0013.jsonl.gz:7368`.
Its source hierarchy uses Paenibacillus_AQ and Paenibacillales,
while the NCBI backbone uses Paenibacillus and Caryophanales.
Keep those source hierarchies separate. The GTDB representative
flag is not a type-strain flag: type-material designation is
unspecified, and the strain-identifier field contains only HW567.
RS232 provenance was read in `data/catalog/PRIMARY.json:823`.
The live GTDB genome UI was unavailable; this mapping check
rests on the pinned complete metadata, not a claimed live UI check.
[GTDB RS232 release](https://data.gtdb.ecogenomic.org/releases/release232/232.0/).

## Evidence

All three attestations match the committed inventories:
NCBITAXON count 1 `NAME`, GTDB count 1 `GENOME` with
the same source ID/label/predicate, and MADIN count 1
`TRAIT_ASSERTION`. The NCBI snapshot is 2026-09-13.
The 2026-09-12 scope entry and the
2026-09-13T17:54:04Z `seed_from_sources` /
`SEEDED_FROM_SOURCES` event agree; scope-entry time and
seed time need not be identical.

The Madin count comes from `data/raw/madin_taxa.tsv:651`.
`src/taxonmech/extract.py:412` counts taxon-subject source
edges, and `src/taxonmech/seed.py:616` carries the count.
The upstream path and pinned hash are documented in
`data/raw/MANIFEST.yaml:64`. Madin et al. is a multi-source
trait compilation, not proof that HW567 underwent one particular
experiment. Its publication metadata/abstract resolve DOI
`10.1038/s41597-020-0497-4`, PMID 32503990.
The YAML asserts no specific phenotype; none was inferred from
the single count. Original-edge reconstruction remains unperformed
because that local input was unavailable.
[Madin compilation](https://pubmed.ncbi.nlm.nih.gov/32503990/).

The exact query `txid1034769[Organism:noexp]` returns
one Assembly item, UID 665358. NCBI explicitly pairs
`GCA_000374185.1` and `GCF_000374185.1` as identical,
current GenBank/RefSeq counterparts, ASM37418v1, strain HW567,
BioSample `SAMN02441697`, GenBank project `PRJNA170089`.
The RefSeq umbrella `PRJNA224116` is not strain-unique.
Assembly size is 6,836,219 bases including 900 gap bases,
6,835,319 ungapped bases, ten contigs, and one scaffold.
One scaffold does not make this a complete chromosome.
[NCBI assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000374185.1/).

The native GenBank and RefSeq rows are
`data/catalog/ncbi_genbank-0000.jsonl.gz:10492` and
`data/catalog/ncbi_refseq-0000.jsonl.gz:9180`.
BV-BRC `data/bvbrc/bvbrc-0000.jsonl.gz:3282` explicitly
links genome `1034769.3` to GCA_000374185.1,
ARFI00000000, PRJNA170089, and SAMN02441697.
These are source-supported accession relationships, not
identity inferred merely from a shared taxon.

The GOLD chain was read in full:

- `data/gold/organisms.jsonl.gz:13327`: `Go0015291`, HW567, taxon 1034769, empty culture-collection field.
- `data/gold/projects.jsonl.gz:12994`: `Gp0015291` explicitly joins that organism to PRJNA170089 and SAMN02441697.
- `data/gold/analyses.jsonl.gz:17278`: `Ga0026595` links to Gp0015291, IMG `2516493025`, and decoded GenBank entries ARFI00000000/GCA_000374185.1. The analysis's direct organism field is empty; the explicit project chain matters.

Go/Gp/Ga identifiers denote organism/project/analysis records,
not extra genomes. The attempted BioProject browser page was
unavailable, but the project and sample links were independently
read in the live NCBI assembly metadata and native GOLD rows.

BacDive supplies a genuine culture bridge, with an important
classification distinction. The full native record
`data/bacdive/records.jsonl.gz:82678` and live
`bacdive:160442` page associate HW567 and cmc22 with
DSM 25994. The general taxon is 58172, Paenibacillus sp.,
whereas its automatically annotated genome entry supplies
taxon 1034769 and GCA_000374185, BV-BRC 1034769.3,
and IMG 2516493025. Native type-strain status is "no".
Genome-link provenance is reference 66792; machine-predicted
phenotypes on the live page are not culture experiments.
[BacDive 160442](https://bacdive.dsmz.de/strain/160442).

The DSMZ deposit page independently gives HW567 and cmc22,
a Puerto Rican forest collection in 2010, and the explicit
WGS accession ARFI00000000. This is stronger deposit-to-WGS
evidence than an unqualified name match.
[DSM 25994](https://www.dsmz.de/collection/catalogue/details/culture/DSM-25994).

The source classification is retained in
`data/raw/bacdive_strains.tsv:82679` and
`data/raw/culture_collection_strains.tsv:74182`.
The relevant strain entry already exists in
`data/taxa/bacteria/paenibacillus_sp.yaml:6714`, under
`NCBITaxon:58172`. It carries the unversioned BacDive
assembly accession, typed IMG/BV-BRC links, and StrainInfo
strain/deposit references. The raw genome rows are
`data/raw/strain_assemblies.tsv:69986` and
`data/raw/strain_genome_records.tsv:54608` /
`data/raw/strain_genome_records.tsv:54609`.
The original unversioned accession is correctly preserved;
a version from another authority must not silently overwrite it.

StrainInfo's complete native row,
`data/straininfo/records.jsonl.gz:302690`, distinguishes
SI-ID 404801 from SI-DP 911970, designation DSM 25994,
available status, non-type status, and record DOI
`10.60712/SI-ID404801.2`. Its classification is the genus
Paenibacillus, NCBI 44249, not an asserted taxonomic merge
with either provisional species record. The row has no
sequence entries. The corresponding deposit match is in
`data/straininfo/strain_links.tsv:59749`; complete typed
references at `data/straininfo/related_records.tsv.gz:140457`
and `data/straininfo/related_records.tsv.gz:140458` were
read, including their evidence JSON. The live StrainInfo
page yielded no usable record body; these details are from
the pinned native row, not a live StrainInfo verification.

NCBI separately retains `NCBITaxon:1192161`,
Paenibacillus sp. cmc22, at species rank under the same
unclassified parent. Its current Taxonomy/Datasets identity
and local backbone/name/scope rows were checked.
The deposit sources support the culture aliases, but do not
authorize merging 1192161, 1034769, and the general taxon
58172. Preserve that cross-source distinction.
[NCBI cmc22 taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1192161).

The exact ATB sample row,
`data/catalog/allthebacteria.tsv.xz:1029885`, has
SAMN02441697 but `NOT_PROCESSED`, no available FASTA,
unknown scientific name, and no assembly/run accession
or download URL. It supplies no available ATB genome.

All 15 Nuccore records' reference, comment, and source
metadata were inspected. Fourteen describe this WGS project:
GenBank/RefSeq masters ARFI00000000.1 and
NZ_ARFI00000000.1; scaffolds KB910518.1 and
NZ_KB910518.1; and ten GenBank components
ARFI01000001.1 through ARFI01000010.1.
The scaffold records explicitly join those ten components
with nine 100-base gaps. Their component lengths are
67,850; 154,616; 515,529; 150; 1,057,516; 3,374,676;
185,919; 765,982; 62,484; and 650,597 bases.
The GenBank master length field of 10 is not a ten-base
genome. All WGS source features name HW567 and taxon 1034769;
their missing environmental fields do not negate the
independently documented deposit/paper origin.
[WGS master](https://www.ncbi.nlm.nih.gov/nuccore/ARFI00000000.1);
[GenBank scaffold](https://www.ncbi.nlm.nih.gov/nuccore/KB910518.1).

The remaining record, `PD240497.1`, is a 1,558-base
patent sequence, JP 2022529421-A/6348, with source organism
HW567 and taxon 1034769. It is unassigned DNA, not an
additional genome or direct proof of a plant-growth phenotype.
No patent efficacy claim was adopted.
[Patent sequence metadata](https://www.ncbi.nlm.nih.gov/nuccore/PD240497.1).

Woo et al. (2017), DOI `10.1128/genomeA.00300-17`,
PMID 28473393, explicitly links HW567 to ARFI00000000
in Table 1, with carboxymethyl cellulose as the isolation
carbon source and Puerto Rican forest-soil provenance.
The primary article was read, including its table and
strain-specific discussion. Its approximate 6.9-Mb table
value should be distinguished from the current exact
assembly length; its prose reverses the Gordonia and
Paenibacillus size ordering. Neither discrepancy changes
this YAML, which asserts no genome length or phenotype.
[Primary genome paper](https://journals.asm.org/doi/10.1128/genomea.00300-17).

The earlier Woo et al. study resolves to DOI
`10.1016/j.syapm.2013.10.001`, PMID 24238986.
Its metadata and full abstract were read, but the publisher
full text was unavailable. The abstract's cohort-level
enzyme results were not converted into HW567-specific
measurements or mechanistic claims.
[Earlier study](https://pubmed.ncbi.nlm.nih.gov/24238986/).

## Completeness

The five raw inventories other than GTDB and Madin have
no exact target row. That does not mean no culture or
genome exists: the verified culture/genome chain is
already represented under the taxon where BacDive files
the strain. The seeder gathers strains from a taxon's
own NCBI subtree, not from siblings sharing an alias;
see `docs/HARMONIZATION.md:146` and
`src/taxonmech/seed.py:484`.
58172 and 1034769 are separate records with the same
unclassified parent. A zero strain-entry count on this
target follows that documented rule and is not a missing
strain-genome link in the corpus.

The verified deposit/source connections are useful future
navigation or reconciliation evidence, but not permission
to move the strain or infer a taxonomy merge. Bare HW567
in the GTDB strain-identifier field is not a recognized
culture-deposit join token. GOLD's empty deposit field and
ATB's unprocessed sample do not establish additional
eligible deposit-to-genome links by themselves.

Missing optional literature evidence, definition, phenotype,
nomenclature, and graph slots are not independent defects
in this seeded record. No causal graph should be invented
from annotations, predicted BacDive traits, or the patent
sequence. The current NCBI identity, snapshot-supported GTDB
mapping, count provenance, and source-specific classification
are complete enough for the record's present claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed YAML. The source-classification
differences, incomplete external access, and unperformed
Madin edge reproduction are documented limits, not claims
that all possible enrichment or source reconciliation is
finished.

## Recommended Edits

No required edit to this record.

If later authorized to improve cross-record discoverability,
keep the HW567/cmc22/DSM 25994 bridge explicitly
source-attributed and retain the separate NCBI identities.
Source classification corrections belong upstream in
BacDive/NCBI or the configured kg-microbe input; an approved
new representation belongs in the maintained extractor/seeder
and schema with tests. Do not hand-edit this generated YAML,
move the existing BacDive strain entry, or overwrite a
source-supplied accession version.

## Follow-up Checks

- Restore the manifest-matching upstream Madin input before claiming independent reproduction of its one taxon-subject edge; do not infer the missing predicate or experimental measurement from the count.
- Recheck the exact GTDB species membership and source mapping on a future snapshot. A one-member cluster and its representative status are snapshot facts, not promises about future releases.
- For any future alias-navigation change, test that 1034769, 1192161, and 58172 remain distinguishable, the source-classifying record retains the DSM deposit/genome links, and StrainInfo strain/deposit identifiers remain typed separately.
- Rerun focused schema and strict validation after any authorized regeneration; use full `just verify-corpus`, tests, QC, provenance/history, and generated-product checks before publishing a broader change.
- External-access limits: live GTDB and StrainInfo record bodies, the BioProject browser page, and the earlier enzyme study's full text were not verified. The current verdict uses inspected pinned sources, live NCBI assembly/taxonomy metadata, live culture authorities, and the 2017 primary paper.

## Additional Notes

Initial non-target matches were M. tuberculosis
ERR1034769 in `data/bvbrc/bvbrc-0006.jsonl.gz:6471`
and `data/catalog/allthebacteria.tsv.xz:569239`.
Neither a run suffix nor an available FASTA for that
unrelated sample establishes an HW567 association.

The 26 newly inspected secondary rows include five
deposit/sample rows and three rows for the separate cmc22
taxon. The 18 rejected rows comprise: seven MUMCMC2276
Streptococcus pyogenes rows; one PRJNA404801 groundwater
project; one PNUSAS404801 Salmonella assembly; one
StrainInfo deposit 404801 belonging to a different strain
record and organism; one Vibrio contig-N50 value 404801;
three Acinetobacter taxon-911970 rows; two Weissella
BCMC 22107 assemblies; one merged NCBI ID 404801; and
one ATB SeqKit-sum substring. All were read fully and
rejected by namespace and native context, not by text
similarity alone. Reading an unrelated source row did
not reopen or modify any Eukaryota review.

The cmc22 local rows are
`data/raw/ncbitaxon_taxa.tsv:267793`,
`data/catalog/ncbi_names-0006.jsonl.gz:36010`, and
`curation/seed_scope.tsv:359732`.
They are contextual evidence, not a completed review of
that separate taxon.

The live DSMZ page contains an inconsistent organism name
in a BacDive helper-link caption; following the link
resolves to the correct BacDive 160442 HW567/cmc22 page.
That caption was not used to infer another organism
identity. The deposit record's main content and direct
WGS link were used instead.

Exact PubMed searches for HW567 and cmc22 returned zero
with missing-phrase diagnostics, while DOI searches
resolved the genome and Madin publications. Those bounded
index misses do not mean that HW567 has no literature.

No sequence bases, full gene-function annotation, whole
patent, or exhaustive phenotype literature review was
performed. No YAML, inventory, scope, history, status,
generated page, prior report, or Eukaryota record was
changed.
