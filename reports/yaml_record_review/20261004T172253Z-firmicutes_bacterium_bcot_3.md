# YAML Record Review: Firmicutes bacterium BCOT-3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/firmicutes_bacterium_bcot_3.yaml`
- Started UTC: 2026-10-04T17:21:57Z
- Finished UTC: 2026-10-04T17:22:53Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for NCBITaxon:1033675, Firmicutes bacterium BCOT-3. It is a species-ranked placeholder in BACTERIA, with `EXACT` grounding, `SEEDED` status, genetic code 11, `strain_count: 0`, one NCBITAXON NAME attestation and the deterministic seed event at 2026-09-13T17:54:04Z. The name does not denote BCOT-15 or another similarly prefixed isolate. No generated field was edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/firmicutes_bacterium_bcot_3.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/firmicutes_bacterium_bcot_3.yaml`: passed, one file scanned and zero errors.
- Ignored-inclusive exact-identifier search across `data/taxa`: only this YAML. Ignored-inclusive report-filename search found no existing report for this stem.
- Structured source comparison checked the full ancestor chain, target backbone, children, seven source inventories, PATHS, scope, attestation and seed-event text; all matched. Separate type-material, merged-ID and dropped-row checks returned no exact target rows.
- Not run: corpus-wide `just qc`, `just verify-corpus`, tests, provenance, render and documentation gates. Global term/reference and history checks were skipped; there are no curator-added graph terms, literature references or separate history artifacts asserted here. Strict validation covered embedded history shape. A bounded source comparison does not prove corpus reproduction.

## Identity and Grounding

The source row at `data/raw/ncbitaxon_taxa.tsv:221285` and complete native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30593` agree with the YAML. `data/taxa/PATHS.tsv:13738` pins the slug; `curation/seed_scope.tsv:321637` records the 2026-09-13 attested-rule inclusion.

The inspected [NCBI browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1033675&lvl=3&mode=node), [taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033675&retmode=xml) and [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033675) verify canonical name, species rank, parent 84086 and code 11. The root-first lineage is root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Bacillota 1239 (PHYLUM), unclassified Bacillota 84086 (NO_RANK). Datasets explicitly includes root 1. No live alternate name was returned.

The older Firmicutes wording in the canonical label coexists with Bacillota in the current lineage at NCBI itself. The repository correctly preserves those fields rather than normalizing the name or inferring a genus. Species rank and exact grounding do not establish formal nomenclatural publication.

## Evidence

The NCBITAXON attestation accurately counts one NAME from the 2026-09-13 snapshot. No direct BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row was present, and no child taxon was found. Zero strains therefore matches the inventoried BacDive subtree; it does not mean that the isolate was never cultured.

The exact-taxid Assembly query returned zero hits with no-items/phrase warnings. Nuccore returned one record: [HQ616501.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616501.1), UID 333408581, a 378-base partial 16S sequence. Inspected GenBank XML source qualifiers explicitly identify strain BCOT-3, taxon 1033675, genomic DNA, Mexico, collection on 2010-02-01 by R. Flores-Magallon and PCR primers. No culture-collection deposit or isolation-source qualifier was supplied. The web sequence page showed a browser check, but the structured sequence response was retrieved successfully. This is marker context, not an assembly.

Both sequence references were read. They name an unpublished Cotija-cheese study and a direct submission on 2010-11-10 by Flores-Magallon, Oliva-Hernandez and Narvaez-Zapata from Instituto Politecnico Nacional, Reynosa. The publisher metadata and abstract of [DOI 10.1007/s10068-011-0137-z](https://link.springer.com/article/10.1007/s10068-011-0137-z), inspected during the immediately preceding review, describe a related 2011 study by the same authors but do not identify BCOT-3 or HQ616501. Its full body was not available. That candidate cannot establish a strain-specific phenotype or finer classification here. The institutional thesis retrieval in that preceding check also failed; no thesis snippet was promoted to evidence.

The full matching ATB row at `data/catalog/allthebacteria.tsv.xz:65035` is SAMEA1033675, ERR068133, ERZ3069116. Its scientific and both Sylph labels are Streptococcus pneumoniae; assembly/FASTA and quality statuses are available/PASS, with prior HQ T. Only the BioSample number and download-path suffix match the taxid's digits. There is no target strain-to-sample chain. Its SeqKit sum, batch-600 OSF archive and mutable AWS URL are retained source context, not evidence for a BCOT-3 genome. Available FASTA status does not cure the identity mismatch.

## Completeness

Ignored-inclusive compressed searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Bounded queries included the taxid, BCOT-3 separator variants and label/slug forms. Four matching lines were inspected: target backbone, scope, native name and unrelated ATB row. A separate structured SOURCE.json scan found no matching manifest evidence in those source roots.

No missing required representation was identified. Optional nomenclature, mappings, evidence, datasets, discussions, strains and causal graphs may remain absent. The short marker and shared study context do not identify a deposit or establish equivalence with another BCOT isolate. No assembly linked to this exact taxid was found, but this bounded query does not exclude sequences filed under other identifiers.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the asserted record fields. Literature access limits remain an optional enrichment uncertainty, not a failed NCBI identity check.

## Recommended Edits

None required. Future supported additions belong in the configured upstream source, `scripts/extract_source_inventory.py`, or a tested `src/taxonmech/seed.py` change. Do not hand-edit the generated YAML, manufacture a BacDive identity, transfer another isolate's findings or change NCBI lineage from a study-level description.

## Follow-up Checks

Obtain inspected primary text explicitly naming BCOT-3 or HQ616501 before claiming literature-supported identity or function. For any later maintained-source update, run the seed dry-run and single-record canary, inspect the emitted record, then repeat open/strict validation and full reproduction/QC. No mutation or canary was run in this review.

## Additional Notes

iModulonDB was not applicable: the record names no gene, regulator, pathway or expression-module claim. No paid research, contact, GitHub action, status promotion or history write occurred. Only this new report was written for the target, and Eukaryota was not revisited.
