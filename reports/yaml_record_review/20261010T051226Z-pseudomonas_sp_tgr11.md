# YAML Record Review: Pseudomonas sp. TGR11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_tgr11.yaml`
- Started UTC: 2026-10-10T05:08:51Z
- Finished UTC: 2026-10-10T05:12:26Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037511` denotes Pseudomonas sp. TGR11, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_tgr11.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_tgr11.yaml --out /private/tmp/taxonmech-tgr11-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, code, complete lineage, empty source synonyms, seven inventories, unique index/scope resolution, attestation and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- The complete native name row, live NCBI EFetch/Datasets taxonomy, nucleotide search and full marker annotations were inspected. The web reader failed on the taxonomy-browser URL; direct retrieval succeeded, and all 74 parsed HTML text lines were read.
- A similar-designation article was inspected through Europe PMC full-text XML: bibliographic metadata, abstract, complete relevant paragraphs and the complete isolate table were read. Two additional search candidates were checked through their complete PubMed abstracts and identifiers; their full articles were not reviewed.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused checks do not establish corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222783` agrees with the directly read [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037511&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037511&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037511). Parent 196821, species rank and code 11 agree; Datasets includes root 1.

The complete root-first lineage matches: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas. The direct parent is correctly `NO_RANK`.

`data/catalog/ncbi_names-0005.jsonl.gz:32421` contains the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. NCBI's species-ranked placeholder and a sequence strain qualifier are compatible metadata layers. Exact grounding does not establish formal species nomenclature or type status. A short designation alone does not establish identity with another study's isolate.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The exact nucleotide query returns one entry, UID 334361454: [JF799822.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799822.1), a 747-base partial 16S rRNA gene with both ends marked partial. Its source explicitly links Pseudomonas sp. TGR11, strain TGR11, `taxon:1037511` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This supports a marker-to-taxon link, not a genome or culture-deposit association.

The sole marker reference is a direct submission dated 10-Apr-2011 by Li, Liu, Shao and Sun at Hebei University. No DOI, PMID, collection country, coordinates or collection date is supplied. The institutional address and submission date are not sampling metadata. Shared authors or habitat wording cannot transfer another isolate's biological claims.

The spaced-designation query returned [Hunter et al. (2005), inspected through Europe PMC XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3810630/fullTextXML). Front matter confirms DOI 10.3390/ijerph2005020010, PMID 16705827 and PMCID PMC3810630. Table 1 describes Tgr 11 as a rod with negative Gram stain and cloudy-white appearance; the paper's identification paragraph does not assign that isolate to Pseudomonas. Its PAH experiments concern B. subtilis Tgr3, and its soil came from Southern Maryland. The full XML contains none of the exact literals Pseudomonas sp. TGR11, JF799822 or 1037511. This is an unjoined similar-designation lead, not proof of either identity or biological impossibility. Neither its phenotype nor its collection locality belongs in the target without an explicit identity cross-reference.

The complete abstracts of [PMID 33254400](https://pubmed.ncbi.nlm.nih.gov/33254400/) and [PMID 31004191](https://pubmed.ncbi.nlm.nih.gov/31004191/) identify P. fluorescens TGR-B2 and/or P. putida TGR-B4/TGRB4. Their retrieved DOI identifiers are 10.1016/j.ecoenv.2020.111538 and 10.1007/s00284-019-01670-3, respectively. Those abstracts do not establish a TGR11 association. The shared TGR string does not transfer their genome, methylmercury-related claims or Three Gorges Reservoir locality to this record.

Datasets omits an assembly-count field rather than explicitly returning zero. No target genome or directly joined experimental publication was established from the inspected evidence. The bounded literature searches do not exclude additional publications.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Bounded taxon ID, slug and designation were searched, then JF799822 and spaced/hyphenated TGR 11 variants were added. Both searches found exactly three lines: own backbone, native name and scope. No extra catalog candidate was found within these searches.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements apply only to inspected repository surfaces.

Zero strain count describes represented culture inventory, not isolate existence or culturability. Empty optional slots are appropriate without exact supporting joins. A partial marker and unjoined literature leads are not missing required genome or phenotype fields. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, full lineage, source count and seed audit are supported. Similar-designation literature does not establish missing associations.

## Recommended Edits

No generated-record correction is justified. Preserve TGR11, species rank, the complete Pseudomonas lineage, `SEEDED` status and existing history. Do not treat the marker as a genome, infer locality from an institutional address or join isolates on designation resemblance alone.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker enrichment needs a supported taxon-level representation rather than an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm exact TGR11 linkage and retain JF799822.1's version. Require explicit assembly and organism/strain evidence before adding a genome, and a documented identity cross-reference before using any similar-designation publication. After maintained-source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `fefa7ab92ffbbfa8a616eed12bace414333bc16a032afc6c02cfc430444a77d5`.
- JF799822.1 lowercase sequence SHA-256: `1a483faca1a60002322c9399e5b344186441ea9f3469cee4658012f9d5c4fe2d`.
- Hunter article XML: 56,488 bytes; SHA-256 `f8622f20dc4cd738b7f09c5e7e684a607c066e2ddea6edde3237ced7ccecade1`. Its table and identification paragraphs were read as source evidence, not inferred from search snippets.
- `data/taxa/PATHS.tsv:15336` and `curation/seed_scope.tsv:323000` uniquely resolve this target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
