# YAML Record Review: Thalassobacillus sp. YIM 93825

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thalassobacillus_sp_yim_93825.yaml`
- Started UTC: 2026-10-06T09:23:16Z
- Finished UTC: 2026-10-06T09:24:47Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035047`, Thalassobacillus sp. YIM 93825. It asserts species rank, bacterial domain, parent `NCBITaxon:2621135`, ten root-first ancestors, code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No synonyms, nomenclature, mappings, xrefs, literature claims, strain/genome relationships, discussion or causal graph are asserted.

`data/taxa/PATHS.tsv:14338` uniquely resolves the ID/stem. `curation/seed_scope.tsv:322150` supplies the NCBI-only inclusion rule dated 2026-09-13. This is an individual NCBI concept, not the genus or another YIM isolate.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/thalassobacillus_sp_yim_93825.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/thalassobacillus_sp_yim_93825.yaml --out /private/tmp/thbyim93825-validation.tsv`: exit 0; one file, zero ERROR rows. Read the header-only TSV.
- Structured comparisons verified complete pinned identity, parent, lineage, code, unique path/scope, attestation and inline seed reason. No classified child was found.
- Exact-ID scans found no target entry in seven other source inventories or the type-material, merged-ID and dropped tables.
- Initial and marker-expanded ignored-inclusive searches returned the same 25 source addresses. All complete rows were inspected and reconciled with no unread candidate. Ignored-inclusive ID/name/slug searches found no prior target report or separate target history artifact.
- The review skill/checklist were reread this turn. Previously inspected guidance, schema and validator recipes remain unchanged against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the pre-report tracked diff exited 0.
- NCBI browser pages for the target and parent were not retrievable through the web tool. Complete taxonomy XML and Datasets API responses succeeded and supplied the authority evidence.
- Not run: full-corpus `just verify-corpus`, `just qc`, tests, all-record validation, full provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file checks. No undocumented focused term/reference/history validator was invented. Inline history was checked; no separate target history artifact was available.
- `just validate-products` is not applicable without curator-added causal-graph nodes. This is not corpus release certification.

## Identity and Grounding

Complete live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035047&retmode=xml) confirms the exact ID/name, species rank, bacterial division, parent 2621135 and genetic code 11. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035047) agrees and supplies all ten ancestor IDs, including root.

The chain is root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae, Thalassobacillus and unclassified Thalassobacillus. Every pinned ancestor ID, label and rank matches the YAML; live taxonomy confirms the non-root chain. Genus `NCBITaxon:331971`, family `NCBITaxon:186817` and order `NCBITaxon:1385` agree.

The isolate designation does not justify changing NCBI's species rank to `STRAIN`; the no-rank parent does not contradict it. Exact grounding denotes the NCBI concept, not formal nomenclatural validation, biological characterization or human review.

## Evidence

1. **Pinned provenance.** Complete `data/raw/ncbitaxon_taxa.tsv:221858` supports identity, parent, code and snapshot 2026-09-13, with empty synonym and retirement-target fields. Complete native name row `data/catalog/ncbi_names-0005.jsonl.gz:31284` gives the scientific name and empty unique name. The attestation counts one `NAME`, not a culture, genome or phenotype. The inline `seed_from_sources` / `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z matches the scope reason.

2. **Marker identity.** Exact Nuccore search returned UID 333798027. Complete metadata, features and references for [JF792101.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792101.1), excluding bases, identify a 691-base 16S rRNA gene partial at both ends. Organism, strain YIM 93825 and `taxon:1035047` agree. Sequence taxonomy includes Caryophanales, Bacillaceae and Thalassobacillus. C. Chen submitted the record on 7 April 2011 through the Yunnan Institute of Microbiology / Yunnan University. Creation and update dates are 28 May 2011 and 26 August 2015. The inspected qualifiers contain no culture-collection, BioSample or assembly accession.

3. **Publication boundary.** GenBank marks the associated Qijiaojing Lake bacteria/enzyme study unpublished, without a DOI or PMID. Name search returned taxonomy-summary leads, not an inspected primary study; these snippets did not support the verdict. The JF792101/Thalassobacillus query returned no result. These bounded checks do not establish worldwide publication absence. The study title does not demonstrate isolate-specific enzyme activity, habitat or culture requirements.

4. **Imported coverage.** The BacDive inventory has no exact target row, and the pinned backbone has no classified child. Zero strains describes imported coverage, not the isolate's nonexistence. Exact assembly query `txid1035047[Organism:noexp]` returned zero with no-items/phrase-not-found diagnostics; this does not exclude assemblies under other classifications or outside NCBI. The partial marker alone supplies no registered-deposit or genome relationship.

5. **Rejected source matches.** Twenty-two rows concern Staphylococcus haemolyticus, Mycobacterium tuberculosis, Bacteroides thetaiotaomicron and plant/fungal metatranscriptomes. Full rows were inspected. Longer BioSample IDs and a run accession caused the numeric matches; none supports a target attestation or strain/genome link.

## Completeness

No consequential omission was established under the seeded-record model. Optional enrichment fields may remain empty without source-backed relationships. No traits, medium requirements or habitat were inferred from the study title or neighboring species.

Searches used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. Queries covered the unbounded taxon number, label, slug and YIM93825 separator variants; expansion added JF792101 and its versioned spelling. Both returned three target provenance rows and twenty-two unrelated matches. Ignored files and compressed rows were included; separate snapshot archives and all external databases were not exhaustively searched.

Exact-ID scans covered BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits. Prior-report/history searches included ignored files. iModulonDB was not applicable to this identity-only record; unrelated metatranscriptomes are not target expression evidence. No sequence alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected evidence supports the represented identity, lineage, grounding, source coverage and audit status. This does not certify formal nomenclature, biological traits, universal assembly absence or full-corpus reproducibility.

## Recommended Edits

None required. Preserve the generated record, authority-assigned species rank, unclassified parent, zero imported strain count and `SEEDED` status. Do not count the partial marker as a genome, use numeric substrings as identity joins or transfer other isolates' properties.

Future authority corrections belong to `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and `scripts/extract_source_inventory.py`. Generation belongs to `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; scope changes belong to `curation/seed_scope.tsv`. Enrichment requires source-owned evidence and existing complete-identifier rules.

## Follow-up Checks

- At source refresh, repeat exact taxonomy, retirement/replacement and JF792101 checks.
- Require complete registered culture identifiers and explicit source-owned sequence/genome relationships before enrichment.
- Require isolate-specific primary results before phenotype or habitat curation in the appropriate sibling repository.
- After authorized maintained-input/generator changes, run the documented dry run and single-record canary, both focused validators, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

The twenty-two rejected numeric matches are accounted for:

- Six Staphylococcus haemolyticus rows match sample SAMEA1035047. BV-BRC `bvbrc-0001.jsonl.gz:18535` identifies taxon 1283, genome 1283.197 and strain 51-29. GOLD project row 87403 supplies Gp0140461, Go0134578 and PRJEB2705. GenBank `ncbi_genbank-0000.jsonl.gz:45880`, RefSeq `ncbi_refseq-0000.jsonl.gz:38658` and GTDB `gtdb_genomes-0010.jsonl.gz:23885` preserve the explicit GCA/GCF_001238865.1 pair. GenBank/BV-BRC/GOLD give PRJEB2705; RefSeq/GTDB give PRJNA224116. GTDB agrees on species while retaining its own higher classification. AllTheBacteria row 66027 supplies ERR085193 and ERZ3070487 with source/current/pre-202505 species agreement and passing pipeline/HQ/Sylph filters.
- Two Mycobacterium tuberculosis rows concern strain ERR1035047: BV-BRC `bvbrc-0006.jsonl.gz:8494` gives taxon 1773 and genome 1773.20480; AllTheBacteria row 569517 supplies SAMEA3558580 and ERZ3501743. Species fields agree and all three filters pass.
- Four Bacteroides thetaiotaomicron rows concern taxon 818, strain RTP21198st1_C1_RTP21198_201120, SAMN41035047 and the explicit GCA/GCF_040928885.1 pair: BV-BRC `bvbrc-0027.jsonl.gz:21485` (genome 818.3299), GenBank `ncbi_genbank-0037.jsonl.gz:21048`, RefSeq `ncbi_refseq-0006.jsonl.gz:20158` and GTDB `gtdb_genomes-0013.jsonl.gz:7996`. GenBank/BV-BRC give PRJNA1093465; RefSeq/GTDB give PRJNA224116. Species assignments agree.

Ten GOLD project rows have empty organism GOLD IDs and describe Pinaceae seedling/Suillus metatranscriptomes. Each matches a longer BioSample ID and is not a target isolate genome or attestation.

| Row in `data/gold/projects.jsonl.gz` | GOLD project | BioProject | BioSample | Project suffix | Location in title |
| --- | --- | --- | --- | --- | --- |
| 228190 | Gp0333795 | PRJNA502036 | SAMN10350472 | Scot/Pstro_rep1 | North Carolina, United States |
| 228191 | Gp0333796 | PRJNA502037 | SAMN10350479 | Scot/Pstro_rep2 | North Carolina, United States |
| 228193 | Gp0333798 | PRJNA502039 | SAMN10350478 | Scot/Prad_rep1 | North Carolina, United States |
| 228197 | Gp0333802 | PRJNA502043 | SAMN10350477 | Scot/Llari_rep2 | North Carolina, United States |
| 228198 | Gp0333803 | PRJNA502044 | SAMN10350476 | Scot/Llari_rep3 | North Carolina, United States |
| 228201 | Gp0333806 | PRJNA502047 | SAMN10350475 | Scot/Pmen_rep3 | North Carolina, United States |
| 228203 | Gp0333808 | PRJNA502049 | SAMN10350474 | Scot/Pmari_rep2 | North Carolina, United States |
| 228324 | Gp0333929 | PRJNA501984 | SAMN10350473 | Ssub/Llari_rep3 | New York, United States |
| 228364 | Gp0333969 | PRJNA501917 | SAMN10350470 | Stom/Pmari_rep1 | Oregon, United States |
| 228375 | Gp0333980 | PRJNA501928 | SAMN10350471 | Sfus/Prad_ES_rep3 | California, United States |

Only this new timestamped report was written for the target. Records, inventories, scope, history, prior reports, generated products and Eukaryota reviews remain unchanged. External reads were public and unpaid. No commits, contacts, GitHub mutations, provider-credit jobs or lifecycle promotions occurred.
