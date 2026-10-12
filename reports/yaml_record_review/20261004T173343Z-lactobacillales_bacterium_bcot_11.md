# YAML Record Review: Lactobacillales bacterium BCOT-11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lactobacillales_bacterium_bcot_11.yaml`
- Started UTC: 2026-10-04T17:32:23Z
- Finished UTC: 2026-10-04T17:33:43Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord`, NCBITaxon:1033680, Lactobacillales bacterium BCOT-11. It denotes a species-ranked BACTERIA placeholder, distinct from BCOT-1 and other related study isolates. It has `EXACT` grounding, `SEEDED` status, code 11, zero inventoried BacDive strains, one NCBITAXON NAME attestation and a seed event dated 2026-09-13T17:54:04Z. No generated field was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/lactobacillales_bacterium_bcot_11.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/lactobacillales_bacterium_bcot_11.yaml`: passed, one file and zero errors.
- Completed ignored-inclusive exact-identifier search across `data/taxa`: only this YAML. Ignored-inclusive exact-stem report search found no prior report.
- Structured comparison matched backbone, full lineage, children, seven source inventories, PATHS, scope, attestation and seed text. Separate exact type-material, merged-ID and dropped-row checks completed.
- Not run: corpus-wide `just qc`, `just verify-corpus`, tests, provenance, render and documentation gates. Global term/reference and history checks were skipped because there are no curator-added graph terms, literature references or separate history artifacts asserted here. Strict validation covered embedded history shape. Focused source comparisons do not prove corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221290` and the full native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30598` agree with the YAML. `data/taxa/PATHS.tsv:13743` pins the identifier/slug; `curation/seed_scope.tsv:321642` records the 2026-09-13 attested-rule inclusion.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033680&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033680) agree on canonical name, species rank, parent 263855 and genetic code 11. No alternate name was returned. The root-first chain is root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Bacillota 1239 (PHYLUM), Bacilli 91061 (CLASS), Lactobacillales 186826 (ORDER), unclassified Lactobacillales 263855 (NO_RANK). Datasets explicitly includes root 1. The browser was unavailable, so the successful structured authority responses supplied the check.

Species rank makes the placeholder eligible under repository scope; it does not assert formal nomenclatural publication. NCBI's unresolved placement below the order is preserved without an inferred genus or a classification copied from another isolate.

## Evidence

The attestation correctly counts one NCBI NAME from snapshot 2026-09-13. Exact scans found no BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits rows and no child taxa. Type-material, merged-ID and dropped inventories had no target row. Zero strains is therefore the supported BacDive inventory count, not evidence that BCOT-11 was never cultured.

Exact-taxid NCBI searches returned zero Assembly hits, with no-items/phrase warnings, and one Nuccore record. [HQ616509.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616509.1), UID 333408589, is a 682-base partial 16S sequence. Inspected GenBank XML source qualifiers identify genomic DNA, BCOT-11, taxon 1033680, Mexico, collection on 2010-02-01 by R. Flores-Magallon and PCR primers. Neither an isolation-source qualifier nor a culture-collection deposit is supplied. A partial marker is not a genome assembly.

Both sequence references were inspected. They name an unpublished Cotija-cheese study and a direct submission on 2010-11-10 by Flores-Magallon, Oliva-Hernandez and Narvaez-Zapata from Instituto Politecnico Nacional, Reynosa. The related [2011 article, DOI 10.1007/s10068-011-0137-z](https://link.springer.com/article/10.1007/s10068-011-0137-z), was inspected at its publisher earlier in this session; the accessible metadata/abstract do not name BCOT-11 or HQ616509. Full article and institutional thesis retrieval were unavailable in those checks. No strain-specific phenotype or finer classification is inferred from a shared topic or author list.

The ATB hit at `data/catalog/allthebacteria.tsv.xz:65041` is SAMEA1033680, with two runs ERR064664 and ERR085923, and analysis ERZ3069122. Its scientific and both Sylph labels are Streptococcus pneumoniae. Available FASTA, assembly/Sylph/HQ PASS statuses and prior HQ T are retained, but the numerical BioSample/download-path suffix is not a taxon association. No source chain links this sample to BCOT-11. The SeqKit sum, batch-600 OSF archive and mutable AWS URL remain source context; neither quality flags nor multiple runs supply target genome evidence.

## Completeness

Ignored-inclusive compressed searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Bounded taxid, BCOT-11 separator variants and label/slug forms produced four matching lines: backbone, scope, native name and unrelated ATB row. A structured SOURCE.json scan found no matching manifest evidence in those roots.

No missing required representation was found. Optional strains, nomenclature, mappings, evidence, discussions, datasets and causal graphs may remain absent. This bounded review found no supported genome relationship; exact-taxid Assembly absence does not rule out records filed under other identifiers. The marker, shared study and collection date cannot establish strain equivalence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the asserted seeded fields. Optional literature enrichment remains limited by unavailable full text.

## Recommended Edits

None required. Future source-backed additions belong in the configured upstream resource, `scripts/extract_source_inventory.py`, or a tested `src/taxonmech/seed.py` rule. Do not hand-edit generated YAML, invent a deposit/BacDive identifier, add the unrelated BioSample, or refine NCBI lineage by inference.

## Follow-up Checks

Require inspected primary text explicitly connecting BCOT-11 or HQ616509 to any proposed literature claim. Later source changes require a seed dry-run, single-record canary, emitted-file inspection, open/strict validation and full reproduction/QC. No seed mutation was performed here.

## Additional Notes

iModulonDB was not applicable: no gene, locus, regulator, pathway or expression-module claim is asserted. No paid research, contact, GitHub operation, status promotion or history write occurred. Only this new report was written for the target; Eukaryota was not revisited.
