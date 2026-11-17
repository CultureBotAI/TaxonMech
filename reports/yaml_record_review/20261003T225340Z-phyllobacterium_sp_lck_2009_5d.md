# YAML Record Review: Phyllobacterium sp. LCK-2009.5d

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/phyllobacterium_sp_lck_2009_5d.yaml`
- Started UTC: 2026-10-03T22:53:08Z
- Finished UTC: 2026-10-03T22:53:40Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord`, `NCBITaxon:1032321`,
Phyllobacterium sp. LCK-2009.5d, rank `SPECIES`, domain `BACTERIA`,
grounding `EXACT`, mapping status `SEEDED`. It contains one NCBI name
attestation, zero inventoried BacDive strains and one seed event. There
are no genome, phenotype, nomenclature, mapping or graph assertions.
No generated record, maintained input, history or status was changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/phyllobacterium_sp_lck_2009_5d.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/phyllobacterium_sp_lck_2009_5d.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Inventory comparison | Identifier, label, rank, parent, code, empty synonyms, ten-entry lineage, path, scope and attestation agree. |
| Embedded history | Strict validation and exact scope/seed-event comparison passed. |
| Standalone history | Ignored-inclusive identifier, label and slug searches found no target history entry. |
| Graph/product gate | Not applicable: no graph or curator-added product grounding is carried. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused
comparisons are not corpus reproduction. No generator or history writer ran.

## Identity and Grounding

The exact name, species rank, parent `NCBITaxon:2638441` and code 11 match
`data/raw/ncbitaxon_taxa.tsv:220824`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032321&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032321).
The ten root-first lineage entries agree through Pseudomonadati,
Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Phyllobacteriaceae,
Phyllobacterium and unclassified Phyllobacterium; Datasets includes root.
The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:30106`. No synonym is supplied.

Path row 13187 in `data/taxa/PATHS.tsv` and scope row 321205 in
`curation/seed_scope.tsv` support this exact target. Preserve suffix 5d;
neither a shared genus nor the similar LCK-2009.5a designation makes the
two isolates equivalent. Species rank satisfies repository scope without
asserting a formally published name or type culture. The taxonomy browser
was unavailable, but both structured authority endpoints succeeded.

## Evidence

- The sole NCBI attestation exactly matches the inventory: one `NAME`,
  snapshot 2026-09-13. No genome or phenotype is implied by that count.
- Exact Nuccore query `txid1032321[Organism:noexp]` returned one sequence.
  Inspected [JF742959.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742959.1)
  is a 789-base partial 16S sequence with the exact organism name,
  strain LCK-2009.5d and taxon1032321. Source annotation records Icelandic
  rock collected in July 2009; this is isolate-level context, not a genome
  assembly or culture-collection registration.
- The sequence references contain an unpublished Kelly/Cockell study and
  a March 28, 2011 direct submission, without DOI or PMID. The study
  title's actinobacteria/rock-weathering wording does not classify this
  Alphaproteobacteria isolate or prove a weathering mechanism.
- Complete structured scans found no target row in BacDive, LPSN, GTDB,
  GOLD, MediaDive, Madin or BactoTraits inventories and no backbone child.
  Zero `strain_count` is the inventoried BacDive count, not a claim that
  no biological isolate exists.
- Ignored-inclusive native searches found the NCBI name and three
  unrelated ATB numeric hits: SAMEA1032321 is Salmonella Pullorum;
  run SRR11032321 belongs to Campylobacter jejuni sample SAMN14049793;
  run SRR31032321 belongs to Klebsiella pneumoniae sample SAMN44336054.
  These are rows 62595, 1776148 and 3092018 of the compressed native ATB
  table. None supplies an identity or genome link for this Phyllobacterium.
- iModulonDB is not applicable: the record carries no gene-function,
  regulator, pathway, trait or transcriptomics assertion. A 16S marker
  does not authorize transfer of another organism's expression modules.

## Completeness

No consequential gap was established. Exact Assembly query returned zero
with phrases-not-found and no-items warnings. This is not global proof
that no genome exists. Native catalog searches found no target-associated
assembly; the unrelated ATB accession/run substrings were excluded.

Identifier, label, slug and isolate-spelling searches included ignored
and hidden files throughout raw inventories, all native catalog shards,
BacDive, BV-BRC, GOLD, SeqCode and StrainInfo. Searches also covered SI
strain links, assemblies, related records and exclusions, ATB strain and
genome links and exclusions, curation and history. The raw and maintained
surfaces returned only the backbone and scope rows. No target type-material,
culture-collection, merged-ID, dropped-row or standalone history entry was
found within these complete scans.

The optional marker is not a missing assembly. No inventoried BacDive
strain or eligible own deposit starts a SI join, and no carried BIOSAMPLE
assertion starts an ATB join. The ATB catalog was searched for target
strings, but sample/FASTA eligibility and sequence equivalence were not
audited; no global ATB-absence claim follows. Empty optional synonyms,
nomenclature, mappings, definitions, general evidence, discussions and
graphs are appropriate.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input fix is required.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future
taxonomy corrections belong in the pinned NCBI input,
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and the seeder.
Optional enrichment requires separately authorized maintained evidence,
not a manual record edit, accession substring or shared-name inference.

## Follow-up Checks

- At source refresh, recheck the exact taxon and suffix 5d, preserving
  distinct related isolates unless explicit identity evidence says otherwise.
- For enrichment, establish own deposit and assembly provenance without
  promoting marker context to genome or species-wide phenotype evidence.
- After authorized changes, use documented extraction/seed dry runs,
  a canary for NCBITaxon:1032321, both focused validators, then
  `just verify-corpus` and `just qc` before publication.

## Additional Notes

All absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
source reads were used. No optional marker context was inserted into the
YAML, and no outbound message, GitHub mutation, history event or status
promotion occurred. Older reports and completed Eukaryota coverage remain
untouched.
