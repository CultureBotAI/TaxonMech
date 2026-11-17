# YAML Record Review: Microbacterium sp. HCZ21

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_hcz21.yaml`
- Started UTC: 2026-10-09T00:50:54Z
- Finished UTC: 2026-10-09T00:54:44Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036511`: species rank, Bacteria domain, parent `NCBITaxon:2609290`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Optional synonyms, nomenclature, mappings, strain/genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. This YAML is generated, not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/microbacterium_sp_hcz21.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/microbacterium_sp_hcz21.yaml --out /private/tmp/hcz21-strict.tsv`: passed, one file and zero errors; complete output TSV was header-only.
- Structured comparisons checked complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Full nucleotide XML consistency check: declared and actual length 1408, rRNA transcription equals DNA, no non-ACGT symbols. This is annotation consistency, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. These individual checks do not prove corpus reproduction. The embedded event was read; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036511&retmode=xml) agrees with identifier, label, rank, parent, genetic code and ancestor labels/ranks. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036511) confirms all ten root-first ancestor IDs. The chain runs through Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Microbacteriaceae, Microbacterium and unclassified Microbacterium. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

Species rank for an unnamed strain-associated NCBI taxon is not proof of a formally described species. Exact grounding denotes this identifier, not equivalence to a named congener. Live EFetch has no other names and pinned synonyms are empty. Pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222511`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32055`: scientific-name object.
- `data/taxa/PATHS.tsv:15018`: identifier and slug.
- `curation/seed_scope.tsv:322758`: date and admission reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records, not the existence of a strain designation.

Exact Nuccore query `txid1036511[Organism:noexp]` returned UID 334361394. Complete [JF806649.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806649.1) XML, including both references, all features and sequence, explicitly identifies HCZ21 and taxon 1036511. It is a 1408-base partial 16S marker, partial at both ends. The source feature supplies organism, genomic DNA, strain and taxon cross-reference, but no host, isolation-source, country, culture-deposit or assembly qualifier. Features are source and rRNA, not CDS.

References name Chen, Wu and Li, an unpublished seagrass-associated actinobacteria study and direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. No PMID or DOI is supplied in this accession. The marker is not a genome or phenotype assay, and missing source qualifiers must not be copied from neighboring sequences.

All 47 additional local candidates were fully read and excluded. Forty concern seven lactic-acid bacterial isolates under project PRJNA503586, not HCZ21. Six current RefSeq pairs use PRJNA224116; the seventh RefSeq record is historical. Their identifying chains are:

| Taxon and strain | Sample | GenBank accession | BV-BRC genomes |
| --- | --- | --- | --- |
| Fructilactobacillus fructivorans 196, taxid 1614 | SAMN10365113 | GCA_025129355.1 | 1614.26; 1614.30 |
| Lactobacillus helveticus 1069, taxid 1587 | SAMN10365114 | GCA_025129335.1 | 1587.771; 1587.796 |
| Lactobacillus helveticus 1072, taxid 1587 | SAMN10365115 | GCA_025129315.1 | 1587.772; 1587.795 |
| Lactobacillus helveticus 1073, taxid 1587 | SAMN10365116 | GCA_025129275.1 | 1587.770; 1587.794 |
| Lactiplantibacillus plantarum 192, taxid 1590 | SAMN10365117 | GCA_025129295.1 | 1590.3077; 1590.3130 |
| Lactiplantibacillus plantarum 1020, taxid 1590 | SAMN10365118 | GCA_025129255.1 | 1590.3076; 1590.3129 |
| Lactiplantibacillus pentosus 1524, taxid 1589 | SAMN10365119 | GCA_025129205.1 | 1589.273; 1589.289 |

These forty complete rows are located at:

- `data/bvbrc/bvbrc-0004.jsonl.gz`: lines 3818, 3819, 3820, 3841, 3842, 3843, 9036, 9052, 9951, 9952, 9999, 10000, 21683 and 21687.
- `data/catalog/ncbi_genbank-0023.jsonl.gz`: lines 14695, 14697, 14698, 14699, 14700, 14701 and 14702.
- `data/catalog/ncbi_refseq-0004.jsonl.gz`: lines 25319, 25320, 25321, 25322, 25323 and 25324; `data/catalog/ncbi_refseq_historical-0001.jsonl.gz:5088`.
- `data/catalog/gtdb_genomes-0005.jsonl.gz:5142`, `data/catalog/gtdb_genomes-0013.jsonl.gz:25472`, `data/catalog/gtdb_genomes-0002.jsonl.gz:14707`, `data/catalog/gtdb_genomes-0014.jsonl.gz:19548`, `data/catalog/gtdb_genomes-0015.jsonl.gz:7092`, `data/catalog/gtdb_genomes-0010.jsonl.gz:13179` and `data/catalog/gtdb_genomes-0001.jsonl.gz:6143`.
- `data/gold/projects.jsonl.gz`: lines 526023, 526075, 526143, 526144 and 526346. These respectively link strains 1524, 1020, 1072, 1069 and 196 to Gp0700452/Go0656196, Gp0700504/Go0656248, Gp0700572/Go0656316, Gp0700573/Go0656317 and Gp0700775/Go0656519.

All seven NCBI pairs explicitly mark paired sequence identity, but their annotation fields differ. GCF_025129315.1 is suppressed, not live since 2024-07-28, with an annotation-completeness failure; its GCA counterpart is retained as latest. GTDB therefore carries GB_GCA_025129315.1, while the other six use RS_GCF accessions. The two BV-BRC records per isolate are distinct source IDs; common sample/strain does not alone establish genome equivalence. GOLD Go/Gp identifiers are related records, not genome identifiers. Food, silage and geographic metadata in these records are not HCZ21 metadata.

Five candidates describe Paludibacter sp., taxid 1898105, Bin2_4: `data/bvbrc/bvbrc-0007.jsonl.gz:47818`, `data/catalog/ncbi_genbank-0009.jsonl.gz:7080`, `data/catalog/gtdb_genomes-0001.jsonl.gz:49869`, `data/raw/gtdb_species.tsv:135945` and `data/raw/gtdb_mappings.tsv:81783`. They link genome 1898105.37, GCA_010365115.1, ASM1036511v1, SAMN12810502, PRJNA573403 and JAAFGX000000000.1. GTDB's one-genome Paludibacter sp010365115 cluster maps to taxid 1898105 by `skos:broadMatch`, not equivalence. Its Antarctic H2-incubated subglacial sediment source does not concern HCZ21.

Two candidates describe Patescibacteria group bacterium, taxid 2052139, isolate SO_2017_GW1_166: `data/catalog/ncbi_genbank-0038.jsonl.gz:6510` and `data/catalog/gtdb_genomes-0001.jsonl.gz:22502`. They identify GCA_041662565.1, SAMN39904738, PRJNA823399, JBAZSE000000000.1 and GTDB JAUYIT01 sp041662565. The matched 1036511 is ungapped genome length, not taxid. Metagenome and undefined-genus flags concern that assembly, not this YAML.

The inspected [Wu et al. (2012) primary paper, DOI 10.5897/AJMR11.981](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii), Table 2, lists HCZ21's closest published species as Microbacterium esteraromaticum at 99.0% identity. Its own screening row is PKS-I negative, PKS-II positive and NRPS positive; the footnote defines PCR results. Methods describe seawater-washed, homogenized Thalassia hemprichii from Nancun Port and an accession range containing JF806649. The NCBI record supplies the exact accession/strain link. Interpretation: neither nearest-sequence similarity nor PCR screening establishes synonymy, a complete pathway, an identified natural product or antimicrobial activity. Methods and the complete table with its footnote were read as author-hosted HTML; original PDF layout was not visually checked.

A [2018 review, Table 1](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2018.01767/full), labels the isolate M. esteraromaticum HCZ21 and frames the table as endophytic diversity. That secondary label differs from NCBI and is preserved as a literature-scope difference, not adopted as an authoritative reassignment or proof of endophytic localization.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, mappings, deposits, genomes and graphs are appropriately unasserted without explicit identity chains. External marker/literature context does not require inventing a BacDive entry or altering this generated record.

Initial and expanded `rg --no-ignore --hidden -n -z -i` searches covered ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, HCZ21 and slug, then JF806649, UID 334361394 and both paper DOIs. Both found the same fifty rows: three own taxonomy/name/scope rows and 47 unrelated candidates. All were read fully. Five `SOURCE.json` files were separately parsed without a target match, and history filenames were independently inventoried. Absence statements are bounded to those roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. Exact accession web search returned no results; label searches also returned unrelated product and bibliographic-code matches. PubMed query for HCZ21/JF806649/JF806649.1 returned zero with quoted-phrase warnings. These are bounded misses, not proof of genome or literature absence; primary literature was directly inspected.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. External PCR screening does not establish expression-module coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. The record agrees with pinned and live NCBI taxonomy; unrelated catalog matches and a literature nearest-species label do not invalidate the seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join identifiers by numeric substring, count samples/projects as genomes, turn similarity into synonymy or promote screening evidence to a demonstrated phenotype.

Future taxonomy corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression tests; scope changes belong in `curation/seed_scope.tsv`. Optional marker/literature enrichment needs maintained-input and model/seeder support, not generated-YAML edits.

## Follow-up Checks

No corrective follow-up required for current claims. Before biological enrichment, visually verify the original paper's table and relevant figure, preserving the exact strain/accession chain and distinguishing study association, comparative identification and PCR evidence.

After an authorized input/seeder change, run focused regression tests, `just seed-canary NCBITaxon:1036511`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

Repository review, checklist and ownership guidance governed this review. The accessible author-hosted primary text was re-inspected for HCZ21. PDF routes had failed during the immediately preceding G2Z35 review; no successful PDF retrieval or visual check is claimed here.

Before/after YAML SHA-256 was `647e5aacb3a326591fd3820d3eeaf8cd9d9b1f8b1265b63d0a7d788e6ffa8a30`. Only this new timestamped report was written for this target. No YAML, input, history, status, generated page or GitHub object changed. Eukaryota and existing worktrees remained untouched.
