# YAML Record Review: Agarivorans sp. HQWB1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/agarivorans_sp_hqwb1.yaml`
- Started UTC: 2026-10-04T16:54:02Z
- Finished UTC: 2026-10-04T16:55:12Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord, NCBITaxon:1033650, Agarivorans sp. HQWB1. Rank SPECIES, domain BACTERIA, parent NCBITaxon:2636026, genetic code 11, EXACT grounding and SEEDED status are retained. It has zero inventoried strains, one NCBITAXON NAME attestation and a single 2026-09-13T17:54:04Z seed event. No YAML or curation status was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/agarivorans_sp_hqwb1.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/agarivorans_sp_hqwb1.yaml`: one file, zero ERROR rows.
- Ignored-inclusive exact identifier search in `data/taxa` resolved only this YAML. Ignored-inclusive report filename search found no prior review for its stem.
- Structured comparisons passed for the full backbone ancestry, seven source inventories, PATHS, scope, NCBI attestation and seed text. Exact type-material, merged-ID and dropped scans were completed.
- Not checked: full-corpus `just qc`, `just verify-corpus`, tests, provenance, global term/reference and history/product gates, or rendering. Bounded source comparisons are not corpus reproduction. No curator-added graph nodes or external record-level evidence references require an additional product check.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221275` supplies the exact label, rank, parent, code and 2026-09-13 snapshot; synonym and retirement fields are empty. The ten root-first ancestors were all checked: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Pseudomonadati 3379134 (KINGDOM), Pseudomonadota 1224 (PHYLUM), Gammaproteobacteria 1236 (CLASS), Alteromonadales 135622 (ORDER), Alteromonadaceae 72275 (FAMILY), Agarivorans 261825 (GENUS), unclassified Agarivorans 2636026 (NO_RANK). `data/catalog/ncbi_names-0005.jsonl.gz:30583` carries the scientific name. PATHS row 13728 and `curation/seed_scope.tsv:321627` match the slug and reason.

Live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033650&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033650) were read and agree on identity, rank and ancestry. EFetch confirms parent and genetic code; Datasets includes root, omitted from EFetch's displayed lineage. The Taxonomy Browser was inaccessible through the web tool, so successful structured responses supplied the authority check. NCBI's species rank for an unnamed isolate does not establish a validly published binomial, type-strain status or a finer species identification.

## Evidence

The sole attestation correctly counts one NCBI NAME. Complete local scans found no direct children or exact target match in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. No exact type-material, merged-ID or dropped row was found.

Live exact-organism queries returned zero Assembly results, including phrase-not-found/no-items warnings, and one Nuccore result, UID 333353478. [JF721993.1](https://www.ncbi.nlm.nih.gov/nuccore/JF721993.1) is a 370 bp partial 16S rRNA sequence. Source qualifiers explicitly name HQWB1, taxon:1033650 and genomic DNA. They report host Styela clava, China, 37.5333 N 122.05667 E, collection on 18-Sep-2009 by Tingting Miao, and the submitted 16S primer pair. These are isolate-specific submission metadata, not proof of host specificity, symbiosis, pathogenicity or a taxon-wide habitat. No agar-degradation phenotype is inferred from the genus name.

Both sequence references were inspected: Miao, Du and Chen's study of bacterial isolation and phylogenetic analysis from Styela clava is marked Unpublished, and their direct submission is dated 2011-03-22 at Shandong University at Weihai. Neither reference supplies a DOI or PMID. The full study was not obtained. The marker and its submitted identification do not independently prove a species assignment, supply a genome assembly or establish an eligible culture-collection deposit.

## Completeness

Ignored-inclusive compressed-file search covered taxon-number boundaries, HQWB1/HQWB-1/HQWB_1/HQWB 1 variants, label and slug in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All four matched rows were inspected: target backbone, scope, native name and one unrelated ATB row. Recursive structured SOURCE.json search found no further match. This is bounded local-source and live-query coverage, not a worldwide absence claim.

`data/catalog/allthebacteria.tsv.xz:65007` records SAMEA1033650, ERR064644/ERR085903 and ERZ3069073. Using the previously inspected native header, scientific name and both Sylph fields are Streptococcus pneumoniae, FASTA is available, assembly/Sylph/HQ filters are PASS and prior-HQ is T. Only the BioSample suffix and its download URL match the target number. There is no target-linked strain/deposit/sample chain. Non-HQ status alone would not exclude a supported available FASTA; the unrelated identity is decisive here. Shared sample alone would not establish assembly equivalence; SeqKit is not MD5 and AWS URLs are mutable.

No supported omitted strain, deposit or genome association was found. Optional nomenclature, mappings, synonyms, genomes, literature evidence and mechanisms are appropriately empty. `strain_count: 0` counts BacDive inventory entries, not whether HQWB1 was ever isolated or cultivated. iModulonDB is not applicable because the record has no gene, regulator, expression dataset or mechanism assertion. The submission's eukaryotic host context does not reopen any eukaryotic record review.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The short marker and unavailable full study limit further interpretation, not the exact seeded taxonomic assertions.

## Recommended Edits

None. Preserve generated YAML; do not invent a deposit, genome, phenotype or host-specific mechanism. Future source-supported additions belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is `curation/seed_scope.tsv:321627`.

## Follow-up Checks

For a future authorized correction, obtain explicit identity and strain/deposit/sample evidence, refresh the owning inventory, run the seed dry-run and `just seed-canary NCBITaxon:1033650 --force`, inspect the output, rerun both focused validators and then `just verify-corpus` / `just qc`. No canary or regeneration was performed here.

## Additional Notes

The local single-record review skill and checklist governed this report. No curation/history event, human-reviewed promotion, generated-page edit or GitHub mutation was made. Eukaryota coverage was left intact.
