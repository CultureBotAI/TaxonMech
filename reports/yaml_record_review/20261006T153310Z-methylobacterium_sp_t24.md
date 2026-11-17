# YAML Record Review: Methylobacterium sp. T24

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_t24.yaml`
- Started UTC: 2026-10-06T15:31:01Z
- Finished UTC: 2026-10-06T15:33:10Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035208`, label `Methylobacterium sp. T24`, SPECIES / BACTERIA. The entire YAML was read before judgement and confirmed byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. An ignored-independent filename check found this target and no earlier report for its stem.

The record has EXACT grounding, SEEDED status, ten root-first ancestors, code 11, zero BacDive strains, one NCBI NAME attestation and one seed event. Synonyms, equivalent xrefs, nomenclature, taxonomy mappings, genome links, definition, citations, phenotype and causal graph are not asserted.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_t24.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_t24.yaml --out /private/tmp/mt24-strict.tsv`: one file, zero ERROR rows. The actual output TSV was read and contains only its header.
- PASS, bounded manual comparison: pinned identity, whole lineage, code, attestation, scope and seed-event content match. This does not replace corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc` and the test suite. No full-corpus pass is claimed.
- No curator-added graph nodes need term validation. `conf/id_label_targets.yaml` excludes taxonomy fields; their agreement was manually checked here.
- No separate target history artifact was found by the ignored-independent filename search. Inline history passed record validation; no external history validator was run against an invented artifact.
- The YAML asserts no DOI, PMID or quotation. The marker-linked publication below was checked for completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221929`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035208&retmode=xml) and [NCBI taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035208) agree on exact identifier, label and SPECIES rank. Both live responses were read in full. XML confirms bacterial division, parent 2615210, code 11 and no alternate names; dataset metadata confirm all ten root-inclusive ancestor IDs. Pinned ancestor labels/ranks match the YAML.

The parent is the no-rank grouping `unclassified Methylobacterium`, below genus 407. Carry this NCBI lineage unchanged. A sequence strain qualifier does not authorize changing the NCBI rank, and EXACT does not imply a validly published binomial.

The complete [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was inspected and searched for T24. It names M. organophilum as type species and supplies no T24 species-name or type-deposit attribution. No genus-level nomenclature was inherited. The legacy taxonomy-browser route was unavailable; the successful structured NCBI responses supplied the identity check.

Exact pinned scans found no child, type-material, merged-ID or dropped row for the target.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221929` supports identity, parent, rank, code, empty synonym fields and NCBI-only provenance.
- Full native `data/catalog/ncbi_names-0005.jsonl.gz:31397` supplies the exact scientific name and taxid with an empty unique-name field.
- `data/taxa/PATHS.tsv:14420` resolves the slug. `curation/seed_scope.tsv:322204` adds it on 2026-09-13 under its one-source attested rule.
- The 2026-09-13T17:54:04Z seed event agrees with that scope and source list. One NAME is a source assertion, not a genome or deposit count.

Two numeric hits are the same unrelated assembly: `data/catalog/ncbi_genbank-0063.jsonl.gz:30063` and `data/catalog/gtdb_genomes-0002.jsonl.gz:32964`. Both complete native rows were read. GCA_964555515.1 / GB_GCA_964555515.1, isolate SRP239243_co2_85, has NCBI taxid 332614, uncultured Pseudomonadales bacterium, BioSample SAMEA117124989 and project PRJEB82487. The matching 1035208 is genome size / total length, not taxonomy. GTDB places this metagenome-derived assembly in UBA1388 sp964555515, Patescibacteriota. Neither classification or assembly belongs to T24; their source disagreement is not a defect in this target.

Exact Entrez `txid1035208[Organism:noexp]` returned zero assemblies with phrases-not-found / no-items diagnostics, and one Nuccore UID, 347300705. The full nucleotide ID list equals the query count. The assembly no-hit is bounded to that exact query.

Complete [GenBank metadata for FR869804.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869804.1) identify a 1,335-nt partial 16S rRNA sequence, strain T24, exact taxon 1035208, host Trifolium repens and host leaf surface as isolation source. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. Every feature, source qualifier and reference was read; bases were omitted. No culture-collection qualifier, BioSample, BioProject or assembly is supplied. This is a marker, not a genome.

The explicit reference is Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. Fresh [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml) inspection confirms the pairing and a phyllosphere-community study across hosts, sites and land-use types. The abstract does not name T24 or establish its isolate-specific phenotype, sampling locality or growth requirement. Full text and supplements were not inspected; community results were not transferred to T24.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded T24/T-24 context and accession searches established no eligible culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit assertion.

Zero strains matches the BacDive subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: no exact BacDive row or descendant contributes an entry. This is not a claim that the isolate was never cultured. The existing `normalize_culture_identifier` function was run on T24 and T-24 and rejected both as bare, unsupported deposit identifiers.

The optional FR869804.1 link is not a required-representation defect under the current contract. No supported strain entry or eligible SI-DP association was established to receive it. Empty optional biological fields are appropriate.

The structured iModulonDB adapter ran before browser follow-up and returned 28 datasets with no Methylobacterium/Methylorubrum coverage. It is not applicable, not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record and inspected evidence scope. Identity and provenance are supported without treating an unrelated genome-length value as a taxonomic match or the 16S marker as a genome. This pass does not certify full-corpus reproducibility.

## Recommended Edits

None required.

Future marker enrichment belongs in maintained extraction/seeding logic such as `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, after explicit identity and an appropriate typed representation are established. Do not edit generated YAML, infer a culture accession from T24, or count FR869804.1 as a genome.

Do not promote SEEDED to REVIEWED or append curation history from this report.

## Follow-up Checks

- Repeat exact taxonomy, lineage, status, schema and strict checks on source refresh.
- After authorized source/import changes, run full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded checks do not replace these gates.
- Require an eligible own-deposit identifier and explicit sequence attribution before a StrainInfo link.
- Inspect the full text and supplements of PMID 22000032 before T24-specific biological enrichment.
- Match taxonomic fields rather than arbitrary numeric occurrences.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial taxid/label/slug search returned five rows, including two unrelated assembly rows. Expanded Methylobacterium/Methylorubrum T24/T-24 context returned the same three target identity/scope rows. All five distinct candidates were read fully through structured comparisons and lossless native JSONL decoding. FR869804 / 347300705 returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored and compressed files and remain bounded to these roots.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Only inspected primary source content supported biological judgements; failed browser output was not evidence.

Only this new report was written for this target. No YAML/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota was not reopened.
