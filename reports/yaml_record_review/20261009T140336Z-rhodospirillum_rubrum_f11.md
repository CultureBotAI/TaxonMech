# YAML Record Review: Rhodospirillum rubrum F11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhodospirillum_rubrum_f11.yaml`
- Started UTC: 2026-10-09T14:00:03Z
- Finished UTC: 2026-10-09T14:03:36Z
- Verdict: needs curation

## Target

The entire 84-line generated `TaxonRecord` for `NCBITaxon:1036743`, Rhodospirillum rubrum F11, was read. It is a bacterial `STRAIN` under species `NCBITaxon:1085`, not the species itself or wild-type ATCC 11170. The YAML contains ten root-first ancestors, one GTDB mapping, three synonyms, one GTDB xref, genetic code 11, zero emitted BacDive strains, three source attestations and one seed event. Its statuses remain `EXACT` and `SEEDED`.

The target's SHA-256 before and after review was `e10b71dd68bf4cf2bdd4d6c9a9c7d076a84ec4cdc87642280b9c8396e058ae4f`. This review writes only this new report, not a correction to the generated YAML.

## Validation

With `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`, both commands exited zero:

```bash
just validate data/taxa/bacteria/rhodospirillum_rubrum_f11.yaml
just validate-strict data/taxa/bacteria/rhodospirillum_rubrum_f11.yaml --out /private/tmp/taxonmech-rrubF11-review-strict.tsv
```

LinkML found no issues. Strict validation scanned one record and reported zero error rows; its complete TSV was header-only. Full backbone-chain, native-name, source-count, PATHS/scope and seed-reason comparisons were also completed. Schema validity does not resolve the biological scope of the GTDB predicate.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, provenance, rendering, documentation-statistics and history gates. The corpus verifier has no target-only selector; no substitute focused command was invented. No target causal nodes or external history files require a focused term/history validator. No generator, curation writer, external history entry or status promotion was invoked.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222617` agrees with the identifier, label, rank, parent and code. Complete native name rows `data/catalog/ncbi_names-0005.jsonl.gz:32178`, `:32179` and `:32180` support the scientific name and the two NCBI equivalent names containing `strain F11` and `str. F11`.

The live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036743&retmode=xml) confirms strain rank, parent 1085, code 11 and those equivalent-name classes. The [NCBI Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036743) confirms all ten ancestor IDs including root: 1, 131567, 2, 3379134, 1224, 28211, 204441, 41295, 1081 and 1085. Their pinned labels/ranks exactly reproduce the root-first YAML lineage through Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rhodospirillales, Rhodospirillaceae and Rhodospirillum.

A cached browser search result displayed an older no-rank label; freshly retrieved structured NCBI responses and the pinned backbone agree on `STRAIN`. The search snippet was not used to override them. Exact scans found no target type-material, merged-ID or dropped row. The NCBI grounding is supported; the GTDB species-equivalence claim is not.

## Evidence

The GTDB mapping row `data/raw/gtdb_mappings.tsv:1464` reproduces `skos:closeMatch` and count 9. The complete species row `data/raw/gtdb_species.tsv:154830` independently identifies 9 genomes under `GTDB:s__Rhodospirillum_rubrum`. An ignored-inclusive decompressed scan followed by exact taxonomy-segment comparison found nine members and nine unique accessions. All nine complete native records were read, not only projected count fields.

| GTDB member | Source strain/isolate | NCBI taxon | Complete native address |
| --- | --- | --- | --- |
| RS_GCF_000225955.1 | F11 | 1036743 | `data/catalog/gtdb_genomes-0015.jsonl.gz:27005` |
| RS_GCF_000013085.1 | ATCC 11170; representative and type material | 269796 | `data/catalog/gtdb_genomes-0010.jsonl.gz:3551` |
| RS_GCF_019134555.1 | DSM 467; type material | 1085 | `data/catalog/gtdb_genomes-0003.jsonl.gz:7781` |
| RS_GCF_016583925.1 | DSM 107 | 1085 | `data/catalog/gtdb_genomes-0015.jsonl.gz:28484` |
| RS_GCF_016583945.1 | DSM 1068 | 1085 | `data/catalog/gtdb_genomes-0001.jsonl.gz:31538` |
| GB_GCA_003530895.1 | UBA12186; metagenome-derived | 1085 | `data/catalog/gtdb_genomes-0000.jsonl.gz:25164` |
| GB_GCA_003457435.1 | UBA10083; metagenome-derived | 1085 | `data/catalog/gtdb_genomes-0004.jsonl.gz:25860` |
| RS_GCF_032086735.1 | CTOTU50883; metagenome-derived | 1085 | `data/catalog/gtdb_genomes-0008.jsonl.gz:9105` |
| RS_GCF_032087155.1 | CTOTU50864; metagenome-derived | 1085 | `data/catalog/gtdb_genomes-0008.jsonl.gz:33934` |

Only one cluster member is explicitly F11/taxon 1036743. The same GTDB species also maps to the parent species and the ATCC strain in raw mapping rows 3107 and 208348. Thus cluster membership supports F11's species classification, not identity between the entire cluster and the mutant. The live GTDB tree page was unavailable to the web reader; the finding relies on the inspected pinned cluster, not a claimed live GTDB result.

The count 9 itself is correct for the source species. `TaxonomyMapping.genome_count` is explicitly defined as the number of genomes under the source taxon (`src/taxonmech/schema/taxonmech.yaml:435`). It is not nine F11 genomes and should not be changed to one to conceal an incorrect predicate. The source-species GTDB attestation preserves that count but repeats the unsupported `closeMatch`.

Complete native GenBank and RefSeq records at `data/catalog/ncbi_genbank-0000.jsonl.gz:3963` and `data/catalog/ncbi_refseq-0000.jsonl.gz:3404` establish GCA_000225955.1 / GCF_000225955.1, paired identical, strain F11, taxon 1036743, a complete 4,352,825-base one-replicon genome, BioSample SAMN02603286 and native PMID 22194448. GenBank gives PRJNA67413; RefSeq uses PRJNA224116. The live [NCBI assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000225955.1/dataset_report) independently confirms the current paired accessions, F11 sample, project and genome size. Complete nuccore summaries verify CP003046.1 and NC_017584.1 as circular 4,352,825-base F11 chromosome records; RefSeq explicitly refers to CP003046.1. No raw genome alignment or sequence-equivalence inference against the wild type was performed.

The assembly-linked primary paper, [Lonjers et al., DOI 10.1128/JB.06319-11](https://journals.asm.org/doi/10.1128/jb.06319-11), PMID 22194448 / PMC3294814, was inspected through its abstract, methods, accession statement and results/discussion. It distinguishes mutant F11, wild-type ATCC 11170 and revertant RF111, and explicitly deposits F11 as CP003046. F11 and RF111 differ at a nonsense mutation in `rquA`; the authors separately tested complementation and a wild-type deletion mutant. Their experiments distinguish anaerobic growth and rhodoquinone-production states rather than demonstrating strain identity. The report does not import those optional phenotypes or turn the paper's then-unresolved enzymatic mechanism into a current biochemical assertion.

That distinction matters for existing source crosslinks:

- Complete BacDive native record `data/bacdive/records.jsonl.gz:13838`, BacDive 14005, is S 1/S1, with DSM 467 and ATCC 11170 among its deposits and general taxonomy 1085/269796. Its genome list also contains the F11 assembly, BV-BRC 1036743.4 and IMG 2511231162. The live [BacDive identity page](https://bacdive.dsmz.de/strain/14005) confirms its S1/type-strain identity, not a distinct F11 deposit. Raw BacDive strain row `data/raw/bacdive_strains.tsv:13839` is classified under 269796, not the reviewed taxon.
- Complete BV-BRC record `data/bvbrc/bvbrc-0000.jsonl.gz:3397` explicitly supplies the F11 assembly, chromosome, sample, project and taxon, but also gives culture collection ATCC 11170 and `type_strain: Yes`. Those latter assertions conflict in scope with the primary mutant/wild-type distinction and the target's absence from NCBI type-material rows. Preserve the conflict; do not infer that F11 is identical to the deposited wild type.
- Complete raw assembly rows `data/raw/strain_assemblies.tsv:43955` and `:43956`, genome rows `data/raw/strain_genome_records.tsv:34410`, `:34417`, `:34418`, and related-record rows `data/raw/strain_related_records.tsv:127596`, `:127611` retain those source assertions against `kgmicrobe.strain:bacdive_14005`, including the BV-BRC whole-deposit match to ATCC 11170. They are not emitted as a strain entry in this F11 YAML. Their presence is not permission to add the wild-type strain or type-strain flag here, nor to declare another taxon record reviewed.

GOLD supplies a separate explicit chain. Complete organism `data/gold/organisms.jsonl.gz:10222` is Go0011632, F11, taxon 1036743, without a culture-collection accession. Complete project `data/gold/projects.jsonl.gz:10078` is Gp0011632, linked to that organism and PRJNA67413, with an empty BioSample field. Complete analysis `data/gold/analyses.jsonl.gz:4122` is Ga0009339, explicitly linked through Gp0011632 to IMG 2511231162 and CP003046/GCA_000225955.1; its direct organism field is empty, so the project chain supplies the inspected relationship. GOLD's Go/Gp/Ga identifiers and project/sample identifiers are not genome identifiers.

There is no own row in `data/raw/gold_organisms.tsv` and hence no emitted GOLD attestation. This is a difference between the native workbook catalog and the pinned kg-microbe count projection, not absence of GOLD evidence: `src/taxonmech/extract.py:676` derives counts from transformed GOLD edges, while `src/taxonmech/seed.py:613` reads the resulting direct-count table. `docs/SOURCE_COVERAGE.md` distinguishes native discovery from admitted taxon-record relationships. A separate refresh/enrichment decision should assess this known chain; no fabricated count or source attestation was added here.

The one NCBI `NAME` attestation and snapshot note agree with the backbone. The one Madin `TRAIT_ASSERTION` agrees with `data/raw/madin_taxa.tsv:698`. Its original individual trait edge was not reverified: a fresh gitignore-independent `find` under the configured kg-microbe checkout found no `madin_etal/edges.tsv`. The count does not identify a specific phenotype or validate the conflicting type-strain claim above.

## Completeness

Ignored-inclusive content searches used `rg --no-ignore --hidden` with decompression over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The identifier, full strain label, equivalent-name forms and slug returned 23 candidate rows, all read in full. Expansion to the versioned/unversioned assembly, chromosome, sample, project, GOLD and IMG identifiers returned 13 already inspected rows and no new candidates. A separate exact-species cluster scan supplied the nine complete GTDB members above. The five source metadata JSON files were read structurally, and ignored-independent filename scans covered the taxon, prior-report and history roots.

Full exact-taxonomy scans found no BacDive strain row, LPSN name row, MediaDive/BactoTraits count row, immediate child, type-material row, redirect, dropped status or external history entry for this taxon. These bounded negatives do not deny the native GOLD and genome records described above. Bare F11 tokens throughout unrelated records were not used as identity evidence; this review makes no global absence claim for that common designation.

`strain_count: 0` correctly reflects the current classified BacDive entries. F11 has a genome, but the BacDive strain used by the existing crosslinks is classified elsewhere and denotes the wild type. Genome enrichment must resolve that conflict rather than relabel the existing type-strain deposit. Missing optional genome lists, literature fields and phenotype mechanisms are not separately counted as record defects. iModulonDB was not applicable: the YAML itself contains no gene, locus, expression-module or transcriptomic claim, and no mechanistic curation was undertaken.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: GTDB species classification is promoted to exact strain identity.** YAML line 43 asserts `skos:closeMatch` between the GTDB species and F11; lines 46-49 make Rhodospirillum rubrum an `EXACT_SYNONYM`; line 57 adds the identity-derived species xref; line 70 repeats the mapping in the attestation. The independently inspected nine-member cluster and primary mutant/wild-type distinction demonstrate that the species concept is broader than F11. Count this as one connected identity-promotion defect, not four findings.

   Maintained owners are upstream kg-microbe GTDB relationship semantics as consumed by `src/taxonmech/extract.py:501`, and rank-blind identity admission at `src/taxonmech/seed.py:451`, including its downstream synonym/xref and attestation construction. Extraction copies the whole source-species count at `src/taxonmech/extract.py:755`. The compatibility script `scripts/seed_from_sources.py` is not the maintained implementation. Do not fix the generated YAML directly.

The BacDive/BV-BRC wild-type association is a material caution for future enrichment and related source review, but this target emits none of those strain links or type-strain claims, so it is not counted as an additional emitted-record defect. The missing projected GOLD attestation is documented above as a source-coverage boundary, not an unsupported claim that the native GOLD record does not exist.

## Recommended Edits

1. Add scope-aware identity admission to `src/taxonmech/seed.py`. F11 must retain its exact NCBI identity and two equivalent names without acquiring a species-wide exact synonym or identity xref solely from `closeMatch`.
2. Correct the upstream relationship and its source-preserving local handling in `src/taxonmech/extract.py` / `src/taxonmech/seed.py`. Represent supported species membership without asserting equality. The schema defines direction from source GTDB taxon to the record; an unexamined replacement with `broadMatch` would also reverse the required scope because F11 is narrower than the species. Resolve the chosen non-equivalence representation before regeneration.
3. Keep 9 as the source-species count if the mapping is retained and explain its scope. Do not relabel it as nine F11 genomes or replace it with one without changing the field's defined meaning.
4. Add focused regression cases to `tests/test_seed.py` for a strain-level incoming `closeMatch`, preservation of genuine NCBI synonyms, consistent mapping/attestation semantics, source-wide counts and valid species-level identity behavior. A separate genome-enrichment/source correction must preserve F11, ATCC 11170 and RF111 as distinct experimental identities and resolve conflicting deposit/type assertions before admitting links.

No implementation, data refresh, source correction, history append or status promotion was performed by this review.

## Follow-up Checks

After an authorized maintained-input fix, run focused seeder regressions, dry-run seeding and inspect an F11 canary before bulk regeneration. Confirm the species exact synonym/xref no longer denotes F11, the two NCBI names remain, mapping and attestation agree in direction, and count 9 remains explicitly species-scoped.

Re-run both focused validators, then `just verify-corpus` and the repository quality gates for the full generator/source change. Recheck the live GTDB view when accessible. If enrichment is authorized, independently resolve F11 deposit ownership, preserve the complete GOLD organism-project-analysis chain, retain accession versions, and test that no type-strain or mutant phenotype is transferred between the three experimental identities. Reverify the original Madin edge before adding an individual phenotype.

## Additional Notes

`data/taxa/PATHS.tsv:15141` identifies this slug; `curation/legacy_page_paths.tsv:901` is its old page-path mapping. `curation/seed_scope.tsv:36178` records the 2026-09-12 three-source reason. The 2026-09-13T17:54:04Z seed event matches the emitted sources and scope reason; it does not claim completed scientific review.

This report follows a separate full-record and source investigation, not a borrowed verdict. Other records, including Eukaryota and the ATCC 11170 record, were not edited or assigned new verdicts. Existing reports, history, pages, branches and worktrees were preserved. No external messaging, GitHub mutation or paid research was undertaken.
