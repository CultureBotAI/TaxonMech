# YAML Record Review: Pseudoclavibacter sp. LCK-2009.7b

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoclavibacter_sp_lck_2009_7b.yaml`
- Started UTC: 2026-10-03T22:54:36Z
- Finished UTC: 2026-10-03T22:55:07Z
- Verdict: pass

## Target

Read all 54 lines of this generated `TaxonRecord`, `NCBITaxon:1032322`,
Pseudoclavibacter sp. LCK-2009.7b: rank `SPECIES`, domain `BACTERIA`,
grounding `EXACT`, mapping status `SEEDED`. One NCBI name attestation,
zero inventoried BacDive strains and one seed event are carried. There
is no genome, phenotype, nomenclature, mapping or graph assertion.
No generated YAML, maintained input, history or status was changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudoclavibacter_sp_lck_2009_7b.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudoclavibacter_sp_lck_2009_7b.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Inventory comparison | Identifier, label, rank, parent, code, empty synonyms, complete lineage, path, scope and attestation agree. |
| Embedded history | Strict validation and exact seed-event/scope comparison passed. |
| Standalone history | Ignored-inclusive identifier, label and slug searches found no target history entry. |
| Graph/product grounding | Not applicable: no graph or curator-added product assertion is carried. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused source
comparisons do not prove corpus reproduction. No generator or history writer ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220825`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032322&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032322)
agree on the exact name, species rank, parent `NCBITaxon:2615177` and
genetic code 11. All ten root-first lineage entries agree, through
Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Microbacteriaceae,
Pseudoclavibacter and unclassified Pseudoclavibacter. Datasets includes
root. The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:30107`; no synonym is supplied.

`data/taxa/PATHS.tsv:13188` and `curation/seed_scope.tsv:321206` support
the exact path and one-source seed reason. Preserve suffix LCK-2009.7b.
Species rank meets repository scope without establishing a formally
published name or registered type culture. The taxonomy browser failed
through the web reader, but both structured endpoints succeeded.

## Evidence

- The sole NCBI attestation exactly matches the inventory: count one,
  unit `NAME`, snapshot 2026-09-13. It is not a genome or trait count.
- Exact Nuccore query `txid1032322[Organism:noexp]` returned one sequence.
  Inspected [JF742961.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742961.1)
  is an 811-base partial 16S marker with the exact organism, strain
  LCK-2009.7b and taxon1032322. Source annotation records Icelandic rock
  collected in July 2009. This is bounded isolate context, not an assembly
  or collection-deposit assertion.
- The marker references an unpublished Kelly/Cockell study and a March
  28, 2011 direct submission, without DOI or PMID. Its study title mentions
  actinobacteria and rock weathering. Even though the taxon is within
  Actinomycetota, the title alone does not prove a mechanism or phenotype
  for this isolate. None was imported into the YAML.
- Complete structured scans found no target row in BacDive, LPSN, GTDB,
  GOLD, MediaDive, Madin or BactoTraits inventories and no backbone child.
  Zero `strain_count` counts inventoried BacDive records, not biological
  isolates or all external sequence evidence.
- Native searches found the NCBI name plus unrelated numeric collisions.
  GenBank shard0014 row11526 is GCA_015691965.1, Shigella flexneri,
  taxon623, strain=1032322. Shard0009 row5003 is GCA_010323225.1,
  Campylobacter jejuni, taxon197. Neither supplies evidence for this taxon.
- ATB numeric hits are likewise unrelated: SAMEA1032322 and SAMEA2063835
  are Staphylococcus aureus entries, the latter matching only within a
  SeqKit sum; run SRR31032322 belongs to E. coli sample SAMN44336053.
  These occur at native table rows 62596, 466302 and 3092017.
  Taxon digits, sample/run substrings and checksums are not identity joins.
- iModulonDB is not applicable: no gene-function, regulator, pathway,
  trait or transcriptomics assertion is carried. Partial 16S context does
  not justify another organism's expression-module evidence.

## Completeness

No consequential gap was established. Exact Assembly query returned zero
with phrases-not-found and no-items warnings. That is an unsuccessful
indexed match, not global proof of genome absence. Native catalog searches
found no target-associated assembly after excluding the collisions above.

Ignored-inclusive identifier, label, slug and isolate-spelling searches
covered raw inventories, all catalog shards, BacDive, BV-BRC, GOLD,
SeqCode and StrainInfo. They also covered SI strain links, assemblies,
related records and exclusions, ATB strain/genome links and exclusions,
curation and history. The raw/maintained surfaces returned only the
backbone and scope rows. No target type-material, culture-collection,
merged-ID, dropped-row or standalone history entry was found within the
complete inspected surfaces.

There is no inventoried BacDive strain or eligible own deposit to start
a SI join and no carried BIOSAMPLE assertion to start an ATB join.
The native ATB table was searched for target strings, but sample/FASTA
eligibility and sequence equivalence were not audited. No global ATB
absence follows. The optional marker is not a required assembly link.
Empty optional synonyms, nomenclature, mappings, definitions, general
evidence, discussions and graph slots are appropriate.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input fix is required.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future
taxonomy corrections belong in the pinned NCBI input,
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and the seeder.
Optional enrichment requires separately authorized maintained evidence,
not a manual record edit, numeric-string join or inference from a title.

## Follow-up Checks

- At refresh, check the exact identifier and full isolate suffix against
  explicit merge or replacement evidence.
- For enrichment, establish own strain/deposit and assembly provenance;
  keep marker identity and isolate context distinct from phenotype claims.
- After authorized changes, run documented extraction/seed dry runs,
  a canary for NCBITaxon:1032322, both focused validators, then
  `just verify-corpus` and `just qc` before publication.

## Additional Notes

All absence checks included ignored and hidden files through complete
structured scans or `rg --no-ignore --hidden -z`. Only free public sources
were used. No optional context was inserted into the YAML, and no outbound
message, GitHub mutation, history event or status promotion occurred.
Older reports and completed Eukaryota coverage were untouched.
