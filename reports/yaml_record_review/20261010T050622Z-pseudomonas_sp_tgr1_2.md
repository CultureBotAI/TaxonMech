# YAML Record Review: Pseudomonas sp. TGR1-2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_tgr1_2.yaml`
- Started UTC: 2026-10-10T05:03:02Z
- Finished UTC: 2026-10-10T05:06:22Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037510` denotes Pseudomonas sp. TGR1-2, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_tgr1_2.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_tgr1_2.yaml --out /private/tmp/taxonmech-tgr1-2-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, code, complete lineage, empty source synonyms, seven inventories, unique index/scope resolution, attestation and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- The complete native name row, live NCBI EFetch/Datasets taxonomy, nucleotide search and full marker annotations were inspected. The web reader failed on the taxonomy-browser URL; direct retrieval succeeded, and all 74 parsed HTML text lines were read.
- A similar-designation publication was inspected through Europe PMC's full-text XML after publisher and PMC web-page retrieval problems. Bibliographic metadata, abstract, complete matching paragraphs and the complete isolate table were read. Another candidate paper remained inaccessible and was not used as evidence.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused passes do not establish corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222782` agrees with the directly inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037510&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037510&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037510). Parent 196821, species rank and code 11 agree; Datasets includes root 1.

The complete root-first lineage matches: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas. The direct parent is correctly `NO_RANK`.

`data/catalog/ncbi_names-0005.jsonl.gz:32420` contains the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. The NCBI species-ranked placeholder and sequence strain qualifier are compatible metadata layers, not a rank conflict. Exact grounding does not establish formal species nomenclature or type status. Preserve the complete TGR1-2 designation; TGR1, TGR2 and TGR12 are not automatic aliases.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The exact nucleotide query returns one entry, UID 334361451: [JF799819.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799819.1), a 771-base partial 16S rRNA gene with both ends marked partial. Its source explicitly links Pseudomonas sp. TGR1-2, strain TGR1-2, `taxon:1037510` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This supports a marker-to-taxon link, not a genome or culture-deposit association.

The sole marker reference is a direct submission dated 10-Apr-2011 by Li, Liu, Shao and Sun at Hebei University. No DOI, PMID, collection country, coordinates or collection date is supplied. The institutional address and submission date are not sampling metadata. Shared authors, genus or habitat wording cannot transfer another isolate's biological claims.

The exact-name and accession searches also returned broad or similar-designation leads. [Hunter et al. (2005), read through Europe PMC XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3810630/fullTextXML), has DOI 10.3390/ijerph2005020010, PMID 16705827 and PMCID PMC3810630, confirmed in its front matter. Table 1 lists Tgr1, Tgr2 and Tgr12 separately. The experiments and discussion concern B. subtilis Tgr3, with other isolates also distinguished. The full XML contains none of the exact literals TGR1-2, JF799819 or 1037510. These observations do not establish identity with this target; the paper does not justify importing PAH-transformation claims into TGR1-2.

Another search lead, [Scortichini et al.'s P. avellanae lineages paper](https://bsppjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-3059.2006.01352.x), could not be inspected beyond search output: publisher retrieval returned 403, and a public mirror download failed with 404. Its search-snippet strain labels were treated only as leads. No target association or biological finding relies on that inaccessible paper.

Datasets omits an assembly-count field rather than explicitly returning zero. No target genome or direct experimental publication was established from the inspected evidence. The search and retrieval limitations do not prove that no additional literature exists.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Bounded taxon ID, slug and designation, including separator variants, were searched, then JF799819 was added. Both searches found exactly three lines: own backbone, native name and scope. No extra catalog candidate was found within these searches.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements are restricted to the inspected repository surfaces.

Zero strain count describes represented culture inventory, not isolate existence or culturability. Empty optional slots are appropriate without exact supporting joins. A partial marker and unjoined literature leads are not missing required genome or phenotype fields. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, full lineage, source count and seed audit are supported. The literature access limitation affects optional contextual investigation, not a citation or assertion required by this YAML.

## Recommended Edits

No generated-record correction is justified. Preserve TGR1-2, species rank, the complete Pseudomonas lineage, `SEEDED` status and existing history. Do not treat the marker as a genome, infer collection locality from an institutional address or conflate separately designated isolates from search results.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker enrichment needs a supported taxon-level representation rather than an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm exact TGR1-2 linkage and retain JF799819.1's version. Require explicit assembly and organism/strain evidence for a genome, and direct isolate-linked evidence for a functional claim. If the inaccessible paper is revisited, inspect its actual strain table and establish an explicit identity cross-reference before using it. After maintained-source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `90386a2742666a4614036b924dad356b95929d623bcc488e0dd9180c50e8e762`.
- JF799819.1 lowercase sequence SHA-256: `3e6dab18963edea1f48d243ff9845695ba7b5c9fecb544b99baa7434a6d15ee1`.
- The MDPI page returned 429, the PMC web reader returned a browser-check page, and both attempted PDF web reads failed. Europe PMC's public XML endpoint returned the 56,488-byte article and resolved the Tgr isolate-table check. No CAPTCHA was bypassed and no valid PDF was obtained or rendered.
- `data/taxa/PATHS.tsv:15335` and `curation/seed_scope.tsv:322999` uniquely resolve this record. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
