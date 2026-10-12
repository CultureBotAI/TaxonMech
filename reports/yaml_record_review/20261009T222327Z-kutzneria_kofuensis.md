# YAML Record Review: Kutzneria kofuensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/kutzneria_kofuensis.yaml`
- Started UTC: 2026-10-09T22:15:43Z
- Finished UTC: 2026-10-09T22:23:27Z
- Verdict: pass

## Target

Entire 1,621-line generated `TaxonRecord` read in three untruncated chunks. `NCBITaxon:103725` denotes Kutzneria kofuensis, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:43356`, genetic code 11, grounding `EXACT`, status `SEEDED`. Reviewed all nine ancestors, four sourced synonyms, nomenclature, GTDB mapping, two strain entries, nested source assertions, seven attestations and complete seed event.

HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. YAML SHA-256: `5147302bc024872b5e596f0fb68eadccd467b21a465c2a20029299d861727876`. Ignored-inclusive filename resolution found one target and no prior review for this stem.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/kutzneria_kofuensis.yaml`: passed, including a fresh rerun before reporting.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/kutzneria_kofuensis.yaml --out /private/tmp/taxonmech-kutz-kofuensis-20261009-validation.tsv --workers 1`: one file, zero errors; fresh rerun passed and header-only output TSV was read.
- `uv run --offline python scripts/validate_history.py history`: reused this turn's 17 valid records, zero invalid links, after a fresh empty diff for history, schema and validator.
- Exact own-row, ancestor, type-material, mapping, attestation, scope, slug and nested-link comparisons passed. Whole-deposit identifier checks passed. These focused comparisons are not corpus reproduction or raw-provenance hash replay.
- Public NCBI taxonomy, assembly and marker metadata, LPSN pages, BacDive pages, StrainInfo API responses and Crossref DOI metadata were inspected. The GTDB tree and publication DOI browser opens failed. Pinned native GTDB records and Crossref bibliography supplied bounded checks, not a successful live GTDB-tree or publication-full-text review.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes. No new focused replacement for a full-corpus gate was invented.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18551`, slug `data/taxa/PATHS.tsv:15243` and scope `curation/seed_scope.tsv:5314` agree. The complete backbone supports the target, parent, code, source set and 2026-09-13 snapshot. Nine ancestor IDs, labels and ranks agree with the pinned chain: root; cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; Pseudonocardiales; Pseudonocardiaceae; Kutzneria. Complete backbone and status scans found no own child, merger or dropped-ID row; thirteen type-material rows preserve the six recognized deposit identities and their source spellings.

The [NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103725&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103725) support the identity and lineage. `EXACT` grounds this NCBI node; it does not reconcile independent taxonomies or make every source deposit assertion taxonomically identical.

[LPSN 777224](https://lpsn.dsmz.de/species/kutzneria-kofuensis) supports the authority `(Nonomura and Ohara 1969) Stackebrandt et al. 1994`, valid publication, legitimacy and correct-name status. Its six type deposits match ATCC 27102, DSM 43851, IFO 13989, JCM 3157, NBRC 13989 and NRRL B-24061. [LPSN 782180](https://lpsn.dsmz.de/subspecies/streptosporangium-viridogriseum-kofuense) is the subspecies-rank basionym, not a second currently accepted species. The shorter LPSN synonym spelling in YAML follows the pinned inventory; the NCBI exact synonym retains `subsp.`. Full authorities are related synonyms, not misfiled exact names.

`data/raw/gtdb_mappings.tsv:1472` and three complete native GTDB genome rows support `GTDB:s__Kutzneria_kofuensis`, `skos:closeMatch` and count 3. GTDB's Mycobacteriales placement is kept separate from NCBI's Pseudonocardiales lineage. Native rows are `data/catalog/gtdb_genomes-0012.jsonl.gz:40154`, `gtdb_genomes-0001.jsonl.gz:6272` and `gtdb_genomes-0000.jsonl.gz:4273`; DSM 43851 is the representative. Live tree verification remains unavailable.

## Evidence

`data/raw/lpsn_names.tsv:17646` supports the nomenclature block. The [Crossref record for the 1994 transfer](https://api.crossref.org/works/10.1099%2F00207713-44-2-265) verifies `DOI:10.1099/00207713-44-2-265`, authors, year, volume 44 and pages 265-269. The [notification metadata](https://api.crossref.org/works/10.1099%2F00207713-44-3-596) verifies `DOI:10.1099/00207713-44-3-596`, volume 44, issue 3, page 596. LPSN connects both to the name. No claim of reading either publication's full text is made.

The two BacDive inventory rows, `data/raw/bacdive_strains.tsv:13133` and `:68259`, agree with fully read native records and the public [13295](https://bacdive.dsmz.de/strain/13295) and [145982](https://bacdive.dsmz.de/strain/145982) pages. The first represents the type-strain group and eleven culture identifiers, including source-preserved IMSNU formatting and S2-28 designation markup. The second is CCUG 30082, not promoted to a type strain and not merged into the type-strain group.

All 121 nested assertions match their source inventories exactly, with no missing or extra entries: type-strain group 25 assembly assertions, 16 genome-record assertions and 78 related-record assertions; CCUG 30082 two related-record assertions. These are provenance-bearing assertions, not 25 independent assemblies or 16 independent physical genomes. Complete own rows were checked in `data/raw/strain_assemblies.tsv`, `strain_genome_records.tsv`, `strain_related_records.tsv`, and `data/straininfo/assemblies.tsv` and `related_records.tsv.gz`, then traced to inspected native records.

Three actual assembly families have explicit whole-deposit support:

| Assembly pair, version 1 | Deposit | BioSample | GenBank BioProject | Level |
| --- | --- | --- | --- | --- |
| GCA_014203355.1 / GCF_014203355.1 | DSM 43851 | SAMN05878009 | PRJNA347128 | Contig |
| GCA_039535315.1 / GCF_039535315.1 | JCM 3157 | SAMD00645472 | PRJDB10510 | Contig |
| GCA_042428765.1 / GCF_042428765.1 | JCM 3157 | SAMN43281792 | PRJNA595761 | Scaffold |

Pinned NCBI records support each paired accession and the source-specific RefSeq umbrella PRJNA224116. Focused live NCBI reports for [014203355](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_014203355.1/dataset_report), [039535315](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_039535315.1/dataset_report) and [042428765](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_042428765.1/dataset_report) confirm current assemblies, paired RefSeq IDs, deposits, samples and GenBank projects. Newer live annotation dates do not invalidate the pinned assembly identities. Unversioned BacDive and StrainInfo accessions remain unversioned source assertions.

Native BV-BRC entries support PATRIC 103725.4, 103725.6 and 103725.7 and their explicit deposit fields. GOLD chains were checked at organism, project and analysis levels: `Go0028502 -> Gp0126969 -> Ga0104557` supports IMG 2845553441 without inventing an assembly accession; the same organism/project leads to `Ga0436916`, IMG 2863024190 and GCA_014203355.1. `Go0605562 -> Gp0854965 -> Ga0682056` supports IMG 8147989155 and GCA_039535315.1. Other matched GOLD organisms name ATCC 27102, CBS 803.70, IFO 13989 and NBRC 13989. The seventh organism's bare S2-28-style designation does not qualify as a culture-collection match, while still contributing to the organism attestation count.

Complete native and live [StrainInfo 45786](https://api.straininfo.dsmz.de/v2/data/strain/max/45786) responses support DOI `10.60712/SI-ID45786.3`, BacDive 13295, published status and nine matched deposits: 123853/ATCC 27102; 123856/DSM 43851; 168867/IFO 13989; 168868/JCM 3157; 230213/CBS 803.70; 278920/NRRL B-24061; 319741/KCTC 9437; 333488/NBRC 13989; 507770/BCRC 13322. The sequence-to-deposit relations explicitly link GCA_014203355 to deposit 123856, MT760419 to 168868 and AF114801 to 278920. CCRC 13322 and NRRL B-21061 also occur in StrainInfo but were not silently normalized into different BacDive deposits.

Source conflict retained: CBS 803.70, SI-DP 230213, carries NCBITaxon:47990 and the older name Streptosporangium viridogriseum within StrainInfo's otherwise K. kofuensis group. NCBI identifies 47990 as the distinct species Kutzneria viridogrisea. Exact native deposit, `data/straininfo/strain_links.tsv:14316`, related rows 35845 and 35858, and live StrainInfo agree on this conflict. YAML preserves the deposit-level source taxon; it neither overwrites the target lineage nor transfers a sequence through this CBS deposit. This is a source disagreement to preserve, not a demonstrated generated-record defect or evidence that the two species are identical.

[StrainInfo 108406](https://api.straininfo.dsmz.de/v2/data/strain/max/108406) supports DOI `10.60712/SI-ID108406.2`, BacDive 145982 and available non-type deposit 324559/CCUG 30082. Its response supplies no sequence relation. Both DOI versions occur in the live archive metadata; DOI landing-page rendering was not required to infer their version strings.

Complete marker annotations and bibliography were inspected: [AF114801.1](https://www.ncbi.nlm.nih.gov/nuccore/AF114801.1) is a 1,502-nt partial 16S sequence for NRRL B-24061T; [MT760419.1](https://www.ncbi.nlm.nih.gov/nuccore/MT760419.1) is a 1,339-nt partial 16S sequence for JCM 3157. Both identify taxon 103725 and type material of the basionym. Declared and actual lengths agree; lowercase-sequence SHA-256 values are `e8cc7f90e7d567c8acf0a724ee1faa90d5e0c8d7ccf2af253fda173ac99f42e3` and `93ca9e6a80aec45e49f0d39c3ff957574252dbab396bf0b0ea7bb1b3b0eccbe5`. The first cites Labeda and Kroppenstedt's 2000 phylogenetic paper, PMID 10826820; the second contains a direct submission. These are marker identities, not whole-genome or phenotype evidence.

Attestations preserve separate units: NCBITAXON 1 NAME, LPSN 1 NAME, GTDB 3 GENOME, BACDIVE 2 STRAIN, MEDIADIVE 4 MEDIUM, GOLD 7 ORGANISM and MADIN 1 TRAIT_ASSERTION. Supporting rows include `data/raw/mediadive_taxa.tsv:137` (65, 84, J42, J50), `gold_organisms.tsv:511` and `madin_taxa.tsv:703`. Counts are source coverage, not biological abundance or an assertion of a particular trait. The complete scope sentence and this turn's inspected seeder plus raw/ATB/StrainInfo manifests support the seed time `2026-09-13T17:54:04Z`; a fresh diff confirmed them unchanged. This event denotes generation, not human review.

## Completeness

Ignored-, hidden- and compression-inclusive `rg --no-ignore --hidden -n -z -i` searched the bounded numeric identity, scientific names and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 298 matching rows were read in full or lossless common-field/delta representations. Five source-metadata JSON files and history filenames were separately checked. No own history entry was established in those bounded searches.

False matches were distinguished explicitly: DSM 103725 belongs to Algisphaera agarilytica, including its BacDive, StrainInfo, ATB and genome chains; CIP 103725 belongs to Anaerococcus lactolyticus; SI-DP 103725 is Stigmatella aurantiaca ATCC 25190; BacDive 103725 is Rhodococcus sp. ST000901. Numeric strain/isolate names also matched unrelated Salmonella, Campylobacter, uncultured Ruminococcus and uncultured bacterial assemblies. An E. coli GTDB row matched contig N50 rather than taxon identity; Enterobacter rows matched plasmid CP103725. These do not supply Kutzneria links. The sole source-metadata match was a BacDive request for BacDive ID 103725, not NCBI taxon 103725. Complete native and transformed rows disambiguated these cases.

Native SeqCode name rows supplied corroborating name leads, not an unrepresented required mapping. Complete own-row scans found no BactoTraits attestation or own ATB strain/assembly link. No additional eligible whole-deposit chain or required missing representation was established. Optional definitions, claim evidence and causal graphs may remain empty. iModulonDB is inapplicable: this YAML has no gene, regulator, pathway, functional trait or transcriptomics assertion. A MADIN coverage count is not such an assertion. Absence conclusions are bounded to the inspected roots, snapshots and responses, not every possible external source.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated YAML. The StrainInfo CBS deposit conflict and differing GTDB order are preserved source-level observations, not silently reconciled identities. Live GTDB access and publication full text remain check limitations, not evidence of an error.

## Recommended Edits

None required. Preserve NCBI identity, source-specific classifications and deposit-level provenance. Any future resolution of CBS 803.70 should first obtain collection or StrainInfo evidence; do not manually change the deposit taxon or infer sequence links from its strain-group membership. Supported future changes belong in the maintained source transforms or `src/taxonmech/seed.py`, with tests and regeneration, not hand-edited generated YAML or an assumed overlay.

## Follow-up Checks

No corrective validation is required by a finding. Before regenerated publication, run `just verify-corpus` and `just qc`. A later source refresh can retry the GTDB authority page and inspect the nomenclatural papers directly. Any CBS identity correction must preserve the evidence for the original disagreement and independently check same-deposit sequence relations; shared name, taxon, sample or group membership alone is insufficient.

## Additional Notes

Only `NCBITaxon:103725` is judged. No neighboring YAML or Eukaryota review was reopened. No YAML, source, scope, history, status, branch, worktree or GitHub item changed. This new report is the only repository write for this target. All ten existing worktrees were left untouched; the other session is closed. No paid research was used.
