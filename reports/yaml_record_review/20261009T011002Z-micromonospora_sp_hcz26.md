# YAML Record Review: Micromonospora sp. HCZ26

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/micromonospora_sp_hcz26.yaml`
- Started UTC: 2026-10-09T01:01:43Z
- Finished UTC: 2026-10-09T01:10:02Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036513`: species rank, Bacteria, parent `NCBITaxon:2617518`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Optional synonyms, nomenclature, mappings, strain/genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. The generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/micromonospora_sp_hcz26.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/micromonospora_sp_hcz26.yaml --out /private/tmp/micromonosporaHCZ26-strict.tsv`: passed, one file and zero errors. Complete TSV was header-only.
- Structured comparisons checked complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Own nucleotide XML consistency check: declared and actual length 1396, rRNA transcription equals DNA, no non-ACGT symbols. This is annotation consistency, not independent taxonomic inference.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. Embedded history was read; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Complete [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036513&retmode=xml) agrees with identifier, label, rank, parent, code and ancestor labels/ranks. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036513) confirms all ten root-first ancestor IDs. The chain includes Bacillati, Actinomycetota, Actinomycetes, Micromonosporales, Micromonosporaceae, Micromonospora and unclassified Micromonospora. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

Species rank for an unnamed strain-associated NCBI taxon does not establish a formally described species. Exact grounding denotes this identifier. Live EFetch supplies no other names; pinned synonyms are empty. Pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

The taxonomy projection is supported. A likely literature association has a genus-level discrepancy, detailed below; it is not evidence sufficient to replace this identifier or label.

## Evidence

Complete own source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222513`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32057`: scientific-name object.
- `data/taxa/PATHS.tsv:15020`: identifier and slug.
- `curation/seed_scope.tsv:322760`: admission date/reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records, not whether the taxon has a strain designation.

Exact Nuccore query `txid1036513[Organism:noexp]` returned UID 334361392. Complete [JF806647.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806647.1) XML, including both references, all features and sequence, explicitly identifies HCZ26 and taxon 1036513. It is a 1396-base partial 16S marker, partial at both ends. Source qualifiers give organism, genomic DNA, strain and taxon cross-reference, but no host, isolation-source, country, culture-deposit or assembly qualifier. Features are source and rRNA, not CDS.

References name Chen, Wu and Li, an unpublished seagrass-associated actinobacteria study, and direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. No PMID or DOI is supplied. A marker is not a genome or phenotype assay.

All 58 additional local candidates were fully read and excluded. Fifty-three concern nine lactic-acid bacterial isolates, with GenBank project PRJNA503586 and paired RefSeq project PRJNA224116:

| Taxon and strain | BioSample | GenBank accession | BV-BRC pair |
| --- | --- | --- | --- |
| Lactococcus lactis 1037, taxid 1358 | SAMN10365130 | GCA_025132965.1 | 1358.1701; 1358.1737 |
| Lactococcus lactis 1040, taxid 1358 | SAMN10365131 | GCA_025132985.1 | 1358.1703; 1358.1739 |
| Streptococcus thermophilus 1047, taxid 1308 | SAMN10365132 | GCA_025132955.1 | 1308.1821; 1308.1878 |
| Lactococcus lactis 1053, taxid 1358 | SAMN10365133 | GCA_025132925.1 | 1358.1700; 1358.1735 |
| Lactococcus lactis 1102, taxid 1358 | SAMN10365134 | GCA_025132885.1 | 1358.1699; 1358.1736 |
| Pediococcus pentosaceus 941, taxid 1255 | SAMN10365135 | GCA_025132915.1 | 1255.441; 1255.455 |
| Pediococcus pentosaceus 1021, taxid 1255 | SAMN10365137 | GCA_025132875.1 | 1255.440; 1255.456 |
| Streptococcus thermophilus 973, taxid 1308 | SAMN10365138 | GCA_025132855.1 | 1308.1820; 1308.1879 |
| Streptococcus thermophilus 974, taxid 1308 | SAMN10365139 | GCA_025132835.1 | 1308.1819; 1308.1877 |

These comprise 18 BV-BRC objects, 18 NCBI assembly objects, nine GTDB objects and eight GOLD projects. Complete native rows, including nested source fields, were inspected at:

- `data/bvbrc/bvbrc-0001.jsonl.gz`: lines 29536, 29537, 29538, 29591, 29592 and 29593; `data/bvbrc/bvbrc-0000.jsonl.gz`: 36081, 36082, 36096 and 36097; `data/bvbrc/bvbrc-0002.jsonl.gz`: 41116, 41117, 41118, 41120, 41151, 41152, 41153 and 41155.
- `data/catalog/ncbi_genbank-0023.jsonl.gz`: lines 14876 through 14884; `data/catalog/ncbi_refseq-0004.jsonl.gz`: 25350 through 25358.
- `data/catalog/gtdb_genomes-0004.jsonl.gz`: lines 37757, 45890 and 46644; `data/catalog/gtdb_genomes-0012.jsonl.gz:49835`; `data/catalog/gtdb_genomes-0003.jsonl.gz`: 21070 and 44852; `data/catalog/gtdb_genomes-0014.jsonl.gz:39825`; `data/catalog/gtdb_genomes-0002.jsonl.gz`: 35402 and 43892.
- `data/gold/projects.jsonl.gz`: lines 526034, 526079, 526130, 526141, 526145, 526165, 526166 and 526239.

All nine GCA/GCF pairs explicitly assert paired sequence identity and latest status; annotation metadata differ. GTDB uses corresponding RS_GCF accessions as nonrepresentatives. These food/dairy isolates do not concern HCZ26. GOLD project/organism identifiers are not genome identifiers. L. lactis 1053 is scaffold-level, unlike the other contig-level assemblies; no such detail is transferred to this target.

The other five rows identify Flavobacterium sp. Bin2_5, taxid 239: `data/bvbrc/bvbrc-0014.jsonl.gz:4276`, `data/catalog/ncbi_genbank-0009.jsonl.gz:7081`, `data/catalog/gtdb_genomes-0007.jsonl.gz:4430`, `data/raw/gtdb_species.tsv:63873` and `data/raw/gtdb_mappings.tsv:184482`. They link BV-BRC 239.70, GCA_010365135.1, assembly ASM1036513v1, SAMN12810503, PRJNA573403 and JAAFGY000000000.1. GTDB uses representative GB_GCA_010365135.1 for a one-genome cluster and broadMatch to taxid 239. This Antarctic subglacial metagenome assembly is excluded from RefSeq for MAG completeness failure/metagenome status. Matching assembly-name digits are not taxon identity.

Expanded public Nuccore phrase search for HCZ26 returned the own marker plus 32 UIDs, 1828754825 through 1828754856. A successfully parsed 32-record EFetch response established shared organism Listeria monocytogenes, BioSample SAMN14422988 and assembly GCF_011881945.1; these are not the target. The displayed per-record metadata output was truncated. Subsequent compact reads failed with incomplete HTTP responses, so no complete CDS/locus-tag audit or explanation of why the search matched is claimed.

The [author-hosted text of Wu et al. (2012), DOI 10.5897/AJMR11.981](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii), Table 2, lists HCZ26 with closest species Streptomyces parvulus, 99.71%, and positive PKS-I, PKS-II and NRPS PCR screens. The accession range in methods includes JF806647, but does not explicitly map that accession to this row. Shared authors, topic and code suggest a connection; that connection remains an inference. The cross-genus discrepancy is unresolved, not synonymy or proof of antimicrobial activity.

## Completeness

Sufficient for the stored NCBI taxonomy-seed assertions, with a non-blocking literature-provenance issue. Optional genomes, deposits, mappings and graphs should stay unasserted without explicit identity chains. Do not import the paper's biological results while the linkage is unresolved.

Initial and expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, HCZ26 and slug, then JF806647, UID 334361392 and the primary DOI. Both found the same 61 rows: three own taxonomy/name/scope rows and 58 unrelated candidates. All local candidates were read fully. Five SOURCE.json files were separately parsed without a target match; history filenames were independently inventoried. Absence claims are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found error and no-items warning. PubMed query for HCZ26/JF806647/JF806647.1 returned zero with quoted-phrase warnings. Neither result establishes universal genome or literature absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. **Minor: unresolved likely literature linkage across genera.** The accession and live taxonomy identify Micromonospora; the likely associated paper's HCZ26 row has a Streptomyces comparison. The record does not cite or import that paper, and exact NCBI grounding is verified, so this is a non-blocking provenance gap rather than a demonstrated wrong-identity or projection defect. Resolve the strain/accession chain before enrichment. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Any supported additional representation requires maintained-input/model support through `src/taxonmech/seed.py`, not a generated-YAML patch.

## Recommended Edits

No immediate YAML edit or status promotion. Preserve `SEEDED` and the verified NCBI identifier. Do not substitute Streptomyces parvulus from a nearest-species table, invent a synonym, or transfer PCR screens into a phenotype claim.

After provenance resolution, only an authoritative correction should change taxonomy inputs. A projection defect, if subsequently demonstrated, belongs in `src/taxonmech/seed.py` with regression tests; admission changes belong in `curation/seed_scope.tsv`. No projection/admission defect was found here.

## Follow-up Checks

Obtain a readable original paper PDF and visually check Table 2 and the HCZ26 positions/accession labels in its phylogenetic figures. Establish an explicit connection to JF806647.1 and check whether an erratum or authoritative corrected submission resolves the discrepancy. No outreach or paid research was performed. Do not choose a genus from an unverified figure extraction or a strain-code match alone.

Original-paper PDF routes were unavailable in the preceding related review. This review used inspected author-hosted methods/table text. Figure image routes returned an empty tool result, a not-found response, or HTTP 403; the institutional paper page timed out. No original figure or PDF was visually verified. External fetch failures are not evidence of absent corrections.

After an authorized input/seeder change, run focused regression tests, `just seed-canary NCBITaxon:1036513`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Local review, checklist and ownership guidance governed this individual review. The full target YAML and its own sequence record were independently read; no verdict or accession identity was inherited from neighboring records.

Before/after YAML SHA-256 was `ea9c28610cc78d5c05e072c91ff85d42e0726839d766e090c6119992b19d9c98`. Only this new timestamped report was written for this target. No YAML, source, history, status, generated page or GitHub object changed. Eukaryota and existing worktrees remained untouched.
