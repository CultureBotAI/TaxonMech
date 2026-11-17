# YAML Record Review: Methylobacterium sp. T13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_t13.yaml`
- Started UTC: 2026-10-06T15:47:40Z
- Finished UTC: 2026-10-06T15:49:31Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035213`, label `Methylobacterium sp. T13`, SPECIES / BACTERIA. The entire YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. An ignored-independent filename search found this exact target and no earlier report for its stem.

EXACT grounding, SEEDED status, ten root-first ancestors, genetic code 11, zero BacDive strains, one NCBI NAME attestation and one seed event are present. Synonyms, equivalent xrefs, nomenclature, taxonomy mappings, genome links, definition, citations, phenotype and causal graph are not asserted.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_t13.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_t13.yaml --out /private/tmp/mt13-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: identity, full lineage, code, attestation, scope and seed-event content match pinned inputs. This does not replace corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc` and the test suite. No full-corpus pass is claimed.
- No curator-added graph nodes need term validation. The product-check configuration excludes taxonomy fields; their inventory agreement was manually checked here.
- No separate target history artifact was found by the ignored-independent filename search. Inline history passed record validation; no external validator was run against an invented artifact.
- The YAML asserts no PMID, DOI or quotation. The marker-linked publication below was inspected for completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221934`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035213&retmode=xml) and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035213) agree on exact identifier, label and SPECIES rank. Both live responses were inspected in full. XML confirms bacterial division, parent 2615210, code 11 and no alternate names. Dataset metadata confirm all ten root-inclusive ancestor IDs; their pinned labels/ranks match the YAML.

The no-rank parent `unclassified Methylobacterium`, below genus 407, belongs in the carried NCBI lineage. A sequence strain qualifier does not authorize changing the NCBI rank. EXACT identifies the source concept, not a validly published binomial.

The [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was previously inspected in full and rechecked for T13 in this review. No target formal-name or type-deposit attribution was established. Genus-level nomenclature was not inherited. The legacy taxonomy-browser route was unavailable; successful structured NCBI responses supplied identity and lineage evidence.

Exact pinned scans found no children, type-material row, merged-ID row or dropped row for this target.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221934` supports identity, rank, parent, code, empty synonyms and NCBI-only provenance.
- Complete native `data/catalog/ncbi_names-0005.jsonl.gz:31402` contains the exact scientific name and taxid with an empty unique-name field.
- `data/taxa/PATHS.tsv:14425` resolves the slug. `curation/seed_scope.tsv:322209` adds it on 2026-09-13 under its one-source attested rule.
- The 2026-09-13T17:54:04Z seed event agrees with that scope reason and source list. One NAME is a source assertion, not a genome or culture-deposit count.

Exact Entrez `txid1035213[Organism:noexp]` returned zero assemblies with phrases-not-found / no-items diagnostics, and one Nuccore UID, 347300710. The complete nucleotide ID list equals the query count. The assembly no-hit is bounded to that exact query, not universal proof of absence.

Complete [GenBank metadata for FR869809.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869809.1) identify a 1,335-nt partial 16S rRNA sequence, strain T13, exact taxon 1035213, host Trifolium repens and host leaf surface as isolation source. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. Every feature, source qualifier and reference was read; bases were omitted. No culture-collection qualifier, BioSample, BioProject or assembly is supplied. This is a marker, not a genome.

Its explicit reference is Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The complete [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml), fetched earlier in this turn, were reread against T13's sequence reference. They confirm a phyllosphere-community study across plant hosts, locations and land-use types. The abstract does not name T13 or establish its isolate-specific phenotype, locality or growth requirement. Full text and supplements were not inspected; community-level results were not transferred to T13.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded T13/T-13 context and marker-accession searches established no eligible culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit assertion for this target.

Zero strains agrees with the BacDive subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: no exact BacDive row or descendant contributes an entry. This does not imply that the original isolate was never cultured. The existing `normalize_culture_identifier` function rejected both T13 and T-13 as bare, unsupported deposit identifiers.

The optional FR869809.1 marker link is not a required-representation defect under the current contract. No supported strain entry or eligible SI-DP association was established to receive it. Empty optional biological fields remain appropriate.

The structured iModulonDB adapter ran before browser follow-up and returned 28 datasets without Methylobacterium/Methylorubrum coverage. It is not applicable, not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and inspected evidence scope. Exact identity and provenance are supported without treating the marker as a genome or inventing a culture-deposit association. This pass does not certify full-corpus reproducibility or unasserted biological properties.

## Recommended Edits

None required.

Future marker enrichment belongs in maintained extraction/seeding logic, including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, after explicit identity and a typed non-genome representation are established. Generated YAML remains read-only; the bare T13 designation cannot supply a culture accession or SI-DP.

Do not promote SEEDED to REVIEWED or append curation history from this report.

## Follow-up Checks

- Repeat exact taxonomy, complete lineage, status, schema and strict checks on source refresh.
- After authorized source/import changes, run full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded comparisons do not replace these gates.
- Require an eligible own-deposit identifier and explicit sequence attribution before a StrainInfo link; keep FR869809.1 outside genome counts.
- Inspect the full text and supplements of PMID 22000032 before T13-specific biological enrichment.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial identifier/label/slug and expanded Methylobacterium/Methylorubrum T13/T-13 context searches each returned the same three identity/scope rows. All three distinct candidates were read fully through structured pinned comparisons and lossless native JSONL decoding. FR869809 / 347300710 returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored and compressed files and remain bounded to these roots.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. The same-turn PubMed response was reread; failed browser output and search snippets were not biological evidence.

Only this new report was written for T13. No YAML/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota was not reopened.
