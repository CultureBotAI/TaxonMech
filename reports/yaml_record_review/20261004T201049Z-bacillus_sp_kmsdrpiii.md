# YAML Record Review: Bacillus sp. KMSDrPIII

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_kmsdrpiii.yaml`
- Started UTC: 2026-10-04T20:09:01Z
- Finished UTC: 2026-10-04T20:10:49Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1033894`,
Bacillus sp. KMSDrPIII: SPECIES, BACTERIA, parent `NCBITaxon:185979`,
`grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11.
It contains ten root-first ancestors, zero inventoried BacDive strains,
one NCBITAXON name attestation and one seed event. It asserts no deposit,
genome, external equivalence or mechanism.

The Roman-numeral KMSDrPIII designation was not equated to KMSDrP3.
The latter was inspected only as a near-match exclusion, not reviewed
as an additional target. No generated record, input, code, lifecycle
status or curation-history entry was changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacillus_sp_kmsdrpiii.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/bacillus_sp_kmsdrpiii.yaml`.
  One file scanned, zero files with errors and zero error rows. This is
  the implementation of `just validate-strict`; it writes the standard
  `reports/instance_validation_failures.tsv` diagnostic.
- Passed bounded source comparisons of identity, every ancestor label
  and rank, directly mapped inventories, scope, filename lock and seed
  wording. A complete backbone scan found no children of this taxon.
- Not run: `just verify-corpus`. Its full-corpus comparison cannot be
  focused through `--max-diffs`, which limits diagnostics only. Bounded
  source comparisons here do not prove byte-level reproduction.
- Not applicable: `just validate-products`, because there are no
  curator-added graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was checked.
  Full-corpus QC, provenance, rendering and test-suite gates were not run.

## Identity and Grounding

The complete backbone row `data/raw/ncbitaxon_taxa.tsv:221328`, native
name object `data/catalog/ncbi_names-0005.jsonl.gz:30668` and inspected
[NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033894&retmode=xml)
agree on identifier, label, species rank, unclassified-Bacillus parent,
bacterial domain and code 11. The
[Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033894)
confirms all ten lineage IDs, including root 1. Live expanded lineage
labels and ranks agree with the pinned backbone where supplied.

The carried genus, family and order are Bacillus, Bacillaceae and
Caryophanales under Bacilli, Bacillota and Bacillati. SPECIES is NCBI's
rank for this placeholder concept, not a formal name-validity claim.
The laboratory designation does not authorize a culture-deposit ID or
a change to STRAIN rank.

The native name object has only the scientific name, and all backbone
synonym fields are empty. Complete exact-ID scans of type-material,
merged-ID and dropped-taxon tables returned no matching rows. No live
replacement or synonym requires a lifecycle change.

## Evidence

The sole attestation reproduces the exact NCBI identifier and label,
one NAME assertion and taxonomy snapshot `2026-09-13`. Complete directly
mapped BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits
inventory scans found no target rows. With no child taxa, there is no
descendant BacDive pool missing from the zero strain count.

The exact-taxonomy nuccore search returned one entry. Its metadata,
references and source qualifiers were inspected in the
[NCBI sequence response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768710.1&rettype=gb&retmode=xml).
`JF768710.1` is a 1,433-base partial 16S rRNA sequence explicitly
assigned to taxon 1033894 and KMSDrPIII. The source records a
uranium-rich site at Domiasiat, India, with no registered deposit or
genome accession.

The entry links [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`. The already-inspected article body and a
fresh [Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
support the KMSDrPIII/JF768710 association. Table headers, footnotes and
row-spanning cells were checked; the closest-match label is Bacillus
thuringiensis, with similarity greater than 99.8%. This is not an NCBI
merge or deposit identity. The supplementary PDF was not inspected.

The near-match KMSDrP3 has another accession, JF768737, in that table.
Independently, the full native name object at
`data/catalog/ncbi_names-0005.jsonl.gz:30693` and backbone row 221353
identify it as Sphingobacterium sp. KMSDrP3, `NCBITaxon:1033919`.
Changing Roman III to digit 3 would therefore transfer evidence across
different taxon concepts. No such transfer occurs in this YAML.

The exact-taxonomy Assembly query returned zero entries with a
`phrasesnotfound` warning for `txid1033894[Organism:noexp]`; it is
not proof of global genome absence. Taxonomy Browser HTML was
inaccessible, but direct NCBI public APIs supplied the primary evidence.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` over
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. Taxon, label, slug and KMSDrPIII
spelling variants produced four matching lines, all inspected.

Three matches were the backbone, scope and native name; the fourth was
unrelated Streptococcus pneumoniae sample `SAMEA1033894` in
AllTheBacteria. This numeric collision is not identity evidence. A
follow-up search for JF768710 and KMSDrP3 produced three matches, all
belonging to the separate Sphingobacterium concept. None matched the
marker. Both relevant native NCBI name objects were read in full.

No eligible deposit or strain-genome assertion for KMSDrPIII was found
within those ignored-inclusive searches. Zero inventoried BacDive
strains is not absence of a biological isolate. A marker sequence and
closest-match literature identification are not missing genome links.
Empty optional nomenclature, mappings, definitions, record-level
evidence and mechanism fields are appropriate for this seeded taxon.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected evidence scope. Identity, lineage,
attestation, strain count, status and inline provenance are supported.
The record correctly keeps the similarly named KMSDrP3 concept separate.

## Recommended Edits

None. Preserve the generated record and exact source spelling. Future
supported source or identity corrections belong in the maintained
inventory pipeline and, as needed, `src/taxonmech/extract.py` or
`src/taxonmech/seed.py`. Scope changes belong in
`curation/seed_scope.tsv`; no such change is justified here.

## Follow-up Checks

On a source refresh, recheck the exact taxon/KMSDrPIII/JF768710 pair
for explicit deposit or genome evidence. Do not normalize Roman III
to digit 3, and preserve nucleotide markers outside genome counts.
Rerun focused validators after an authorized change and the full
`just verify-corpus` gate after regeneration. No unresolved blocker
prevents the present verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13784` locks the slug.
`curation/seed_scope.tsv:321658` records the September 13, 2026 scope
addition and one-source reason. The event at `2026-09-13T17:54:04Z`
exactly reproduces the NCBITAXON source list and scope reason. This
review does not promote SEEDED to REVIEWED or append an event.

Ignored-inclusive report/history/curation filename searches found no
earlier target report or target-specific history artifact before this
report was created. iModulonDB is not applicable to this taxonomic
record; no gene, regulator or expression-module claim was added.
No paid research, outside contact, GitHub mutation or generator run
occurred.
