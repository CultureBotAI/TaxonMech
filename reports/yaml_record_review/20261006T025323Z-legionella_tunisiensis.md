# YAML Record Review: Legionella tunisiensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/legionella_tunisiensis.yaml`
- Started UTC: 2026-10-06T02:50:30Z
- Finished UTC: 2026-10-06T02:53:23Z
- Verdict: pass

## Target

Read the entire 306-line generated `TaxonRecord` for `NCBITaxon:1034944`, Legionella tunisiensis: `SPECIES`, `BACTERIA`, parent `NCBITaxon:445` (Legionella), genetic code 11, `EXACT` grounding and `SEEDED` mapping status. The record contains one LPSN nomenclature entry, one GTDB mapping, three source-qualified synonyms, two xrefs, one type strain, eight attestations and one inline seed event. Its strain contains two assembly assertions, three genome-record assertions and nine related-record assertions. Fourteen assertions do not mean fourteen distinct genomes.

The identifier and slug agree with `data/taxa/PATHS.tsv:14231`, `curation/seed_scope.tsv:4045` and `curation/legacy_page_paths.tsv:849`. The scope reason names eight sources including NCBI; the inline event is dated `2026-09-13T17:54:04Z`. The target, inventories, scope, history and prior reports remain unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/legionella_tunisiensis.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/legionella_tunisiensis.yaml --out /private/tmp/tunisiensis-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured inventory inspection matched the identity, complete lineage, NCBI synonym scopes, source rows, attestations and scope/path references. Exact multiset comparison matched all fourteen strain-linked objects, including the nested StrainInfo evidence and provenance-distinct repeated identifiers. These are bounded checks, not full-corpus reproduction.
- Two gitignore-independent, compressed-file searches returned 55 identity/deposit candidates and 24 crosslink candidates. The second set was wholly contained in the first. Read every candidate row in full, with lossless common-field grouping for native JSON records.
- `git diff HEAD --` for local guidance and maintained inputs, followed by `git diff --exit-code HEAD --` for the target and source/configuration/history surfaces, returned no differences. Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance and history gates, rendering/site drift, README statistics, publication-size and vendored-file gates. No generated products were regenerated.
- `just validate-products` is not applicable to this record, which has no curator-added causal-graph nodes. No undocumented focused term/history validator was substituted.

## Identity and Grounding

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034944&retmode=xml) confirms the scientific name, species rank, bacterial division, parent 445 and genetic code 11. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034944) supplies the same identity and full ancestor-ID chain including root. The record's nine ancestors are root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Legionellales, Legionellaceae and Legionella. Every carried label and rank agrees with the pinned backbone.

`data/raw/ncbitaxon_taxa.tsv:221762` and native name rows `data/catalog/ncbi_names-0005.jsonl.gz:31183` through 31185 support the scientific name, former LegM label and authority string. The two NCBI names correctly remain related synonyms. Exact-ID scans of `ncbi_merged_ids.tsv` and `dropped.tsv` found no retirement or drop for this taxon; no child taxa were found in the pinned backbone.

The [LPSN entry](https://lpsn.dsmz.de/species/legionella-tunisiensis) identifies record 790329, Campocasso et al. 2012, valid publication under the ICNP and correct-name status, including its source-specific medical-use qualification. No contrary ruling was encountered for the pinned legitimate flag. GTDB's Tatlockia placement is represented separately; it does not rewrite the NCBI parent or assert that a Tatlockia combination is validly published under the ICNP.

## Evidence

1. **Nomenclature and type identity.** `data/raw/lpsn_names.tsv:27306` reproduces all nomenclature values, the two DOIs, PMID 22307511 and `INSDC:JF779686`. LPSN names LegM, DSM 24805 and CSUR P145 as the type. The imported LPSN-specific designation list contains DSM-24805, while the strain entry also retains CSUR P145 and LegM. The narrower source-specific list does not lose the type's identity or those aliases from the record. Six pinned NCBI type-material rows at `data/raw/ncbi_type_material.tsv:1772` onward corroborate the same designations and source spellings.

2. **Literature and marker accession.** The complete author abstract from [PMID 22307511](https://pubmed.ncbi.nlm.nih.gov/22307511/) verifies [DOI 10.1099/ijs.0.037853-0](https://doi.org/10.1099/ijs.0.037853-0) and expressly assigns LegM = DSM 24805 = CSUR P145 to tunisiensis. LegA = DSM 24804 = CSUR P146 belongs to the separately described massiliensis species. The publisher page for [DOI 10.1099/ijs.0.050427-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.050427-0) verifies the subsequent notification list, not a second characterization experiment. Full GenBank metadata for [JF779686.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779686.1) describes a 1,507-base partial 16S rRNA gene from type strain LegM, taxon 1034944, and cites the same primary paper. [NR_109416.1](https://www.ncbi.nlm.nih.gov/nuccore/NR_109416.1) explicitly derives from that marker and names DSM:24805. The record's unsuffixed INSDC citation is preserved; a marker is not counted as a genome.

3. **GTDB mapping.** `data/raw/gtdb_mappings.tsv:1405` and `gtdb_species.tsv:174547` specify `GTDB:s__Tatlockia_tunisiensis`, `skos:closeMatch` and one genome. Native row `data/catalog/gtdb_genomes-0005.jsonl.gz:17895` supplies the sole matching `RS_GCF_000308315.1` entry, classified as Tatlockia tunisiensis and carrying NCBI species/taxon 1034944. This supports the mapping and source-qualified synonym/xref. The GTDB tree page was inaccessible through the web tool; verification used the full pinned primary metadata, not an asserted live-release census.

4. **BacDive identity and direct links.** `data/raw/bacdive_strains.tsv:6672`, native `data/bacdive/records.jsonl.gz:6671` and the [BacDive 6789 page](https://bacdive.dsmz.de/strain/6789) agree on LegM, DSM 24805, CSUR P145, type status and species classification. Reference 66792 explicitly supplies unversioned GCA_000308315, IMG 2551306136 and BV-BRC 1034944.5, with the retained contig-level description. The page identifies that reference as automated DiASPora annotation. These remain source-reported relationships, not proof of experimental genome equivalence. Native BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:3292` independently names LegM, GCA_000308315.1, PRJEB109 and SAMEA2271965. Row 3291 is the deprecated 1034944.4 record, not a replacement for the current asserted identifier.

5. **GOLD chain and repeated organism assertions.** Native `data/gold/organisms.jsonl.gz:19801`, `projects.jsonl.gz:19276` and `analyses.jsonl.gz:12810` establish `Go0023407 -> Gp0023407 -> Ga0020806`. The organism's culture-collection field names DSM 24805; its strain field says LegM. Only the eligible culture-collection match supports this chain. The project supplies PRJEB109 and SAMEA2271965; the analysis supplies GCA_000308315.1 and IMG 2551306136. Native organism row 37205 is Go0044364, with DSM 24805 in both culture-collection and strain fields. Its two provenance-distinct organism assertions are correctly retained without copying the other organism's project or genome chain onto it. The local CAFI functions accept DSM 24805 and its existing CURIE, but not bare LegM or CSUR P145. Go0614039 at organism row 444771 contains CSUR P145 and is consequently not a deposit-joined assertion under the pinned rules. The unavailable live GOLD analysis page was not substituted with an inferred relationship.

6. **Assembly corroboration.** Exact-species NCBI Assembly ESearch returned one result; its full summary was read. The [assembly authority record](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000308315.1/) identifies type strain LegM, assembly ASM30831v1, BioSample SAMEA2271965 and GenBank project PRJEB109. It explicitly pairs GCA_000308315.1 and GCF_000308315.1. Pinned GenBank row `data/catalog/ncbi_genbank-0000.jsonl.gz:7594` and RefSeq row `ncbi_refseq-0000.jsonl.gz:6515` agree. The assembly is contig-level, not a finished chromosome. This explicit pairing corroborates the imported links; it does not license appending a version to BacDive's unsuffixed accession or inferring additional strain joins from an accession stem.

7. **StrainInfo identifiers and evidence.** Native `data/straininfo/records.jsonl.gz:302070`, `strain_links.tsv:98810`, related rows 244534-244535 and the [public rich-record API](https://api.straininfo.dsmz.de/v2/data/strain/max/404181) agree on SI-ID 404181, its own available DSM 24805 deposit SI-DP 911301, BacDive 6789, species/LPSN IDs, type status and published-online status. The deposit is not flagged erroneous and its collection is not deprecated. [DataCite metadata](https://api.datacite.org/dois/10.60712/SI-ID404181.3) verifies DOI 10.60712/SI-ID404181.3 as version 3 of the strain dataset. Neither the native nor live rich record has a sequence object. Thus the strain and deposit related records are supported, without attributing the other resources' genomes to StrainInfo.

8. **Attestations and audit state.** All eight source/count/unit tuples match their inventories: NCBITAXON 1 NAME, LPSN 1 NAME, GTDB 1 GENOME, BACDIVE 1 STRAIN, MEDIADIVE 1 MEDIUM, GOLD 3 ORGANISM, MADIN 3 TRAIT_ASSERTION and BACTOTRAITS 9 TRAIT_ASSERTION. Supporting count rows include `mediadive_taxa.tsv:113`, `gold_organisms.tsv:472`, `madin_taxa.tsv:657` and `bactotraits_taxa.tsv:86`. The MediaDive inventory names medium 585, also linked on the inspected BacDive page. These counts are not summed or treated as measured phenotypes. The seed event and `SEEDED` status do not claim that a human curator reviewed this record.

## Completeness

No consequential gap was established within the pinned model. One inventoried BacDive strain is fully listed, with no descendant-taxon strains to add. All fourteen imported link assertions are present and correctly typed; projects, samples, GOLD Go/Gp/Ga objects and StrainInfo IDs remain outside genome counts.

The ignored-inclusive searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the taxon ID, both genus spellings, slug, DSM/CSUR aliases, BacDive/StrainInfo identifiers, assembly and genome accessions, whole project/sample identifiers, marker and GOLD chain IDs. `SOURCE.json` manifests were excluded from candidate searches. No target ATB crosswalk, additional eligible StrainInfo sequence link or project chain for Go0044364 was found within those searched roots. This does not claim absence from external snapshot archives or worldwide databases.

The GTDB native strain field contains only LegM, which fails the pinned full-deposit matcher. Its RefSeq accession is useful corroborating catalog evidence but is not an omitted eligible GTDB strain-join assertion. The rejected CSUR alias remains in the record as source-reported identity; its ineligibility as a machine-join key is not a biological judgment against the deposit. The source-only zero BacDive medium count and the taxon-level MediaDive count of one describe different imported relationships; omission of the optional strain-level medium count is not a no-growth claim.

Both SeqCode name candidates were inspected through their native API: [Legionella tunisiensis](https://api.seqco.de/v1/names/10675.json) is marked ICNP-valid and identifies the same type, while [Tatlockia tunisiensis](https://api.seqco.de/v1/names/43504.json) is an automated-discovery entry without a registered description or type definition. Those entries do not independently establish a new validated combination or require an inferred source mapping.

Numeric search collisions were rejected after full-row inspection: NCBITaxon 911301 is Acinetobacter sp. KZ_AalM_Mm6, whereas this record's 911301 is a StrainInfo deposit ID. The unrelated SI-ID 144680 record contains SI-DP 404181 and fungal sequence MW577268; it is not this record's SI-ID 404181. No sequence was transferred across identifier namespaces.

Exact-species rRNA/16S-filtered Nuccore search returned only JF779686.1 and NR_109416.1, both inspected. This was not an unrestricted nucleotide census or an alignment analysis. Empty optional mechanism/evidence slots do not require invented content; iModulonDB was not applicable to the claims in this record.

Before this report, `rg --no-ignore --hidden` found no target ID, name or slug in `reports/yaml_record_review` or `history`. The inline seed event is present. Per the review skill's write boundary, no separate history record was created.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The pass is bounded by the source and validation checks above; it does not establish whole-corpus reproducibility, live GTDB/GOLD freshness or physical identity of every database genome record.

## Recommended Edits

None required on the inspected evidence. Preserve the generated YAML, original accession versions, typed namespaces and provenance-distinct organism assertions.

Optional future enrichment of the LPSN-specific type-designation list belongs in the upstream kg-microbe LPSN transform and `src/taxonmech/extract.py`, invoked by `scripts/extract_source_inventory.py`, not in this generated record. Any authorized change to GOLD-chain or CAFI matching belongs in `src/taxonmech/gold_genomes.py` or `src/taxonmech/genome_sources.py` with focused regression tests. StrainInfo sequence enrichment must follow its own deposit-evidence importer rather than reuse another resource's associations. Record emission remains owned by `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`.

## Follow-up Checks

- At a future source refresh, retry the inaccessible GTDB tree, GOLD analysis and DSMZ deposit pages. LPSN/BacDive pages, primary literature, pinned native metadata and the live StrainInfo deposit response support the present verdict despite those access limits.
- Require a primary source chain before adding another genome link. Keep Go0044364 separate from Go0023407, and require any StrainInfo sequence to explicitly name SI-DP 911301.
- After any later authorized source change, use the documented extraction dry run and single-record seed canary, repeat `just validate` and `just validate-strict`, then run full `just verify-corpus` and `just qc` before release.

## Additional Notes

The complete target and relevant native rows were inspected; publication checking used the complete author abstract and the notification publisher page, not unread full article bodies. Web-rendered BacDive content may be older than the committed source snapshot; no live freshness claim is made for that page. The native BacDive projection retains its own DOI version and the matching genome fields. Nomenclatural medical-use wording is source terminology, not medical or biosafety advice.

This review used public unpaid reads. Only this new timestamped report was written; no records, sources, history, prior reports, rendered pages or Eukaryota reviews were changed. No commits, GitHub operations, external contacts, lifecycle promotions or paid research were performed. The full corpus-review goal remains incomplete.
