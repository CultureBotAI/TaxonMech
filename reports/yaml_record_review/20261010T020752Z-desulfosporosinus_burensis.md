# YAML Record Review: Desulfosporosinus burensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/desulfosporosinus_burensis.yaml`
- Started UTC: 2026-10-10T02:03:53Z
- Finished UTC: 2026-10-10T02:07:52Z
- Verdict: pass

## Target

The complete 267-line generated `TaxonRecord` was read. `NCBITaxon:1037382` denotes Desulfosporosinus burensis, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:79206`, genetic code 11, grounding `EXACT`, status `SEEDED`.

It contains nine ancestors, one LPSN entry, two related synonyms, one BacDive strain, two assembly assertions, ten related-record assertions, seven source attestations and one seed event. Source-search candidates were examined only for their relevance to this target.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/desulfosporosinus_burensis.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/desulfosporosinus_burensis.yaml --out /private/tmp/taxonmech-burensis-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, complete lineage, code, synonym columns, source attestations, index/scope entries and exact seed reason. Complete backbone and status inventories found no direct child, own merged-ID entry or own dropped entry.
- Exact multiset comparisons verified both assembly assertions and all ten related assertions against raw and StrainInfo inventories, including serialized provenance. Whole-deposit CAFI matching passed. No own genome-record or ATB strain-link row was present.
- Independent complete native reads covered BacDive 23183, StrainInfo 398030, the two NCBI assembly rows, three NCBI name rows, three GOLD organisms and the target SeqCode catalog row. Native StrainInfo content was checked separately from the link deserializer.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, source replay, rendering and publication gates. No graph is asserted, so `just validate-products` has no applicable nodes. Focused agreement is not corpus reproduction.
- Configured external kg-microbe MediaDive, Madin and BactoTraits edge files were unavailable at their exact paths. Committed inventories and count-extraction code were inspected; the original assertions were not independently replayed. No absence claim is made about all external checkouts.
- Publication landing pages and the full primary PubMed abstract/bibliography were inspected, but both publisher full-text endpoints were unavailable through the web reader. The MediaDive J865 page was also unavailable. No live GOLD refresh, phylogenetic reanalysis, independent ANI calculation or experimental genome-quality assessment was performed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222738`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037382&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037382) agree on name, species rank, parent and code. Datasets reports one assembly.

The complete stored lineage matches the backbone: root, cellular organisms, Bacteria, Bacillati, Bacillota, Clostridia, Eubacteriales, Desulfitobacteriaceae and Desulfosporosinus. Live EFetch confirms every ancestor below root, while Datasets includes root 1. Older BacDive Peptococcaceae/Clostridiales/Firmicutes strings and the JCM page's differing higher classification do not supersede this record's NCBI chain.

Native NCBI names `data/catalog/ncbi_names-0005.jsonl.gz:32367` through 32369 contain the authority, scientific name and included BSREI1 label. The authority and included label are appropriately related synonyms, not exact biological equivalence assertions. Six own type-material rows support DSM 24089, JCM 17380 and BSREI1 with source spelling variants.

[LPSN 790530](https://lpsn.dsmz.de/species/desulfosporosinus-burensis) supports the accepted name, Mayeux et al. 2013 authority, species rank, valid-publication/correct-name status, marker and both culture deposits. The pinned LPSN row is `data/raw/lpsn_names.tsv:27472`. No own GTDB mapping is in the complete inventory; the omitted mapping and xref are appropriate to this snapshot, not evidence of universal absence from GTDB.

## Evidence

The inspected [Mayeux et al. description, PMID 22544786](https://pubmed.ncbi.nlm.nih.gov/22544786/), DOI 10.1099/ijs.0.035238-0, identifies BSREI1 = DSM 24089 = JCM 17380 as the type strain. Its abstract reports the isolate from deep pore water at Bure and strain-level physiological characterization. The [second DOI, 10.1099/ijs.0.051771-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.051771-0), resolves to the May 2013 notification for names published in IJSEM volume 63, part 2. It is not a second experimental description.

[JF810424.1](https://www.ncbi.nlm.nih.gov/nuccore/JF810424.1) resolves the stored unversioned marker. Its full annotation identifies a 1,533-base partial 16S sequence from BSREI1, taxon 1037382, type material, deep-clay isolation source and the same description DOI/PMID. Declared and actual lengths agree; the sequence includes N bases. Preserve the unversioned source accession and do not count this marker as a genome.

[BacDive 23183](https://bacdive.dsmz.de/strain/23183) and native row `data/bacdive/records.jsonl.gz:22986` support BSREI1, both deposits, species-level classification and type status. Its native projection has a 16S block but no genome block. The generated strain therefore does not claim a BacDive-sourced genome. The [JCM 17380 catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=17380) independently supports the BSREI1 provenance, DSM 24089 equivalence, type designation, marker and assembly family.

The complete native GenBank/RefSeq rows identify GCA_054657535.1 and GCF_054657535.1 as a paired assembly from type material, strain JCM 17380, at contig level, with 128 contigs and 5,755,548 bases. They are two source assertions about the pair, not two biological strains. Both carry BioSample SAMD00887380. GenBank carries PRJDB20344, while RefSeq carries umbrella PRJNA224116; the YAML preserves those separate source paths.

The live [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_054657535.1/dataset_report) confirms current version 1, the paired RefSeq accession, species/deposit, type-material status, BioSample and GenBank project. Native rows are `data/catalog/ncbi_genbank-0050.jsonl.gz:24767` and `data/catalog/ncbi_refseq-0008.jsonl.gz:16202`. No unversioned-to-versioned equivalence is invented.

Three native GOLD organisms agree with the attestation count of three. Go0043658 supplies DSM 24089 in culture-collection and strain fields; Go0613493 supplies JCM 17380 in both fields. Their four related-record assertions retain these distinct provenance paths rather than counting four organisms. Go0613494 supplies only the bare designation BSREI1, so it does not satisfy the whole-culture-identifier join used here. The ignored-inclusive GOLD-ID follow-up found no project or analysis rows attached to these organisms. Do not infer a genome chain from their species or strain names.

StrainInfo native row `data/straininfo/records.jsonl.gz:295919` verifies SI-ID398030, DOI version 10.60712/SI-ID398030.3, BacDive 23183, taxon 1037382 and published-online status. Its only deposit object is available type deposit DSM 24089/SI-DP904706. JCM 17380 is a relation designation, not a second SI-DP object; no sequence list is supplied. The YAML correctly retains only the DSM deposit and strain assertions and invents neither a JCM deposit ID nor a StrainInfo genome. The [DataCite DOI record](https://api.datacite.org/dois/10.60712/SI-ID398030.3) resolves to the corresponding StrainInfo record and version 3.

All attestations agree with their committed inventory units: NCBITAXON 1 NAME, LPSN 1 NAME, BACDIVE 1 STRAIN, MEDIADIVE 2 MEDIUM, GOLD 3 ORGANISM, MADIN 13 TRAIT_ASSERTION and BACTOTRAITS 19 TRAIT_ASSERTION. The MediaDive inventory identifies 641 and J865. BacDive associates the strain with DSMZ medium 641, and JCM lists medium 865. This is supporting catalog context, not an independent replay of the unavailable MediaDive edge file or verification of every medium formulation.

Madin and BactoTraits counts are source subject-row counts in `src/taxonmech/extract.py`, not thirteen and nineteen experimentally revalidated phenotypes. Their underlying trait values are not asserted in this YAML.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It included the taxon ID, exact name/slug, BSREI1, DSM 24089, JCM 17380, BacDive/SI identifiers and deposit ID.

Identity and matched fields of all 121 candidates were inspected. The fourteen ATB hits were checksum substrings for other taxa, not own-strain links. Other collisions included KCTC/ATCC/ICMP 23183, unrelated BV-BRC genome suffixes, assembly statistics and unrelated SI deposits. Eukaryotic source matches were distinguished by their source identities without opening any Eukaryota YAML.

A narrower assembly/BioSample/marker/GOLD-ID search returned seventeen lines, all already represented in inspected own-source rows, and no ATB entry. Five SOURCE.json files were independently enumerated and parsed. Gitignore-independent filename enumeration found one target YAML and no prior target report; history filenames had no target-specific hit.

The single classified BacDive strain is retained without truncation. Empty optional definitions, mechanistic claims and graphs need not be invented. iModulonDB is not applicable to the taxonomy/deposit/identifier assertions under review; no transcriptomic claim is present.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the assertions made by this generated record. Native sources support identity, type deposits, marker placement and the complete stored identifier/provenance inventories. External metadata discrepancies and unavailable checks below constrain future biological reuse but do not contradict an asserted YAML field.

## Recommended Edits

None required for this record. Do not patch generated YAML, promote its review status or append curation history from this review.

Future corrections, if independently established, belong in maintained source inputs and their transforms, followed by extraction/seeding. In particular, do not create a JCM StrainInfo deposit or import a sequence without an explicit same-deposit SI-DP binding. Preserve both source-specific project assertions.

## Follow-up Checks

For later trait or habitat curation, inspect the complete primary description and reconcile the depth/Gram-stain discrepancies noted below before introducing those fields. Review the assembly's quality evidence before using it for comparative-genome conclusions. Any external correction would need a separately authorized source update; this review contacts no provider.

A later source replay should check the two MediaDive links and the Madin/BactoTraits count units against their configured KGX files, then run the documented canary, schema/strict/history and full-corpus reproduction/QC gates. Those deferred checks are not represented as passing here.

## Additional Notes

- The primary description's abstract reports a borehole depth of 490 m below surface; JCM and the live BioSample report 4490 m. The source discrepancy is unresolved here. The YAML does not assert a depth.
- The description's abstract says Gram-positive, while BacDive's inspected web page says Gram-negative. The YAML does not assert Gram stain, and the aggregate trait counts cannot resolve this conflict.
- Live NCBI reports CheckM completeness 84.66 and contamination 12.07. These source estimates warrant caution; the YAML does not claim a high-quality or contamination-free genome. The ANI metadata says taxonomy check OK and notes that a type-strain match is not expected; its below-threshold other-species match is not evidence that this taxon should be renamed.
- YAML SHA-256: `29491dd7cb114b8fa8bfe21929d4cd44b6fb1dd232b6db8481b0918a4e62f82a`.
- `data/taxa/PATHS.tsv:15288` and `curation/seed_scope.tsv:7217` uniquely resolve the target; legacy page row 925 is only an alias. The seed retains 2026-09-13T17:54:04Z and its exact seven-source reason.
- SeqCode record 6544 is catalog context, not an additional curated grounding assertion.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No YAML, source input, schema, history, page, branch, worktree or GitHub state was changed.
