# YAML Record Review: Lactobacillales bacterium BCOT-14

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lactobacillales_bacterium_bcot_14.yaml`
- Started UTC: 2026-10-04T17:36:26Z
- Finished UTC: 2026-10-04T17:37:27Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for NCBITaxon:1033682, Lactobacillales bacterium BCOT-14. It is a species-ranked BACTERIA placeholder, not another BCOT isolate or a genome. It carries `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried BacDive strains, one NCBITAXON NAME attestation and a seed event dated 2026-09-13T17:54:04Z. No generated field was edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/lactobacillales_bacterium_bcot_14.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/lactobacillales_bacterium_bcot_14.yaml`: passed, one file scanned and zero errors.
- Completed ignored-inclusive exact-identifier search across `data/taxa`: only this YAML. Ignored-inclusive exact-stem report search found no previous report.
- Structured comparisons matched backbone, complete lineage, children, seven source inventories, PATHS, scope, attestation and embedded seed text. Exact type-material, merged-ID and dropped-row checks also completed.
- Not run: full-corpus `just qc`, `just verify-corpus`, tests, provenance, render and documentation gates. Global term/reference and history validation were skipped; no curator-added graph terms, literature references or separate history artifacts are asserted here. Strict validation covered embedded history shape. Focused source comparisons do not prove corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221292` and the complete native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30600` match the record. `data/taxa/PATHS.tsv:13745` pins the identifier/slug and `curation/seed_scope.tsv:321644` records the 2026-09-13 attested-rule inclusion.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033682&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033682) confirm canonical name, species rank, parent 263855 and code 11. No alternate name was returned. The root-first chain matches root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Bacillota 1239 (PHYLUM), Bacilli 91061 (CLASS), Lactobacillales 186826 (ORDER), unclassified Lactobacillales 263855 (NO_RANK). Datasets explicitly supplies root 1. The browser was unavailable; the structured authority responses were successful.

The NCBI placeholder is eligible at species rank but does not establish formal nomenclatural publication or a genus-level identity. The unresolved lineage is correctly carried rather than inferred from nearby study records.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME in snapshot 2026-09-13. Exact inventory scans found no BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits rows and no child taxa. Type-material, merged-ID and dropped inventories had no target rows. Thus zero strains agrees with BacDive coverage; it does not assert that BCOT-14 was never cultured.

Exact-taxid searches returned zero Assembly hits with no-items/phrase warnings and one Nuccore record. [HQ616512.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616512.1), UID 333408592, is a 672-base partial 16S sequence. Inspected GenBank XML source qualifiers identify genomic DNA, strain BCOT-14, taxon 1033682, Mexico, collection on 2010-02-01 by R. Flores-Magallon and PCR primers. Neither a culture-collection deposit nor an isolation-source qualifier is supplied. The web sequence page displayed a browser check, but the structured sequence record was retrieved successfully. A marker is not a genome assembly.

Both sequence references were inspected. They name an unpublished Cotija-cheese study and a direct submission on 2010-11-10 by Flores-Magallon, Oliva-Hernandez and Narvaez-Zapata, Instituto Politecnico Nacional, Reynosa. The related [2011 article, DOI 10.1007/s10068-011-0137-z](https://link.springer.com/article/10.1007/s10068-011-0137-z), was inspected at its publisher earlier in this session. Accessible metadata and abstract do not name BCOT-14 or HQ616512. Full paper and institutional thesis retrieval were unavailable in those checks. No phenotype, maturation stage or finer classification is inferred from shared authors, a common study topic or indexed thesis snippets.

The ATB row at `data/catalog/allthebacteria.tsv.xz:65043` is SAMEA1033682, ERR068189, ERZ3069121. Scientific and both Sylph names are Streptococcus pneumoniae. Available FASTA, assembly/Sylph/HQ PASS and prior HQ T are retained, but there is no BCOT-14 source chain. Only the BioSample/download-path suffix matches the taxid digits. The SeqKit sum, batch-600 OSF archive and mutable AWS URL remain context for that unrelated sample, not evidence for a target genome. Sequence quality flags do not establish organism identity.

## Completeness

Ignored-inclusive compressed searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The bounded taxid, BCOT-14 separator variants and label/slug patterns returned four lines: backbone, scope, native name and unrelated ATB row. Structured SOURCE.json scans found no matching manifest evidence in those roots.

No required representation was found missing. Optional strains, nomenclature, mappings, citations, datasets, discussions and causal graphs may remain absent. No supported genome association was found in this bounded review; zero exact-taxid Assembly hits do not prove global absence under other identifiers. Similar isolate names, study membership and common dates do not merge strains.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the asserted fields. Unavailable full literature limits optional enrichment, not the verified seeded identity.

## Recommended Edits

None required. Any future supported addition belongs in the configured upstream source, `scripts/extract_source_inventory.py`, or a tested `src/taxonmech/seed.py` change. Do not hand-edit generated YAML, invent a BacDive/deposit identifier, import the unrelated BioSample or refine NCBI lineage by inference.

## Follow-up Checks

Inspect primary text explicitly linking BCOT-14 or HQ616512 to any proposed literature claim. Later maintained-source changes require the seed dry-run, single-record canary, emitted-file inspection, open/strict validation and full reproduction/QC. No seed mutation was performed in this review.

## Additional Notes

iModulonDB was not applicable because no gene, locus, regulator, pathway or expression-module claim is asserted. No paid research, outbound contact, GitHub mutation, status promotion or history write occurred. Only this new review report was written for the target; Eukaryota was not revisited.
