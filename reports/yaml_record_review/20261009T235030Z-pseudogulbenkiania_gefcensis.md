# YAML Record Review: Pseudogulbenkiania gefcensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudogulbenkiania_gefcensis.yaml`
- Started UTC: 2026-10-09T23:45:14Z
- Finished UTC: 2026-10-09T23:50:30Z
- Verdict: pass

## Target

Entire 134-line generated `TaxonRecord` read. `NCBITaxon:1037320` denotes Pseudogulbenkiania gefcensis, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:568394`, genetic code 11, grounding `EXACT`, status `SEEDED`. All nine ancestors, nomenclature, two related synonyms, one xref, one type-strain entry, five source attestations and the seed event were inspected.

The strain is BacDive 133838, designation yH16, with JCM 17850 and KCCM 90100. Its two GOLD related-record assertions preserve two source fields for one organism identifier; they are not two strains or genomes. No genome assembly or genome-record assertion is present.

## Validation

Repository commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudogulbenkiania_gefcensis.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/pseudogulbenkiania_gefcensis.yaml --out /private/tmp/taxonmech-pseudogulbenkiania-gefcensis-20261009-validation.tsv --workers 1`: one file, zero errors. The TSV was reread and contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Bounded structured comparisons matched the complete pinned lineage, own count rows, scope/index entries, seed text and both GOLD assertions. Raw, StrainInfo and ATB inventories supply no additional own-strain assembly/genome/related links. Both retained GOLD fields pass the maintained CAFI whole-deposit match. These comparisons are not full corpus reproduction or independent native-source validation.
- Native BacDive and GOLD rows were independently read in full. NCBI taxonomy and sequence metadata, LPSN, JCM, BacDive and publication metadata were checked at their public authorities.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. `just validate-products` has no applicable graph nodes.
- Live GOLD page access and the notification-list full-text endpoint returned HTTP 403. The primary species paper was checked through its publisher abstract and PubMed metadata, not its full experimental text. The original MediaDive KGX file was unavailable at the configured checkout path, so its upstream edge was not replayed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222714` agrees with inspected [NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037320) and [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037320&retmode=xml): species Pseudogulbenkiania gefcensis, parent 568394 and code 11. The complete pinned chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Neisseriales, Chromobacteriaceae and Pseudogulbenkiania. A complete backbone scan found no immediate child; exact-ID scans found no own merge/drop row.

Native NCBI name rows `data/catalog/ncbi_names-0005.jsonl.gz:32320`, `:32321` and `:32322` support the scientific name, authority name and included designation Pseudogulbenkiania sp. yH16. The latter two correctly remain related rather than exact synonyms. Live NCBI additionally returns the misspelling Pseudogulbenkiania geefcense, absent from these pinned name rows. This is an observed live-versus-snapshot difference, not evidence for changing the species identity or silently altering its generated synonyms.

`data/raw/lpsn_names.tsv:27406` and the [LPSN species page](https://lpsn.dsmz.de/species/pseudogulbenkiania-gefcensis) support name 790450, authority Lee et al. 2013, legitimate/validly published/correct-name status, JCM 17850, JF728876 and the two cited publications. The current authority also lists KCCM 90100 and yH16. The generated nomenclature faithfully retains its pinned single-deposit input, while the strain entry already preserves KCCM 90100 and the yH16 designation. There is no conflicting type-strain identity.

The [JCM 17850 catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=17850) independently confirms the type strain, its receipt from D.-G. Lee as yH16, equivalence to KCCM 90100, the BacDive and NCBI identifiers and JF728876. JCM's medium recommendation is strain-specific, not a species-wide growth assertion.

No GTDB species mapping or GTDB attestation is supplied by the exact own-taxon inventory. Numeric GTDB catalog hits inspected below are unrelated; a GTDB species link must not be inferred from genus membership.

## Evidence

The five source attestations retain distinct units:

| Source | Count and unit | Inspected support |
| --- | --- | --- |
| NCBITAXON | 1 NAME | Own backbone row, snapshot 2026-09-13 |
| LPSN | 1 NAME, closeMatch | Name 790450 and native nomenclature row |
| BACDIVE | 1 STRAIN | Raw strain row 56148 and native BacDive 133838 |
| GOLD | 1 ORGANISM | Own count row 523 and native organism Go0044582 |
| MADIN | 20 TRAIT_ASSERTION | Own count row `data/raw/madin_taxa.tsv:708` |

Counts are upstream source attestations, not independent biological entities or a set of newly curated phenotype claims.

Complete native `data/bacdive/records.jsonl.gz:56147` and the public [BacDive record](https://bacdive.dsmz.de/strain/133838) agree on the classification, yH16 designation, JCM/KCCM deposits, type flag and 16S accession. The native record contains no genome sequence block. The strain's `medium_count: 1` exactly matches `data/raw/bacdive_strains.tsv:56148`. `src/taxonmech/extract.py:388` counts strain-directed MediaDive edges separately from taxon-directed edges, so a strain medium count can legitimately coexist with no species-level MEDIADIVE attestation. The corresponding original KGX edge was not available for independent replay; no particular MediaDive medium ID is inferred from the count.

Complete `data/gold/organisms.jsonl.gz:37390` identifies Go0044582 as Pseudogulbenkiania gefcensis JCM 17850, taxon 1037320, with JCM 17850 in both organism-strain and culture-collection fields. Raw related-record rows 87645 and 87646 preserve those two explicit fields and the same whole matched deposit. Neither source row claims an assembly, sample, sequencing project or IMG genome. The exact organism ID search across the native GOLD projects and analyses found no referring project/analysis row; unsupported genome or project links should not be invented. The native primary-source projection supports the identity despite live GOLD page access being unavailable.

The [original species paper](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.040873-0), DOI 10.1099/ijs.0.040873-0, and [PMID 22389280](https://pubmed.ncbi.nlm.nih.gov/22389280/) identify the same Lee et al. article, IJSEM 63:187-191, January 2013. Its inspected abstract explicitly designates yH16, KCCM 90100 and JCM 17850 as the type-strain equivalents. Its comparison with Pseudogulbenkiania subflava is taxonomic evidence, not an assertion that the species are equivalent. Earlier online/text-mining dates do not contradict the 2013 nomenclatural authority.

DOI 10.1099/ijs.0.051581-0 resolves to the [April 2013 notification list](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.051581-0) for names in volume 63, part 1. Its bibliography and abstract were inspected, and LPSN explicitly links that notification to this name. The full target row in the publisher table was not retrievable. A notification list is not treated as a second experimental characterization.

Live [JF728876 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF728876) resolves to JF728876.1, a 1,460-base partial 16S rRNA sequence. The source feature explicitly names yH16, taxon 1037320 and the type strain of Pseudogulbenkiania gefcensis; its reference cites the same DOI and PMID. This supports the nomenclatural marker, not a genome assembly. The source-supplied unversioned INSDC accession remains unversioned.

## Completeness

An initial ignored-inclusive compressed search across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history` used the label, slug, source IDs, full culture IDs, marker and publications. It returned 558 broad candidate lines, including shared notification citations and numeric substrings. That number is not a count of relevant source records.

A second `rg --no-ignore --hidden -n -z -i` search used whole numeric IDs, whole culture accessions, yH16, the exact marker, GOLD ID and BacDive's SI-ID 132819 cross-reference. Its 38 candidates comprised 23 TSV rows, all read completely, and 15 JSON rows whose identities and matching fields were inspected. Material own-source native rows were read fully. An additional ignored-inclusive compressed search for gefcensis, geefcense, both culture IDs, yH16 and Go0044582 across catalog, StrainInfo, ATB and GOLD found only the already inspected own GOLD organism and NCBI name rows. No own assembly or deposit evidence appeared within that bounded source scope.

False hits include NCBITaxon 133838, an unrelated uncultured bacterium; BacDive 132819, a Rhodobacter strain; SI-DP 790450, a fungal deposit; CBS 132819 in a different StrainInfo record; three unrelated GTDB assembly statistics; and Salmonella strain 790450. These numbers do not share identity across namespaces. No Eukaryota YAML was opened.

BacDive's native `Literature.straininfo link` points to SI-ID 132819. The ignored-inclusive native catalog search found no rich StrainInfo record with that own ID or the target's exact deposits. The documented [public rich-record endpoint](https://api.straininfo.dsmz.de/v2/data/strain/max/132819) returned HTTP 404 on three attempts, while a control request for known SI-ID 39578 resolved through the same route. The public target HTML shell supplied no record detail. This establishes an unavailable target response, not that the historical source ID never existed. BacDive cross-references alone cannot supply eligible own-deposit or sequence evidence under `docs/STRAININFO.md`. Since the YAML does not assert this unresolved reference, it is not a broken record-level link.

The [NCBI Assembly query for taxon 1037320](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=assembly&term=txid1037320%5BOrganism%3Aexp%5D&retmode=json) returned zero indexed results and a phrase-not-found warning. Together with the local source checks, this found no supported assembly to add; it does not prove that no genome exists elsewhere. ATB has no eligible own BioSample evidence to join, and no sample is inferred from a taxon or strain name.

All five local SOURCE.json metadata files were separately parsed. A gitignore-independent target filename inventory found the target YAML and no prior target report. The ignored-independent history filename inventory found no target-specific history filename. SeqCode name 16799 was read as a catalog name entry, not a strain or genome evidence object.

The local `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets` adapter ran with bytecode writes disabled. All 28 rows were inspected; none covered Pseudogulbenkiania. Gene/module searches were therefore inapplicable. Dataset absence is not negative biological evidence.

Optional definition, functional traits, record-level evidence and causal graph may remain empty. The source-attestation counts and marker sequence do not require invention of a mechanism.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and source scope. The missing genome and StrainInfo assertions are not demonstrable omissions of eligible evidence. The unresolved external BacDive-to-StrainInfo cross-reference and inaccessible publisher/GOLD pages are recorded as limitations, not silently treated as successful verification.

## Recommended Edits

None required. Do not hand-edit this generated YAML, infer genomes from marker sequences or names, add an unverified StrainInfo link, or collapse the two GOLD field assertions. A future source refresh may capture additional nomenclatural spellings or source records, but that is not authorized by this read-only review.

## Follow-up Checks

Retry the GOLD page, notification-list table and SI-ID 132819 endpoint when available. Any future StrainInfo import must demonstrate an eligible own JCM 17850 or KCCM 90100 deposit and, for sequences, an explicit same-deposit binding. A source cross-reference or matching species name alone is insufficient.

When the configured upstream KGX snapshot is available, its MediaDive edge can independently verify the strain count. Future authorized input or source-policy changes should follow the documented extraction/seed workflow and repeat schema, strict, history, corpus reproduction and QC gates. No status promotion or curation event was performed.

## Additional Notes

- YAML SHA-256: `599d6f0788515b41d12f6b67a7d39dcc8af5b0712ef3a316804a0a2aec91b779`, unchanged on reread.
- `data/taxa/PATHS.tsv:15258` and `curation/seed_scope.tsv:14833` uniquely identify the target. The seed event exactly retains 2026-09-13T17:54:04Z and its five-source scope reason.
- Original-source replay was not performed. The configured MediaDive file and local StrainInfo snapshot directory were unavailable at their configured paths. A broader sibling-directory inventory encountered permission-denied paths and is not used to claim that no other copy exists.
- Read-only review against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The sole new repository artifact is this report; records, maintained inputs, schemas, history, pages, branches, all ten existing worktrees and GitHub state were preserved. Eukaryota coverage remains untouched.
