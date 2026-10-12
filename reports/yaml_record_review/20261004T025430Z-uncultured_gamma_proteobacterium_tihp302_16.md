# YAML Record Review: uncultured gamma proteobacterium TIHP302-16

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_16.yaml`
- Started UTC: 2026-10-04T02:51:02Z
- Finished UTC: 2026-10-04T02:54:30Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:103272`, uncultured gamma proteobacterium TIHP302-16. It has SPECIES rank, BACTERIA domain, parent environmental samples (50423), seven lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. It makes no curated phenotype, gene-function, causal-graph or genome-equivalence claim.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_16.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_16.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked the full lineage, source inventories, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph term or separate history reference requires a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18381` and `data/catalog/ncbi_names-0000.jsonl.gz:38399` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103272&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103272) confirm the label, species rank, parent, code 11 and all seven root-first lineage entries: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria and environmental samples.

Complete structured scans found no backbone synonym or direct child and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI environmental placeholder. It does not establish a formally named species, a cultured isolate or equivalence to another taxon carrying the number 103272.

## Evidence

The single NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13290` and `curation/seed_scope.tsv:144041` confirm the identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [AB031602.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031602.1) is a 792-base partial 16S rRNA gene sequence with genomic DNA molecule type, clone TIHP302-16, explicit taxon 103272, an environmental-sample flag and coastal marine sediment source context.

The references comprise an unpublished community 16S rDNA and quinone-profiling study by Urakawa, Yoshida, Nishimura and Ohwada, and Urakawa's direct submission on 1999-08-25. No PMID or DOI is supplied. Community profiling does not establish a clone-specific phenotype, metabolic mechanism or quinone composition; the YAML asserts none of these.

Exact Assembly search returned zero with a phrase-not-found warning. That bounded query is not universal proof of genome absence. The partial marker is not an assembly, culture deposit or isolate-level genome. Structured taxonomy and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric identifier with digit boundaries, full label, slug and bounded TIHP302-16 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 57 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those bounded surfaces, no independently supported target deposit, genome association, extra source mapping or separate history record was found. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only record; an external marker sequence is not a gene-function assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve the source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require explicit identity crosswalks before adding culture or genome identifiers. Do not transfer community-level observations to this clone.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:103272 --force`, inspect the YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

CIP 103272 belongs to Pseudomonas lundensis (86185), BacDive 13017, StrainInfo strain 7808 and its own deposit 31767. Associated AJ717428 is a partial rpoB nucleotide record, not a TIHP302-16 genome.

DSM 103272 belongs to the Corynebacterium taxon 1852380, BacDive 160190, StrainInfo strain 403126 and its own deposit 910176. The StrainInfo group uses urinipleomorphum with LPSN 12129, while the own deposit and BacDive preserve urinapleomorphum; the deposit uses LPSN 12126. These source-specific spelling and identifier differences are retained, not silently reconciled or transferred to the target.

NBRC 103272 occurs as Sphingobium sp. NBRC 103272 (1113922), including BacDive 162027 and JCM 17495 / FERM AP-20677 aliases. The inspected GOLD chain Go0003693 / Gp0003693 / Ga0009326 instead names Sphingobium sp. SYK-6 (627192), with GCA_000283515.1, IMG 2511231055, SAMD00061118 and PRJNA67115. Those other-taxon classification distinctions were not resolved by this review. Neither numeric overlap nor the presence of that assembly establishes any identity relationship to NCBITaxon:103272.

Other excluded matches include Debaryomyces maramus KY103272; Bacteroides faecis BFG513 CP103272; Escherichia coli PNUSAE103272 GCA_023670805.1/.2; Salmonella PNUSAS103272; Listeria FLAG103272 GCA_050884885.1; uncultured Prevotellamassilia MGBC103272 GCA_948694795.1; MarMAG103272 GCA_977537075.1; Escherichia coli run DRR103272 with sample SAMD00077680; assembly statistics; and a Bordetella SeqKit checksum. None supplies target-specific evidence.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
