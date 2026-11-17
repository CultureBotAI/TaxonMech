# YAML Record Review: uncultured gamma proteobacterium TIHP302-06

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_06.yaml`
- Started UTC: 2026-10-04T02:06:55Z
- Finished UTC: 2026-10-04T02:07:52Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:103266`, uncultured gamma proteobacterium TIHP302-06. It is a SPECIES-rank environmental-clone placeholder in BACTERIA under environmental samples (50423), with seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NAME assertion and one seed event. No gene-function, phenotype, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_06.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_06.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18375` and native name row `data/catalog/ncbi_names-0000.jsonl.gz:38393` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103266&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103266) confirm identity, species rank, parent, code 11 and all seven root-first lineage IDs. The environmental-samples division in NCBI does not replace the Bacteria domain in the lineage.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT describes this NCBI identity, not a formally named cultured species. The TIHP302-06 suffix denotes a distinct clone, not a synonym of the neighboring TIHP302 entries.

## Evidence

The single NCBITAXON NAME assertion and 2026-09-13 snapshot note agree with the inventory. `data/taxa/PATHS.tsv:13267` and `curation/seed_scope.tsv:144035` confirm identifier, slug and the NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one sequence, inspected as GenBank XML. [AB031594.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031594.1) is a 749-base partial 16S rRNA gene sequence with genomic DNA molecule type, taxon 103266, clone TIHP302-06 and an environmental-sample flag. Its stated isolation source is coastal marine sediment, not a culture-collection deposit.

The entry cites an unpublished microbial-community study by Urakawa, Yoshida, Nishimura and Ohwada, plus Urakawa's direct submission on 1999-08-25; neither reference supplies a PMID or DOI. The reference title's community-level quinone profiling does not establish a clone-specific phenotype. The YAML correctly makes no such extrapolation.

A partial marker is not a genome assembly. Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than universal absence evidence. The browser sequence view failed, but both structured taxonomy requests and the GenBank XML request succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the number with digit boundaries, full label, slug and clone-separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 38 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

No independently supported target culture deposit, genome association, extra source mapping or separate history record was found within those surfaces. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML; an external marker annotation is not a record gene-function claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve environmental-clone identity, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not promote community measurements or similarly numbered culture accessions into this clone record.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:103266 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded identity collisions include CIP 103266, Sporosarcina globispora/Bacillus globisporus W25 (taxon 1459; BacDive 11976; StrainInfo strain 1121, own deposit 148805), and DSM 103266, Escherichia coli APEC 10400 (562; BacDive 158945; StrainInfo strain 398869, own deposit 905615). Their full source identities differ from NCBITaxon:103266.

Other numeric matches concern Enterococcus MGBC103266, MarMAG and Flavobacterium metagenome identifiers, Listeria FLAG-103266, Salmonella PNUSAS103266, nucleotide accession CP103266, run DRR103266 and unrelated contig statistics. None establishes a target link.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
