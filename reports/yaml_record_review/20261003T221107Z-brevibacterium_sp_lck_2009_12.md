# YAML Record Review: Brevibacterium sp. LCK-2009.12

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/brevibacterium_sp_lck_2009_12.yaml`
- Started UTC: 2026-10-03T22:09:58Z
- Finished UTC: 2026-10-03T22:11:07Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord`, `NCBITaxon:1032308`,
Brevibacterium sp. LCK-2009.12: rank `SPECIES`, domain `BACTERIA`,
grounding `EXACT`, mapping status `SEEDED`. This provisional isolate
taxon carries one NCBI name attestation, zero inventoried BacDive strains
and one seed event. It has no nomenclature, mappings, genomes, phenotypes,
general evidence or graph. No record, source input, history, status or
earlier report was changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/brevibacterium_sp_lck_2009_12.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/brevibacterium_sp_lck_2009_12.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Source comparisons | Identity, empty synonyms, all ten root-first lineage entries, scope, path and sole attestation agree. |
| Embedded history | Strict validation passed; timestamp, one-source context and scope reason agree. |
| Standalone history | Not applicable: ignored-inclusive identifier, label and slug searches in `history/` found no target entry. |
| Graph and ontology-product gates | Not applicable: neither graph nor curator-added product grounding is present. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports or sequence alignment. The
focused comparisons do not prove corpus reproduction. No generator,
history writer or lifecycle-status promotion was run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220811` supports the exact identifier/name,
species rank, parent `NCBITaxon:2614124` and genetic code 11. Live NCBI
[EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032308&retmode=xml)
and [taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032308)
agree with the chain through Micrococcales, Brevibacteriaceae,
Brevibacterium and unclassified Brevibacterium; Datasets includes root.
The native name row is `data/catalog/ncbi_names-0005.jsonl.gz:30093`.
No synonym is supplied in the inspected taxonomy evidence. The browser
page was unavailable through the web tool; both structured endpoints worked.

`data/taxa/PATHS.tsv:13173` and `curation/seed_scope.tsv:321192` agree
with the path and seed reason. Preserve the full `LCK-2009.12` suffix and
source lineage. NCBI species rank satisfies scope but does not establish
valid publication, a formal epithet or a type culture. Higher-ranked
taxa are lineage context, not additional records.

## Evidence

- **Carried provenance:** Exact NCBI identifier/name, count one, unit
  `NAME` and snapshot 2026-09-13 agree with the backbone inventory. This
  is a name attestation, not a genome count or functional assertion.
- **Marker identity:** Exact Nuccore query `txid1032308[Organism:noexp]`
  returned one sequence. Inspected
  [JF742921.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742921.1) is an
  827-base partial 16S rRNA sequence bearing the exact organism name,
  strain LCK-2009.12 and `taxon:1032308`. Source annotation describes
  Icelandic rock collected in July 2009. This supports isolate identity,
  not an assembly, registered culture deposit or demonstrated phenotype.
- **Citation scope:** The marker cites an unpublished Kelly/Cockell
  reference about actinobacteria and rock weathering and a direct
  submission dated March 28, 2011. The inspected reference objects have
  no DOI or PMID. The title alone does not prove a weathering mechanism
  for this isolate; the YAML makes no such claim.
- **Raw inventories:** Complete scans found no target entry in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories and no
  child in the full backbone. Zero `strain_count` means zero inventoried
  BacDive records, not that no biological isolate exists.
- **Native catalog exclusions:** Ignored-inclusive identifier, exact label
  and slug searches across native JSONL shards in `data/catalog/`, BacDive,
  BV-BRC, GOLD, StrainInfo and SeqCode found the name and two numeric
  collisions. `data/catalog/ncbi_genbank-0014.jsonl.gz:11564` describes
  GCA_015692725.1, Salmonella enterica serovar Oslo, taxon 1005394,
  strain 1032308. `data/catalog/ncbi_genbank-0054.jsonl.gz:17317`
  describes GCA_058712145.1, Streptococcus pneumoniae, taxon 1313,
  isolate 1032308. Neither genome or sample belongs to this Brevibacterium
  taxon on that evidence; the unrelated second hit's PMID is not a
  citation supporting this record.
- **Expression adapter:** iModulonDB is not applicable: the record carries
  no gene, regulator, pathway, trait or transcriptomics assertion. External
  partial 16S identity context does not justify another organism's modules.

## Completeness

No consequential missing representation was established. Exact NCBI
Assembly query returned zero records with `phrasesnotfound` and no-items
warnings: an unsuccessful indexed match, not global proof of genome
absence. Native searches found no target-associated genome evidence after
excluding the two numeric collisions.

Full scans of NCBI type-material, culture-collection, merged-ID and dropped
inventories found no target row. Ignored-inclusive identifier, label, slug
and isolate-spelling searches through raw inventories and SI/ATB link,
assembly, related-record and exclusion surfaces returned only the backbone
row; curation returned the scope row, and history returned none. Absence
conclusions are bounded to these inspected surfaces.

The partial marker is optional context, not a required missing assembly.
No inventoried BacDive strain or eligible own deposit anchors a StrainInfo
overlay, and no BIOSAMPLE assertion supports an ATB join. The full ATB
sample catalog was not audited; no global ATB absence is claimed. Empty
optional nomenclature, synonyms, mappings, definition, evidence, discussions
and graphs are appropriate. Do not infer a formal species, deposit, genome
or trait from the provisional name.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input fix is required.

## Recommended Edits

None required; preserve the generated record and `SEEDED` status. Future
taxonomy corrections belong in the pinned NCBI input,
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and the normal
seeder. Optional marker/literature enrichment requires separately authorized
maintained curation, not a hand-edited YAML, numeric join or transferred
evidence from another LCK isolate.

## Follow-up Checks

- At source refresh, check the exact taxon, full isolate suffix and explicit
  merge or replacement evidence.
- For enrichment, establish actual strain/deposit identity, distinguish
  markers from genomes and exclude unrelated numeric catalog matches.
- After authorized source changes, use documented extraction and seed dry
  runs, a canary for NCBITaxon:1032308, both focused validators and full
  `just verify-corpus` and `just qc` before publication.

## Additional Notes

All absence checks included ignored and hidden files through complete
structured scans or `rg --no-ignore --hidden -z`. Only free public source
reads were used. No optional context was inserted into the YAML; no outbound
message, GitHub mutation, history event or status promotion occurred.
Earlier reports and completed Eukaryota coverage were untouched.
