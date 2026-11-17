# YAML Record Review: Pseudomonas sp. TGR5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_tgr5.yaml`
- Started UTC: 2026-10-10T05:21:00Z
- Finished UTC: 2026-10-10T05:24:09Z
- Verdict: pass

## Target

The entire 53-line generated `TaxonRecord` was read. `NCBITaxon:1037513` denotes Pseudomonas sp. TGR5, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. It asserts no synonym, formal nomenclature, GTDB mapping, deposit, genome, phenotype or causal graph.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_tgr5.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_tgr5.yaml --out /private/tmp/taxonmech-tgr5-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, code, full lineage, source synonyms, seven inventories, index/scope resolution, attestation and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Complete native name and all 38 additional catalog candidate rows were read through a lossless common-field/differing-field representation. Live NCBI EFetch/Datasets taxonomy, exact nucleotide search and full marker annotations were inspected.
- The taxonomy-browser web reader failed; direct HTML retrieval succeeded and all 74 parsed text lines were read. A previously identified similar-isolate paper was checked through its Europe PMC full-text XML: metadata, abstract, complete relevant paragraphs and complete isolate table.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused checks do not prove corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222785` agrees with the directly inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037513&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037513&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037513). Species rank, parent 196821 and code 11 agree; Datasets includes root 1.

The full root-first lineage agrees: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas. The immediate parent is correctly `NO_RANK`.

`data/catalog/ncbi_names-0005.jsonl.gz:32423` contains the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. The species-ranked placeholder and a marker strain qualifier are compatible; exact taxonomy grounding does not establish formal nomenclature or type status.

## Evidence

The one-NAME NCBITAXON attestation and 2026-09-13 snapshot note match the pinned inventory. No additional own source-count row was found.

The exact nucleotide query returns one entry, UID 334361453: [JF799821.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799821.1), a 780-base partial 16S rRNA gene with both ends partial. The source explicitly names Pseudomonas sp. TGR5, strain TGR5, `taxon:1037513` and wetland soil. Declared and actual lengths agree, with alphabet `acgt`. This supports a marker-to-taxon association, not a genome or culture-deposit link.

The only marker reference is a direct submission dated 10-Apr-2011 by Li, Liu, Shao and Sun at Hebei University. It supplies no DOI, PMID, collection country, collection date or coordinates. Institutional address and submission date must not become collection metadata.

All 38 extra local candidate rows arise from BioProject `PRJNA1037513`: 19 BV-BRC rows and their 19 GenBank assembly counterparts. Every row identifies Streptococcus suis, taxon 1307, with Ss-series strains, not Pseudomonas sp. TGR5. For example, `data/bvbrc/bvbrc-0001.jsonl.gz:27793` and `data/catalog/ncbi_genbank-0031.jsonl.gz:49444` both describe Ss_51, `GCA_034297355.1`, `SAMN38182199`; the BV-BRC ID is `1307.7156`. The matching numeral belongs to a different identifier namespace. No target assembly is missing on that basis.

[Hunter et al. (2005), inspected through Europe PMC XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3810630/fullTextXML), has verified DOI 10.3390/ijerph2005020010, PMID 16705827 and PMCID PMC3810630. Its Table 1 describes Tgr 5 as a rod with negative Gram stain and cloudy-white appearance, but the identification paragraph does not assign it to Pseudomonas. The PAH experiments concern B. subtilis Tgr3; the source soil was from Southern Maryland. None of the exact target name, JF799821 or 1037513 occurs in the XML. This is an unjoined similar designation, not proof of identity or of biological impossibility. Neither phenotype nor locality was transferred.

Exact-name, designation-variant and accession web searches established no directly joined experimental publication. Other snippets were only discovery leads, not evidence for this target. Datasets omits an assembly-count field rather than explicitly returning zero; the checks do not exclude other genomes or publications.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Bounded taxon ID, slug and designation were searched, then JF799821 and spaced/hyphenated TGR 5 variants were added. Both searches yielded 41 lines: three own backbone/name/scope rows and the 38 BioProject-number collisions, all individually read and excluded.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were fully parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. Absence statements apply only to those inspected repository surfaces.

Zero strain count describes represented culture inventory, not isolate existence or culturability. Empty optional fields are appropriate without exact supporting joins. Neither a partial marker nor an unjoined isolate paper establishes a required missing genome or phenotype. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, lineage, attestation and seed audit are supported. Numeric cross-namespace collisions and similar isolate names do not establish missing associations.

## Recommended Edits

No generated-record correction is justified. Preserve TGR5, species rank, full lineage, `SEEDED` status and existing history. Do not join BioProject numerals to taxon IDs, promote a partial marker to a genome or transfer biological claims through designation similarity.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not direct YAML edits. Optional marker enrichment needs a supported taxon-level representation, not an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm exact organism linkage and retain JF799821.1's version. Require typed identifier joins and explicit strain/assembly evidence before adding a genome, and an identity cross-reference before using similar-isolate literature. After maintained-source changes, run the seed canary, schema/strict/history checks, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `bbaf7c27ed0a9e774be0c07f1f02f5b5851fe2e953dbbdac3dab480c013e0f4b`.
- JF799821.1 lowercase sequence SHA-256: `8c17a6a5b7962ffb321321bb6a93ae2e9d208bb99b358c14b6a5e149eec50e26`.
- Hunter article XML: 56,488 bytes; SHA-256 `f8622f20dc4cd738b7f09c5e7e684a607c066e2ddea6edde3237ced7ccecade1`.
- Additional native candidates were in `data/bvbrc/bvbrc-0001.jsonl.gz`, `data/catalog/ncbi_genbank-0031.jsonl.gz` and `data/catalog/ncbi_genbank-0032.jsonl.gz`. All 38 complete rows, not merely their search excerpts, were inspected.
- `data/taxa/PATHS.tsv:15338` and `curation/seed_scope.tsv:323002` uniquely resolve the target. Scope addition is 2026-09-13; the seed preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this report was added for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
