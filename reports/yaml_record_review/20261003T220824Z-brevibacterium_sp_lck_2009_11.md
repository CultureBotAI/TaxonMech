# YAML Record Review: Brevibacterium sp. LCK-2009.11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/brevibacterium_sp_lck_2009_11.yaml`
- Started UTC: 2026-10-03T22:07:22Z
- Finished UTC: 2026-10-03T22:08:24Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord`, `NCBITaxon:1032307`,
Brevibacterium sp. LCK-2009.11, rank `SPECIES`, domain `BACTERIA`,
grounding `EXACT`, mapping status `SEEDED`. This is the provisional
isolate taxon, not the genus or another LCK isolate. It contains one NCBI
name attestation, zero inventoried BacDive strains and a seed event, with
no nomenclature, mappings, genome assertions, phenotypes, general evidence
or graph. No YAML, maintained input, history, status or prior report was
changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/brevibacterium_sp_lck_2009_11.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/brevibacterium_sp_lck_2009_11.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Inventory comparisons | Identity, empty synonyms, all ten root-first lineage entries, scope, path and sole attestation agree. |
| Embedded history | Strict validation passed; timestamp, one-source seed context and scope reason agree. |
| Standalone history | Not applicable: ignored-inclusive identifier, label and slug searches under `history/` found no target entry. |
| Graph and ontology-product gates | Not applicable: neither graph nor curator-added product grounding is present. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports or sequence alignment.
Focused comparisons do not prove corpus reproduction. No generator,
history writer or lifecycle-status promotion was run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220810` supports the exact identifier, name,
species rank, parent `NCBITaxon:2614124` and genetic code 11. Live NCBI
[EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032307&retmode=xml)
and [taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032307)
agree with the parent chain through Micrococcales, Brevibacteriaceae,
Brevibacterium and unclassified Brevibacterium; Datasets includes root.
The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:30092`. No synonym is supplied in
the inspected taxonomy evidence. The NCBI browser page was unavailable
through the web tool; both structured authority endpoints succeeded.

`data/taxa/PATHS.tsv:13172` and `curation/seed_scope.tsv:321191` agree
with the filename and seed reason. Preserve the full `LCK-2009.11`
suffix and the source lineage. NCBI species rank meets the scope rule
but does not establish a formal epithet, valid publication or type culture.
Higher-ranked taxa appear only as lineage context.

## Evidence

- **Carried provenance:** Exact NCBI identifier/name, count one, unit
  `NAME` and snapshot 2026-09-13 agree with the backbone inventory.
  This attests a taxonomic name, not a genome or biological function.
- **Independent marker:** Exact no-descendants Nuccore search
  `txid1032307[Organism:noexp]` returned one sequence. Inspected
  [JF742920.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742920.1) is an
  837-base partial 16S rRNA sequence with the exact organism name,
  strain LCK-2009.11 and `taxon:1032307`. Its source annotation describes
  Icelandic rock collected in July 2009. This corroborates isolate
  identity, not a genome assembly or registered culture deposit.
- **Citation scope:** The marker carries an unpublished Kelly/Cockell
  reference about actinobacteria and rock weathering and a direct
  submission dated March 28, 2011. No DOI or PMID appears in the inspected
  reference objects. The title does not establish a weathering phenotype
  or causal mechanism for this isolate; the YAML asserts neither.
- **Raw sources:** Complete structured scans found no target entry in
  BacDive strains, LPSN names, GTDB mappings, GOLD organisms, MediaDive,
  Madin or BactoTraits. The full backbone scan found no children.
  `strain_count: 0` counts inventoried BacDive records, not physical isolates.
- **Native catalogs:** Ignored-inclusive identifier, exact label and slug
  searches across native JSONL shards in `data/catalog/`, BacDive,
  BV-BRC, GOLD, StrainInfo and SeqCode found the NCBI name and one numeric
  collision. `data/catalog/ncbi_genbank-0014.jsonl.gz:11681` describes
  GCA_015695185.1, Salmonella enterica serovar Enteritidis, taxon 149539,
  with the bare strain name 1032307. Its genome and BioSample are not
  evidence for NCBITaxon:1032307.
- **Expression adapter:** iModulonDB is not applicable: no gene, regulator,
  pathway, trait or transcriptomics assertion is carried. External partial
  16S identity context does not justify cross-organism expression evidence.

## Completeness

No consequential missing representation was established. Exact NCBI
Assembly search returned zero records with `phrasesnotfound` and no-items
warnings. This is an unsuccessful indexed match, not global proof of
genome absence. Native searches independently found no target-associated
genome evidence after excluding the Salmonella numeric collision.

Full target scans of NCBI type-material, culture-collection, merged-ID and
dropped inventories found no row. Ignored-inclusive identifier, label,
slug and isolate-spelling searches through raw inventories and SI/ATB
link, assembly, related-record and exclusion surfaces found only the
backbone row; curation returned the scope row and history returned none.
These conclusions are bounded to the inspected surfaces.

The partial marker is optional context, not a mandatory missing assembly.
There is no inventoried BacDive strain or eligible own deposit to anchor
a StrainInfo overlay, nor a BIOSAMPLE assertion for an ATB join. The full
ATB sample catalog was not audited; no global ATB absence is claimed.
Empty optional nomenclature, synonyms, mappings, definition, general
evidence, discussions and graphs are appropriate. Do not infer a formal
species, culture deposit, genome or trait from the provisional name.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this focused review. Identity authority and inspected
inventories agree; no maintained-input fix is required.

## Recommended Edits

None required. Preserve the generated record and `SEEDED` status. Future
authoritative taxonomy corrections belong in the pinned NCBI source,
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and the normal
seeder. Optional marker or literature enrichment requires separately
authorized maintained curation, not a manual YAML edit, bare-number join
or evidence transferred from another LCK isolate.

## Follow-up Checks

- At source refresh, verify the exact taxon, full isolate suffix and any
  explicit replacement or merge evidence.
- For optional enrichment, establish strain/deposit identity, distinguish
  markers from assemblies and exclude the unrelated Salmonella hit.
- After an authorized source change, use documented extraction and seed
  dry runs, a canary for NCBITaxon:1032307, both focused validators, then
  full-corpus `just verify-corpus` and `just qc` before publication.

## Additional Notes

All absence checks included ignored and hidden files through complete
structured scans or `rg --no-ignore --hidden -z`. Sequence evidence was
fetched independently for this exact taxon. Only public, free reads were
used. No optional sequence context was inserted into the YAML; no outbound
message, GitHub mutation, history event or status promotion occurred.
Earlier reports and completed Eukaryota coverage were untouched.
