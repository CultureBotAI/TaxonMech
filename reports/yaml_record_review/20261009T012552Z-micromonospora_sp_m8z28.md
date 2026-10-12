# YAML Record Review: Micromonospora sp. M8Z28

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/micromonospora_sp_m8z28.yaml`
- Started UTC: 2026-10-09T01:23:29Z
- Finished UTC: 2026-10-09T01:25:52Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036516`: species rank, Bacteria domain, parent `NCBITaxon:2617518`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has zero BacDive records, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. The YAML is generated, not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/micromonospora_sp_m8z28.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/micromonospora_sp_m8z28.yaml --out /private/tmp/micromonosporaM8Z28-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons checked the full backbone and ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared and actual length 1392, rRNA transcription equals DNA, no non-ACGT symbols. This is annotation consistency, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, tests, `just qc`, vendored synchronization, generated-site drift and publication builds. These individual checks do not establish corpus reproduction. Embedded history was read; ignored-inclusive inventory found no separate target history artifact. Graph-product validation is inapplicable without graph nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036516&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036516) match identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs. EFetch supplies matching ancestor labels/ranks while omitting root from its displayed lineage; the views are compatible.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Micromonosporales, Micromonosporaceae, Micromonospora and unclassified Micromonospora. Live EFetch supplies no other names; pinned synonyms are empty. Exact pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

Species rank for an unnamed strain-associated taxon is not proof of a formally described species. `EXACT` denotes the supplied NCBI concept, not a formal identification as a named congener.

## Evidence

Complete own source rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222516`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32060`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15023`: identifier/slug.
- `curation/seed_scope.tsv:322763`: admission date/reason matching the seed event.

The attestation counts one `NAME`, not an experiment or genome. Exact scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw rows. Under schema semantics, `strain_count: 0` counts represented BacDive records, not whether M8Z28 is a strain designation.

Exact Nuccore query `txid1036516[Organism:noexp]` and the broader M8Z28 phrase search each returned only UID 334361386. Complete [JF806641.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806641.1) XML was read: both references, all features and sequence. It is a 1392-base partial 16S marker, partial at both ends. Source qualifiers explicitly identify M8Z28 and taxon 1036516 alongside organism and genomic DNA. No host, isolation-source, geographic, culture-deposit or assembly qualifier is supplied. Source and rRNA are the only features.

References name Chen, Wu and Li, an unpublished seagrass-associated study, and direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. The accession supplies no PMID or DOI. The marker does not establish a genome or phenotype; missing qualifiers must not be copied from neighboring accessions.

The inspected [Wu et al. (2012) Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii) compares M8Z28 with Micromonospora marina, 99.78%, and records PKS-I positive, PKS-II negative and NRPS positive PCR screens. Comparison and screening do not establish synonymy or an antimicrobial phenotype. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links, citations and graphs are appropriately unasserted without explicit evidence chains. The external marker does not require an invented BacDive entry.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` scans covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded taxid 1036516, M8Z28 and slug; expansion added JF806641 and word-bounded UID 334361386. Both found only the three own taxonomy/name/scope rows, all read fully. Numeric boundaries avoid treating another identifier's embedded digits as this taxon. Five SOURCE.json files were separately fully parsed without a match; history filenames were independently inventoried.

Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. PubMed M8Z28/JF806641/JF806641.1 search returned zero with quoted-phrase warnings. Strain/accession web searches led to taxonomy listings and the same primary study; search snippets were not used as a substitute for inspected primary text. These bounded results do not prove universal genome or literature absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. No unsupported genome, phenotype or species reassignment is present.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future authoritative taxonomy corrections belong first at NCBI and then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression tests; admission changes belong in `curation/seed_scope.tsv`. Optional enrichment requires maintained-input/model support, not a hand-edited output.

## Follow-up Checks

No corrective follow-up for current claims. Before literature enrichment, establish an explicit strain/accession/deposit chain and visually verify the original table/figure. Author-hosted table text and its footnote were inspected; original PDF visual verification was not performed. Prior related-record PDF/figure routes were inaccessible.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:1036516`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and field checklist governed this individual review. Its own YAML, source rows, live taxonomy and marker were read independently. The shared study's own M8Z28 row was inspected; no adjacent record's identity or verdict was inherited.

Before/after YAML SHA-256: `91b0285476183d4e01249baad9ee217c2264800edb1970f80498d25cdbc84665`. Only this new timestamped report was written for this target. No YAML, source, history, status, generated page or GitHub object changed. Eukaryota and existing worktrees remained untouched.
