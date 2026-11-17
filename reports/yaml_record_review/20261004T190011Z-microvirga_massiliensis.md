# YAML Record Review: Microvirga massiliensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microvirga_massiliensis.yaml`
- Started UTC: 2026-10-04T18:56:50Z
- Finished UTC: 2026-10-04T19:00:11Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033741`, rank
`SPECIES`, domain `BACTERIA`, with `EXACT` grounding and `SEEDED` mapping
status. It has one LPSN name, one GTDB mapping, one BacDive strain, seven
source attestations and one seed event dated 2026-09-13T17:54:04Z.

Maintained owners are the source inventories and extraction, seed scope,
path lock and `src/taxonmech/seed.py`. This review does not edit generated
YAML, curate a phenotype or promote a lifecycle status.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/microvirga_massiliensis.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/microvirga_massiliensis.yaml`: exit 0, one file, zero errors; normal diagnostic TSV written under `reports/`.
- Structured comparisons checked identity, all nine root-first ancestors, code 11, both emitted synonyms, direct source rows, exact strain crosswalks, path lock, scope and seed-event wording. These bounded comparisons are not a replacement corpus reproduction gate.
- `just verify-corpus` was skipped because it rebuilds the full corpus and has no target-record selector. `--max-diffs` only limits diagnostics.
- `just validate-products` was not run: there are no curator-grounded graph nodes, and the configured OAK gate does not check these identity/source fields. NCBI identity was checked directly.
- Ignored-inclusive target searches found no separate target history artifact. Full-history validation, full `just qc`, all-record validation, corpus tests, provenance hashing and rendering checks were skipped for this read-only review. No history entry was added.

## Identity and Grounding

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033741&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033741)
confirm the species label, parent Microvirga (`NCBITaxon:186650`), code 11
and ancestry through Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Hyphomicrobiales and Methylobacteriaceae. Pinned backbone row
`data/raw/ncbitaxon_taxa.tsv:221306` agrees. Complete relevant tables
contain no children, redirects or dropped status for this ID.

The authority name and `Microvirga sp. JC119` are respectively authority
and includes names in native NCBI metadata. Their related-synonym scope
is appropriate. Live NCBI also lists `Microvirga senegalensis` as a
misspelling; it was not treated as a valid alternative species name or
silently added to the pinned synonym inventory.

[LPSN 794280](https://lpsn.dsmz.de/species/microvirga-massiliensis) confirms
the validly published correct name, Caputo et al. 2016, JC119 = DSM 26813
= CSUR P153 as type material, and marker JF824802. All emitted fields
trace to `data/raw/lpsn_names.tsv:30833`. The inventory's nomenclature
type list has DSM 26813; CSUR P153 is also retained in the strain entry.

The complete native GTDB scan covered 901,341 rows and found exactly three
unique cluster members, all assigned NCBI taxon 1033741:

| GTDB accession | Source designation | BioSample |
|---|---|---|
| `RS_GCF_001006805.1` | JC119; representative, assembly from type material | SAMEA3246152 |
| `GB_GCA_001050495.1` | JC119 | SAMEA3146248 |
| `RS_GCF_902385745.1` | MGYG-HGUT-02310 | SAMEA5851814 |

Mapping row 1369 and species row 121782 agree with `skos:closeMatch` and
count three. The GTDB xref and LPSN-link note are supported. GTDB's higher
lineage uses Rhizobiales/Beijerinckiaceae, unlike NCBI's
Hyphomicrobiales/Methylobacteriaceae; the record correctly retains NCBI's
lineage rather than reconciling the hierarchies.

## Evidence

| Assertion | Inspected support |
|---|---|
| JC119 / DSM 26813 is the type strain | LPSN, NCBI type-material rows 1675-1680, [BacDive 132571](https://bacdive.dsmz.de/strain/132571), its full native object at `data/bacdive/records.jsonl.gz:54881`, and [DSMZ DSM 26813](https://www.dsmz.de/collection/catalogue/details/culture/DSM-26813) agree. |
| Two BacDive assembly assertions | Reference 66792 explicitly supplies unversioned GCA_001006805 and GCA_001050495, with scaffold and contig levels respectively. Raw rows 25191-25192 match the record; neither accession is silently versioned or replaced with a RefSeq ID. |
| Other genome identifiers | The same BacDive object supplies IMG 2802429303 and BV-BRC 1033741.6 for the first assertion, and IMG 2634166464 for the second. Raw genome-record rows 20122-20124 preserve separate source assertions. |
| GOLD related-record provenance | Native organism row 446741, Go0616041, has DSM 26813 in both culture-collection and strain fields. Raw related rows 70035-70036 preserve both matching-field provenances. These are two assertions about one GOLD organism, not two genomes. |
| StrainInfo own-deposit match | Native row 300024 links strain 402135 to its own available, type-strain DSM 26813 deposit 909114, BacDive 132571, NCBI 1033741 and record-version DOI `10.60712/SI-ID402135.3`. The strain status is published online. No sequence assertion is present. |

The [primary description](https://europepmc.org/articles/PMC4831475), DOI
`10.1002/mbo3.329`, was read through its complete Europe PMC XML. PubMed
metadata confirms PMID 26749561 denotes that 2016 paper. It describes
JC119 = CSUR P153 = DSM 26813, marker JF824802 and the CDSD genome project.
Its phenotype, genome-size superlative and clinical claims are not emitted
by this TaxonMech record.

**Literature caveat:** the publisher issued an
[expression of concern](https://europepmc.org/articles/PMC12918391),
DOI `10.1002/mbo3.70240`, PMID 41711396, on 2026-02-19. Its full text and
PubMed relationship were inspected. It concerns questions about compliance
with human-subject research requirements and consent involving vulnerable
populations, with investigation ongoing. It is not a retraction or a
taxonomic invalidation. The independently checked NCBI, LPSN and DSMZ
identity assertions remain supported; this review does not endorse the
paper's ethics or treat it as unqualified evidence for new biological claims.

The article XML also links notice `10.1002/mbo3.70251` / PMC12918396.
Inspection showed that notice's title and substantive text concern a
different Raoultibacter paper, despite an additional metadata link to
Microvirga. Its duplicate-strain concern was therefore not attributed to
this record. The directly matching notice above is the relevant one.

The [Microbiology Society validation-list page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.001149)
confirms the other DOI, publication on 2016-07-01 and reference 6 to Caputo
et al. LPSN explicitly associates the name with Validation List 170. The
publisher's embedded full-text endpoint was inaccessible, so the individual
validation-table row was not independently inspected.

[NCBI marker EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF824802&rettype=gb&retmode=xml)
resolves JF824802 to version `.2`, a 1,475-base partial 16S rRNA sequence
from JC119 with type-material and taxon qualifiers. Preserving the
unversioned source accession is correct; inventing `.1` would not be.

All seven attestations match the inventories: NCBI one name, LPSN one name,
GTDB three genomes, BacDive one strain, MediaDive two media (830 and 840),
GOLD four organisms and BactoTraits one trait assertion. The complete
Madin table has no target row, consistent with its absence here. The
strain's source medium count is zero in the crosswalk; taxon-level medium
counts and DSMZ cultivation information do not justify inventing a
MediaDive strain-level join. Counts with different units are not additive.

## Completeness

The sole classified BacDive strain is retained without truncation. Complete
exact-strain crosswalk scans recover precisely two assembly assertions,
three other genome assertions, two GOLD related assertions and two
StrainInfo related assertions. No StrainInfo assembly or ATB strain/genome
link exists for this strain in those full crosswalks.

Ignored-inclusive searches also read compressed native content in
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
Search keys included the taxon ID/name, DSM 26813, CSUR P153, both matched
GOLD organism IDs, marker, primary-paper DOI and all three BioSamples.
Numeric substring collisions in unrelated samples/runs were excluded.
No ATB sample row was found for those three BioSamples. Absence findings
are limited to these inspected artifacts, not every remote source.

GOLD also contains Go0068447 (bare JC119), Go0616042 (CSUR P153) and
Go0637030 (MGYG-HGUT-02310). The JC119 projects Gp0068447 and Gp0143866,
and analyses Ga0078563 and Ga0124009, explicitly connect to Go0068447,
not the deposit-matched Go0616041. Their native rows corroborate the two
assembly/IMG pairs, but do not supply a new eligible DSM-deposit join.
Complete ID searches found no project/analysis chain referencing
Go0616041 or Go0616042.

An ignored-inclusive pinned CAFI registry search found no CSUR entry.
The actual matcher accepts DSM 26813 but rejects CSUR P153, its encoded
CURIE and bare JC119 as join keys. This does not remove the CSUR alias or
BacDive's direct genome assertions. Native GTDB, NCBI and BV-BRC rows use
bare JC119 or MGYG rather than a registered deposit token. Thus BV-BRC
1033741.4, although retained in its native catalog, is not automatically
a missing culture-matched link. Shared species, assembly statistics or
names cannot transfer MGYG's genome to the type culture.

Optional record-level evidence, definitions, discussions and causal graphs
need not be populated for this seeded identity record. Path-lock row 13759,
scope row 7209 and the seed-event reason agree.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the emitted record's identity and source-assertion contract.
The expression of concern and assembly-quality warnings are material
limitations documented here, not evidence that the cited name, accession
or BacDive association is false. A passing record review does not certify
source-study ethics, genome purity or fitness for downstream analyses.

## Recommended Edits

None required to the generated record on the evidence inspected. Preserve
both source-supplied assembly identifiers, the type-strain distinction,
typed related records and the three-member GTDB source count. Do not
replace the GenBank link with a suppressed RefSeq accession or drop a
source assertion solely because the associated sequence has a warning.

Before any future biological curation based on the paper or assemblies,
carry forward the literature and quality caveats. Source corrections
belong at the relevant upstream authority and in maintained extraction
(`scripts/extract_source_inventory.py`, `src/taxonmech/extract.py`);
projection-rule changes belong in `src/taxonmech/seed.py` or the relevant
source-link module with regression coverage. No direct YAML edit is proposed.

## Follow-up Checks

- Recheck the directly matching expression-of-concern notice before reusing the paper for new claims; do not conflate the unrelated notice's metadata linkage with its substantive scope.
- Before sequence analysis, check current accession versions, quality and suppression independently. The record retains source links, not a guarantee of analysis-ready genomes.
- Recheck the validation-list table when accessible. If a future source or projection correction is implemented, rerun both target validators, then full `just verify-corpus` and applicable `just qc` gates.

## Additional Notes

[NCBI's current first-assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_001006805.1/dataset_report)
confirms a current scaffold assembly, current paired RefSeq accession,
JC119/type material, SAMEA3246152 and PRJEB8433. Its CheckM estimates are
77.44% completeness and 17.03% contamination; those estimates warrant
caution, but the record makes no quality claim. Its low-coverage ANI
diagnostic explicitly explains that it is the type strain, for which no
match is expected.

[The second assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_001050495.1/dataset_report)
confirms current GenBank GCA_001050495.1, isolate JC119, SAMEA3146248 and
PRJEA82707, with contamination and not-used-as-type warnings. Its paired
GCF_001050495.1 is suppressed; native historical RefSeq row 8630 dates
that suppression to 2023-05-15. This does not change the type status of
the culture or make the explicitly retained GenBank accession nonexistent.
The native current and historical NCBI objects and all three BV-BRC
objects were read in full.

The GTDB browser page could not be fetched; complete pinned native cluster
objects supplied the check. PubMed browser and DOI landing pages for the
concern notice were inaccessible, but PubMed XML and Europe PMC full text
were retrieved successfully. SeqCode native name 12937 corroborates the
spelling without establishing a claimed SeqCode validation.

iModulonDB was not applicable: there is no gene, regulator, pathway or
transcriptomic claim. Only this report was added; no record, inventory,
history, status, source code or previous report was edited. No paid
research, external contact or GitHub mutation was performed.
