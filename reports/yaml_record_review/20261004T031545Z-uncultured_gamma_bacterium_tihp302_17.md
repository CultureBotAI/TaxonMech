# YAML Record Review: uncultured gamma bacterium TIHP302-17

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_bacterium_tihp302_17.yaml`
- Started UTC: 2026-10-04T03:14:52Z
- Finished UTC: 2026-10-04T03:15:45Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103273`, uncultured gamma bacterium TIHP302-17. It carries SPECIES rank, BACTERIA domain, parent environmental samples (50423), seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, gene-function, causal-graph or genome-equivalence assertion is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_bacterium_tihp302_17.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_bacterium_tihp302_17.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared all lineage entries, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18382` and `data/catalog/ncbi_names-0000.jsonl.gz:38400` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103273&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103273) confirm the exact label, species rank, parent, code 11 and all seven root-first lineage IDs. The chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria and environmental samples. NCBI's environmental division does not contradict the Bacteria lineage domain.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. Preserve the source label's gamma bacterium wording. EXACT identifies this environmental placeholder, not a cultured strain or formally named species.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13301` and `curation/seed_scope.tsv:144042` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without claiming human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [AB031603.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031603.1) is a 713-base partial 16S rRNA gene sequence with genomic DNA molecule type, clone TIHP302-17, explicit taxon 103273, an environmental-sample flag and coastal marine sediment source context.

References comprise an unpublished community 16S rDNA and quinone-profiling study by Urakawa, Yoshida, Nishimura and Ohwada, and Urakawa's direct submission on 1999-08-25. No PMID or DOI is supplied. Community profiling is not clone-specific phenotype, quinone-composition or mechanism evidence; the YAML makes none of those claims.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. The marker is not an assembly. The Nuccore browser page was unavailable through the web tool; structured taxonomy and GenBank XML requests succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric identifier with digit boundaries, full label, slug and bounded TIHP302-17 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 45 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found two BacDive request/URL contexts for its distinct record 103273, not target-taxonomy evidence.

Within those bounded surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. The clone label is not a verified collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; the external marker is not a functional assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not transfer community observations or numeric collection matches to this clone. Require explicit source identity evidence before adding culture or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:103273 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

CIP 103273 is BacDive 13146, classified at strain taxon 1236960 and species taxon 86184. BacDive, LPSN and StrainInfo use Stenotrophomonas pictorum; GOLD and some NCBI source text preserve Pseudomonas pictorum. StrainInfo strain 6107 and its own deposit 154309 carry Stenotrophomonas pictorum (86184). Associated AJ717488 is a partial rpoB nucleotide record, not a target genome. GOLD Go0599628 is an organism reference, not an assembly.

DSM 103273 is Mycobacterium rhizamassiliense AB57 (1841860), BacDive 160307, StrainInfo strain 402751 and its own deposit 909778, with CSUR P2566 also named. BacDive record 103273 instead denotes Agromyces sp. ST020983 (51513). StrainInfo deposit 103273 is ATCC 23831 within strain 38255, classified as Corynebacterium (1716). All four identifier namespaces remain distinct from the target NCBI ID.

Other excluded matches include Debaryomyces maramus KY103273; Bacteroides faecis BFG-513 CP103273; uncultured Escherichia MGBC103273 GCA_948631115.1 and historical GCF_948631115.1; Listeria FLAG-103273 GCA_050886085.1; Salmonella PNUSAS103273 GCA_008827225.1; MarMAG_103273 GCA_977587815.1; Escherichia run DRR103273 with sample SAMD00077681; assembly statistics; and Salmonella ATB SeqKit checksums. None supplies clone-specific evidence.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
