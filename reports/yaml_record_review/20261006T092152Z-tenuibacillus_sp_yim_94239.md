# YAML Record Review: Tenuibacillus sp. YIM 94239

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/tenuibacillus_sp_yim_94239.yaml`
- Started UTC: 2026-10-06T09:20:11Z
- Finished UTC: 2026-10-06T09:21:52Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035046`, Tenuibacillus sp. YIM 94239. It carries species rank, bacterial domain, parent `NCBITaxon:1508757`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No synonyms, nomenclature, mappings, xrefs, literature assertions, strain/genome relationships, discussion or causal graph are asserted.

`data/taxa/PATHS.tsv:14337` uniquely resolves the ID/stem. `curation/seed_scope.tsv:322149` supplies the NCBI-only inclusion rule dated 2026-09-13. This record is distinct from other YIM isolates and the named Tenuibacillus species.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/tenuibacillus_sp_yim_94239.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/tenuibacillus_sp_yim_94239.yaml --out /private/tmp/tyim94239-validation.tsv`: exit 0; one file, zero ERROR rows. Read the header-only TSV.
- Structured comparisons verified the complete pinned identity, parent, lineage, code, unique path/scope, attestation and inline seed reason. No classified child was found in the backbone.
- Exact-ID scans found no target row in seven other source inventories or the type-material, merged-ID and dropped tables.
- Initial and marker-expanded ignored-inclusive compressed searches returned the same 26 addresses. Complete rows were read and reconciled, with no unread candidate. Ignored-inclusive ID/name/slug searches found no prior target report or separate target history artifact.
- The review skill/checklist were reread. Previously inspected guidance, schema and validator recipes remain unchanged against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the pre-report tracked diff exited 0.
- Not run: full-corpus `just verify-corpus`, `just qc`, tests, all-record validation, full provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file checks. No undocumented focused term/reference/history validator was invented. Inline history was checked; no separate target history artifact was available.
- `just validate-products` is not applicable without curator-added causal-graph nodes. This is not corpus release certification.

## Identity and Grounding

Complete live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035046&retmode=xml) confirms the exact identifier/name, species rank, bacterial division, parent 1508757 and code 11. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035046) agrees and supplies all ten ancestor IDs, including root.

The root-first chain is root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae, Tenuibacillus and unclassified Tenuibacillus. Every pinned ancestor ID, label and rank matches the YAML; live taxonomy confirms the non-root chain. The inspected [NCBI genus tree](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=286800&lvl=&mode=tree) lists YIM 94239 under the unclassified parent, separately from YIM 94141, YIM 94174 and named species.

The isolate designation is not a reason to replace the authority-assigned species rank with `STRAIN`. Exact NCBI grounding does not imply formal nomenclatural validation, biological characterization or human review.

## Evidence

1. **Pinned provenance.** Complete `data/raw/ncbitaxon_taxa.tsv:221857` supports identity, parent, code and snapshot 2026-09-13, with empty synonym and retirement-target fields. Complete native name row `data/catalog/ncbi_names-0005.jsonl.gz:31283` supplies the scientific name and empty unique name. The attestation counts one `NAME`, not a strain, genome or phenotype. The inline `seed_from_sources` / `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z agrees with the scope reason.

2. **Marker identity.** Exact Nuccore search returned UID 333798090. Complete metadata, features and references for [JF792164.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792164.1), excluding bases, identify a 691-base 16S rRNA gene partial at both ends. Organism, strain YIM 94239 and `taxon:1035046` agree. Sequence taxonomy includes Caryophanales, Bacillaceae and Tenuibacillus. C. Chen submitted the record on 7 April 2011 through the Yunnan Institute of Microbiology / Yunnan University. Creation and update dates are 28 May 2011 and 26 August 2015. The inspected qualifiers contain no culture-collection, BioSample or assembly accession.

3. **Publication boundary.** GenBank marks the associated Qijiaojing Lake bacteria/enzyme study unpublished, without a DOI or PMID. Name search supplied the inspected NCBI tree; the JF792164/Tenuibacillus query returned no results. These bounded searches do not establish worldwide publication absence. The study title does not demonstrate isolate-specific enzyme activity, habitat or culture requirements.

4. **Imported strain/genome coverage.** The BacDive inventory has no exact target row, and the pinned backbone has no classified child. Zero strains describes imported coverage, not the isolate's nonexistence. Exact assembly search `txid1035046[Organism:noexp]` returned zero, with no-items/phrase-not-found diagnostics; it does not exclude assemblies under different classifications or outside NCBI. The marker alone does not establish a registered culture or genome relationship.

5. **Rejected candidates.** Twenty-three source rows concern unrelated organisms or plant/fungal metatranscriptomes. All were read in full. Numeric fragments in BioSamples, a run, a GenBank assembly accession and a SeqKit sum explain the matches. None supports an additional target attestation or strain/genome link.

## Completeness

No consequential omission was established under the seeded-record model. Optional enrichment fields may remain empty without source-backed relationships. No deposit/classification discrepancy was found for YIM 94239 within the inspected sources; a discrepancy involving a neighboring isolate cannot be transferred to this record.

Searches used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. Queries covered the unbounded taxon number, label, slug and YIM94239 separator variants; expansion added JF792164 and its versioned spelling. Both returned three target provenance rows and twenty-three unrelated matches. Ignored files and compressed rows were included; separate snapshot archives and all external databases were not exhaustively searched.

Exact-ID inventory scans covered BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits. Prior-report/history searches included ignored files. iModulonDB was not applicable to this identity-only record. No sequence alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets were not used as evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected evidence supports the represented identity, lineage, grounding, source coverage and audit status. This does not certify formal nomenclature, biological traits, universal assembly absence or full-corpus reproducibility.

## Recommended Edits

None required. Preserve the generated record, authority-assigned species rank, unclassified parent, zero imported strain count and `SEEDED` status. Do not count the partial marker as a genome or attach other isolates' deposit relationships.

Future authority corrections belong to `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and `scripts/extract_source_inventory.py`. Generation belongs to `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; scope changes belong to `curation/seed_scope.tsv`. New strain/genome links require source-owned evidence under existing identifier rules.

## Follow-up Checks

- At source refresh, repeat exact taxonomy, retirement/replacement and JF792164 checks.
- Require complete culture identifiers and explicit source-owned sequence/genome relationships before enrichment.
- Require isolate-specific primary evidence before phenotype or habitat curation in the appropriate sibling repository.
- After authorized maintained-input/generator changes, run the documented dry run and single-record canary, both focused validators, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

All twenty-three rejected numeric matches are accounted for:

- Six Staphylococcus haemolyticus rows match sample SAMEA1035046. BV-BRC `bvbrc-0001.jsonl.gz:17978` identifies taxon 1283, genome 1283.103 and strain 25-12. GOLD project row 87378 gives Gp0140436, Go0134553 and PRJEB2705. GTDB `gtdb_genomes-0012.jsonl.gz:49928`, RefSeq `ncbi_refseq-0000.jsonl.gz:38114` and GenBank `ncbi_genbank-0000.jsonl.gz:45317` identify the explicit GCA/GCF_001227585.1 pair. GenBank/BV-BRC/GOLD give PRJEB2705; RefSeq/GTDB give PRJNA224116. GTDB agrees on species while retaining its own higher taxonomy. AllTheBacteria row 66026 supplies ERR085165 and ERZ3070486 with source/current/pre-202505 species agreement and passing pipeline/HQ/Sylph filters.
- Four Bacteroides thetaiotaomicron rows concern taxon 818, strain RTP21198st1_B1_RTP21198_201120, SAMN41035046 and the explicit GCA/GCF_040928905.1 pair: BV-BRC `bvbrc-0027.jsonl.gz:21486` (genome 818.3300), GenBank `ncbi_genbank-0037.jsonl.gz:21049`, RefSeq `ncbi_refseq-0006.jsonl.gz:20159` and GTDB `gtdb_genomes-0016.jsonl.gz:7175`. GenBank/BV-BRC give PRJNA1093465; RefSeq/GTDB give PRJNA224116. Species assignments agree.
- GenBank `ncbi_genbank-0009.jsonl.gz:6359` matches accession GCA_010350465.1. It identifies Campylobacter jejuni, taxon 197, strain PNUSAC013576, SAMN13342393 and PRJNA239251. The row supplies no RefSeq partner and is excluded as part of a large multi-isolate project.
- AllTheBacteria row 569516 matches run ERR1035046. It identifies Mycobacterium tuberculosis, SAMEA3558579 and ERZ3501747, with species agreement and passing filters.
- AllTheBacteria row 614713 matches digits inside its SeqKit sum, `seqkit.v0.1_DLS_k0_527340ce240898801035046ab0fea283`. It identifies Salmonella enterica subsp. enterica serovar Typhimurium, SAMEA4349637, ERR1540596 and ERZ3537543. Current and pre-202505 Sylph species are Salmonella enterica; all three filters pass. The SeqKit sum is not a taxon identifier or an MD5-based identity claim.

Ten GOLD project rows have empty organism GOLD IDs and describe Pinaceae seedling/Suillus metatranscriptomes. Each matches a longer BioSample ID; none is a target isolate genome or attestation.

| Row in `data/gold/projects.jsonl.gz` | GOLD project | BioProject | BioSample | Project suffix | Location in title |
| --- | --- | --- | --- | --- | --- |
| 228239 | Gp0333844 | PRJNA502206 | SAMN10350460 | Sbov/Psyl_rep2 | Occitanie, France |
| 228245 | Gp0333850 | PRJNA502212 | SAMN10350461 | Sbov/Prad_rep2 | Occitanie, France |
| 228256 | Gp0333861 | PRJNA502223 | SAMN10350462 | Sfus/Pmen_rep1 | California, United States |
| 228261 | Gp0333866 | PRJNA502228 | SAMN10350463 | Scav/Psyl_rep3 | Minnesota, United States |
| 228267 | Gp0333872 | PRJNA502234 | SAMN10350464 | Scav/Prad_rep3 | Minnesota, United States |
| 228291 | Gp0333896 | PRJNA501951 | SAMN10350465 | Scae/Pmen_rep3 | Washington, United States |
| 228305 | Gp0333910 | PRJNA501965 | SAMN10350466 | Sgla/Llari_rep2 | Minnesota, United States |
| 228309 | Gp0333914 | PRJNA501969 | SAMN10350467 | Sgla/Pmen_rep3 | Minnesota, United States |
| 228313 | Gp0333918 | PRJNA501973 | SAMN10350468 | Ssub/Psyl_rep1 | New York, United States |
| 228315 | Gp0333920 | PRJNA501975 | SAMN10350469 | Ssub/Psyl_rep3 | New York, United States |

Only this new timestamped report was written for the target. Records, inventories, scope, history, prior reports, generated products and Eukaryota reviews remain unchanged. External reads were public and unpaid. No commits, contacts, GitHub mutations, provider-credit jobs or lifecycle promotions occurred.
