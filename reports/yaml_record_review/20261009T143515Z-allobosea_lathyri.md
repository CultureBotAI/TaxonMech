# YAML Record Review: Allobosea lathyri

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/allobosea_lathyri.yaml`
- Started UTC: 2026-10-09T14:23:56Z
- Finished UTC: 2026-10-09T14:35:15Z
- Verdict: pass

## Target

The complete 926-line generated `TaxonRecord` was read before judgement. It denotes `NCBITaxon:1036778`, Allobosea lathyri, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:85413`, genetic code 11, `EXACT` grounding and `SEEDED` lifecycle. It contains nine ancestors, seven source-qualified synonyms, one current LPSN name, one GTDB species mapping, one type-strain entry, eight source attestations and one seed event.

The listed strain is `kgmicrobe.strain:bacdive_1791`, R-46060, with CCUG 61247, DSM 26656 and LMG 26379 deposits. Its 10 assembly links, eight other genome links and 36 related-record links are source assertions, not 54 distinct biological genomes. `data/taxa/PATHS.tsv:15145`, `curation/seed_scope.tsv:4049` and `curation/legacy_page_paths.tsv:902` were checked. The YAML is generated output, not the maintained curation input.

## Validation

Both commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/allobosea_lathyri.yaml`: exit 0, no issues; the documented `just validate` implementation.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/allobosea_lathyri.yaml --workers 1 --out /private/tmp/taxonmech-alathyri-20261009-validation.tsv`: exit 0, one file, zero errors. The entire result TSV was read; it contains only its header.

A separate read-only structured comparison checked all 10 assembly, eight genome and 36 related assertions against their complete raw, StrainInfo and ATB inventory rows. Nested StrainInfo evidence was converted and checked through the inspected `straininfo._link` function. All seven ATB sample assertions were validated through `atb._sample_links`, matched the YAML without loss, and occur in the strain's related records. This bounded comparison is not the repository's full reproduction gate.

CAFI's maintained matcher accepted the three deposited accessions and matched their existing CURIEs exactly. It rejected bare R-46060, B1199 and B1203T1 as cross-source deposit keys. The additional LMG 26380 accession is valid but distinct.

Not checked: corpus-wide schema validation, `just verify-corpus`, `just qc`, the full test suite, complete provenance hashes and rendered products. The reproduction command has no record selector. `just validate-products` does not apply to the record's NCBITaxon identity or its absent curator-grounded graph. No separate target history file was found for `just validate-history`; the embedded event passed schema validation. No generator or lifecycle promotion was run.

## Identity and Grounding

The full backbone row `data/raw/ncbitaxon_taxa.tsv:222618` and seven native name rows at `data/catalog/ncbi_names-0005.jsonl.gz:32181` onward agree with the YAML. Fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036778&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036778) confirm the ID, label, parent, species rank and code. The complete root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Alloboseaceae, Allobosea. All ancestor IDs and carried ranks agree.

The native NCBI synonym Bosea lathyri is correctly retained as exact; authority strings and the three strain-qualified `includes` names remain related synonyms. The latter do not equate LMG 26380 with the type strain. The 11 native type-material spellings support the recognized type deposits and personal designations. Two merged IDs, 1053469 and 946786, resolve to 1036778 in `data/raw/ncbi_merged_ids.tsv:1836` and `:99832`; neither is a separate current child. No own child or dropped row was found in the complete structured inventory scans.

[LPSN 70769](https://lpsn.dsmz.de/species/allobosea-lathyri) confirms the 2026 combination, authority, valid publication, correct-name status, three type deposits and FR774993 marker. [LPSN 790217](https://lpsn.dsmz.de/species/bosea-lathyri) retains the old homotypic synonym as illegitimate. Their complete raw rows, `data/raw/lpsn_names.tsv:11182` and `:27197`, were read. The old name has no direct NCBI mapping in that inventory and is reached by the reciprocal synonym link, explaining why it is a related synonym rather than another current nomenclature entry.

Fresh PubMed metadata resolves PMID 41649870 to [DOI 10.1099/ijsem.0.007072](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.007072). Its complete abstract explicitly includes this replacement combination. The separately cited [notification list, DOI 10.1099/ijsem.0.007121](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.007121), resolves at its publisher and Crossref; its title concerns volume 76 part 2, although the notification itself appeared in issue 5. No bibliographic mismatch is present in the YAML.

## Evidence

The following source chains were read in full, not inferred from matching species names:

| Claim | Inspected support and scope |
|---|---|
| One type strain and three deposits | BacDive native row `data/bacdive/records.jsonl.gz:1786`, raw strain row `data/raw/bacdive_strains.tsv:1787`, LPSN type designations and the current [BacDive 1791 page](https://bacdive.dsmz.de/strain/1791) agree. The original description's fresh [PMID 22155761 abstract](https://pubmed.ncbi.nlm.nih.gov/22155761/) independently names LMG 26379 = CCUG 61247 = R-46060. |
| BacDive genome assertions | Its own genome row, reference 66792, supplies unversioned GCA_900108245, IMG 2622736433 and PATRIC 1036778.3. The reference resolves on BacDive to automated DiASPora annotation, not experimental proof. Versions were not silently appended to the unversioned assertion. |
| BV-BRC | `data/bvbrc/bvbrc-0000.jsonl.gz:3398` links genome 1036778.3, GCA_900108245.1, SAMN04488115 and PRJEB16701 through explicit DSM 26656 values in both culture-collection and strain fields. Both distinct provenance assertions are preserved. |
| GOLD | Organism Go0043698 (`data/gold/organisms.jsonl.gz:36620`) identifies DSM 26656. Project Gp0113046 (`projects.jsonl.gz:64685`) connects it to SAMN04488115 and PRJNA303611. Analysis Ga0070576 (`analyses.jsonl.gz:44414`) names that project and supplies GCA_900108245.1 and IMG 2622736433. Its empty direct organism field is resolved by the explicit project chain, not taxonomy. |
| Other GOLD organisms | Complete rows 446580, 446581 and 446582 identify Go0615878/R-46060, Go0615879/LMG 26379 and Go0615880/CCUG 61247. Four organism records support the taxon-level count. The bare R-46060 row has no eligible collection identifier and does not create an extra direct strain join. |
| NCBI assemblies | GenBank row `data/catalog/ncbi_genbank-0056.jsonl.gz:39507` and RefSeq row `data/catalog/ncbi_refseq-0009.jsonl.gz:27240` explicitly pair GCA/GCF_900108245.1 and name DSM 26656. Their source filenames match `conf/ncbi_assemblies.yaml`. Fresh [NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_900108245.1/dataset_report) confirms the current scaffold assembly, pair, taxon, type material and sample. |
| GTDB | `data/catalog/gtdb_genomes-0013.jsonl.gz:37266` is RS_GCF_900108245.1, DSM 26656, a representative/type genome in Allobosea lathyri. `data/raw/gtdb_species.tsv:7709` and `gtdb_mappings.tsv:1465` support the one-genome close match; LPSN independently links this species. Native GTDB Rhizobiales/Beijerinckiaceae classification is not substituted for NCBI's lineage. Live GTDB pages were inaccessible; current-release agreement beyond the pinned catalog is not claimed. |

The assembly is a 25-scaffold, 26-contig sequence of 5,918,613 total bases, not a complete chromosome. BioProject PRJEB16701 is the submission project, PRJNA303611 is carried by the BioSample/GOLD project, and PRJNA224116 is the RefSeq/GTDB inventory context. Those distinct source scopes are retained rather than collapsed into genome identity.

StrainInfo native record `data/straininfo/records.jsonl.gz:286718` supplies SI-ID 371088, the three own deposits, source statuses and [version DOI 10.60712/SI-ID371088.3](https://api.datacite.org/dois/10.60712/SI-ID371088.3). DataCite confirms that DOI denotes version 3 of a three-deposit dataset, not a research paper. Deposit 908008/DSM 26656 owns the unversioned genome assertion. Deposit 865462/LMG 26379 owns the six marker assertions. Deposit 873364/CCUG 61247 is not used to transfer those sequences across deposits.

Fresh complete GenBank feature/reference metadata verified every carried marker, all assigned to taxon 1036778 and all version 1 at retrieval. The actual sequence lengths matched their declarations and used only A/C/G/T:

| Accession | Length | Source qualifier and annotation |
|---|---:|---|
| [FR774993.1](https://www.ncbi.nlm.nih.gov/nuccore/FR774993.1) | 1441 | Type strain R-46060 = B1199; partial 16S. LPSN nomenclatural marker, not an assembly. |
| [FR871206.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871206.1) | 496 | Type strain LMG 26379; atpD. |
| [FR871218.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871218.1) | 399 | Type strain LMG 26379; recA. |
| [FR871226.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871226.1) | 673 | Type strain LMG 26379; gyrB. |
| [FR871234.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871234.1) | 1439 | Type strain LMG 26379; rpoB. |
| [FR871242.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871242.1) | 286 | Type strain LMG 26379; dnaK. |
| [KM065742.1](https://www.ncbi.nlm.nih.gov/nuccore/KM065742.1) | 809 | LMG 26379; partial 16S-23S spacer/23S sequence. Its later comparative-study citation is not a different source organism. |

These are source sequence descriptions, not independently validated protein functions or expression claims. The repository's structured iModulonDB runner was resolved in the local `culturebotai-claw` checkout and `kg-microbe-sources imodulondb datasets` succeeded after network approval. Its complete 28-dataset list contains no Bosea/Allobosea organism. iModulonDB is therefore not applicable; absence is not negative biological evidence.

ATB native catalog row `data/catalog/allthebacteria.tsv.xz:1133134`, compact assembly row 4114, strain-link row 3235 and five genome-link rows 13952-13956 support `atb.assembly:202505.SAMN04488115`. The release, dataset, run, SeqKit sum, both PASS flags, Sylph label, download/archive locators and all seven sample-evidence objects are retained exactly. Fresh [ENA analysis ERZ26864573](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ26864573) explicitly names SAMN04488115 and SRR4163852; the [run record](https://www.ebi.ac.uk/ena/browser/api/xml/SRR4163852) names DSM 26656. ENA describes a Shovill/SPAdes reassembly, whereas NCBI describes the original ALLPATHS assembly. A shared sample is not assembly equivalence. No FASTA/archive download or byte-level SeqKit reproduction was performed.

The eight attestation counts match their own inventories: NCBI 1 NAME, LPSN 1 NAME, GTDB 1 GENOME, BacDive 1 STRAIN, MediaDive 1 MEDIUM, GOLD 4 ORGANISM, Madin 4 TRAIT_ASSERTION and BactoTraits 6 TRAIT_ASSERTION. Units are not summed. MediaDive's native medium is [1a](https://mediadive.dsmz.de/medium/1a); the [DSM 26656 catalog](https://www.dsmz.de/collection/catalogue/details/culture/DSM-26656) independently lists that medium. The absent strain-level `medium_count` faithfully reflects raw BacDive count zero, not a claim that the strain cannot be cultured. Full upstream Madin/BactoTraits KGX edges were unavailable: an ignored-independent `find` of the configured kg-microbe `data` tree found no `edges.tsv`. Those counts were verified against committed inventories, not independently reconstructed phenotypes.

## Completeness

The ignored-inclusive source search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It covered the bounded taxon number, old/current species names and all three deposits plus R-46060. All 113 matching rows were read in full using structured compressed JSON/TSV readers. The expanded exact-token search covered merged IDs, all markers, sample, run, analysis, assembly, IMG, GOLD and additional strain aliases. Its 72 hits were already-read rows. An initial loose B1199 substring search also hit unrelated identifiers/hashes; those were not treated as identity evidence. All five source metadata JSON files were parsed separately, and filename/history inventories included ignored files.

StrainInfo SI-ID 388204 (`data/straininfo/records.jsonl.gz:291808`) identifies non-type LMG 26380, deposit 886374, with HE565554. It is cataloged but does not share the listed strain's exact deposit. Fresh [HE565554.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/HE565554.1) confirms LMG 26380 and the same species, without a type qualifier. Its 1441-base 16S sequence is byte-identical to FR774993.1 after case normalization, illustrating why marker identity alone cannot merge the strains. Under `docs/SOURCE_COVERAGE.md`, independent source discovery is not a requirement to mint another BacDive-backed strain entry. SeqCode name 3960 (`data/seqcode/names.jsonl.gz:3712`) likewise remains catalog discovery, not an automatically asserted equivalence.

All supported listed-strain links are present; no listing cap hides further inventoried BacDive strains. There is no missing required causal graph, trait definition, mechanistic evidence or literature narrative. The marker and catalog evidence above does not authorize inventing those optional slots. Searches establish bounded local completeness, not universal database completeness.

## Findings

None found in the record's current claims.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

No corrective edit is required. Preserve current nomenclature, source-qualified historical labels, per-deposit evidence, accession versions and `SEEDED` status.

Optional future enrichment of LMG 26380 must start from its own StrainInfo deposit and evidence, not merge it into BacDive 1791. Such work belongs in maintained extraction/overlay support (`src/taxonmech/straininfo_links.py`, the source inventory machinery and `src/taxonmech/seed.py`), with focused tests and regenerated output after separate authorization. No direct YAML patch is recommended.

## Follow-up Checks

If source refresh or enrichment is authorized later, recheck LPSN 70769/790217, each own culture deposit, the explicit GenBank/RefSeq pair, the GOLD project chain, and ATB's sample-specific reassembly provenance. Preserve the distinct LMG 26380 record. Resolve the host-source conflict below before adding an isolation claim. Then run both focused validators, an inspected generator canary, `just verify-corpus` and `just qc`. A live GTDB recheck and upstream KGX trait-edge reconstruction would close the specifically stated verification limits; no present corpus-wide success is claimed.

## Additional Notes

An external conflict is deliberately retained: the inspected DSM 26656 catalog says the isolation host was Lupinus polyphyllus, while BacDive's summary and the exact type-strain GenBank source features say Lathyrus latifolius. The current YAML asserts neither host, so this is not a defect in its claims. Root-nodule isolation also does not establish nodulation or nitrogen fixation; the original description reports negative nodA/nodC amplification and nonspecific nifH products. ENA's generic `clinical isolate assembly` label is likewise not imported as a clinical-origin claim.

GTDB pages returned access errors; StrainInfo's human page required JavaScript, but its complete pinned native record and DataCite DOI metadata were read. PMC returned a browser challenge; publisher abstracts, PubMed metadata and LPSN provided the nomenclatural support actually used. The notification list's bibliographic identity was verified, not its full article table. Initial ENA requests used an unsuitable JSON Accept header and returned 406; XML-header retries succeeded. Initial shell network attempts failed under the sandbox and succeeded with approved read-only network access. The configured `data/source_snapshots` directory was unavailable; committed native assembly catalog rows were inspected, not the original multi-gigabyte source dumps.

Record SHA-256 before and after checks: `1e396ee61b0648e5644dff9b9c5fca0ef5713db912c353e7a883c20685b1690d`. HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The embedded 2026-09-13T17:54:04Z event agrees with the inspected seeder's newest-input timestamp rule and ATB manifest. Its action, curator, eight-source list and scope text are consistent with seeding, not human sign-off.

Only this new report was written for this target. No YAML, source, scope, history, generated page, status, branch, worktree or GitHub state was changed. The completed Eukaryota review remained untouched.
