# YAML Record Review: Mycobacterium sp. LCK-2009.14b

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mycobacterium_sp_lck_2009_14b.yaml`
- Started UTC: 2026-10-03T22:28:20Z
- Finished UTC: 2026-10-03T22:29:40Z
- Verdict: pass

## Target

Read all 54 lines of this generated `TaxonRecord`, `NCBITaxon:1032316`,
Mycobacterium sp. LCK-2009.14b: rank `SPECIES`, domain `BACTERIA`, grounding
`EXACT`, mapping status `SEEDED`. This provisional isolate taxon has one
NCBI name attestation, zero inventoried BacDive strains and one seed event.
It carries no nomenclature, mappings, genomes, phenotypes, general evidence
or graph. No record, source input, history, status or earlier report changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/mycobacterium_sp_lck_2009_14b.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/mycobacterium_sp_lck_2009_14b.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Inventory comparisons | Identity, empty synonyms, ten root-first lineage entries, scope, path and attestation agree. |
| Embedded history | Strict validation passed; seed timestamp, one-source context and scope reason agree. |
| Standalone history | Not applicable: ignored-inclusive identifier, label and slug searches in `history/` found no target entry. |
| Graph and product gates | Not applicable: no graph or curator-added product grounding is carried. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports or sequence alignment. Focused
comparisons do not prove corpus reproduction. No generator or history writer ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220819` supports the exact identifier/name,
species rank, parent `NCBITaxon:2642494` and code 11. The inspected
[NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032316),
[EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032316&retmode=xml)
and [taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032316)
agree with the name and lineage through Mycobacteriales, Mycobacteriaceae,
Mycobacterium and unclassified Mycobacterium; Datasets includes root.
All three public reads succeeded. The native name row is
`data/catalog/ncbi_names-0005.jsonl.gz:30101`. No synonym is supplied in
the inspected taxonomy evidence.

`data/taxa/PATHS.tsv:13181` and `curation/seed_scope.tsv:321200` agree
with the path and seed reason. Preserve the full `LCK-2009.14b` suffix
and source lineage. Species rank satisfies scope but does not establish
valid publication, a formal epithet or a type culture. Higher ranks are context.

## Evidence

- The sole NCBI identifier/name, count one, unit `NAME` and snapshot
  2026-09-13 agree with the inventory. This attests a name, not a genome
  count or biological function.
- Exact Nuccore query `txid1032316[Organism:noexp]` returned one sequence.
  Inspected [JF742923.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742923.1)
  is a 935-base partial 16S rRNA sequence with the exact organism name,
  strain LCK-2009.14b and `taxon:1032316`. Its annotation describes Icelandic
  rock collected in July 2009. It supports isolate identity, not an assembly
  or registered culture deposit.
- The marker's inspected references comprise an unpublished Kelly/Cockell
  study title about actinobacteria and rock weathering and a direct submission
  dated March 28, 2011, without DOI or PMID. The title does not establish
  a weathering phenotype or mechanism for this isolate; the YAML claims neither.
- Complete structured scans found no target row in BacDive, LPSN, GTDB,
  GOLD, MediaDive, Madin or BactoTraits inventories and no child in the
  backbone. Zero `strain_count` counts inventoried BacDive records, not
  the existence or number of biological isolates.
- Ignored-inclusive identifier, label and slug searches across all native
  JSONL shards in `data/catalog/`, BacDive, BV-BRC, GOLD, StrainInfo and
  SeqCode found the NCBI name and one unrelated numeric match.
  `data/catalog/ncbi_genbank-0014.jsonl.gz:11735` describes GCA_015696265.1,
  Salmonella enterica serovar Enteritidis, taxon 149539, with bare strain
  name 1032316. Its genome and sample are not evidence for this
  Mycobacterium taxon.
- iModulonDB is not applicable: no gene, regulator, pathway, trait or
  transcriptomics claim is carried. Partial 16S identity context does not
  justify another organism's expression modules.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with `phrasesnotfound` and no-items warnings: an
unsuccessful indexed match, not global proof of genome absence. Native
catalog searches found no target-associated genome after excluding the
unrelated Salmonella strain.

Full target scans of NCBI type-material, culture-collection, merged-ID and
dropped inventories found no row. Ignored-inclusive identifier, label, slug
and isolate-spelling searches through raw inventories and SI/ATB link,
assembly, related-record and exclusion surfaces found only the backbone
row; curation returned the scope row and history returned none. These
absence conclusions are bounded to the inspected surfaces.

The marker is optional context, not a mandatory missing assembly. There
is no inventoried BacDive strain or eligible own deposit for a StrainInfo
overlay and no BIOSAMPLE assertion for an ATB join. The full ATB sample
catalog was not audited; no global ATB absence is claimed. Empty optional
nomenclature, synonyms, mappings, definition, general evidence, discussions
and graphs are appropriate. Do not invent a formal species, deposit, genome
or trait from the provisional name.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input fix is required.

## Recommended Edits

None required; preserve the generated record and `SEEDED` status. Future
taxonomy corrections belong in the pinned NCBI input,
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and the normal
seeder. Optional enrichment requires separately authorized maintained
curation, not a manual YAML edit, numeric join or transfer from another isolate.

## Follow-up Checks

- At source refresh, check the exact taxon, full suffix and explicit merge
  or replacement evidence.
- For enrichment, establish strain/deposit identity and distinguish markers
  from genomes, excluding unrelated numeric catalog matches.
- After authorized changes, use documented extraction and seed dry runs,
  a canary for NCBITaxon:1032316, both focused validators, then full
  `just verify-corpus` and `just qc` before publication.

## Additional Notes

All absence checks included ignored and hidden files through complete
structured scans or `rg --no-ignore --hidden -z`. Only free public source
reads were used. No optional context was inserted into the YAML; no outbound
message, GitHub mutation, history event or status promotion occurred.
Earlier reports and completed Eukaryota coverage were untouched.
