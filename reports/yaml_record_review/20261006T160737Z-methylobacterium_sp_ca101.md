# YAML Record Review: Methylobacterium sp. CA101

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_ca101.yaml`
- Started UTC: 2026-10-06T16:02:31Z
- Finished UTC: 2026-10-06T16:07:37Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035217`, label `Methylobacterium sp. CA101`, SPECIES / BACTERIA. The entire YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. An ignored-independent report-filename search found no earlier report for this stem.

The record carries EXACT grounding, SEEDED status, ten root-first ancestors, genetic code 11, zero BacDive strains, one NCBI NAME attestation and one seed event. Synonyms, equivalent xrefs, nomenclature, mappings, genome links, definition, citations, phenotype and causal graph are not asserted.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_ca101.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_ca101.yaml --out /private/tmp/mca101-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: identity, full lineage, code, attestation, scope and seed-event content match the pinned inputs. This is not a substitute for corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc` and the test suite. No full-corpus pass is claimed.
- No curator-added graph nodes require term validation. The product-check configuration excludes taxonomy fields; their source agreement was checked manually.
- No separate target history artifact was found by the ignored-independent filename search. Inline history passed record validation. Full-corpus `just validate-history` was not run, and no focused substitute was invented.
- The YAML asserts no DOI, PMID or quotation. The marker-linked publication below was inspected for completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221938`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035217&retmode=xml) and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035217) agree on the exact identifier, label and SPECIES rank. Both structured responses were inspected in full. XML confirms bacterial division, parent 2615210, code 11 and no alternate names. Dataset metadata confirm all ten root-inclusive ancestor IDs; their pinned labels and ranks agree with the YAML.

The no-rank parent `unclassified Methylobacterium`, below genus 407, is part of the carried NCBI lineage. A strain qualifier on a sequence does not authorize changing the NCBI rank. EXACT identifies the source concept, not a validly published binomial.

The [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was previously inspected in full and rechecked for CA101 during this review. No target formal-name or type-deposit attribution was established; genus-level nomenclature was not inherited. The legacy NCBI taxonomy-browser route was unavailable; successful structured NCBI responses supplied identity and lineage evidence.

Exact pinned scans found no children, type-material row, merged-ID row or dropped row for this taxid.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221938` supports identity, rank, parent, genetic code, empty synonyms and NCBI-only provenance.
- Complete native `data/catalog/ncbi_names-0005.jsonl.gz:31406` contains the exact scientific name and taxid with an empty unique-name field.
- `data/taxa/PATHS.tsv:14429` resolves the slug. `curation/seed_scope.tsv:322213` adds it on 2026-09-13 under its one-source attested rule.
- The 2026-09-13T17:54:04Z seed event agrees with that scope reason and source list. One NAME is a source assertion, not a genome or culture-deposit count.

Exact Entrez `txid1035217[Organism:noexp]` returned zero assemblies with phrases-not-found / no-items diagnostics and one Nuccore UID, 347300714. The complete nucleotide ID list equals the query count. The assembly no-hit is bounded to that exact query, not universal evidence of absence.

Full [GenBank metadata for FR869813.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869813.1) identify a 1,334-nt partial 16S rRNA sequence, strain CA101, exact taxon 1035217, host Cerastium holosteoides and host leaf surface as isolation source. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. Every feature, source qualifier and reference was read; bases were omitted. No culture-collection qualifier, BioSample, BioProject or assembly is supplied. This marker is not a genome.

The explicit reference is Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. Fresh [PubMed citation and abstract XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml) were read completely. They describe a phyllosphere-community study across hosts, locations and land-use types. The abstract does not name CA101 or establish its isolate-specific phenotype, collection locality or growth requirement. Full text and supplements were not inspected; community-level results were not transferred to CA101.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded CA101/CA-101 context and marker-accession searches established no eligible target culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit assertion.

The additional native GenBank search hit was inspected losslessly in full: `data/catalog/ncbi_genbank-0063.jsonl.gz:16495` is GCA_964419425.1, isolate SRP287540_co1_250, uncultured Candidatus Saccharibacteria bacterium, taxid 179883, BioSample SAMEA117286853 and project PRJEB82487. Its ungapped genome length is 1035217. This numeric collision does not associate it with CA101, and none of its evidence was transferred.

Zero strains agrees with the BacDive subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: no exact BacDive row or descendant contributes an entry. It does not imply that the source isolate was never cultured. The existing `normalize_culture_identifier` function rejected both CA101 and CA-101 as unsupported bare deposit identifiers.

The optional FR869813.1 marker link is not a required-representation defect under the current contract. No supported strain entry or eligible SI-DP association was established to receive it. Empty optional biological fields remain appropriate.

The structured iModulonDB adapter ran before browser follow-up and returned 28 datasets without Methylobacterium/Methylorubrum coverage. It is not applicable, not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and inspected evidence scope. Exact identity and provenance are supported without promoting a marker to a genome or inventing a culture-deposit association. This pass does not certify full-corpus reproducibility or unasserted biological properties.

## Recommended Edits

None required.

Future marker enrichment belongs in maintained extraction/seeding logic, including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, after explicit identity and a typed non-genome representation are established. Generated YAML remains read-only. CA101 alone cannot supply a culture accession or SI-DP.

Do not promote SEEDED to REVIEWED or append curation history from this report.

## Follow-up Checks

- Repeat exact taxonomy, complete lineage, status, schema and strict checks on source refresh.
- After authorized source/import changes, run full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded comparisons do not replace these gates.
- Require an eligible own-deposit identifier and explicit sequence attribution before a StrainInfo link; keep FR869813.1 outside genome counts.
- Inspect the full text and supplements of PMID 22000032 before CA101-specific biological enrichment.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial identifier/label/slug search returned four rows, all fully inspected using structured pinned comparisons and lossless native JSONL decoding. The expanded Methylobacterium/Methylorubrum CA101/CA-101 search returned only the three identity/scope rows. FR869813 / 347300714 returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored and compressed files and remain bounded to these roots.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. The PubMed HTML route returned only a footer; successful primary XML, not that HTML or search snippets, supplied publication evidence.

Only this new report was written for CA101. No YAML/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota was not reopened.

