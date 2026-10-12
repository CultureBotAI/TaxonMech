# YAML Record Review: Exiguobacterium sp. M2N2c

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/exiguobacterium_sp_m2n2c.yaml`
- Started UTC: 2026-10-06T23:28:24Z
- Finished UTC: 2026-10-06T23:30:56Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035347` denotes Exiguobacterium sp. M2N2c, rank SPECIES, domain BACTERIA, parent NCBITaxon:2644629. It carries eleven root-first ancestors, genetic code 11, EXACT grounding, SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotype assertions, citations or causal graph are present. The generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/exiguobacterium_sp_m2n2c.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/exiguobacterium_sp_m2n2c.yaml --out /private/tmp/em2-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and is header-only.
- Exact backbone, all ancestors, children, seven other raw inventories, PATHS, scope, attestation and seed-event comparisons passed. Exact type-material, merged-ID and dropped-ID checks found no target entry.
- All 47 initial ignored-inclusive candidates, comprising 34 JSON objects and 13 TSV rows, and the one secondary candidate were read losslessly. Five SOURCE.json files were fully parsed and history filenames checked.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0, all 28 rows read. No organism/dataset matches M2N2c; iModulonDB is not applicable, not negative evidence.
- Live NCBI taxonomy XML/Datasets, exact Assembly/nuccore searches, full marker metadata excluding bases/translations and independent Datasets genome lookup succeeded.
- All ten BioSamples implicated by numeric matches were read in full with exact requested/returned-set agreement.
- PubMed metadata/abstract and the sequence-cited publisher paper's methods, results, Table 1 with footnotes, figure captions and discussion were inspected during this session, with the M2N2c-specific accession and row distinguished from neighboring isolates.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration or raw experimental data. Bounded comparisons do not reproduce the corpus.

## Identity and Grounding

The exact backbone at `data/raw/ncbitaxon_taxa.tsv:222034`, name object at `data/catalog/ncbi_names-0005.jsonl.gz:31509`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035347&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035347) agree on identifier, label, rank, parent, domain and code.

Every ancestor ID, label and normalized rank agrees: root (1); cellular organisms (131567); Bacteria (2); Bacillati (1783272); Bacillota (1239); Bacilli (91061); Caryophanales (1385); Caryophanales incertae sedis (539002); Caryophanales Family XII. Incertae Sedis (539742); Exiguobacterium (33986); unclassified Exiguobacterium (2644629). Datasets independently supplies root ID 1. Both incertae-sedis nodes are NO_RANK despite the family wording.

Pinned synonyms and live alternate-name content are empty; there are no pinned direct children. M2N2c, including its terminal lowercase c, is distinct from M2N2a, M2N2b and B1N2b. NCBI species rank is not formal nomenclatural standing or type status. A marker comparison does not establish a named-species reassignment.

## Evidence

The one NCBITAXON NAME attestation agrees with snapshot 2026-09-13. `data/taxa/PATHS.tsv:14525` pins the stem; `curation/seed_scope.tsv:322306` agrees with the event reason. The parsed raw, ATB and StrainInfo extraction timestamps are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected `src/taxonmech/seed.py` rule. This report does not promote SEEDED or provide human sign-off.

The exact nuccore search returned only [JF795956.1](https://www.ncbi.nlm.nih.gov/nuccore/JF795956.1), UID 333826810, a 523-bp partial 16S rRNA sequence. Its source explicitly names M2N2c and taxon 1035347, root nodules and host fenugreek. The 10-Apr-2011 direct submission by Rajendran and Patel names ARIBAS/Sardar Patel University, India; a submitter's address does not independently establish isolation locality. This marker contains no culture-deposit, BioSample or assembly assertion. Genetic code 11 is taxonomy metadata, not a marker CDS result.

The sequence and [PubMed 22518149](https://pubmed.ncbi.nlm.nih.gov/22518149/) identify Rajendran, Patel and Joshi's 2012 article, [DOI 10.1155/2012/693982](https://onlinelibrary.wiley.com/doi/10.1155/2012/693982), PMC3299478. The paper explicitly pairs M2N2c with JF795956 and reports 93% partial-16S identity to M527, not strain equivalence. Its distinct Table 1 row and coinoculation experiments cannot be transferred to neighboring isolate labels or treated as standalone nitrogen-fixation proof. The current NCBI lineage is carried verbatim; historical literature terminology is not a reason to hand-edit it.

Exact Assembly search returned zero with a phrase-not-found warning; [Datasets genome](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035347/dataset_report) independently returned an empty object. This is a bounded dated search, not proof of genome absence everywhere.

## Completeness

The taxon-ID, separator-tolerant M2N2c and stem searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included.

Three initial rows are exact identity/scope records. Two concern Mycobacterium tuberculosis ERR1035347, taxon 1773: BV-BRC 1773.18363 at `data/bvbrc/bvbrc-0006.jsonl.gz:6161`, and ATB SAMEA3558880/ERR1035347/ERZ9334526 at `data/catalog/allthebacteria.tsv.xz:569817`.

The other 42 rows all concern ten Escherichia coli samples, taxon 562, BioProject PRJNA218110: ten BV-BRC rows, ten current GenBank rows, nine historical GenBank rows, ten ATB rows and three GOLD project rows. The complete source records and each full live BioSample agree on these distinct sample/strain identities:

| BioSample | E. coli strain | Current GenBank | ATB ENA analysis |
|---|---|---|---|
| SAMN10353470 | PNUSAE019768 | GCA_003760045.2 | ERZ9092839 |
| SAMN10353471 | PNUSAE019767 | GCA_003768825.2 | ERZ9092838 |
| SAMN10353472 | PNUSAE019766 | GCA_003769105.2 | ERZ9092842 |
| SAMN10353473 | PNUSAE019388 | GCA_003757345.2 | ERZ25499666 |
| SAMN10353474 | PNUSAE018364 | GCA_003768385.2 | ERZ9092840 |
| SAMN10353475 | PNUSAE017849 | GCA_047775255.1 | ERZ9092856 |
| SAMN10353476 | PNUSAE019764 | GCA_003754985.2 | ERZ9092845 |
| SAMN10353477 | PNUSAE019763 | GCA_003760925.2 | ERZ9092846 |
| SAMN10353478 | PNUSAE019762 | GCA_003760785.2 | ERZ9092847 |
| SAMN10353479 | PNUSAE019761 | GCA_003757305.2 | ERZ9092848 |

These live BioSamples describe 2018 USA PulseNet samples with source_type human, not the fenugreek isolate. Every ATB row has PASS filters and an available FASTA; availability does not establish target identity. Nine historical .1 assemblies are replaced by their .2 versions, while the BV-BRC source retains the .1 accessions. Their non-live date is 2020-03-07 except GCA_003757345.1, dated 2020-03-13. The PNUSAE017849 BV-BRC row has no assembly_accession field, although its current GenBank row supplies GCA_047775255.1; this unrelated source difference is not a target defect.

The three GOLD project rows pair Gp0386906/Go0502629 with SAMN10353476, Gp0386907/Go0502630 with SAMN10353477, and Gp0386971/Go0502694 with SAMN10353473. They are project/organism records for the named E. coli strains, not M2N2c genomes. ATB rows occupy physical lines 1502977-1502986. None of these numerical BioSample matches supplies an M2N2c identity chain.

Follow-up searches for JF795956, PMID digits and the full DOI returned only `data/catalog/ncbi_genbank-0044.jsonl.gz:21313`: Salmonella enterica serovar Muenster FSIS22518149, taxon 82689, GCA_048160595.1, SAMN47108730, PRJNA242847, with no pubmed_id. A strain suffix is not a citation. No exact marker or DOI evidence was found within the bounded roots or separately parsed metadata/history names.

Zero inventoried BacDive strains agrees with the exact inventory and empty descendant set. It is not a denial that M2N2c is a biological isolate. No missing required nomenclature, mapping, strain or genome assertion was established. Literature, marker and definition fields remain optional for this seeded record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated assertions. The limited marker comparison is not sufficient to independently resolve biological species membership, but the record correctly represents its current NCBI identity rather than claiming such a resolution.

## Recommended Edits

None required. Leave the generated YAML and lifecycle status unchanged. Do not join numeric BioSample matches, collapse accession versions or convert JF795956.1 to a genome.

Future supported strain/deposit enrichment belongs in maintained source ingestion, including `scripts/extract_source_inventory.py`, followed by the documented seeder workflow. Optional literature needs a maintained representation that survives regeneration. Experimental trait, habitat, medium and interaction assertions belong in the respective sibling repositories.

## Follow-up Checks

After authorized upstream changes, repeat both exact-target validators and inspect the emitted TSV. Generator/source changes also require the documented canary and full `just verify-corpus`/QC gates; no target-only reproduction gate is asserted.

Any future reclassification must be resolved at the taxonomic authority rather than inferred from the short marker's similarity value. Genome associations need an exact supported deposit/sample chain and preservation of source-specific identities and versions.

## Additional Notes

Guidance and generation/history boundaries were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target remains byte-identical to its initial complete read. Only this new timestamped report is written; no source input, YAML, generated product, prior report, history record, event or lifecycle status is changed. Eukaryota remains untouched.
