# YAML Record Review: Legionella massiliensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/legionella_massiliensis.yaml`
- Started UTC: 2026-10-06T02:40:57Z
- Finished UTC: 2026-10-06T02:47:44Z
- Verdict: pass

## Target

Read all 364 lines of this generated `TaxonRecord`: `NCBITaxon:1034943`, Legionella massiliensis, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:445` (Legionella), genetic code 11, `EXACT` grounding and `SEEDED` mapping status. The record contains one LPSN nomenclature entry, one GTDB mapping, three source-qualified synonyms, two xrefs, one type strain, eight source attestations and one inline seed event. Its strain has three assembly assertions, four genome-record assertions and twelve related-record assertions. These are provenance-bearing assertions, not nineteen distinct genomes.

`data/taxa/PATHS.tsv:14230` and `curation/seed_scope.tsv:4044` resolve this target uniquely. The seed event is dated `2026-09-13T17:54:04Z`; the scope reason names eight sources including NCBI. No generated record, inventory, history, prior report or lifecycle status was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/legionella_massiliensis.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/legionella_massiliensis.yaml --out /private/tmp/massiliensis-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured inventory inspection matched the identity, complete root-first lineage, source-qualified synonyms, eight attestations, scope and path. A separate structured comparison established exact multiset equality for all 19 strain-linked assertions, including source fields and nested StrainInfo evidence. These bounded comparisons are not a substitute for `just verify-corpus`.
- Gitignore-independent searches included compressed native catalogs. All 66 initial candidate rows and all five additional crosslink candidates were read in full, using lossless common-field grouping where applicable. No candidate was judged from a search excerpt alone.
- `git diff --exit-code HEAD --` for the target, inventories, scope, history, source code, scripts, documentation, configuration and local guidance: exit 0. Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site-drift checks, README statistics, publication-size and vendored-file gates. This was a read-only, single-record evidence review, not a corpus release certification.
- `just validate-products` was not applicable: this record has no curator-added causal-graph nodes. No replacement focused term/history validator was invented.

## Identity and Grounding

The live [NCBI Taxonomy record](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034943), taxonomy EFetch XML and [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034943) agree on the species identity, bacterial domain, parent and genetic code. The nine-ancestor chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Legionellales, Legionellaceae and Legionella. Every label and rank matches the pinned backbone; live EFetch omits the synthetic root entry while Datasets includes its ID.

`data/raw/ncbitaxon_taxa.tsv:221761` and the three native NCBI name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31180` onward support the scientific name and the two related synonyms. The authority string and former LegA label have not been promoted to exact NCBI synonyms. Exact-ID scans of `ncbi_merged_ids.tsv` and `dropped.tsv` found no target retirement or drop. A broad numeric search hit for old taxon 396864 concerns another NCBI identity, not StrainInfo SI-ID 396864.

The [LPSN name page](https://lpsn.dsmz.de/species/legionella-massiliensis) confirms name ID 790328, Campocasso et al. 2012, valid publication under the ICNP and correct-name status. The pinned legitimate flag is consistent with that entry; no contrary nomenclatural ruling was encountered. The GTDB spelling Tatlockia massiliensis is retained as a source-qualified taxonomy treatment, not an asserted ICNP recombination or a replacement for the NCBI lineage.

## Evidence

1. **Nomenclature and the type strain.** `data/raw/lpsn_names.tsv:27305` reproduces every nomenclature field, both DOIs, PMID 22307511 and `INSDC:JF779685`. LPSN lists CSUR P146, DSM 24804 and LegA. The imported nomenclature slot contains DSM 24804; the strain entry separately retains CSUR P146 and designation LegA. Thus the type's identity and aliases remain represented even though the LPSN-specific imported list is narrower. The [DSMZ deposit page](https://www.dsmz.de/collection/catalogue/details/culture/DSM-24804) independently confirms the designation and deposit aliases.

2. **Cited publications and marker.** The complete author abstract for [PMID 22307511](https://pubmed.ncbi.nlm.nih.gov/22307511/), also supplied in publisher-deposited Crossref metadata for [DOI 10.1099/ijs.0.037853-0](https://doi.org/10.1099/ijs.0.037853-0), explicitly identifies LegA = DSM 24804 = CSUR P146 as the massiliensis type. LegM = DSM 24805 = CSUR P145 belongs to the separately described tunisiensis species. [DOI 10.1099/ijs.0.050427-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.050427-0) resolves to the subsequent notification list, not a second characterization experiment. GenBank metadata for [JF779685.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779685.1) identifies a 1,512-base partial 16S rRNA gene from LegA, taxon 1034943, and cites the same paper. Its RefSeq marker derivative [NR_109415.1](https://www.ncbi.nlm.nih.gov/nuccore/NR_109415.1) explicitly names DSM:24804 and the source sequence. These are markers, not assemblies. Full article bodies and sequence alignments were not examined.

3. **GTDB mapping.** `data/raw/gtdb_mappings.tsv:1404` and `gtdb_species.tsv:174536` specify `GTDB:s__Tatlockia_massiliensis`, `skos:closeMatch`, count 2. Full native rows `data/catalog/gtdb_genomes-0008.jsonl.gz:5260` and `gtdb_genomes-0012.jsonl.gz:31664` give `RS_GCF_000756815.1` and `GB_GCA_000756695.1`; both carry NCBI species/taxon 1034943 and that GTDB species. This supports the one-to-one mapping and source-qualified synonym/xref. The live GTDB tree view could not be retrieved, so this is a pinned-primary-metadata verification, not a live-release census.

4. **BacDive strain and direct genome assertions.** `data/raw/bacdive_strains.tsv:6671`, native `data/bacdive/records.jsonl.gz:6670` and the [BacDive 6788 page](https://bacdive.dsmz.de/strain/6788) agree on LegA, DSM 24804, CSUR P146, type status and species classification. Reference 66792 supplies unversioned `GCA_000756815`, IMG `2627853956` and BV-BRC `1034943.4`, with the retained contig label and description. The page identifies that reference as automated DiASPora annotation; the record preserves it as source-reported evidence, not experimental equivalence. Native BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:3290` additionally names LegA, `GCA_000756815.1`, `PRJEB6598` and `SAMEA2747211`. The dotted BV-BRC suffix and IMG identifier are database identities, not an NCBI accession version or a taxon ID.

5. **GOLD provenance chain.** Full native rows `data/gold/organisms.jsonl.gz:37203`, `projects.jsonl.gz:31176` and `analyses.jsonl.gz:45641` establish `Go0044362 -> Gp0044362 -> Ga0072353`. Both organism culture-collection and organism-strain fields independently say DSM 24804. The project names `PRJEB6598` and `SAMEA2747211`; the analysis names `GCA_000756815.1` and IMG `2627853956`. The local CAFI matcher accepts DSM 24804 and the existing DSM-24804 CURIE. This supports both provenance-distinct copies of each GOLD assertion. Go/Gp/Ga remain correctly typed related records. The live GOLD analysis page was unavailable; the complete pinned source projection, not a live page, supplied this check.

6. **NCBI assembly corroboration.** Exact-species Assembly ESearch returned two records; both full summaries were read. The [LegA assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000756815.1/) is from type material and explicitly pairs GenBank `GCA_000756815.1` with RefSeq `GCF_000756815.1`, BioSample SAMEA2747211 and GenBank project PRJEB6598. Pinned GenBank/RefSeq rows independently agree. This authority-reported pairing corroborates the source links; it does not justify silently adding a version to BacDive's unsuffixed assertion.

7. **StrainInfo evidence.** Native `data/straininfo/records.jsonl.gz:294753`, `strain_links.tsv:98809`, related rows 244532-244533 and the [public rich-record API](https://api.straininfo.dsmz.de/v2/data/strain/max/396864) agree on SI-ID 396864, its own available DSM 24804 deposit SI-DP 903451, BacDive 6788, species/LPSN IDs and published-online status. [DataCite's DOI record](https://api.datacite.org/dois/10.60712/SI-ID396864.3) verifies version 3 of the strain dataset and its StrainInfo destination. The DOI is not a deposit identifier or literature paper. Neither the pinned nor live rich record supplies a sequence object; the two typed related records are supported without transferring another source's genomes into StrainInfo provenance.

8. **Attestations and scope.** The eight attestation tuples match their owning inventories: NCBITAXON 1 NAME, LPSN 1 NAME, GTDB 2 GENOME, BACDIVE 1 STRAIN, MEDIADIVE 1 MEDIUM, GOLD 3 ORGANISM, MADIN 4 TRAIT_ASSERTION and BACTOTRAITS 8 TRAIT_ASSERTION. Respective supporting rows include `mediadive_taxa.tsv:112`, `gold_organisms.tsv:471`, `madin_taxa.tsv:656` and `bactotraits_taxa.tsv:85`. The MediaDive row names [medium 585](https://mediadive.dsmz.de/medium/585), also linked by DSMZ/BacDive. No phenotype, clinical property or causal mechanism is inferred from these counts.

## Completeness

No consequential omission was established within the pinned model and its conservative strain-join rules. `strain_count: 1` equals the complete BacDive listing for this taxon; the backbone contains no child taxa to contribute additional classified strains.

The ignored-inclusive search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using taxon ID, both genus spellings, slug, culture aliases and StrainInfo IDs. A second compressed-file search covered the exact genome, project, sample, GOLD-chain and marker strings. Source manifests named `SOURCE.json` were excluded from these candidate searches. The searches found no target ATB crosswalk or additional eligible deposit-specific StrainInfo sequence assertion in those roots. This is not a claim of worldwide sequence absence or an exhaustive inspection of ignored external snapshot archives outside these roots.

The following candidates were inspected and not incorrectly attached to the type strain:

- GTDB's strain identifiers are LegA or missing, not eligible full CAFI deposit tokens. The native RefSeq partner is therefore corroborating catalog evidence, not an omitted GTDB deposit-join assertion under the current importer contract.
- GOLD Go0023406 has bare LegA, Go0102104 has FF2, and Go0614038 has CSUR P146. The pinned matcher rejects each as a genome-join key. CSUR P146 remains a valid source-reported alias in the record; matcher rejection is not a biological rejection of the deposit. No identity was inferred from taxonomy alone.
- The FF2-associated chain `Go0102104 -> Gp0102104 -> Ga0072351`, BV-BRC 1034943.3 and GCA_000756695.1 are not automatically the LegA strain. Its historical RefSeq partner GCF_000756695.1 is suppressed for a missing strain identifier. Shared species or equal assembly lengths do not establish strain identity.
- Broad numeric matches in two unrelated GTDB assembly statistics and the NCBI merged-ID table were rejected after full-row inspection. Five extra project-string hits were for PRJEB65989, not PRJEB6598.
- Both SeqCode name candidates were inspected through their native API. [Legionella massiliensis](https://api.seqco.de/v1/names/10647.json) is marked ICNP-valid; [Tatlockia massiliensis](https://api.seqco.de/v1/names/42578.json) is an automated-discovery entry without a registered description or type definition. Their existence does not license a new nomenclatural claim or an inferred source mapping.

The GOLD count of three comes from the kg-microbe attestation inventory, whereas the independent native workbook projection contains four matching organisms. `src/taxonmech/extract.py` explicitly uses those different inputs for counts and strain links. The count is not a claim to enumerate the complete native GOLD catalog. Similarly, the BacDive strain inventory's zero medium count and the taxon-level MediaDive count of one are different source relationships; the omitted optional strain medium count is not a no-growth assertion.

The exact-species, rRNA/16S-filtered Nuccore search returned five records, all inspected: JF779685.1, NR_109415.1, KJ677097.1, MK910197.1 and PZ477884.1. The latter three concern separate clones/isolates, not evidence to expand the LegA deposit links. Other gene accessions listed by DSMZ are contextual leads, not claims already made by this YAML. Empty optional mechanism/evidence slots do not require fabricated graph content. iModulonDB was not applicable to the record's identity and source-link assertions.

Before this report, `rg --no-ignore --hidden` found no target ID/name/slug in `reports/yaml_record_review` or `history`; filesystem `find` independently located the target YAML. The inline seed event is present. No separate history event was created for this read-only review.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The live-view limitations and narrower source-specific projections above remain explicit; a pass does not certify live GTDB/GOLD freshness, physical equivalence of every linked genome, or whole-corpus reproducibility.

## Recommended Edits

None required for this record on the inspected evidence. Preserve the generated YAML, accession versions, typed namespaces, source-qualified taxonomy differences and provenance-distinct assertions.

Optional future enrichment of the LPSN-specific type list belongs in the upstream kg-microbe LPSN transform and `src/taxonmech/extract.py`, invoked by `scripts/extract_source_inventory.py`; it must not be implemented by editing the generated record. Any change to CAFI eligibility or genome-join behavior belongs in `src/taxonmech/genome_sources.py` and the owning source importer, with regression tests. Record emission remains owned by `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; none of these changes is authorized by this review.

## Follow-up Checks

- Retry the live GTDB species and GOLD analysis views at a future source refresh; compare the same explicit identifiers and preserve snapshot dates.
- Before adopting additional aliases or links, require the appropriate source-owned evidence and full CAFI accession match. For StrainInfo sequences, require the sequence to name SI-DP 903451 itself; a strain-level association is insufficient.
- Any later authorized extraction/seeding change should use the documented dry run and single-record canary, repeat `just validate` and `just validate-strict`, then run full `just verify-corpus` and `just qc` before release.

## Additional Notes

This review used public, unpaid source reads and local committed evidence. No private contacts, provider-credit jobs, GitHub operations, commits, record promotions or regeneration were performed. Nomenclatural medical-use wording is reported as source terminology, not medical or biosafety advice. The parallel session is closed and Git reports one worktree; work stayed on the existing dedicated review branch. Eukaryota records and their completed reviews were left untouched.
