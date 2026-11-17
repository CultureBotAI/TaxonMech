# YAML Record Review: Planktothrix suspensa

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/planktothrix_suspensa.yaml`
- Started UTC: 2026-10-06T23:53:39Z
- Finished UTC: 2026-10-06T23:57:50Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read before judgment. It identifies
`NCBITaxon:1035353`, Planktothrix suspensa, at `SPECIES` rank in
`BACTERIA`, with parent `NCBITaxon:54304`, genetic code 11,
`grounding_status: EXACT`, and `mapping_status: SEEDED`. It has three
NCBI-sourced synonyms, zero listed BacDive strains, one NCBITAXON NAME
attestation, and one seed event. It contains no phenotype, mechanism, genome,
publication, LPSN mapping, or human-review assertion.

This review concerns the species, not its SAG 5.81 strain descendant
`NCBITaxon:498567`, the qualified descendant Planktothrix cf. suspensa
FEM_DD592 (`NCBITaxon:1035354`), or a culture-collection deposit. The PATHS
entry is unique, and an ignored-inclusive report filename search found no
prior report for this exact stem.

The YAML is generated from committed inventories and scope. No record,
source, generator, page, history entry, or lifecycle status was changed.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and
the existing offline environment:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/planktothrix_suspensa.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/planktothrix_suspensa.yaml --out /private/tmp/psus-strict.tsv`: exit 0, exactly one file scanned, zero ERROR rows. The emitted TSV was read and contains only its header.
- Read-only structured comparisons checked the complete pinned ancestor chain,
  source synonym categories, exact taxon rows in seven non-NCBI inventories,
  PATHS, scope, source attestation, and seed-event text.
- A complete traversal of the pinned NCBI subtree found 55 taxon IDs,
  including this species and 54 descendants. A full parsed
  `data/raw/bacdive_strains.tsv` scan found zero rows classified anywhere
  in that subtree. This checks the actual descendant-inclusive strain-count
  rule, not only direct species matches.
- Type-material, merged-ID and dropped-ID tables were read for this exact
  taxon: two type-material rows; no merged or dropped row.

Not checked: full-corpus `just verify-corpus`, `just qc`,
`just validate-all`, `just validate-history`, `just validate-products`,
provenance hashes, tests, rendered-site drift, and publication-size gates.
These were not represented as target-only gates or replaced by an invented
focused reproduction check. No causal graph or curator-added ontology node
requires a new grounding check; no history record was created by this
read-only review. Validator success proves shape, not biological correctness.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:222038` agrees with the entire target.
`data/taxa/PATHS.tsv:14529` and `curation/seed_scope.tsv:322310` agree
with its ID, filename and inclusion reason.

The root-first lineage is:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 1783272 Bacillati / KINGDOM; 1798711 Cyanobacteriota/Melainabacteria group / CLADE; 1117 Cyanobacteriota / PHYLUM; 3028117 Cyanophyceae / CLASS; 1301283 Oscillatoriophycideae / SUBCLASS; 1150 Oscillatoriales / ORDER; 1892252 Microcoleaceae / FAMILY; 54304 Planktothrix / GENUS`.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035353&retmode=xml)
and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035353)
were inspected. They agree on species identity, parent, bacterial placement,
genetic code, ancestor IDs and the descendant set. Datasets includes the
root omitted by the XML lineage presentation.

The four complete native rows in
`data/catalog/ncbi_names-0005.jsonl.gz:31513` through physical line 31516
distinguish the scientific name, the synonym Oscillatoria agardhii var.
suspensa, and two authority-bearing strings. The YAML correctly retains the
plain NCBI synonym as exact and both authority strings as related synonyms.
It does not treat an authority string as a culture accession or silently
replace the species by the old variety.

The live [LPSN species page](https://lpsn.dsmz.de/species/planktothrix-suspensa)
identifies this combination as the correct name, published under the
botanical code, and links the [older variety](https://lpsn.dsmz.de/variety/oscillatoria-agardhii-suspensa)
as its homotypic synonym at a different rank. LPSN's displayed class is
Chroococcophyceae, whereas NCBI carries Cyanophyceae. This source difference
is preserved here; it does not authorize altering NCBI lineage. The local
LPSN inventory has no matching taxon or name row from which the seeder could
emit a nomenclature entry.

## Evidence

The NCBITAXON attestation's ID, label, count 1, unit NAME and snapshot
2026-09-13 all match the pinned backbone. Four native name rows are not four
attestations. The seed text matches the scope reason and source list.
The seed timestamp 2026-09-13T17:54:04Z is the newest of the parsed raw,
ATB and StrainInfo manifest timestamps (17:50:44Z, 17:54:04Z and 17:29:00Z,
respectively), as required by `src/taxonmech/seed.py::_seed_timestamp`.
It is not an assertion of a biological review on that date.

The 54 descendants comprise SAG 5.81, FEM_DD592, 27 taxa
`NCBITaxon:1189340` through `NCBITaxon:1189366`, and 25 taxa
`NCBITaxon:1311732` through `NCBITaxon:1311756`. Native names, backbone
and scope rows were inspected without interpreting those taxon concepts as
BacDive records.

SAG 5.81 has additional evidence that is not a strain-listing obligation under
the current BacDive-owned model:

- `data/raw/ncbi_type_material.tsv:1829` and physical line 1830, plus
  live NCBI XML, identify SAG 5.81 and SAG:5.81 as type material of the
  historical variety. These are two source spellings, not two cultures.
- The complete rich StrainInfo row
  `data/straininfo/records.jsonl.gz:276777` identifies SI-ID352825,
  its record-version DOI `10.60712/SI-ID352825.1`, and its own deposit
  SI-DP820989, SAG 5.81, classified under 1035353. The snapshot says
  published offline, deposit available, and `typeStrain: false`; it supplies
  no sequence list. The source DOI is a versioned strain-record identifier,
  not a publication or assembly. This row does not join any inventoried
  BacDive deposit.
- The [SAG public lookup](https://sagdb.uni-goettingen.de/detailedList.php?str_number=5.81)
  was fetched and read directly after the web reader failed. It returned an
  unavailable-strain notice, rather than a detailed strain record. This
  differs from the pinned StrainInfo availability value; it does not prove
  extinction, removal of historical identity, or a reason for unavailability.
  NCBI type material and StrainInfo's false type-strain flag also remain
  distinct source assertions. No source conflict was silently reconciled.

Both exact-taxonomy nucleotide records were read in full metadata form,
including references and feature qualifiers:

| NCBI record | Exact source assertion | Scope |
|---|---|---|
| [NR_125522.1](https://www.ncbi.nlm.nih.gov/nuccore/NR_125522.1) | SAG 5.81; SAG:5.81; taxon 1035353; type material of the old variety | 302-base partial 16S rRNA reference sequence, BioProject PRJNA33175 |
| [LC037449.1](https://www.ncbi.nlm.nih.gov/nuccore/LC037449.1) | NIES-3736; NIES:3736; taxon 1035353 | 1,417-base partial 16S rRNA marker; direct submission 24 March 2015, unpublished study reference |

RefSeq explicitly says NR_125522.1 is identical to EU266131 positions
1-302; that is a source-provided marker relationship, not an inferred genome
equivalence. EU266131 itself was not independently fetched in this review.
The NIES catalogue URL returned general site navigation without the target
strain detail, so current NIES availability was not verified.

NR_125522.1 links Christiansen and colleagues' 2008 paper,
[PMID 18502770](https://pubmed.ncbi.nlm.nih.gov/18502770/),
[DOI 10.1093/molbev/msn120](https://doi.org/10.1093/molbev/msn120).
PubMed bibliographic metadata and abstract were inspected and agree with the
sequence reference. The abstract concerns microcystin-cluster deletion in
studied Planktothrix strains; it is not a universal species phenotype.
PMC returned a browser challenge, so the full article and its supplementary
strain-level results were not inspected. No toxin, gene-deletion or mechanism
claim is added or required by this taxonomy-only record.

An exact non-expanded NCBI Assembly search returned zero and a
phrase-not-found warning; the genome Datasets endpoint for this species
returned an empty object. These bounded results do not prove that no genome
exists under another taxon or source. Neither marker, the BioProject,
StrainInfo IDs nor the native SeqCode name is an assembly.

The local SeqCode name row `data/seqcode/names.jsonl.gz:34921` names record
36808. The [live SeqCode API](https://api.seqco.de/v1/names/36808.json)
was successfully read after the web reader failed: it reports this species
name, status Valid (ICNafp), and unknown nomenclatural type, not a type genome
or an explicit NCBI identity mapping. Catalogue presence alone does not
justify adding an equivalent cross-reference.

The structured iModulonDB dataset inventory was read before web research
using `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
Its 28 rows include no matching Planktothrix dataset. iModulonDB was therefore
not applicable; its absence is not negative evidence.

## Completeness

The initial ignored-inclusive, hidden-inclusive, compressed-file search used
`1035353|Planktothrix[ _]suspensa|Oscillatoria agardhii var\. suspensa`
over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation`, and `history`. All 204 candidate rows were read losslessly:
58 native NCBI names, 11 BV-BRC rows, 10 GenBank summaries, three other native
JSON rows, and 122 TSV/XZ rows. The five SOURCE.json files were separately
parsed in full, and history filenames searched independently of gitignore.

The 204 rows resolve to eight target backbone/name/type/scope rows, 161
descendant backbone/name/scope rows, one StrainInfo deposit group, one
SeqCode name, 31 unrelated E. coli genome/sample rows, and two unrelated
M. tuberculosis rows. The unrelated hits contain the digit string in sample
or run identifiers, not this taxon.

A broad follow-up that included bare short numeric catalogue IDs returned
1,996 discovery lines; it was overbroad, truncated and was not used as
evidence. A completed replacement search restricted to explicit SAG 5.81,
its encoded spelling, SI-ID352825, the two nomenclatural slugs, NIES 3736,
NR_125522, EU266131 and LC037449 found eight rows, all inspected. Seven were
already inspected; the additional native name at
`data/catalog/ncbi_names-0003.jsonl.gz:5316` is the SAG 5.81 strain's
historical name Planktothrix agardhii SAG 5.81. No marker or NIES association
was present in those searched local roots. The same replacement patterns
found no SOURCE.json value or target-named history path.

The empty strain listing is consistent with zero BacDive rows in the whole
subtree. It does not say that no cultures exist. StrainInfo enriches existing
culture-matched BacDive entries and does not create them. Optional
nomenclature, mappings, definition, evidence and causal graphs need not be
populated merely because external research found related material.
Additional culture support and the LPSN mapping are bounded enrichment
opportunities, not evidence of a dropped required field.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the assertions actually emitted by this seeded record.
The availability and type-material differences above are retained as
source-specific follow-up context, not misreported as assertions made by the
YAML. No unsupported strain-to-genome association is present.

## Recommended Edits

None required. Do not hand-edit the generated YAML.

For later authorized enrichment, the LPSN-to-NCBI mapping belongs upstream
in kg-microbe, followed by extraction to `data/raw/lpsn_names.tsv` and
regeneration. Preserve the botanical-code status and rank distinction.
Any new non-BacDive strain-listing behavior would require an explicit model
decision and tested maintained changes in `src/taxonmech/seed.py` and
the appropriate source importer, not a name-only join or a fabricated BacDive
identifier. StrainInfo snapshot refreshes belong to the configured source
capture and overlay workflow; their identifiers must retain deposit-specific
provenance. Marker accessions, if later represented, belong in typed nucleotide
related records rather than genome counts.

## Follow-up Checks

- Resolve SAG's availability notice against a future dated authoritative
  catalogue capture; do not infer a cause or contact the collection from
  this review. Resolve NIES-3736's current catalogue detail before making
  availability or transfer claims.
- Before any LPSN enrichment, inspect and approve the exact upstream mapping
  and verify both nomenclatural records and their source-specific statuses.
- Before importing a sequence, require an eligible exact culture-deposit
  path and keep SAG, NIES and their marker records separate.
- After an authorized maintained-input change, use the documented extraction
  or overlay rebuild, seed dry run and canary, inspect the resulting file,
  rerun schema/strict validation, then run full `just verify-corpus` and
  `just qc`. No such mutation was performed here.

## Additional Notes

The unrelated sample substring hits are retained here to make rejection
auditable. Ten E. coli samples SAMN10353530 through SAMN10353539 belong to
NCBITaxon:562 and BioProject PRJNA218110, not this cyanobacterium.
The matching BV-BRC and current GenBank rows retain the following .1
assemblies; ATB independently supplies the listed ENA analyses.

| BioSample | E. coli strain | NCBI assembly | ATB ENA analysis |
|---|---|---|---|
| SAMN10353530 | PNUSAE018737 | GCA_003768985.1 | ERZ9092923 |
| SAMN10353531 | PNUSAE018736 | GCA_003760145.1 | ERZ9092925 |
| SAMN10353532 | PNUSAE018735 | GCA_003760225.1 | ERZ9092927 |
| SAMN10353533 | PNUSAE018734 | GCA_003782185.1 | ERZ9092929 |
| SAMN10353534 | PNUSAE018733 | GCA_003762585.1 | ERZ9092928 |
| SAMN10353535 | PNUSAE019611 | GCA_003769045.1 | ERZ9092930 |
| SAMN10353536 | PNUSAE018741 | GCA_003759405.1 | ERZ9092938 |
| SAMN10353537 | PNUSAE018740 | GCA_003782245.1 | ERZ9092931 |
| SAMN10353538 | PNUSAE017875 | GCA_003782365.1 | ERZ9092934 |
| SAMN10353539 | PNUSAE017874 | GCA_003770145.1 | ERZ9092933 |

These comprise ten BV-BRC rows, ten current GenBank rows, ten ATB rows, and
GOLD project Gp0386992 / organism Go0502715 for SAMN10353534. All ten ATB
rows say PASS and FASTA available; that does not link them to Planktothrix or
equate assemblies across databases.

The M. tuberculosis run ERR1035353 belongs to taxon 1773, BV-BRC 1773.18360,
and ATB sample SAMEA3558886 / analysis ERZ9334541. Its ATB record retains
SYLPH_RESULTS_FAIL context. A run-number substring is not a taxon match.

No genome FASTA, paid report, private source, external contact, GitHub
mutation, curation-history event or review-status promotion was involved.
Eukaryota records were not reviewed again or modified.
