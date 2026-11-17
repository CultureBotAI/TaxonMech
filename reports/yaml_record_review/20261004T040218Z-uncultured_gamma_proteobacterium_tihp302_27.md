# YAML Record Review: uncultured gamma proteobacterium TIHP302-27

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_27.yaml`
- Started UTC: 2026-10-04T04:01:49Z
- Finished UTC: 2026-10-04T04:02:18Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103283`: SPECIES rank, BACTERIA domain, parent environmental samples (50423), seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No culture-deposit, genome-equivalence, phenotype, functional or graph claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_27.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_27.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only source comparisons checked lineage, inventories, attestation, scope, path and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. There are no curator-added graph terms or separate history references requiring a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18392` and `data/catalog/ncbi_names-0000.jsonl.gz:38410` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103283&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103283) confirm identity, species rank, parent, code 11 and all seven root-first lineage IDs. Labels and ranks through Bacteria, Pseudomonadati, Pseudomonadota and Gammaproteobacteria match. Environmental samples is the NCBI division/parent context, not a conflicting domain.

Complete structured scans found no backbone synonyms, direct children or own-ID type-material, merged-ID or dropped entry. EXACT grounds this clone-labelled NCBI placeholder, not formal nomenclature or a cultured isolate.

## Evidence

The NAME assertion and snapshot date match the inventory. `data/taxa/PATHS.tsv:13322` and `curation/seed_scope.tsv:144052` verify the slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event reproduces that reason without claiming human review.

Exact-taxon Nuccore search returned one record, inspected as GenBank XML. [AB031613.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031613.1) is a 748-base partial 16S rRNA gene sequence with genomic DNA molecule type, taxon 103283, clone TIHP302-27, an environmental-sample flag and coastal marine sediment as isolation source. These support clone and collection context, not a culture, assembly or measured phenotype.

References comprise an unpublished community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, and Urakawa's direct submission on 1999-08-25, without a PMID or DOI. A clone-specific quinone profile is not inferred. Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than universal proof of absence. All live requests succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No direct children or target-classified BacDive strain occurs in the checked backbone/inventory; zero is a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered numeric 103283 with digit boundaries, label, slug and TIHP302-27 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 41 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files; both matches were request metadata for BacDive 103283.

Within those surfaces, no supported target deposit, genome association, extra mapping or separate history record was found. Optional nomenclature, strain, phenotype and graph fields may remain empty. iModulonDB is not applicable to this taxonomy-only environmental-clone record and supplies no negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. New associations require explicit identity and claim-specific evidence.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, run `just seed-canary NCBITaxon:103283 --force`, inspect the YAML and repeat both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

CIP 103283 is Actinobacillus capsulatus 11-61/P243, BacDive 11676, with species taxon 717 and strain taxon 1120931. StrainInfo 45302 and its own deposit SI-DP 121649 carry species 717; NCBI type material and LPSN 783276 list this culture, also DSM 19761, ATCC 51571, CCUG 12396 and NCTC 11408. GOLD Go0600225 is its organism identifier, not an assembly. These species/strain scopes are not the reviewed clone.

DSM 103283 is Serratia fonticola H1w (47917), BacDive 131924, StrainInfo 401582, own deposit 908530. SI-DP 103283 instead denotes ATCC 23839: its own deposit says Mycoplasma hyorhinis (LPSN 784385, no NCBI field), whereas its StrainInfo 38260 group says Mesomycoplasma hyorhinis (2100; LPSN 798594). The group classification is not silently assigned to the deposit. BacDive 103283 itself is Agromyces ST000963 (51513).

Other matches concern Debaryomyces nepalensis marker KY103283, Bacteroides thetaiotaomicron BFG-119 sequence CP103283 within GCA_024760245.1, Oscillospiraceae MGBC103283 (GCA_948634135.1; BV-BRC 707003.3482), and an Absconditicoccaceae bin in GCA_964663645.1. Salmonella PNUSAS103283 has GCA_008795155.1; Listeria FLAG-103283 has GCA_050886145.1. ATB DRR103283 belongs to Escherichia coli sample SAMD00077691. Genome statistics and an Enterococcus checksum substring do not assign taxonomic identity. None supplies target genome evidence.

Only this report was manually written. No record YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
