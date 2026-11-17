# YAML Record Review: Leptospira sp. SPO4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/leptospira_sp_spo4.yaml`
- Started UTC: 2026-10-04T00:03:53Z
- Finished UTC: 2026-10-04T00:04:57Z
- Verdict: pass

## Target

Read all 53 lines of generated `TaxonRecord` NCBITaxon:103235,
Leptospira sp. SPO4. It carries `SPECIES`, `BACTERIA`, `EXACT`, `SEEDED`,
one NCBI name attestation, zero inventoried BacDive strains and one seed
event. No genome, phenotype, nomenclature, taxonomy mapping or graph
assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/leptospira_sp_spo4.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/leptospira_sp_spo4.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, complete lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused source
checks do not prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18359`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103235&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103235)
agree on exact label, species rank, parent NCBITaxon:2633828 and code 11.
All ten root-first lineage entries agree through Pseudomonadati,
Spirochaetota, Leptospiria, Leptospirales, Leptospiraceae, Leptospira and
unclassified Leptospira. Datasets includes root. The taxonomy browser
failed, but both structured authority reads succeeded.

Native name row `data/catalog/ncbi_names-0000.jsonl.gz:38377` supplies
the scientific name. `data/taxa/PATHS.tsv:13218` and
`curation/seed_scope.tsv:144019` support the exact slug and seed reason.
Complete backbone scans found no target synonym or child. Species rank
satisfies scope; it does not assert a formal species name, type-culture
designation, serovar or equivalence to another Leptospira isolate.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid103235[Organism:noexp]` returned one record.
  Inspected [AB031510.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031510.1)
  is a 746-base partial `flaB` coding sequence for flagellin. Source
  qualifiers explicitly name SPO4 and taxon103235. This is not a 16S
  record or whole-genome assembly. No clinical, geographic or serovar
  assertion follows from the submitter's institutional address.
- Its references name Kawabata, Dancel, Yanagihara and Watanabe, with
  a database-only publication in 2000 and an August 25, 1999 direct
  submission. The inspected reference metadata provide no DOI or PMID;
  none was invented or borrowed from nearby Leptospira records.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. `strain_count: 0`
  correctly counts inventoried BacDive records, not all biological isolates.
- The search's `CIP 103235` hits belong to Serratia marcescens,
  taxon615, BacDive5165, GOLD Go0228451 and StrainInfo SI-ID4950 /
  SI-DP154947. The native SI record explicitly assigns its sequence
  links to its own deposits. Neither the culture number nor SI grouping
  links that evidence to Leptospira taxon103235. LPSN780876/780877 and
  NCBI type-material entries in these hits likewise concern Serratia.
- Another numeric SI hit is SI-DP103235, ATCC23811, in SI-ID38241 for
  Escherichia coli taxon562. A deposit's numeric ID is not an NCBI taxon
  identifier. Agrococcus sp. SPO4, taxon1712082, is also a distinct
  organism despite the bare strain-name match.
- Other genome hits are GCA_033091495.1, Pseudomonas aeruginosa
  PSA-BAB-IMI-103235, taxon287; GCA_022115575.1, Klebsiella pneumoniae
  strain103235, taxon573; and GCA/GCF_023112095.1, Staphylococcus aureus
  strain103235, taxon1280. The latter RefSeq row is historical/suppressed.
  Their samples, projects, publications and genomes do not belong here.
- The resolved `kg-microbe-sources imodulondb datasets` runner returned
  28 keys, none for Leptospira. It was not applicable to this gene-context
  lead; lack of coverage is not negative biological evidence, and no
  unrelated module was transferred.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. The own-strain partial gene sequence and
unrelated catalog assemblies do not establish a missing whole genome.

Ignored-inclusive identifier, exact-label, slug and SPO4 spelling searches
covered raw inventories, all catalog shards, BacDive, BV-BRC, GOLD,
SeqCode, StrainInfo, ATB strain/genome links and exclusions, curation and
history. After identity-scoping the collisions above, no target-associated
native genome, type-material, culture-collection, merged-ID, dropped-row
or standalone history entry was found on these surfaces. Own raw and
maintained matches were the backbone and scope rows.

No own eligible deposit starts a StrainInfo join, and no carried BIOSAMPLE
assertion starts an ATB join. Sample/FASTA eligibility and sequence
equivalence were not audited; no global ATB absence is claimed. A bounded
primary-database web search provided taxonomy-directory leads, not
additional inspected own-strain genome evidence. Empty optional synonyms,
nomenclature, mappings, definitions, evidence, discussion and graphs are
appropriate for the present NCBI-only assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input correction is
required by the inspected evidence.

## Recommended Edits

None required. Preserve generated YAML, exact isolate, NCBI lineage and
`SEEDED` status. Future taxonomy corrections belong upstream and in the
pinned inventory; extraction/seeding fixes belong in
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
`src/taxonmech/seed.py`, with tests. Optional sequence-context enrichment
requires separately authorized maintained evidence, not a manual YAML
edit or a link inferred from a bare strain name or numeric substring.

## Follow-up Checks

- At refresh, recheck the exact taxon and parent and any explicit merge
  evidence. Preserve Leptospira SPO4 versus Agrococcus SPO4 and the
  unrelated CIP/SI and other-organism strain identifiers.
- If sequence context is later curated, retain the exact accession/version
  and partial `flaB` classification, outside whole-genome counts.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:103235, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

Genome collision rows were inspected at GenBank0030:40697,
GenBank0020:21844, GenBank0021:19141 and historical RefSeq0001:1263.
Native SI collision records are at `data/straininfo/records.jsonl.gz:4950`
and `:26656`; own-versus-other organism identity was retained before
making absence or completeness judgements.

All local absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No YAML mutation, outbound message, GitHub mutation,
history event or status promotion occurred. Older reports and completed
Eukaryota coverage were untouched.
