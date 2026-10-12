# YAML Record Review: Vibrio vulnificus JY1701

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_vulnificus_jy1701.yaml`
- Started UTC: 2026-10-06T12:19:08Z
- Finished UTC: 2026-10-06T12:24:55Z
- Verdict: needs curation

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1035117`, Vibrio vulnificus JY1701. It has STRAIN rank, BACTERIA domain, parent Vibrio vulnificus (672), ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one GTDB species mapping/xref, three synonyms, NCBITAXON/GTDB/MADIN attestations and one seed event. It asserts no phenotype, habitat, individual genome link or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/vibrio_vulnificus_jy1701.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/vibrio_vulnificus_jy1701.yaml --out /private/tmp/jy1701-validation.tsv`: passed, one file and zero errors. Read the header-only TSV.
- Structured comparisons inspected the complete backbone row, all ancestors, seven other imported taxon tables, PATHS/scope, synonyms, attestations and seed provenance. Source-row agreement does not prove biological scope.
- Exact-ID checks found no target entry in `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` or `dropped.tsv`.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches, the full Assembly summary and WGS master metadata were read. The Nuccore query returned 337 items, not 337 genomes; individual sequence annotations were not all reviewed.
- The live GTDB genome page could not be read through the browser tool. Checked its pinned native row and imported species/mapping tables instead.
- `just validate-products` is inapplicable because there are no curator-added graph nodes. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history filename and content searches found no separate target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, schema validation, tests, history validation, provenance/site checks and `just qc` were not run. These focused checks do not certify a release.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221894` supports the identifier, label, STRAIN rank, parent, genetic code and both strain-qualified NCBI synonyms. Full native scientific/equivalent-name rows were read at `data/catalog/ncbi_names-0005.jsonl.gz:31331`, line 31332 and line 31333. `data/taxa/PATHS.tsv:14381` and `curation/seed_scope.tsv:36166` agree with the file and its three-source scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035117&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035117) support the strain identity, parent 672 and root-first ancestor IDs 1, 131567, 2, 3379134, 1224, 1236, 135623, 641, 662 and 672. The browser/search display said no rank, whereas both structured authorities and the pinned backbone say STRAIN. Preserve this display discrepancy without changing the supported YAML rank.

NCBI identity and lineage are sound. GTDB species membership is not an exact alternate identity for the strain. GTDB's order-level classification also differs from NCBI's in the native metadata; the repository carries NCBI lineage and does not reconcile the hierarchies.

## Evidence

NCBITAXON counts one NAME from the 2026-09-13 snapshot. MADIN's one TRAIT_ASSERTION matches `data/raw/madin_taxa.tsv:660`; the imported row does not specify a phenotype. No phenotype is asserted in this YAML. The inline 2026-09-13T17:54:04Z seed event matches its provenance and scope.

The entire GTDB species row at `data/raw/gtdb_species.tsv:195992` has 186 genomes. The target mapping at `data/raw/gtdb_mappings.tsv:1412` repeats that number with closeMatch. All eight imported mappings for this species were inspected; their destinations are seven strain concepts and species 672. The extractor counts assembly-to-species edges in `src/taxonmech/extract.py:501` and copies the species total into each mapping. Thus 186 is an imported species-cluster count, not a JY1701-specific assembly census.

The full native row at `data/catalog/gtdb_genomes-0007.jsonl.gz:30081` identifies GB_GCA_000269765.1 as JY1701, with strain taxid 1035117, species taxid 672 and GTDB species classification s__Vibrio vulnificus. Its strain identifier is JY1701, not an eligible culture-deposit accession. This supports classification into the species, not species/strain equivalence.

[NCBI Assembly summary 654438](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&id=654438&retmode=json) identifies GCA_000269765.1 and paired GCF_000269765.1, assembly ASM26976v1, 329 contigs and 4,938,837 bases. NCBI calls the pair identical. The GenBank record remains latest; RefSeq is suppressed, with annotation completeness failure and many frameshifted proteins recorded as exclusions. The native historical RefSeq row dates its non-live status to 2020-07-04; the live summary's 2026-09-10 update date is not the suppression date.

[AFSY00000000.1](https://www.ncbi.nlm.nih.gov/nuccore/AFSY00000000.1) explicitly names JY1701 and taxon 1035117 and links BioProject PRJNA67137 and BioSample SAMN01893931. Its 329-length WGS master describes component contigs AFSY01000001 through AFSY01000329, not a 329-base marker. The full GenBank and historical RefSeq catalog rows were inspected at `data/catalog/ncbi_genbank-0000.jsonl.gz:5850` and `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:1702`.

The WGS master cites Morrison et al. (2012), PMID:22662170, DOI:10.1371/journal.pone.0037553. [The inspected primary article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037553) distinguishes JY1701 from E64MW and JY1305 and attributes project 67137 to JY1701. Its accession paragraph prints ASFY00000000, conflicting with the authoritative AFSY00000000 WGS record and assembly metadata. Preserve that apparent transposition; do not propagate the printed spelling as a verified accession. Comparative gene-content analysis is not direct causal evidence, and no mechanism claim was added.

The full BV-BRC row at `data/bvbrc/bvbrc-0000.jsonl.gz:3303` links genome 1035117.3 to GCA_000269765.1 and the same sample/project. GOLD's organism Go0011875, project Gp0011875 and analysis Ga0020018 connect that assembly to IMG 2548876514. The analysis has no direct organism ID, but its explicit project chain resolves the organism. The organism's culture-collection field is empty. GOLD record IDs, BioSample and BioProject are not genome IDs.

## Completeness

Initial searches used `rg --no-ignore --hidden -n -z` for the taxid, full name, slug and JY1701 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All 113 initial candidate addresses reconcile to the inspected output: eight full TSV rows, fourteen full GOLD rows and 91 other native rows. Native rows directly identifying JY1701 were expanded in full; other rows were inspected through organism/taxon identity, accessions and every matching field, not as full annotation reviews. Common-field factoring was reconstruction-checked.

Expanded searches used the observed assembly, WGS, BioSample, BioProject, GOLD, IMG and publication identifiers. Forty-five addresses comprised seven previously inspected rows and 38 new rows: eight full GOLD rows, one full ATB row and 29 native identity/matching-field projections. This address set also reconciles exactly.

The ATB row at `data/catalog/allthebacteria.tsv.xz:1012927` is SAMN01893931, NOT_PROCESSED, with no assembly accession and no available FASTA. It cannot supply an ATB genome link. No eligible JY1701 culture-deposit join was established in the checked sources. Zero BacDive strains is consistent with the imported inventory; it does not mean no isolate or genome exists.

The backbone has no direct children. Five imported taxon tables other than GTDB and MADIN have no exact target row. The five SOURCE.json metadata files were separately fully traversed for the initial identity pattern, with no match. History content and filename searches found no target artifact. These are bounded local findings, not claims of global absence.

Optional phenotype, habitat and graph slots need not be populated. iModulonDB is inapplicable because this YAML names no functional gene, regulator, pathway or expression-module assertion.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**Major: a species association is promoted to exact strain identity.** YAML line 46 makes Vibrio vulnificus an EXACT_SYNONYM of JY1701, with an identity-oriented GTDB xref at line 57. NCBI and native GTDB metadata distinguish strain 1035117 from species 672. The eight imported mapping destinations also contradict a one-to-one concept interpretation. Retaining an upstream closeMatch assertion does not justify automatically treating it as identity.

The mapping's 186 genomes are correctly traceable to the source species, but that count must remain explicitly species-scoped when repeated in the strain's attestation. It is not a count of JY1701 genomes. These manifestations are one connected scope defect, not separate findings.

Maintained owners: upstream kg-microbe GTDB mapping semantics; `src/taxonmech/extract.py:501` and its mapping-row construction; `src/taxonmech/seed.py:451` for the rank-insensitive identity decision, line 468 for exact-synonym emission and the GTDB attestation construction near line 585. Do not patch the generated record.

## Recommended Edits

1. Add rank/scope-aware mapping handling upstream and in TaxonMech extraction/seeding. Preserve source predicates as source assertions without promoting a species-to-strain association into an exact synonym or identity xref. Retain the supported strain-qualified NCBI synonyms.
2. Explicitly retain the 186 count as source-species evidence wherever it is displayed or attested. Do not relabel it as strain-specific, arbitrarily reverse mapping direction or replace the predicate without checking upstream semantics.
3. Add a focused regression test for this exact strain/species case, then regenerate through the validated writer. Keep NCBI identity and lineage unchanged.

Publishing taxon-level genome associations is a separate possible extension, not permission to fabricate a BacDive or culture-deposit identifier. Preserve native genome evidence and RefSeq suppression status; do not turn the unprocessed ATB sample into an assembly.

## Follow-up Checks

Inspect the regenerated YAML after an accepted generator fix: JY1701 identity, rank, lineage, NCBI aliases and provenance must survive; the broader species must no longer be an exact strain alias. Verify that GTDB evidence remains queryable with its source scope and species count.

Run the focused regression test and both record validators. Before release, run corpus reproduction and full QC, including tests of other strain-rank mappings. A live GTDB UI recheck remains useful, but its current unavailability does not prevent establishing the cross-rank exact-synonym defect.

## Additional Notes

Initial numeric collisions include Staphylococcus haemolyticus 51-22 with SAMEA1035117, Mycobacterium tuberculosis ERR1035117, Bifidobacterium bifidum with SAMN41035117, Streptococcus pneumoniae's matching SeqKit sum, community samples SAMN10351170-79 and MAGs carrying SAMN10351174 in their names. None establishes a JY1701 link.

Expanded collisions include longer WGS prefixes containing AFSY, unrelated accession/strain/GOLD/IMG strings containing 0037553, and comparator genomes linked by the shared PMID. These were disambiguated using their identities and complete matching fields.

An exploratory expanded query accidentally included the short numeric token 1427 and produced excessive unrelated hits. It was superseded by the full DOI pattern before evidence assessment; no absence or coverage claim relies on that exploratory output. A later PMC paper was a search lead, but a browser recheck hit a challenge page; no uninspected result from it supports this verdict.

No sequence-equivalence analysis, review of all 337 nucleotide annotations, complete paper-supplement review or live GTDB census was performed. Only this new review report was written. No taxon, source, code, page, history, status or prior report was changed, and completed eukaryotic reviews were not reopened.
