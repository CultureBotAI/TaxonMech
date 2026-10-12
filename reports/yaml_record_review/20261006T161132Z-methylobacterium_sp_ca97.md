# YAML Record Review: Methylobacterium sp. CA97

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_ca97.yaml`
- Started UTC: 2026-10-06T16:08:45Z
- Finished UTC: 2026-10-06T16:11:32Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035218`, label `Methylobacterium sp. CA97`, SPECIES / BACTERIA. The entire YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. An ignored-independent filename search resolved this target without an existing report for its stem.

EXACT grounding, SEEDED status, ten root-first ancestors, code 11, zero BacDive strains, one NCBI NAME attestation and one seed event are present. No synonyms, equivalent xrefs, nomenclature, taxonomy mappings, genomes, definition, citations, phenotype or causal graph are asserted.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_ca97.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_ca97.yaml --out /private/tmp/mca97-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: identity, full lineage, code, attestation, scope and seed-event content match pinned inputs. This does not replace corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just validate-history`, `just qc` and the test suite. No full-corpus pass is claimed.
- No curator-added graph nodes require term validation. The product-check configuration excludes taxonomy fields; their inventory agreement was manually checked.
- No separate target history artifact was found by the ignored-independent filename search. Inline history passed record validation; no focused history substitute was invented.
- No PMID, DOI or quotation is asserted in the YAML. The marker-linked publication below was inspected for completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221939`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035218&retmode=xml) and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035218) agree on exact taxid, label and SPECIES rank. Both structured responses were inspected in full. XML confirms bacterial division, parent 2615210, code 11 and no alternate names. Dataset metadata confirm all ten root-inclusive ancestor IDs; the pinned labels and ranks match the YAML.

The no-rank parent `unclassified Methylobacterium`, below genus 407, is part of NCBI's carried lineage. A strain-qualified sequence does not justify changing NCBI's rank. EXACT identifies the source concept rather than a validly published binomial.

The [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was previously inspected in full and rechecked for CA97 in this review. No target formal-name or type-deposit attribution was established; genus-level nomenclature was not inherited. The legacy taxonomy-browser route was unavailable; successful structured NCBI responses supplied identity and lineage evidence.

Exact pinned scans found no children, type-material row, merged-ID row or dropped row for this taxid.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221939` supports identity, rank, parent, code, empty synonyms and NCBI-only provenance.
- Complete native `data/catalog/ncbi_names-0005.jsonl.gz:31407` contains the exact scientific name and taxid, with an empty unique-name field.
- `data/taxa/PATHS.tsv:14430` resolves the slug; `curation/seed_scope.tsv:322214` adds it on 2026-09-13 under the one-source attested rule.
- The 2026-09-13T17:54:04Z seed event agrees with that scope reason and source list. One NAME is a source assertion, not a genome or culture-deposit count.

Exact Entrez `txid1035218[Organism:noexp]` returned zero assemblies with phrases-not-found / no-items diagnostics and one Nuccore UID, 347300715. The complete nucleotide ID list equals the query count. The assembly result is bounded to that exact query, not universal proof of absence.

Full [GenBank metadata for FR869814.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869814.1) identify a 1,334-nt partial 16S rRNA sequence, strain CA97, exact taxon 1035218, host Cerastium holosteoides and host leaf surface as isolation source. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. Every feature, source qualifier and reference was inspected; bases were omitted. No culture-collection qualifier, BioSample, BioProject or assembly is supplied. This marker is not a genome.

The explicit reference is Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The complete [PubMed citation and abstract XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml), fetched earlier in this turn, were reread against CA97's reference. They describe a phyllosphere-community study across hosts, locations and land-use types. The abstract does not name CA97 or establish its isolate-specific phenotype, collection locality or growth requirement. Full text and supplements were not inspected; community results were not transferred to the isolate.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded CA97/CA-97 context and marker-accession searches established no eligible target culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit assertion.

Ten additional numeric search hits were read losslessly in full and excluded:

- `data/bvbrc/bvbrc-0022.jsonl.gz:21689`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20879`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20025` and `data/catalog/gtdb_genomes-0014.jsonl.gz:16524` share BioSample SAMN41035218. They concern Escherichia coli, NCBI taxid 562, strain RTP21230st1_A3_RTP21230_210325, GCA/GCF_040925495.1 and BV-BRC 562.157452, not CA97.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6444` is GCA_010352185.1, Campylobacter jejuni taxid 197, strain FSIS12027775 and BioSample SAMN13828702. The matching digits occur within the assembly accession.
- `data/catalog/allthebacteria.tsv.xz:66140` has SAMEA1035218, Melissococcus plutonius, rejected ASM_LEN status and no available FASTA.
- ATB lines 569688, 1715450, 1715452 and 3092434 match ERR1035218, SRR10352181, SRR10352180 and SRR31035218 respectively. Their samples are SAMEA3558751, SAMN13134355, SAMN13134357 and SAMN44339162; their reported organisms are Mycobacterium tuberculosis and three Salmonella enterica serovars. No CA97 identity bridge is supplied.

None of those source records supports a CA97 genome link. A substring match cannot replace exact taxonomy, a whole BioSample accession or an eligible own-deposit association.

Zero strains agrees with the BacDive subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: no exact row or descendant contributes a BacDive entry. This does not imply that the original isolate was never cultured. The existing `normalize_culture_identifier` function rejected both CA97 and CA-97 as unsupported bare deposit identifiers.

The optional FR869814.1 marker link is not a required-representation defect under the current contract. No supported strain entry or eligible SI-DP association was established to receive it. Empty optional biological fields remain appropriate.

The structured iModulonDB adapter ran before browser follow-up and returned 28 datasets without Methylobacterium/Methylorubrum coverage. It is not applicable, not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and inspected evidence scope. Identity and provenance are supported without transferring unrelated catalog evidence or treating a marker as a genome. This pass does not certify full-corpus reproducibility or unasserted biological properties.

## Recommended Edits

None required.

Future marker enrichment belongs in maintained extraction/seeding logic, including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, after explicit identity and a typed non-genome representation are established. Generated YAML remains read-only; CA97 alone cannot supply a culture accession or SI-DP.

Do not promote SEEDED to REVIEWED or append curation history from this report.

## Follow-up Checks

- Repeat exact taxonomy, complete lineage, status, schema and strict checks on source refresh.
- After authorized source/import changes, run full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded comparisons do not replace these gates.
- Require an eligible own-deposit identifier and explicit sequence attribution before a StrainInfo link; keep FR869814.1 outside genome counts.
- Inspect the full text and supplements of PMID 22000032 before CA97-specific biological enrichment.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial identifier/label/slug search returned 13 rows, all fully inspected using structured pinned comparisons and lossless native JSONL/TSV decoding. The expanded Methylobacterium/Methylorubrum CA97/CA-97 search returned only the three identity/scope rows. FR869814 / 347300715 returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored and compressed files and remain bounded to these roots.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Same-turn primary PubMed XML was reread; failed browser responses and search snippets were not biological evidence.

Only this new report was written for CA97. No YAML/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota was not reopened.
