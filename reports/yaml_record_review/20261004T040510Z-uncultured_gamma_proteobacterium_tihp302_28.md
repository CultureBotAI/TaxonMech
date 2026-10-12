# YAML Record Review: uncultured gamma proteobacterium TIHP302-28

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_28.yaml`
- Started UTC: 2026-10-04T04:04:41Z
- Finished UTC: 2026-10-04T04:05:10Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103284`: SPECIES rank, BACTERIA domain, parent environmental samples (50423), seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No culture-deposit, genome-equivalence, phenotype, functional or graph claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_28.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_28.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only source comparisons checked lineage, inventories, attestation, scope, path and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. There are no curator-added graph terms or separate history references requiring a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18393` and `data/catalog/ncbi_names-0000.jsonl.gz:38411` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103284&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103284) confirm identity, species rank, parent, code 11 and all seven root-first lineage IDs. Labels and ranks through Bacteria, Pseudomonadati, Pseudomonadota and Gammaproteobacteria match. Environmental samples is the NCBI division/parent context, not a conflicting domain.

Complete structured scans found no backbone synonyms, direct children or own-ID type-material, merged-ID or dropped entry. EXACT grounds this clone-labelled NCBI placeholder, not formal nomenclature or a cultured isolate.

## Evidence

The NAME assertion and snapshot date match the inventory. `data/taxa/PATHS.tsv:13324` and `curation/seed_scope.tsv:144053` verify the slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event reproduces that reason without claiming human review.

Exact-taxon Nuccore search returned one record, inspected as GenBank XML. [AB031614.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031614.1) is a 675-base partial 16S rRNA gene sequence with genomic DNA molecule type, taxon 103284, clone TIHP302-28, an environmental-sample flag and coastal marine sediment as isolation source. These support clone and collection context, not a culture, assembly or measured phenotype.

References comprise an unpublished community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, and Urakawa's direct submission on 1999-08-25, without a PMID or DOI. A clone-specific quinone profile is not inferred. Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than universal proof of absence. All live requests succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No direct children or target-classified BacDive strain occurs in the checked backbone/inventory; zero is a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered numeric 103284 with digit boundaries, label, slug and TIHP302-28 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 45 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files; both matches were request metadata for BacDive 103284.

Within those surfaces, no supported target deposit, genome association, extra mapping or separate history record was found. Optional nomenclature, strain, phenotype and graph fields may remain empty. iModulonDB is not applicable to this taxonomy-only environmental-clone record and supplies no negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. New associations require explicit identity and claim-specific evidence.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, run `just seed-canary NCBITaxon:103284 --force`, inspect the YAML and repeat both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

CIP 103284 is Actinobacillus equuli subsp. equuli PM 30/53, BacDive 11689, with subspecies taxon 202947 and species taxon 718. StrainInfo 92092 carries subspecies 202947, but its own CIP deposit SI-DP 148140 lacks a taxon object; the group classification is not silently assigned to that deposit. Its linked AJ549506 is a partial 23S marker, not an assembly. Native BacDive, NCBI type material and LPSN list the culture, also DSM 19655, ATCC 19392, JCM 2432 and NCTC 8529. Cataloged CIP103284T assemblies GCA_965135905.1 and GCF_965135905.1 belong to this Actinobacillus, and GOLD Go0600089 is an organism identifier.

DSM 103284 is Neomoorella thermoacetica (1525), named Moorella thermoacetica in GOLD/BV-BRC, with GCA_001874605.1, GCF_001874605.1 and BV-BRC 1525.8. BacDive 103284 itself is Agromyces ST000936 (51513). Neither is the environmental clone.

Other matches concern Debaryomyces prosopidis marker KY103284, Bacteroides thetaiotaomicron BFG-119 sequence CP103284 within GCA_024760245.1, Muribaculaceae MGBC103284 (GCA_948665055.1; BV-BRC 2301481.5811), an Acidimicrobiales bin in GCA_964967835.1 and Salmonella PNUSAS103284 (GCA_008791545.1). ATB DRR103284 belongs to Escherichia coli sample SAMD00077692. Genome statistics and checksum substrings do not assign taxonomic identity. None supplies target genome evidence.

Only this report was manually written. No record YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
