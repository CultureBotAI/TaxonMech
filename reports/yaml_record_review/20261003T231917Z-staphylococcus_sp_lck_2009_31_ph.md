# YAML Record Review: Staphylococcus sp. LCK-2009.31(pH)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_lck_2009_31_ph.yaml`
- Started UTC: 2026-10-03T23:18:06Z
- Finished UTC: 2026-10-03T23:19:17Z
- Verdict: pass

## Target

Read all 54 lines of generated `TaxonRecord` NCBITaxon:1032331,
Staphylococcus sp. LCK-2009.31(pH). It carries `SPECIES`, `BACTERIA`,
`EXACT`, `SEEDED`, one NCBI name attestation, zero inventoried BacDive
strains and one seed event. No genome, phenotype, nomenclature, mapping
or graph assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_sp_lck_2009_31_ph.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_sp_lck_2009_31_ph.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, full lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused source
comparisons do not prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220834`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032331&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032331)
agree on the exact label, species rank, parent NCBITaxon:91994 and code 11.
All ten root-first lineage entries agree through Bacillati, Bacillota,
Bacilli, Caryophanales, Staphylococcaceae, Staphylococcus and unclassified
Staphylococcus. Datasets includes root. Preserve the literal `(pH)` suffix;
the name alone is not evidence of a pH phenotype or culture condition.

Native scientific-name row
`data/catalog/ncbi_names-0005.jsonl.gz:30116` supplies no synonym.
`data/taxa/PATHS.tsv:13198` and `curation/seed_scope.tsv:321215` support
the exact slug and seed reason. Species rank satisfies scope, not formal
nomenclatural publication or a type-culture claim. The taxonomy browser
was inaccessible; both structured authority reads succeeded.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid1032331[Organism:noexp]` returned one sequence.
  Inspected [JF742942.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742942.1)
  is an 823-base partial 16S sequence with exact organism, strain
  LCK-2009.31(pH) and taxon1032331. Annotation records Icelandic rock
  collected in July 2009. This is bounded isolate context, not an assembly
  or culture-collection registration.
- The marker references an unpublished Kelly/Cockell study and a March
  28, 2011 direct submission, without DOI or PMID. Its study title about
  actinobacteria and weathering does not reclassify this Staphylococcus or
  demonstrate a weathering phenotype. No such inference is in the YAML.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits and no backbone child.
  `strain_count: 0` counts inventoried BacDive records, not all isolates.
- Native GenBank shard0014:11560 is GCA_015692645.1, Salmonella
  Typhimurium taxon90371, sample SAMN16930339, with bare strain1032331.
  This is an unrelated numeric match, not a Staphylococcus genome or
  target source attestation.
- iModulonDB was not applicable: no gene-function, regulator, pathway,
  trait or transcriptomics claim is present. Partial 16S context does not
  warrant another organism's expression-module evidence.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. The unrelated Salmonella assembly does
not establish a missing genome for this record.

Ignored-inclusive identifier, exact label including parentheses, slug and
isolate-spelling searches covered raw inventories, all catalog shards,
BacDive, BV-BRC, GOLD, SeqCode, StrainInfo, ATB strain/genome links and
exclusions, curation and history. After identity-scoping numeric matches,
no target-associated type-material, culture-collection, merged-ID,
dropped-row or standalone history entry was found on these surfaces.
The raw/maintained target matches were the backbone and scope rows.

No inventoried BacDive strain or eligible own deposit starts a SI join;
no carried BIOSAMPLE assertion starts an ATB join. The native ATB catalog
was searched for target strings, but sample/FASTA eligibility and sequence
equivalence were not audited. No global ATB absence follows. Empty optional
synonyms, nomenclature, mappings, definitions, general evidence,
discussions and graphs are appropriate to the supported assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input fix is required.

## Recommended Edits

None required. Preserve generated YAML, exact suffix, lineage and `SEEDED`
status. Future taxonomy fixes belong in the pinned NCBI input,
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and the seeder.
Optional enrichment needs separately authorized maintained evidence,
not a manual YAML edit, bare-number join or inference from a study title.

## Follow-up Checks

- At refresh, verify the exact taxon and parent against explicit source
  identity or replacement evidence, retaining the literal `(pH)` suffix.
- For enrichment, establish own strain/deposit and assembly provenance;
  keep partial-marker annotations distinct from demonstrated phenotypes.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:1032331, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

All absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No optional context was inserted into the YAML, and no
outbound message, GitHub mutation, history event or status promotion
occurred. Older reports and completed Eukaryota coverage were untouched.
