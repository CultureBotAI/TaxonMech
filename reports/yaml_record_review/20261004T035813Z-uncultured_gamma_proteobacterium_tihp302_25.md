# YAML Record Review: uncultured gamma proteobacterium TIHP302-25

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_25.yaml`
- Started UTC: 2026-10-04T03:57:42Z
- Finished UTC: 2026-10-04T03:58:13Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103281`: SPECIES rank, BACTERIA domain, parent environmental samples (50423), seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No culture-deposit, genome-equivalence, phenotype, functional or graph claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_25.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_25.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only source comparisons checked lineage, inventories, attestation, scope, path and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. There are no curator-added graph terms or separate history references requiring a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18390` and `data/catalog/ncbi_names-0000.jsonl.gz:38408` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103281&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103281) confirm identity, species rank, parent, code 11 and all seven root-first lineage IDs. Labels and ranks through Bacteria, Pseudomonadati, Pseudomonadota and Gammaproteobacteria match. Environmental samples is the NCBI division/parent context, not a conflicting domain.

Complete structured scans found no backbone synonyms, direct children or own-ID type-material, merged-ID or dropped entry. EXACT grounds this clone-labelled NCBI placeholder, not formal nomenclature or a cultured isolate.

## Evidence

The NAME assertion and snapshot date match the inventory. `data/taxa/PATHS.tsv:13320` and `curation/seed_scope.tsv:144050` verify the slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event reproduces that reason without claiming human review.

Exact-taxon Nuccore search returned one record, inspected as GenBank XML. [AB031611.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031611.1) is a 698-base partial 16S rRNA gene sequence with genomic DNA molecule type, taxon 103281, clone TIHP302-25, an environmental-sample flag and coastal marine sediment as isolation source. These support clone and collection context, not a culture, assembly or measured phenotype.

References comprise an unpublished community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, and Urakawa's direct submission on 1999-08-25, without a PMID or DOI. A clone-specific quinone profile is not inferred. Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than universal proof of absence. All live requests succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No direct children or target-classified BacDive strain occurs in the checked backbone/inventory; zero is a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered numeric 103281 with digit boundaries, label, slug and TIHP302-25 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 33 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files; both matches were request metadata for BacDive 103281.

Within those surfaces, no supported target deposit, genome association, extra mapping or separate history record was found. Optional nomenclature, strain, phenotype and graph fields may remain empty. iModulonDB is not applicable to this taxonomy-only environmental-clone record and supplies no negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. New associations require explicit identity and claim-specific evidence.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, run `just seed-canary NCBITaxon:103281 --force`, inspect the YAML and repeat both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

CIP 103281 is Pseudomonas putida Berlin 33/2 (303), BacDive 12920, also DSM 50026, StrainInfo 50932, own deposit SI-DP 154334. GOLD Go0207078 refers to that culture, not an assembly. DSM 103281 is Morganella morganii H1r (582), BacDive 131822, StrainInfo 400885, own deposit 907776. SI-DP 103281 is Edwardsiella tarda ATCC 23837 (636), StrainInfo 38259. BacDive 103281 is Agromyces ST000770 (51513). These authority-qualified identifiers are not interchangeable.

Other matches concern Debaryomyces nepalensis marker KY103281, Bacteroides fragilis BFG-569 sequence CP103281 in BV-BRC 817.2244, and uncultured bacterium MGBC103281 (GCA_948703425.1; BV-BRC 77133.5305). ATB DRR103281 belongs to Escherichia coli sample SAMD00077689; another match is in a Salmonella sample's checksum. Genome-statistic matches do not assign taxonomic identity. None supplies target genome evidence.

Only this report was manually written. No record YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
