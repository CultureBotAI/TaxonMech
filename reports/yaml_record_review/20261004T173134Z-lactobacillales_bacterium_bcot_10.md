# YAML Record Review: Lactobacillales bacterium BCOT-10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lactobacillales_bacterium_bcot_10.yaml`
- Started UTC: 2026-10-04T17:30:36Z
- Finished UTC: 2026-10-04T17:31:34Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for NCBITaxon:1033679, Lactobacillales bacterium BCOT-10. It is a species-ranked BACTERIA placeholder, not BCOT-1 or another isolate sharing the prefix. The record has `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried BacDive strains, one NCBITAXON NAME attestation and its deterministic 2026-09-13T17:54:04Z seed event. No generated field was edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/lactobacillales_bacterium_bcot_10.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/lactobacillales_bacterium_bcot_10.yaml`: passed, one file scanned and zero errors.
- Completed ignored-inclusive exact-identifier search across `data/taxa`: only this YAML. Ignored-inclusive report-filename search found no existing report for this stem.
- Structured checks matched the target backbone, full ancestor chain, child scan, seven source inventories, PATHS, scope, attestation and seed text. Exact type-material, merged-ID and dropped-row scans completed separately.
- Not run: full-corpus `just qc`, `just verify-corpus`, tests, provenance, documentation and render gates. Global term/reference and history validation were skipped; no curator-added graph terms, literature references or separate history artifacts are asserted. Strict validation covered embedded history shape. Focused source comparisons are not corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221289` and the full native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30597` match the record. `data/taxa/PATHS.tsv:13742` pins the slug and `curation/seed_scope.tsv:321641` records the 2026-09-13 attested-rule inclusion.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033679&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033679) agree on canonical name, species rank, parent 263855 and genetic code 11. No alternate name was returned. The root-first lineage matches root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Bacillota 1239 (PHYLUM), Bacilli 91061 (CLASS), Lactobacillales 186826 (ORDER), and unclassified Lactobacillales 263855 (NO_RANK). Datasets explicitly includes root 1. The browser was unavailable; the structured authority responses supplied verification.

The species-ranked placeholder is eligible for this repository but does not assert valid nomenclatural publication or a resolved genus. Its lineage is carried from NCBI rather than inferred from study membership.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME in snapshot 2026-09-13. Exact scans found no BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits rows, and the target has no child taxa. Type-material, merged-ID and dropped inventories had no target row. `strain_count: 0` therefore agrees with the BacDive inventory; it does not deny that BCOT-10 was cultured.

Exact-taxid searches returned zero Assembly hits with no-items/phrase warnings and one Nuccore record. [HQ616508.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616508.1), UID 333408588, is a 475-base partial 16S sequence. The inspected GenBank XML explicitly identifies genomic DNA, strain BCOT-10, taxon 1033679, Mexico, collection on 2010-02-01 by R. Flores-Magallon and PCR primers. It supplies neither an isolation-source qualifier nor a culture-collection deposit. The web sequence page displayed a browser check, but the structured record was retrieved successfully. Marker sequence evidence is not a genome assertion.

Both sequence references were inspected: an unpublished Cotija-cheese study and direct submission on 2010-11-10 by Flores-Magallon, Oliva-Hernandez and Narvaez-Zapata, Instituto Politecnico Nacional, Reynosa. The related [2011 article, DOI 10.1007/s10068-011-0137-z](https://link.springer.com/article/10.1007/s10068-011-0137-z), was inspected at its publisher earlier in this session. Its accessible metadata/abstract do not identify BCOT-10 or HQ616508. The full paper and institutional thesis were unavailable in those checks, so a published isolate-specific phenotype or finer classification remains unverified. Study context is not transferred from another BCOT record.

The unrelated ATB hit at `data/catalog/allthebacteria.tsv.xz:65040` is SAMEA1033679, ERR064705, ERZ3069124. Scientific and both Sylph labels are Streptococcus pneumoniae. The row has an available FASTA, assembly/Sylph/HQ PASS statuses and prior HQ T, but those flags do not establish a target identity link. The taxid digits occur only as a BioSample/download-path suffix. There is no BCOT-10 strain-to-sample chain. Its SeqKit sum, batch-600 OSF archive and mutable AWS URL remain context for that sample, not missing genome evidence for this record.

## Completeness

Ignored-inclusive compressed searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded taxid, BCOT-10 separator variants and label/slug forms. Four lines matched: backbone, scope, native name and the unrelated ATB row. Structured SOURCE.json scans found no matching manifest evidence in those roots.

No required representation is missing from the inspected inventories. Optional strains, nomenclature, mappings, evidence, datasets, discussions and causal graphs may remain absent. The bounded Assembly search does not prove global genome absence under other identifiers; the evidence reviewed here supports a marker only. A related study, collection date or numeric suffix cannot establish strain equivalence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the currently asserted fields. Literature access limits affect optional enrichment, not the verified seeded identity.

## Recommended Edits

None required. Future supported additions belong in the configured upstream source, `scripts/extract_source_inventory.py`, or a tested `src/taxonmech/seed.py` rule. Do not hand-edit generated YAML, invent a BacDive or deposit identifier, import the unrelated BioSample, or refine NCBI lineage by inference.

## Follow-up Checks

Inspect primary text explicitly connecting BCOT-10 or HQ616508 to any proposed literature claim. Later source changes require the seed dry-run, single-record canary, emitted-file inspection, repeated open/strict validation and full reproduction/QC. No seed mutation was run in this review.

## Additional Notes

iModulonDB was not applicable: no gene, locus, regulator, pathway or expression-module claim is asserted. No paid access, author contact, GitHub mutation, lifecycle promotion or history write occurred. Only this new report was written for the target. Eukaryota was not revisited.
