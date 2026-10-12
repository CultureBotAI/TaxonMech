# YAML Record Review: Cryobacterium sp. MB-5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/cryobacterium_sp_mb_5.yaml`
- Started UTC: 2026-10-06T23:32:06Z
- Finished UTC: 2026-10-06T23:37:26Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. NCBITaxon:1035348 denotes Cryobacterium sp. MB-5, rank SPECIES, domain BACTERIA, parent NCBITaxon:2649013. It contains ten root-first ancestors, genetic code 11, EXACT grounding, SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation and its seed event.

There are no synonyms, nomenclature assertions, taxonomy mappings, strain listing, genome assertions, phenotype claims, citations or causal graph. The generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/cryobacterium_sp_mb_5.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/cryobacterium_sp_mb_5.yaml --out /private/tmp/cmb5-strict.tsv`: exit 0, one file and zero errors. The actual emitted TSV was read and contains only its header.
- Exact backbone, every ancestor, children, seven other raw inventories, PATHS, scope and source-attestation comparisons passed. Exact type-material, merged-ID and dropped-ID inventories have no target row.
- All 117 broad-search candidates were read losslessly: 84 JSON objects and 33 TSV rows. Five SOURCE.json files were fully parsed; ignored-independent history filenames and secondary accession/literature searches were checked.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0, all 28 rows inspected before open web research. No covered organism/dataset matches this target; iModulonDB is not applicable, not negative evidence.
- Live NCBI taxonomy XML/Datasets, exact Assembly/nuccore searches, full marker metadata excluding bases/translations and a Datasets genome lookup succeeded.
- The related publication's PubMed bibliographic metadata/abstract and publisher abstract were inspected. The publisher exposes an abstract/purchase page, not accessible strain-level full text. A search-indexed teaching-slide table is only a lead and was not used as primary phenotype evidence.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, paper full text or raw experimental data. Bounded comparisons are not corpus reproduction.

## Identity and Grounding

The exact backbone at `data/raw/ncbitaxon_taxa.tsv:222035`, name object at `data/catalog/ncbi_names-0005.jsonl.gz:31510`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035348&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035348) agree on identifier, label, rank, parent, domain and genetic code.

Every ancestor ID, label and normalized rank agrees: root (1); cellular organisms (131567); Bacteria (2); Bacillati (1783272); Actinomycetota (201174); Actinomycetes (1760); Micrococcales (85006); Microbacteriaceae (85023); Cryobacterium (69578); unclassified Cryobacterium (2649013). Datasets independently includes root ID 1. The final parent has NO_RANK.

Pinned synonyms and live alternate-name content are empty, and the pinned child set is empty. NCBI species rank does not imply formal nomenclatural standing, a named-species assignment or type-strain status. The short MB5/MB-5 label alone cannot identify a strain across genera.

## Evidence

The single NCBITAXON NAME attestation agrees with snapshot 2026-09-13. `data/taxa/PATHS.tsv:14526` pins the stem; `curation/seed_scope.tsv:322307` agrees with the event reason. The parsed raw, ATB and StrainInfo extraction timestamps are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum agrees with the seed event under the inspected `src/taxonmech/seed.py` rule. This report does not promote SEEDED or provide human sign-off.

The exact nuccore search returned only [JF790972.1](https://www.ncbi.nlm.nih.gov/nuccore/JF790972.1), UID 335331582, a 1,289-bp partial 16S rRNA sequence. Its source explicitly links strain MB-5 to taxon 1035348, cryoconite-hole soil at Midre Lovenbreen glacier, and Svalbard: Ny-Alesund. The 8-Apr-2011 submission names Singh, Singh and two Dhakephalkar authors at BITS Goa. Its research reference remains marked Unpublished. No culture deposit, BioSample, assembly or CDS is supplied. The submitter's Indian address is not the isolation location; genetic code 11 comes from taxonomy rather than this noncoding marker.

[PubMed 24283367](https://pubmed.ncbi.nlm.nih.gov/24283367/) and the [publisher abstract](https://academic.oup.com/femsle/article-abstract/351/1/14/501000) identify Singh, Hanada, Singh and Tsuda's 2014 article, Antifreeze protein activity in Arctic cryoconite bacteria, DOI 10.1111/1574-6968.12345. The abstract concerns a multi-strain screening study, not a universal Cryobacterium phenotype. Search results connect JF790972 to this publication and suggest the isolate alias Cry-5, but the exact table and experimental conditions were not verified in primary full text. Neither positive nor negative antifreeze activity is assigned to MB-5 here.

Exact Assembly search returned zero with a phrase-not-found warning. [Datasets genome](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035348/dataset_report) independently returned an empty object. These are dated bounded results, not proof that no genome exists anywhere.

## Completeness

The initial taxon-ID, separator-tolerant MB5 and stem searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included.

The 117 candidates comprise 15 BV-BRC objects, 11 name objects, seven GOLD objects, eight GTDB objects, 36 current/historical assembly objects, seven StrainInfo objects and 33 TSV rows. Three are exact target identity/scope rows. The other rows are unrelated identities, numeric coincidences or an unresolved short-label deposit lead:

| Candidate group | Inspected distinction |
|---|---|
| Ten other name concepts and corresponding backbone/scope rows | Massilia sp. MB5 (2919578), Acinetobacter sp. MB5 (2069438), Photobacterium sp. MB5 (671541), Bacillus sp. MB-5 (161534), Bacillus sp. MB-5(2016) (1857934), Burkholderia sp. MB5 (1617798), methanogenic archaeon LGM-MB5 (1423967), bacterium IBRC-M MB5 (1437579), Methanobacterium sp. Mb5 (1460266), Micrococcus sp. IK-MB5-518F (643131). None is taxon 1035348. |
| Acinetobacter MB5 | GCA/GCF_003261585.1, SAMN08295223, PRJNA428584, BV-BRC 2069438.3. GTDB calls it Acinetobacter sp003261585; GOLD organism Go0403289 uses Acinetobacter mangrosoli with taxon 469. GOLD Gp0294110 and Ga0392977/IMG 3006147052 preserve the same sample/project chain, not a Cryobacterium identity. |
| Massilia MB5 | GCA_022492935.1, SAMN26146637, PRJNA809127, BV-BRC 2919578.4 and deprecated 2919578.6. GTDB uses Rugamonas sp001191005. Historical GCF_022492935.1 is suppressed, non-live date 2026-07-23, with unverified-source-organism exclusion. These external classification/status differences do not establish an MB-5 match. |
| Corynebacterium pseudotuberculosis MB5 | Taxon 1719, BV-BRC 1719.2933, GCA/GCF_026650845.1, SAMN22442118, PRJNA758392. |
| Serratia nevei MB5 | Taxon 2703794, BV-BRC 2703794.87, GCA/GCF_034093155.1, SAMN37774686, PRJNA1026344. |
| Mycoplasmopsis bovis P-MB5 | Taxon 28903, BV-BRC 28903.773, GCA/GCF_037137155.1, SAMN40260450, PRJNA1083793; its GTDB source translation table is 4, not target code 11. |
| Two Listeria monocytogenes MB5 samples | Taxon 1639: GCA_902838455.1/SAMEA6786264/PRJEB35939 and GCA/GCF_018336735.1/SAMN14260728/PRJNA609411. The first RefSeq assembly is historical/suppressed, non-live 2025-09-09; the second is current. An unrelated BV-BRC type flag is not transferred or independently endorsed. |
| Other assembly-name matches | Pseudomonas aeruginosa MB5, taxon 287, GCA_021601425.1/SAMN17025079/PRJNA514245; and Mycobacterium tuberculosis variant bovis, taxon 1765, GCA_001369335.1/SAMEA2794687/PRJEB7273, whose assembly title says caprae MB5 but strain field says MB4. Its RefSeq is suppressed, non-live 2024-03-17. Neither inconsistency changes this target. |
| Numeric accession matches | Campylobacter jejuni 305166, taxon 197, GCA_010353485.1/SAMN13268831/PRJNA505131; and M. tuberculosis ERR1035348, taxon 1773, BV-BRC 1773.18358, ATB SAMEA3558881/ERR1035348/ERZ9334531. Accession digits are not taxon identifiers. |
| Environmental GOLD projects | Gp0571582/SAMN51146281/PRJNA1317322 and Ga0496968/IMG 3300049750 concern Russell Ranch soil community MB5; Gp0586031/SAMN13316691/PRJNA590073 concerns maize soil community MB5 in China. These are community projects/analyses, not isolate genomes. |

RefSeq/GTDB BioProject PRJNA224116 is retained as source-specific umbrella metadata, not substituted for each GenBank study. GOLD organism, project, analysis and IMG identifiers are distinct object types.

Ten Escherichia coli samples, taxon 562 and BioProject PRJNA218110, account for seven BV-BRC rows, ten current GenBank rows, eight historical GenBank rows, ten ATB rows and GOLD project Gp0386905/Go0502628. The latter concerns SAMN10353487. Full native values establish:

| BioSample | E. coli strain | Current GenBank | ATB analysis |
|---|---|---|---|
| SAMN10353480 | PNUSAE019760 | GCA_003768965.2 | ERZ9092849 |
| SAMN10353481 | PNUSAE019759 | GCA_003757205.2 | ERZ9092850 |
| SAMN10353482 | PNUSAE019758 | GCA_016555905.1 | ERZ9092852 |
| SAMN10353483 | PNUSAE019757 | GCA_003769405.2 | ERZ9092855 |
| SAMN10353484 | PNUSAE019756 | GCA_003760165.2 | ERZ9092858 |
| SAMN10353485 | PNUSAE019755 | GCA_003768905.2 | ERZ9092859 |
| SAMN10353486 | PNUSAE019325 | GCA_016556165.1 | ERZ9092870 |
| SAMN10353487 | PNUSAE019769 | GCA_003756685.2 | ERZ9092861 |
| SAMN10353488 | PNUSAE018210 | GCA_016555885.1 | ERZ9092863 |
| SAMN10353489 | PNUSAE015625 | GCA_003746545.3 | ERZ9092864 |

The seven older .1 assemblies are replaced, with non-live date 2020-03-07; GCA_003746545.2 was subsequently replaced on 2025-02-22. BV-BRC retains older .1 accessions. Every listed ATB row has PASS filters and an available FASTA, which does not change its identity. These accession fragments cannot supply MB-5 strains or genomes.

Six StrainInfo candidates explicitly denote fungi: ATCC 56409-56413, SI-IDs 260531-260535, have Agaricus/Agaricus bisporus identities and MB5-prefixed designations; FGSC 8293, SI-ID 331809, is Neurospora crassa mb5. No fungal record is reviewed or edited here. The remaining SI-ID 13307/siDP 49914 record lists LMG 19212, R-10003, Leisner MB5 and MB 5, but supplies no taxon object. It was read completely and is an unresolved deposit-name lead, not a demonstrated Cryobacterium match. Exact web searches did not establish that join; a bare MB5 designation is insufficient.

Secondary searches for JF790972, PMID 24283367, the full DOI and separator-tolerant Cry-5 found no content matches in the same bounded roots. Metadata and history filenames were separately checked. This is not a claim that the literature or deposit does not exist externally.

Zero inventoried BacDive strains agrees with the exact inventory and empty descendant set; it does not deny that MB-5 is a biological isolate. No missing required nomenclature, mapping, strain or genome assertion was established. Marker, literature and experimental fields are optional for this seeded taxon record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated assertions. The unresolved LMG designation and inaccessible strain-level paper text are bounded enrichment uncertainties, not evidence that an existing assertion is false.

## Recommended Edits

None required. Leave generated YAML and lifecycle status unchanged. Do not import MB5 homonyms, infer type status, collapse assembly versions or represent JF790972.1 as a genome.

Future supported strain/deposit enrichment belongs in maintained source ingestion, including `scripts/extract_source_inventory.py`, followed by the documented seeder workflow. Optional literature needs a maintained representation that survives regeneration. Trait, habitat, medium and interaction observations belong in the respective sibling repositories.

## Follow-up Checks

For optional enrichment, verify LMG 19212 at the collection authority before any deposit join, and obtain lawful primary full text to confirm the marker/alias and strain-specific assay conditions. Do not transfer the abstract's multi-strain findings to MB-5.

After authorized upstream changes, repeat both exact-target validators and read the emitted TSV. Source/generator changes also require the documented canary and full `just verify-corpus`/QC gates; no target-only reproduction gate is asserted. Future genome associations require an exact supported sample/deposit chain.

## Additional Notes

Guidance and generation/history boundaries were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target remains byte-identical to its initial complete read. Only this new timestamped report is written; no source input, YAML, generated product, prior report, history record, event or lifecycle status is changed. Eukaryota remains untouched.
