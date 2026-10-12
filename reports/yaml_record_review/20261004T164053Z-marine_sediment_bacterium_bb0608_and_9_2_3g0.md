# YAML Record Review: marine sediment bacterium BB0608_AND_9.2_3G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_3g0.yaml`
- Started UTC: 2026-10-04T16:39:44Z
- Finished UTC: 2026-10-04T16:40:53Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, NCBITaxon:1033634. Its label is marine sediment bacterium BB0608_AND_9.2_3G0, rank SPECIES, domain BACTERIA, parent NCBITaxon:49928, and genetic code 11. Grounding is EXACT and lifecycle status SEEDED. It contains zero inventoried strains, one NCBITAXON NAME attestation, and one seed event dated 2026-09-13T17:54:04Z. No YAML, history or status was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_3g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_3g0.yaml`: one file scanned, zero ERROR rows.
- Ignored-inclusive exact identifier search across `data/taxa` resolved only this YAML. Ignored-inclusive filename search across the corpus and review directory found no prior report for its stem.
- Structured comparisons checked the complete backbone parent chain, seven source inventories, PATHS row, scope reason, attestation and seed-event text; all agreed. These bounded comparisons are not corpus reproduction.
- Not checked: `just qc`, `just verify-corpus`, corpus tests, global provenance/history/product gates, rendering and full-corpus term/reference checks. They were not run for this read-only single-record review; no invented focused replacement is claimed. The record has no curator-added graph nodes or external evidence citations requiring an additional product check.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221268` supplies the exact identity, rank, parent, code and 2026-09-13 snapshot. Its synonym fields and retirement field are empty. The complete root-first chain agrees: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), unclassified Bacteria (49928, NO_RANK). `data/catalog/ncbi_names-0005.jsonl.gz:30576` contains the scientific name. PATHS row 13721 fixes the filename, and `curation/seed_scope.tsv:321620` supplies the seed reason.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033634&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033634) were read and agree on identity, rank and ancestry; EFetch also confirms parent and genetic code. Datasets includes root, which EFetch omits from its displayed lineage. The Taxonomy Browser could not be retrieved through the web tool; successful structured authority responses supplied the check. Species rank is NCBI's placement, not a claim of valid nomenclatural publication or independent sequence-based identification.

## Evidence

The sole attestation correctly counts one NCBI NAME, not one genome or culture. The pinned source contains no direct children or matching BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. Exact structured scans of type-material, merged-ID and dropped inventories found no target entry.

Live exact-organism queries returned zero Assembly results (with phrase-not-found/no-items warnings) and one Nuccore result, UID 333384526. [JF750179.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750179.1) is a 447 bp partial 16S rRNA sequence. Inspected source qualifiers explicitly identify strain BB0608_AND_9.2_3G0, taxon:1033634 and genomic DNA, with coastal marine sediment, Australia: Gulf of Carpentaria, and Jun-2008 collection context. It is a marker sequence, not an assembly, deposit accession or independent justification for a finer classification.

Both sequence reference entries were inspected. Cornall, Beyer, Streten-Joyce, McGuinness, Parry and Gibb are credited with a bulk-sediment cryopreservation study marked Unpublished; Cornall's direct submission is dated 2011-04-01. Neither entry supplies a DOI or PMID. The full study was not obtained. No viability, phenotype, treatment-response or community-level claim is inferred from its title or transferred into this record.

## Completeness

An ignored-inclusive, compressed-file-aware search covered identifier, label/designation spelling variants and filename slug in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five matched rows were inspected: three target rows and the two unrelated cases below. Recursive structured SOURCE.json inspection found no additional match. This establishes bounded local-source absence, not worldwide absence of cultures or genomes.

- `data/catalog/gtdb_genomes-0014.jsonl.gz:6036` was read in full. RS_GCF_046984845.1 explicitly references GCA_046984845.1, Parabacteroides goldsteinii (taxon/species 328812), isolate 39-1_66, SAMN43246446, PRJNA224116 and JBKVGS000000000.1. It is a Scaffold assembly with 24 contigs and 10 scaffolds. Only `ncbi_scaffold_n50=1033634` matches the target number. The unrelated identity, not its metagenomic origin, excludes it.
- `data/catalog/allthebacteria.tsv.xz:64990` matches the numeric suffix of SAMEA1033634, not the NCBI taxon. With the native header checked, the row records ERR068309/ERR086018, ERZ3069050, scientific_name Streptococcus pneumoniae, both Sylph species fields unknown, available FASTA, assembly PASS, Sylph/HQ SYLPH_RESULTS_FAIL and prior-HQ F. Unknown classification is not a positive target identification. It lacks a target-linked culture/sample chain. Non-HQ/Sylph failure alone would not exclude an otherwise supported available FASTA; the missing identity chain is decisive here. SeqKit remains a sequence checksum rather than MD5, and the supplied AWS URL is mutable.

No supported strain/deposit/genome association was omitted in the inspected evidence. Empty synonyms, nomenclature, mappings, genomes, mechanisms and record-level literature evidence are appropriate for this seeded record. `strain_count: 0` counts inventoried BacDive strains and does not mean the organism was never cultivated. iModulonDB is not applicable to this taxonomy-only record with no gene, regulator, expression dataset or mechanism claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The unavailable manuscript and bounded genome search remain evidence limits, not established defects in the assertions actually present.

## Recommended Edits

None. Do not hand-edit the YAML or infer culture/genome links from identifier suffixes or assembly statistics. Future source-supported additions belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope changes belong in `curation/seed_scope.tsv:321620`.

## Follow-up Checks

For a future authorized source correction, verify the exact strain/deposit/sample chain, refresh the appropriate inventory, run the seed dry-run and `just seed-canary NCBITaxon:1033634 --force`, inspect the resulting YAML, rerun both focused validators, then run `just verify-corpus` and `just qc`. No canary or regeneration was run during this review.

## Additional Notes

Review followed the local single-record skill and checklist. Source identity, sample identity and genome identity were kept separate. No curation event, human-reviewed promotion, generated-page edit or GitHub mutation was made. Eukaryota coverage was not reopened.
