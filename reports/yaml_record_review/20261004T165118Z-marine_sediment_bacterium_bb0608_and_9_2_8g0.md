# YAML Record Review: marine sediment bacterium BB0608_AND_9.2_8G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_8g0.yaml`
- Started UTC: 2026-10-04T16:50:18Z
- Finished UTC: 2026-10-04T16:51:18Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for NCBITaxon:1033639, marine sediment bacterium BB0608_AND_9.2_8G0. It is SPECIES / BACTERIA, parent NCBITaxon:49928, genetic code 11, EXACT grounding and SEEDED status. Zero inventoried strains, one NCBITAXON NAME attestation and the 2026-09-13T17:54:04Z seed event remain unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_8g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_8g0.yaml`: one file, zero ERROR rows.
- Ignored-inclusive exact-ID search across `data/taxa` found only this YAML; ignored-inclusive filename search in the review directory found no earlier report for this stem.
- Structured comparisons passed for the complete backbone lineage, seven source inventories, PATHS, scope, seed-event text and NCBI attestation. Exact type-material, merged-ID and dropped scans were completed.
- Not checked: full-corpus `just qc`, `just verify-corpus`, tests, provenance, global term/reference and history/product gates, or rendering. Bounded source comparisons do not prove corpus reproduction. This record has no curator-added graph nodes or external evidence references requiring a product check.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221273` agrees on identity, rank, parent, code and snapshot 2026-09-13, with empty synonym and retirement fields. The root-first chain agrees in full: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), unclassified Bacteria 49928 (NO_RANK). The scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:30581`. PATHS row 13726 and `curation/seed_scope.tsv:321625` fix the slug and seed reason.

Live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033639&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033639) were read and confirm the identity, rank and ancestry. EFetch also confirms parent and code; Datasets includes root, which EFetch omits from its displayed lineage. The Taxonomy Browser was inaccessible through the web tool, so successful structured authority responses supplied the check. NCBI species rank is not proof of valid nomenclatural publication or independent sequence-based classification.

## Evidence

The sole attestation correctly counts one NAME. Complete scans found no direct children or matching BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory rows. Type-material, merged-ID and dropped inventories had no exact target entry.

Live exact-organism queries returned zero Assembly results, with phrase-not-found/no-items warnings, and one Nuccore result, UID 333384531. [JF750184.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750184.1) is a 389 bp partial 16S rRNA sequence. Inspected source qualifiers explicitly name strain BB0608_AND_9.2_8G0, taxon:1033639 and genomic DNA, with coastal marine sediment, Australia: Gulf of Carpentaria, and Jun-2008 collection context. This marker is not an assembly, culture deposit or independent resolution of the unclassified placement.

Both reference entries were read. Cornall, Beyer, Streten-Joyce, McGuinness, Parry and Gibb's bulk-sediment cryopreservation study is marked Unpublished; Cornall's direct submission is dated 2011-04-01. Neither supplies a DOI or PMID. The full manuscript was not obtained, and its title does not establish viability, phenotype or treatment response.

## Completeness

Ignored-inclusive compressed-file search covered taxon-number boundaries, label/designation variants and filename slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All four matched rows were inspected: target backbone, scope, scientific name and one unrelated ATB row. Recursive structured SOURCE.json search found no further match. This establishes bounded local-source coverage, not worldwide absence of cultures or genomes.

`data/catalog/allthebacteria.tsv.xz:64995` identifies SAMEA1033639, ERR068135 and ERZ3069064. Using the previously inspected native header, scientific name and both Sylph fields are Streptococcus pneumoniae; FASTA is available, assembly/Sylph/HQ filters are PASS and prior-HQ is T. The match is only the BioSample numeric suffix and its download URL, not NCBITaxon:1033639. There is no explicit target strain/deposit/sample chain. Non-HQ status alone would not exclude a supported available FASTA; no quality-based exclusion is used. Shared samples would not prove assembly equivalence, SeqKit is not MD5, and the supplied AWS URL is mutable.

No supported omitted target strain/deposit/genome link was found. Empty optional synonyms, nomenclature, mappings, genomes, literature evidence and mechanisms are appropriate. Zero inventoried BacDive strains is not proof the organism was never cultivated. iModulonDB is not applicable: no gene, regulator, expression dataset or mechanism assertion is present.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The unavailable manuscript and bounded Assembly query remain evidence limits, not defects in the actual narrow assertions.

## Recommended Edits

None. Keep the generated YAML unchanged and do not infer identity from a numeric BioSample suffix. Future source-supported changes belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope changes belong in `curation/seed_scope.tsv:321625`.

## Follow-up Checks

For a future authorized correction, verify exact source identity and strain/deposit/sample chains, refresh the owning inventory, run the seed dry-run and `just seed-canary NCBITaxon:1033639 --force`, inspect the emitted YAML, rerun both focused validators and then `just verify-corpus` / `just qc`. No canary or regeneration was run here.

## Additional Notes

The local single-record review skill and checklist governed this report. No curation/history event, human-reviewed promotion, generated-page edit or GitHub mutation was made. Eukaryota coverage was not reopened.
