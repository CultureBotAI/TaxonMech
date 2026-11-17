# YAML Record Review: Lactobacillales bacterium BCOT-12

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lactobacillales_bacterium_bcot_12.yaml`
- Started UTC: 2026-10-04T17:34:32Z
- Finished UTC: 2026-10-04T17:35:36Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord`, NCBITaxon:1033681, Lactobacillales bacterium BCOT-12. It is a species-ranked placeholder in BACTERIA with `EXACT` grounding, `SEEDED` status, code 11, zero inventoried BacDive strains, one NCBITAXON NAME attestation and a seed event dated 2026-09-13T17:54:04Z. It is not another BCOT isolate or a genome. No generated field was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/lactobacillales_bacterium_bcot_12.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/lactobacillales_bacterium_bcot_12.yaml`: passed, one file and zero errors.
- Completed ignored-inclusive exact-identifier search across `data/taxa`: only the target YAML. Ignored-inclusive exact-stem report search found no prior report.
- Structured checks matched backbone, complete lineage, child scan, seven source inventories, PATHS, scope, attestation and seed text. Exact type-material, merged-ID and dropped-row checks completed separately.
- Not run: full-corpus `just qc`, `just verify-corpus`, tests, provenance, render and documentation gates. Global term/reference and history checks were skipped; this record asserts no curator-added graph terms, literature references or separate history artifacts. Strict validation covered embedded history shape. Focused comparisons do not substitute for full corpus reproduction.

## Identity and Grounding

The source row at `data/raw/ncbitaxon_taxa.tsv:221291` and full native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30599` agree with the record. `data/taxa/PATHS.tsv:13744` pins the identifier/slug, and `curation/seed_scope.tsv:321643` records its 2026-09-13 attested-rule inclusion.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033681&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033681) confirm canonical name, species rank, parent 263855 and code 11. No alternate name was returned. The root-first chain matches root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Bacillota 1239 (PHYLUM), Bacilli 91061 (CLASS), Lactobacillales 186826 (ORDER), and unclassified Lactobacillales 263855 (NO_RANK). Datasets explicitly includes root 1. The browser was unavailable; structured authority responses supplied verification.

The placeholder's species rank makes it eligible for this corpus but does not imply formal nomenclatural publication or a resolved genus. The NCBI lineage is carried without reclassification from related study isolates.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME from snapshot 2026-09-13. Exact inventory scans found no direct BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits rows and no child taxa. Type-material, merged-ID and dropped inventories had no target rows. `strain_count: 0` agrees with inventoried BacDive coverage; it is not a claim that BCOT-12 was never cultured.

The exact-taxid Assembly query returned zero hits with no-items/phrase warnings; Nuccore returned one record. [HQ616510.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616510.1), UID 333408590, is a 702-base partial 16S sequence. The inspected GenBank XML explicitly names genomic DNA, strain BCOT-12, taxon 1033681, Mexico, collection on 2010-02-01 by R. Flores-Magallon and PCR primers. Neither an isolation-source qualifier nor a culture-collection deposit is supplied. Marker evidence does not establish a genome link.

Both sequence references were read: an unpublished Cotija-cheese study and direct submission on 2010-11-10 by Flores-Magallon, Oliva-Hernandez and Narvaez-Zapata from Instituto Politecnico Nacional, Reynosa. The related [2011 article, DOI 10.1007/s10068-011-0137-z](https://link.springer.com/article/10.1007/s10068-011-0137-z), was inspected at its publisher earlier in this session. Its accessible metadata/abstract do not name BCOT-12 or HQ616510. Full paper and institutional thesis retrieval were unavailable in those checks. No phenotype, maturation stage or finer identity is inferred from the common study context or indexed thesis snippets.

The unrelated ATB row at `data/catalog/allthebacteria.tsv.xz:65042` is SAMEA1033681, ERR064816, ERZ3069119. Scientific and both Sylph labels are Streptococcus pneumoniae; available FASTA, assembly/Sylph/HQ PASS and prior HQ T are retained. Those flags do not supply a BCOT-12 association. Only a BioSample/download-path suffix matches the taxid digits, and no source chain connects the sample to this isolate. Its SeqKit sum, batch-600 OSF archive and mutable AWS URL remain context for that source sample, not missing target genome evidence.

## Completeness

Ignored-inclusive compressed searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxid, BCOT-12 separator variants and label/slug forms. Four lines matched: backbone, scope, native name and unrelated ATB row. Structured SOURCE.json searches found no matching manifest evidence in those roots.

No missing required representation was identified. Optional strains, nomenclature, mappings, citations, datasets, discussions and causal graphs may remain absent. No supported genome relationship was found in this bounded review; zero exact-taxid Assembly hits do not prove global absence under other identifiers. Common sample dates and similar study labels cannot establish strain equivalence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the asserted fields. Unavailable full literature limits optional enrichment, not the verified seeded identity.

## Recommended Edits

None required. Future supported additions belong in the configured upstream source, `scripts/extract_source_inventory.py`, or a tested `src/taxonmech/seed.py` change. Do not hand-edit generated YAML, invent a deposit/BacDive identity, add the unrelated BioSample or refine NCBI lineage by inference.

## Follow-up Checks

Before adding literature, inspect primary text explicitly connecting BCOT-12 or HQ616510 to the claim. Later source changes require a seed dry-run, single-record canary, emitted-YAML inspection, open/strict validation and full reproduction/QC. No seed mutation was performed during this review.

## Additional Notes

iModulonDB was not applicable: no gene, locus, regulator, pathway or expression-module claim is asserted. No paid research, contact, GitHub mutation, lifecycle promotion or history write occurred. Only this new report was written for the target; Eukaryota was not revisited.
