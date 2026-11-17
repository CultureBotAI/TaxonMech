# YAML Record Review: Saccharothrix syringae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/saccharothrix_syringae.yaml`
- Started UTC: 2026-10-09T23:51:27Z
- Finished UTC: 2026-10-09T23:57:42Z
- Verdict: pass

## Target

Entire 1,426-line generated `TaxonRecord` read, including all nested evidence. `NCBITaxon:103733` denotes Saccharothrix syringae, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2071`, genetic code 11, grounding `EXACT`, status `SEEDED`.

The record contains nine ancestors, source-qualified synonyms, LPSN nomenclature, a GTDB mapping, eight source attestations and one BacDive type-strain entry with 12 culture identifiers. Its 18 assembly, 12 genome and 69 related-record assertions total 99 source-qualified assertions, not 99 independent biological entities. The seed event was also inspected.

## Validation

Repository commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/saccharothrix_syringae.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/saccharothrix_syringae.yaml --out /private/tmp/taxonmech-saccharothrix-syringae-20261009-validation.tsv --workers 1`: one file, zero errors. The output was reread and contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Bounded structured comparisons matched the complete pinned lineage, scope/index entries, seed text, source counts and the exact multiset of all 99 assertions, with no missing or extra own-strain inventory entries. Retained culture joins satisfy the maintained whole-deposit CAFI matcher. These comparisons are not full-corpus reproduction or independent native-source verification.
- Native BacDive, StrainInfo, BV-BRC, NCBI assembly, GTDB and GOLD material rows were independently read in full. Live NCBI taxonomy, assembly/sample metadata, BioProjects, marker metadata, DataCite and retrieved LPSN pages were checked separately.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering or publication gates. `just validate-products` has no applicable causal-graph nodes.
- The public GTDB tree request failed. Direct access to the 1989 publisher article returned HTTP 403; its DOI bibliography was verified through publisher-deposited Crossref metadata and LPSN, not a retrieved full experimental paper. The 1990 validation-list bibliography and references were inspected, but its complete species table was not retrieved. Assembly metadata verification did not compare genome sequence payloads.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18559` agrees with inspected [NCBI taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103733) and [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103733&retmode=xml): species Saccharothrix syringae, parent Saccharothrix and code 11. The root-first chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Pseudonocardiales, Pseudonocardiaceae and Saccharothrix. A complete pinned backbone scan found no immediate child; exact own-ID scans found no merge/drop row.

The pinned NCBI name rows support the bare Nocardiopsis syringae exact synonym and three authority-bearing related strings. The Gause/Gauze variation is source-supplied and is not silently corrected. Live NCBI additionally classifies Actinosynnema syringae as a misspelling; the YAML's occurrence is explicitly GTDB-derived, not attributed to the pinned NCBI name inventory.

`data/raw/lpsn_names.tsv:19712` and the [LPSN species authority](https://lpsn.dsmz.de/species/saccharothrix-syringae) support name 780711, valid/correct-name status, the 1990 combination, the 2018 emendation, AF114812 and the six stored type deposits: ATCC 51364, DSM 43886, IFO 14523, JCM 6844, NBRC 14523 and NRRL B-16468. The authority also lists INA 2240 and VKM Ac-1858; both already occur in the nested strain inventory. The medical-use wording concerns which name to use, not clinical efficacy or safety.

The [Nocardiopsis syringae authority](https://lpsn.dsmz.de/species/nocardiopsis-syringae), name 778879, explicitly resolves to Saccharothrix syringae as its current name and identifies the homotypic relationship. It also explains why the nomenclatural authors differ from the original publication authors. Its separate historical genus does not replace the record's current lineage.

`data/raw/gtdb_mappings.tsv:1482` and `data/raw/gtdb_species.tsv:5111` support `GTDB:s__Actinosynnema_syringae`, `skos:closeMatch`, count two. Both full native GTDB rows retain NCBI species 103733 and NRRL B-16468 while classifying them under Actinosynnema and Mycobacteriales in GTDB. The complete assembly is representative; the older draft is not. This is a preserved source-classification difference, not an exact-equivalence claim or a reason to replace the NCBI lineage.

## Evidence

The eight attestations retain their own count units:

| Source | Count and unit | Inspected support |
| --- | --- | --- |
| NCBITAXON | 1 NAME | Own backbone and name rows, snapshot 2026-09-13 |
| LPSN | 1 NAME | Name 780711 and nomenclature row 19712 |
| GTDB | 2 GENOME | Species/mapping rows and both native genomes |
| BACDIVE | 1 STRAIN | Raw strain row 13316 and native BacDive 13480 |
| MEDIADIVE | 2 MEDIUM | Own row 142, medium IDs 65 and J58 |
| GOLD | 8 ORGANISM | Own row 524 and eight native organism rows |
| MADIN | 1 TRAIT_ASSERTION | Own row 709 |
| BACTOTRAITS | 4 TRAIT_ASSERTION | Own row 106 |

These are source inventory counts, not independently curated growth or phenotype claims. The BacDive strain row has medium count zero; omission of a strain-level count is consistent with that input and does not contradict the separate taxon-level MediaDive attestation.

Full `data/bacdive/records.jsonl.gz:13315` and the [BacDive authority](https://bacdive.dsmz.de/strain/13480) support the type strain and culture identifiers. Its own literature list contains ATCC 51364, BCRC 16262, CGMCC 4.1716, DSM 43886, IFO 14523, IMET 9675, INA 2240, JCM 6844, KCTC 9398, NBRC 14523, NRRL B-16468 and VKM Ac-1858. Its sequence block explicitly links the two assemblies, IMG accessions and BV-BRC genome identifiers below. Internal BacDive reference 67770 remains local source provenance, not a PMID.

Two distinct sequencing chains refer to the same NRRL deposit:

| Chain | Draft | Complete |
| --- | --- | --- |
| GenBank / RefSeq | GCA_000716755.1 / GCF_000716755.1 | GCA_009498035.1 / GCF_009498035.1 |
| Assembly | ASM71675v1, Contig | ASM949803v1, Complete Genome |
| BioSample | SAMN02645315 | SAMN10600592 |
| Sequencing BioProject | PRJNA238534 | PRJNA510219 |
| BV-BRC | 103733.3 | 103733.7 |
| IMG | 2751185736 | 8066685052 |
| GOLD analysis / project | Ga0163380 / Gp0188076 | Ga0486336 / Gp0546421 |
| GOLD organism | Go0353819 | Go0353819 |

Four native NCBI assembly rows, both native GTDB rows, both BV-BRC rows and both GOLD analysis/project chains agree on these relationships. Live [draft assembly metadata](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000716755.1/) and [complete assembly metadata](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_009498035.1/) confirm the identity, paired RefSeq accessions, samples and release histories. The sample aliases P068 and nocamycin producing strain are source annotations, not independently established experimental conclusions.

The inspected [BioProject XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=238534,510219,224116&retmode=xml) distinguishes PRJNA238534, a multispecies actinomycete sequencing project, from PRJNA510219, the NRRL B-16468 isolate sequencing project. PRJNA224116 is the RefSeq annotation umbrella, appropriately retained where the RefSeq/GTDB source supplies it. It is not an additional isolate or the original sequencing project.

Full GOLD organisms comprise Go0028569 for DSM 43886, Go0353819 for NRRL B-16468, and Go0605692 through Go0605697 for ATCC 51364, IFO 14523, IMET 9675, INA 2240, JCM 6844 and NBRC 14523 respectively. Historical Nocardiopsis names retain taxon 103733. Seven eligible culture identifiers yield organism links from two source fields each. Direct execution of `normalize_culture_identifier` returns an empty key for INA 2240, so Go0605695 contributes to the organism count but not a fabricated whole-deposit join. The YAML preserves INA 2240 as its source-supplied escaped culture identifier.

Full StrainInfo native row `data/straininfo/records.jsonl.gz:31147` identifies SI-ID 42951 and BacDive 13480. All 13 deposits were read. Eleven exact eligible own deposits support the YAML's deposit/strain links: ATCC/115549, DSM/115550, IFO/115551, IMET/115552, JCM/115554, NRRL/182464, VKM/227899, KCTC/319697, NBRC/335201, BCRC/512036 and CGMCC/753426, with the full designations listed above. AS 4.1716/319698 and CCRC 16262/512037 are additional historical deposit identifiers, not aliases the matcher may rewrite into CGMCC or BCRC. INA 2240 is a designation in the relationship block, not an own deposit object.

All three StrainInfo sequence objects explicitly name NRRL B-16468 and the same SI-DP 182464. Thus the two assembly assertions and AF114812 sequence assertion have same-deposit evidence, not merely a shared species name or BacDive cross-reference. The [DataCite metadata for SI-ID42951.3](https://api.datacite.org/dois/10.60712/si-id42951.3) confirms the findable version-three strain DOI and 13-deposit description; the DOI alone is not sequence-binding proof. BacDive/StrainInfo unversioned assembly identifiers remain unversioned.

The final assertion split is 18 assemblies (BacDive 2, BV-BRC 2, GOLD 4, GTDB 4, NCBI 4, StrainInfo 2), 12 genome records (BacDive 4, BV-BRC 2, GOLD 4, GTDB 2), and 69 related records (BV-BRC 4, GOLD 30, GTDB 4, NCBI 8, StrainInfo 23). Distinct GOLD fields and distinct source witnesses are intentionally retained.

The [1989 DOI's registered bibliography](https://api.crossref.org/works/10.1016%2Fs0723-2020%2889%2980073-6) confirms Grund and Kroppenstedt, Systematic and Applied Microbiology 12(3):267-274, for the five-species transfer. The [1990 publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-40-3-320?crawler=true) identifies Validation List 34 and cites that transfer paper. LPSN explicitly connects both publications to this combination. Effective publication in 1989 and nomenclatural validation in 1990 are not conflicting dates.

The inspected target emendation in [Nouioui et al. 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6113628/) specifies SAMN02645315, approximately 10.88 Mbp and 73.5% G+C. It supports the older draft chain, not the later complete assembly. No new genome-size or phenotype assertion was added to the YAML.

Live [AF114812 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AF114812) resolves to AF114812.1, a 1,510-base partial 16S sequence, explicitly NRRL B-16468T and taxon 103733. Its bibliography matches [PMID 10826820](https://pubmed.ncbi.nlm.nih.gov/10826820/), DOI 10.1099/00207713-50-1-331. This historical phylogenetic paper is marker evidence, not authority to replace the current lineage. The separately inspected [complete-genome study abstract](https://pubmed.ncbi.nlm.nih.gov/33136202/), DOI 10.1007/s00284-020-02272-0, describes the same NRRL strain and complete chromosome; predicted biosynthetic clusters are not promoted into experimentally verified mechanisms or species-wide phenotypes.

## Completeness

An ignored-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It used the target names, bounded numeric source IDs, full culture identifiers, marker, assembly numbers, BioSamples and GOLD identifiers. It returned 411 candidate lines: 162 native JSON and 249 TSV rows. Native candidate identities and matched-field contexts were inspected, and material own native rows were read completely. TSV evidence was inspected with structured lossless projections; truncated output was reread in smaller groups.

Numeric collisions include DSM 103733 in Silvibacterium bohemicum, CIP 103733 in Klebsiella, BacDive 103733 in Rhodococcus, unrelated SI-ID/SI-DP values, GTDB assembly statistics and sequence identifiers containing the same digits. The ATB candidate links belong to Silvibacterium's SAMN14908528, not either target BioSample. No own ATB assertion was found in the searched native catalog or join inventories. This is bounded source coverage, not proof that no assembly exists elsewhere. No Eukaryota YAML was opened.

Raw BacDive rows 29514-29516 contain LPSN 780711 but explicitly assign their strains to NCBITaxon 316335, with different HKI/VTT deposits. `src/taxonmech/seed.py:247` indexes these strain rows by their explicit taxon IDs. A shared LPSN field alone cannot move them into this record or demonstrate an omitted own strain. This discordant source context is preserved rather than silently resolved.

Five SOURCE.json files were parsed separately. Gitignore-independent filename checks found this target YAML and no previous target report; history filename checks found no target-specific filename. Native SeqCode name entries 18463, 28720 and 42772 support name-catalog identities only, not additional genome or strain evidence.

iModulonDB gene/module searches were not applicable: this seeded record makes no gene, regulator, pathway or transcriptomics claim. No dataset absence is asserted, and the adapter was not run for this target. Optional definition, functional traits, record-level evidence and causal graph need not be populated from source counts or project descriptions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and source scope. The GTDB classification difference, historical nomenclature, multiple sequencing studies, source-specific duplicate witnesses and excluded unsupported deposit joins are represented consistently. Unretrieved public pages and skipped full-corpus checks remain limitations, not successful validations.

## Recommended Edits

None required. Do not hand-edit the generated YAML, rewrite historical culture acronyms, invent a CAFI match for INA 2240, merge the two sequencing studies, replace the NCBI lineage with GTDB, or upgrade unversioned source accessions without source evidence.

Future authorized source corrections belong in the maintained extraction inputs/policies, including `src/taxonmech/extract.py`, `src/taxonmech/genome_sources.py`, the source-specific adapters and `src/taxonmech/straininfo.py`, followed by the documented extraction and seed workflow. No such correction is established by this review.

## Follow-up Checks

Retry the public GTDB tree and retrieve the original transfer paper/complete Validation List 34 table when accessible. These follow-ups would strengthen independent public-source coverage without changing the currently supported identity.

Any future source refresh should repeat whole-deposit joins, same-SI-DP sequence checks, schema/strict/history validation and the documented full-corpus reproduction and QC gates. Preserve the different sequencing and annotation-project roles. A future biological trait claim would require claim-specific primary evidence, not the present attestation counts.

## Additional Notes

- YAML SHA-256: `95280b7e4633e2de9da9f9ee37aab14ce3b1c4c9e88128cc8eda81ddcf16dba8`, unchanged on reread.
- `data/taxa/PATHS.tsv:15259` and `curation/seed_scope.tsv:604` uniquely identify the target. The seed retains 2026-09-13T17:54:04Z and the eight-source scope reason. Seventeen NCBI type-material rows, 2072-2088, were inspected.
- Own raw assertion rows are assembly 36457-36472, genome 28474-28485 and related 98006-98051; StrainInfo contributes assembly 2758-2759, related 42484-42506 and strain links 17195-17205.
- Native material addresses include BacDive 13315, StrainInfo 31147, BV-BRC 3433-3434; NCBI GenBank shards 0000:26433 and 0008:18917; RefSeq shards 0000:22984 and 0002:33796; GTDB shards 0008:26050 and 0002:12612. GOLD organism rows are 24293, 263166 and 436685-436690; analyses 104171 and 313750; projects 122119 and 400200.
- Read-only review against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The only new repository artifact is this report. Records, maintained inputs, schemas, history, pages, branches, all ten existing worktrees and GitHub state were preserved. No curation event or status promotion was performed; Eukaryota coverage remains untouched.
