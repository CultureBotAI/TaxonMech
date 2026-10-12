# YAML Record Review: Methylobacterium sp. M1-22

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_m1_22.yaml`
- Started UTC: 2026-10-06T16:35:55Z
- Finished UTC: 2026-10-06T16:39:40Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035225`, label `Methylobacterium sp. M1-22`, SPECIES / BACTERIA. The entire YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. An ignored-independent filename search resolved the target and found no earlier report for its stem.

EXACT grounding, SEEDED status, ten root-first ancestors, code 11, zero BacDive strains, one NCBI NAME attestation and one seed event are present. Synonyms, equivalent xrefs, nomenclature, mappings, genome links, definition, citations, phenotype and causal graph are not asserted.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_m1_22.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_m1_22.yaml --out /private/tmp/mm122-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: identity, full lineage, code, attestation, scope and seed-event content match pinned inputs. This does not replace corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just validate-history`, `just qc` and the test suite. No full-corpus pass is claimed.
- No curator-added graph nodes require term validation. The product-check configuration excludes taxonomy fields; their source agreement was manually checked.
- No separate target history artifact was found by ignored-independent filename search. Inline history passed record validation; no focused history substitute was invented.
- No PMID, DOI or quotation is asserted in the YAML. The marker-linked publication below was inspected for completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221946`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035225&retmode=xml) and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035225) agree on exact taxid, label and SPECIES rank. Both structured responses were inspected in full. XML confirms bacterial division, parent 2615210, code 11 and no alternate names. Dataset metadata confirm all ten root-inclusive ancestor IDs; the pinned labels and ranks match the YAML.

The no-rank parent `unclassified Methylobacterium`, below genus 407, is part of the carried NCBI lineage. A sequence strain qualifier does not authorize changing NCBI's rank. EXACT identifies the source concept rather than a validly published binomial. The pinned slug correctly preserves the label through the repository's filename representation.

The [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was previously inspected in full and rechecked for M1-22 during this review. No target formal-name or type-deposit attribution was established; genus-level nomenclature was not inherited. The legacy NCBI browser route was unavailable; successful structured responses supplied identity and lineage evidence.

Exact pinned scans found no children, type-material row, merged-ID row or dropped row for this taxid.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221946` supports identity, rank, parent, code, empty synonyms and NCBI-only provenance.
- Complete native `data/catalog/ncbi_names-0005.jsonl.gz:31414` contains the exact scientific name and taxid with an empty unique-name field.
- `data/taxa/PATHS.tsv:14437` resolves the slug; `curation/seed_scope.tsv:322221` adds it on 2026-09-13 under its one-source attested rule.
- The 2026-09-13T17:54:04Z seed event agrees with that scope reason and source list. One NAME is a source assertion, not a genome or deposit count.

Exact Entrez `txid1035225[Organism:noexp]` returned zero assemblies with phrases-not-found / no-items diagnostics and one Nuccore UID, 347300722. The complete nucleotide ID list equals the query count. The assembly no-hit is bounded to that exact query, not universal proof of absence.

Full [GenBank metadata for FR869821.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869821.1) identify a 1,335-nt partial 16S rRNA sequence, strain M1-22, exact taxon 1035225, host Trifolium repens and host leaf surface as isolation source. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. Every feature, source qualifier and reference was read; bases were omitted. No culture-collection qualifier, BioSample, BioProject or assembly is supplied. This marker is not a genome.

The explicit reference is Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The complete [PubMed citation and abstract XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml), fetched earlier in this turn, were reread against M1-22's reference. They describe a phyllosphere-community study across hosts, locations and land-use types. The abstract does not name M1-22 or establish its isolate-specific phenotype, locality or growth requirement. Full text and supplements were not inspected; community results were not transferred to the isolate.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded M1-22/M1 22/M122 context and marker-accession searches established no eligible target culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit assertion. Search spelling variants were leads, not asserted aliases.

Twenty additional numeric search hits were read losslessly in full and excluded:

- Four E. coli rows, taxid 562: `data/bvbrc/bvbrc-0022.jsonl.gz:21679`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20870`, `data/catalog/gtdb_genomes-0016.jsonl.gz:11330` and `data/catalog/ncbi_refseq-0006.jsonl.gz:20016`. They concern strain RTP21230st2_F1_RTP21230_210325, GCA/GCF_040925325.1, BV-BRC 562.157442 and BioSample SAMN41035225.
- Five Pseudomonas aeruginosa rows, taxid 287 in the taxonomy-bearing records: `data/bvbrc/bvbrc-0016.jsonl.gz:22047`, `data/catalog/ncbi_refseq-0000.jsonl.gz:30444`, `data/catalog/gtdb_genomes-0007.jsonl.gz:28559`, `data/catalog/ncbi_genbank-0000.jsonl.gz:36039` and `data/gold/analyses.jsonl.gz:101320`. They concern Pae_CF67.08r, GCA/GCF_001035225.1, BV-BRC 287.1612 and BioSample SAMN03566382. The GOLD row supplies Ga0158541, Gp0189772 and GCA_001035225.1, with an empty organism-GOLD field. It supplies no M1-22 culture-deposit or organism chain.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6250` is BV-BRC 1773.18444, Mycobacterium tuberculosis taxid 1773, strain field ERR1035225.
- `data/catalog/ncbi_genbank-0037.jsonl.gz:25649` is GCA_041035225.1, Klebsiella pneumoniae taxid 573, strain zj02021, BioSample SAMN37542637.
- `data/catalog/ncbi_genbank-0018.jsonl.gz:21522` is GCA_020045025.1, Salmonella enterica taxid 28901, strain 1035225001, BioSample SAMN21475426.
- `data/catalog/ncbi_genbank-0026.jsonl.gz:19635` is GCA_028372175.1, Amylibacter sp. taxid 1872504, isolate AH-273-B18, BioSample SAMN29366136; its genome length is 1035225.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6448` is GCA_010352255.1, Campylobacter jejuni taxid 197, strain PNUSAC013410, BioSample SAMN13327262.
- `data/catalog/ncbi_genbank-0047.jsonl.gz:6721` and `data/catalog/ncbi_refseq_historical-0001.jsonl.gz:38989` concern Vibrio parahaemolyticus taxid 670, strain VP20054, GCA/GCF_051035225.1 and BioSample SAMN46338793. The historical RefSeq row is marked suppressed, not a current M1-22 assembly.
- `data/catalog/ncbi_genbank-0019.jsonl.gz:18993` is GCA_021035225.1, E. coli taxid 562, isolate PP58, BioSample SAMEA8581603.
- `data/catalog/ncbi_genbank-0066.jsonl.gz:46397` is GCA_983090895.1, uncultured Candidatus Poseidoniales archaeon taxid 274854, BioSample SAMEA122364720; its ungapped length is 1035225.
- `data/catalog/allthebacteria.tsv.xz:569695` has ERR1035225, SAMEA3558758, Mycobacterium tuberculosis and ERZ3502558. Line 3103615 has SAMN44572436, SRR31220724 and ERZ27066186; its source scientific name is Salmonella enterica and Sylph species is Salmonella houtenae. The matching digits occur within its SeqKit sum.

These are accession, strain-number or checksum substrings, or assembly metrics, not M1-22 identity evidence. Available FASTAs and related source IDs cannot replace an eligible own-deposit association. None of this unrelated evidence was transferred.

Zero strains agrees with the BacDive subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: no exact BacDive row or descendant contributes an entry. It does not imply that the original isolate was never cultured. The existing `normalize_culture_identifier` function rejected M1-22, M1 22 and M122 as unsupported bare deposit identifiers.

The optional FR869821.1 marker link is not a required-representation defect under the current contract. No supported strain entry or eligible SI-DP association was established to receive it. Empty optional biological fields remain appropriate.

The structured iModulonDB adapter ran before browser follow-up and returned 28 datasets without Methylobacterium/Methylorubrum coverage. It is not applicable, not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and inspected evidence scope. Identity and provenance are supported without transferring unrelated catalog evidence or treating a marker as a genome. This pass does not certify full-corpus reproducibility or unasserted biological properties.

## Recommended Edits

None required.

Future marker enrichment belongs in maintained extraction/seeding logic, including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, after explicit identity and a typed non-genome representation are established. Generated YAML remains read-only; M1-22 alone cannot supply a culture accession or SI-DP.

Do not promote SEEDED to REVIEWED or append curation history from this report.

## Follow-up Checks

- Repeat exact taxonomy, complete lineage, status, schema and strict checks on source refresh.
- After authorized source/import changes, run full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded comparisons do not replace these gates.
- Require an eligible own-deposit identifier and explicit sequence attribution before a StrainInfo link; keep FR869821.1 outside genome counts.
- Inspect the full text and supplements of PMID 22000032 before M1-22-specific biological enrichment.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial identifier/label/slug search returned 23 rows, all fully inspected using structured pinned comparisons and lossless native JSONL/TSV decoding. The expanded Methylobacterium/Methylorubrum M1-22 context search, allowing optional spaces/hyphens/underscores around its numbers, returned only the three identity/scope rows. FR869821 / 347300722 returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored and compressed files and remain bounded to these roots.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Same-turn primary PubMed XML was reread; failed browser output and search snippets were not biological evidence. Other taxa appearing in numeric collisions were not separately reviewed as targets.

Only this new report was written for M1-22. No YAML/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota was not reopened.
