# YAML Record Review: Micromonospora sp. SGA19

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/micromonospora_sp_sga19.yaml`
- Started UTC: 2026-10-04T00:09:23Z
- Finished UTC: 2026-10-04T00:10:15Z
- Verdict: pass

## Target

Read all 54 lines of generated `TaxonRecord` NCBITaxon:1032352,
Micromonospora sp. SGA19. It carries `SPECIES`, `BACTERIA`, `EXACT`,
`SEEDED`, one NCBI name attestation, zero inventoried BacDive strains and
one seed event. No genome, phenotype, nomenclature, taxonomy mapping or
graph assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/micromonospora_sp_sga19.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/micromonospora_sp_sga19.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, complete lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports, sequence alignment or unpublished
manuscript text. Focused source checks do not prove corpus reproduction.
No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220855`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032352&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032352)
agree on exact label, species rank, parent NCBITaxon:2617518 and code 11.
All ten root-first lineage entries agree through Bacillati,
Actinomycetota, Actinomycetes, Micromonosporales, Micromonosporaceae,
Micromonospora and unclassified Micromonospora. Datasets includes root.
The taxonomy browser failed, but both structured authority reads worked.

Native name row `data/catalog/ncbi_names-0005.jsonl.gz:30137` supplies
the scientific name. `data/taxa/PATHS.tsv:13221` and
`curation/seed_scope.tsv:321236` support the exact slug and seed reason.
Complete backbone scans found no target synonym or child. Species rank
satisfies scope; it does not assert formal nomenclatural publication,
type-strain status or equivalence to another Micromonospora isolate.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid1032352[Organism:noexp]` returned one record.
  Inspected [FR856637.1](https://www.ncbi.nlm.nih.gov/nuccore/FR856637.1)
  is a 1,437-base partial 16S sequence explicitly naming strain SGA19
  and taxon1032352. Source qualifiers identify host nodules, Pisum
  sativum and Spain:Salamanca. This is bounded isolate context, not a
  whole genome, culture registration or proof of nitrogen fixation by SGA19.
- The sequence references Carro and Trujillo's unpublished study of
  Micromonospora diversity associated with pea nodules and rhizosphere,
  plus Trujillo's May 4, 2011 INSDC submission. Inspected reference
  metadata provide no DOI or PMID. No later publication identity or
  experimental phenotype was inferred from the reference title.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. `strain_count: 0`
  correctly counts inventoried BacDive records, not all biological isolates.
- The numeric catalog hit at `data/catalog/ncbi_genbank-0063.jsonl.gz:35706`
  is GCA_964612115.1, an uncultured Candidatus Bathyarchaeia archaeon,
  taxon3037984, isolate binchicken_co103_225, sample SAMEA117372998 and
  project PRJEB82487. Its genome length is 1032352; this number is not
  its taxon ID. No genome, sample, project or classification transfers
  from this unrelated metagenome-derived assembly to SGA19.
- The public structured iModulonDB catalog inspected during this review
  turn contains 28 dataset keys, none for Micromonospora. It was not
  applicable to optional expression context. Lack of coverage is not
  negative biological evidence; no unrelated module was transferred.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. The own partial 16S record and unrelated
archaeal genome do not establish a missing own-strain assembly.

Ignored-inclusive identifier, exact-label, slug and SGA19 spelling searches
covered raw inventories, all catalog shards, BacDive, BV-BRC, GOLD,
SeqCode, StrainInfo, ATB strain/genome links and exclusions, curation and
history. After excluding the numeric collision, the completed search
found the own backbone, scope and native name rows; no own native genome,
type-material, culture-collection, merged-ID, dropped-row or standalone
history entry was found on these inspected surfaces.

No own eligible deposit starts a StrainInfo join, and no carried BIOSAMPLE
assertion starts an ATB join. Sample/FASTA eligibility and sequence
equivalence were not audited; no global ATB absence is claimed. Empty
optional synonyms, nomenclature, mappings, definitions, evidence,
discussion and graphs remain appropriate for the NCBI-only assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input correction is
required by the inspected evidence.

## Recommended Edits

None required. Preserve generated YAML, exact isolate, NCBI lineage and
`SEEDED` status. Future taxonomy corrections belong upstream and in the
pinned inventory; extraction/seeding fixes belong in
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
`src/taxonmech/seed.py`, with tests. Optional host, literature or sequence
context requires separately authorized maintained evidence at exact
isolate scope, not a manual generated-YAML edit or a numeric join.

## Follow-up Checks

- At refresh, verify the exact taxon and parent and require explicit
  source identity before any reclassification or genome assignment.
- Before optional functional enrichment, inspect primary evidence for
  SGA19. Host nodules alone do not establish symbiotic function.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:1032352, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

The sequence accession, length and exact SGA19 source were inspected
independently; no evidence was inherited from neighboring Micromonospora
records. The submitted partial-sequence status is preserved.

All local absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No YAML mutation, outbound message, GitHub mutation,
history event or status promotion occurred. Older reports and completed
Eukaryota coverage were untouched.
