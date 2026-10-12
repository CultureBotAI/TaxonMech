# YAML Record Review: Pseudomonas sp. CP6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_cp6.yaml`
- Started UTC: 2026-10-04T03:46:25Z
- Finished UTC: 2026-10-04T03:49:52Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1032761`, Pseudomonas sp. CP6. It carries SPECIES rank, BACTERIA domain, parent unclassified Pseudomonas (196821), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, host-interaction, functional, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_cp6.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pseudomonas_sp_cp6.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared every lineage entry, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220924` and `data/catalog/ncbi_names-0005.jsonl.gz:30230` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032761&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032761) confirm identity, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs. Labels and ranks through Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales and Pseudomonadaceae match the carried hierarchy.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder, not formal species nomenclature or equivalence to another organism sharing CP6.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13315` and `curation/seed_scope.tsv:321295` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [JF280144.1](https://www.ncbi.nlm.nih.gov/nuccore/JF280144.1) is a 1,409-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain CP6 and explicit taxon 1032761. Source qualifiers identify soil and China: Shandong Province.

The sole reference is Shi and Yan's direct submission on 2011-01-30; no PMID, DOI or research-article reference is supplied. This establishes marker and collection context, not degradation capacity, antimicrobial production, pathogenicity or another strain-specific function. None is asserted by this YAML.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. A partial marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered numeric 1032761 with digit boundaries, full label, slug and bounded CP6 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 92 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry. The full native StrainInfo 66239 and GOLD Go0213319 rows were additionally inspected to assess the other CP6 designation.

Within those surfaces, no supported target culture deposit, genome association, extra source mapping or separate history record was found. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only record; no expression or functional claim is made.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require explicit strain identity crosswalks and claim-specific evidence before adding deposit, genome or functional assertions.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032761 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found. Resolve the CP6 designation ambiguity with explicit accession/deposit provenance before any proposed cross-source merge.

## Additional Notes

StrainInfo 66239 is published online as Burkholderia cepacia (292; LPSN 774277), with designations CP6 and J. Klinger 77-16. Its own deposit SI-DP 217993 is CCM 3920, available, non-type and also classified as Burkholderia cepacia. The inspected native record supplies no sequence link or target-taxon crosswalk. GOLD Go0213319 likewise names Burkholderia cepacia strain CP6 under 292 without a culture-collection identifier. A shared CP6 designation alone cannot establish or disprove isolate equivalence; these rows were not transferred to this Pseudomonas record. GOLD organism identifiers are not assemblies.

Separately cataloged actinobacterium CP6 (858254), Bacillus CP-6 (1673078), eleven Sulfurimonas Cp_6 sample names and GOLD Eubacteriales Cp6 were not equated with the target. Hospital-wastewater CP6 from Edinburgh and a soil-community CP6 from Ebinur, Xinjiang are sample designations without a target identity chain.

Other CP6 genome rows belong to Bacillus velezensis (492670; GCA_013284575.1, GCF_013284575.1; BV-BRC 492670.748), Bacillus licheniformis (1402; GCA_017338795.1, GCF_017338795.1; BV-BRC 1402.478), Corynebacterium propinquum (43769; GCA_030515735.1, GCF_030515735.1; BV-BRC 43769.49) and Escherichia coli (562; GCA_017675865.1, isolate CP6). Staphylococcus aureus S0007-EN-NS1-C1-CP-6-CL has GCA_028949185.1. None supplies a crosswalk to taxon 1032761.

SAMEA1032761 belongs to Streptococcus equi subsp. equi EQUI0227 (148942; species 1336), with GCA_001175225.1, GCF_001175225.1, BV-BRC 148942.20 and ATB ERR059771. Its BioSample suffix is not the reviewed taxon identifier. None of the excluded matches supplies target genome evidence.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
