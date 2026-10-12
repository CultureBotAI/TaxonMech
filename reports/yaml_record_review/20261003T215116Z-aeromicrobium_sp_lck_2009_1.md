# YAML Record Review: Aeromicrobium sp. LCK-2009.1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aeromicrobium_sp_lck_2009_1.yaml`
- Started UTC: 2026-10-03T21:50:10Z
- Finished UTC: 2026-10-03T21:51:16Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord`, `NCBITaxon:1032300`,
Aeromicrobium sp. LCK-2009.1, rank `SPECIES`, domain `BACTERIA`, grounding
`EXACT`, mapping status `SEEDED`. This is NCBI's provisional isolate
taxon under unclassified Aeromicrobium, not the genus or a formally
described species name.

It has one NCBI name attestation, zero inventoried BacDive strains and one
seed event. No nomenclature, taxonomy mapping, genome relationship,
phenotype, causal graph or general evidence object is carried. The review
is read-only and leaves generated and maintained data unchanged.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/aeromicrobium_sp_lck_2009_1.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/aeromicrobium_sp_lck_2009_1.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Inventory comparisons | Identity, empty synonym set, all ten root-first lineage entries, path, scope and NCBI attestation agree. |
| Embedded history | Strict validation passed; timestamp, one-source seed context and scope reason agree. |
| Standalone history | Not applicable: identifier, label and slug searches under `history/`, including ignored and hidden files, found no target entry. |
| Graph and ontology-product gates | Not applicable: no causal graph or curator-added product grounding occurs in the complete YAML. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports or sequence alignment. Focused
source comparisons do not replace corpus reproduction. No generator,
history writer or lifecycle-status promotion was run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220803` supports the exact identifier, label,
species rank, genetic code 11 and parent `NCBITaxon:2633570`, unclassified
Aeromicrobium. Live NCBI EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032300)
confirm the identity and complete lineage through Propionibacteriales,
Nocardioidaceae and Aeromicrobium. The native scientific name is in
`data/catalog/ncbi_names-0005.jsonl.gz:30085`.

The NCBI browser page was unavailable through the web tool; the structured
authority endpoints succeeded. No alternative source name or synonym is
carried or supplied by those inspected taxonomy records.
`data/taxa/PATHS.tsv:13165` and `curation/seed_scope.tsv:321184` match the
file and seed-event reason. `SPECIES` reflects NCBI's rank and does not
assert valid publication or a type strain. Higher-ranked ancestors remain
lineage context, satisfying the species-or-below scope rule.

Preserve the full isolate suffix and punctuation. A broader isolate-label
search also found Pseudomonas sp. LCK-2009.1a, `NCBITaxon:1032325`, in
`data/raw/ncbitaxon_taxa.tsv:220828`. That is a separate source taxon, not
a spelling variant or valid source of evidence for this record.

## Evidence

- **Carried provenance:** The sole attestation is NCBI Taxonomy, exact
  identifier/name, count one, unit `NAME`, snapshot 2026-09-13. It agrees
  with the backbone row and supports the seeded identity only. The count
  is not a genome, experiment or phenotype count.
- **Independent marker context:** Exact no-descendants Nuccore search
  `txid1032300[Organism:noexp]` returned one sequence. Inspected
  [JF742918.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742918.1) is a
  1,421-base partial 16S rRNA sequence with organism Aeromicrobium sp.
  LCK-2009.1, strain LCK-2009.1 and `taxon:1032300`. Source annotations
  describe an Icelandic rock sample collected in July 2009. This
  corroborates isolate identity, not a whole genome or culture deposit.
- **Citation boundary:** The sequence references an unpublished work by
  Kelly and Cockell on actinobacteria and terrestrial rock weathering,
  plus a direct submission dated March 28, 2011. No DOI or PMID appears
  in those inspected reference objects. The unpublished title does not
  establish this isolate's weathering activity or a causal mechanism.
- **Other inventories:** Complete structured scans of BacDive strains,
  LPSN names, GTDB mappings, GOLD organisms, MediaDive, Madin and
  BactoTraits raw tables found no target row. Complete backbone scanning
  found no children. Thus `strain_count: 0` accurately counts inventoried
  BacDive strains, without denying the existence of the sequenced isolate.
- **Native source catalogs:** Ignored-inclusive searches across all native
  JSONL shards in `data/catalog/`, BacDive, BV-BRC, GOLD, StrainInfo and
  SeqCode found the scientific-name entry but no additional target-associated
  source entry. An unrelated NCBI assembly, GCA_015708035.1, uses the bare
  strain number 1032300 for Listeria monocytogenes, taxon 1639. That numeric
  collision was inspected and excluded, not treated as a genome match.
- **Structured expression evidence:** iModulonDB is not applicable: the
  record contains no gene, regulator, pathway, phenotype or transcriptomics
  assertion. The external 16S identity check does not authorize
  cross-organism expression-module transfer.

## Completeness

No consequential missing representation was established. An exact NCBI
Assembly query returned zero records with `phrasesnotfound` and no-items
warnings. That is an unsuccessful indexed match, not proof that a genome
cannot exist elsewhere. The native source searches independently found
no target genome evidence.

The partial marker is optional context, not a mandatory assembly or
genome-record link. There is no inventoried BacDive strain or matched own
deposit to anchor a StrainInfo sequence overlay. There is no BIOSAMPLE
assertion to support ATB linking. The full ATB sample catalog was not
audited, and no global absence from ATB is claimed.

Full target scans of type-material, culture-collection, merged-ID and
dropped inventories found no row. Ignored-inclusive identifier, label,
slug and isolate-spelling searches through raw inventories and SI/ATB
link/exclusion surfaces found the target backbone identity, plus the
explicitly excluded LCK-2009.1a near-match. No target SI/ATB association
was identified. History searches found no target entry; the corresponding
curation entry is the existing scope row. These findings are bounded to
the inspected files and source identities.

Empty nomenclature, synonyms, taxonomy mappings, definition, general
evidence, discussions and causal graphs are appropriate for this seeded
provisional taxon. Do not invent a formal epithet, type deposit or trait
from the genus assignment, isolation source or marker sequence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. The isolate identity and carried
taxonomy agree with their authority. No maintained-input correction is
currently required.

## Recommended Edits

None required. Keep the record generated and `SEEDED`. Future authoritative
taxonomy updates belong in the pinned NCBI source and its
`src/taxonmech/ncbi_taxdump.py` / `src/taxonmech/extract.py` import path,
then the normal seeder. Optional marker or literature enrichment needs
separately authorized maintained curation with narrow evidence, not a
manual YAML change or a match to a similar isolate label.

## Follow-up Checks

- On a source refresh, recheck this exact taxon and any explicit
  replacement/merge evidence; retain the distinction from LCK-2009.1a.
- Before optional genome or marker enrichment, establish a real strain
  or deposit association, preserve supplied accession versions and
  exclude numeric collisions and partial-name matches.
- For an authorized input change, use the documented extraction and seed
  dry runs, a canary for NCBITaxon:1032300, both focused validators, then
  `just verify-corpus` and `just qc` before publication.

## Additional Notes

Absence searches included ignored and hidden files through explicit
complete structured scans or `rg --no-ignore --hidden -z`. The marker was
independently fetched for this record; evidence was not inherited from
another LCK isolate. No optional source context was added to the YAML.
Public reads incurred no paid-provider use. No outbound message, GitHub
mutation, history event, earlier-report edit or generated-data change was
made. Completed Eukaryota coverage remains untouched.
