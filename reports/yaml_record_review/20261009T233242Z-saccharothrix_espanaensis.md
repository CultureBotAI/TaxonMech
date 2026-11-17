# YAML Record Review: Saccharothrix espanaensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/saccharothrix_espanaensis.yaml`
- Started UTC: 2026-10-09T23:25:13Z
- Finished UTC: 2026-10-09T23:32:42Z
- Verdict: needs curation

## Target

Entire 946-line generated `TaxonRecord` read. `NCBITaxon:103731` denotes Saccharothrix espanaensis, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2071`, genetic code 11, grounding `EXACT`, status `SEEDED`. All nine ancestors, nomenclature, synonyms, xref, two nested strains, six source attestations and seed event were inspected.

This is the species record, not its separately indexed child strain `NCBITaxon:1179773`, Saccharothrix espanaensis DSM 44229. Child taxonomy and source rows were checked only to verify descendant-strain gathering. The 7 assembly, 6 genome-record and 44 related-record entries are 57 source-specific assertions, not 57 independent genomes or cultures. Fifty-five belong to BacDive 13482 and two to BacDive 13483.

## Validation

Commands used the repository environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/saccharothrix_espanaensis.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/saccharothrix_espanaensis.yaml --out /private/tmp/taxonmech-saccharothrix-espanaensis-20261009-validation.tsv --workers 1`: one file, zero errors. The output TSV was reread and contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured comparisons matched the entire lineage, own scope/index rows, seed text and all 57 strain assertions against the raw, StrainInfo and ATB inventories, with no missing or extra assertions. These comparisons are bounded inventory checks, not corpus reproduction or independent source verification.
- Complete source-native candidate rows were separately inspected, including deposit-level sequence evidence. Public NCBI taxonomy, assembly, sequence and BioProject metadata, ENA project XML, DataCite, LPSN, BacDive and BV-BRC checks succeeded within the scopes below. The live GTDB genome page could not be retrieved.
- A direct call to the maintained NCBI strain-token and culture-normalization helpers confirmed that `strain=type strain: DSM 44229` does not join, whereas `strain=DSM 44229` normalizes to `DSM-44229`.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, source-provenance replay, rendering and publication gates. `just validate-products` has no applicable graph nodes. Public accession checks do not establish identical genome sequences or validate downloaded assembly payloads.

Schema success does not resolve the external BioProject reference finding.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18557` agrees with the label, rank, parent, code, authority-related synonym and exact equivalent-name spelling Saccharothrix espanensis. The root-first lineage matches the pinned backbone and inspected live [NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103731): root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Pseudonocardiales, Pseudonocardiaceae and Saccharothrix. No exact own-ID merge or dropped row was found in the complete corresponding raw tables.

The child row `data/raw/ncbitaxon_taxa.tsv:262991` places DSM 44229 directly beneath the species. Its alternative strain designations are not synonyms of every strain in the species. BacDive 13482 correctly retains this most-specific classification in `classified_as`; BacDive 13483 is filed directly under the species.

`data/raw/lpsn_names.tsv:19707` and the current [LPSN page](https://lpsn.dsmz.de/species/saccharothrix-espanaensis) support `lpsn:780706`, authority Labeda and Lechevalier 1989, validly published/legitimate/correct-name status, the four stored type deposits, AF114807 and the original publication. The live type list additionally includes VKM Ac-1969 and LL-C19004-NS29; the nested BacDive type strain already includes VKM Ac-1969. The generated nomenclature accurately retains its pinned four-deposit input. The medical-use wording concerns the recommended name, not clinical use of the organism.

The [original 1989 paper](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-39-4-420), DOI 10.1099/00207713-39-4-420, explicitly identifies NRRL 15764 as this species' type strain. Publisher bibliographic information and abstract were inspected; no full-text review is claimed.

No direct species-level GTDB mapping is supplied by the inventories. `data/raw/gtdb_mappings.tsv:10012` belongs to child 1179773 and uses Actinosynnema espanaense. The complete native genome row `data/catalog/gtdb_genomes-0004.jsonl.gz:30914` supports RS_GCF_000328705.1 and that GTDB classification. GTDB's different genus/order placement does not authorize replacing the record's NCBI lineage, copying the child's mapping count into this species, or interpreting source rows as independent genomes.

## Evidence

The six attestations retain distinct units and scopes:

| Source | Count and unit | Support |
| --- | --- | --- |
| NCBITAXON | 1 NAME | Own backbone row and 2026-09-13 snapshot |
| LPSN | 1 NAME, closeMatch | Own name record 780706 |
| BACDIVE | 2 STRAIN | One direct strain plus one explicitly gathered descendant |
| MEDIADIVE | 1 MEDIUM | Own row `data/raw/mediadive_taxa.tsv:140`, medium 65 |
| GOLD | 5 ORGANISM | Own count row 521 and five direct-species native organisms |
| MADIN | 5 TRAIT_ASSERTION | Own row `data/raw/madin_taxa.tsv:706` |

Child-only MediaDive, Madin and BactoTraits counts are not added to the species' direct attestations. Source counts do not establish particular metabolic functions or species-wide growth conditions.

Native BacDive rows `data/bacdive/records.jsonl.gz:13317` and `:13318`, raw strain rows 13318-13319, and the public [13482](https://bacdive.dsmz.de/strain/13482) and [13483](https://bacdive.dsmz.de/strain/13483) pages support the two distinct strain identities and culture collections. The type strain carries ATCC 51144, CGMCC 4.1714, DSM 44229, IFO 15066, IMSNU 21342, JCM 9112, KCTC 9392, NBRC 15066, NRRL 15764 and VKM Ac-1969. DSM 42033/UTMC 702 is not promoted to the nomenclatural type. No type-strain genome is transferred to that second strain.

BacDive reference 66792 supplies the unversioned assembly GCA_000328705. Its source-specific IMG 2540341184 and PATRIC 1179773.3 links remain distinct genome identifiers. Native BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:24494` and a fresh [public genome API response](https://www.bv-brc.org/api/genome/?eq(genome_id,1179773.3)&select(genome_id,genome_name,taxon_id,strain,culture_collection,assembly_accession,biosample_accession,bioproject_accession,public)&limit(1)) independently associate DSM 44229 with GCA_000328705.1 and SAMEA2272236. The match uses the exact strain field, not the different source culture spelling DSM 44229T. The response also reproduces the problematic PRJNA28 value; this is upstream source content, not a prefix invented by the seeder.

Complete GOLD rows `data/gold/analyses.jsonl.gz:10209`, `projects.jsonl.gz:23106` and `organisms.jsonl.gz:29314` support Ga0016689 -> Gp0034502 -> Go0034502, the DSM deposit, IMG identifier, assembly and PRJEB28. Both organism strain and culture fields supply retained, separate provenance assertions. The five direct-species organisms Go0606143-Go0606147 correspond respectively to ATCC 51144, IFO 15066, JCM 9112, NBRC 15066 and NRRL 15764. They support the count of five organism records, not five new sequenced isolates. The DSM organism belongs to child 1179773 and is not added to that count.

Native NCBI rows `data/catalog/ncbi_genbank-0000.jsonl.gz:8462` and `ncbi_refseq-0000.jsonl.gz:7295`, and focused live [GenBank](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000328705.1/dataset_report) and [RefSeq](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000328705.1/dataset_report) metadata confirm the current paired complete assemblies, DSM 44229, child taxon 1179773 and SAMEA2272236. The absence of direct NCBI-source assertions is explained below; it is not absence of an assembly.

The pinned GTDB/RefSeq project PRJNA224116 resolves to a multispecies RefSeq annotation project. [Focused NCBI BioProject XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=224116,183921&retmode=xml) distinguishes it from PRJEB28, whose taxon, DSM designation and explicit assembly/sample locus-prefix entry agree with this genome. The [ENA PRJEB28 record](https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB28) independently supports that sequencing-project identity. These annotation and sequencing contexts should not be collapsed. PRJNA28 remains a separate, unresolved source assertion, not another verified project.

Complete native StrainInfo rows `data/straininfo/records.jsonl.gz:34139` and `:295622` support SI-ID 46138 and 397733, respectively. Their [versioned DOI metadata](https://api.datacite.org/dois/10.60712/SI-ID46138.3) and [DSM 42033 DOI metadata](https://api.datacite.org/dois/10.60712/SI-ID397733.1) resolve to the correct records. DOI issuance, archival dates and version strings are distinct provenance layers, not interchangeable dates.

The type strain's nine eligible exact own-deposit matches are ATCC 51144/125132, NRRL 15764/125133, DSM 44229/169329, IFO 15066/169330, JCM 9112/169331, VKM Ac-1969/227890, KCTC 9392/319688, NBRC 15066/335702 and CGMCC 4.1714/753893. All are available and non-erroneous in the native record. Two further StrainInfo deposits, NRRL B-15764/303740 and AS 4.1714/335700, do not exactly match the listed BacDive deposit IDs; alias rewriting is not allowed. IMSNU 21342 is not an extra own SI-DP. StrainInfo's genome explicitly names DSM deposit 169329, AF114807 names NRRL deposit 125133, and DQ001145 names ATCC deposit 125132. All same-deposit sequence checks pass. The unversioned accessions remain unversioned.

The second strain's SI-ID 397733, DOI 10.60712/SI-ID397733.1 and sole available DSM 42033 deposit 904387 support its two related-record assertions. UTMC 702 is an alias, not another deposit. Its native record has no sequence; the type strain's sequences are not borrowed.

Live [AF114807 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AF114807) identifies AF114807.1, a 1,510-base partial 16S sequence for NRRL 15764 with the type qualifier. [DQ001145 metadata](https://www.ncbi.nlm.nih.gov/nuccore/DQ001145) identifies DQ001145.1, a 456-base partial coding sequence from ATCC 51144, translation table 11 and protein AAY21234.1. Both currently carry child taxon 1179773; StrainInfo's source taxon 103731 is retained as source provenance, not silently overwritten. DQ001145's cyclase-like annotation and [associated PCR study](https://pubmed.ncbi.nlm.nih.gov/15995652/) do not establish acarbose production by this strain. Likewise, the [DSM 44229 genome paper](https://pubmed.ncbi.nlm.nih.gov/22958348/) supplies genome context, not automatically curated functions or causal edges.

## Completeness

An ignored-independent bounded search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It included the label/slug and spelling variant, both taxonomy IDs, both BacDive IDs, full culture identifiers, assembly, sample and marker accessions. All 155 candidate native/TSV rows were inspected, with compact complete-row representations used for repeated columns. Five SOURCE.json files were separately parsed. No matching target history filename was found in the ignored-independent history inventory.

Unrelated hits were rejected after reading their records: Rhodococcus BacDive 103731, Trueperella CIP 103731, SI-DP 103731 for a Cystobacter culture, a fungal IMI 103731 deposit, unrelated assembly statistics and Salmonella strain/assembly-name number collisions. Native SeqCode record 18452 was inspected as a name-catalog entry, not as an additional curated strain assertion. No Eukaryota YAML was reopened.

ATB catalog row `data/catalog/allthebacteria.tsv.xz:5421` is a same-species candidate for SAMD00064385, DRR073080 and ERZ2885584, with available FASTA and PASS filters. It does not share the represented strain's SAMEA2272236 BioSample key. An additional ignored-inclusive compressed search for all three candidate accessions in `data/atb`, `data/raw`, `curation` and `history` found no linked evidence rows. Species-name agreement alone cannot create the required whole-sample/source-chain join. This is not evidence that the organism lacks an ATB assembly.

The native NCBI assembly rows carry `infraspecific_name=strain=type strain: DSM 44229`. `src/taxonmech/ncbi_assemblies.py:72` strips only the leading `strain=`; the remaining phrase is not a full CAFI accession. `docs/SOURCE_COVERAGE.md`, `docs/STRAIN_GENOMES.md` and the tests in `tests/test_source_expansion.py` explicitly require whole supported deposit formats, excluding descriptive strings. This documented conservative limitation explains the missing direct NCBI provenance; the assembly itself is already represented through other sources. No change to global substring or alias matching is justified.

The structured iModulonDB adapter was run through the local `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets` runner with bytecode writes disabled. All 28 returned dataset rows were read; none covered Saccharothrix or Actinosynnema. Further gene/module queries were inapplicable. This absence is not negative biological evidence.

Optional definition, functional traits and causal graph may remain empty. Aggregate source counts and sequence annotations do not require invention of mechanistic claims. The consequential identified defect is the public BioProject reference below.

## Findings

Counts: 1 blocker, 0 major, 0 minor.

**Blocker: unresolvable public BioProject reference retained as a normal related record.** `data/taxa/bacteria/saccharothrix_espanaensis.yaml:265` asserts `bioproject:PRJNA28`, sourced through `patric:1179773.3`. It traces exactly to `data/raw/strain_related_records.tsv:98173`, the complete native BV-BRC row and the fresh public API response. However, an [exact NCBI Project Accession search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=bioproject&term=PRJNA28%5BProject%20Accession%5D&retmode=json) returns zero records and an unrecognized phrase; numeric BioProject ID 28 EFetch reports that it is not public. PRJEB28 resolves separately to UID 183921 and explicitly links this strain, assembly and sample. The evidence establishes a broken public reference, not that PRJNA28 never existed or denotes a different organism. A prefix error is a plausible explanation, not an authorized correction.

This is a blocker under the review rubric's broken-reference category; it does not invalidate the species identity or the independently supported genome link. Maintained owner: `src/taxonmech/bvbrc.py`, especially its syntax-only project accession promotion, with regression coverage in `tests/test_source_expansion.py`. A future source-specific exclusion/curation decision must preserve the native value and evidence. No matching existing exception was found by an ignored-inclusive search of `src`, `scripts`, `tests`, `docs`, `conf`, `curation` and `history`.

## Recommended Edits

1. Resolve or quarantine the exact BV-BRC `1179773.3/bioproject_accession/PRJNA28` assertion in a deterministic maintained source policy before presenting it as a verified public BioProject link. Keep the original source value and reason in provenance/exclusions. Do not discard the otherwise supported BV-BRC assembly, genome or sample associations.
2. Do not globally convert PRJNA to PRJEB, replace BV-BRC evidence with GOLD evidence, or hand-edit this generated YAML. A replacement requires explicit source-specific curation evidence. PRJEB28 already has independent GOLD support.
3. Add a targeted regression fixture in `tests/test_source_expansion.py`, then use the documented inventory and seed workflow. Any approved future accommodation of NCBI's type-strain prefix is separate scope and must preserve whole-deposit validation; it is not required to resolve this reference finding.

## Follow-up Checks

Repeat exact authority resolution for PRJNA28 and retain a dated disposition. Prove the source-specific exclusion or correction in the focused extractor test while preserving valid project IDs, assembly/sample chains and native source text. Rebuild inventories through `just extract-inventory-dry` followed by the authorized extraction workflow, run a species canary, inspect its generated record, and repeat schema/strict validation. After any maintained-input change, run `just verify-corpus` and the full `just qc` gates. Do not use a review report to alter source provenance or status.

Retry live GTDB access when available. The public BioProject reference remains unresolved; no curation fix was performed in this review.

## Additional Notes

- YAML SHA-256: `a56c8da127cff5dbc51efdd36fe1107ec8f3330aa2e75b02f100eb2a846a1a8e`, unchanged on reread.
- `data/taxa/PATHS.tsv:15256` and `curation/seed_scope.tsv:9421` uniquely identify the target. The seed event retains timestamp 2026-09-13T17:54:04Z, six named source attestations and the exact six-source scope reason.
- Local catalog evidence was inspected without replaying every original large source snapshot or recomputing the corpus manifests. Live page/API retrieval failures are not treated as proof of source absence; the BioProject finding relies on successful exact authority responses and source-chain comparisons.
- Read-only review against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, input, schema, history, page, branch, worktree or GitHub mutation. The only new repository artifact is this timestamped report. The ten existing worktrees and complete Eukaryota report coverage were preserved.
