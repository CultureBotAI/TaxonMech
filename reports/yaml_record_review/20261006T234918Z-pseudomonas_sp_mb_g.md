# YAML Record Review: Pseudomonas sp. MB-g

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_mb_g.yaml`
- Started UTC: 2026-10-06T23:44:22Z
- Finished UTC: 2026-10-06T23:49:18Z
- Verdict: pass

## Target

The entire generated TaxonRecord was read. NCBITaxon:1035350 denotes Pseudomonas sp. MB-g, rank SPECIES, domain BACTERIA, parent NCBITaxon:196821. It has ten root-first ancestors, code 11, EXACT grounding, SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event. No synonyms, nomenclature, mappings, listed strains, genomes, experimental claims, citations or causal graph are populated. The YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_mb_g.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_mb_g.yaml --out /private/tmp/pmbg-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and is header-only.
- Exact backbone, every ancestor, children, seven other raw inventories, PATHS, scope and attestation comparisons passed. Type-material, merged-ID and dropped-ID inventories contain no exact target row.
- All 58 focused-search candidate records were inspected losslessly, comprising 41 JSON objects and 17 TSV rows. Secondary accession/deposit/literature searches and separately parsed SOURCE.json metadata/history filenames were checked.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0, all 28 rows read before open web research. No organism/dataset matches MB-g; other Pseudomonas datasets do not establish strain coverage.
- Live NCBI taxonomy XML/Datasets, exact Assembly/nuccore searches, both full marker metadata records excluding bases/translations and Datasets genome lookup succeeded.
- PubMed metadata, abstract and DataBankList were inspected. The related journal's publisher abstract was inspected earlier in this same review session; the full journal article was not available. The exact JCM query was read from the official catalog form and executed successfully.
- Both complete pages of a relevant primary conference abstract, including its table and figure caption, were read and visually inspected from the university-hosted PDF.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, journal full text, raw experiments or current physical deposit availability. Bounded comparisons do not reproduce the corpus.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222037`, name object at `data/catalog/ncbi_names-0005.jsonl.gz:31512`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035350&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035350) agree on identifier, label, rank, parent, domain and code.

Every ancestor ID, label and normalized rank agrees: root (1); cellular organisms (131567); Bacteria (2); Pseudomonadati (3379134); Pseudomonadota (1224); Gammaproteobacteria (1236); Pseudomonadales (72274); Pseudomonadaceae (135621); Pseudomonas (286); unclassified Pseudomonas (196821). Datasets independently includes root ID 1. The terminal unclassified parent is NO_RANK.

Pinned synonyms and live alternate names are empty, with no pinned direct children. Preserve the lowercase g in MB-g. NCBI species rank is not formal nomenclatural standing or type status. A publication's marker-similarity comparison with P. ficuserectae does not justify replacing the current taxonomic identity.

## Evidence

The single NCBITAXON NAME attestation matches snapshot 2026-09-13. `data/taxa/PATHS.tsv:14528` and `curation/seed_scope.tsv:322309` agree with the stem and seed-event reason. The raw, ATB and StrainInfo manifest timestamps inspected in this session are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z; their maximum matches the event under the inspected `src/taxonmech/seed.py` rule. This review does not promote SEEDED.

Exact nuccore search returned two partial 16S rRNA sequences, not genomes:

| Accession | Length | Inspected source identity |
|---|---|---|
| [JF790967.1](https://www.ncbi.nlm.nih.gov/nuccore/JF790967.1) | 1,432 bp | MB-g, taxon 1035350; cryoconite-hole soil, Vestre Broggerbreen glacier, Svalbard: Ny-Alesund; direct submission 8-Apr-2011 by Singh and Dhakephalkar authors at BITS Goa. |
| [AB897867.1](https://www.ncbi.nlm.nih.gov/nuccore/AB897867.1) | 1,461 bp | MB-g, taxon 1035350, explicit culture_collection JCM:19509; glacier cryoconite sediment, Norway:Svalbard, collected 22-Aug-2009 by S. M. Singh; direct submission 18-Dec-2013 from JCM/RIKEN by Iino and colleagues. |

Both research references remain marked Unpublished in their sequence records. Neither record supplies a BioSample, assembly or CDS. Their different lengths/versions are preserved; shared taxonomy is not proof of sequence equivalence. India and Japan in submission addresses are not isolation localities.

The [official JCM form](https://jcm.brc.riken.jp/en/catalogue_e) identifies the public accession lookup endpoint. The exact [JCM 19509 query](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=19509) completed and returned Nothing found. An earlier request to the wrong host returned 404; the successful current-endpoint result is the relevant observation. This does not erase the explicit deposit association in AB897867.1 or establish withdrawal, misidentification or present unavailability. The [JCM FAQ](https://jcm.brc.riken.jp/en/ordering_e_faq) acknowledges that published accession numbers may lack public catalog entries; no contact was made.

[PubMed 24283367](https://pubmed.ncbi.nlm.nih.gov/24283367/), DOI [10.1111/1574-6968.12345](https://academic.oup.com/femsle/article-abstract/351/1/14/501000), explicitly lists JF790967 in its DataBankList. Its abstract discusses Cry-g and P. ficuserectae, but the exact MB-g/Cry-g/MB-9 alias relationship was not verified from the journal table. This is not evidence for silently renaming MB-g.

The primary 2015 conference contribution by Purnima Singh, Utpal Roy, Yuichi Hanada and Sakae Tsuda, Poster C-24, was inspected on printed pages 153-154, PDF pages 156-157, of the [Polar and Alpine Microbiology abstract book](https://pubblicazioni.unicam.it/retrieve/e0ff0073-a2af-9bac-e053-1705fe0af019/Polar%20Alpine%20Microbiology%202015%2C%20book%20of%20Abstracts.pdf). Table 1 explicitly places JCM 19509 beside a P. ficuserectae/AB021378 comparison of 96.9% and an AFP N-terminal sequence. This is bounded deposit-level experimental context, not a genome, validated species reassignment, or evidence for a genus-wide phenotype. The abstract's Cry-C mass-spectrometry details concern another organism and are not transferred.

Exact Assembly search returned zero with a phrase-not-found warning, and [Datasets genome](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035350/dataset_report) returned an empty object. These are dated bounded results, not proof of genome absence everywhere.

## Completeness

An initial case-insensitive, separator-tolerant MB-g/MBG query produced 366 discovery lines. It conflated distinct spellings and was replaced by the literal MB-g token, taxon-ID digits and exact slug. The other broad leads were not all read or used to support this verdict; no exhaustive claim about hypothetical MBG aliases is made.

The focused search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. All 58 focused candidate values were inspected.

Three candidates are the exact target name/backbone/scope rows. Six concern distinct gamma proteobacterium MB-G-3 (294660) and Micromonospora sp. MB-G-3 (537736), each with its own name/backbone/scope rows. These longer strain names are not MB-g.

Two rows concern M. tuberculosis ERR1035350, taxon 1773: BV-BRC 1773.18359 and ATB SAMEA3558883/ERR1035350/ERZ9334552. Another is Campylobacter jejuni FSIS12027779, taxon 197, GCA_010353505.1/SAMN13828706/PRJNA287430, at `data/catalog/ncbi_genbank-0009.jsonl.gz:6508`. Run and assembly digits are not taxon identifiers.

The other 46 rows concern ten E. coli samples, taxon 562 and PRJNA218110: ten BV-BRC, ten current GenBank, eleven historical GenBank, ten ATB and five GOLD project rows.

| BioSample | E. coli strain | Current GenBank | ATB analysis |
|---|---|---|---|
| SAMN10353500 | PNUSAE019643 | GCA_003770085.2 | ERZ9092883 |
| SAMN10353501 | PNUSAE019726 | GCA_003755005.2 | ERZ9092884 |
| SAMN10353502 | PNUSAE019725 | GCA_003760985.2 | ERZ9092885 |
| SAMN10353503 | PNUSAE018214 | GCA_003760945.2 | ERZ9092888 |
| SAMN10353504 | PNUSAE018213 | GCA_003756625.2 | ERZ9092890 |
| SAMN10353505 | PNUSAE018212 | GCA_003768465.3 | ERZ9092891 |
| SAMN10353506 | PNUSAE019703 | GCA_003760905.2 | ERZ9092892 |
| SAMN10353507 | PNUSAE019648 | GCA_003770445.2 | ERZ9092894 |
| SAMN10353508 | PNUSAE019647 | GCA_003761025.2 | ERZ9092895 |
| SAMN10353509 | PNUSAE019706 | GCA_003756445.2 | ERZ9092896 |

Ten historical .1 assemblies were replaced, nine on 2020-03-07 and GCA_003760945.1 on 2020-03-13. GCA_003768465.2 was replaced again on 2025-02-22. BV-BRC retains .1 identifiers. ATB retains full run IDs, SeqKit sums and PASS/available-FASTA fields; these do not supply an MB-g identity chain.

GOLD Gp0386911/Go0502634 corresponds to SAMN10353501; Gp0386912/Go0502635 to SAMN10353502; Gp0386916/Go0502639 to SAMN10353506; Gp0386997/Go0502720 to SAMN10353503; Gp0386998/Go0502721 to SAMN10353504. Organism/project IDs remain distinct from genome identifiers.

Secondary ignored-inclusive searches for AB897867, JF790967, JCM 19509 with separators, PMID 24283367 and its full DOI found no local content matches in the same roots. Five SOURCE.json files and history filenames were separately checked. These bounded misses do not contradict the inspected external deposit and sequence evidence.

Zero inventoried BacDive strains matches the exact inventory and empty child set; it is not a count of all biological isolates or all collection holdings. The JCM association is a genuine optional enrichment opportunity outside the pinned mapped inventory, not a reason to change this count manually. No missing required representation or supported genome association was established.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in existing generated assertions. The historical JCM association and present catalog miss are preserved as an unresolved enrichment/status question, not silently reconciled.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status. Do not convert either 16S accession into a genome or infer a named-species assignment from a similarity percentage.

For authorized enrichment, add supported collection evidence through a maintained input/adapter, including `scripts/extract_source_inventory.py` where appropriate, with source-specific identity and accession typing; then use the documented seeder. Do not assign a BacDive or StrainInfo identifier that has not been established. Experimental protein/trait, habitat and medium assertions belong in their sibling repositories.

## Follow-up Checks

Resolve JCM 19509's current catalog status before asserting availability, withdrawal or classification changes. Preserve the sequence submission as historical deposit evidence. Any later genome claim needs an explicit sample/deposit/assembly chain; the current markers do not provide one.

Obtain lawful journal full text before treating MB-g, Cry-g and MB-9 as aliases or transferring assay results. After authorized upstream changes, rerun both exact-target validators and inspect the emitted TSV, plus the documented canary and full `just verify-corpus`/QC gates for source/generator changes.

## Additional Notes

Guidance and generation boundaries were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target remains byte-identical. Only this timestamped report is written to the repository; no YAML, source inventory, prior report, generated product, history event or lifecycle status is changed. Eukaryota remains untouched.

The conference-host download failed certificate verification; no certificate check was disabled. The university-hosted public copy downloaded successfully and its relevant pages were rendered in temporary storage for visual inspection. No provider credit, collection order, contact or access-control bypass was used.
