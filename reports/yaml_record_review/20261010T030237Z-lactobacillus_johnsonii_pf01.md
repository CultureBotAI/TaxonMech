# YAML Record Review: Lactobacillus johnsonii pf01

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lactobacillus_johnsonii_pf01.yaml`
- Started UTC: 2026-10-10T02:59:57Z
- Finished UTC: 2026-10-10T03:02:37Z
- Verdict: needs curation

## Target

The entire 84-line generated `TaxonRecord` was read. `NCBITaxon:1037411` denotes Lactobacillus johnsonii pf01, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:33959`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

It contains ten ancestors, one GTDB species mapping with 38 genomes, three exact synonyms, one GTDB xref, zero inventoried strains, NCBITAXON/GTDB/MADIN attestations and one seed event. No individual genome, culture deposit, phenotype or causal graph is asserted in the YAML. Preserve the lowercase pf01 designation used by NCBI; uppercase PF01 in the linked publication is source-specific typography.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/lactobacillus_johnsonii_pf01.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/lactobacillus_johnsonii_pf01.yaml --out /private/tmp/taxonmech-pf01-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, all ancestors, code, NCBI synonyms, own source counts, unique index/scope resolution and exact seed reason. Complete backbone scanning found no immediate child. Own type-material, merged-ID and dropped-record inventories had no rows.
- Complete own NCBI names, current/historical assembly rows, GTDB genome, BV-BRC and GOLD source chains were read. Exact structured GTDB cluster filtering counted 38 unique assemblies; all member identities and the full representative row were inspected. This is a source comparison, not a substitute corpus validator.
- Live NCBI taxonomy and assembly APIs, LPSN species text and the inventory-linked PubMed record/abstract were inspected. The GTDB browser returned only a loading shell without populated genome data; native pinned metadata supplied the cluster evidence. PMC returned a browser-check page, so full-text genome methods were not inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, source replay, rendering and publication gates. No graph is present for `just validate-products`.
- Ignored-independent enumeration of the configured kg-microbe `data` directory found no GTDB/Madin files or `edges.tsv`. Original transformed edges and the four individual Madin assertions were unavailable for replay. Inventory agreement is distinguished from verification of their underlying biological content.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222748`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037411&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037411) agree on the exact label and strain rank. EFetch confirms parent 33959 and code 11. Datasets includes root 1 and explicitly reports one assembly.

The complete root-first chain matches the backbone: root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Lactobacillales, Lactobacillaceae, Lactobacillus and Lactobacillus johnsonii. The native NCBI name rows `data/catalog/ncbi_names-0005.jsonl.gz:32384` through `:32386` and EFetch support the scientific name and both strain-qualified equivalent names. Those NCBI exact synonyms are sound.

[LPSN's species page](https://lpsn.dsmz.de/species/lactobacillus-johnsonii) recognizes Lactobacillus johnsonii and names type deposits including ATCC 33200 and DSM 10533, not pf01. Species nomenclature is not evidence that pf01 is the type strain.

GTDB places this assembly in the placeholder species `s__Lactobacillus sp945980025`, whereas NCBI retains L. johnsonii. Preserve that source-specific classification difference rather than silently renaming the NCBI record. Neither difference in names nor membership in a GTDB cluster establishes exact identity between a strain and the cluster. NCBI `EXACT` grounding remains supported independently of the GTDB finding.

## Evidence

`data/raw/gtdb_mappings.tsv:1491` supplies the copied closeMatch and 38-genome count. Exact parsing of `gtdb_taxonomy` in the ignored-inclusive compressed catalog found 38 unique cluster assemblies: 34 assigned to NCBI taxon 33959, two to 153152, one to 909954 and one to 1037411. These are source assignments, not a declaration that those NCBI taxa are interchangeable.

The complete own row `data/catalog/gtdb_genomes-0014.jsonl.gz:19198` links `GB_GCA_000219475.3`, taxon 1037411, species taxon 33959 and strain pf01 to the placeholder cluster. It is not the representative. Other member identities include DPC 6026, GHZ10a, TCI250 and several metagenome-derived bins. Thus 38 is supported for the whole GTDB cluster, not for pf01 alone.

The full representative row `data/catalog/gtdb_genomes-0014.jsonl.gz:17880` is `GB_GCA_945980025.1`, an uncultured Lactobacillus metagenome-derived assembly, taxon 153152, BioSample `SAMEA110426465`, project `PRJEB53141`, and isolate `SRR15725434_bin.8_metaWRAP_v1.3_MAG`. Its accession-derived cluster name is not a culture designation or an exact synonym for pf01. Its habitat and assembly properties must not be transferred onto pf01.

The complete native assembly inventories and [live NCBI assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000219475.3,GCA_000219475.2,GCF_000219475.1/dataset_report) establish these version-specific distinctions:

- Current `GCA_000219475.3`, ASM21947v3, is a 1,973,006-base complete-genome-level assembly with three sequence components, BioSample `SAMN02469597`, project `PRJNA67469`, released 2017-11-13. The native row has no current paired RefSeq accession and carries the exclusion reason `missing tRNA genes`; the live response retains the same genome note. Complete-genome assembly level does not erase that qualification.
- Historical `GCA_000219475.1`, ASM21947v1, is suppressed, not live since 2012-01-28. Historical `GCA_000219475.2`, ASM21947v2, is replaced, not live since 2018-03-13. Both describe the earlier 1,882,804-base assembly and WGS master `AFQJ00000000.1`.
- Historical `GCF_000219475.1` pairs with GenBank .2, not current .3, and is suppressed, not live since 2018-03-16. A live request containing current and historical accessions returned only current GenBank .3. Historical statuses are supported by the inspected historical inventories, not inferred solely from API omission.

Do not interpret zero annotation counts in the current catalog as a genome with no genes; the row lacks an annotation provider and annotation date. Do not interpret the three sequence components as three different strain genomes.

BV-BRC `1037411.3` still links the older `GCA_000219475.2`, `AFQJ00000000`, the same BioSample and project. Preserve its original version and age rather than silently rewriting its evidence. GOLD's complete native chain is organism `Go0002278` to project `Gp0002278` to analysis `Ga0325189`, IMG 2860555079, explicitly pointing to `GCA_000219475.3` with sequence identifiers `CP024781`, `CP024782` and `CP024783`. The distinct source histories are compatible with one named strain, not additional current genomes.

The inventory-linked [PMID 21742886](https://pubmed.ncbi.nlm.nih.gov/21742886/) is the 2011 PF01 genome publication, DOI `10.1128/JB.05640-11`, PMCID `PMC3165652`. Its abstract identifies the strain and reports experimental biological properties. No phenotype was imported into this taxonomy-only record, and the 2011 article must not be assumed to describe the later 2017 assembly version or its current annotation.

`data/raw/madin_taxa.tsv:716` supports four `TRAIT_ASSERTION` inventory entries; the YAML does not enumerate four experimental outcomes. The NCBITAXON one-NAME attestation and 2026-09-13 snapshot note match the source. No units are summed across sources.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon ID, exact label, slug and pf01/PF-01 variants. Thirty-two source lines matched. Every native candidate identity and matching field was inspected; own rows and matched TSV rows were read in full. The cluster census was a separate exact structured-taxonomy check.

Unrelated PF01 candidates denote Staphylococcus aureus, Streptococcus agalactiae, Candidatus Brocadia, Klebsiella pneumoniae or a hot-spring microbial community. Their taxonomy and assembly identifiers are not pf01 evidence for this Lactobacillus record.

Complete own-taxonomy inventory scans found no BacDive, LPSN, GOLD, MediaDive or BactoTraits attestation row. The native GOLD organism does exist, but `conf/sources.yaml` distinguishes native workbook genome-link evidence from the transformed GOLD edges used to generate attestation counts. Without replaying those original edges, the different surfaces do not establish an additional missing-attestation defect.

Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly one target YAML, no prior target report and no target-specific history filename. These are bounded repository findings, not proof that further evidence cannot exist elsewhere.

`strain_count: 0` means zero represented inventory strains, not no biological isolate or genome. No eligible own culture-deposit join was established by the bounded search. Optional culture, genomic and graph slots need not be invented; the important correction is the over-scoped GTDB identity claim. iModulonDB is not applicable to the taxonomy and source-count assertions.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**Major: a GTDB species cluster is promoted to an exact pf01 strain identity.** YAML line 43 carries closeMatch; lines 52-55 make Lactobacillus sp945980025 an `EXACT_SYNONYM`; line 57 promotes the species identifier to identity xrefs. Lines 67-72 repeat the close mapping and unqualified 38-genome cluster count. Native metadata supports pf01's cluster membership but distinguishes it from the representative MAG and the other 37 assemblies. A cluster label without the strain designation cannot be an exact synonym for this strain. Thirty-eight is valid as a cluster count, not as a pf01 assembly count.

Owner: the maintained kg-microbe GTDB mapping consumed through `conf/sources.yaml` and `src/taxonmech/extract.py:501`, plus `src/taxonmech/seed.py:439` identity promotion and `src/taxonmech/seed.py:574` attestation generation. The seeder currently treats closeMatch as identity without checking rank compatibility. This is one grouped semantic defect, not separate findings for each emitted field. The supported NCBI identity is not a blocker.

## Recommended Edits

1. Distinguish strain membership from species identity in the upstream mapping and seeder. Do not promote a GTDB placeholder species into an exact strain synonym or identity xref solely because the input predicate is closeMatch. Retain the GTDB assignment as appropriately scoped evidence; do not discard it merely because its label differs from NCBI.
2. Retain 38 only with explicit species-cluster scope where the representation supports it. A strain-specific assembly count must be derived independently. Do not mechanically replace the predicate with broadMatch without checking edge direction, and do not force the cluster to equal the entire NCBI L. johnsonii species.
3. Add rank-aware and placeholder-cluster regression tests, then regenerate from maintained inputs under a separately authorized curation task. Preserve the two valid NCBI synonyms, the NCBI lineage, genetic code and complete source/version history. Do not edit the generated YAML or extracted TSV by hand.

No history append, curation event or status promotion is authorized by this review. Optional genomic enrichment must retain the current assembly's quality note and distinguish replaced/suppressed evidence.

## Follow-up Checks

Restore the pinned upstream inputs in `data/raw/MANIFEST.yaml` before replaying transforms. Test a named strain assigned to a placeholder GTDB species: membership should remain, but the species-only exact synonym and identity xref should not be generated. Test explicit cluster-count scope even when only one mapping exists, with rank-compatible species mappings as positive controls.

For an authorized fix, run `just seed`, the documented `just seed-canary NCBITaxon:1037411`, schema/strict/history checks, full `just verify-corpus`, tests and QC. The canary writes the record and was not run here. Manually inspect the semantic relationship and preserved NCBI/GTDB disagreement rather than relying only on schema validation.

Any further assembly enrichment must recheck current `GCA_000219475.3`, its RefSeq exclusion note and source-specific historical versions. Do not count GenBank .1/.2/.3 or suppressed RefSeq .1 as four current genomes, and do not borrow a culture identity from the representative MAG.

## Additional Notes

- YAML SHA-256 remained `3318e5990dab7b9edc104113a2cd964198ab73b3bc9f40ea0ded1629674e54ac`.
- `data/taxa/PATHS.tsv:15301` and `curation/seed_scope.tsv:36186` uniquely resolve the target. The 2026-09-13T17:54:04Z seed event exactly matches the GTDB/MADIN/NCBITAXON scope reason.
- Complete native assembly rows: `data/catalog/ncbi_genbank-0000.jsonl.gz:3735`, `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:1095` and `:1096`, and `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:1069`. Own BV-BRC is line 3452; GOLD organism/project/analysis rows are 2047, 2069 and 190452 respectively.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
