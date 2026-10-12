# YAML Record Review: Diaphorobacter sp. QH-6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/diaphorobacter_sp_qh_6.yaml`
- Started UTC: 2026-10-04T00:15:37Z
- Finished UTC: 2026-10-04T00:16:40Z
- Verdict: pass

## Target

Read all 54 lines of generated `TaxonRecord` NCBITaxon:1032355,
Diaphorobacter sp. QH-6. It carries `SPECIES`, `BACTERIA`, `EXACT`,
`SEEDED`, one NCBI name attestation, zero inventoried BacDive strains and
one seed event. No genome, phenotype, nomenclature, taxonomy mapping or
graph assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/diaphorobacter_sp_qh_6.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/diaphorobacter_sp_qh_6.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, complete lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports, sequence alignment or unpublished
manuscript text. Focused source checks do not prove corpus reproduction.
No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220858`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032355&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032355)
agree on exact label, species rank, parent NCBITaxon:2649760 and code 11.
All ten root-first lineage entries agree through Pseudomonadati,
Pseudomonadota, Betaproteobacteria, Burkholderiales, Comamonadaceae,
Diaphorobacter and unclassified Diaphorobacter. Datasets includes root.
The taxonomy browser failed, but both structured authority reads worked.

Native name row `data/catalog/ncbi_names-0005.jsonl.gz:30140` supplies
the scientific name. `data/taxa/PATHS.tsv:13224` and
`curation/seed_scope.tsv:321239` support the exact slug and seed reason.
Complete backbone scans found no target synonym or child. Species rank
satisfies scope; it does not assert formal nomenclatural publication,
type-strain status or equivalence to another QH6-labeled isolate.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid1032355[Organism:noexp]` returned two records.
  Both source features and reference lists were inspected.
  [HQ588350.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ588350.1) is a
  1,233-base partial `gyrB` coding sequence; [HQ588349.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ588349.1)
  is a 1,395-base partial 16S sequence. Both explicitly identify QH-6
  and taxon1032355. They are distinct marker records, not two genomes.
- Each sequence cites an unpublished isolation/identification study whose
  title describes dibutyl-phthalate degradation. Reference authors are
  recorded as Decai,J.; Ping,W.; Bai,Z.; Wang,X. Direct submissions
  are dated November 8, 2010 for gyrB and November 5, 2010 for 16S.
  Inspected references supply no DOI or PMID. The title is an optional
  research lead, not inspected experimental proof of a phenotype or pathway.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. `strain_count: 0`
  correctly counts inventoried BacDive records, not all biological isolates.
- GCA_003672715.1 is an unrelated Candidatus Poseidoniales archaeon,
  taxon2163009, isolate77692, sample SAMN09667261. Its ungapped genome
  length is 1032355; that is not its taxon ID. The hit at native
  GenBank0002:45015 supplies no target genome, project or publication.
- GCA/GCF_019373385.1 concern Escherichia coli strain QH6, taxon562,
  sample SAMN17183586, not Diaphorobacter. GenBank0017:39055 and
  historical RefSeq0000:43211 retain that ownership; the RefSeq row is
  suppressed. A bare strain spelling does not authorize transfer.
- GOLD Go0520502 / Gp0444693 / Ga0656133 concern Saccharomyces
  cerevisiae QH6.5, taxon4932, sample SAMN07436989 and assembly
  GCA_003271925.1. GOLD Gp0281372 is a soil-community metatranscriptome
  project labeled QH6, with sample SAMN06349544 and no organism ID in
  the inspected project row. Neither gives an explicit QH-6 organism,
  culture-deposit or genome link. GOLD IDs remain related-record types,
  not genome identifiers; no links were imported from these false matches.
- The resolved `kg-microbe-sources imodulondb datasets` runner returned
  28 keys, none for Diaphorobacter. It was not applicable to the gene
  and optional degradation-study context. Lack of coverage is not negative
  biological evidence, and no unrelated expression module was transferred.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. Neither marker sequence nor the unrelated
catalog genomes establish a missing own-strain assembly.

Ignored-inclusive identifier, exact-label, slug and QH-6 spelling searches
covered raw inventories, all catalog shards, BacDive, BV-BRC, GOLD,
SeqCode, StrainInfo, ATB strain/genome links and exclusions, curation and
history. After identity-scoping the false matches, no own native genome,
type-material, culture-collection, merged-ID, dropped-row or standalone
history entry was found on these surfaces. Own raw and maintained
matches were backbone and scope rows.

No own eligible deposit starts a StrainInfo join, and no carried BIOSAMPLE
assertion starts an ATB join. Sample/FASTA eligibility and sequence
equivalence were not audited; no global ATB absence is claimed. A bounded
publication search did not establish a primary paper's identity; an
unrelated review result was not used to support QH-6 claims. Empty
optional synonyms, nomenclature, mappings, definitions, evidence,
discussion and graphs remain appropriate for the NCBI-only assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input correction is
required by the inspected evidence. The unpublished study remains a
bounded optional follow-up rather than a missing required citation.

## Recommended Edits

None required. Preserve generated YAML, exact isolate, NCBI lineage and
`SEEDED` status. Future taxonomy corrections belong upstream and in the
pinned inventory; extraction/seeding fixes belong in
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
`src/taxonmech/seed.py`, with tests. Optional study or sequence context
requires separately authorized maintained evidence at exact isolate
scope, not a manual generated-YAML edit or an alias/numeric join.

## Follow-up Checks

- At refresh, verify the exact taxon and parent and require explicit
  source identity before any reclassification or genome assignment.
- Before functional enrichment, resolve and inspect the primary QH-6
  study and its condition-specific evidence. Do not infer degradation
  from a sequence-reference title, marker annotation or related strain.
- Preserve gyrB and 16S links as partial nucleotide context outside genome
  counts; verify exact own-deposit evidence before any SI or GOLD join.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:1032355, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

GOLD collision rows were inspected at organisms:366524,
projects:188220/316332 and analyses:439436. The yeast's linked analysis
does not change the organism identity established by its own project and
organism records; the community project's QH6 label is not a strain join.
No geographic claim was inferred from the sequence submitter's address.

All local absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No YAML mutation, outbound message, GitHub mutation,
history event or status promotion occurred. Older reports and completed
Eukaryota coverage were untouched.
