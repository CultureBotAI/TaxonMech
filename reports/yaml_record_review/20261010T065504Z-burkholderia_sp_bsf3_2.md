# YAML Record Review: Burkholderia sp. BSF3(2)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsf3_2.yaml`
- Started UTC: 2026-10-10T06:52:09Z
- Finished UTC: 2026-10-10T06:55:04Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037594`, Burkholderia sp. BSF3(2). This bacterial species-ranked placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` mapping status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. The maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated taxon YAML is read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsf3_2.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsf3_2.yaml --out /private/tmp/taxonmech-bsf32-20261010-validation.tsv --workers 1`: one file, zero errors; output TSV was inspected and contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured source comparisons passed for identity, complete lineage labels/ranks, synonyms, code, name attestation, unique identifier/slug, scope reason, and seed-event wording. They do not replace corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph nodes or causal claims. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222809` agrees with the exact identifier, label, species rank, parent, code, and 2026-09-13 snapshot. Synonym and retirement fields are empty. All root-first ancestor labels and ranks match their individual backbone rows: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037594&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037594), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037594) agree. All 74 parsed browser text lines were inspected. EFetch omits root in its ancestry while Datasets includes it. Datasets does not supply an assembly count; omission is not zero. A sequence strain qualifier is compatible with the species-ranked placeholder and does not establish formal nomenclature or a culture deposit.

The full native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32445` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15362` uniquely resolves this identifier/slug; `curation/seed_scope.tsv:323024` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event. No review-status promotion is claimed.

## Evidence

The source attestation counts one NCBI `NAME`, not one strain, genome, publication, or assay. Structured scans found no own rows in the pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional strain, nomenclature, and mapping sections are correctly empty relative to those inputs. Zero inventoried strains does not mean the isolate does not exist or is unculturable.

Exact Nucleotide search `txid1037594[Organism:exp]` returned one UID, `345019008`. Complete [GenBank annotation JF779757.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779757.1) explicitly joins Burkholderia sp. BSF3(2), strain BSF3(2), and `taxon:1037594`. It contains a 450-base 16S rRNA fragment partial at both ends, with isolation source annotated as fertilized bulk soil in a beech forest. Declared and actual lengths match, alphabet is A/C/G/T, and lowercase sequence SHA-256 is `bb503883b68ffa7bb756db0aefc207c33a62f1221216c60b54af0585474125df`. This fragment is not a genome assembly. No collection country/date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The sequence cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study in Soil Biology and Biochemistry 43(11):2275-2282. The complete requested [HAL deposit metadata and abstract](https://hal.science/hal-02916138v1), read earlier in this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Full text was not inspected. No BSF3(2)-specific assay result was verified, and no weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred from the citation, cohort, genus, or nearby sequence.

All 20 non-target native rows were read in full, including compressed TSV entries:

- `data/catalog/ncbi_genbank-0019.jsonl.gz:22535`: metagenome-derived bacterium, taxid 1869227, isolate SMBSF32, `GCA_021107875.1`, `SAMN21083260`, `PRJNA758896`, `JAIOSA000000000.1`. The loose designation pattern matches a substring of SMBSF32, not BSF3(2). The same assembly/sample/project occur in complete BV-BRC rows `data/bvbrc/bvbrc-0007.jsonl.gz:5924` and `:6195`, genome IDs `1869227.1978` (WGS) and `1869227.2222` (Deprecated). These are not target strain links.
- `data/catalog/ncbi_genbank-0042.jsonl.gz:43548`, `:43549`, and `:43550` share unrelated BioProject `PRJNA1037594`. The first two are Pseudomonas capeferrum, taxid 1495066, strains UC_21.30 A.1 and UC_21.3 A.1, assemblies `GCA_046537655.1` and `GCA_046537675.1`, samples `SAMN38191812` and `SAMN38191811`, WGS `JAWWUZ000000000.1` and `JAWWVA000000000.1`. The third is Bacillus amyloliquefaciens, taxid 1390, strain UC_2.4, `GCA_046537695.1`, `SAMN38191810`, `JAWWVB000000000.1`. Their complete BV-BRC counterparts are `data/bvbrc/bvbrc-0003.jsonl.gz:25454` (`1495066.14`), `:25455` (`1495066.15`), and `data/bvbrc/bvbrc-0002.jsonl.gz:49094` (`1390.1170`), respectively. The project number cannot be used as a taxon identifier.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:45971`: Acinetobacter baumannii, taxid 470, strain AB2, isolate 10BC170021544, `GCA_050821965.1`, `SAMN41037594`, `PRJNA514245`, `DBJBAT000000000.1`; the match is in its BioSample.
- `data/catalog/ncbi_genbank-0051.jsonl.gz:19510`: Streptococcus pneumoniae, taxid 1313, isolate `1037594`, `GCA_055615015.1`, `SAMEA120831694`, `PRJNA514245`, `DBMUMG000000000.1`. PMID 30286803 on this and the Acinetobacter row is not a target citation.
- Nine `data/catalog/allthebacteria.tsv.xz` rows concern Salmonella enterica, with PASS filters and available FASTAs. Line 1716840 links `SAMN13162652` / `ERZ25668181` / `SRR10375948`; 1716841 links `SAMN13162653` / `ERZ25668192` / `SRR10375945`; 1716842 links `SAMN13162654` / `ERZ25668202` / `SRR10375941`; 1716843 links `SAMN13162655` / `ERZ25668212` / `SRR10375943`; 1716844 links `SAMN13162656` / `ERZ25668222` / `SRR10375942`; 1716845 links `SAMN13162657` / `ERZ25668231` / `SRR10375947`; 1716846 links `SAMN13162658` / `ERZ25668239` / `SRR10375944`; 1716848 links `SAMN13162660` / `ERZ25668260` / `SRR10375940`; 1716849 links `SAMN13162661` / `ERZ25668270` / `SRR10375946`. These run substrings are unrelated to target identity.

No candidate establishes an additional target genome, deposit, synonym, or attestation.

## Completeness

Ran `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, covering identifier, exact slug, organism/designation, and punctuation/space/hyphen variants. The expanded pass added `JF779757`, `soilbio.2011.07.010`, and `S003807171100280X`. Both searches returned 23 lines: own backbone, scope, scientific name, and the 20 unrelated entries above. Ignored and compressed files were included. No extra target-linked assertion, genome/strain association, or history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a matching value/key. Ignored-independent filename checks found the exact target YAML and no pre-existing report/history filename. No Eukaryota YAML contents were read. Exact organism search produced taxonomy and unrelated leads, and accession search returned no result; no search snippet supported a claim.

Optional slots need not be populated without source support; no causal graph is required. iModulonDB is not applicable because there are no gene, regulator, expression-module, or stress-response claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected inputs and live authorities support the taxonomy/name-only assertions. Unverified isolate assays and unavailable article full text are enrichment limitations, not unsupported claims in this record.

## Recommended Edits

None required. Do not edit generated YAML, add a history event, or promote review status. Preserve BSF3(2) separately from SMBSF32 and keep partial markers outside genome counts. Verified future enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Obtain the cited study and isolate-level table before functional enrichment, explicitly resolve BSF3(2)/JF779757, and verify assay conditions and outcomes. Require an explicit source chain for any genome or deposit link. After authorized input changes, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Human sign-off is separately required for review-status promotion.

## Additional Notes

The complete primary taxonomy browser, taxonomy APIs, and marker annotation were inspected for this target. Shared HAL metadata and abstract were inspected earlier this turn. Earlier access checks for the shared paper found ScienceDirect 403 and an ISTEX redirect returning institutional-authentication HTML rather than a PDF; those failed routes were not retried per isolate. No login, paid access, or full-text reading occurred.

YAML SHA-256: `8185e3ff646c788fa07790f2f66559cce31986d5caedaa7cde2a396819f3fe29`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
