# YAML Record Review: Staphylococcus sp. YIM 94352

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_yim_94352.yaml`
- Started UTC: 2026-10-06T08:55:43Z
- Finished UTC: 2026-10-06T08:57:29Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035041`, Staphylococcus sp. YIM 94352. It asserts species rank, bacterial domain, parent `NCBITaxon:91994`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence, strain/genome relationships, definition or causal graph are asserted.

`data/taxa/PATHS.tsv:14333` uniquely resolves the ID/stem. `curation/seed_scope.tsv:322146` supplies the NCBI-only inclusion rule dated 2026-09-13. A matching genus or numeric accession fragment does not identify the target isolate.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_sp_yim_94352.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_sp_yim_94352.yaml --out /private/tmp/styim94352-validation.tsv`: exit 0; one file, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured comparisons verified full pinned identity, lineage, genetic code, unique path/scope, attestation and inline seed reason. No classified child was found in the backbone.
- Exact-ID scans found no target row in seven other source inventories or the NCBI type-material, merged-ID and dropped tables.
- Initial and marker-expanded ignored-inclusive compressed-source searches returned the same 28 row addresses. All complete rows were read and reconciled by address. An ignored-inclusive ID/full-label/slug search found no prior target report or separate history artifact.
- The review skill/checklist and validator recipes were reread this turn. Previously inspected guidance and schema remain unchanged against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The pre-report tracked-file diff across records, maintained inputs, history, code, configuration and guidance exited 0.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file checks. No undocumented focused term/reference/history validator was invented. Inline history was checked; no separate target history artifact exists within the searched history root.
- `just validate-products` is not applicable without curator-added causal-graph nodes. This review is not corpus release certification.

## Identity and Grounding

Complete live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035041&retmode=xml) confirms the exact identifier/name, species rank, bacterial division, parent 91994 and genetic code 11. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035041) agrees and supplies all ten ancestor IDs, including root.

The chain is root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Staphylococcaceae, Staphylococcus and unclassified Staphylococcus. Every pinned ancestor ID, label and rank agrees with the YAML; live taxonomy confirms all non-root ancestors. Order `NCBITaxon:1385`, family `NCBITaxon:90964`, genus `NCBITaxon:1279` and parent `NCBITaxon:91994` agree. The inspected [NCBI parent tree](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=91994) lists YIM 94352 among unclassified Staphylococcus.

The strain designation in the label does not justify replacing the authority-assigned species rank with `STRAIN`; the no-rank parent does not contradict it. `EXACT` denotes NCBI concept grounding, not formal nomenclatural validation or human review. The record is not Staphylococcus haemolyticus or a general Staphylococcus concept.

## Evidence

1. **Pinned provenance.** Complete `data/raw/ncbitaxon_taxa.tsv:221853` supports identity, rank, parent, code and snapshot 2026-09-13, with empty synonym and retirement-target fields. Complete `data/catalog/ncbi_names-0005.jsonl.gz:31276` supplies the scientific name/ID and empty unique name. The attestation counts one `NAME`, not a strain, genome or biological property. The scope rule agrees with the inline `seed_from_sources` / `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z.

2. **Marker identity.** Exact Nuccore search returned UID 333798106. Complete metadata, features and references for [JF792180.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792180.1), excluding sequence bases, identify a 681-base 16S rRNA gene partial at both ends. The organism, strain YIM 94352 and `taxon:1035041` agree. Sequence taxonomy includes Caryophanales, Staphylococcaceae and Staphylococcus. C. Chen submitted it on 7 April 2011 through the Yunnan Institute of Microbiology / Yunnan University. Creation and update dates are 28 May 2011 and 26 August 2015. Inspected qualifiers contain no culture-collection, BioSample or assembly identifier. The marker does not establish a genome or registered-deposit relationship.

3. **Publication boundary.** GenBank marks the associated Qijiaojing Lake bacteria/enzyme study unpublished and supplies no DOI or PMID. Name search yielded NCBI taxonomy tree leads; the parent tree was inspected as source text. The JF792180/Staphylococcus web search returned no results. These bounded checks do not establish worldwide publication absence. The study title alone does not demonstrate isolate-specific enzyme activity, habitat or culture requirements.

4. **Imported coverage.** The inspected BacDive inventory has no exact target row, and the pinned backbone has no classified child. `strain_count: 0` denotes imported coverage, not the isolate's nonexistence. Exact assembly search `txid1035041[Organism:noexp]` returned zero with no-items/phrase-not-found diagnostics. This does not exclude assemblies under other classifications or outside NCBI.

5. **Rejected matches.** Twenty-five other source rows concern Staphylococcus haemolyticus, Mycobacterium tuberculosis, Bacteroides salyersiae, an Actinomarina MAG, Streptococcus pneumoniae and plant/fungal metatranscriptome projects. Complete rows were inspected. Accession fragments or an assembly-size statistic caused the matches; none establishes a target culture/genome relationship. A shared genus in the haemolyticus candidates does not overcome the different taxon, strain designation and provenance.

## Completeness

No consequential omission was established under the seeded-record model. Optional enrichment slots may remain empty without explicit source-backed relationships. The partial marker alone does not establish a registered culture or genome. No traits, habitats or culture requirements were inferred from the study title or from related Staphylococcus species.

Local source searches used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. Queries covered the unbounded taxon number, full label, slug and YIM94352 separator variants; the expansion added JF792180 and its versioned spelling. Both returned three target provenance rows and twenty-five unrelated matches, with no additional eligible target culture/genome link. Ignored files and compressed rows were included; separate snapshot archives and every external database were not searched.

Exact-ID scans covered BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. Prior-report/history searches included ignored files. iModulonDB was not applicable to this identity-only record; neither genus-level proximity nor unrelated metatranscriptome projects constitute target expression evidence. No sequence alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets were not used as evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected evidence supports the represented identity, lineage, grounding, provenance and source coverage. This does not certify formal nomenclature, biological traits, universal assembly absence or full-corpus reproducibility.

## Recommended Edits

None required. Preserve the generated record, authority-assigned species rank, unclassified parent, zero imported strain count and `SEEDED` status. Do not import unrelated same-genus candidates, treat numeric accession matches as taxon identity, count the partial marker as a genome or infer biology from the study title.

Future authority corrections belong to `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and `scripts/extract_source_inventory.py`. Generation belongs to `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; inclusion changes belong to `curation/seed_scope.tsv`. Enrichment requires source-owned evidence.

## Follow-up Checks

- At source refresh, repeat exact taxonomy, retirement/replacement and JF792180 checks while preserving authority rank assignments.
- Require complete culture identifiers and explicit sequence/genome relationships before enrichment. Distinguish BioSample identifiers, run accessions, assembly labels and length statistics from taxon IDs.
- Require isolate-specific primary results before phenotype or habitat curation in the appropriate sibling repository. Do not transfer properties from Staphylococcus haemolyticus or another named species.
- After authorized input/generator changes, run the documented dry run and single-record canary, both focused validators, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

The twenty-five rejected numeric matches are accounted for:

- Seven Staphylococcus haemolyticus rows match sample SAMEA1035041, not taxon 1035041. `data/bvbrc/bvbrc-0001.jsonl.gz:18136` identifies genome 1283.125, taxon 1283, strain 8-9 and GCF_001230625.1. `data/gold/projects.jsonl.gz:87369` supplies Gp0140427, Go0134544 and PRJEB2705. `data/catalog/gtdb_genomes-0003.jsonl.gz:14039`, `data/catalog/ncbi_refseq-0000.jsonl.gz:38262` and `data/catalog/ncbi_genbank-0000.jsonl.gz:45469` identify the explicit GCA/GCF_001230625.1 pair and strain 8-9. GTDB agrees on species while retaining its own higher classification. RefSeq/GTDB give PRJNA224116; GenBank/BV-BRC/GOLD give PRJEB2705. `data/catalog/ncbi_genbank-0064.jsonl.gz:28602` is a separate GCA_976940605.1 assembly of strain 8-9, isolate 8_9-sc-2011-10-11T10:53:46Z-1288573, under PRJEB2705. It has three contigs, no listed RefSeq partner and a large-multi-isolate-project exclusion; it is not declared equivalent to the earlier pair. `data/catalog/allthebacteria.tsv.xz:66021` supplies ERR085215 and ERZ3070474 for the same BioSample. Source/current/pre-202505 Sylph species agree and assembly-pipeline/HQ/Sylph filters pass. No equivalence between distinct assembly accessions is inferred merely from a shared sample.
- Two Mycobacterium tuberculosis rows: `data/bvbrc/bvbrc-0006.jsonl.gz:8492` identifies genome 1773.20479, taxon 1773 and strain ERR1035041. `data/catalog/allthebacteria.tsv.xz:569511` supplies ERR1035041, SAMEA3558574 and ERZ3501733; source/current/pre-202505 Sylph species agree and all three filters pass.
- Four Bacteroides salyersiae rows match sample SAMN41035041: `data/bvbrc/bvbrc-0017.jsonl.gz:24314`, `data/catalog/ncbi_genbank-0037.jsonl.gz:21053`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20163` and `data/catalog/gtdb_genomes-0007.jsonl.gz:20643`. They identify taxon 291644, strain D46st1_E5_2201SCRN_220225 and the explicit GCA/GCF_040928985.1 pair; BV-BRC genome ID is 291644.358. GenBank/BV-BRC give PRJNA1093465, while RefSeq/GTDB give PRJNA224116. GTDB agrees on species. These records are not target strain attestations.
- `data/catalog/ncbi_genbank-0063.jsonl.gz:37586` identifies uncultured Candidatus Actinomarina sp., taxon 1985113, MAG SRP329387_co2_22, GCA_964630945.1, SAMEA117374031 and PRJEB82487. Ungapped length 1035041 causes the match; total length is 1038441. The row has no paired RefSeq assembly and is excluded as metagenome-derived. No target linkage or paired accession is inferred.
- `data/catalog/ncbi_genbank-0033.jsonl.gz:35490` identifies Streptococcus pneumoniae, taxon 1313, isolate 442, GCA_036051915.1, sample SAMN11116928 and PRJNA514245. Assembly label PDT001035041.1 causes the match. It has no paired RefSeq assembly and is excluded as part of a large multi-isolate project. Its citation field concerns that unrelated record, not a YIM 94352 publication; it was not used as target evidence.

Ten GOLD rows match longer BioSample accessions. Each is a Pinaceae seedling/Suillus ectomycorrhiza metatranscriptome project with an empty organism GOLD ID, not a Staphylococcus isolate genome or attestation. Complete rows were inspected and their distinct relationships are retained below. No Eukaryota record or review was modified.

| Row in `data/gold/projects.jsonl.gz` | GOLD project | BioProject | BioSample | Project suffix | Location in title |
| --- | --- | --- | --- | --- | --- |
| 228195 | Gp0333800 | PRJNA502041 | SAMN10350410 | Scot/Prad_rep3 | North Carolina, United States |
| 228196 | Gp0333801 | PRJNA502042 | SAMN10350411 | Scot/Llari_rep1 | North Carolina, United States |
| 228218 | Gp0333823 | PRJNA502064 | SAMN10350412 | Sgre/Pmen_rep2 | Minnesota, United States |
| 228236 | Gp0333841 | PRJNA502203 | SAMN10350413 | Slak/Pmari_rep2 | Colorado, United States |
| 228255 | Gp0333860 | PRJNA502222 | SAMN10350414 | Sbov/Pmari_rep3 | Occitanie, France |
| 228269 | Gp0333874 | PRJNA502236 | SAMN10350415 | Scav/Llari_rep2 | Minnesota, United States |
| 228277 | Gp0333882 | PRJNA501937 | SAMN10350416 | Scae/Psyl_rep1 | Washington, United States |
| 228279 | Gp0333884 | PRJNA501939 | SAMN10350417 | Scae/Psyl_rep3 | Washington, United States |
| 228280 | Gp0333885 | PRJNA501940 | SAMN10350418 | Scae/Pstro_rep1 | Washington, United States |
| 228282 | Gp0333887 | PRJNA501942 | SAMN10350419 | Scae/Pstro_rep3 | Washington, United States |

Only this new timestamped report was written for the target. Records, inventories, scope, history, prior reports, generated products and Eukaryota reviews remain unchanged. External reads were public and unpaid. No commits, GitHub mutations, contacts, provider-credit jobs or lifecycle promotions occurred.
