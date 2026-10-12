# YAML Record Review: Cytophagaceae bacterium LCK-2009.32

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/cytophagaceae_bacterium_lck_2009_32.yaml`
- Started UTC: 2026-10-03T22:15:51Z
- Finished UTC: 2026-10-03T22:16:59Z
- Verdict: pass

## Target

Read all 57 lines of the generated `TaxonRecord`, `NCBITaxon:1032311`,
Cytophagaceae bacterium LCK-2009.32: rank `SPECIES`, domain `BACTERIA`,
grounding `EXACT`, mapping status `SEEDED`. This provisional isolate taxon
is not the family Cytophagaceae. It has one NCBI name attestation, zero
inventoried BacDive strains and a seed event, without nomenclature,
mappings, genomes, phenotypes, general evidence or graph. No record,
maintained input, history, status or earlier report was changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/cytophagaceae_bacterium_lck_2009_32.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/cytophagaceae_bacterium_lck_2009_32.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Source comparisons | Identity, empty synonyms, all eleven root-first lineage entries, scope, path and sole attestation agree. |
| Embedded history | Strict validation passed; timestamp, one-source context and scope reason agree. |
| Standalone history | Not applicable: ignored-inclusive identifier, label and slug searches in `history/` found no target entry. |
| Graph and ontology-product gates | Not applicable: no graph or curator-added product grounding is present. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports or sequence alignment. Focused
comparisons do not prove corpus reproduction. No generator, history writer
or lifecycle-status promotion was run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220814` supports the exact identifier/name,
species rank, parent `NCBITaxon:94253` and genetic code 11. Live NCBI
[EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032311&retmode=xml)
and [taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032311)
agree with the chain through Pseudomonadati, FCB group,
Bacteroidota/Chlorobiota group, Bacteroidota, Cytophagia, Cytophagales,
Cytophagaceae and unclassified Cytophagaceae; Datasets includes root.
The native name row is `data/catalog/ncbi_names-0005.jsonl.gz:30096`.
No synonym is supplied in the inspected taxonomy evidence. The browser
page was unavailable through the web tool; both structured endpoints worked.

`data/taxa/PATHS.tsv:13176` and `curation/seed_scope.tsv:321195` agree
with the filename and seed reason. The target's species rank satisfies
scope despite its family-based provisional label. Family `NCBITaxon:89373`
and unclassified parent `NCBITaxon:94253` are different entities. Preserve
the exact `LCK-2009.32` suffix, clade ranks and source lineage; do not
invent a genus or infer valid publication or a type culture from the name.

## Evidence

- **Carried provenance:** Exact NCBI identifier/name, count one, unit
  `NAME` and snapshot 2026-09-13 agree with the backbone inventory. This
  is a name attestation, not a genome count or functional assertion.
- **Marker identity:** Exact Nuccore query `txid1032311[Organism:noexp]`
  returned one sequence. Inspected
  [JF742943.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742943.1) is a
  797-base partial 16S rRNA sequence with the exact organism name,
  strain LCK-2009.32 and `taxon:1032311`. Source annotation describes
  Icelandic rock collected in July 2009. This supports isolate identity,
  not an assembly, registered culture deposit or demonstrated phenotype.
- **Citation scope:** The marker cites an unpublished Kelly/Cockell
  reference about actinobacteria and rock weathering and a direct
  submission dated March 28, 2011. The inspected reference objects have
  no DOI or PMID. That broad title neither places the isolate in
  Actinomycetota nor proves a weathering mechanism. The actual taxonomy
  places this isolate in Bacteroidota; the YAML does not import the
  title's taxonomic scope or a phenotype.
- **Raw inventories:** Complete scans found no target entry in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories and no
  child in the full backbone. Zero `strain_count` means zero inventoried
  BacDive records, not that no biological isolate exists.
- **Native catalog exclusion:** Ignored-inclusive identifier, exact label
  and slug searches across native JSONL shards in `data/catalog/`, BacDive,
  BV-BRC, GOLD, StrainInfo and SeqCode found the name and one unrelated
  numeric hit. `data/catalog/ncbi_genbank-0067.jsonl.gz:12096` describes
  GCA_988140645.1, uncultured bacterium, taxon 77133, isolate
  MFD15113.bin.s.113; 1032311 is its genome length. It does not identify
  NCBITaxon:1032311 or justify transferring its genome or sample.
- **Expression adapter:** iModulonDB is not applicable: the record carries
  no gene, regulator, pathway, trait or transcriptomics assertion. External
  partial 16S context does not justify another organism's expression modules.

## Completeness

No consequential missing representation was established. Exact NCBI
Assembly query returned zero records with `phrasesnotfound` and no-items
warnings: an unsuccessful indexed match, not global proof of genome
absence. Native searches found no target-associated genome evidence after
excluding the unrelated genome-length match.

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
and graphs are appropriate. The missing genus is part of the source's
unclassified placement, not a license to infer one or a required missing
lineage node. Do not invent a formal species, deposit, genome or trait.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input fix is required.

## Recommended Edits

None required; preserve the generated record and `SEEDED` status. Future
taxonomy corrections belong in the pinned NCBI input,
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and the normal
seeder. Optional marker/literature enrichment requires separately authorized
maintained curation, not a hand-edited YAML, numeric join or classification
inferred from a study title or family-based provisional name.

## Follow-up Checks

- At source refresh, check the exact isolate taxon and full suffix,
  distinguishing it from the family and unclassified parent.
- For enrichment, establish actual strain/deposit identity, distinguish
  markers from genomes and retain the narrow scope of source evidence.
- After authorized source changes, use documented extraction and seed dry
  runs, a canary for NCBITaxon:1032311, both focused validators and full
  `just verify-corpus` and `just qc` before publication.

## Additional Notes

All absence checks included ignored and hidden files through complete
structured scans or `rg --no-ignore --hidden -z`. Only free public source
reads were used. No optional context was inserted into the YAML; no outbound
message, GitHub mutation, history event or status promotion occurred.
Earlier reports and completed Eukaryota coverage were untouched.
