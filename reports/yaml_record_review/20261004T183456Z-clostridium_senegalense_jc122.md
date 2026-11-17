# YAML Record Review: Clostridium senegalense JC122

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/clostridium_senegalense_jc122.yaml`
- Started UTC: 2026-10-04T18:31:38Z
- Finished UTC: 2026-10-04T18:34:56Z
- Verdict: needs curation

## Target

The complete 81-line generated TaxonRecord was read. It denotes `NCBITaxon:1033737`, Clostridium senegalense JC122, at STRAIN rank in BACTERIA, with species parent `NCBITaxon:1465809`. Grounding is EXACT and lifecycle status is SEEDED.

An ignored-inclusive identifier search across `data/taxa/` resolved only this target. The parent species YAML was also read in full as context for strain/genome placement, not assigned a second review verdict. This report does not alter either record, generated inventories, prior reports, or curation history.

## Validation

Both documented single-record validators passed:

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/clostridium_senegalense_jc122.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/clostridium_senegalense_jc122.yaml`: exit 0, one file, zero errors; standard diagnostic output at `reports/instance_validation_failures.tsv`.

Manual structured comparisons checked the entire backbone lineage, source names, mapping row, attestations, scope reason, and related native evidence. These checks do not replace corpus reproduction.

Skipped: full-corpus `just verify-corpus`, `just qc`, `just provenance-check`, tests, rendering, and all-reference/history gates. No documented single-record corpus-reproduction substitute was invented. The record has no causal graph applicable to `validate-products`; live NCBI verification addressed taxonomy identity. An ignored-inclusive history search found no target-specific standalone event, so none was submitted to the history validator. The embedded seed event was schema-validated and compared with the scope row and manifest timestamps.

## Identity and Grounding

The pinned backbone row `data/raw/ncbitaxon_taxa.tsv:221302` and live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033737&retmode=xml) agree on identifier, strain label, rank, parent, and genetic code 11. All ten root-first ancestor entries match the pinned parent chain. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033737) confirms the complete lineage identifiers and strain rank. The taxonomy browser was inaccessible through the web tool, but both structured responses were inspected.

The NCBI exact synonym Clostridium sp. JC122 is source-supported. It denotes this strain, unlike the GTDB species synonym discussed below. No child, merged-ID, or dropped-record row affecting this target was found in the inspected structured tables.

[LPSN 790107](https://lpsn.dsmz.de/species/clostridium-senegalense) denotes the parent species, lists JC122 with DSM 25507 and CSUR P152 as type material, and records the 2015 validly published name. Its raw mapping is to `NCBITaxon:1465809`, not the child strain. The child's absent nomenclature entry is therefore not evidence of missing species-name ingestion.

## Evidence

### Record-Level Inventories

| Evidence | Inspected location | Result |
| --- | --- | --- |
| NCBI backbone | `data/raw/ncbitaxon_taxa.tsv:221302` | Strain identity, parent, code 11, NCBI synonym |
| GTDB mapping | `data/raw/gtdb_mappings.tsv:1364` | closeMatch to the source species, cluster count 5 |
| GTDB species inventory | `data/raw/gtdb_species.tsv:43121` | Same source cluster, count 5 |
| Madin inventory | `data/raw/madin_taxa.tsv:626` | 5 trait assertions for this strain taxon |
| Record index | `data/taxa/PATHS.tsv:13755` | Correct identifier-to-slug mapping |
| Scope | `curation/seed_scope.tsv:36148` | Three-source scope reason |
| BacDive/LPSN/GOLD/MediaDive/BactoTraits direct taxon tables | Full exact-target scans | No directly filed target row |

The NCBI count is one name; Madin counts five source assertions, not five strains or a validated trait narrative. The GTDB count is the source species' data volume. Its value is correctly reproduced even though the inferred identity relationship is not.

### Complete GTDB Cluster Check

All 901,341 native GTDB catalog records were scanned, and all five full objects in the relevant cluster were inspected:

| GTDB genome | Source strain/isolate | NCBI taxon |
| --- | --- | --- |
| RS_GCF_000285575.1 | JC122T | 1033737 |
| RS_GCF_010692705.1 | AGRFS4 | 1465809 |
| RS_GCF_018916625.1 | N2 | 1465809 |
| RS_GCF_001573875.1 | ATCC 25772 | 1676991 |
| RS_GCF_902374755.1 | MGYG-HGUT-01407 | 1465809 |

There are five distinct accession strings: one assigned to the target strain, three to its parent species, and one to Clostridium sp. ATCC 25772. JC122 is the representative, but a representative genome does not make a species identical to its strain.

The full mapping inventory also contains closeMatch rows from the same cluster to the parent species at line 31613 and to `NCBITaxon:1676991` at line 48653. Thus the claimed one-to-one species identity cannot be inferred merely from the imported predicate. This review does not adjudicate the separate parent or ATCC taxon records.

The live [GTDB taxon page](https://gtdb.ecogenomic.org/tree?r=s__Clostridium_J_senegalense) was inaccessible; the membership/count conclusion is explicitly based on the inspected pinned catalog.

The schema defines `TaxonomyMapping.genome_count` as assemblies classified under the source taxon. Therefore five is a supported cluster total and should not be blindly replaced by one. It must not be presented as five JC122 genomes or used to infer strain equivalence.

### Culture and Genome Context

[BacDive 2859](https://bacdive.dsmz.de/strain/2859), its full native object at `data/bacdive/records.jsonl.gz:2758`, and `data/raw/bacdive_strains.tsv:2759` classify the culture at the parent species while retaining JC 122/JC122 and DSM 25507/CSUR P152. Its sequence fields independently name the child strain taxon. The [DSMZ deposit page](https://www.dsmz.de/collection/catalogue/details/culture/DSM-25507) corroborates the culture designation, deposits, type role, JF824801, and the CAEV genome project.

The parent YAML already embeds this BacDive strain and its evidence. Its source assertions distinguish:

- BacDive's unversioned GCA_000285575, IMG 2597489894, and BV-BRC/PATRIC 1033737.3 under reference 66792.
- GOLD's versioned GCA_000285575.1 and IMG 2597489894 through the exact chain DSM 25507 -> Go0017286 -> Gp0017286 -> Ga0039963.
- Project PRJEA70833 and BioSample SAMEA2272503 as related records, not genomes.

The full GOLD organism, sequencing-project, and analysis objects at native rows 14777, 14308, and 25264 support that chain. The analysis's direct organism field is blank, but its project resolves the organism without conflict. The full BV-BRC 1033737.3 object independently records JC122, GCA_000285575.1, the same sample/project, and the child taxonomy.

Both pinned GenBank/RefSeq objects and the live [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000285575.1/dataset_report) confirm the current paired GCA/GCF_000285575.1 assembly from type material, assigned to `NCBITaxon:1033737`. Exact-taxon Assembly ESearch returned one assembly family. The live type-assembly ANI response marks taxonomy OK; its below-threshold comparison to another species is not a misidentification verdict.

The full StrainInfo native object at `data/straininfo/records.jsonl.gz:297987` supports SI-ID400098, SI-DP906936, DOI `10.60712/SI-ID400098.2`, DSM 25507, the parent taxonomy, and the BacDive cross-reference. It has no sequence array. Its own deposit/strain references on the parent are not additional genome assertions. This was a pinned-source verification, not a claim to have inspected the live rich API.

### Marker and Literature

Live [JF824801.1](https://www.ncbi.nlm.nih.gov/nuccore/JF824801.1) is a 1,462-base partial 16S sequence whose source feature explicitly identifies JC122, `taxon:1033737`, and type material of the parent species. Its bibliography supplies PMID 23408737 and DOI 10.4056/sigs.2766062 for the species description.

The inspected [species description](https://link.springer.com/article/10.4056/sigs.2766062) links JC122 to DSM 25507/CSUR P152 and the CAEV project. It supports the specific strain context, not equivalence between JC122 and every member of the GTDB species. Physiological experiments were not generalized into new record claims.

## Completeness

`strain_count: 0` faithfully reflects the direct/subtree BacDive classification inventory: the child has no direct BacDive strain and no descendants. The generator gathers descendants, not ancestors. The culture and its genome links are present on the species record, so this is not evidence that no culture or genome exists.

A future explicit association could improve navigation from the strain taxon to the parent-hosted culture. That would require a maintained, provenance-aware rule; simply copying all parent strains downward would be incorrect. No such relationship was invented in this review.

Ignored-inclusive compressed searches covered raw inventories, native catalogs, BacDive, BV-BRC, GOLD, SeqCode, StrainInfo, ATB, curation, and history. Both target and parent identifiers, labels, and JC122 were included. SOURCE.json files initially excluded from the content scan were checked separately with recursive structured traversal. No target-specific manifest values were found in the searched manifests. Absence statements here are bounded to those local surfaces.

An exact ignored-inclusive scan of `data/atb/` and the full compressed AllTheBacteria catalog found no SAMEA2272503 or local BacDive 2859 row. Other species-labelled ATB samples were found, including AGRFS4's SAMN14052883 and two other sample IDs. Their species names do not supply a JC122 sample link.

The native SeqCode name entry is species-level context, not another strain or genome identity. No required causal graph, experimental trait narrative, or transcriptomics representation is missing. iModulonDB is not applicable to this record's claims.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: GTDB species membership is promoted to strain equivalence.** Target lines 43 and 67 carry closeMatch; lines 46-49 add a GTDB EXACT_SYNONYM; line 54 adds an equivalence xref. The target is a strain, whereas the source concept is a five-genome species spanning three NCBI taxon identifiers. The schema reserves xrefs for true equivalences and describes closeMatch as the same species. The correct NCBI identity remains intact, so this is scope inflation rather than a wrong primary identifier.

The source relationship comes through the configured kg-microbe GTDB transform and `src/taxonmech/extract.py:501`. Local amplification occurs in `src/taxonmech/seed.py:451`, which treats any closeMatch as identity and then emits an exact synonym and xref. The fix belongs to those maintained transformations, not the generated YAML. The valid cluster count of five is not a second finding.

## Recommended Edits

1. Review the upstream GTDB-to-NCBI edge with explicit rank and relationship direction. Preserve evidence that JC122 belongs to the source species, but do not describe the two concepts as equivalent. A source-side narrower-target relation would need the appropriately directed predicate and documented treatment, not an automatic switch to broadMatch.
2. Guard local identity promotion in `src/taxonmech/seed.py` against species-to-strain mappings. Remove the derived GTDB exact synonym/xref through regeneration while preserving the source assertion and genuine NCBI synonym.
3. Qualify any retained GTDB count as source-cluster data volume. Preserve five for the cluster and distinguish the one exact strain-assigned catalog member; do not silently change count semantics.
4. Consider an explicit strain-taxon-to-culture association separately, with evidence from the existing genome/deposit chain. Preserve BacDive's parent classification and do not copy parent-only genome, medium, or nomenclature claims into the child.
5. After approved changes, refresh affected inventories and follow the documented seed dry-run/canary workflow. Do not hand-edit target YAML, source snapshots, or historical seed events.

## Follow-up Checks

- Add a regression fixture where a species cluster contains the representative strain plus genomes assigned to a parent species and another NCBI taxon. Assert no species-to-strain equivalence synonym/xref is generated.
- Check relationship direction and notes in both taxonomy_mappings and source_attestations. Preserve the NCBI identifier, rank, lineage, code, and true exact synonym.
- Recheck cluster counts against all five native objects and retain the source count's documented semantics.
- Keep parent-hosted BacDive/GOLD/StrainInfo assertions intact, including accession versions and typed related records.
- Rerun both record validators after changes, followed by full corpus reproduction, provenance, tests/QC, and rendering gates for shared-transform changes.
- Revisit the unavailable live GTDB page before claiming verification against a newer live release. No access failure invalidates the inspected pinned membership evidence.

## Additional Notes

The scope reason and three-source seed history match `curation/seed_scope.tsv:36148`. The seed timestamp equals the newest of the raw, ATB, and StrainInfo manifest extraction timestamps. No reviewed status or curation event was added.

The inspected LPSN display also includes an accession-like extra type designation, JF82824801, while its marker field and NCBI use JF824801. That source inconsistency is not present as a child-record claim and was not imported as a deposit. The paper's isolation date and the sequence submission chronology were not used to rewrite source history.

The parent record was examined only to resolve evidence placement for this target. This report is one completed strain-record review, not a verdict on the whole species or all sibling strains.

