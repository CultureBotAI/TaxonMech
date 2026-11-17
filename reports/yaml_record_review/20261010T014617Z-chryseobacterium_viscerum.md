# YAML Record Review: Chryseobacterium viscerum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chryseobacterium_viscerum.yaml`
- Started UTC: 2026-10-10T01:41:20Z
- Finished UTC: 2026-10-10T01:46:17Z
- Verdict: pass with minor issues

## Target

The complete 360-line generated `TaxonRecord` was read. `NCBITaxon:1037377` denotes Chryseobacterium viscerum, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:59732`, genetic code 11, grounding `EXACT`, status `SEEDED`.

It carries twelve ancestors, one LPSN nomenclature entry, two GTDB mappings, six related synonyms, three BacDive strains, six source attestations and one seed event. This review concerns that species record, not separate reviews of the other taxa encountered in source searches.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/chryseobacterium_viscerum.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/chryseobacterium_viscerum.yaml --out /private/tmp/taxonmech-viscerum-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified own identity, complete lineage, code, synonym source columns, index/scope entries and seed reason. The backbone has no direct child. Own-ID type-material, merged-ID and dropped inventories were inspected.
- Exact multiset comparisons for all three strains verified every stored assembly, genome record and related-record assertion against raw and StrainInfo inventories, including serialized provenance. Whole-deposit CAFI normalization checks passed. No own ATB strain link was present. This comparison uses the existing StrainInfo deserializer; independent native-row reads additionally verified deposit IDs, statuses, DOI versions and the absence of sequence lists in the three relevant native records.
- Complete native rows were read for the three BacDive records, three StrainInfo records, seven NCBI name rows, all six relevant GTDB genomes, four GOLD organisms, two relevant GOLD projects, three GOLD analyses, three target BV-BRC genomes and current/historical type-strain NCBI assembly pairs. All broad-search candidates had identity and matching fields inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. No causal graph is asserted, so `just validate-products` has no applicable nodes. Focused source agreement does not prove corpus reproduction.
- The configured upstream KGX GOLD, Madin and LPSN edge files were unavailable at their exact configured paths; committed inventories and extraction code were inspected instead. No claim is made that those files are absent from every external checkout.
- Live GTDB, BV-BRC, IMG, GOLD and the two non-type BacDive pages were unavailable through the web reader. Their pinned native projections were inspected. The description's publisher full text returned HTTP 403; its complete PubMed abstract and bibliography were read. The notification article landing page resolved, but its full-text endpoint was unavailable. No ANI, phylogeny, sequence-equivalence, phenotype or experimental reanalysis was performed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222736`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037377&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037377) agree on scientific name, species rank, parent and code.

The lineage is root, cellular organisms, Bacteria, Pseudomonadati, FCB group, Bacteroidota/Chlorobiota group, Bacteroidota, Flavobacteriia, Flavobacteriales, Weeksellaceae, Chryseobacterium group and Chryseobacterium. All stored IDs, labels and ranks match the pinned backbone. EFetch verifies the chain below root; Datasets includes root 1. GTDB's Bacteroidia classification and older BacDive family/phylum strings do not replace NCBI's lineage.

Native name rows `data/catalog/ncbi_names-0005.jsonl.gz:32355` through 32361 contain five `includes` names, the scientific name and its authority. The six related synonyms preserve the includes/authority scope rather than asserting that five isolates are one exact strain. Live NCBI additionally exposes Chryseobacterium piscis as a misspelling; it is not an alternate accepted species or a required exact synonym. Four older taxon IDs, 1037374, 1037375, 1037376 and 1037378, merge into 1037377 in the pinned merged-ID inventory.

[LPSN record 790317](https://lpsn.dsmz.de/species/chryseobacterium-viscerum), inspected both through the web reader and by a direct current fetch, supports the name, authority, species rank and publication/correct-name status. The pinned LPSN row is `data/raw/lpsn_names.tsv:27294`. Its type-deposit list is narrower than the primary description and LPSN page; see the minor finding below.

The two GTDB entries are correctly preserved as pooling mappings under the repository's documented predicate convention, not six genomes proven to be this NCBI taxon or one strain:

| GTDB species | Pinned genomes | NCBI identities of members |
| --- | --- | --- |
| Chryseobacterium viscerum | 4 | 687B-08/GCF_002899945.2 and DPS/GCF_008386485.1 under 1037377; KBW03/GCF_003852415.1 under 2153362; MEBOG07/GCF_021869745.1 under 2879939 |
| Chryseobacterium viscerum_A | 2 | HW314/GCF_025949665.1 under 1037377; HR92/GCF_045689405.1 under 3094839 |

The six complete native GTDB rows agree with `data/raw/gtdb_species.tsv:42652` and 42653 and the five inspected mapping rows. LPSN's transformed link selects the unsuffixed primary mapping. Only that mapping becomes an xref; the GTDB attestation correctly counts its four genomes and notes the additional pool. This does not reconcile GTDB and NCBI species boundaries.

## Evidence

[Zamora et al., PMID 22268076](https://pubmed.ncbi.nlm.nih.gov/22268076/), DOI 10.1099/ijs.0.036699-0, describes five isolates and identifies the type strain as 687B-08 = CECT 7793 = CCUG 60103. The inspected abstract supports their taxonomic study and type-deposit relationship, not a blanket species-wide disease mechanism. The second DOI, [10.1099/ijs.0.050427-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.050427-0), resolves to the 2013 notification list for names in IJSEM volume 62, part 12. It is a nomenclatural notification, not a second experimental species description.

[FR871426.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871426.1) resolves the record's unversioned INSDC accession. The full annotation identifies a 1,333-base partial 16S sequence from type strain 687B-08, host Oncorhynchus mykiss, isolation source host gills, taxon 1037377, and the same PMID/description DOI. Declared and actual lengths agree; the sequence includes ambiguous N bases. This marker is correctly in nomenclature sequence accessions, not genome counts. Preserve the supplied unversioned accession in the generated record.

[BacDive 133773](https://bacdive.dsmz.de/strain/133773) and its native projection support 687B-08, CCUG 60103, CECT 7793 and species-level classification 1037377. Its explicit genome block, reference 66792, supplies all three identifiers stored in the YAML: unversioned GCA_002899945, IMG 2871710237 and BV-BRC 1037377.3. The field paths, scaffold level, source reference and verbatim description are retained.

Assembly versions must remain distinct. Current NCBI GenBank/RefSeq and GTDB identify GCA/GCF_002899945.2, while their historical catalogs mark version 1 replaced. BV-BRC 1037377.3 explicitly retains GCA_002899945.1. BacDive's description says ASM289994v2 but its accession is unversioned. GOLD analysis Ga0336172 associates IMG 2871710237 with GCA_002899945.2 through Gp0359032/Go0475402. These observations verify the source identifiers while exposing version differences; they do not prove all three sequence objects equivalent. The YAML does not add an equivalence edge or silently choose a version.

BacDive 156019 carries CCUG 60107 under the source label Chryseobacterium viscerum subsp. anurealyticum, with a source type flag, but maps it to NCBI species 1037377. BacDive 156020 carries CCUG 60108 under Chryseobacterium viscerum subsp. viscerum and is not source-flagged type. Their empty generated designations match the BacDive inventory. The species record correctly retains both strains without inventing NCBI subspecies or promoting CCUG 60107 to the species type. The generated type flag is derived from this taxon's LPSN deposit list, not every native BacDive type flag.

Independent StrainInfo rows support four exact own-deposit paths:

| BacDive | SI-ID / version DOI | Matched SI-DP | Preserved status |
| --- | --- | --- | --- |
| 133773 | 382383 / 10.60712/SI-ID382383.3 | 876812, CCUG 60103 | published online / available |
| 133773 | 382383 / 10.60712/SI-ID382383.3 | 876813, CECT 7793 | published online / available |
| 156019 | 412214 / 10.60712/SI-ID412214.2 | 920345, CCUG 60107 | published offline / private |
| 156020 | 409001 / 10.60712/SI-ID409001.2 | 916552, CCUG 60108 | published online / available |

All three DOI versions resolve in the public DataCite API to the corresponding StrainInfo record and version. A private deposit status is public metadata about availability, not evidence that the culture can be obtained. The two non-type-record SI sources lack an own NCBI identifier, and the YAML appropriately omits that taxon field on those assertions. The same native SI group 382383 also contains CECT 7845/SI-DP898679; it does not match either existing BacDive deposit and cannot be imported solely by group membership. None of these three source records supplies a sequence list, so no StrainInfo genome assertion is missing from their inspected native content.

GOLD Go0043523 supports two source-field assertions for CCUG 60103, one from the culture-collection field and one from the strain field. They are provenance paths, not two organisms. No inspected project attaches to Go0043523. The 687B-08 project/analysis belongs to different organism Go0475402 with a bare strain designation and no culture identifier; its genome chain must not be transferred to the CCUG record through a name or species match.

All six attestations match their committed inventory units: NCBITAXON 1 NAME, LPSN 1 NAME, GTDB 4 GENOME, BACDIVE 3 STRAIN, GOLD 5 ORGANISM and MADIN 8 TRAIT_ASSERTION. GOLD's count comes from the pinned KGX-derived inventory; the separately captured native workbook projection has four own-taxonomy organism rows. Those are different source surfaces, not proof of five current native organisms or five genomes. The underlying KGX count could not be independently replayed at the unavailable configured path. Madin's eight is an assertion count, not eight phenotypes independently verified here.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It included bounded taxon/source IDs, the exact species label/slug, 687B-08, CCUG 60103/60107/60108 and CECT 7793. Identity and matching fields of all 168 matching lines were inspected; claim-bearing native rows were read in full as detailed above. All sixteen matching ATB catalog rows were read in full.

The only species-matching ATB catalog row was SAMN12659179/ERZ25637948, with SRR10056317 and PASS filters. NCBI, BV-BRC and GOLD identify that sample with DPS, not the three inventoried BacDive strains. It supplies no eligible own-strain link. Other ATB hits were unrelated accessions or SeqKit-sum substrings. Other numeric collisions included MGBC labels, sequence accession components, unrelated source record/deposit IDs and assembly statistics; none established an additional target strain link.

Five SOURCE.json files were separately parsed, retaining own request metadata and distinguishing numerical collisions. Gitignore-independent filename enumeration found one target YAML and no prior target report; history filename inspection found no target-specific filename. No direct backbone child or own MediaDive/BactoTraits row was present in complete structured scans. These are bounded repository checks, not universal absence claims.

All three classified BacDive strains are retained without a presentation cap. Optional definitions, mechanistic evidence and causal graphs need not be invented. iModulonDB is not applicable to the asserted taxonomy, deposit and identifier relationships; a cited 16S marker does not create a transcriptomics claim. No global dataset-absence claim is made.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**Minor: the nomenclature type-deposit list omits CECT 7793.** `nomenclature[0].type_strain_designations` contains only CCUG 60103, faithfully copied from `data/raw/lpsn_names.tsv:27294`. The current LPSN page, the original description's inspected abstract and pinned NCBI type-material rows identify both CCUG 60103 and CECT 7793. CECT 7793 already appears on the correctly type-flagged BacDive 133773 strain, so strain identity and genome/deposit joins remain intact; the gap is the narrower typed nomenclature list.

Maintained owner: the upstream kg-microbe LPSN name-to-culture-deposit transform/input consumed by `src/taxonmech/extract.py` (`extract_lpsn`), then the generated raw inventory and seeding. `src/taxonmech/seed.py` preserves the current inventory faithfully. The unavailable upstream edge file prevents identifying whether the omission arose in its source snapshot or transform. Do not hand-edit the generated YAML or invent a broader subspecies correction.

No other blocker, major or minor defect was established within the inspected source scope. Assembly-version differences, native subspecies labels, GOLD snapshot-count differences and unavailable checks remain explicitly bounded observations, not silently resolved equivalences.

## Recommended Edits

In a separately authorized curation, verify and preserve the LPSN association to `kgmicrobe.strain:CECT-7793` alongside `kgmicrobe.strain:CCUG-60103` in the maintained upstream input. Inspect the upstream transform before deciding whether this requires a source refresh or parser fix. Regenerate the LPSN inventory through the documented extractor and regenerate the taxon through the validated seed path. Preserve the existing type strain, deposit identities, source provenance, mapping predicates and accession versions.

Do not add CECT 7845 through SI group membership, use CCUG 60107's source subspecies type flag as species-type evidence, transfer the DPS ATB sample to 687B-08, or unify the version-1 BV-BRC sequence with version 2 by inference.

## Follow-up Checks

For the minor fix, confirm the maintained LPSN input has both supported full culture IDs; assert that extraction retains both in `type_strain_ids` and the seeded nomenclature list while BacDive 133773 remains the single recognized species type strain. Use focused extraction/seeding tests, a documented canary and schema/strict/history validation, then full-corpus reproduction and QC gates.

A later source refresh should separately reconcile dated GOLD count provenance and investigate the BacDive/BV-BRC assembly-version description difference without rewriting the historical assertions. Any new genome link must have its own explicit deposit-to-source chain. A new StrainInfo sequence additionally requires the same matched SI-DP.

## Additional Notes

- YAML SHA-256: `bd65fb81d1d0857bbb1750ab505938c17f74b13bf032f107fa0c749de65232c9`.
- `data/taxa/PATHS.tsv:15285` and `curation/seed_scope.tsv:8798` uniquely resolve the target; `curation/legacy_page_paths.tsv:923` is a page alias, not another record. The seed retains 2026-09-13T17:54:04Z and its exact six-source reason.
- SeqCode native record 5195 retains this name as catalog context; it is not an additional curated SeqCode-grounding assertion.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
