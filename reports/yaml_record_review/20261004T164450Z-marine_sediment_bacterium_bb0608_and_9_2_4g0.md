# YAML Record Review: marine sediment bacterium BB0608_AND_9.2_4G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_4g0.yaml`
- Started UTC: 2026-10-04T16:43:51Z
- Finished UTC: 2026-10-04T16:44:50Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for NCBITaxon:1033636, marine sediment bacterium BB0608_AND_9.2_4G0. It is SPECIES / BACTERIA, with parent NCBITaxon:49928, genetic code 11, EXACT grounding and SEEDED status. It contains zero inventoried strains, one NCBITAXON NAME attestation and the 2026-09-13T17:54:04Z seed event. No source YAML was edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_4g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_4g0.yaml`: one file, zero ERROR rows.
- Ignored-inclusive exact-ID search across `data/taxa` resolved one YAML. An ignored-inclusive filename search in the review directory found no previous report for this stem.
- Structured comparisons passed for the complete backbone chain, seven source inventories, PATHS, scope reason, seed-event text and NCBI attestation. Exact type-material, merged-ID and dropped scans were also completed.
- Not checked: full-corpus `just qc`, `just verify-corpus`, tests, provenance, global term/reference and history/product gates, or rendering. Focused source comparisons do not substitute for corpus reproduction. No curator-added graph nodes or external record-level evidence references require an additional product check here.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221270` matches the record's identity, rank, parent, code and 2026-09-13 snapshot, with empty synonym and retirement fields. The complete root-first chain agrees: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), unclassified Bacteria 49928 (NO_RANK). The native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:30578`. PATHS row 13723 and `curation/seed_scope.tsv:321622` confirm the slug and seed reason.

Live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033636&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033636) were read and agree on identity, rank and lineage. EFetch additionally confirms parent and code; Datasets includes root, absent from EFetch's displayed lineage. The Taxonomy Browser could not be retrieved through the web tool; successful structured authority responses supplied verification. Species rank is an NCBI classification, not valid-publication evidence or a claim that a marker sequence independently resolves the organism's finer placement.

## Evidence

The NCBI attestation correctly counts one NAME. Complete scans found no direct children or target matches in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. Type-material, merged and dropped scans returned no target entries.

Live exact-organism searches returned zero Assembly results (with phrase-not-found/no-items warnings) and one Nuccore result, UID 333384528. [JF750181.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750181.1) is a 539 bp partial 16S rRNA sequence. Its source qualifiers explicitly identify strain BB0608_AND_9.2_4G0, taxon:1033636 and genomic DNA, with coastal marine sediment, Australia: Gulf of Carpentaria, and Jun-2008 collection context. It is not an assembly or a culture-collection deposit.

Both reference entries were inspected. The bulk-sediment cryopreservation study by Cornall, Beyer, Streten-Joyce, McGuinness, Parry and Gibb is marked Unpublished; Cornall's direct submission is dated 2011-04-01. Neither supplies a DOI or PMID. The full manuscript was not obtained, so its title is not treated as evidence of viability, phenotype, treatment response or a taxon-wide mechanism.

## Completeness

The ignored-inclusive compressed-file search covered exact taxon-number boundaries, designation/label variants and filename slug throughout `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All four matched rows were inspected: backbone, scope, native NCBI name and the unrelated ATB row below. Recursive structured SOURCE.json search found no further match. This bounded search does not prove worldwide absence of genomes or cultures.

`data/catalog/allthebacteria.tsv.xz:64992` identifies SAMEA1033636, ERR068171 and ERZ3069059. The native header was checked in this review session. Scientific name and both Sylph species fields are Streptococcus pneumoniae; FASTA is available, assembly/Sylph/HQ filters are PASS and prior-HQ is T. The number matches only a BioSample suffix and its download URL, not NCBITaxon:1033636. No exact target strain/deposit/sample chain supports attaching that assembly. Non-HQ status alone would not exclude a supported available FASTA; no quality-based exclusion is used here. A shared sample would still not establish genome equivalence, SeqKit is not MD5, and the AWS URL is mutable.

No supported omitted strain/deposit/genome link was found. Empty optional synonyms, nomenclature, mappings, genomes, record-level literature evidence and mechanisms are appropriate. `strain_count: 0` is a BacDive inventory count, not proof of never having been cultivated. iModulonDB is not applicable because this record has no gene, regulator, expression dataset or mechanism assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The unavailable manuscript and bounded genome query are documented limits, not established defects in this narrow seeded record.

## Recommended Edits

None. Do not edit generated YAML or infer genome identity from numeric suffixes. Future evidence-backed changes belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is `curation/seed_scope.tsv:321622`.

## Follow-up Checks

For a future authorized correction, verify explicit source identity and strain/deposit/sample links, refresh the owning inventory, run the seed dry-run and `just seed-canary NCBITaxon:1033636 --force`, inspect the emitted YAML, rerun both focused validators and then `just verify-corpus` / `just qc`. No canary or regeneration was performed here.

## Additional Notes

Review followed the local single-record skill and checklist. No curation/history event, human-reviewed promotion, generated-page edit or GitHub mutation was made. Eukaryota coverage was left intact.
