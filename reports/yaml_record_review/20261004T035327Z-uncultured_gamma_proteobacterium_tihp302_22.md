# YAML Record Review: uncultured gamma proteobacterium TIHP302-22

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_22.yaml`
- Started UTC: 2026-10-04T03:52:54Z
- Finished UTC: 2026-10-04T03:53:27Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103278`. It represents the named environmental clone at SPECIES rank, BACTERIA domain, parent environmental samples (50423), with seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. It makes no phenotype, culture-deposit, functional, graph or genome-equivalence claim.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_22.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_22.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only source comparisons checked lineage, inventories, attestation, scope, path and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. There are no curator-added graph terms or separate history references requiring a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18387` and `data/catalog/ncbi_names-0000.jsonl.gz:38405` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103278&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103278) confirm identity, species rank, parent, code 11 and all seven root-first lineage IDs. The chain through Bacteria, Pseudomonadati, Pseudomonadota and Gammaproteobacteria agrees in labels and ranks. Environmental samples is the NCBI division/parent context, not a conflicting taxon domain.

Complete structured scans found no backbone synonyms, direct children or own-ID type-material, merged-ID or dropped entry. EXACT grounds the clone-labelled NCBI placeholder; it does not establish formal nomenclature or an isolated culture.

## Evidence

The NAME assertion and snapshot date agree with the inventory. `data/taxa/PATHS.tsv:13317` and `curation/seed_scope.tsv:144047` verify the slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event reproduces that reason and does not claim human review.

Exact-taxon Nuccore search returned one record, inspected as GenBank XML. [AB031608.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031608.1) is a 748-base partial 16S rRNA gene sequence with genomic DNA molecule type, explicit taxon 103278, clone TIHP302-22, an environmental-sample flag and coastal marine sediment as isolation source. It supports clone and collection context, not a cultured strain, genome assembly or measured phenotype.

The references are an unpublished community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, and Urakawa's direct submission dated 1999-08-25. No PMID or DOI is supplied. No clone-specific quinone profile is inferred. Exact Assembly search returned zero with a phrase-not-found warning; this bounded search does not prove universal genome absence. All live taxonomy and sequence requests succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No direct children or target-classified BacDive strains were found in the checked backbone/inventory, consistent with the source count of zero.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered numeric 103278 with digit boundaries, label, slug and TIHP302-22 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 25 matching lines were inspected in structured context. Recursive SOURCE.json traversal also included ignored files; its two matches were request metadata for BacDive 103278, not this NCBI taxon.

Within those surfaces, no supported target deposit, genome association, additional source mapping or separate history record was found. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only environmental-clone record; absence there is not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require explicit identity and claim-specific evidence for future deposit, genome or phenotype additions.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, run `just seed-canary NCBITaxon:103278 --force`, inspect the generated YAML and repeat both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

DSM 103278 is Pseudomonas PH 1b/PH1b, BacDive 131910 with NCBI mapping 306. StrainInfo 406404 and its own deposit SI-DP 913703 instead carry genus Pseudomonas (286); both classifications are preserved here and neither is target taxon 103278. CIP 103278 is Burkholderia cepacia (292), StrainInfo 67664, own deposit 149489, published offline; GOLD labels the same culture designation. BacDive 103278 itself is Agromyces ST023737 (51513). Numeric equality across authorities supplies no identity crosswalk.

Other numeric matches include Debaryomyces maramus marker KY103278, Bacteroides fragilis BFG-569 sequence CP103278 in BV-BRC 817.2244, uncultured Mailhella MGBC103278 (GCA_948624375.1; BV-BRC 1981031.393), MarMAG_103278 (GCA_977587485.1; BV-BRC 77133.13721), and Listeria monocytogenes FLAG-103278 (GCA_050885285.1). ATB DRR103278 belongs to Escherichia coli sample SAMD00077686. Genome-statistic matches are not taxon assignments. None provides a target genome association.

Only this new report was manually written. No record YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
