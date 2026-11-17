# YAML Record Review: Chryseobacterium tructae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chryseobacterium_tructae.yaml`
- Started UTC: 2026-10-10T01:52:47Z
- Finished UTC: 2026-10-10T02:01:24Z
- Verdict: pass with minor issues

## Target

The complete 837-line generated `TaxonRecord` was read. `NCBITaxon:1037380` denotes Chryseobacterium tructae, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:59732`, genetic code 11, grounding `EXACT`, status `SEEDED`.

The record contains twelve ancestors, one LPSN nomenclature entry, one GTDB mapping, four related synonyms, two BacDive strains, five source attestations and one seed event. Source-search candidates are identity checks, not additional completed taxon reviews.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/chryseobacterium_tructae.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/chryseobacterium_tructae.yaml --out /private/tmp/taxonmech-tructae-20261010-validation.tsv --workers 1`: one file, zero errors. The output was reread and contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, full lineage, genetic code, synonym columns, source counts, scope/index entries and exact seed reason. The complete backbone scan found no immediate child. Own type-material, merged-ID and dropped inventories were checked.
- Exact multiset comparisons verified every assembly, genome and related-record assertion against raw and StrainInfo inventories, including provenance fields. Whole-deposit CAFI normalization checks passed. No own ATB strain link was present. Native StrainInfo records were independently read to verify the deposit-level sequence binding, not merely accepted from the deserializer.
- Complete native rows were read for both BacDive records, both StrainInfo records, two GTDB genomes, four NCBI assemblies, five NCBI name rows, three BV-BRC genomes, two GOLD organisms, two GOLD projects and two GOLD analyses.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. No causal graph is asserted, so `just validate-products` has no applicable nodes.
- The configured external kg-microbe LPSN and GOLD edge paths were unavailable. Their committed inventories and relevant extraction/seeding code were inspected; this is not an upstream replay or an absence claim about all other checkouts.
- The original description's full PubMed abstract and bibliography were inspected; publisher full text was unavailable through the web reader. The validation-list landing page resolved, but its full-text endpoint did not. The live GTDB tree was unavailable. No live IMG/GOLD/BV-BRC refresh, sequence equivalence test, experimental reanalysis or independent ANI calculation was performed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222737`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037380&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037380) agree on species identity, parent and code. Live Datasets reports two assemblies.

All stored ancestor IDs, labels and ranks match the backbone: root, cellular organisms, Bacteria, Pseudomonadati, FCB group, Bacteroidota/Chlorobiota group, Bacteroidota, Flavobacteriia, Flavobacteriales, Weeksellaceae, Chryseobacterium group and Chryseobacterium. GTDB's Bacteroidia and older native BacDive family/phylum strings must not replace this verbatim NCBI lineage.

Native NCBI name rows `data/catalog/ncbi_names-0005.jsonl.gz:32362` through 32366 contain three includes names, the scientific name and the authority. The three isolate labels 1083-08, 1084-08 and 1095B-08 and the authority string are appropriately related synonyms, not assertions that all isolates are one exact strain. Old taxon IDs 1037379 and 1037381 merge into 1037380. Live NCBI's additional Chryseobacterium plurextorum misspelling does not establish another accepted species.

[LPSN 790403](https://lpsn.dsmz.de/species/chryseobacterium-tructae) supports the species name, authority Zamora et al. 2013, valid-publication and correct-name status. The 2012 effective description and 2013 validation date have different roles; the authority year is not an error. The pinned LPSN row is `data/raw/lpsn_names.tsv:27360`.

The GTDB `skos:closeMatch` and count two agree with `data/raw/gtdb_mappings.tsv:1488` and `data/raw/gtdb_species.tsv:42647`. The complete native genome rows are RS_GCF_030409875.1 and RS_GCF_042649085.1; both identify NCBI 1037380 and CECT 7798 under the unsuffixed GTDB species. The LPSN link selects this primary mapping. Neither the mapping nor its count asserts sequence equivalence.

## Evidence

[Zamora et al., PMID 22795568](https://pubmed.ncbi.nlm.nih.gov/22795568/), DOI 10.1016/j.syapm.2012.06.003, describes three isolates from diseased rainbow trout and identifies type strain 1084-08 = CECT 7798 = CCUG 60111. This supports the type-deposit relationship, not a species-wide disease mechanism. [DOI 10.1099/ijs.0.049312-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.049312-0) resolves to the January 2013 validation list, not another experimental description. LPSN identifies it as Validation List 149.

[MT760280.1](https://www.ncbi.nlm.nih.gov/nuccore/MT760280.1) resolves the stored unversioned marker. Its complete annotation identifies a 1,363-base partial 16S sequence from type strain CECT 7798, taxon 1037380, submitted in 2020. Declared and actual lengths agree; the sequence includes N bases. It is not a genome and is not the 2012 description itself. Preserve the supplied unversioned accession.

[BacDive 156023](https://bacdive.dsmz.de/strain/156023) and its native record support CCUG 60111, CECT 7798 and the type status. Reference 124043 supplies two explicit genome blocks: unversioned GCA_030409875 with IMG 8053469890 and BV-BRC 1037380.5; and unversioned GCA_042649085 without those additional identifiers. The YAML preserves the source-specific field paths and descriptions without borrowing identifiers between blocks. The BacDive matching reference is identifier-linking evidence, not independent experimental validation.

[BacDive 156022](https://bacdive.dsmz.de/strain/156022) supports CCUG 60110, with no native genome sequence block and type status no. Its text-only web rendering exposes a Type strain heading without the value; direct HTML inspection found the negative `ph-x text-danger` status icon. That agrees with the native record and is not a conflicting positive type claim.

Two distinct versioned assembly pairs are supported by pinned NCBI/GTDB and live NCBI Datasets:

| GenBank / RefSeq | BioSample | GenBank BioProject | Deposit |
| --- | --- | --- | --- |
| GCA_030409875.1 / GCF_030409875.1 | SAMN35653678 | PRJNA980407 | CECT 7798 |
| GCA_042649085.1 / GCF_042649085.1 | SAMN43282071 | PRJNA595761 | CECT 7798 |

The live [first assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_030409875.1/dataset_report) and [second assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_042649085.1/dataset_report) confirm current version 1, paired RefSeq accessions, contig level, type material and the deposit/BioSample/project associations. The assemblies have different lengths and contig counts; they must not be collapsed into one sequence object. Pinned RefSeq and GTDB metadata use umbrella project PRJNA224116, which is retained as its own source assertion rather than substituted for the GenBank project.

BV-BRC 1037380.4 and 1037380.5 both explicitly link CECT 7798 to GCA_030409875.1; 1037380.6 links it to GCA_042649085.1. The native status for 1037380.4 is Deprecated, while .5 and .6 are WGS. The generated record retains a provenance association, not an assertion that .4 is a current independent genome. Do not count these repeated source records as three new biological strains.

GOLD Go0043522 supplies CCUG 60111 in both culture-collection and strain fields; the two related assertions preserve separate source paths. The ignored-inclusive identifier follow-up found no project attached to that organism. Go0670738 explicitly supplies CECT 7798 in its strain field. Its Gp0761072/Ga0616053 chain supports IMG 8053469890 and GCA_030409875.1; Gp0880570/Ga0689266 supports IMG 8143691053 and GCA_042649085.1. The analyses resolve through their explicit projects, not an invented direct organism field.

Native StrainInfo records verify three own-deposit matches:

| BacDive | SI-ID / DOI version | SI-DP | Deposit |
| --- | --- | --- | --- |
| 156023 | 386765 / 10.60712/SI-ID386765.3 | 884086 | CCUG 60111 |
| 156023 | 386765 / 10.60712/SI-ID386765.3 | 884087 | CECT 7798 |
| 156022 | 394988 / 10.60712/SI-ID394988.2 | 898911 | CCUG 60110 |

Both versioned DOIs resolve in the public DataCite API to the corresponding StrainInfo records and versions. All three matched deposits are available and their strain records published online. SI-ID386765 identifies designation 1084-08 and explicitly binds both unversioned GCA_030409875 and MT760280 only to SI-DP884087. The YAML correctly retains that same-deposit binding; it does not transfer either sequence to SI-DP884086. SI-ID394988 identifies 1083-08, has no sequence list and also contains CECT 7797/SI-DP898910, which is not an existing BacDive deposit and is not imported solely by group membership.

BacDive 156023 has 16 assembly assertions, nine genome-record assertions and 34 related-record assertions; BacDive 156022 has two related-record assertions. These are source-provenance counts, not 16 assemblies or nine independently characterized genomes. All five attestations match their inventory units: NCBITAXON 1 NAME, LPSN 1 NAME, GTDB 2 GENOME, BACDIVE 2 STRAIN and GOLD 2 ORGANISM.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The primary pattern included taxon/source IDs, exact species label/slug, CCUG 60110/60111, CECT 7798 and the three original isolate designations. Identity and matching fields of the 532 primary-search candidates were inspected; claim-bearing native rows were additionally read in full.

The ATB candidates were unrelated accession or checksum substrings, not species/deposit matches. Other numeric collisions included unrelated culture IDs, source IDs, assembly statistics, MGBC labels and NCBI names. No Eukaryota YAML was opened to investigate those source collisions.

A narrower follow-up for the two assembly families, two BioSamples, exact GOLD organism/project/analysis IDs and MT760280 returned 65 lines, all already in the inspected own-source rows. No corresponding ATB catalog row was returned. An earlier project-inclusive search returned 9,244 lines because PRJNA595761 is a shared sequencing umbrella; it was not treated as a strain-specific candidate set or exhaustively adjudicated.

Five SOURCE.json files were separately parsed, distinguishing own request IDs from numeric collisions. Gitignore-independent filename enumeration found one target YAML and no prior target report; history filename inspection found no target-specific filename. Structured full-inventory checks found no own MediaDive, Madin or BactoTraits row. These are bounded repository checks, not universal absence claims.

Both classified BacDive strains are retained without a presentation cap. Empty optional definitions, mechanistic evidence and causal graphs need not be invented. iModulonDB is not applicable to this record's asserted taxonomy, deposits and identifier associations; the marker does not create a transcriptomic claim.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**Minor: the nomenclature type-deposit list omits CECT 7798.** `nomenclature[0].type_strain_designations` contains only CCUG 60111, faithfully copied from `data/raw/lpsn_names.tsv:27360`. LPSN, the original description's inspected abstract and the six own NCBI type-material rows support CECT 7798 as well. The correct type-flagged BacDive 156023 strain already retains both deposits, so identity and genome/deposit joins are intact; this is a non-blocking nomenclature completeness gap.

Maintained owner: the upstream kg-microbe LPSN name-to-culture-deposit input/transform consumed by `src/taxonmech/extract.py` (`extract_lpsn`), specifically its `data/transformed/lpsn/edges.tsv` input, followed by inventory extraction and seeding. `src/taxonmech/seed.py` preserves the supplied list. The unavailable configured upstream edge file prevents assigning the omission specifically to its snapshot or transform. Do not hand-edit generated YAML.

No other blocker, major or minor defect was established within the inspected scope. Deprecated BV-BRC source status and distinct assembly objects remain explicitly noted, not silently converted into current-genome or equivalence claims.

## Recommended Edits

In separately authorized curation, verify and preserve the LPSN association to `kgmicrobe.strain:CECT-7798` alongside `kgmicrobe.strain:CCUG-60111` in the maintained upstream input. Determine whether a source refresh or transform correction is needed, then regenerate the LPSN inventory and taxon through the documented extraction/seeding workflow.

Preserve full culture IDs, source-specific project chains and accession versions. Do not add a .1 suffix to imported unversioned fields, transfer StrainInfo sequences between deposits, import CECT 7797 solely through group membership, or promote CCUG 60110 to the species type.

## Follow-up Checks

Confirm both supported culture IDs survive the maintained LPSN input, extraction into `type_strain_ids` and seeded nomenclature. Assert that BacDive 156023 remains the recognized type and that both strain records retain their exact source-level assertion multisets.

Run focused extraction/seeding tests, the documented canary, schema/strict/history checks and then full-corpus reproduction/QC gates. Any later current-genome presentation should consult native BV-BRC status rather than treating the retained .4 association as current. New StrainInfo sequence evidence must explicitly bind the same matched SI-DP.

## Additional Notes

- YAML SHA-256: `f24ba6f9c4d832debbbf1a2230bccdb4e327244917752468eaa4c41393ceefad`.
- `data/taxa/PATHS.tsv:15287` and `curation/seed_scope.tsv:13874` uniquely resolve the target. `curation/legacy_page_paths.tsv:924` is a page alias, not another taxon.
- The seed retains 2026-09-13T17:54:04Z and its exact five-source reason. SeqCode native record 5191 is catalog context, not an additional curated grounding assertion.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
- Only this new report was added for the target. No YAML, maintained input, schema, history, generated page, branch, worktree or GitHub state was changed. No review status was promoted.
