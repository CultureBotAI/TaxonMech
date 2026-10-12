# YAML Record Review: Actinomyces urogenitalis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/actinomyces_urogenitalis.yaml`
- Started UTC: 2026-10-08T03:30:21Z
- Finished UTC: 2026-10-08T03:48:30Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:103621`, Actinomyces urogenitalis, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:1654` (Actinomyces), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 1,309 YAML lines were read before judgement, including all eleven strain blocks and their complete nested provenance.

`data/taxa/PATHS.tsv:14816`, `curation/seed_scope.tsv:8538`, and `curation/legacy_page_paths.tsv:891` resolve the same species. The scope row was added on 2026-09-12 under the six-source attested rule; the embedded seed event is dated `2026-09-13T17:54:04Z`. The species record is distinct from its three named NCBI strain descendants; those records were not assigned review verdicts here.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/actinomyces_urogenitalis.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/actinomyces_urogenitalis.yaml --out /private/tmp/aurogen-strict.tsv` | Pass; one file, zero errors; output TSV contains only its header. |
| Structured identity and lineage comparison | Full backbone row, all nine ancestors, rank, parent, domain, genetic code, synonyms, nomenclature, mapping, and source attestations agree with the pinned inventories. |
| Full pinned-subtree traversal | Exactly three descendants; eleven distinct BacDive strains, ten filed directly and one under DSM 15434. The entire listing is present. |
| Per-strain assertion comparison | All fields agree for all eleven strains: 10 assembly assertions, 7 genome-record assertions, and 66 related-record assertions. No missing or extra assertion was found against the raw inventories plus eligible StrainInfo and ATB overlays. |
| Native source checks | All 410 candidate rows/objects from the bounded ignored-inclusive source search were read. Structured common-field compression was lossless; BacDive objects were covered by all four native sections. |
| GTDB count diagnostic | 25 distinct genomes in the exact GTDB species; representative `RS_GCF_000159035.1`. Twenty-four have NCBI species 103621 and one has NCBI species 249061. |
| Live authority and citation checks | NCBI species and type-strain taxonomy, assembly, BioSample, both BioProjects, LPSN, BacDive, type catalogs, original-description abstract, exact emendation passage, notification metadata, marker metadata, and all eleven versioned StrainInfo DOIs inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. The bounded comparisons are diagnostics, not replacements for corpus or component reproduction. There is no documented focused reference validator for this record. `just validate-products` addresses curator-added causal-node labels and is not applicable to this graph-free record. No target-specific separate history artifact was found in the ignored-inclusive searches; the embedded seed event was checked directly. No history event or review-status promotion was made.

## Identity and Grounding

The full backbone row `data/raw/ncbitaxon_taxa.tsv:18521` agrees with live NCBI Taxonomy XML and Datasets on species 103621, the label, parent 1654, and genetic code 11. The root-first lineage is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Actinomycetales, Actinomycetaceae, and Actinomyces. All ancestor identifiers, labels, and ranks match the pinned parent chain. Datasets includes root; the XML lineage begins with cellular organisms. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103621&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103621).

The three descendants are DSM 15434 (`NCBITaxon:525246`), S6-C4 (`NCBITaxon:1284679`), and DORA_12 (`NCBITaxon:1403939`). Full traversal found no additional descendants in the pinned backbone. Current Datasets confirms the same three children, and the type-strain endpoint confirms DSM 15434's strain rank and lineage through this species. The species is not interchangeable with any one isolate. [DSM 15434 taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/525246).

Native NCBI names preserve three `includes` entries for CCUG 28744, CCUG 38702, and CCUG 42029 plus the emended authority. Their placement as related synonyms is appropriate. The merged-ID inventory maps old IDs 100471, 100472, and 99917 into 103621, not the reverse; none of the four current subtree IDs is dropped or retired. The six type-material rows are space/colon variants of CCUG 38702, CIP 106421, and DSM 15434.

## Evidence

**Nomenclature and publications.** `data/raw/lpsn_names.tsv:15012` supplies `lpsn:772811`, valid and legitimate publication, correct-name status, authority, four type designations, two DOIs, PMID 10939672, and AJ243791. Current LPSN agrees on the name, nomenclatural standing, four type designations, marker, original description, notification, and 2018 emendation. The source's medical-use wording is nomenclatural status, not a clinical recommendation. [LPSN species record](https://lpsn.dsmz.de/species/actinomyces-urogenitalis).

- PMID 10939672 resolves to Nikolaitchouk and colleagues' 2000 description and DOI `10.1099/00207713-50-4-1649`. Its inspected abstract describes three isolates and identifies CCUG 38702 and CIP 106421 as the type strain. Full original-paper text was not inspected. [Original description](https://pubmed.ncbi.nlm.nih.gov/10939672/).
- DOI `10.1099/00207713-50-5-1701` resolves at the publisher to the September 2000 notification for names appearing in volume 50, part 4. This matches the LPSN bibliography; the publisher page has no abstract and did not expose the complete list as text. The individual list entry was not independently read. [Notification](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-50-5-1701).
- PMID 30186281 and DOI `10.3389/fmicb.2018.02007` identify Nouioui and colleagues' emendation paper. The exact publisher passage for A. urogenitalis adds type-genome information and explicitly identifies SAMN00002545. This supports the emended authority without requiring an invented phenotype or causal graph. [Primary emendation](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2018.02007/full).
- Complete source and reference metadata for AJ243791.1 identifies a 1,423-bp 16S rRNA sequence, taxon 103621, and the original PMID. It is a nomenclatural marker, not a genome assembly. [Sequence record](https://www.ncbi.nlm.nih.gov/nuccore/AJ243791.1).

**Type identity and assembly.** The native BacDive 178 object and current page agree on DSM 15434, CCUG 38702, CIP 106421, and the type flag. The DSMZ and CCUG catalogs independently connect these deposits; CCUG also links NCTC 14285, whose own catalog identifies it as this species' type strain. The BacDive-owned culture inventory remains three deposits, while the LPSN-owned nomenclature list correctly contains four. These different source surfaces should not be silently homogenized. [BacDive 178](https://bacdive.dsmz.de/strain/178), [DSMZ catalog](https://www.dsmz.de/collection/catalogue/details/culture/DSM-15434), [CCUG catalog](https://www.ccug.se/strain?id=38702), [NCTC catalog](https://www.culturecollections.org.uk/nop/product/actinomyces-urogenitalis).

The current NCBI assembly report confirms scaffold assembly GCA_000159035.1, paired current GCF_000159035.1, DSM 15434, taxon 525246, SAMN00002545, and PRJNA31429. BioSample explicitly names DSM:15434 and type material. PRJNA31429 is the strain's Human Microbiome Project reference-genome project; PRJNA224116 is a separate multispecies RefSeq annotation umbrella. Both are valid source-scoped related records, not two independent strain experiments. [Assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000159035.1/dataset_report), [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN00002545&retmode=xml), [Strain BioProject](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA31429), [RefSeq BioProject](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA224116).

The full pinned assembly summaries are `ncbi_genbank-0000.jsonl.gz:1666` and `ncbi_refseq-0000.jsonl.gz:1530`. The matching native GTDB object is `gtdb_genomes-0007.jsonl.gz:27849`; BV-BRC is `bvbrc-0021.jsonl.gz:30356`, genome 525246.3. GOLD analysis Ga0027364 links through its single project Gp0003592 to organism Go0003592 and DSM 15434, with IMG 643886015, the assembly, project, and sample. Its blank direct organism field is resolved by that explicit single-project relationship, not by a name guess.

The ten assembly assertions preserve three supplied identifier forms: unversioned GCA_000159035, versioned GCA_000159035.1, and GCF_000159035.1. The seven genome assertions retain three distinct identifiers: GTDB RS_GCF_000159035.1, IMG 643886015, and PATRIC 525246.3. Multiple assertions retain different sources or match fields; they are not ten or seven biological genomes. BacDive reference 66792 is explicitly automatic DiASPora annotation on the current source page, not a primary sequencing paper.

**All eleven strain blocks.** Native BacDive and StrainInfo objects support the following joins. Each imported StrainInfo deposit is the source record's own available deposit, in a published-online strain record, with the matching BacDive reference. The complete nested evidence, including field names, original identifiers, and taxon scope, matches the overlays.

| BacDive | Culture identifiers | StrainInfo version and matched deposit IDs | GOLD organism links |
| --- | --- | --- | --- |
| 178 | CCUG 38702; CIP 106421; DSM 15434 | 51192.3; 126788, 148398, 301784 | Go0216362; Go0216363; Go0003592 |
| 135407 | CIP 100478 | 67181.1; 148358 | Go0216359 |
| 136099 | CIP 102474 | 67169.1; 148346 | None in the eligible inventory |
| 137236 | CIP 103188; designation 723-82 | 68155.1; 150311 | Go0216483 |
| 137749 | CIP 100493; designation 820.83 | 68074.1; 150230 | Go0216366 |
| 145523 | CCUG 28744 | 51191.2; 126787 | Go0216365 |
| 150711 | CCUG 42029 | 87795.2; 278175 | Go0216484 |
| 151396 | CCUG 44038 | 109790.2; 329030 | Go0216486 |
| 151531 | CCUG 44229 | 118607.2; 355807 | Go0216488 |
| 152932 | CCUG 48051 | 118611.2; 355829 | Go0216490 |
| 156620 | CCUG 63604 | 410646.2; 918489 | None in the eligible inventory |

Each table version was independently retrieved from DataCite as `10.60712/SI-ID<version>` and confirmed as a findable A. urogenitalis dataset with the expected version, title, publisher, deposit count, and landing URL. The type record has four source deposits, but only three overlap the BacDive inventory. Its GCA_000159035 sequence explicitly belongs only to SI-DP301784, DSM 15434; it is not transferred to the other deposits. [Type-record DOI metadata](https://api.datacite.org/dois/10.60712/si-id51192.3).

The additional KCTC 5117 deposit in SI-ID51192 and the separate KCTC 5153 source record do not authorize new BacDive strains. NCTC 14285 and other relation-only designations likewise do not become imported StrainInfo deposits. The ten non-type strains have no eligible assembly or genome assertions in the inventories; their related-record links remain present. The total 66 related assertions comprise 40 raw-source assertions and 26 StrainInfo assertions.

**Mappings, attestations, and exclusions.** The GTDB `closeMatch` is supported by the LPSN link and exact mapping row 1457. `data/raw/gtdb_species.tsv:4850` and the 25 complete native target genomes reproduce its count. The one genome classified by NCBI as uncultured Actinomyces sp. remains a GTDB clustering difference, not an excuse to replace NCBI lineage or assert exact equivalence. The native GTDB representative is the type assembly; NCBI's reference-genome category for another isolate is a different designation.

| Attestation | Inventory support and scope |
| --- | --- |
| NCBITAXON: 1 NAME | Species backbone and scientific-name object; snapshot 2026-09-13. |
| LPSN: 1 NAME | One exact nomenclature row, lpsn:772811. |
| GTDB: 25 GENOME | Exact species mapping and 25 distinct native genome objects. |
| BACDIVE: 11 STRAIN | Ten direct strains plus BacDive 178 under descendant 525246; the note and `classified_as` preserve this distinction. |
| GOLD: 23 ORGANISM | `data/raw/gold_organisms.tsv:498`; 23 native organisms filed directly under 103621. Three additional native organisms belong to its strain descendants and are not added to this count. |
| MADIN: 7 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:689`, direct species scope. This is a source assertion count, not seven newly reviewed phenotypes. |

MediaDive's two media and BactoTraits' three assertions are filed under DSM 15434, not directly under the species. Their omission from species-level attestations follows the documented direct-only rule. Counts with different units are not summed.

The ATB catalog does contain the type-strain sample, but `data/atb/exclusions.tsv:1212` explicitly excludes it as `metadata_identity_flags:META_FAIL`. The full assembly row 1932 and catalog row 999310 agree on SAMN00002545, analysis ERZ9429932, SRR014456, and metadata flags. `src/taxonmech/atb_catalog.py:82` rejects identity-warning flags even when an assembly artifact exists. Thus zero ATB links is correct; the rejection neither invalidates the independently supported NCBI assembly nor licenses importing a flagged reassembly. Other ATB species-named samples do not establish a culture-deposit match.

## Completeness

No consequential gap was established under the current source-owned model. All eleven eligible BacDive strains are listed without a cap loss. Genome links remain on the type strain; unrelated isolate genomes, metagenomic bins, bare strain labels, marker sequences, and source grouping alone are not sufficient to populate the other strain blocks. Optional phenotype, experimental evidence, discussion, and causal-graph slots need not be invented. iModulonDB is not applicable because the YAML has no gene, regulator, transcriptomic, or causal claims.

Record resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`; no prior report or separate history artifact for this exact species was found. Compressed source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All five `SOURCE.json` files were separately parsed and history filenames independently inspected.

The 410 inspected candidates comprise 178 TSV rows, 82 NCBI catalog/name objects, 32 GTDB objects, 38 BV-BRC objects, 48 GOLD objects, 17 StrainInfo objects, 14 BacDive objects, and one SeqCode object. False numeric matches include BacDive ID 103621 for Rhodococcus, DSM 103621 for Rhizobium, CIP 103621 for Anaerococcus, and assembly/run/sample/length substrings. None was used as species evidence. SeqCode object 1398 is a name cross-reference, not a second nomenclatural authority required in this generated record. These searches establish bounded local coverage, not the absence of additional evidence anywhere online.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, nomenclature, related-synonym scope, mapped genome count, complete strain listing, deposit-specific genome provenance, direct-only attestations, and seeded history are supported within the inspected scope. Source-specific differences and intentional exclusions are preserved rather than treated as missing data or merged into equivalence.

## Recommended Edits

None required for this record. Do not hand-edit generated YAML, append an unearned review event, or weaken the ATB exclusion.

Any future source refresh belongs in maintained inputs and adapters: `conf/ncbi_taxdump.yaml`, `conf/ncbi_assemblies.yaml`, `conf/sources.yaml`, the upstream kg-microbe LPSN/GTDB transforms and `src/taxonmech/extract.py`, or the relevant genome, GOLD, StrainInfo, and ATB adapters. `conf/straininfo.yaml`, `src/taxonmech/straininfo_links.py`, `src/taxonmech/atb_catalog.py`, and `src/taxonmech/seed.py` own the overlay and materialization boundaries. Generated inventories, YAMLs, and pages are not independent correction surfaces. No such change is requested by this verdict.

## Follow-up Checks

- After an authorized input refresh, compare exact species 103621, all nine ancestors, three descendants, eleven BacDive identities, LPSN 772811, and the GTDB cluster before a one-record seed canary.
- Recheck complete assertion objects, not only accessions. Preserve unversioned versus versioned assemblies, source-specific match fields, and the DSM-specific SI-DP301784 sequence binding.
- Keep SAMN00002545 excluded from ATB linking unless refreshed pinned evidence resolves its metadata-identity flags; a passing taxonomic classifier alone is insufficient.
- Rerun schema and strict validation after authorized regeneration, then run corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation actually creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report target SHA-256: `586ffa57d3960ca609738621777acab39c04b468a040fd64cfe1085b362cbbd6`. No YAML, source, scope, lifecycle, or history change was made. Existing reports and all seven worktrees were preserved. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, GitHub mutation, or source refresh occurred.

GTDB's live genome page was unavailable; the full pinned native catalog supports its identifiers and count. The GOLD and StrainInfo landing pages did not expose usable record details through the web tool; native snapshots and, for StrainInfo, live DataCite metadata supplied the checks. IMG and BV-BRC links were checked in native source records and the current BacDive page, not independently through live IMG/BV-BRC APIs. The notification's metadata and LPSN association were verified, but its individual full-text list entry remains uninspected. These access limits are not evidence of a broken identifier.

The NCBI assembly's ANI block reports taxonomy status OK and explicitly explains that no same-species match is expected because this is the type-strain assembly. Its below-threshold match to another species was not misread as a supported reassignment. Sequence bases, genome quality, phenotype predictions, biosafety classifications, and clinical implications were not independently evaluated. The review verdict does not confer human `REVIEWED` status.
