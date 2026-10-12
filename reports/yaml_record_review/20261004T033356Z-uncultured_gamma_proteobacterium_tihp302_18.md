# YAML Record Review: uncultured gamma proteobacterium TIHP302-18

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_18.yaml`
- Started UTC: 2026-10-04T03:32:49Z
- Finished UTC: 2026-10-04T03:33:56Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103274`, uncultured gamma proteobacterium TIHP302-18. It carries SPECIES rank, BACTERIA domain, parent environmental samples (50423), seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No cultured-isolate, phenotype, functional, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_18.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_18.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared every lineage entry, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18383` and `data/catalog/ncbi_names-0000.jsonl.gz:38401` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103274&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103274) confirm identity, species rank, parent, code 11 and all seven root-first lineage IDs. The hierarchy is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria and environmental samples. The XML's Environmental samples division does not replace the Bacteria domain established by that lineage.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies the NCBI environmental placeholder, not formal species nomenclature or an isolated culture. Preserve the full authority label, including gamma proteobacterium.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13309` and `curation/seed_scope.tsv:144043` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [AB031604.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031604.1) is a 775-base partial 16S rRNA gene sequence with genomic DNA molecule type, explicit taxon 103274, clone TIHP302-18, an environmental-sample flag and coastal marine sediment as isolation source. It does not identify a deposited strain.

References comprise an unpublished microbial-community study by Urakawa, Yoshida, Nishimura and Ohwada and Urakawa's direct submission on 1999-08-25; no PMID or DOI is supplied. Community 16S and quinone-profiling context is not direct evidence of a clone-specific metabolic phenotype. None is asserted by this YAML.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. A partial marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered numeric 103274 with digit boundaries, full label, slug and TIHP302-18 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 53 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files; its two matches are request metadata for BacDive 103274, not this NCBI identifier.

Within those surfaces, no supported target culture deposit, genome association, extra source mapping or separate history record was found. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only environmental record; a community study is not target functional evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not convert the clone into a cultured strain or infer identity from bare numeric accession suffixes.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:103274 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

CIP 103274 is Staphylococcus carnosus (1281), BacDive 14516, associated with strain 361, DSM 20501, ATCC 51365 and other deposits. StrainInfo 46150 carries the subspecies label Staphylococcus carnosus subsp. carnosus and its own CIP deposit SI-DP 155326; the local LPSN inventory treats that subspecies as a synonym of the species. The related sequence rows AJ343899, EU652788, EU659871, EU659917, EU659937 and EU727181 describe partial marker genes, not assemblies. GOLD Go0296902 is an organism record, not an assembly. None of this evidence belongs to TIHP302-18.

DSM 103274 is Mycobacterium numidiamassiliense AB215 (1841861), BacDive 160156, with CSUR P2567 and StrainInfo 404699, own deposit SI-DP 911863. BacDive 103274 itself is Agromyces ST020997 (51513), not a taxonomic crosswalk. KY103274 belongs to a Debaryomyces maramus sequence; CP103274 occurs with Bacteroides faecis BFG-467 and GCA_024760145.1.

Other numeric matches include uncultured Lachnospiraceae MGBC103274 (GCA_948729435.1), uncultured bacterium MarMAG_103274 (GCA_977601205.1; BV-BRC 77133.14314), Listeria FLAG-103274 (GCA_050885145.1), Salmonella PNUSAS103274 (GCA_008826705.1), Escherichia coli ATB run DRR103274/SAMD00077682, genome statistics and sequence checksums. The shared digits do not support a target genome association.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
