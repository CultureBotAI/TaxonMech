# YAML Record Review: Saccharomonospora sp. G2Z41

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/saccharomonospora_sp_g2z41.yaml`
- Started UTC: 2026-10-09T01:28:28Z
- Finished UTC: 2026-10-09T01:31:24Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036517`: species rank, Bacteria domain, parent `NCBITaxon:2634184`, ten root-first ancestors, code 11, `EXACT` grounding and `SEEDED` status. It has zero BacDive entries, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional names, nomenclature, mappings, strain/genome links, record-level evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior target report. This generated file is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/saccharomonospora_sp_g2z41.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/saccharomonospora_sp_g2z41.yaml --out /private/tmp/saccharomonosporaG2Z41-strict.tsv`: passed, one file and zero errors; full TSV was header-only.
- Structured checks matched full backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own nucleotide consistency passed: declared and actual length 1417, rRNA transcription equals DNA, no non-ACGT symbols. This is not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. Embedded history was inspected; ignored-inclusive inventory found no separate target history artifact. Graph-product validation is inapplicable without graph nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036517&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036517) agree with identifier, label, rank, parent, code and lineage. Datasets confirms ten root-first ancestor IDs; EFetch supplies matching ancestor labels/ranks while omitting root from its displayed chain.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Pseudonocardiales, Pseudonocardiaceae, Saccharomonospora and unclassified Saccharomonospora. Live EFetch has no other names; pinned synonyms are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children.

Species rank for an unnamed strain-associated taxon does not establish a formally described species. Exact grounding identifies this NCBI concept, not equivalence to a named comparison species.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222517`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32061`: scientific-name object, empty unique name.
- `data/taxa/PATHS.tsv:15024`: identifier/slug.
- `curation/seed_scope.tsv:322764`: admission date/reason matching the event.

The attestation counts one `NAME`, not a genome or experiment. Exact scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw rows. Schema semantics make `strain_count: 0` a represented BacDive count, not a denial of the strain designation.

Exact Nuccore query `txid1036517[Organism:noexp]` and a broader G2Z41 phrase search each returned only UID 334361413. Complete [JF806668.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806668.1) XML, including both references, all features and sequence, was read. This 1417-base 16S marker is partial at both ends. Source qualifiers explicitly identify G2Z41 and taxon 1036517 alongside organism and genomic DNA. They supply no host, isolation-source, geographic, culture-deposit or assembly qualifier. Only source and rRNA features occur.

The accession names Chen, Wu and Li, an unpublished seagrass-associated study, and direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. No PMID or DOI is supplied. This marker is not a genome or phenotype assay; missing qualifiers cannot be inherited from neighboring accessions.

The inspected [Wu et al. (2012) Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii) compares G2Z41 with Saccharomonospora xinjiangensis, 98.44%, and reports positive PKS-I, PKS-II and NRPS PCR screens. Comparison and screening are not synonymy or demonstrated antimicrobial activity. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981. No biological assertion was imported.

## Completeness

Complete enough for its supported taxonomy-seed claims. Optional nomenclature, deposits, genome links, citations and graphs are appropriately unasserted without explicit evidence chains. The external marker does not require an invented BacDive strain.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded taxid 1036517, G2Z41 and slug; expansion added JF806668 and word-bounded UID 334361413. Both found only the three own taxonomy/name/scope rows, all fully read. Numeric boundaries avoid false matches inside unrelated identifiers. Five SOURCE.json files were separately fully parsed without a match; history filenames were independently inventoried. These absence statements are bounded to the named roots and terms.

Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. PubMed G2Z41/JF806668/JF806668.1 search returned zero with quoted-phrase warnings. Strain/accession web searches led to taxonomy and the same primary study. Search snippets were not treated as primary evidence, and indexed misses do not prove universal genome or literature absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with inspected pinned and live authorities. No unsupported species reassignment, genome or phenotype is asserted.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future authoritative taxonomy corrections belong first at NCBI and then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression tests; scope changes belong in `curation/seed_scope.tsv`. Optional enrichment requires maintained-input/model support, not hand-edited output.

## Follow-up Checks

No corrective follow-up for current claims. Before literature enrichment, verify an explicit strain/accession/deposit chain and visually inspect the original paper table/figure. Author-hosted table text, column headings and footnote were inspected; the original PDF was not visually verified. Prior related-record PDF/figure requests were inaccessible.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036517`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and field checklist governed this individual review. Its own YAML, source rows, live taxonomy, marker and paper row were inspected; no adjacent record's identity or verdict was inherited.

Before/after YAML SHA-256: `ec64d31b647595742ff8dc8da417dc2d05552e1af43900842f753fbef942baef`. Only this new report was written for this target. YAML, sources, history, status, generated pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
