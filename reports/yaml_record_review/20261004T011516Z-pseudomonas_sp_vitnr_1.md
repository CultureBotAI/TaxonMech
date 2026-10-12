# YAML Record Review: Pseudomonas sp. VITNR-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_vitnr_1.yaml`
- Started UTC: 2026-10-04T01:14:16Z
- Finished UTC: 2026-10-04T01:15:16Z
- Verdict: pass

## Target

Read the complete 54-line generated TaxonRecord for `NCBITaxon:1032618`, Pseudomonas sp. VITNR-1. It is a SPECIES-rank NCBI placeholder in BACTERIA under unclassified Pseudomonas (196821), with EXACT grounding, SEEDED status, ten lineage entries, genetic code 11, zero BacDive strains, one source attestation and one seed event. It does not claim a formal species description, a registered culture deposit, a genome, a phenotype or a causal graph.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_vitnr_1.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pseudomonas_sp_vitnr_1.yaml` passed: one file and zero errors; the validator's TSV diagnostic was refreshed.

Read-only structured comparisons checked the entire lineage, raw source matches, scope, path, source assertion and seed-event wording. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. These comparisons do not constitute corpus reproduction. No curator-added graph identifier or separate-history reference requires a target-specific term/reference gate.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:220868` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:30160` match the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032618&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032618) confirm the ID, label, species rank, parent, bacterial domain, genetic code and all ten root-first lineage identifiers. This includes Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae and Pseudomonas.

The full backbone scan found no children or target synonyms. Full structured scans found no own-ID row in the type-material, merged-ID or dropped inventories. EXACT is warranted for the NCBI placeholder; a strain-like suffix does not authorize changing its source rank. Browser access failed, but the two structured authority endpoints succeeded.

## Evidence

The one NCBITAXON NAME assertion and 2026-09-13 snapshot note reproduce the source inventory. `data/taxa/PATHS.tsv:13244` and `curation/seed_scope.tsv:321241` agree on ID, slug and NCBI-only scope reason. The 2026-09-13 seed event is consistent; it is not a human review event.

Live exact-taxon Nuccore search returned one entry, [FR848954.1](https://www.ncbi.nlm.nih.gov/nuccore/FR848954.1), inspected as GenBank XML. It is a 1,037-base partial 16S rRNA sequence with organism Pseudomonas sp. VITNR-1, strain VITNR-1 and taxon 1032618. Its cited study is unpublished; the title refers to Pseudomonas stutzeri isolated from forest soil. Direct submission was by Kumar R. on 2011-03-29 through VIT University, India. No PMID or DOI is supplied.

The study title is not an inspected species-identification analysis. It does not justify an exact Pseudomonas stutzeri synonym, formal nomenclature or a revised lineage. The source qualifiers do not independently establish collection location from the submitter's institutional address. The YAML correctly makes none of these extra claims.

Exact Assembly search returned zero with a phrase-not-found warning. This is a bounded search result, not a universal assertion that no genome exists.

## Completeness

Structured scans found no exact target in BacDive, LPSN, GTDB mappings, GOLD aggregate, MediaDive, Madin or BactoTraits. There are no descendant taxa from which classified BacDive strains should be gathered, supporting `strain_count: 0`.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric identifier, label, slug and VITNR-1 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All four matching lines were inspected in context. Recursive SOURCE.json traversal also included ignored files and found no target-specific match.

No independent target deposit, assembly assertion, taxonomic mapping or standalone history entry was found within these searched surfaces. The bare strain label and 16S accession cannot supply a registered collection join or genome identity. Empty optional nomenclature, genome, phenotype and graph slots are appropriate. iModulonDB is not applicable to this record's taxonomy-only claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The unpublished study-title identification remains limited source context, not a contradictory taxonomic assertion carried by this YAML.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status. A future supported source-identity correction belongs to the maintained authority input and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`, not a manual YAML edit. Scope remains owned by `curation/seed_scope.tsv`.

## Follow-up Checks

If a later source supplies a formal identification or eligible deposit, inspect its evidence before importing it. For an authorized refresh, regenerate one canary with `just seed-canary NCBITaxon:1032618 --force`, inspect the file, rerun both focused validators, and run the full documented reproduction, provenance, history and QC gates before publishing corpus changes.

## Additional Notes

The only additional numeric catalog hit was `GCA_983005345.1` at `data/catalog/ncbi_genbank-0066.jsonl.gz:44366`: its ungapped genome size is 1032618, but its taxon is Cryomorphaceae bacterium (1898111). This is a numeric collision, not target genomic evidence.

Only this new report was manually written. No taxon YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.

