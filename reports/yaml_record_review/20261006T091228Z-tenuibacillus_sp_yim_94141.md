# YAML Record Review: Tenuibacillus sp. YIM 94141

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/tenuibacillus_sp_yim_94141.yaml`
- Started UTC: 2026-10-06T09:10:32Z
- Finished UTC: 2026-10-06T09:12:28Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035044`, Tenuibacillus sp. YIM 94141. It asserts species rank, bacterial domain, parent `NCBITaxon:1508757`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No synonyms, nomenclature, mappings, xrefs, literature claims, strain/genome relationships or causal graph are asserted.

`data/taxa/PATHS.tsv:14335` uniquely resolves the ID/stem. `curation/seed_scope.tsv:322147` gives the NCBI-only inclusion rule dated 2026-09-13. This target is not the adjacent Tenuibacillus halotolerans record or another YIM isolate.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/tenuibacillus_sp_yim_94141.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/tenuibacillus_sp_yim_94141.yaml --out /private/tmp/tyim94141-validation.tsv`: exit 0; one file, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured comparisons verified full pinned identity, lineage, code, parent, unique path/scope, attestation and inline seed reason. No classified child was found in the backbone.
- Exact-ID scans found no target entry in seven other source inventories or the type-material, merged-ID and dropped tables.
- Initial and marker-expanded ignored-inclusive searches returned the same 29 row addresses. All complete rows were read and reconciled; no unread candidate remained. An ignored-inclusive ID/name/slug search found no prior report or separate target history artifact.
- The review skill/checklist were reread. Previously inspected guidance and validator recipes remain unchanged against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the pre-report tracked diff exited 0.
- Not run: full-corpus `just verify-corpus`, `just qc`, tests, all-record validation, full provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file checks. No undocumented focused term/reference/history validator was invented. Inline history was checked, but there is no separate target history artifact within the searched root.
- `just validate-products` is not applicable without curator-added causal-graph nodes. This is not corpus release certification.

## Identity and Grounding

Complete live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035044&retmode=xml) confirms the exact ID/name, species rank, bacterial division, parent 1508757 and code 11. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035044) agrees and includes all ten ancestor IDs, including root.

The chain is root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae, Tenuibacillus and unclassified Tenuibacillus. Each pinned ancestor ID, label and rank matches the YAML; live taxonomy confirms the non-root chain. The inspected [NCBI genus tree](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=286800&lvl=&mode=tree) places YIM 94141 under the unclassified parent, separately from the named species and other YIM isolates.

The isolate designation does not justify overriding NCBI's species rank with `STRAIN`. The no-rank parent is not a contradiction. Exact NCBI grounding does not imply validly published nomenclature or human review.

## Evidence

1. **Pinned provenance.** Complete `data/raw/ncbitaxon_taxa.tsv:221855` supports the identity, parent, code and 2026-09-13 snapshot, with empty synonym and retirement-target fields. Complete native name row `data/catalog/ncbi_names-0005.jsonl.gz:31281` gives the scientific name and empty unique name. The attestation counts one `NAME`, not a culture, genome or phenotype. The inline event at 2026-09-13T17:54:04Z, `seed_from_sources` / `SEEDED_FROM_SOURCES`, agrees with the scope rule.

2. **Marker identity.** Exact Nuccore search returned UID 333798071. Complete metadata, features and references for [JF792145.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792145.1), excluding sequence bases, identify a 681-base 16S rRNA gene partial at both ends. The organism, strain YIM 94141 and `taxon:1035044` agree. Sequence taxonomy includes Caryophanales, Bacillaceae and Tenuibacillus. C. Chen submitted the record on 7 April 2011 through the Yunnan Institute of Microbiology / Yunnan University; creation and update dates are 28 May 2011 and 26 August 2015. Inspected qualifiers supply no culture-collection, BioSample or assembly accession.

3. **Publication boundary.** GenBank marks the associated Qijiaojing Lake bacteria/enzyme study unpublished, with no DOI or PMID. The inspected genus tree corroborates taxonomic context. The marker/name web search returned no additional result. These bounded searches do not establish worldwide publication absence. The study title does not establish isolate-specific habitat, enzyme activity or culture requirements.

4. **Imported coverage.** The BacDive inventory has no exact target entry and the pinned backbone has no classified child. The zero strain count describes imported coverage, not nonexistence of the isolate. Exact NCBI assembly query `txid1035044[Organism:noexp]` returned zero, with no-items/phrase-not-found diagnostics; this does not exclude assemblies under other taxonomic classifications or outside NCBI.

5. **Rejected source matches.** Twenty-six other rows concern Staphylococcus haemolyticus, Mycobacterium tuberculosis, Bacteroides stercoris, a groundwater MAG, Campylobacter jejuni and plant/fungal metatranscriptome projects. Full source rows were inspected. Numeric accession fragments or an ungapped-length statistic caused the matches; none supplies an eligible target strain/genome relationship.

## Completeness

No consequential omission was established under the seeded-record model. Optional enrichment fields may remain empty without source-backed relationships. A partial marker carrying a bare strain qualifier does not establish a registered culture link or genome.

Local searches used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. Queries covered the unbounded taxon number, full label, slug and YIM94141 separator variants; expansion added JF792145 and its versioned spelling. Both searches returned three target provenance rows and twenty-six unrelated matches. Ignored files and compressed rows were included; separate snapshot archives and all external databases were not exhaustively searched.

Exact-ID scans covered BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. Prior-report/history searches also included ignored files. iModulonDB was not applicable to this identity-only record; unrelated metatranscriptome projects are not target expression evidence. No sequence alignment, experimental reanalysis, genome comparison or exhaustive literature census was performed. Search snippets did not support the verdict.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected evidence supports the represented identity, lineage, grounding, source coverage and audit status. This does not certify formal nomenclature, biological traits, universal assembly absence or full-corpus reproducibility.

## Recommended Edits

None required. Preserve the generated record, NCBI species rank, unclassified parent, zero imported strain count and `SEEDED` status. Do not import neighboring species' culture identifiers or genomes, count the partial marker as a genome, or infer traits from a study title.

Future authority corrections belong to `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and `scripts/extract_source_inventory.py`; generation belongs to `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`. Scope changes belong to `curation/seed_scope.tsv`. New strain/genome links require source-owned evidence and the existing identifier rules.

## Follow-up Checks

- At source refresh, repeat exact taxonomy, retirement/replacement and JF792145 checks.
- Require complete registered culture identifiers and explicit source-owned relationships before strain/genome enrichment. Keep sample IDs, assembly accessions and length statistics distinct from taxon IDs.
- Require isolate-specific primary results before phenotype or habitat curation; do not transfer evidence from Tenuibacillus halotolerans or another YIM isolate.
- After authorized input/generator changes, run the documented dry run and single-record canary, both focused validators, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

The twenty-six rejected matches are accounted for:

- Seven Staphylococcus haemolyticus rows match sample SAMEA1035044. BV-BRC `bvbrc-0001.jsonl.gz:18379` identifies taxon 1283, genome 1283.168, strain 51-13 and GCA_001235665.1. GOLD project row 87401 supplies Gp0140459, Go0134576 and PRJEB2705. GenBank `ncbi_genbank-0000.jsonl.gz:45721`, RefSeq `ncbi_refseq-0000.jsonl.gz:38504` and GTDB `gtdb_genomes-0006.jsonl.gz:28880` preserve the explicit GCA/GCF_001235665.1 pair. GenBank/BV-BRC/GOLD give PRJEB2705; RefSeq/GTDB give PRJNA224116. GTDB agrees on species while retaining its own higher classification. GenBank `ncbi_genbank-0064.jsonl.gz:28605` supplies a separate complete assembly GCA_976940635.1, isolate 51_13-sc-2011-10-11T10:53:24Z-1288541, one contig and no listed RefSeq partner. It is excluded as part of a large multi-isolate project. Its unrelated PMID is not target publication evidence. AllTheBacteria row 66024 supplies ERR085183 and ERZ3070476, with source/current/pre-202505 species agreement and passing pipeline/HQ/Sylph filters. Sample sharing does not establish equivalence of the distinct assemblies.
- Two Mycobacterium tuberculosis rows concern strain ERR1035044: BV-BRC `bvbrc-0006.jsonl.gz:8500` gives taxon 1773 and genome 1773.20486; AllTheBacteria row 569514 supplies SAMEA3558577 and ERZ3501742. Species fields agree and all three filters pass.
- Four Bacteroides stercoris rows concern taxon 46506, strain RTP21198st1_D4_RTP21198_201120, sample SAMN41035044 and the explicit GCA/GCF_040928945.1 pair: BV-BRC `bvbrc-0020.jsonl.gz:26091` (genome 46506.2636), GenBank `ncbi_genbank-0037.jsonl.gz:21051`, RefSeq `ncbi_refseq-0006.jsonl.gz:20161` and GTDB `gtdb_genomes-0002.jsonl.gz:21701`. GenBank/BV-BRC give PRJNA1093465; RefSeq/GTDB give PRJNA224116. GTDB agrees on species.
- Two groundwater MAG rows match ungapped length 1035044: GTDB `gtdb_genomes-0017.jsonl.gz:11004` and GenBank `ncbi_genbank-0014.jsonl.gz:35857`. They identify GCA_016188385.1, taxon 2053634, isolate NC_groundwater_423_Ag_B-0.1um_48_14, SAMN15434919 and PRJNA640378. NCBI names Candidatus Uhrbacteria bacterium; GTDB assigns its own JACQSB01 species under Patescibacteriota. Total length is 1035094; there is no listed RefSeq partner, and the source excludes the assembly as metagenome-derived with undefined genus.
- GenBank `ncbi_genbank-0009.jsonl.gz:6358` matches accession GCA_010350445.1, not a taxon. It identifies Campylobacter jejuni, taxon 197, strain PNUSAC013609, SAMN13347993 and PRJNA239251. The source supplies no RefSeq partner and excludes it as part of a large multi-isolate project.

Ten GOLD rows have empty organism GOLD IDs and describe Pinaceae seedling/Suillus metatranscriptomes. Each matched a longer BioSample accession. They are not target isolate genomes or attestations.

| Row in `data/gold/projects.jsonl.gz` | GOLD project | BioProject | BioSample | Project suffix | Location in title |
| --- | --- | --- | --- | --- | --- |
| 228160 | Gp0333765 | PRJNA502006 | SAMN10350440 | Slut/Llari_rep1 | Pennsylvania, United States |
| 228161 | Gp0333766 | PRJNA502007 | SAMN10350448 | Slut/Llari_rep2 | Pennsylvania, United States |
| 228163 | Gp0333768 | PRJNA502009 | SAMN10350449 | Slut/Pmen_rep1 | Pennsylvania, United States |
| 228168 | Gp0333773 | PRJNA502014 | SAMN10350441 | Slut/Pmari_rep3 | Pennsylvania, United States |
| 228173 | Gp0333778 | PRJNA502019 | SAMN10350442 | Same/Pstro_rep2 | Pennsylvania, United States |
| 228187 | Gp0333792 | PRJNA502033 | SAMN10350443 | Scot/Psyl_rep1 | North Carolina, United States |
| 228215 | Gp0333820 | PRJNA502061 | SAMN10350444 | Sgre/Llari_rep2 | Minnesota, United States |
| 228233 | Gp0333838 | PRJNA502200 | SAMN10350445 | Slak/Pmen_rep2 | Colorado, United States |
| 228252 | Gp0333857 | PRJNA502219 | SAMN10350446 | Sbov/Pmen_rep3 | Occitanie, France |
| 228264 | Gp0333869 | PRJNA502231 | SAMN10350447 | Scav/Pstro_rep3 | Minnesota, United States |

Only this new timestamped report was written for the target. Records, inventories, scope, history, prior reports, generated products and Eukaryota reviews remain unchanged. External reads were public and unpaid. No commits, GitHub mutations, contacts, provider-credit jobs or lifecycle promotions occurred.
