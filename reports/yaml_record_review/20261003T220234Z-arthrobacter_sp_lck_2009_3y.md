# YAML Record Review: Arthrobacter sp. LCK-2009.3y

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_lck_2009_3y.yaml`
- Started UTC: 2026-10-03T22:01:18Z
- Finished UTC: 2026-10-03T22:02:34Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord`, `NCBITaxon:1032304`,
Arthrobacter sp. LCK-2009.3y, rank `SPECIES`, domain `BACTERIA`, grounding
`EXACT`, mapping status `SEEDED`. This is the provisional isolate taxon,
not the genus Arthrobacter or another LCK isolate.

It carries one NCBI name attestation, zero inventoried BacDive strains
and a seed event. There are no nomenclature, mappings, genome assertions,
phenotypes, general evidence or causal graph. This review changes no
YAML, maintained input, scope, history, status or earlier report.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/arthrobacter_sp_lck_2009_3y.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/arthrobacter_sp_lck_2009_3y.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Inventory comparisons | Identity, empty synonyms, all ten root-first lineage entries, scope, path and sole attestation agree. |
| Embedded history | Strict validation passed; one-source seed context, timestamp and scope reason agree. |
| Standalone history | Not applicable: identifier, label and slug searches under `history/`, including ignored and hidden files, found no target entry. |
| Graph and ontology-product gates | Not applicable: no graph or curator-added product grounding occurs in the full YAML. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports or sequence alignment.
Focused comparisons do not prove corpus reproduction. No generator,
history writer or lifecycle-status promotion was run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220807` supports the identifier, exact name,
species rank, parent `NCBITaxon:235627` and genetic code 11. Live NCBI
[EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032304&retmode=xml)
and [taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032304)
agree with the lineage through Micrococcales, Micrococcaceae, Arthrobacter
and unclassified Arthrobacter; Datasets includes the root ancestor.
The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:30089`. No synonym is supplied in
the inspected taxonomy evidence.

The NCBI browser page was unavailable through the web tool; both structured
authority endpoints succeeded. Preserve the exact `LCK-2009.3y` suffix
and source parent chain without inferring a new placement from the marker.

`data/taxa/PATHS.tsv:13169` and `curation/seed_scope.tsv:321188` agree
with the filename and seed reason. NCBI species rank satisfies the scope
rule but does not establish valid publication, a formal epithet or a type
culture. Higher-ranked taxa appear only as lineage context.

## Evidence

- **Carried provenance:** The NCBI identifier/name, count one, unit `NAME`
  and snapshot 2026-09-13 agree with the backbone inventory. This attests
  a taxonomic name, not a genome count or biological function.
- **Independent marker:** Exact no-descendants Nuccore search
  `txid1032304[Organism:noexp]` returned one sequence. Inspected
  [JF742953.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742953.1) is a
  751-base partial 16S rRNA sequence with the exact organism name,
  strain LCK-2009.3y and `taxon:1032304`. Its source annotation describes
  an Icelandic rock sample collected in July 2009. This corroborates
  isolate identity, not a genome assembly or registered culture deposit.
- **Citation scope:** The sequence retains an unpublished Kelly/Cockell
  reference about actinobacteria and terrestrial rock weathering and a
  direct submission dated March 28, 2011. No DOI or PMID appears in
  those inspected reference objects. The title does not establish a
  weathering phenotype or causal mechanism for this isolate; the YAML
  claims neither.
- **Raw sources:** Complete structured scans found no target entry in
  BacDive strains, LPSN names, GTDB mappings, GOLD organisms, MediaDive,
  Madin or BactoTraits. A full backbone scan found no children.
  `strain_count: 0` counts inventoried BacDive strains without denying
  the existence of the sequenced isolate.
- **Native catalogs:** Ignored-inclusive identifier, exact label and slug
  searches across all native JSONL shards in `data/catalog/`, BacDive,
  BV-BRC, GOLD, StrainInfo and SeqCode found the NCBI name and one numeric
  collision. `data/catalog/ncbi_genbank-0014.jsonl.gz:11566` describes
  GCA_015692765.1, Listeria monocytogenes taxon 1639, with the bare strain
  name 1032304. It is not NCBITaxon:1032304 and cannot supply a genome or
  BioSample link for this Arthrobacter isolate.
- **Expression adapter:** iModulonDB is not applicable because no gene,
  regulator, pathway, trait or transcriptomics assertion is carried.
  External partial 16S identity context does not justify expression
  evidence from another organism.

## Completeness

No consequential missing representation was established. Exact NCBI
Assembly search returned zero records with `phrasesnotfound` and no-items
warnings. This is an unsuccessful indexed match, not global proof of
genome absence. The native catalog searches independently found no
target-associated genome evidence.

Full target scans of NCBI type-material, culture-collection, merged-ID and
dropped inventories found no row. Ignored-inclusive identifier, label,
slug and isolate-spelling searches through raw inventories and SI/ATB
link, assembly, related-record and exclusion surfaces found only the
backbone row. The curation hit was the scope row; history searches were
empty. These conclusions are bounded to the inspected source surfaces.

The partial marker is optional context, not a required missing assembly.
There is no inventoried BacDive strain or eligible own deposit to anchor
a StrainInfo overlay and no BIOSAMPLE assertion to support an ATB join.
The full ATB sample catalog was not audited; no global ATB absence is
claimed. Empty optional nomenclature, synonyms, mappings, definition,
general evidence, discussions and graphs are appropriate. Do not infer
a formal species, deposit, genome or trait from the provisional name.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. Identity authority and inspected
inventories agree; no maintained-input fix is required.

## Recommended Edits

None required. Preserve the generated record and `SEEDED` status.
Future authoritative taxonomy corrections belong in the pinned NCBI
source, `src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
the normal seeder. Optional marker or literature enrichment requires
separately authorized maintained curation with narrow evidence, not a
manual YAML edit, bare-number match or transfer from another LCK isolate.

## Follow-up Checks

- At a source refresh, verify the exact taxon, full isolate suffix and
  any explicit replacement or merge evidence.
- For optional enrichment, establish strain/deposit identity, distinguish
  marker sequences from assemblies and exclude the unrelated Listeria hit.
- For an authorized source change, use documented extraction and seed
  dry runs, a canary for NCBITaxon:1032304, both focused validators, then
  full-corpus `just verify-corpus` and `just qc` before publication.

## Additional Notes

All absence checks included ignored and hidden files through complete
structured scans or `rg --no-ignore --hidden -z`. Sequence evidence was
independently fetched for this exact taxon. Only public, free source reads
were used. No optional sequence context was inserted into the YAML, and
no outbound message, GitHub mutation, history event or status promotion
occurred. Earlier reports and completed Eukaryota coverage were untouched.
