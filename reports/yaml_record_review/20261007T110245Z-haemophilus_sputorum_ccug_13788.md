# YAML Record Review: Haemophilus sputorum CCUG 13788

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/haemophilus_sputorum_ccug_13788.yaml`
- Started UTC: 2026-10-07T10:55:39Z
- Finished UTC: 2026-10-07T11:02:45Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035839`: rank STRAIN, domain BACTERIA, parent `NCBITaxon:1078480` (Haemophilus sputorum), ten root-first lineage entries, genetic code 11, EXACT grounding, and SEEDED mapping status. It carries one GTDB species mapping, four synonyms, a GTDB species xref, one BacDive strain with three deposits, seven source attestations, and one seed event.

The single strain is `kgmicrobe.strain:bacdive_11717`. Its nine assembly assertions, six other genome-record assertions, and 32 related-record assertions are separate evidence-bearing links, not 47 biological genomes. The target is indexed at `data/taxa/PATHS.tsv:14678` and scoped at `curation/seed_scope.tsv:7213`.

Generated YAML remains read-only. A future synonym correction belongs in the maintained seeder, not this file.

## Validation

- `just validate data/taxa/bacteria/haemophilus_sputorum_ccug_13788.yaml`: passed; no issues.
- `just validate-strict data/taxa/bacteria/haemophilus_sputorum_ccug_13788.yaml --out /private/tmp/haemoCcug13788-strict.tsv`: passed; one file, zero errors. The actual TSV contains only the header.
- Complete parsed backbone, lineage, synonym, scope, and attestation comparisons passed. Every one of the nine assembly, six genome-record, and 32 related-record entries matched its raw or StrainInfo inventory assertion, including nested deposit evidence. These are bounded source comparisons, not corpus reproduction.
- The local CAFI matcher accepts the complete CCUG 13788, DSM 24472, and NCTC 13537 identifiers and matches their existing deposit CURIEs.
- Live NCBI taxonomy, assembly, BioSample, BioProject, and four nucleotide-reference metadata checks were performed. The StrainInfo rich API record was also read in full.
- `just validate-products`: not applicable; there are no curator-added graph nodes. Carried NCBI lineage is not an OAK reconciliation target.
- `just validate-history`: not run; ignored-inclusive content and filename searches found no target-specific external history artifact. The embedded seed event was inspected.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, full-corpus schema validation, raw-provenance, generated-site, documentation-statistics, publication-budget, and vendored-sync gates.
- The whole target remained byte-identical to the initial read. No YAML, inventory, history, status, generated-page, or GitHub mutation was performed.

## Identity and Grounding

The pinned backbone row at `data/raw/ncbitaxon_taxa.tsv:222179` agrees with fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035839&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035839): the exact target is the CCUG 13788 strain, not the broader species. All ten lineage entries agree, including Pseudomonadati and Pasteurellales. The three NCBI synonyms preserve historical CCUG 13788 names, including the former parainfluenzae attribution; four native name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31665` through line 31668 support them.

[BacDive 11717](https://bacdive.dsmz.de/strain/11717), [CCUG 13788](https://www.ccug.se/strain?id=13788), and [DSM 24472](https://www.dsmz.de/collection/catalogue/details/culture/DSM-24472) corroborate the three collection deposits and identify this as the type strain of Haemophilus sputorum. CCUG retains a taxonomic remark about possible parahaemolyticus affinity; that historical uncertainty is not silently substituted for the NCBI identity.

The LPSN source row `data/raw/lpsn_names.tsv:26889`, `lpsn:789886`, maps to parent species 1078480, not strain taxid 1035839. The inspected [LPSN species page](https://lpsn.dsmz.de/species/haemophilus-sputorum) retains Haemophilus sputorum as the validly published correct name and lists CCUG 13788 and DSM 24472 as type deposits; it treats Pseudohaemophilus sputorum as a not-validly-published homotypic synonym. These species-level nomenclatural assertions should not become exact strain synonyms or a local lineage reconciliation.

The GTDB genome link is supported, but the GTDB species-cluster identity is broader than this strain. That distinction is the major finding.

## Evidence

- **Strain and deposit provenance:** `data/raw/bacdive_strains.tsv:11563` supplies BacDive 11717 and the three culture identifiers. The full primary projection at `data/bacdive/records.jsonl.gz:11562` includes both strain and species NCBI classifications, the type-strain indication, and source reference 66792 for GCA_000238795, PATRIC 1035839.4, and IMG 2513237309. The reference ID is a BacDive source reference, not a PMID.
- **NCBI assembly chain:** native GenBank `-0000.jsonl.gz:4484` and RefSeq `-0000.jsonl.gz:3811` explicitly pair GCA_000238795.2 with GCF_000238795.1. They share ASM23879v2, CCUG 13788, SAMN02393707, 87 contigs, and 2,143,543 bp. Fresh [NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000238795.2/dataset_report) confirms the current pair, strain, type-material annotation, sample, and GenBank project PRJNA67089. Different GenBank and RefSeq version suffixes are valid explicit source evidence, not a prefix-derived guess.
- **Samples and projects:** live BioSample SAMN02393707 names CCUG 13788 and type material; BioProject PRJNA67089 explicitly links the strain, assembly, and sample. PRJNA224116 resolves to the multispecies RefSeq annotation project, so it is contextual provenance, not another strain-specific sequencing experiment. The global project's identity/scope fields were inspected; its many unrelated secondary projects and locus-tag assignments were not individually reviewed.
- **GTDB classification:** native row `data/catalog/gtdb_genomes-0013.jsonl.gz:48081` names CCUG 13788 as the matching culture, uses `RS_GCF_000238795.1`, and supplies the explicit GenBank partner and BioSample. The row is the representative of `s__Haemophilus_A sputorum`. A complete exact-cluster census across the compressed GTDB genome shards found 12 distinct members, with identity projections inspected for all 12. They include HK 2154/GCF_000287615.1 and other isolates or metagenome-derived genomes, not only CCUG 13788. The 12-genome mapping count agrees with `data/raw/gtdb_mappings.tsv:1444` and `data/raw/gtdb_species.tsv:72266`.
- **BV-BRC and IMG:** full BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:3344` supports PATRIC 1035839.4, the versioned GenBank assembly, strain, sample, and project. IMG 2513237309 is independently carried by the BacDive genome row and the primary GOLD analysis. These are source assertions; their co-occurrence does not, by itself, prove cross-database sequence equivalence.
- **GOLD:** full rows at `data/gold/organisms.jsonl.gz:9907`, `projects.jsonl.gz:9771`, and `analyses.jsonl.gz:4443` establish Go0011280 -> Gp0011280 -> Ga0009663. The analysis' organism field is empty, but its explicit project resolves to the known organism. The analysis supplies unversioned GCA_000238795 and IMG 2513237309; the project supplies PRJNA67089 and SAMN02393707. Both culture-collection and strain fields independently match CCUG 13788 and are preserved as distinct assertions.
- **Other GOLD organism references:** Go0172189 and Go0172190 at organism lines 110461 and 110462 explicitly name DSM 24472 and NCTC 13537, respectively, with the older Haemophilus parainfluenzae classification, taxid 729. The generated related records preserve that disagreement. Their culture matches do not transfer the CCUG project's assembly through these separate organism rows.
- **StrainInfo:** native `data/straininfo/records.jsonl.gz:42252` and the live [SI-ID54522 rich API record](https://api.straininfo.dsmz.de/v2/data/strain/max/54522) agree on DOI 10.60712/SI-ID54522.3, published status, BacDive 11717, species-level source classification, and three available source deposits: SI-DP136301/CCUG 13788, SI-DP872035/DSM 24472, and SI-DP888822/NCTC 13537. Every asserted sequence explicitly names only SI-DP136301. The YAML correctly restricts those sequence links to CCUG 13788; neither group membership nor the BacDive cross-reference transfers them to the other deposits.
- **Nucleotide references:** live NCBI GenBank metadata verifies JF506642.1 (1,364-bp partial 16S), JF506666.1 (453-bp partial infB), JF506694.1 (393-bp partial pgi), and JF506721.1 (447-bp partial recA), all attributed to CCUG 13788/taxid 1035839 with type-material notes. Full source, feature, and citation metadata were inspected, excluding sequence payloads and translations. The YAML properly retains StrainInfo's unversioned accessions as nucleotide references outside genome counts.
- **Literature:** these four accessions cite PMID 22336150, DOI 10.1016/j.ijmm.2012.01.001. The [primary description's abstract](https://pubmed.ncbi.nlm.nih.gov/22336150/), retrieved through NCBI, explicitly identifies CCUG 13788, DSM 24472, and NCTC 13537 as the type strain. The abstract supports that identity and the study's sequence-based characterization; it does not support transferring all cohort phenotypes to every linked genome. Full article tables were not retrieved.
- **Attestations:** all seven sources, labels, counts, and units match the inventories: NCBITAXON 1 NAME, GTDB 12 GENOME, BACDIVE 1 STRAIN, MEDIADIVE 1 MEDIUM, GOLD 1 ORGANISM, MADIN 4 TRAIT_ASSERTION, and BACTOTRAITS 1 TRAIT_ASSERTION. [MediaDive 804 for this strain](https://mediadive.dsmz.de/medium/804?bacdive=11717) independently supports the one medium association. Original KGX edges for the aggregate source counts were unavailable in the configured checkout; individual Madin/BactoTraits assertions were not independently reconstructed.

## Completeness

The one listed BacDive strain is the entire target subtree inventory; no direct descendants were found. All 47 embedded links were compared field-for-field against `data/raw/strain_assemblies.tsv`, `strain_genome_records.tsv`, `strain_related_records.tsv`, and the StrainInfo assembly/related-record overlays. Source-supplied unversioned assembly identifiers remain unversioned. GOLD Go/Gp/Ga, SI-ID/SI-DP, BioSample, BioProject, and nucleotide references remain outside genome counts.

The target has no direct LPSN name row. Consequently its `nomenclature` and `is_type_strain` fields are not populated under the schema's same-taxon LPSN derivation rule. The type relationship is established for the parent species by the actual LPSN row and six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:5153` through line 5158. The missing optional flag on this strain-level record is not an assertion that the culture is non-type, nor a separate violation of the documented rule. A future explicit species-scoped type relationship would require a deliberate model change, not blindly inheriting species identity into this record.

The BacDive inventory's per-strain medium count is zero, whereas the taxon-level MediaDive inventory records one medium. The sources and aggregation paths differ, and the YAML makes no explicit zero-growth claim. Original per-strain KGX edges were unavailable; no unsupported negative interpretation or forced count rewrite is warranted.

Ignored and hidden files were included in searches with `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. The taxid, all three deposit designations, and record slug produced 87 rows, all read in full through structured JSON/TSV readers, including compressed files. Expanded accession/sample/project/GOLD/IMG/StrainInfo/WGS searches produced 78 rows: 64 were already inspected, and all 14 additional matches were checked using complete identity and matched-field projections. Those 14 are unrelated longer WGS identifiers containing the AFNK token, not this accession. The five `SOURCE.json` files were separately parsed in full for target names/IDs, and history/report filenames were checked independently of ignore rules.

No matching ATB sample row was found for SAMN02393707 in the bounded catalog search; the complete target strain/genome ATB overlays also contained no row. This supports the absence of an imported ATB association, not absence of all possible sequencing elsewhere. The initial ATB hit is an unrelated Staphylococcus aureus run ERR1035839; a separate unrelated assembly's ungapped-length value 1035839 is likewise not a taxonomic match.

The local `culturebotai-claw` runner was resolved and `kg-microbe-sources imodulondb datasets` was run through `uv run --offline --no-sync --project`. Its dataset catalog has no Haemophilus target, so iModulonDB was not applicable and no cross-organism gene-module inference was made. Optional phenotype and causal-graph slots need not be invented.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species name is asserted as an exact synonym of an individual strain.** The record's `Haemophilus A sputorum` synonym is typed `EXACT_SYNONYM` and attributed to `GTDB:s__Haemophilus_A_sputorum`. The NCBI target is strain 1035839, while that GTDB species cluster contains 12 genomes, including the separately named HK 2154 strain and other isolates. Being the cluster's representative does not make the representative strain identical to the species. The source species count and classification are supported; the exact-strain synonym is not. The maintained owner is `src/taxonmech/seed.py:450` and the promotion block through line 469: a supplied `skos:closeMatch` is treated as identity and promoted into xrefs/exact synonyms without a rank/scope guard. Its underscore-to-space conversion also does not preserve the literal suffixed GTDB genus token. This is one identity-promotion defect, not multiple counted findings. The upstream KGX predicate should be reviewed at its source; reproducibility of that predicate does not prove biological equivalence.

No blocker was found in the NCBI identity or the inspected strain-genome evidence chains. No independent minor defect was established. Unavailable source endpoints are limitations, not extra findings.

## Recommended Edits

1. In `src/taxonmech/seed.py`, prevent GTDB species mappings from becoming exact synonyms or identity xrefs of strain-level or otherwise narrower NCBI taxa without scope-compatible identity evidence. Retain this strain's three supported NCBI designation synonyms. Preserve the original GTDB classification, accession-level links, predicate provenance, and 12-member cluster count without presenting species membership as strain equivalence.
2. Add a regression in `tests/test_seed.py` covering an infraspecific target that is the representative of a larger GTDB species cluster and has an upstream closeMatch. Confirm that representation status does not bypass scope checks; retain existing species-level and pooled-mapping behavior. Preserve suffixed GTDB labels when carrying source names.
3. Route any correction to the upstream mapping predicate to kg-microbe, rather than silently rewriting the supplied predicate in generated YAML. Do not alter the carried NCBI lineage or erase GOLD's historical classification differences.
4. During an authorized implementation, run the seed dry run, then `just seed-canary NCBITaxon:1035839`, and inspect the resulting canary before broader regeneration. This review authorizes neither that write nor a review-status/history promotion.

## Follow-up Checks

- Run `uv run pytest tests/test_seed.py` with the new rank/scope and suffixed-label cases.
- Repeat focused schema and strict validation after regeneration. Confirm the species-as-strain exact synonym is removed while all three NCBI synonyms and all 47 evidence-bearing links are preserved.
- Recheck the GTDB membership census and representative accession separately from species identity. The count of 12 must not become a count of genomes established for the individual strain.
- Recheck the StrainInfo sequence deposit IDs: the assembly and four nucleotide references must remain associated only with SI-DP136301.
- Run the documented full-corpus reproduction and QC gates before accepting a seeder change; they were not run here.
- For unresolved source availability, retry GTDB, BV-BRC, GOLD, and IMG native web records and retrieve the manifest-pinned KGX edges if exact original aggregate assertions are needed. No current-database availability or cross-database sequence-equivalence claim should be inferred from this report alone.

## Additional Notes

The historical native GenBank record GCA_000238795.1 is suppressed; the current record correctly uses source-supplied GCA_000238795.2 and GCF_000238795.1 alongside explicitly unversioned assertions. Absence of a version suffix in BacDive, GOLD, or StrainInfo must not be silently converted to the obsolete .1 or today's .2.

BioSample metadata describes a Denmark/Aarhus location, whereas the collection catalogs and StrainInfo describe Swedish sample origin. These are retained as source-context differences, not collapsed into a newly curated isolation statement. The YAML does not assert an isolation location. Likewise, GTDB's Enterobacterales placement and suffixed Haemophilus_A genus do not replace NCBI's Pasteurellales/Haemophilus lineage.

GTDB, BV-BRC, GOLD, and IMG native web endpoints were inaccessible through the web tool; complete relevant pinned native rows were available. The StrainInfo web/DOI frontends were inaccessible, but the source's rich API succeeded and directly confirmed the DOI and deposit evidence. NCBI PubMed API retrieval succeeded after its web frontend was uninformative. The full publisher article returned HTTP 403; only the primary abstract and sequence citation metadata support the literature statements.

The configured kg-microbe checkout had no files under the searched gold, gtdb, madin_etal, bactotraits, or mediadive transform directory patterns, including ignored/hidden files. This bounds the original-edge verification limitation; it is not a global claim that the datasets do not exist.

The 2026-09-13T17:54:04Z embedded seed event matches the latest contributing inventory timestamp (ATB); raw and StrainInfo manifests are earlier. All seven source names and the scope reason agree. Status remains SEEDED.

Exactly one new timestamped review report was added for this target. Existing reports, records, inputs, history, branches, and worktrees were left untouched.
