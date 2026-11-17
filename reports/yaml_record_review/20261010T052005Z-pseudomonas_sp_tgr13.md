# YAML Record Review: Pseudomonas sp. TGR13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_tgr13.yaml`
- Started UTC: 2026-10-10T05:13:17Z
- Finished UTC: 2026-10-10T05:20:05Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037512` denotes Pseudomonas sp. TGR13, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_tgr13.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_tgr13.yaml --out /private/tmp/taxonmech-tgr13-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, genetic code, full lineage, empty source synonyms, seven inventories, index/scope resolution, attestation and seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- The complete native name row, live NCBI EFetch/Datasets taxonomy, exact nucleotide search and full marker annotations were inspected. The taxonomy-browser web reader failed; direct retrieval succeeded, and all 74 parsed HTML text lines were read.
- A thesis candidate was inspected in its primary PDF after the web reader returned 403. Full-document text search, relevant methods and appendix text, and rendered pages 1, 66, 67, 152, 153 and 154 were checked. Rendering used temporary PyMuPDF tooling because Poppler was unavailable; no repository dependency changed.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused checks do not establish corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222784` agrees with the directly read [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037512&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037512&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037512). Parent 196821, species rank and code 11 agree; Datasets includes root 1.

The full root-first lineage agrees: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas. The immediate parent's `NO_RANK` value is correct.

`data/catalog/ncbi_names-0005.jsonl.gz:32422` supplies the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. NCBI's species-ranked placeholder and the marker's strain qualifier describe compatible metadata layers; they do not establish formal nomenclature or type status.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The exact nucleotide query returns one entry, UID 334361452: [JF799820.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799820.1), a 771-base partial 16S rRNA gene, partial at both ends. Its source explicitly links Pseudomonas sp. TGR13, strain TGR13, `taxon:1037512` and wetland soil. Declared and observed sequence lengths agree, with alphabet `acgt`. This is marker-to-taxon evidence, not an assembly or culture-deposit association.

The sole marker reference is a direct submission dated 10-Apr-2011 by Li, Liu, Shao and Sun at Hebei University. It supplies no DOI, PMID, collection country, collection date or coordinates. An institutional address and submission date are not sampling metadata.

The exact-name search led to [Aniko Konya's Oklahoma State University dissertation, Benzene and Toluene Biodegradation Limitations with Heavy Metal Co-Contamination](https://openresearch.okstate.edu/bitstreams/9968d137-8907-44aa-b9ad-a132993580a8/download). The title page dates the PhD dissertation to July 2021. Appendix A, PDF page 154 / printed page 140, assigns OTUs 1, 4554 and 7128 to Pseudomonas sp. tgr13; the preceding primer table gives their 242-base amplicon. Methods on PDF pages 65-67 describe community sequencing and selection of relatively abundant OTUs for qPCR, with targets closely related to bacterial strains at greater than 97% identity. Thus this is a related-sequence OTU assignment, not evidence that isolate TGR13 itself was cultured, degraded either compound or tolerated heavy metals. The appendix provides the name, not JF799820; full-PDF search did not find that accession. No trait or marker-identity claim was imported from this lead.

Datasets omits an assembly-count field rather than explicitly returning zero. No target genome or directly joined experimental isolate study was established from the inspected evidence. The additional exact-accession/name web query returned no results, but these bounded searches do not exclude other publications.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Bounded taxon ID, slug and designation were searched, followed by JF799820 and spaced/hyphenated TGR 13 variants. Both searches returned exactly three lines: own backbone, native name and scope. No extra catalog candidate was found within those searches.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target review and no target-specific history filename. These absence statements are limited to the inspected repository surfaces.

Zero strain count describes represented culture inventory, not isolate existence or culturability. Empty optional slots are appropriate without exact supporting joins. A partial marker and a similarity-based community assignment are not missing required genome or phenotype fields. iModulonDB is not applicable to the record's taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, full lineage, attestation and seed audit are supported. The thesis does not establish an omitted isolate-level phenotype.

## Recommended Edits

No generated-record correction is justified. Preserve TGR13, the species-ranked placeholder, complete lineage, `SEEDED` status and existing history. Do not treat the partial marker as a genome, an institutional address as collection locality or a related environmental OTU as the deposited isolate.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker enrichment requires a supported taxon-level representation rather than an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm the exact organism association and retain JF799820.1's version. Require explicit assembly and organism/strain evidence before adding a genome, and direct isolate identity plus experimental evidence before assigning a phenotype. After maintained-source changes, run the documented seed canary, schema/strict/history validation, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `2327845e720d72be6084759ff0909c7c0e77a145429540297451d7a01e8ab85e`.
- JF799820.1 lowercase sequence SHA-256: `4d545d79d5329bc9d849c77f353d195d5862ba63e3d77d2395da36a296d04641`.
- Thesis PDF: 161 pages; SHA-256 `c715f1cfe2e2c3411e452cae28f720809f987ab6a7a04a90c88dcd37fc12866c`. Its methods, primer table and OTU footnote were inspected, not inferred from a search snippet. A search-index recency label was not treated as the publication date.
- `data/taxa/PATHS.tsv:15337` and `curation/seed_scope.tsv:323001` uniquely resolve the target. Scope addition is 2026-09-13; the seed preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
