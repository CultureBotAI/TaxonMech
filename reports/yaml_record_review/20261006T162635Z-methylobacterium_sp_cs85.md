# YAML Record Review: Methylobacterium sp. CS85

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_cs85.yaml`
- Started UTC: 2026-10-06T16:24:11Z
- Finished UTC: 2026-10-06T16:26:35Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035222`, label `Methylobacterium sp. CS85`, SPECIES / BACTERIA. The entire YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. An ignored-independent filename search resolved this target and found no earlier report for its stem.

EXACT grounding, SEEDED status, ten root-first ancestors, code 11, zero BacDive strains, one NCBI NAME attestation and one seed event are present. Synonyms, equivalent xrefs, nomenclature, mappings, genome links, definition, citations, phenotype and causal graph are not asserted.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_cs85.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_cs85.yaml --out /private/tmp/mcs85-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: identity, full lineage, code, attestation, scope and seed-event content match pinned inputs. This does not replace corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just validate-history`, `just qc` and the test suite. No full-corpus pass is claimed.
- No curator-added graph nodes require term validation. The product-check configuration excludes taxonomy fields; their source agreement was manually checked.
- No separate target history artifact was found by ignored-independent filename search. Inline history passed record validation; no focused history substitute was invented.
- No PMID, DOI or quotation is asserted in the YAML. The marker-linked publication below was inspected for completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221943`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035222&retmode=xml) and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035222) agree on exact taxid, label and SPECIES rank. Both structured responses were inspected in full. XML confirms bacterial division, parent 2615210, code 11 and no alternate names. Dataset metadata confirm all ten root-inclusive ancestor IDs; their pinned labels and ranks match the YAML.

The no-rank parent `unclassified Methylobacterium`, below genus 407, is part of the carried NCBI lineage. A sequence strain qualifier does not authorize changing NCBI's rank. EXACT identifies the source concept rather than a validly published binomial.

The [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was previously inspected in full and rechecked for CS85 during this review. No target formal-name or type-deposit attribution was established; genus-level nomenclature was not inherited. The legacy NCBI browser route was unavailable; successful structured responses supplied identity and lineage evidence.

Exact pinned scans found no children, type-material row, merged-ID row or dropped row for this taxid.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221943` supports identity, rank, parent, code, empty synonyms and NCBI-only provenance.
- Complete native `data/catalog/ncbi_names-0005.jsonl.gz:31411` contains the exact scientific name and taxid with an empty unique-name field.
- `data/taxa/PATHS.tsv:14434` resolves the slug; `curation/seed_scope.tsv:322218` adds it on 2026-09-13 under its one-source attested rule.
- The 2026-09-13T17:54:04Z seed event agrees with that scope reason and source list. One NAME is a source assertion, not a genome or deposit count.

Exact Entrez `txid1035222[Organism:noexp]` returned zero assemblies with phrases-not-found / no-items diagnostics and one Nuccore UID, 347300719. The complete nucleotide ID list equals the query count. The assembly no-hit is bounded to that exact query, not universal proof of absence.

Full [GenBank metadata for FR869818.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869818.1) identify a 1,333-nt partial 16S rRNA sequence, strain CS85, exact taxon 1035222, host Cerastium holosteoides and host leaf surface as isolation source. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. Every feature, source qualifier and reference was read; bases were omitted. No culture-collection qualifier, BioSample, BioProject or assembly is supplied. This marker is not a genome.

The explicit reference is Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The complete [PubMed citation and abstract XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml), fetched earlier in this turn, were reread against CS85's reference. They describe a phyllosphere-community study across hosts, locations and land-use types. The abstract does not name CS85 or establish its isolate-specific phenotype, locality or growth requirement. Full text and supplements were not inspected; community results were not transferred to the isolate.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded CS85/CS-85 context and marker-accession searches established no eligible target culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit assertion.

Ten additional numeric search hits were read losslessly in full and excluded:

- `data/bvbrc/bvbrc-0022.jsonl.gz:21683`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20020`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20874` and `data/catalog/gtdb_genomes-0009.jsonl.gz:13251` concern Escherichia coli taxid 562, strain RTP21230st2_B10_RTP21277_210401, GCA/GCF_040925405.1, BV-BRC 562.157446 and BioSample SAMN41035222.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6242` is BV-BRC 1773.18437, Mycobacterium tuberculosis taxid 1773, strain field ERR1035222.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6446` is GCA_010352225.1, Campylobacter jejuni taxid 197, strain 89868 and BioSample SAMN13326912.
- `data/catalog/ncbi_genbank-0018.jsonl.gz:24004` is GCA_020096375.1, Salmonella enterica taxid 28901, strain 1035222001 and BioSample SAMN21554063.
- `data/catalog/allthebacteria.tsv.xz:66145` has SAMEA1035222, Melissococcus plutonius and ERZ3070650. Line 569692 has ERR1035222, SAMEA3558755, Mycobacterium tuberculosis and ERZ3502560. Line 3092432 has SRR31035222, SAMN44339160, Salmonella enterica serovar Enteritidis and ERZ27111471.

These are accession or unrelated strain-number substrings, not CS85 identity evidence. ATB rows were excluded for identity, not merely because one failed HQ filters. No evidence from them was transferred.

Zero strains agrees with the BacDive subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: no exact BacDive row or descendant contributes an entry. This does not imply that the original isolate was never cultured. The existing `normalize_culture_identifier` function rejected CS85 and CS-85 as unsupported bare deposit identifiers.

The optional FR869818.1 marker link is not a required-representation defect under the current contract. No supported strain entry or eligible SI-DP association was established to receive it. Empty optional biological fields remain appropriate.

The structured iModulonDB adapter ran before browser follow-up and returned 28 datasets without Methylobacterium/Methylorubrum coverage. It is not applicable, not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and inspected evidence scope. Identity and provenance are supported without transferring unrelated catalog evidence or treating a marker as a genome. This pass does not certify full-corpus reproducibility or unasserted biological properties.

## Recommended Edits

None required.

Future marker enrichment belongs in maintained extraction/seeding logic, including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, after explicit identity and a typed non-genome representation are established. Generated YAML remains read-only; CS85 alone cannot supply a culture accession or SI-DP.

Do not promote SEEDED to REVIEWED or append curation history from this report.

## Follow-up Checks

- Repeat exact taxonomy, complete lineage, status, schema and strict checks on source refresh.
- After authorized source/import changes, run full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded comparisons do not replace these gates.
- Require an eligible own-deposit identifier and explicit sequence attribution before a StrainInfo link; keep FR869818.1 outside genome counts.
- Inspect the full text and supplements of PMID 22000032 before CS85-specific biological enrichment.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial identifier/label/slug search returned 13 rows, all fully inspected using structured pinned comparisons and lossless native JSONL/TSV decoding. The expanded Methylobacterium/Methylorubrum CS85/CS-85 search returned only the three identity/scope rows. FR869818 / 347300719 returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored and compressed files and remain bounded to these roots.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Same-turn primary PubMed XML was reread; failed browser output and search snippets were not biological evidence.

Only this new report was written for CS85. No YAML/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota was not reopened.
