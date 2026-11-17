# YAML Record Review: uncultured gamma proteobacterium TIHP302-23

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_23.yaml`
- Started UTC: 2026-10-04T03:54:21Z
- Finished UTC: 2026-10-04T03:55:16Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103279`. It represents the named environmental clone at SPECIES rank, BACTERIA domain, parent environmental samples (50423), with seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. It makes no phenotype, culture-deposit, functional, graph or genome-equivalence claim.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_23.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_23.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only source comparisons checked lineage, inventories, attestation, scope, path and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. There are no curator-added graph terms or separate history references requiring a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18388` and `data/catalog/ncbi_names-0000.jsonl.gz:38406` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103279&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103279) confirm identity, species rank, parent, code 11 and all seven root-first lineage IDs. The chain through Bacteria, Pseudomonadati, Pseudomonadota and Gammaproteobacteria agrees in labels and ranks. Environmental samples is the NCBI division/parent context, not a conflicting taxon domain.

Complete structured scans found no backbone synonyms, direct children or own-ID type-material, merged-ID or dropped entry. EXACT grounds the clone-labelled NCBI placeholder; it does not establish formal nomenclature or an isolated culture.

## Evidence

The NAME assertion and snapshot date agree with the inventory. `data/taxa/PATHS.tsv:13318` and `curation/seed_scope.tsv:144048` verify the slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event reproduces that reason and does not claim human review.

Exact-taxon Nuccore search returned one record, inspected as GenBank XML. [AB031609.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031609.1) is a 733-base partial 16S rRNA gene sequence with genomic DNA molecule type, explicit taxon 103279, clone TIHP302-23, an environmental-sample flag and coastal marine sediment as isolation source. It supports clone and collection context, not a cultured strain, genome assembly or measured phenotype.

The references are an unpublished community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, and Urakawa's direct submission dated 1999-08-25. No PMID or DOI is supplied. No clone-specific quinone profile is inferred. Exact Assembly search returned zero with a phrase-not-found warning; this bounded search does not prove universal genome absence. All live taxonomy and sequence requests succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No direct children or target-classified BacDive strains were found in the checked backbone/inventory, consistent with the source count of zero.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered numeric 103279 with digit boundaries, label, slug and TIHP302-23 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 107 matching lines were inspected in structured context; initially truncated output was reread in complete chunks. Recursive SOURCE.json traversal also included ignored files; its two matches were request metadata for BacDive 103279, not this NCBI taxon.

Within those surfaces, no supported target deposit, genome association, additional source mapping or separate history record was found. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only environmental-clone record; absence there is not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require explicit identity and claim-specific evidence for future deposit, genome or phenotype additions.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, run `just seed-canary NCBITaxon:103279 --force`, inspect the generated YAML and repeat both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

DSM 103279 is Klebsiella michiganensis H1g (1134687), BacDive 132136, StrainInfo 404237, own deposit SI-DP 911365. Its native sequence association and BacDive assembly accession are unversioned GCA_020115525; separate NCBI/GTDB/BV-BRC rows carry GCA_020115525.1 and GCF_020115525.1. BV-BRC identifiers 1134687.344, 1134687.398, 1134687.454, 1134687.514 and 1134687.581 refer to this culture. Its BioSample SAMN12212321 supports ATB `shares_biosample` links, not sequence-level genome equivalence and not association with this clone. Project identifiers PRJNA543274 and PRJNA224116 are also not assemblies.

CIP 103279 is Sporolactobacillus inulinus EU (2078), BacDive 14396, StrainInfo 297026, own deposit 155206, with aliases including DSM 20348, ATCC 15538 and JCM 6014. Native BacDive, LPSN and NCBI type-material records concern that organism. SI-DP 103279 is instead Streptomyces ATCC 23836 (1883), StrainInfo 38258. BacDive 103279 itself is Agromyces ST000801 (51513). These authority-qualified identifiers are not interchangeable.

Other numeric matches include Debaryomyces mycophilus marker KY103279, Bacteroides fragilis BFG-569 sequence CP103279 in BV-BRC 817.2244, Muribaculaceae MGBC103279 (GCA_948670065.1; BV-BRC 2301481.5898), MarMAG_103279 (GCA_977594965.1; BV-BRC 77133.14016), and a Sphingobacteriales bin in GCA_964843215.1. ATB DRR103279 belongs to Escherichia coli sample SAMD00077687. Other ATB checksum substrings and genome-statistic matches are not taxon assignments. None provides a target genome association.

Only this new report was manually written. No record YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
