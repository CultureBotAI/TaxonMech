# YAML Record Review: Coprothermobacter sp. CT-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/coprothermobacter_sp_ct_1.yaml`
- Started UTC: 2026-10-03T23:54:19Z
- Finished UTC: 2026-10-03T23:55:59Z
- Verdict: pass

## Target

Read all 54 lines of generated `TaxonRecord` NCBITaxon:1032348,
Coprothermobacter sp. CT-1. It carries `SPECIES`, `BACTERIA`, `EXACT`,
`SEEDED`, one NCBI name attestation, zero inventoried BacDive strains and
one seed event. No genome, phenotype, nomenclature, taxonomy mapping or
graph assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/coprothermobacter_sp_ct_1.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/coprothermobacter_sp_ct_1.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, full lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. The linked
paper's complete publisher text was unavailable (403); PubMed EFetch
metadata and abstract were inspected. Focused source comparisons do not
prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220851`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032348&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032348)
agree on exact label, species rank, parent NCBITaxon:2640764 and code 11.
All ten root-first lineage entries agree through Pseudomonadati,
Coprothermobacterota, Coprothermobacteria, Coprothermobacterales,
Coprothermobacteraceae, Coprothermobacter and unclassified
Coprothermobacter. Datasets includes root. Preserve this current NCBI
lineage and exact CT-1 identity without inferring equivalence to another
Coprothermobacter strain or species genome.

Native scientific-name row
`data/catalog/ncbi_names-0005.jsonl.gz:30133` supplies no synonym.
`data/taxa/PATHS.tsv:13216` and `curation/seed_scope.tsv:321232` support
the exact slug and seed reason. Species rank satisfies scope, not formal
nomenclatural publication or a type-culture claim. The taxonomy browser
was inaccessible; both structured authority reads succeeded.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid1032348[Organism:noexp]` returned one sequence.
  Inspected [AB630185.1](https://www.ncbi.nlm.nih.gov/nuccore/AB630185.1)
  is a 1,461-base partial 16S sequence with exact organism, strain CT-1
  and taxon1032348. Annotation places the isolate in a thermophilic
  methane fermentor processing artificial garbage slurry in Abiko,
  Chiba, Japan. This is bounded isolate context, not an assembly or a
  culture-collection registration. Preserve the submitted partial status.
- The sequence directly links Sasaki and colleagues' 2011 study,
  [PMID21802987](https://pubmed.ncbi.nlm.nih.gov/21802987/) and
  [DOI10.1016/j.jbiosc.2011.07.003](https://doi.org/10.1016/j.jbiosc.2011.07.003),
  J. Biosci. Bioeng.112(5):469-472. PubMed EFetch independently confirmed
  the authors, title, journal and both identifiers. Its abstract identifies
  CT-1, the reactor source and a close relationship to C. proteolyticus.
  It reports condition-specific protein degradation and co-culture results
  with Methanothermobacter thermautotrophicus. Those results are optional
  strain/condition context, not assertions carried by this YAML.
- Preserve the naming distinction: the paper title uses C. proteolyticus,
  while the abstract describes CT-1 as closely related to that species
  and current NCBI retains Coprothermobacter sp. CT-1. This does not
  authorize a local reclassification, a genome transfer or a taxon merge.
  The other sequence reference is a May 12, 2011 direct submission.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits and no backbone child.
  `strain_count: 0` counts inventoried BacDive records, not all isolates.
- The native search also matched assembly name `concoct_113` in
  GCA/GCF_982385115.1, Coprothermobacter proteolyticus DTU70,
  taxon35786, sample SAMEA122080822. GenBank0066:12729 and
  RefSeq0010:28844 identify a distinct metagenome-derived genome;
  the `ct_1` substring is not the CT-1 strain designation. No link follows.
- The resolved `kg-microbe-sources imodulondb datasets` runner returned
  28 keys, none for Coprothermobacter. iModulonDB was not applicable to
  the optional study context; lack of coverage is not negative biological
  evidence, and no unrelated expression module was transferred.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. The unrelated DTU70 catalog genome does
not establish a missing assembly for CT-1. A related species' comparison
sequence would likewise require explicit own-strain evidence before use.

Ignored-inclusive identifier, exact label, slug and genus-qualified CT-1
spelling searches covered raw inventories, all catalog shards, BacDive,
BV-BRC, GOLD, SeqCode, StrainInfo, ATB strain/genome links and exclusions,
curation and history. After excluding the assembly-name substring match,
no target-associated type-material, culture-collection, merged-ID,
dropped-row or standalone history entry was found within these inspected
surfaces. The raw/maintained target matches were backbone and scope rows.
This is a bounded identity search, not an assertion that every bare CT-1
alias across all organisms has been reconciled.

No inventoried BacDive strain or eligible own deposit starts a SI join;
no carried BIOSAMPLE assertion starts an ATB join. The native ATB catalog
was searched for target strings, but sample/FASTA eligibility and sequence
equivalence were not audited. No global ATB absence follows. The verified
publication is an optional enrichment lead rather than a missing required
citation for the NCBI-only assertions. Empty optional synonyms,
nomenclature, mappings, definitions, general evidence, discussions and
graphs remain appropriate.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. The literature/current-taxonomy
naming distinction is preserved as a bounded follow-up, not silently
resolved. No maintained-input fix is required on the inspected evidence.

## Recommended Edits

None required. Preserve generated YAML, exact isolate, lineage and `SEEDED`
status. Any later taxonomy reconciliation belongs upstream in NCBI and
the pinned input; extraction changes belong in
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and the seeder.
Optional publication or phenotype enrichment needs separately authorized
maintained evidence at exact strain/condition scope, not a manual YAML
edit or inference from a related-species name.

## Follow-up Checks

- At refresh, verify the exact taxon and parent against explicit source
  identity, merge or replacement evidence; retain CT-1 versus DTU70.
- For authorized enrichment, inspect complete primary text to resolve
  strain naming, deposits and the scope of experimental evidence before
  adding citations or graph claims. Do not treat search snippets as
  inspected full-text evidence or transfer the co-culture partner's IDs.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:1032348, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

PubMed's browser page presented a challenge and the publisher text was
inaccessible; the structured PubMed read succeeded. Search-only review
articles and later study leads were not used to assert additional traits,
genomes or a mandatory taxonomy change. No experimental protocol was
added to this identity review.

All absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No optional context was inserted into the YAML, and no
outbound message, GitHub mutation, history event or status promotion
occurred. Older reports and completed Eukaryota coverage were untouched.
