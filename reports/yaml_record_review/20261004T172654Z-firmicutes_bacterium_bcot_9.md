# YAML Record Review: Firmicutes bacterium BCOT-9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/firmicutes_bacterium_bcot_9.yaml`
- Started UTC: 2026-10-04T17:25:38Z
- Finished UTC: 2026-10-04T17:26:54Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for NCBITaxon:1033677, Firmicutes bacterium BCOT-9. It denotes a species-ranked placeholder in BACTERIA with parent 84086, code 11, `EXACT` grounding, `SEEDED` status, zero inventoried BacDive strains, one NCBITAXON NAME attestation and the seed event dated 2026-09-13T17:54:04Z. It is distinct from the other BCOT isolates. No generated YAML field was edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/firmicutes_bacterium_bcot_9.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/firmicutes_bacterium_bcot_9.yaml`: passed, one file and zero errors.
- Completed ignored-inclusive exact-identifier search across `data/taxa`: only the target YAML. Ignored-inclusive exact-stem report search found no prior report.
- Structured comparison matched the target backbone, complete ancestor chain, children, seven source inventories, PATHS, scope, attestation and embedded seed text. Exact type-material, merged-ID and dropped-row checks completed separately.
- Not run: corpus-wide `just qc`, `just verify-corpus`, tests, provenance, render and documentation checks. Global term/reference and history gates were skipped; this target asserts no curator-added graph terms, literature references or separate history artifacts. Strict validation covered embedded history shape. Focused comparisons do not prove full corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221287` and the complete native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30595` agree with the generated identity. `data/taxa/PATHS.tsv:13740` pins the slug, while `curation/seed_scope.tsv:321639` supplies the 2026-09-13 attested-rule inclusion.

Live [taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033677&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033677) verify the identifier, canonical name, species rank, parent 84086 and genetic code 11. The browser request was unavailable; structured authority responses were inspected instead. No live alternate name was returned. The root-first chain matches exactly: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Bacillota 1239 (PHYLUM), unclassified Bacillota 84086 (NO_RANK). Datasets explicitly supplies root 1.

The older Firmicutes wording is retained in NCBI's canonical name even though the lineage uses Bacillota. This is faithful source carry-through, not a reason to rename the YAML or infer a genus. Species rank does not imply formal nomenclatural publication.

## Evidence

The sole attestation correctly reports one NCBI NAME from snapshot 2026-09-13. No exact rows were found in BacDive, LPSN, GTDB mappings, GOLD, MediaDive, Madin or BactoTraits inventories. The child scan was empty, and type-material, merged-ID and dropped inventories had no target row. Thus zero BacDive strains is the supported source count, not a statement that BCOT-9 was never cultured.

Exact-taxid NCBI queries returned zero Assembly hits, with no-items/phrase warnings, and one Nuccore hit. [HQ616507.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616507.1), UID 333408587, is a 576-base partial 16S sequence. Its inspected GenBank XML identifies genomic DNA, strain BCOT-9, taxon 1033677, Mexico, collection on 2010-02-01 by R. Flores-Magallon, and PCR primers. No isolation-source qualifier or culture-collection deposit was supplied. This is a marker record, not a genome assertion.

The two sequence references were inspected: an unpublished Cotija-cheese study and direct submission on 2010-11-10 by Flores-Magallon, Oliva-Hernandez and Narvaez-Zapata, Instituto Politecnico Nacional, Reynosa. The related [2011 article, DOI 10.1007/s10068-011-0137-z](https://link.springer.com/article/10.1007/s10068-011-0137-z), was inspected at its publisher during the BCOT-15 review earlier in this session. Its metadata and abstract match the authors and broad topic but do not identify BCOT-9 or HQ616507. The full body was not available. The unretrieved institutional thesis and indexed snippets are leads only; no isolate-specific phenotype, maturation stage or alternative classification is asserted from them.

The complete object at `data/catalog/ncbi_genbank-0051.jsonl.gz:33549` is GCA_055919465.1, Aquificota bacterium taxon 2202151, isolate DRTY-2_201912_bins_18. It supplies BioSample SAMN40878115, BioProject PRJNA544494, WGS JBCTOA000000000.1 and 130 contigs/scaffolds. The search matched its 1,033,677-base total and ungapped genome lengths, not its taxon field. This metagenomic contig assembly is unrelated to BCOT-9; no strain or genome link follows from the numerical match.

The ATB row at `data/catalog/allthebacteria.tsv.xz:65038` is SAMEA1033677, ERR068214, ERZ3069112, scientifically labelled Streptococcus pneumoniae with both Sylph labels agreeing. Available FASTA and assembly/Sylph/HQ PASS statuses, with prior HQ T, are preserved. Only the BioSample suffix and download path match the taxid digits. No source chain connects that sample to BCOT-9, so this is not a missing genome association. The SeqKit sum is not MD5; the batch-600 OSF archive and mutable AWS URL remain source context.

## Completeness

Ignored-inclusive compressed searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The query used the bounded taxid, BCOT-9 separator variants and label/slug forms. Five lines matched: backbone, scope, native name, unrelated GenBank assembly and unrelated ATB sample. Structured SOURCE.json scans found no matching manifest evidence within those source roots.

No missing required representation was identified. Optional strains, nomenclature, mappings, citations, datasets, discussions and causal graphs may remain absent. No supported genome relationship was found in this bounded review; exact-taxid Assembly absence does not rule out records under different identifiers. Study membership and similar isolate names cannot transfer evidence between BCOT records.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The literature-access limit affects optional enrichment, not verification of the NCBI-only seeded fields.

## Recommended Edits

None required. A future supported source addition belongs in the configured upstream resource, `scripts/extract_source_inventory.py`, or a tested `src/taxonmech/seed.py` rule. Do not hand-edit the generated record, infer a culture deposit, promote a marker to a genome, or use either numeric collision as a strain association. NCBI lineage corrections belong upstream.

## Follow-up Checks

Inspect primary text that explicitly links BCOT-9 or HQ616507 to any proposed literature claim. Future maintained-source changes require the seed dry-run and single-record canary, inspection of emitted YAML, open/strict validation, and full reproduction/QC. None of those mutation steps was performed in this review.

## Additional Notes

iModulonDB was not applicable because no gene, locus, regulator, pathway or expression-module claim is asserted. No paid access, contact, GitHub mutation, lifecycle promotion or history write occurred. Only this new report was written for the target. Eukaryota was not revisited.
