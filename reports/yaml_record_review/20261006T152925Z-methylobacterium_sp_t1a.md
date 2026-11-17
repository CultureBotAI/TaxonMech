# YAML Record Review: Methylobacterium sp. T1a

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_t1a.yaml`
- Started UTC: 2026-10-06T15:24:44Z
- Finished UTC: 2026-10-06T15:29:25Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035207`, label `Methylobacterium sp. T1a`, SPECIES / BACTERIA. The entire YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

EXACT grounding, SEEDED status, ten root-first ancestors, genetic code 11, zero BacDive strains, one NCBI NAME attestation and one seed event are present. There are no synonyms, equivalent xrefs, nomenclature, taxonomy mappings, genome links, definition, citations, phenotype assertions or causal graph. This review concerns the exact taxid, not every use of the short designation T1a.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_t1a.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_t1a.yaml --out /private/tmp/mt1a-strict.tsv`: one file, zero ERROR rows. The actual TSV was read; it contains only its header.
- PASS, bounded manual comparison: pinned identity, entire lineage, code, attestation, scope and seed-event content agree. This is not corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc` and the test suite. No full-corpus pass is claimed.
- No curator-added graph nodes require term validation; the product-check configuration excludes taxonomy fields. Their inventory agreement was checked manually here.
- No separate target history artifact was found in the ignored-independent filename search. Inline history passed record validation; no external history validator was run against an invented artifact.
- No DOI, PMID or quotation is asserted by the YAML. The marker-linked publication below was checked as completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221928`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035207&retmode=xml) and [NCBI taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035207) agree on identifier, label and SPECIES rank. Both live responses were inspected in full. XML confirms bacterial division, parent 2615210, genetic code 11 and no alternate names; the dataset confirms all ten root-inclusive ancestor identifiers. Their pinned labels and ranks match the YAML.

The parent is the no-rank group `unclassified Methylobacterium`, below genus 407. This carried NCBI lineage is appropriate. A sequence strain qualifier does not authorize changing NCBI's SPECIES rank, and EXACT does not imply a validly published binomial.

The [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was previously inspected in full and rechecked for T1a in this review. No target formal-name or type-deposit attribution was established. Genus-level nomenclature was not inherited. The legacy taxonomy-browser route was unavailable; successful structured NCBI responses supplied identity and lineage evidence.

Pinned exact scans found no children, type-material row, merged-ID row or dropped row for this taxid.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221928` supports the exact name, rank, parent, code, empty synonym fields and NCBI-only provenance.
- Full native `data/catalog/ncbi_names-0005.jsonl.gz:31396` contains the same scientific name and taxid, with an empty unique-name field.
- `data/taxa/PATHS.tsv:14419` resolves the slug; `curation/seed_scope.tsv:322203` adds it on 2026-09-13 under its one-source attested rule.
- The 2026-09-13T17:54:04Z seed event matches that scope reason and source list. The attestation counts one NAME, not a genome or deposit.

The numeric search also matched `data/catalog/ncbi_genbank-0026.jsonl.gz:18314`. Full native inspection identifies GCA_028345745.1, isolate AH-558-B16, as Deltaproteobacteria bacterium, taxid 2026735. Its genome-size fields contain 1035207; those numbers are not its taxonomy. This unrelated single-cell assembly, with BioSample SAMN29371158 and project PRJNA846736, supplies no T1a link.

Exact Entrez `txid1035207[Organism:noexp]` searches returned zero assemblies with phrases-not-found / no-items diagnostics, and one Nuccore UID, 347300704. The complete nucleotide ID list equals the query count. This assembly result is bounded to that query, not proof of universal absence.

Full [GenBank metadata for FR869803.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869803.1) identify a 1,335-nt partial 16S rRNA sequence, strain T1a, exact taxon 1035207, host Trifolium repens and host leaf surface as isolation source. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. Every feature, source qualifier and reference was inspected; sequence bases were omitted. No culture-collection qualifier, BioSample, BioProject or assembly is supplied. This is a marker, not a genome.

Its reference is Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The freshly fetched [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml) confirm that pairing and a study of phyllosphere communities across plant hosts, sites and land-use types. The abstract does not name T1a or establish an isolate-specific phenotype, locality or growth requirement. Full text and supplements were not inspected; community results were not transferred to the isolate.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded T1a/T-1a context and sequence-accession searches found no eligible target culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit assertion.

Zero strains agrees with the BacDive subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: no exact row or descendant contributes an entry. It does not mean the original isolate was never cultured. The existing culture normalizer rejects bare T1a and T-1a as unsupported deposit keys.

An optional FR869803.1 marker link is not a required-representation defect under the current contract. No existing supported strain entry or eligible SI-DP association was established to receive it. Optional definition, phenotype and graph fields may remain empty.

The structured iModulonDB adapter ran before browser follow-up and returned 28 datasets without Methylobacterium or Methylorubrum coverage. It is not applicable; absence is not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and inspected evidence scope. The YAML supports its exact identity and provenance without importing the unrelated genome-size match or treating the 16S marker as a genome. This pass does not certify full-corpus reproducibility or unasserted biological properties.

## Recommended Edits

None required for this record.

Future enrichment belongs in maintained source extraction/seeding code, including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, only after explicit identity evidence and an appropriate typed representation are established. Keep FR869803.1 outside genome counts. Never create a culture accession or SI-DP from the bare designation, or an assembly link from an arbitrary numeric hit. Generated YAML remains read-only.

Do not promote SEEDED to REVIEWED or append curation history from this report.

## Follow-up Checks

- On refresh, repeat exact taxonomy, full lineage, status and target schema/strict checks.
- After an authorized source/import change, run real full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded comparisons do not replace these gates.
- Require an eligible own-deposit identifier and explicit sequence attribution before any StrainInfo link.
- Inspect the full text and supplements of PMID 22000032 before proposing T1a-specific ecological or phenotype assertions.
- Compare taxonomic identifier fields, not incidental occurrences in genome statistics.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial identifier/label/slug search returned four rows. Expanded Methylobacterium/Methylorubrum T1a/T-1a context returned the same three target identity/scope rows, adding none. All four distinct candidates were read fully using structured pinned comparisons and lossless native JSONL decoding. The FR869803 / 347300704 search returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored and compressed files and remain bounded to these sources.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Successful taxonomy/sequence APIs, complete marker metadata, the primary PubMed response and inspected LPSN text supplied evidence. Failed browser output and search snippets were not biological evidence.

Only this new report was written. No YAML/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota reviews were not reopened.
