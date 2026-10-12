# YAML Record Review: Lactobacillales bacterium BCOT-2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lactobacillales_bacterium_bcot_2.yaml`
- Started UTC: 2026-10-04T17:39:07Z
- Finished UTC: 2026-10-04T17:40:16Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, NCBITaxon:1033683, Lactobacillales bacterium BCOT-2. This is a species-ranked BACTERIA placeholder with `EXACT` grounding, `SEEDED` status, code 11, zero inventoried BacDive strains, one NCBITAXON NAME attestation and a seed event dated 2026-09-13T17:54:04Z. It is distinct from the other BCOT isolates and from genome records. No generated field was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/lactobacillales_bacterium_bcot_2.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/lactobacillales_bacterium_bcot_2.yaml`: passed, one file and zero errors.
- Completed ignored-inclusive exact-identifier search across `data/taxa`: only this YAML. Ignored-inclusive exact-stem report search found no prior report.
- Structured comparisons matched backbone, complete lineage, children, seven source inventories, PATHS, scope, attestation and seed text. Exact type-material, merged-ID and dropped-row checks completed separately.
- Not run: corpus-wide `just qc`, `just verify-corpus`, tests, provenance, render and documentation checks. Global term/reference and history gates were skipped; no curator-added graph terms, literature references or separate history artifacts are asserted here. Strict validation covered embedded history shape. Focused source comparisons do not prove full corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221293` and the full native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30601` agree with the YAML. `data/taxa/PATHS.tsv:13746` pins the identifier/slug; `curation/seed_scope.tsv:321645` records the 2026-09-13 attested-rule inclusion.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033683&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033683) confirm canonical name, species rank, parent 263855 and code 11. No alternate name was returned. The complete root-first chain matches root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Bacillota 1239 (PHYLUM), Bacilli 91061 (CLASS), Lactobacillales 186826 (ORDER), unclassified Lactobacillales 263855 (NO_RANK). Datasets explicitly includes root 1. The browser was unavailable; successful structured authority responses supplied the check.

Species rank establishes repository eligibility, not formal nomenclatural publication or a resolved genus. The NCBI lineage is preserved without reclassification from related isolates or study-level descriptions.

## Evidence

The NCBITAXON attestation correctly counts one NAME from snapshot 2026-09-13. Exact scans found no direct BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits rows and no child taxa. Type-material, merged-ID and dropped inventories had no target row. Zero strains therefore means zero inventoried BacDive entries, not that BCOT-2 was never cultured.

Exact-taxid NCBI searches returned zero Assembly hits with no-items/phrase warnings and one Nuccore record. [HQ616500.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616500.1), UID 333408580, is a 751-base partial 16S sequence. Its inspected GenBank XML explicitly names genomic DNA, strain BCOT-2, taxon 1033683, Mexico, collection on 2010-02-01 by R. Flores-Magallon and PCR primers. Neither a culture-collection deposit nor an isolation-source qualifier is supplied. The web sequence page displayed a browser check, but structured retrieval succeeded. This is marker evidence, not an assembly.

Both sequence references were inspected: an unpublished Cotija-cheese study and direct submission on 2010-11-10 by Flores-Magallon, Oliva-Hernandez and Narvaez-Zapata from Instituto Politecnico Nacional, Reynosa. The related [2011 article, DOI 10.1007/s10068-011-0137-z](https://link.springer.com/article/10.1007/s10068-011-0137-z), was inspected at its publisher earlier in this session. The accessible metadata and abstract do not name BCOT-2 or HQ616500. Full paper and institutional thesis retrieval were unavailable in those checks. No isolate-level phenotype, maturation stage or finer classification is inferred from those leads.

The complete GenBank object at `data/catalog/ncbi_genbank-0052.jsonl.gz:47735` is GCA_057283515.1, Caviibacter sp. taxon 2024962, isolate HROM_Genome_2910, SAMN47000912, PRJNA1206836 and WGS DBHIYF000000000.1. This metagenomic scaffold assembly has 52 contigs, 33 scaffolds and total length 1,034,005; only its ungapped length, 1,033,683, matches the target's taxid digits. No organism, strain or deposit field links it to BCOT-2. Its source-reported RefSeq exclusion is not the basis for rejection; the identities differ.

The ATB row at `data/catalog/allthebacteria.tsv.xz:65044` is SAMEA1033683, ERR064788, ERZ3069127. Its scientific and both Sylph labels are Streptococcus pneumoniae. Available FASTA, assembly/Sylph/HQ PASS and prior HQ T are retained, but only a BioSample/download-path suffix matches the taxid digits. No source chain links this sample to BCOT-2. The SeqKit sum, batch-600 OSF archive and mutable AWS URL remain source context, not target genome evidence.

## Completeness

Ignored-inclusive compressed searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The bounded taxid, BCOT-2 separator variants and label/slug forms returned five lines: backbone, scope, native name and two unrelated numeric matches. Structured SOURCE.json searches found no matching manifest evidence in those roots.

No missing required representation was found. Optional strains, nomenclature, mappings, evidence, datasets, discussions and causal graphs may remain absent. No supported genome relationship was found in this bounded review; zero exact-taxid Assembly hits do not prove global absence under other identifiers. Shared study metadata and similar numerical identifiers cannot establish strain equivalence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the asserted fields. Full-text access limits affect optional enrichment, not the verified source identity.

## Recommended Edits

None required. Future supported additions belong in the configured upstream resource, `scripts/extract_source_inventory.py`, or a tested `src/taxonmech/seed.py` rule. Do not hand-edit generated YAML, invent a deposit/BacDive identity, add either unrelated genome source, or refine NCBI lineage by inference.

## Follow-up Checks

Inspect primary text explicitly linking BCOT-2 or HQ616500 to a proposed literature claim. Later maintained-source changes require the seed dry-run, single-record canary, emitted-file inspection, open/strict validation and full reproduction/QC. No seed mutation was performed in this review.

## Additional Notes

iModulonDB was not applicable because no gene, locus, regulator, pathway or expression-module claim is asserted. No paid research, contact, GitHub mutation, status promotion or history write occurred. Tracked status was clean at the start, with only reports untracked. Eukaryota was not revisited.
