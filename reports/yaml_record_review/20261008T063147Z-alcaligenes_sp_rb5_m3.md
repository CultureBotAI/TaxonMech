# YAML Record Review: Alcaligenes sp. RB5-M3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alcaligenes_sp_rb5_m3.yaml`
- Started UTC: 2026-10-08T06:24:28Z
- Finished UTC: 2026-10-08T06:31:47Z
- Verdict: pass

## Target

The entire 54-line `TaxonRecord` was read before judgment. It identifies `NCBITaxon:1036329`, Alcaligenes sp. RB5-M3, as a species-rank bacterial taxon under `NCBITaxon:259357` (unclassified Alcaligenes). This is a generated, NCBI-attested seed record with `grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11, zero linked BacDive strains, one NAME assertion, and one seed event dated 2026-09-13. A species-rank placeholder does not imply a formally named species.

The exact identifier, label and filename resolved one target. Eukaryota and other records were not reviewed as part of this individual report.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/alcaligenes_sp_rb5_m3.yaml`: passed, "No issues found".
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/alcaligenes_sp_rb5_m3.yaml --out /private/tmp/arb5-strict.tsv`: passed; one file scanned, zero ERROR files and zero ERROR rows. The output TSV was read and contains only its header.
- Read-only structured comparisons checked the complete target backbone row, every stored ancestor, source attestations, seed-scope membership, path index, and seed-event text against the pinned local inputs. All matched. These comparisons are not a substitute for full-corpus reproduction.
- Exact taxonomy identifiers were checked against live NCBI Taxonomy EFetch and Datasets responses. Their identity, parent, rank, genetic code and lineage agree with the record, accounting for EFetch's omission of root from `LineageEx`.
- Not checked: full-corpus `verify-corpus`, provenance and history gates, rendering/site/docs builds, full tests, vendored-source checks and global QC. They were not run in this single-record review; no focused substitute for a documented corpus-only gate is claimed.
- Graph-product validation is not applicable: the record contains no causal graph. iModulonDB is not applicable: it contains no gene, regulator, functional or transcriptomic assertion. This is not negative biological evidence.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:222333` gives the same taxon ID, name, species rank, parent, genetic code and 2026-09-13 snapshot. Its exact, related and broad synonym fields are empty; the YAML does not invent synonyms. The scientific-name entry in `data/catalog/ncbi_names-0005.jsonl.gz:31877` corroborates the identity.

All ten stored ancestor IDs, labels, ranks and their order match the pinned backbone: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Betaproteobacteria (28216), Burkholderiales (80840), Alcaligenaceae (506), Alcaligenes (507), and unclassified Alcaligenes (259357). These numbers denote NCBI Taxonomy identifiers, not additional strain identifications.

The inspected [NCBI Taxonomy EFetch record](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036329&retmode=xml) agrees with the stored name, species rank, bacterial division, parent 259357 and genetic code 11. It has no `OtherNames` element. The [NCBI Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036329) independently supplies the same root-inclusive ordered ancestor IDs. `EXACT` is justified as identity to this NCBI taxon; it is not a claim of formal nomenclatural status or independently demonstrated phenotype.

Complete scans of the pinned backbone found no child row, and exact-target scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no matching row. These are bounded statements about the inspected local snapshots, not universal assertions about culture holdings or taxonomy history.

## Evidence

The single NCBITAXON attestation supports a NAME assertion for exactly `NCBITaxon:1036329`, not a phenotype or an isolate count. The seed event agrees with `curation/seed_scope.tsv:322580`; `data/taxa/PATHS.tsv:14840` maps the identifier to the reviewed filename stem.

An exact NCBI Nuccore search, `txid1036329[Organism:noexp]`, returned one record (UID 334701518). The inspected top-level, source-feature and reference metadata for [JN019025.1](https://www.ncbi.nlm.nih.gov/nuccore/JN019025.1) describe a 1,492-base partial 16S rRNA sequence with organism Alcaligenes sp. RB5-M3, strain RB5-M3 and `taxon:1036329`. These fields corroborate the exact taxon/strain association. Sequence bases and non-source features were not inspected; no alignment, species determination or genome-quality conclusion is claimed.

The sequence includes an unpublished reference by Yu, W., titled "Biological decoloring performance of Aeromonas hydrophila strain RB5-M". That reference title names a different genus and a shorter strain designation than the sequence's source qualifiers. It does not establish that RB5-M and RB5-M3 are identical, that the taxon should be renamed, or that a decolorization result applies to this record. The relationship between the unpublished study title and this sequence remains unresolved. The YAML makes none of those study claims, so this is an evidence-scope caution rather than a demonstrated record defect.

The direct submission is dated 25-MAY-2011; the sequence creation and update dates are 07-JUN-2011. Inspected source qualifiers contain organism, molecular type, strain and taxon cross-reference, but no isolation-source, geographic-location or culture-deposit qualifier. The submitter's Shanghai institutional address is not evidence of where the isolate was collected.

Exact-name, accession and unpublished-title searches did not establish an inspected exact-target primary publication. A near-name literature lead associated with DOI `10.3390/ijerph110202033`, PMID `24534769` and PMCID `PMC3945583` was not usable as primary evidence: the publisher returned HTTP 429 and PMC displayed a browser-check page. Search snippets concerning RB5-M1 are not evidence for RB5-M3. No claim about the article's contents, pathogenicity or isolation environment is used in this verdict.

## Completeness

All required seed fields are populated consistently. Zero `strain_count` means zero linked BacDive strain records in the inspected seed inputs, not absence of a biological strain or of nucleotide data. Complete exact-target scans of the seven raw inventories for BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin traits and BactoTraits found no target row requiring an additional attestation or link.

Ignored and hidden files were included in compressed-aware searches (`rg --no-ignore --hidden -z`) across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches covered the exact taxon number, slug and RB5-M3 label variants; an expanded search also included JN019025 and the unpublished reference title. The only matching content rows were the backbone, scientific-name catalog and seed-scope rows above, all read losslessly as complete TSV or JSON records. Five `SOURCE.json` metadata files were separately parsed, without an exact identity match. History filename and content searches found no target entry within those bounded roots.

An ignored-independent filename inventory across `data/taxa`, `reports/yaml_record_review` and `history` found the one target YAML and no pre-existing target report before this report was created. These bounded searches are not claims that no evidence exists elsewhere.

The exact-taxonomy NCBI Assembly search returned zero results with a phrase-not-found warning. That is a limitation of this query, not proof that no genome exists. Empty optional literature, discussion, trait, gene, culture-link and graph slots are not consequential omissions on the evidence inspected. Neither marker metadata nor a study title authorizes phenotype transfer.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed YAML. The unpublished reference-title relationship and inaccessible near-name article remain evidence limits, not demonstrated YAML errors. No wrong identity, unsupported record assertion, missing required representation or broken stored reference was established.

## Recommended Edits

None. Preserve the generated record and its SEEDED status. Do not rename it to Aeromonas, add dye-decolorization or pathogenicity claims, infer a Chinese isolation location, or create a culture link from the inspected metadata.

If subsequent evidence establishes an upstream taxonomy error, the identity correction belongs with NCBI and the maintained import configuration/transform (`conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py`), followed by the documented refresh and seed workflow. A demonstrated seed transformation defect would belong in `src/taxonmech/seed.py` and focused tests; scope membership is owned by `curation/seed_scope.tsv`. No such change is requested or made by this review. Do not patch the generated YAML to bypass those owners.

## Follow-up Checks

No follow-up is required for the current verdict. Before any future phenotype or publication enrichment, inspect an exact-strain primary source and resolve the relationship between JN019025.1, RB5-M3 and the unpublished RB5-M study. A shared prefix or a paper about RB5-M1 would not be sufficient. Recheck accession source qualifiers and authoritative taxonomy after any supported upstream correction.

For a separately authorized curation change, rerun both focused validators above, the documented provenance/corpus/history gates and any affected generated-product checks. Passing this review does not claim those unrun global gates passed.

## Additional Notes

This was a sequential, read-only individual review using the local review skill and curation checklist. No YAML, source input, curation event, review status, history entry or generated product was changed. No paid research, outreach, GitHub mutation, source refresh or regeneration was performed. Existing worktrees were left intact.

The record SHA-256 before and after evidence checks was `8a7c78e8549c1d7a193d5b0e1783eae4b045db8cf8e608c0d1f7469d315aca83`. This report is the sole new review artifact for this target.
