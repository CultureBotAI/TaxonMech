# YAML Record Review: Aggregatibacter actinomycetemcomitans Y4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aggregatibacter_actinomycetemcomitans_y4.yaml`
- Started UTC: 2026-10-06T14:26:30Z
- Finished UTC: 2026-10-06T14:32:58Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1035194`, label `Aggregatibacter actinomycetemcomitans Y4`, rank STRAIN, domain BACTERIA. The entire YAML was read before findings and checked byte-for-byte unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED with ten root-first ancestors, one GTDB mapping, four synonyms, one equivalent xref, genetic code 11, one BacDive strain with three culture identifiers, six source attestations and one inline seed event. Its nested strain has two assembly assertions, three genome-record assertions and 25 related-record assertions. These are source assertions, not counts of distinct biological genomes. Only this new review report is written.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/aggregatibacter_actinomycetemcomitans_y4.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/aggregatibacter_actinomycetemcomitans_y4.yaml --out /private/tmp/aay4-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: pinned identity, aliases, all ten lineage entries, genetic code, six source counts, scope and seed provenance agree. Complete native and transformed rows were inspected for the nested links. This is not a focused corpus-reproduction validator.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- No curator-added ontology graph nodes require term validation. The documented product checker excludes taxonomy fields and delegates them to corpus reproduction.
- No separate target history artifact was found by the ignored-independent history filename search. Inline history passed schema validation and agrees with scope provenance. No external history validator was run against an invented artifact.
- The StrainInfo dataset DOI, BacDive reference 66792, source accessions and deposit relationships were checked as described below. No additional record-specific citation validator is documented in the inspected commands.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221917`, inspected [live NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035194&retmode=xml), and [NCBI taxonomy dataset response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035194) agree on the strain identity, parent species `NCBITaxon:714`, three aliases and genetic code 11. All ten root-inclusive ancestor identifiers agree; pinned labels/ranks match the YAML, and live XML confirms the non-root lineage. No children, exact type-material entry, merged-ID entry or dropped entry were found in their pinned structured tables.

The [BacDive strain page](https://bacdive.dsmz.de/strain/11754) and native record identify Y4 and the three listed deposits: ATCC 43718, DSM 11123 and JCM 8578. The [ATCC authority page](https://www.atcc.org/products/43718) explicitly identifies Y4 and says it is not a type strain. The [JCM authority page](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=8578) independently traces JCM 8578 to ATCC 43718 and Reynolds Y4, links BacDive 11754, and lists both 16S accessions present in the record.

The [LPSN species page](https://lpsn.dsmz.de/species/aggregatibacter-actinomycetemcomitans), record 785424, concerns the validly published species and its type, including ATCC 33384 and DSM 8324, not Y4. Its exact raw row at `data/raw/lpsn_names.tsv:23348` maps to parent taxid 714. The lack of a type flag and species-level nomenclature entry on this strain is appropriate. Historical Actinobacillus and Haemophilus names in sequence titles are preserved source nomenclature, not evidence for different deposits.

GTDB's native classification uses Enterobacterales while the carried NCBI lineage uses Pasteurellales. These are source-specific classifications. No local reconciliation or lineage replacement is justified. The unsupported promotion of GTDB species membership to exact strain equivalence is the major finding below.

## Evidence

- NCBI: complete native rows at `data/catalog/ncbi_names-0005.jsonl.gz:31375` through 31378 support the scientific name and three aliases. The ATCC name has native class synonym; the str. Y4 and strain Y4 names are equivalent names. The attestation is one NAME, not a count of aliases.
- GTDB: `data/catalog/gtdb_genomes-0002.jsonl.gz:17938` places RS_GCF_000318155.1 in the A. actinomycetemcomitans species cluster and marks it as not the representative. `data/raw/gtdb_species.tsv:5994` and mapping line 1421 carry 167 cluster genomes. The same cluster maps to parent taxid 714 at mapping line 305016 and to other strain taxa. The extraction owner at `src/taxonmech/extract.py:501` counts genome-to-species edges; 167 is not a Y4 genome count.
- BacDive: `data/raw/bacdive_strains.tsv:11600` and the complete native record at `data/bacdive/records.jsonl.gz:11599` support strain ID `kgmicrobe.strain:bacdive_11754`, designation Y4, all three deposits and one STRAIN assertion. The native record explicitly says non-type. Raw culture-collection rows 5524, 62643 and 112311 retain the same taxid.
- MediaDive: `data/raw/mediadive_taxa.tsv:121` supports five MEDIUM assertions, with source identifiers 215, 693, J14, J156 and J84. These are separate from the BacDive inventory's zero medium count; neither field establishes a phenotype or mechanism by itself.
- MADIN and BactoTraits: `data/raw/madin_taxa.tsv:670` and `data/raw/bactotraits_taxa.tsv:92` each support one TRAIT_ASSERTION. The counts do not specify experimental outcomes.
- Scope: `data/taxa/PATHS.tsv:14408` and `curation/seed_scope.tsv:10799` identify this target. Its six-source reason and 2026-09-12 scope date agree with the inline seed event of 2026-09-13T17:54:04Z. There is no exact target row in the transformed GOLD taxon-attestation inventory; that does not invalidate separately imported native GOLD strain links.

The two assembly and three genome-record assertions reproduce `data/raw/strain_assemblies.tsv:8121` and 8122, and `data/raw/strain_genome_records.tsv:6227` through 6229:

- BacDive reference 66792 supplies unversioned GCA_000318155, IMG 2537561947 and BV-BRC/PATRIC 1035194.3 under the exact source fields recorded in the YAML. The live BacDive reference list identifies 66792 as automatic DiASPora annotation, not a strain-specific experimental paper. The source spelling and unversioned accession should remain source-faithful.
- GOLD's complete native chain is `Go0011041 -> Gp0011041 -> Ga0016256`, inspected at `data/gold/organisms.jsonl.gz:9694`, `data/gold/projects.jsonl.gz:9560` and `data/gold/analyses.jsonl.gz:9785`. Explicit ATCC 43718 matches the existing deposit. The chain supports versioned GCA_000318155.1, IMG 2537561947, PRJNA67199 and SAMN02436929. An empty analysis-level organism field does not conflict with its explicit project-to-organism join.
- Native GenBank and RefSeq rows at `data/catalog/ncbi_genbank-0000.jsonl.gz:8020` and `data/catalog/ncbi_refseq-0000.jsonl.gz:6886`, and the [live assembly dataset response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000318155.1/dataset_report), confirm current GCA_000318155.1 and GCF_000318155.1: 121 contigs, 87 scaffolds and 2,186,501 bp. Assembly comments explicitly identify ATCC 43718 as supplied material.
- Complete [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN02436929&retmode=xml) identifies Y4, ATCC:43718, a human host and subgingival oral plaque. These are sample-level facts, not a clinical phenotype. The [BioProject page](https://www.ncbi.nlm.nih.gov/bioproject/67199) independently connects the monoisolate project, assembly, sample, AMEN WGS master, GOLD Gp0011041 and IMG 2537561947.
- The live assembly response reports ANI status OK / species_match, with 97.8% identity against a DSM 8324 type assembly. This computational comparison does not make Y4 the nomenclatural type or merge its strain identity with the species.
- `data/bvbrc/bvbrc-0000.jsonl.gz:3316` corroborates PATRIC 1035194.3, the same GenBank assembly, project and sample. Repeated IMG assertions preserve independent BacDive and GOLD provenance; they are not extra genomes.

All nine GOLD related-record assertions reproduce `data/raw/strain_related_records.tsv:24140` through 24148. In addition to the ATCC chain, `data/gold/organisms.jsonl.gz:113207` and 113209 support DSM 11123 / Go0174947 and JCM 8578 / Go0174949. Each deposit has separate culture-collection-field and strain-field assertions. Their source taxid 714 is correctly retained; exact culture identity, not a forced taxid rewrite, establishes the link.

All sixteen StrainInfo related assertions and the three eligible deposit links reproduce `data/straininfo/related_records.tsv.gz:14858` through 14873 and `data/straininfo/strain_links.tsv:5705` through 5707. The complete native `data/straininfo/records.jsonl.gz:30236` supplies SI-ID 42003, published-online status, available deposits and their identifiers. ATCC 43718 is SI-DP 113048, DSM 11123 is 162502, and JCM 8578 is 184241. Each sequence retains its explicit deposit association; no sequence is transferred merely because it shares the StrainInfo group.

The [DataCite DOI response](https://api.datacite.org/dois/10.60712/SI-ID42003.2) verifies dataset `10.60712/SI-ID42003.2`, version 2, issued 2025-02-25, DSMZ publisher, four deposits, active/findable state and a StrainInfo 42003 landing URL. The landing request returned HTTP 200, but only its response headers and byte count were inspected. Its dynamic record content was not treated as live evidence; deposit and sequence details were checked in the complete pinned native record.

Current NCBI Nuccore GenBank XML metadata were retrieved and read for all ten asserted nucleotide accessions. Every returned version is .1. The record correctly preserves its source's unversioned identifiers rather than silently assigning a version:

| Accession | Inspected scope and deposit support |
| --- | --- |
| [AB015936](https://www.ncbi.nlm.nih.gov/nuccore/AB015936) | 1,464 nt; complete omp34 coding region; source ATCC 43718, taxid 1035194. |
| [AB071169](https://www.ncbi.nlm.nih.gov/nuccore/AB071169) | 748 nt; complete flp coding region; source ATCC 43718, taxid 1035194. |
| [AB595137](https://www.ncbi.nlm.nih.gov/nuccore/AB595137) | 1,501 nt; partial 16S rRNA; source JCM 8578, taxid 714; SI-DP 184241. |
| [AF319465](https://www.ncbi.nlm.nih.gov/nuccore/AF319465) | 1,023 nt; complete cagE coding region; ATCC 43718 / Y4 source and culture cross-reference, taxid 1035194. |
| [AY362884](https://www.ncbi.nlm.nih.gov/nuccore/AY362884) | 1,362 nt; partial 16S rRNA; ATCC 43718, serotype b, taxid 1035194. |
| [AY362930](https://www.ncbi.nlm.nih.gov/nuccore/AY362930) | 520 nt; partial rpoB coding region; ATCC 43718, serotype b, taxid 1035194. |
| [S44313](https://www.ncbi.nlm.nih.gov/nuccore/S44313) | 1,010 nt; 23S rRNA; title explicitly identifies ATCC 43718 / FDC Y4. Its source feature has serotype b and taxid 714 but no strain qualifier. |
| [U26968](https://www.ncbi.nlm.nih.gov/nuccore/U26968) | 1,881 nt; complete htpG coding region; source FDC Y4 / ATCC 43718, taxid 1035194. |
| [U66056](https://www.ncbi.nlm.nih.gov/nuccore/U66056) | 1,148 nt; IRP35 coding region; source ATCC 43718, taxid 1035194. |
| [X54632](https://www.ncbi.nlm.nih.gov/nuccore/X54632) | 1,010 nt; partial 23S rRNA; source ATCC 43718, taxid 1035194. |

The nine ATCC-associated sequences have explicit native SI-DP 113048 associations. For S44313, this and the explicit sequence title establish the link; an absent source-feature strain qualifier was not invented. ATCC independently lists S44313, X54632, U26968 and U66056. The ten accessions are typed NUCLEOTIDE_SEQUENCE related records, not whole-genome identifiers. GenBank metadata and bibliography were inspected, but their cited experiments and article full texts were not independently reviewed. No mechanism or phenotype claim is inferred from a gene title, protein annotation or citation list.

## Completeness

`strain_count: 1` agrees with the one BacDive strain at this exact taxid and absence of descendants under the subtree rule in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`. It is not a statement about the number of deposits or genomes. The three-deposit BacDive inventory explains the current eligible join keys.

Native StrainInfo also contains available, non-type CCUG 37001 / SI-DP 126422 in the same group; the live BacDive StrainInfo section displays this additional deposit. The expanded source search found `data/gold/organisms.jsonl.gz:113206`, Go0174946, explicitly naming CCUG 37001 at species taxid 714. This is a supported future enrichment lead, not an existing BacDive culture key that the importer silently dropped. Adding it requires a provenance-qualified maintained culture inventory/source change; do not transfer all group members or their sequences automatically.

The absence of additional NCBI_ASSEMBLY, GTDB or BV-BRC assertions is explainable under the guarded whole-deposit join: their native assembly-summary/strain fields contain bare Y4, while the NCBI importer at `src/taxonmech/ncbi_assemblies.py:90` does not import the richer BioSample culture field. Live ATCC:43718 support is useful for a future evidence-aware enhancement, not permission to join every bare Y4 name. Existing BacDive and GOLD links already carry the assembly. RefSeq availability does not establish a missing required nested assertion under the present importer contract.

The ignored-independent source expansion found no exact SAMN02436929 ATB row. No genome or FASTA was inferred from species names. The structured `imodulondb datasets` adapter completed before open-ended follow-up; none of its 28 returned datasets covers Aggregatibacter. iModulonDB is not applicable, not negative biological evidence. Optional definition, experimental phenotype and causal-graph slots can remain empty.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species concept is promoted to exact strain identity.** The record emits `GTDB:s__Aggregatibacter_actinomycetemcomitans` as an equivalent xref and the species name as an EXACT_SYNONYM on strain taxid 1035194. The native genome and cluster rows support Y4's membership in a 167-genome species cluster, not equality of that cluster with Y4. LPSN assigns the species to parent taxid 714. This violates the true-equivalence contract in `src/taxonmech/schema/taxonmech.yaml:180`. The maintained local owner is rank-insensitive promotion in `src/taxonmech/seed.py:449`; regression coverage belongs in `tests/test_seed.py`. The upstream kg-microbe closeMatch producer also needs rank- and direction-aware review. Mapping, synonym and xref manifestations are one finding.

Blockers: None found. Minor findings: None found. The NCBI identity and inspected nested links are supported. Source taxid differences, historical sequence nomenclature, repeated provenance assertions and the fourth-deposit enrichment lead are not separate identity defects.

## Recommended Edits

1. Make GTDB identity promotion in `src/taxonmech/seed.py` rank-aware. Preserve supported source classification and cluster counts without creating an equivalent species xref or exact species synonym on a strain.
2. Review rank and relation direction in the upstream kg-microbe mapping producer; do not mechanically replace closeMatch with a guessed broad/narrow predicate. Keep the NCBI lineage and GTDB classification separately attributable.
3. Add a strain-versus-species regression in `tests/test_seed.py`, retaining genuine species equivalences. Regenerate through maintained extraction/seeding inputs after an authorized fix; do not patch this generated YAML or raw tables manually.
4. Preserve all three listed culture identifiers, the explicit GOLD organism/project/analysis chain, deposit-specific StrainInfo evidence and source taxids. Keep BacDive's unversioned GCA accession distinct from GOLD's versioned assertion, and gene/rRNA accessions distinct from genome records.
5. Treat CCUG 37001 and BioSample-backed RefSeq enrichment as optional follow-up work. Any extension belongs in maintained source/inventory integration and guarded joins, including `src/taxonmech/genome_sources.py` and `src/taxonmech/ncbi_assemblies.py` where applicable, with provenance and conflict tests. Do not weaken whole-authority/accession matching to accept bare Y4.

## Follow-up Checks

- After an authorized rank-aware change, run `uv run pytest tests/test_seed.py` and the target's documented schema and strict commands.
- Confirm removal of unsupported species identity assertions while preserving the strain ID, ten ancestors, three NCBI aliases, genetic code, six attestations and all supported nested source assertions.
- Run actual full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc` after regeneration. Manual source comparisons do not replace those gates.
- Retry the GTDB species page and record its release before a classification update; the live tree endpoint was unavailable in this review. Pinned native metadata support the present bounded classification assessment.
- Before optional culture or genome enrichment, recheck source versions, CCUG deposit provenance, current assembly status and exact BioSample relationships. Require deposit-specific sequence evidence and do not infer genome equivalence from a shared label or species taxid.
- Any future phenotype or mechanism curation needs separately inspected, claim-specific experimental evidence. Sequence descriptions and aggregate source counts are insufficient.

## Additional Notes

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial pattern covered taxid 1035194, Aggregatibacter/Actinobacillus/Haemophilus actinomycetemcomitans with Y4 separator variants, ATCC 43718, DSM 11123, JCM 8578, BacDive 11754, the StrainInfo DOI and target slug. It returned 59 candidate rows. Expansion with observed source identifiers, CCUG 37001 and all ten sequence accessions returned 35 rows, adding one distinct GOLD organism row. All 60 distinct candidates were read in full using lossless structured decoding, including compressed files. Separate exact scans covered GTDB cluster/mapping rows, LPSN, backbone/status tables and scope. Five SOURCE.json files were searched structurally and history filenames checked separately. Absence findings are bounded to those sources, including ignored files; bare Y4 across unrelated organisms was not treated as a matching identity.

The structured adapter command was `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. NCBI APIs, BacDive, LPSN, ATCC, JCM and DataCite checks succeeded. The DOI browser route and GTDB tree had access errors; DataCite independently verified the DOI, and the StrainInfo landing URL subsequently returned HTTP 200 without its dynamic contents being reviewed.

No source/YAML/generated-page edits, history events, review-status promotions, paid research, outbound contact or Git/GitHub mutations were performed. Eukaryota reviews were not reopened.
