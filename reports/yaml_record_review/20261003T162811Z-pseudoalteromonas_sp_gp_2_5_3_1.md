# YAML Record Review: Pseudoalteromonas sp. Gp-2-5.3.1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_gp_2_5_3_1.yaml`
- Started UTC: 2026-10-03T16:27:11Z
- Finished UTC: 2026-10-03T16:28:11Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read before judgement. It denotes
`NCBITaxon:1303819`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:194690`, genetic code 11, grounding `EXACT`, status `SEEDED`.
It has ten lineage entries, one NCBI NAME attestation, zero strains and
one embedded seed event. Synonyms, nomenclature, mappings, equivalence
xrefs, strain/genome links, experimental claims and causal graphs are
not asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudoalteromonas_sp_gp_2_5_3_1.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_gp_2_5_3_1.yaml`:
  PASS; one file, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison supports identity, parent, rank,
  code and every lineage entry. No target children occur. Complete
  exact-field scans found no direct membership in the seven other source
  inventories. PATHS and scope each contain exactly one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated pages,
  exports and sequence content were not audited.
- No target standalone history entry was found by ignored-inclusive
  searches, so standalone history validation had no target. The strict
  validator checked the embedded event. Graph/product gates do not apply.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308152` agrees with the label, rank,
parent, genetic code and empty synonym fields. The full native name
object at `data/catalog/ncbi_names-0007.jsonl.gz:30703` independently
supports the exact spelling and taxon ID. The ten-entry lineage is
the root-first NCBI parent chain, including unclassified Pseudoalteromonas
at `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303819&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 194690,
code 11 and all non-root lineage labels/ranks, with no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303819)
confirms rank and all ten ancestor IDs including root. The grounding
matches this exact source entity.

Preserve the source's species rank despite the isolate-like designation.
Neither genus membership nor proximity to another Gp label establishes
equivalence to a named species, a culture deposit or a type strain.
`EXACT` does not assert valid publication of a binomial.

## Evidence

The NCBITAXON / NCBITaxon:1303819 / 1 NAME attestation is reproduced
by the backbone row and its 2026-09-13 snapshot. Its unit describes
source-name coverage, not a strain, genome or biological phenotype.
No DOI, PMID, assembly accession or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106257` pins the slug.
`curation/seed_scope.tsv:393099` admits the taxon on 2026-09-13 with
the exact one-source reason reproduced by the embedded seed event.
The event timestamp 2026-09-13T17:54:04Z, seed_from_sources curator,
SEEDED_FROM_SOURCES action and source list agree with the record.
`SEEDED` remains appropriate; this review is not human sign-off.

## Completeness

Ignored-inclusive searches by ID, label, slug and Gp-2-5.3.1 covered
raw inventories, curation, history and all compressed JSONL catalogs
under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. Only the NCBI scientific-name
object was a target native match. Complete exact-field BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin and BactoTraits membership scans returned
no target row. Zero descendants and zero BacDive membership support
the uncapped strain count of zero.

Numeric catalog hits were inspected as full objects and excluded:
`GCA_023321745.1` at `data/catalog/ncbi_genbank-0021.jsonl.gz:29129`
is Salmonella enterica, taxon 28901, with assembly name PDT001303819.1;
`GCA_013038195.1` at `ncbi_genbank-0011.jsonl.gz:36308` is E. coli,
taxon 562, isolate A405. Neither is the Pseudoalteromonas target.

Further ignored-inclusive searches covered `data/atb/`, the complete
ATB catalog and StrainInfo link, assembly, exclusion and compressed
related-record tables. Two full ATB rows were unrelated Salmonella
enterica entries: SAMN30567378 matched run SRR21303819, while
SAMN36347470 matched digits inside its SeqKit sum. No target association
or eligible culture-deposit/BioSample source chain was found. The raw
directory search included all assembly/genome/related inventories.

These are bounded source-coverage results, not claims that the organism
lacks sequences or isolates elsewhere. Optional names, mappings and
links are correctly empty at the checked boundary. No functional gene,
regulator, pathway, trait or transcriptomics dataset is asserted;
iModulonDB is not applicable. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Keep the supported identity, lineage and `SEEDED` status.
Any future enrichment belongs in maintained source inputs or
`src/taxonmech/extract.py`; changed harmonization belongs in
`src/taxonmech/seed.py` with regression tests. Do not hand-edit generated
YAML or inherit a similar designation's evidence.

## Follow-up Checks

No finding-specific check remains. Future evidence requires exact
taxon/deposit verification, authorized extraction/canary steps and both
focused validators after regeneration. A corpus change also requires
`just verify-corpus` and full QC, neither claimed by this focused pass.

## Additional Notes

Absence checks included ignored files using full structured reads,
`find`, and `rg --no-ignore --hidden`, with `-z` for compressed sources.
Public NCBI API reads used network escalation after established sandbox
DNS failures. The only manual write is this new report; strict validation
wrote its standard diagnostic. No YAML, source, earlier report, history
or status was edited. No generator, source refresh, paid research,
GitHub action or cross-repository write occurred. Eukaryota was not
re-reviewed.
