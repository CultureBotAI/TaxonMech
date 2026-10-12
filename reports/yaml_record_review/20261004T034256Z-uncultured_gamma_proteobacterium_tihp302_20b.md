# YAML Record Review: uncultured gamma proteobacterium TIHP302-20b

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_20b.yaml`
- Started UTC: 2026-10-04T03:42:04Z
- Finished UTC: 2026-10-04T03:42:56Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103276`, uncultured gamma proteobacterium TIHP302-20b. It carries SPECIES rank, BACTERIA domain, parent environmental samples (50423), seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No cultured-isolate, phenotype, functional, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_20b.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_20b.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared every lineage entry, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18385` and `data/catalog/ncbi_names-0000.jsonl.gz:38403` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103276&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103276) confirm identity, species rank, parent, code 11 and all seven root-first lineage IDs. The hierarchy is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria and environmental samples. The XML's Environmental samples division does not replace the Bacteria domain established by that lineage.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies the NCBI environmental placeholder, not formal species nomenclature or an isolated culture. TIHP302-20b is not automatically interchangeable with TIHP302-20a (103275); preserve the source's complete clone designation.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13313` and `curation/seed_scope.tsv:144045` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [AB031606.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031606.1) is a 367-base partial 16S rRNA gene sequence with genomic DNA molecule type, explicit taxon 103276, clone TIHP302-20b, an environmental-sample flag and coastal marine sediment as isolation source. It does not identify a deposited strain.

References comprise an unpublished microbial-community study by Urakawa, Yoshida, Nishimura and Ohwada and Urakawa's direct submission on 1999-08-25; no PMID or DOI is supplied. Community 16S and quinone-profiling context is not direct evidence of a clone-specific metabolic phenotype. The short marker does not independently establish formal species status; the YAML carries the authority's rank without those broader claims.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. A partial marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered numeric 103276 with digit boundaries, full label, slug and TIHP302-20b separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 28 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files; its two matches are request metadata for BacDive 103276, not this NCBI identifier.

Within those surfaces, no supported target culture deposit, genome association, extra source mapping or separate history record was found. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only environmental record; a community study is not target functional evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not convert the clone into a cultured strain, merge the 20a/20b identifiers without explicit authority support, or infer identity from bare numeric accession suffixes.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:103276 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

CIP 103276 is Corynebacterium urealyticum A21397 (43771), BacDive 135241, StrainInfo 68179 and own deposit SI-DP 150345. GOLD Go0218011 is an organism record for that culture, not an assembly or this environmental clone. BacDive 103276 itself is Agromyces ST021803 (51513). Full authority-qualified accessions, not their numeric suffixes, determine these identities.

KY103276 belongs to a Debaryomyces maramus sequence; CP103276 occurs with Bacteroides faecis BFG-467 and GCA_024760145.1. Other numeric matches include uncultured Alphaproteobacteria MGBC103276 (GCA_948686475.1), uncultured bacterium MarMAG_103276 (GCA_977601365.1; BV-BRC 77133.14329), Listeria FLAG-103276 (GCA_050885265.1), Escherichia coli ATB DRR103276/SAMD00077684 and genome statistics. None supplies target genome evidence.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
