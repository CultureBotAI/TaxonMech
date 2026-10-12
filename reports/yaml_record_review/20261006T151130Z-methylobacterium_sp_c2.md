# YAML Record Review: Methylobacterium sp. C2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c2.yaml`
- Started UTC: 2026-10-06T15:09:33Z
- Finished UTC: 2026-10-06T15:11:30Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035203`, label `Methylobacterium sp. C2`, SPECIES / BACTERIA. The full YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD is `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record has EXACT grounding, SEEDED status, code 11, ten ancestors, zero BacDive strains, one NCBI NAME attestation and one seed event. It asserts no synonyms, equivalent xrefs, nomenclature, taxonomy mappings, genome/sequence links, definition, citations, phenotype or causal graph. C2 here is the exact NCBI concept, not a general culture-collection accession.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c2.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c2.yaml --out /private/tmp/mc2-strict.tsv`: one file, zero ERROR rows. The actual output TSV was read; it contains only the header.
- PASS, bounded manual comparison: identity, every lineage entry, code, attestation, scope and seed-event text agree with pinned inputs. This is not a focused substitute for corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc` and the test suite. Their success is not claimed.
- No curator-added ontology node needs validation; `conf/id_label_targets.yaml` excludes taxonomy fields and delegates inventory correspondence to corpus reproduction.
- No separate target history file was found by an ignored-independent filename search. Inline history passed schema/strict checks. No external history artifact was invented or validated.
- The YAML contains no DOI, PMID or quoted evidence. The sequence-linked publication was inspected as completeness context, not as support for an assertion absent from the record.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221924`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035203&retmode=xml) and [NCBI dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035203) agree on taxid, label and SPECIES rank. Both live responses were read fully. XML confirms bacterial division, parent 2615210, genetic code 11 and no alternate names. Dataset metadata supply all ten root-inclusive ancestor IDs; the pinned labels and ranks match the complete YAML lineage.

The parent is the no-rank `unclassified Methylobacterium` grouping below genus 407, not a named species to be substituted. The sequence's C2 strain qualifier does not change this NCBI rank. EXACT refers to the NCBI concept rather than valid publication of a binomial.

The complete [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was inspected earlier in this turn and checked specifically for C2. It names M. organophilum as type species, not this isolate. No genus nomenclature or type status was inherited.

A broader designation search found `Methylobacterium sp. MMA-C-2`, `NCBITaxon:692281`, in complete pinned backbone, native-name and scope rows. This is a distinct label and taxid, not a C2 synonym or supported genome join. Its source rows were read for disambiguation only; its review was not reopened.

No target children occur in the pinned backbone; exact type-material, merged-ID and dropped-row checks also returned no target entries. The legacy NCBI Taxonomy browser route was inaccessible, so identity verification uses the two successful structured responses.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221924` supplies the target identity, parent, code, empty synonym fields and NCBI-only source.
- Complete `data/catalog/ncbi_names-0005.jsonl.gz:31392` contains the scientific name, exact taxid and empty unique-name field.
- `data/taxa/PATHS.tsv:14415` resolves the slug. `curation/seed_scope.tsv:322199` adds the target on 2026-09-13 under its one-source attested rule.
- The 2026-09-13T17:54:04Z inline event agrees with the scope reason and source list. The source count is one NAME, not one genome or biological strain.
- The MMA-C-2 candidate is explicitly taxid 692281 in `data/raw/ncbitaxon_taxa.tsv:162426`, `data/catalog/ncbi_names-0004.jsonl.gz:13185` and `curation/seed_scope.tsv:269250`. All three rows were read fully.

The initial numeric search also matched `data/catalog/gtdb_genomes-0006.jsonl.gz:45511`. The entire native record identifies `RS_GCF_001353415.1` as Staphylococcus aureus, taxid 1280, strain USFL110. The number 1035203 occurs in `ncbi_contig_n50`, not a taxonomic field. It is a numeric collision and supplies no target GTDB evidence.

Exact Entrez queries `txid1035203[Organism:noexp]` returned zero assemblies, with no-items / phrases-not-found diagnostics, and one nucleotide UID, 347300700. The returned nucleotide list was complete relative to the query's count. The assembly no-hit is bounded to that exact query, not universal genome absence.

Full [GenBank metadata for FR869799.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869799.1) identify a 1,335-nt partial 16S rRNA sequence for strain C2 and taxon 1035203. Its source names host leaf surface and Cerastium holosteoides. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. There is no culture-collection qualifier, BioSample, BioProject or assembly in the inspected metadata. All feature/source/reference metadata were read; bases were omitted. A partial rRNA sequence must not be counted as a genome.

FR869799.1 cites Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The complete [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml), fetched in this turn, were reread for this exact citation. The paper studies phyllosphere communities across hosts, locations and land-use regimes; its abstract does not identify C2 or prove a C2-specific phenotype, sampling location or growth requirement. Full text and supplements were not inspected. Community findings are not reassigned to this isolate.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive identity, expanded designation and sequence-accession searches found no eligible target deposit, genome-source assertion or explicit StrainInfo sequence-to-own-deposit chain.

Zero listed strains follows the BacDive-subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: no exact BacDive row or descendant can contribute an entry. It does not imply that the original isolate was uncultured. The existing culture normalizer rejects both C2 and C-2 as unqualified designations.

Absence of an FR869799.1 link is not a required-representation defect under the present contract. No supported existing strain entry or eligible SI-DP association was established to host that optional non-genome marker. Future enrichment requires a maintained import path with explicit identity; a shared C2 substring is insufficient.

The iModulonDB dataset adapter ran before web follow-up and returned 28 datasets without Methylobacterium or Methylorubrum coverage. It is not applicable and supplies no negative biological evidence. Optional definition, phenotype and graph slots may remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and inspected evidence scope. The YAML preserves the supported exact NCBI identity and does not borrow the MMA-C-2 concept, the unrelated Staphylococcus genome or community-level phenotypes.

This pass is not a full-corpus reproduction result and does not validate unasserted biological properties.

## Recommended Edits

None required for this record.

If later evidence permits sequence enrichment, use maintained source extraction and seeding logic, retain FR869799.1 as a typed non-genome marker, and preserve explicit identity provenance. Do not join on bare C2, a taxid-like statistic or a designation substring. Generated YAML must remain read-only.

Do not promote SEEDED to REVIEWED or append a curation-history event from this report.

## Follow-up Checks

- On source refresh, repeat exact taxonomy/lineage/status comparisons and the target schema/strict commands.
- After an authorized importer or source change, run actual `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; manual target comparisons do not replace these gates.
- Require a supported own-deposit identifier and explicit sequence attribution for a StrainInfo link; keep markers outside genome counts.
- Keep taxid 1035203 distinct from MMA-C-2 taxid 692281. Match numeric IDs by source field, not arbitrary text occurrence.
- Inspect full text and supplements of PMID 22000032 before proposing isolate-specific ecological or phenotype claims.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial taxid/name/slug query returned four rows, including the unrelated GTDB numeric collision. Expanded Methylobacterium/Methylorubrum C2/C-2 context searches returned six rows, adding the three MMA-C-2 candidates. All seven distinct rows were read completely via structured pinned comparisons and lossless native/TSV decoding. A separate FR869799 / 347300700 search returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored files but are bounded to these sources.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. NCBI structured taxonomy, sequence search and full metadata supplied live evidence. The LPSN page and same-paper PubMed response already inspected during this turn were rechecked for C2. Failed browser output and search snippets were not used as biological evidence.

No YAML/code/generated-page edits, history events, review-status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota reviews were not reopened.

