# YAML Record Review: Actinomycetales bacteriuum LCK-2009.34

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/actinomycetales_bacteriuum_lck_2009_34.yaml`
- Started UTC: 2026-10-03T21:47:23Z
- Finished UTC: 2026-10-03T21:49:03Z
- Verdict: pass

## Target

Read all 48 lines of the generated `TaxonRecord`, `NCBITaxon:1032299`,
Actinomycetales bacteriuum LCK-2009.34, rank `SPECIES`, domain `BACTERIA`,
grounding `EXACT`, mapping status `SEEDED`. It is an NCBI provisional
isolate taxon under unclassified Actinomycetales, not the order itself
and not a formally described species established by this record.

The record carries one NCBI name attestation, zero inventoried BacDive
strains and a seed event. It contains no nomenclature, mappings, genomes,
phenotype assertions, causal graph or general evidence object. This
read-only review changes none of those fields or their maintained sources.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/actinomycetales_bacteriuum_lck_2009_34.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/actinomycetales_bacteriuum_lck_2009_34.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Inventory comparisons | Identifier, label, rank, parent, genetic code, all eight lineage entries, empty synonyms, scope, path and NCBI attestation match the maintained inventories. |
| Embedded history | Strict validation passed; timestamp, one-source seed context and scope reason are consistent. |
| Standalone history | Not applicable: identifier, exact label and slug searches under `history/`, including ignored and hidden files, found no target entry. |
| Graph and ontology-product gates | Not applicable: no graph or curator-added product grounding occurs in the complete YAML. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports or sequence alignment. Focused
comparisons do not prove corpus reproduction. No generator, curation-status
promotion or history writer was run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220802` identifies exactly this taxon with
parent `NCBITaxon:105426`, unclassified Actinomycetales, and genetic code
11. Live NCBI EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032299)
agree on the name, species rank and complete lineage. The native scientific
name is also present in `data/catalog/ncbi_names-0005.jsonl.gz:30084`.
NCBI's browser page was unavailable through the web tool; its structured
authority endpoints succeeded.

Preserve both the unusual source spelling `bacteriuum` and the isolate
punctuation `LCK-2009.34`. They are not local transcription errors.
The filename's underscore normalization is supported by
`data/taxa/PATHS.tsv:13164`; the scope entry is
`curation/seed_scope.tsv:321183`. No source synonym offers a different
name. A spelling correction would belong to NCBI and a later pinned-source
refresh, not a manual YAML rename.

`SPECIES` is NCBI's taxonomic rank for this provisional entry, not an
assertion of valid publication, a type strain or resolved genus placement.
The order and unclassified parent are lineage context. The record meets
the repository's species-or-below scope rule without inferring a genus.

## Evidence

- **Carried attestation:** The sole source is NCBI Taxonomy, with the
  exact identifier/name, count one, unit `NAME` and snapshot 2026-09-13.
  This matches the backbone row and is sufficient provenance for the
  seeded identity record. It does not attest one genome or a phenotype.
- **Independent sequence context:** An exact, no-descendants NCBI Nuccore
  search for `txid1032299[Organism:noexp]` returned one record. Inspected
  [JF742948.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742948.1) is a
  720-base partial 16S rRNA sequence with the same organism name, strain
  LCK-2009.34 and `taxon:1032299`. Its source annotations describe a
  July 2009 Icelandic rock sample. This corroborates isolate identity;
  it is neither a whole genome nor a registered culture deposit.
- **Citation scope:** The sequence includes an unpublished Kelly/Cockell
  reference titled "Actinobacteria - major contributors to terrestrial
  rock weathering processes" and a direct submission dated March 28,
  2011. No DOI or PMID is supplied in those inspected reference objects.
  The title is not experimental proof that this isolate weathers rock,
  and no corresponding trait or causal claim is made in the YAML.
- **Other source inventories:** Complete structured scans of
  `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`,
  `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` and
  `bactotraits_taxa.tsv` found no target row. Complete backbone scanning
  found no children. Thus zero BacDive strains is faithful to the
  inventory, not a claim that an isolate never existed.
- **Native-source checks:** Ignored-inclusive searches of all native
  JSONL shards in `data/catalog/`, BacDive, BV-BRC, GOLD, StrainInfo and
  SeqCode found the NCBI name but no additional target-associated entry.
  Numeric hits were inspected and rejected: one unrelated Shigella
  assembly has strain number 1032299, while another genome has an
  ungapped sequence length of 1032299. Neither is this NCBI taxon.
- **Structured expression sources:** iModulonDB is not applicable to this
  record: no gene, regulator, pathway, phenotype or transcriptomics claim
  is carried. The external partial 16S identity check does not justify
  transferring expression modules from another organism.

## Completeness

No consequential missing representation was established. The exact NCBI
Assembly query returned zero records, with `phrasesnotfound` and a no-items
warning; treat that as an unsuccessful indexed match rather than a
standalone proof that no genome exists anywhere. The native catalog
searches above independently found no target genome evidence.

The marker accession is useful optional source context but does not create
a missing mandatory strain or assembly entry. There is no inventoried
BacDive strain or eligible own deposit to anchor a StrainInfo sequence
overlay. No BIOSAMPLE assertion exists in the record to support an ATB
join; the complete ATB sample catalog was not audited and no global ATB
absence is claimed.

Full target scans of NCBI type-material, culture-collection, merged-ID and
dropped inventories found no row. Ignored-inclusive exact-label, slug and
isolate-spelling searches through `data/raw/` and the SI/ATB link and
exclusion surfaces found only the backbone identity. The corresponding
history search was empty; the curation search found the existing scope
row. These are bounded searches, not evidence against a future source
update or formal description.

Empty nomenclature, synonyms, taxonomy mappings, genome fields, definition,
general evidence, discussions and causal graphs are appropriate. Do not
infer a type culture, valid name, genus, genome, habitat phenotype or
mechanism from the isolate label or 16S source annotation.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. The exact source spelling and
provisional name are intentional source fidelity, not formatting defects.
There is no current incorrect assertion requiring a maintained-input fix.

## Recommended Edits

None required. Preserve the generated record and its `SEEDED` status.
Any future NCBI name/rank update should enter through the pinned taxonomy
source, `src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
the normal seeder. Do not manually modify the YAML or PATHS entry to
regularize the name. Optional literature or marker enrichment would
require separately authorized maintained curation with scoped evidence.

## Follow-up Checks

- Recheck NCBI identity and any replacement/merge evidence if the pinned
  taxonomy is refreshed; retain source spelling until an authoritative
  change exists.
- Before any optional enrichment, distinguish the partial 16S marker
  from assemblies and establish a real strain/deposit identity. An
  unpublished title or shared numeric string is insufficient.
- For an authorized source change, use the documented extraction and
  seed dry runs, a canary for NCBITaxon:1032299, both focused validators,
  then full-corpus `just verify-corpus` and `just qc` before publication.

## Additional Notes

Absence searches included ignored and hidden files, using explicit
complete structured scans or `rg --no-ignore --hidden -z`. The publicly
read sequence adds context only; no source or evidence field was inserted.
No paid research, outbound message, GitHub mutation, curation event or
generated output change occurred. Existing reports and completed Eukaryota
coverage were left unchanged.
