# YAML Record Review: Methylobacterium sp. T43

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_t43.yaml`
- Started UTC: 2026-10-06T15:37:49Z
- Finished UTC: 2026-10-06T15:39:44Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035210`, label `Methylobacterium sp. T43`, SPECIES / BACTERIA. The entire YAML was read before judgement and confirmed byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. An ignored-independent filename search resolved this target and found no earlier report for its stem.

The record has EXACT grounding, SEEDED status, ten root-first ancestors, genetic code 11, zero BacDive strains, one NCBI NAME attestation and one seed event. It asserts no synonyms, equivalent xrefs, nomenclature, taxonomy mappings, genome links, definition, citations, phenotype or causal graph.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_t43.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_t43.yaml --out /private/tmp/mt43-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: identity, entire lineage, code, attestation, scope and seed-event content match pinned inputs. This is not corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc` and the test suite. No full-corpus pass is claimed.
- No curator-added graph nodes require term validation. The product-check configuration excludes taxonomy fields, whose agreement was manually checked here.
- No separate target history artifact was found by the ignored-independent filename search. Inline history passed record validation; no external validator was run against an invented artifact.
- No PMID, DOI or quotation is asserted by this YAML. The marker-linked publication below was checked as completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221931`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035210&retmode=xml) and [NCBI taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035210) agree on identifier, exact label and SPECIES rank. Both live responses were read in full. XML confirms bacterial division, parent 2615210, code 11 and no alternate names; dataset metadata confirm all ten root-inclusive ancestor IDs. Their pinned labels/ranks match the YAML.

The no-rank parent `unclassified Methylobacterium`, below genus 407, belongs in the carried NCBI lineage. A sequence strain qualifier does not authorize changing NCBI's rank, and EXACT identifies the source concept rather than claiming a validly published binomial.

The complete [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was inspected earlier in this turn and rechecked for T43. No target formal-name or type-deposit attribution was established. Genus-level nomenclature was not inherited. The legacy taxonomy-browser route was unavailable; successful structured NCBI responses supplied identity and lineage evidence.

Pinned exact scans found no children, type-material row, merged-ID row or dropped row.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221931` supports identity, rank, parent, code, empty synonyms and NCBI-only provenance.
- Complete native `data/catalog/ncbi_names-0005.jsonl.gz:31399` contains the exact scientific name and taxid with an empty unique-name field.
- `data/taxa/PATHS.tsv:14422` resolves the slug. `curation/seed_scope.tsv:322206` adds it on 2026-09-13 under its one-source attested rule.
- The 2026-09-13T17:54:04Z seed event matches that scope and source list. The attestation counts one NAME, not a genome or culture deposit.

Exact Entrez `txid1035210[Organism:noexp]` searches returned zero assemblies with phrases-not-found / no-items diagnostics, and one Nuccore UID, 347300707. The complete nucleotide ID list equals the query count. The assembly no-hit is bounded to that exact query, not universal proof of absence.

Full [GenBank metadata for FR869806.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869806.1) identify a 1,335-nt partial 16S rRNA sequence, strain T43, exact taxon 1035210, host Trifolium repens and host leaf surface as isolation source. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. Every feature, source qualifier and reference was read; sequence bases were omitted. There is no culture-collection qualifier, BioSample, BioProject or assembly. This is a marker, not a genome.

The sequence cites Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The complete [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml), fetched earlier in this turn, were reread against T43's explicit reference. They confirm a phyllosphere-community study across plant hosts, locations and land-use types. The abstract does not name T43 or establish its isolate-specific phenotype, locality or growth requirement. Full text and supplements were not inspected; community-level results were not transferred to the isolate.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded T43/T-43 context and sequence-accession searches established no eligible target culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit assertion.

Zero strains matches the BacDive subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: no exact row or descendant contributes an entry. It does not imply that the original isolate was never cultured. The existing `normalize_culture_identifier` function was run on T43 and T-43; both are unsupported bare deposit keys.

The optional FR869806.1 link is not a required-representation defect under the current contract. No supported strain entry or eligible SI-DP association was established to receive it. Empty optional biological fields remain appropriate.

The structured iModulonDB adapter ran before browser follow-up and returned 28 datasets without Methylobacterium/Methylorubrum coverage. It is not applicable, not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and inspected evidence scope. Exact identity and provenance are supported without converting the 16S marker to a genome or inventing a culture deposit. This pass does not certify full-corpus reproducibility or unasserted biological properties.

## Recommended Edits

None required.

Future marker enrichment belongs in maintained extraction/seeding logic, including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, only after explicit identity and a typed non-genome representation are established. Generated YAML remains read-only; the bare T43 designation cannot supply a culture accession or SI-DP.

Do not promote SEEDED to REVIEWED or append curation history from this report.

## Follow-up Checks

- Repeat exact taxonomy, complete lineage, status, schema and strict checks on refresh.
- After authorized source/import changes, run full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded comparisons do not replace these gates.
- Require an eligible own-deposit identifier and explicit sequence attribution before a StrainInfo link; keep FR869806.1 outside genome counts.
- Inspect the full text and supplements of PMID 22000032 before proposing T43-specific biological enrichment.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial taxid/label/slug and expanded Methylobacterium/Methylorubrum T43/T-43 context searches each returned the same three identity/scope rows. All three distinct rows were read fully through structured pinned comparisons and lossless native JSONL decoding. FR869806 / 347300707 returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored and compressed files and remain bounded to these roots.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Same-turn primary PubMed content was reread; failed browser output and search snippets were not biological evidence.

Only this new report was written for this target. No YAML/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota was not reopened.
