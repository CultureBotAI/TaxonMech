# YAML Record Review: Thermoanaerobacter sp. xyl-d

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thermoanaerobacter_sp_xyl_d.yaml`
- Started UTC: 2026-10-04T17:01:54Z
- Finished UTC: 2026-10-04T17:03:00Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for NCBITaxon:1033656, Thermoanaerobacter sp. xyl-d. Rank SPECIES, domain BACTERIA, parent NCBITaxon:2636821, genetic code 11, EXACT grounding and SEEDED status are retained. It contains zero inventoried strains, one NCBITAXON NAME attestation and the 2026-09-13T17:54:04Z seed event. No YAML, history or status was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/thermoanaerobacter_sp_xyl_d.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/thermoanaerobacter_sp_xyl_d.yaml`: one file, zero ERROR rows.
- Ignored-inclusive exact identifier search across `data/taxa` resolved only this YAML; ignored-inclusive report filename search found no previous review for its stem.
- Structured comparisons passed for complete backbone ancestry, seven source inventories, PATHS, scope, NCBI attestation and seed-event text. Exact type-material, merged-ID and dropped scans were completed.
- Not checked: full-corpus `just qc`, `just verify-corpus`, tests, provenance, global term/reference and history/product gates, or rendering. Bounded comparisons do not establish corpus reproduction. No curator-added graph nodes or external record-level evidence references require an additional product check here.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221279` agrees on identity, rank, parent, code and snapshot 2026-09-13; synonym and retirement fields are empty. The ten ancestors agree in full: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Bacillota 1239 (PHYLUM), Clostridia 186801 (CLASS), Thermoanaerobacterales 68295 (ORDER), Thermoanaerobacteraceae 186814 (FAMILY), Thermoanaerobacter 1754 (GENUS), unclassified Thermoanaerobacter 2636821 (NO_RANK). The native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:30587`; PATHS row 13732 and `curation/seed_scope.tsv:321631` fix the slug and seed reason.

Live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033656&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033656) were inspected and confirm identity, rank and ancestry. EFetch confirms parent and code; Datasets includes root, omitted from EFetch's displayed lineage. The Taxonomy Browser was inaccessible through the web tool, so successful structured authority responses supplied verification. An unnamed isolate's NCBI species rank is not evidence of a validly published binomial or type-strain status.

## Evidence

The sole attestation correctly counts one NCBI NAME, not a genome. Complete scans found no direct children or target matches in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. Type-material, merged-ID and dropped inventories also had no exact target entry.

Live exact-organism queries returned zero Assembly results, including phrase-not-found/no-items warnings, and one Nuccore result, UID 333411329. [HQ710549.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ710549.1) is a 1482 bp partial 16S rRNA sequence. Its inspected source qualifiers explicitly identify strain xyl-d, taxon:1033656 and genomic DNA, and report oil-field water in Shengli oilfield, China, plus the submitted primer sequences. No collection date or culture-collection deposit is supplied in those qualifiers.

The sole sequence reference is Zhang W.'s direct submission dated 2010-12-14 from the Biogas Institute of the Ministry of Agriculture in Chengdu. It supplies no DOI, PMID or named research article. The marker is not an assembly or an independent resolution of the isolate's species identity. The collection context does not establish hydrocarbon degradation, and neither the genus nor the xyl-d designation proves temperature range, oxygen requirements or xylose metabolism. No such phenotype is asserted by the YAML.

## Completeness

Ignored-inclusive compressed-file search covered taxon-number boundaries, xyl-d/xyl_d/xyl d designations, the label and filename slug throughout `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The search and recursive structured SOURCE.json scan were rerun with a cross-engine-compatible alphanumeric boundary before assessing completeness. All four matched rows were inspected: target backbone, scope, scientific name and one unrelated ATB row. SOURCE.json returned no additional match. This is bounded local-source and live-query coverage, not worldwide biological absence.

`data/catalog/allthebacteria.tsv.xz:65014` identifies SAMEA1033656, ERR064663/ERR085922 and ERZ3069088. Using the previously inspected native header, scientific name and both Sylph fields are Streptococcus pneumoniae, FASTA is available, assembly/Sylph/HQ filters are PASS and prior-HQ is T. Only the BioSample suffix and its download URL match the taxon number. No target-linked strain/deposit/sample chain is present. Non-HQ status alone would not exclude a supported available FASTA; unrelated identity is decisive here. Shared samples do not establish genome equivalence, SeqKit is not MD5 and the AWS URL is mutable.

No supported omitted target strain, deposit or genome association was found. Optional synonyms, nomenclature, mappings, genomes, literature evidence and mechanisms are appropriately empty. Zero BacDive strain entries does not mean xyl-d was never cultivated. iModulonDB is not applicable: xyl-d is a submitted strain designation here, not an asserted gene, regulator or expression-module identifier, and no mechanistic claim is present.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The limited sequence metadata and bounded Assembly query constrain interpretation but do not contradict the taxonomic assertions present.

## Recommended Edits

None. Preserve generated YAML; do not invent a culture deposit, genome or phenotype from the designation or isolation source. Future evidence-backed changes belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is `curation/seed_scope.tsv:321631`.

## Follow-up Checks

For an authorized future correction, establish explicit source identity and strain/deposit/sample links, refresh the owning inventory, run the seed dry-run and `just seed-canary NCBITaxon:1033656 --force`, inspect the emitted YAML, rerun both focused validators and then `just verify-corpus` / `just qc`. No canary or regeneration was performed here.

## Additional Notes

The local single-record review skill and checklist governed this report. No curation/history event, human-reviewed promotion, generated-page edit or GitHub mutation was made. Eukaryota coverage was left intact.
