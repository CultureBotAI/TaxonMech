# YAML Record Review: Kurthia senegalensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/kurthia_senegalensis.yaml`
- Started UTC: 2026-10-04T18:50:10Z
- Finished UTC: 2026-10-04T18:54:55Z
- Verdict: pass with minor issues

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033740`, rank
`SPECIES`, domain `BACTERIA`, with `EXACT` grounding and `SEEDED` mapping
status. It contains one LPSN name, two GTDB mappings, two BacDive strains,
eight source attestations and the seed event of 2026-09-13T17:54:04Z.
Maintained owners are the source inventories, extractor, seed scope,
path lock and `src/taxonmech/seed.py`; generated YAML was not edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/kurthia_senegalensis.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/kurthia_senegalensis.yaml`: exit 0, one file, zero errors; normal diagnostic TSV under `reports/`.
- Structured comparisons checked identity, all nine ancestors, code 11, synonyms, direct source rows, crosswalks, scope, path lock and seed event. These are bounded comparisons, not a corpus reproduction validator.
- `just verify-corpus` was skipped: its documented implementation rebuilds the full corpus and has no target-record selector. `--max-diffs` does not narrow its scope.
- `just validate-products` was not run because there are no curator-grounded graph nodes and its OAK configuration does not validate these identity/source fields. NCBI identity was checked directly.
- Ignored-inclusive target searches found no separate target history artifact. Full-history validation, `just qc`, all-record validation, provenance hashing, corpus tests and rendering checks were not run. No history or review-status change was made.

## Identity and Grounding

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033740&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033740)
confirm the species, parent Kurthia (`NCBITaxon:1649`), nine root-first
ancestors and genetic code. Pinned backbone row
`data/raw/ncbitaxon_taxa.tsv:221305` agrees. Complete relevant tables contain
no children or merged/dropped status for this ID. NCBI's authority name
and includes name `Kurthia sp. JC8E` are conservatively represented as
related synonyms, not exact synonym claims.

[LPSN 792183](https://lpsn.dsmz.de/species/kurthia-senegalensis) confirms
the correct, validly published name, Roux et al. 2016, type JC8E = DSM
24641 = CSUR P138, and marker JF824796. Inventory row
`data/raw/lpsn_names.tsv:28963` supports the emitted nomenclature fields.
Its type-designation list has DSM 24641; the JC8E strain entry also retains
CSUR P138, so that alias is not lost.

The complete pinned GTDB scan covered 901,341 genome rows and found:

| GTDB species | Complete cluster membership | Mapping interpretation |
|---|---|---|
| `s__Kurthia_senegalensis` | `RS_GCF_000285595.1` (type JC8E), `RS_GCF_902385695.1` (MGYG-HGUT-02309), `GB_GCA_963596445.1` (MAG) | Three genomes; first two use NCBI 1033740, last uses NCBI 3077420, Acutalibacteraceae bacterium. LPSN supports the primary name link. |
| `s__Cryptobacteroides_sp963620825` | `GB_GCA_963620825.1`, H07613-L1_cleanbin_000037 | One genome, assigned NCBI 1033740. Exactly one mapping row, to this NCBI taxon. |

Native singleton evidence is
`data/catalog/gtdb_genomes-0006.jsonl.gz:8913`; mapping row 1367 and species
row 47464 agree with its count. GTDB places this MAG in Bacteroidota,
whereas NCBI retains the Kurthia/Bacillota assignment. This is a genuine
upstream classification conflict, not evidence that the type culture is
Cryptobacteroides. The repository explicitly uses `broadMatch` as a pooling
signal; the secondary species is correctly excluded from xrefs and exact
synonyms. Only its explanatory note overstates what the cluster proves.

## Evidence

| Claim | Inspected support |
|---|---|
| JC8E is type material | LPSN, NCBI type-material rows 1669-1674, [BacDive 130537](https://bacdive.dsmz.de/strain/130537), native BacDive row 52850 and the primary description agree on DSM 24641 / CSUR P138. |
| JC8J / DSM 24642 is distinct and non-type | [BacDive 130538](https://bacdive.dsmz.de/strain/130538), native row 52851 and its own StrainInfo deposit agree; its BacDive sequence section is empty. |
| JC8E genome assertions | BacDive reference 66792 explicitly supplies unversioned `GCA_000285595`, IMG 2548876796 and BV-BRC 1033740.3, with the emitted assembly name and level. Raw assembly row 15474 and genome-record rows 12048-12049 preserve that provenance. |
| GOLD related records | Native organism row 444582, Go0613849, has DSM 24641 in both culture-collection and strain fields. Raw related rows 45775-45776 preserve two different matching-field provenances, not an accidental duplicate genome. |
| JC8E StrainInfo evidence | Native row 297619 connects strain 399730 to its own available DSM 24641 deposit 906545, BacDive 130537, taxon 1033740 and versioned DOI `10.60712/SI-ID399730.3`. |
| JC8J StrainInfo evidence | Native row 298580 independently connects strain 400691, own DSM 24642 deposit 907572, BacDive 130538 and DOI `10.60712/SI-ID400691.2`. Both native strain statuses are published online. Neither object supplies a sequence assertion. |

The [primary description](https://europepmc.org/articles/PMC4148981), DOI
`10.4056/sigs.5078947`, was read in full through Europe PMC XML. PubMed XML
confirms PMID 25197500 denotes that 2014 paper. Its type-strain description,
marker and CAEW genome project support the identity links, without making
its strain-level phenotypes assertions of this record.

The [publisher validation-list page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.001149)
confirms the cited DOI and 2016 publication and references the Roux paper.
LPSN identifies Validation List 170 as the valid publication. The individual
validation-table row was not independently inspected: the publisher's
embedded full-text endpoint was inaccessible. The 2014 effective paper
and 2016 nomenclatural authority are not inconsistent.

[NCBI marker EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF824796&rettype=gb&retmode=xml)
resolves JF824796 to `.1`, a 1,476-base partial 16S rRNA sequence from
JC8E, with the target taxon and type-material qualifier. It is correctly
kept separate from whole-genome accessions.

All eight attestations match their direct inventories: NCBI one name,
LPSN one name, GTDB three primary-cluster genomes plus a note for one
additional pooled species, BacDive two strains, MediaDive one medium (92),
GOLD four organisms, Madin one trait assertion and BactoTraits one trait
assertion. The GTDB count is not an aggregate of both clusters; the
different assertion units must not be summed.

## Completeness

Both BacDive strains and all eligible exact-strain crosswalk assertions
are retained. Complete crosswalk scans found no StrainInfo assembly rows
or ATB strain/genome links for these two strains. StrainInfo related rows
25652-25655 are fully represented. Searches included ignored and compressed
content using the target ID/name, species mapping, both DSM deposits,
CSUR P138, the relevant GOLD organism IDs and all three NCBI BioSamples,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
Numeric collisions were excluded. These absence findings are bounded to
the inspected artifacts, not all remote sources.

GOLD's other organisms are Go0017287 (JC8E), Go0613850 (CSUR P138) and
Go0636940 (MGYG-HGUT-02309). JC8E's project Gp0017287 and analysis Ga0020300
link to Go0017287, not the deposit-matched Go0613849. The expanded complete
search found no project/analysis chain referencing Go0613849. Shared
species or a bare isolate designation does not authorize transferring the
other organism's genome chain to this culture.

An ignored-inclusive search of the pinned CAFI registry found no CSUR
entry. The actual matcher accepts DSM 24641 and DSM 24642, but returns no
key for CSUR P138 or its encoded CURIE. The CSUR-only GOLD organism thus
does not supply an eligible new join under current authority rules. Native
GTDB, NCBI and BV-BRC metadata corroborate JC8E's genome but use bare JC8E,
not a new deposit token. MGYG and MAG records must not be assigned to
JC8E or JC8J on taxon membership alone.

Optional graph, discussion and record-level evidence slots are correctly
unpopulated in this seeded identity record. `data/taxa/PATHS.tsv:13758`
and `curation/seed_scope.tsv:1529` agree with the target and its seed event.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. **Minor: the secondary GTDB note claims additional NCBI taxa without support.**
   It says the singleton Cryptobacteroides species "also maps to other NCBI
   taxa", but its complete pinned membership and mapping table show only
   NCBI 1033740. The pooling signal is supported; that additional clause is
   not. The wording is emitted unconditionally by
   `src/taxonmech/seed.py:461`, not authored in this generated record.
   Identity, count, primary mapping and strain associations remain sound.

## Recommended Edits

Correct the broad-match note in maintained `src/taxonmech/seed.py` to
describe a source assignment/pooling signal without asserting other NCBI
taxa unless those have actually been established. Add a singleton pooled
cluster regression in `tests/test_seed.py`; its existing mapping assertions
only require the word `Pooled` and would not detect this overstatement.

After an authorized implementation and test pass, regenerate through the
documented seed workflow and verify the generated products. Do not patch
this YAML directly, delete the secondary source mapping, change the NCBI
lineage or move the MAG into a type-strain genome list to address a prose
finding. Any resolution of the MAG classification conflict belongs in
the upstream authorities and subsequent inventory extraction, not an
inferred identity override in the seed projection.

## Follow-up Checks

- Add a regression with one NCBI taxon pooling into multiple GTDB species, including a singleton secondary cluster, and assert the note makes no unsupported reverse-cardinality claim.
- Run `uv run pytest tests/test_seed.py`, regenerate through the maintained seed workflow, rerun both target validators, then full `just verify-corpus` and applicable `just qc` gates. These proposed post-change checks were not reported as passed here.
- Recheck the validation-list table when accessible. On the next source refresh, separately recheck NCBI and GTDB assignments for GCA_963620825.1 without treating the two classifications as equivalent.

## Additional Notes

[Current NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000285595.1/dataset_report)
confirms JC8E's current scaffold assembly, paired RefSeq version, type
material, SAMEA2272665 and PRJEA70835. Its ANI diagnostic explicitly notes
the type-strain situation; it was not treated as evidence of a wrong
record identity. Exact-taxonomy assembly search returns three current
assemblies: the type assembly, MGYG-HGUT-02309 (`GCA/GCF_902385695.1`), and
the MAG (`GCA_963620825.1`, excluded from RefSeq as metagenome-derived).
Their full native NCBI and BV-BRC objects were inspected. Current NCBI
still places the MAG under taxon 1033740, so the conflict has not been
silently resolved in the record's favor.

The primary paper's assembly statistics differ from current assembly
metadata; no conflicting statistics are emitted in this YAML. SeqCode
record 10287 corroborates the name, but no SeqCode validation or identifier
is claimed. iModulonDB is not applicable: no gene, regulator, pathway or
transcriptomic claim is present.

Only this report was added as a review artifact. No record, inventory,
history, status, source code or prior report was edited; no paid research,
external contact or GitHub mutation was performed.
