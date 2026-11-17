# YAML Record Review: marine sediment bacterium BB0608_AND_9.2_5G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_5g0.yaml`
- Started UTC: 2026-10-04T16:47:22Z
- Finished UTC: 2026-10-04T16:48:31Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for NCBITaxon:1033638, marine sediment bacterium BB0608_AND_9.2_5G0. It carries rank SPECIES, domain BACTERIA, parent NCBITaxon:49928, genetic code 11, EXACT grounding and SEEDED status. Zero inventoried strains, one NCBITAXON NAME attestation and the 2026-09-13T17:54:04Z seed event remain unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_5g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_5g0.yaml`: one file, zero ERROR rows.
- Ignored-inclusive exact-ID search across `data/taxa` resolved one YAML; ignored-inclusive report filename search found no previous report for this stem.
- Complete structured source comparisons passed for backbone ancestry, seven source inventories, PATHS, scope reason, the NCBI attestation and seed text. Exact type-material, merged-ID and dropped scans were completed.
- Not checked: full-corpus `just qc`, `just verify-corpus`, tests, provenance, global term/reference and history/product gates, or rendering. Bounded comparisons are not corpus reproduction. There are no curator-added graph nodes or external evidence references requiring an additional product check here.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221272` supplies the exact identity, rank, parent, code and 2026-09-13 snapshot; synonym and retirement fields are empty. The full lineage agrees: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), and unclassified Bacteria 49928 (NO_RANK). The native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:30580`. PATHS row 13725 and `curation/seed_scope.tsv:321624` match the slug and seed reason.

Live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033638&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033638) were inspected and agree on identity, rank and ancestry. EFetch confirms parent and code; Datasets includes root, omitted from EFetch's displayed lineage. The Taxonomy Browser was inaccessible through the web tool, so structured authority responses supplied verification. NCBI species rank does not establish valid nomenclatural publication or independent resolution of this organism's finer placement.

## Evidence

The sole attestation correctly counts one NCBI NAME, not a genome or culture. Complete scans found no direct children and no target match in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. Type-material, merged-ID and dropped inventories also contained no exact target row.

Live exact-organism queries returned zero Assembly results (with phrase-not-found/no-items warnings) and one Nuccore result, UID 333384530. [JF750183.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750183.1) is a 533 bp partial 16S rRNA sequence. Its inspected source qualifiers explicitly identify strain BB0608_AND_9.2_5G0, taxon:1033638 and genomic DNA, with coastal marine sediment, Australia: Gulf of Carpentaria and Jun-2008 collection context. This marker is neither an assembly nor a culture-collection accession, and its submitted name does not independently validate a finer classification.

Both reference entries were read. Cornall, Beyer, Streten-Joyce, McGuinness, Parry and Gibb's bulk-sediment cryopreservation study is marked Unpublished; Cornall's direct submission is dated 2011-04-01. Neither entry supplies a DOI or PMID. The full manuscript was not obtained. Its title is not evidence for a taxon-wide phenotype, viability or treatment response.

## Completeness

Ignored-inclusive compressed-file search covered taxon-number boundaries, label/designation variants and filename slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All four matched rows were inspected: target backbone, scope, native scientific name, and one unrelated ATB row. Recursive structured SOURCE.json inspection found no additional match. This is bounded source coverage, not proof that no culture or genome exists anywhere.

`data/catalog/allthebacteria.tsv.xz:64994` records SAMEA1033638, ERR064814 and ERZ3069061. The native header was checked in this review session. Scientific name and both Sylph fields are Streptococcus pneumoniae, FASTA is available, assembly/Sylph/HQ filters are PASS and prior-HQ is T. The numeric match is a BioSample suffix and its download URL, not the target NCBI identity. No explicit target strain/deposit/sample chain supports a link. Non-HQ status alone would not exclude an otherwise supported available FASTA; quality is not the exclusion reason. Shared samples do not establish assembly equivalence, SeqKit is not MD5 and the AWS URL is mutable.

No supported omitted strain/deposit/genome link was found. Empty optional synonyms, nomenclature, mappings, genomes, record-level literature evidence and mechanisms are appropriate. Zero BacDive strains means zero inventoried strain records, not never cultivated. iModulonDB is not applicable because this taxonomic record contains no gene, regulator, expression dataset or mechanism assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The unavailable manuscript and bounded genome query are evidence limits, not established defects in the actual seeded assertions.

## Recommended Edits

None. Preserve the generated YAML and do not join on numeric accession suffixes. Future evidence-backed changes belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is `curation/seed_scope.tsv:321624`.

## Follow-up Checks

For a future authorized correction, verify exact strain/deposit/sample evidence, refresh the owning inventory, run the seed dry-run and `just seed-canary NCBITaxon:1033638 --force`, inspect the resulting YAML, rerun both focused validators, then `just verify-corpus` and `just qc`. No canary or regeneration was performed here.

## Additional Notes

Review followed the local single-record skill and checklist. No curation/history event, human-reviewed promotion, generated-page change or GitHub mutation was made. Eukaryota coverage was not reopened.
