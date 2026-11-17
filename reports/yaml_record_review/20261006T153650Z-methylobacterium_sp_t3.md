# YAML Record Review: Methylobacterium sp. T3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_t3.yaml`
- Started UTC: 2026-10-06T15:34:15Z
- Finished UTC: 2026-10-06T15:36:50Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035209`, label `Methylobacterium sp. T3`, SPECIES / BACTERIA. The whole YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The exact target was resolved by its path and taxid. An ignored-independent stem search also listed T32, T34, T35 and T3-YH-2228 record filenames; none changes the selected target. No earlier report for the exact T3 stem was found.

EXACT grounding, SEEDED status, ten root-first ancestors, code 11, zero BacDive strains, one NCBI NAME attestation and one seed event are present. Synonyms, equivalent xrefs, nomenclature, mappings, genomes, definition, citations, phenotype and causal graph are not asserted.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_t3.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_t3.yaml --out /private/tmp/mt3-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and has only its header.
- PASS, bounded manual comparison: pinned identity, full lineage, code, attestation, scope and seed-event content match. This is not corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc` and the test suite. No full-corpus pass is claimed.
- No curator-added graph nodes need term validation. The product-check configuration excludes taxonomy fields; their inventory agreement was manually checked.
- No separate target history artifact was found by the ignored-independent filename check. Inline history passed record validation; no external history validator was run against an invented artifact.
- The record asserts no PMID, DOI or quotation. A sequence-linked publication was inspected for completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221930`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035209&retmode=xml) and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035209) agree on exact ID, label and SPECIES rank. Both live responses were inspected in full. XML confirms bacterial division, parent 2615210, code 11 and no alternate names. Dataset metadata confirm all ten root-inclusive ancestor IDs; pinned labels and ranks match the YAML.

The parent is the no-rank grouping `unclassified Methylobacterium`, below genus 407. Carry this NCBI lineage unchanged. The sequence's strain qualifier does not authorize rewriting the NCBI rank. EXACT identifies the source concept, not a validly published binomial.

The complete [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was inspected earlier in this turn and rechecked for T3. It supplies no T3 species-name or type-deposit attribution. Genus-level nomenclature was not inherited. The legacy taxonomy-browser route was unavailable; successful NCBI structured responses supplied the identity check.

Exact pinned scans found no children, type-material, merged-ID or dropped row for the target.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221930` supports identity, rank, parent, code, empty synonyms and NCBI-only provenance.
- Full native `data/catalog/ncbi_names-0005.jsonl.gz:31398` supplies the exact scientific name and taxid, with empty unique-name field.
- `data/taxa/PATHS.tsv:14421` resolves the slug; `curation/seed_scope.tsv:322205` adds it on 2026-09-13 under its one-source attested rule.
- The 2026-09-13T17:54:04Z seed event agrees with that scope reason and source list. One NAME is a source assertion, not a biological genome or culture-deposit count.

Exact Entrez `txid1035209[Organism:noexp]` returned zero assemblies with phrases-not-found / no-items diagnostics, and one Nuccore UID, 347300706. The full ID list equals the nucleotide query count. The assembly no-hit is bounded to that exact query.

Complete [GenBank metadata for FR869805.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869805.1) identify a 1,335-nt partial 16S rRNA sequence, strain T3, exact taxon 1035209, host Trifolium repens and host leaf surface as isolation source. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. Every feature, source qualifier and reference was read; bases were omitted. No culture-collection qualifier, BioSample, BioProject or assembly is supplied. This is a marker, not a genome.

The explicit reference is Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The full [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml), fetched earlier in this turn, were reread against T3's sequence reference. They confirm a study of phyllosphere communities across hosts, sites and land-use types, not a T3-specific phenotype, locality or growth requirement. The abstract does not name T3; full text and supplements were not inspected.

The name search also found `Methylobacterium sp. T3-YH-2228`, `NCBITaxon:1540490`, at `data/raw/ncbitaxon_taxa.tsv:396840`, `curation/seed_scope.tsv:466057` and `data/catalog/ncbi_names-0009.jsonl.gz:27216`. All three rows were read fully. [Live taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1540490&retmode=xml) and [dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1540490) confirm that separate species-ranked source concept without a synonym bridge to T3.

Exact searches for taxid 1540490 returned zero assemblies with the same diagnostics and one nucleotide UID, 675823557. Complete [KJ922679.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=KJ922679.1) describe a different 581-nt partial 16S marker, strain T3-YH-2228, taxon 1540490, submitted by Lu and Guan on 31 May 2014. Its unpublished study title concerns Panax notoginseng rhizosphere microbes, but the source feature itself gives no host or isolation-source qualifier. No DOI, PMID, culture deposit or assembly is provided. The title is not transferred into a T3 isolation claim. No inspected source equates T3-YH-2228 / KJ922679.1 with T3 / FR869805.1; their shared name fragment and genus do not establish identity.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded T3/T-3 context and target accession searches established no eligible culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit attribution for T3.

Zero strains agrees with the BacDive subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: no exact BacDive row or descendant contributes an entry. This does not imply that the isolate was never cultured. The existing `normalize_culture_identifier` function rejected T3, T-3 and T3-YH-2228 as unsupported bare designations.

The optional FR869805.1 marker link is not a required-representation defect under the current contract; no supported strain entry or eligible SI-DP association was established to receive it. Empty optional biological fields remain appropriate.

The iModulonDB structured adapter ran before browser follow-up and returned 28 datasets without Methylobacterium/Methylorubrum coverage. It is not applicable, not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and inspected evidence scope. Identity and provenance are supported without merging the T3-YH-2228 near-match or promoting a marker to a genome. This pass does not certify full-corpus reproducibility or establish unasserted biological properties.

## Recommended Edits

None required.

Any future marker enrichment belongs in maintained extraction/seeding logic, including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, after explicit identity and a typed non-genome representation are established. Do not edit generated YAML or create deposit equivalence from the T3 fragment. Do not promote SEEDED to REVIEWED or append curation history from this report.

## Follow-up Checks

- Repeat exact taxonomy, complete lineage, status, schema and strict checks on refresh.
- After authorized source/import changes, run full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded comparisons do not replace these gates.
- Require an eligible own-deposit accession and explicit sequence-to-deposit attribution before a StrainInfo link; keep FR869805.1 outside genome counts.
- Inspect the full text and supplements of PMID 22000032 before T3-specific biological enrichment.
- Preserve the distinct T3 and T3-YH-2228 source concepts unless an explicit authoritative equivalence is supplied.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial identifier/label/slug search returned six rows; expanded Methylobacterium/Methylorubrum T3/T-3 context returned those same six. All six distinct rows were read fully using structured TSV and lossless native JSONL decoding. Target FR869805 / 347300706 search returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored and compressed files and remain bounded to these roots.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Same-turn primary PubMed content was reread, not replaced with search snippets. The near-match inspection is identity context, not a completed review or verdict for its own YAML.

Only this new report was written for T3. No YAML/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota was not reopened.
