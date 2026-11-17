# YAML Record Review: Kurthia massiliensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/kurthia_massiliensis.yaml`
- Started UTC: 2026-10-04T18:45:37Z
- Finished UTC: 2026-10-04T18:48:40Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033739`, rank
`SPECIES`, domain `BACTERIA`. It has `EXACT` grounding, `SEEDED` mapping
status, one LPSN name, one GTDB mapping, two BacDive strains, eight source
attestations and one seed event dated 2026-09-13T17:54:04Z.

The maintained owners are the source inventories, `curation/seed_scope.tsv`,
`data/taxa/PATHS.tsv`, the extractor and `src/taxonmech/seed.py`. This review
does not authorize editing generated YAML or promoting its status.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/kurthia_massiliensis.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/kurthia_massiliensis.yaml`: exit 0, one file, zero errors; normal diagnostic TSV written under `reports/`.
- Structured source comparisons checked identity, all nine root-first ancestors, genetic code, both NCBI synonyms, direct source rows, path lock, scope and seed-event wording. Complete crosswalk scans recovered exactly the two assembly assertions, three other genome assertions, five GOLD related records and four StrainInfo related records represented in the YAML.
- `just verify-corpus` was skipped because the documented implementation rebuilds the full corpus and offers no target-record selector. These bounded source comparisons are not a replacement reproduction validator.
- `just validate-products` was not run: there are no curator-grounded graph nodes, and its configuration excludes these identity/source fields from OAK lookup. NCBI was checked directly.
- Ignored-inclusive target searches found no separate target history artifact. No history was added; full-history validation was skipped. Full `just qc`, corpus tests, all-record validation, provenance hashing and render checks were not run for this read-only review.

## Identity and Grounding

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033739&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033739)
confirm the species label, parent Kurthia (`NCBITaxon:1649`), lineage and
code 11. The authority name and `Kurthia sp. JC30` are respectively
authority and includes names in the native name catalog, consistent with
their conservative `RELATED_SYNONYM` representation. The pinned backbone
row is `data/raw/ncbitaxon_taxa.tsv:221304`; no children or merged/dropped
status rows were found in the complete relevant tables.

[LPSN record 790602](https://lpsn.dsmz.de/species/kurthia-massiliensis)
confirms the validly published correct name and authority Roux et al. 2013.
It identifies JC30 = DSM 24639 = CSUR P141 as the type strain and JF824795
as the marker accession. `data/raw/lpsn_names.tsv:27543` supports every
emitted nomenclature field and its GTDB link. The inventory's type-designation
list contains DSM 24639; CSUR P141 is also preserved in the actual JC30
strain entry, so the type culture's identity is not lost.

The full GTDB native catalog scan found exactly two unique genomes in
`s__Kurthia massiliensis`, both assigned NCBI taxon 1033739. The representative
is `RS_GCF_000285555.1`, JC30, marked as assembly from type material.
`skos:closeMatch`, the count of two, the GTDB xref and the LPSN-link note
are supported. There is no broader pooled mapping or strain-to-species
scope inflation here.

## Evidence

| Assertion | Inspected support |
|---|---|
| JC30 is the type strain | LPSN, native NCBI type-material rows 1663-1668, [BacDive 23194](https://bacdive.dsmz.de/strain/23194), [DSMZ DSM 24639](https://www.dsmz.de/collection/catalogue/details/culture/DSM-24639) and the primary description agree. DSMZ also confirms CSUR P141. |
| JC31 / DSM 24640 is a separate non-type strain | [BacDive 23195](https://bacdive.dsmz.de/strain/23195), its complete native object and StrainInfo's own deposit object agree. Its native sequence section is empty. No JC30 genome was transferred to it. |
| BacDive genome assertions | `data/bacdive/records.jsonl.gz:22997` explicitly supplies reference 66792, unversioned `GCA_000285555`, IMG 2547132137 and BV-BRC 1033739.3 for JC30. The record preserves those identifiers, versions and provenance. |
| GOLD genome and related-record chain | `data/gold/organisms.jsonl.gz:14776` explicitly names DSM 24639 and Go0017285; project row 14307 links Gp0017285 to that organism, SAMEA2272071 and PRJEA70831; analysis row 11784 links Ga0019635 to that project, `GCA_000285555.1` and IMG 2547132137. The five typed related records are not genome identifiers. |
| StrainInfo JC30 association | Native record row 296229 links SI-ID 398340 to its own available DSM 24639 deposit SI-DP 905044, BacDive 23194 and record-version DOI `10.60712/SI-ID398340.3`; the deposit is type material. |
| StrainInfo JC31 association | Native row 303825 independently links SI-ID 405936, own DSM 24640 deposit SI-DP 913196, BacDive 23195 and DOI `10.60712/SI-ID405936.2`; the deposit is non-type. Neither StrainInfo object supplies a sequence assertion. |

The [primary description](https://europepmc.org/articles/PMC3569394), DOI
`10.4056/sigs.3206554`, was read through Europe PMC's full-text XML after
the PMC browser page failed. NCBI PubMed XML confirms PMID 23407462 denotes
that same 2012 article. Its description and genome section support
JC30 = CSUR P141 = DSM 24639 and the CAEU genome project.

The [Microbiology Society validation-list page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.058222-0)
confirms DOI `10.1099/ijs.0.058222-0`, publication on 2013-11-01, and the
Roux paper reference. LPSN explicitly identifies this as Validation List
154 for the species. The publisher's embedded full-text table could not be
retrieved, so its individual table row was not independently inspected.
The difference between the 2012 effective publication and 2013 authority
is supported, not a date error.

[NCBI marker EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF824795&rettype=gb&retmode=xml)
resolves JF824795 to version `.1`, a 1,471-base partial 16S rRNA sequence
from JC30, with target taxonomy and type-material qualifiers. It belongs
in nomenclature sequence accessions, not among genome assemblies.

All eight attestations match their direct inventories: NCBI one name,
LPSN one name, GTDB two genomes, BacDive two strains, MediaDive one medium
(92), GOLD three organisms, Madin four trait assertions and BactoTraits
one trait assertion. Counts have different units and must not be summed.
Neither the trait counts nor BacDive predictions assert a phenotype here.

## Completeness

Both classified BacDive strains are retained without a cap. Exact strain-ID
crosswalk scans found no omitted eligible assertion: StrainInfo assembly
rows and committed ATB strain/genome links were empty for these two strains.
Searches included ignored and compressed content in `data/raw`,
`data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`, using the target
identifier/name, both DSM deposits, CSUR P141, the marker accession,
both genome BioSamples and the additional GOLD organism ID. Numeric
collisions were excluded. Absence findings are bounded to these artifacts,
not every possible remote genome or external cache.

GOLD also retains Go0613848 with culture field CSUR P141, and Go0636848 for
MGYG-HGUT-01406. The current pinned CAFI registry has no CSUR entry
(ignored-inclusive registry search); the existing matcher returns no join
key for CSUR P141 or its encoded CURIE. It accepts both DSM deposits.
Consequently retaining the CSUR alias in BacDive while excluding a
CSUR-only GOLD join follows the documented authority boundary, not a
missing proven assembly. The MGYG organism lacks a culture identifier and
cannot be assigned to JC30 or JC31 by shared species membership.

GTDB and native NCBI/BV-BRC metadata name bare JC30, rather than an eligible
culture-deposit token. They corroborate the known genome but do not supply
new deposit-matched links under the current rules. The native GOLD chain
already provides the versioned NCBI accession and sample/project evidence.
Two IMG assertions with distinct sources are useful provenance, not two
different genomes to deduplicate. No sequence is inferred from a StrainInfo
group or DOI alone.

Optional graph, discussion and record-level evidence slots need not be
populated; source attestations provide the seeded provenance. The path-lock
row 13757 and scope row 1528 match the target and its unchanged seed event.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. The verdict is bounded by the unavailable
pages and skipped full-corpus gates described above. It does not certify
corpus-wide reproduction or imply that every source count is a census of
currently live assemblies.

## Recommended Edits

None required. Preserve the two source-specific NCBI accession forms,
both IMG provenance assertions, JC30/JC31 separation, and SI-ID/SI-DP/DOI
distinctions. Do not hand-edit generated YAML, infer new links from species
membership or relax the culture-collection matcher for this record.

Any future source correction belongs in its upstream authority and
`scripts/extract_source_inventory.py` / `src/taxonmech/extract.py`; any
projection-rule change belongs in the relevant maintained module, including
`src/taxonmech/genome_sources.py` or `src/taxonmech/seed.py`, with regression
coverage before regeneration.

## Follow-up Checks

- Recheck the validation-list table when its full text is available; its DOI, publisher metadata and LPSN association have already been verified.
- On a source refresh, verify each culture's own deposits and sequence assertions independently. Only consider a new CSUR join after an explicit maintained authority-registry update and accession-template tests.
- Rerun both target validators after any future change, then documented full `just verify-corpus` and applicable `just qc` gates. Do not report skipped corpus gates as passed.

## Additional Notes

[Current NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000285555.1/dataset_report)
confirms JC30's current scaffold assembly and paired RefSeq accession,
SAMEA2272071 and PRJEA70831. Exact-taxonomy assembly search returns one
current assembly pair. The second member of the pinned GTDB cluster,
MGYG-HGUT-01406 (`GCA/GCF_902374725.1`), is in both historical NCBI catalogs
with suppression dated 2026-04-04. The GTDB count remains two source-cluster
members, not a claim of two currently live NCBI assemblies. No equality of
their biological isolates is inferred from matching assembly statistics.

The GTDB browser page and DSMZ's DSM 24640 page were inaccessible through
the web reader. Complete pinned GTDB objects, both BacDive objects and both
StrainInfo objects were inspected. The GTDB scan covered 901,341 native rows;
the manifest identifies release RS232. Native GOLD, BV-BRC, NCBI current and
historical assembly objects were also read in full.

iModulonDB was not applicable: the record contains no gene, regulator,
pathway or transcriptomics claim. No record, inventory, history or mapping
status was changed; no paid research, external contact or GitHub mutation
was performed.
