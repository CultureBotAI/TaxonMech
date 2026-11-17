# YAML Record Review: Phyllobacterium sp. LCK-2009.5a

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/phyllobacterium_sp_lck_2009_5a.yaml`
- Started UTC: 2026-10-03T22:50:48Z
- Finished UTC: 2026-10-03T22:52:04Z
- Verdict: pass

## Target

Read all 54 lines of this generated `TaxonRecord`, `NCBITaxon:1032320`,
Phyllobacterium sp. LCK-2009.5a: rank `SPECIES`, domain `BACTERIA`,
grounding `EXACT`, mapping status `SEEDED`. The provisional isolate taxon
has one NCBI name attestation, zero inventoried BacDive strains and one
seed event. It carries no nomenclature, mapping, genome, phenotype or
graph. No generated record, maintained input, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/phyllobacterium_sp_lck_2009_5a.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/phyllobacterium_sp_lck_2009_5a.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Structured comparisons | Identifier, label, rank, parent, code, empty synonyms, complete lineage, path, scope and attestation agree. |
| Embedded history | Strict validation and exact seed-event/scope comparison passed. |
| Standalone history | Ignored-inclusive identifier, label and slug searches found no target entry under `history/`. |
| Graph/product grounding | Not applicable: no causal graph or curator-added product assertion is carried. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused source
comparisons are not corpus reproduction. No generator or history writer ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220823`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032320&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032320)
agree on the exact name, species rank, parent `NCBITaxon:2638441`, code
11 and the source lineage. All ten root-first entries match the inventory,
through Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Hyphomicrobiales, Phyllobacteriaceae, Phyllobacterium and unclassified
Phyllobacterium. Datasets includes root. No synonym is supplied.
The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:30105`.

`data/taxa/PATHS.tsv:13186` and `curation/seed_scope.tsv:321204` support
the path and one-source seed reason. Preserve the full LCK-2009.5a suffix.
Species rank satisfies scope, but a provisional name does not establish
valid publication or a type culture. The taxonomy browser was unavailable;
both structured authority endpoints succeeded.

## Evidence

- The sole NCBI attestation has count one, unit `NAME` and snapshot
  2026-09-13, exactly as inventoried. It is not a genome or trait assertion.
- Exact Nuccore query `txid1032320[Organism:noexp]` returned one sequence.
  Inspected [JF742957.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742957.1)
  is a 795-base partial 16S sequence with the exact organism, strain
  LCK-2009.5a and taxon1032320. Its source annotation places collection
  in Icelandic rock in July 2009; that remains isolate-level context.
- The marker has an unpublished Kelly/Cockell reference and a March 28,
  2011 direct submission, without DOI or PMID. The study title mentions
  actinobacteria and rock weathering; it does not override this isolate's
  Alphaproteobacteria classification or prove a weathering function.
- Complete structured scans found no target row in BacDive, LPSN, GTDB,
  GOLD, MediaDive, Madin or BactoTraits inventories and no backbone child.
  Zero `strain_count` counts inventoried BacDive records, not biological
  isolates or all external strain evidence.
- Ignored-inclusive native catalog searches found the NCBI name and
  unrelated numeric matches. GenBank shard 0014 row 22423 is
  GCA_015913555.1, Escherichia coli, taxon562, with strain=1032320.
  Shard 0009 row 5002 is GCA_010323205.1, Campylobacter jejuni,
  taxon197. The ATB table matches SAMEA1032320 for Salmonella Pullorum
  and SRR31032320 for an E. coli sample. None is evidence for this taxon;
  bare numbers and accession substrings are not identity joins.
- iModulonDB is not applicable: no gene-function, regulator, pathway,
  phenotype or expression-module claim is carried. A 16S identity marker
  does not warrant another organism's module evidence.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, so it
is an unsuccessful indexed match rather than global genome-absence proof.
The ignored-inclusive native searches found no target-associated assembly
after excluding the unrelated numeric matches described above.

Complete target scans of raw inventories found no type-material,
culture-collection, merged-ID or dropped-row entry. Identifier, label,
slug and isolate-spelling searches covered raw inventories, SI link,
assembly, related-record and exclusion tables, ATB strain/genome links
and exclusions, `curation/` and `history/`. Only the backbone and scope
rows matched those surfaces. Native searches covered all catalog shards,
BacDive, BV-BRC, GOLD, SeqCode and StrainInfo, including ignored files.

No inventoried BacDive strain or eligible own deposit starts a StrainInfo
join; no carried BIOSAMPLE assertion starts an ATB join. The compressed
ATB catalog was searched for target strings, but sample eligibility,
available FASTAs and sequence equivalence were not audited. No global
ATB absence claim follows. The optional marker need not be a genome link.
Empty nomenclature, mappings, synonyms, definition, general evidence,
discussions and graph slots are appropriate.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input fix is required.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future
taxonomy corrections belong in the pinned NCBI input,
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and the normal
seeder. Optional enrichment needs separately authorized maintained evidence,
not a manual YAML edit, numeric match or study-title inference.

## Follow-up Checks

- At refresh, verify the exact taxon and full isolate suffix against
  explicit merge or replacement evidence.
- For enrichment, establish own strain/deposit identity and distinguish
  markers from assemblies and isolate evidence from species-wide claims.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:1032320, both focused validators and then full
  `just verify-corpus` and `just qc` before publication.

## Additional Notes

All absence checks included ignored and hidden files through complete
structured scans or `rg --no-ignore --hidden -z`. The initial marker fetch
received HTTP429; an independent retry succeeded and supplied the inspected
sequence metadata. No optional context was inserted into the YAML.
Only free public sources were used; no GitHub mutation, outbound message,
history event or status promotion occurred. Older reports and completed
Eukaryota coverage were untouched.
