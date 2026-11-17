# YAML Record Review: Pseudomonas sp. enrichment culture clone DV-AL 2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_enrichment_culture_clone_dv_al_2.yaml`
- Started UTC: 2026-10-07T08:58:20Z
- Finished UTC: 2026-10-07T09:02:35Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035631`, Pseudomonas sp. enrichment culture clone DV-AL 2, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:62104` (environmental samples), ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and `strain_count: 0`. It has one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. This environmental clone label is not a culture-collection accession. Generated YAML is read-only; future fixes belong to maintained source/extraction inputs and `src/taxonmech/seed.py`, with scope and slug ownership in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudomonas_sp_enrichment_culture_clone_dv_al_2.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_enrichment_culture_clone_dv_al_2.yaml --out /private/tmp/dval2-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/dval2-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, full lineage, seven inventories, path, scope and attestations | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |
| Linked PubMed abstract and identifiers | PMID/DOI/title/authors agree with GenBank; consortium scope retained. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons are not byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. No literature/internal evidence references occur in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222159` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31639` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14659` and `curation/seed_scope.tsv:322426`.

All ten ancestors match the committed parent chain: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas and environmental samples, with identical IDs, labels, ranks and order. Live EFetch confirms species rank, parent 62104, code 11, no alternate names and the nine non-root ancestors; Datasets includes root. EFetch's division is Environmental samples, while its lineage establishes the bacterial domain; these are different fields, not a contradiction. No retirement or replacement was found in inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035631&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035631)

This species-rank environmental placeholder satisfies record scope without claiming a validly published binomial or a deposited pure culture. `EXACT` applies to the NCBI concept. The environmental-samples parent is deliberately carried from NCBI, not an inferred species assignment.

## Evidence

The sole `NCBITAXON` attestation agrees on ID, label, count 1, unit `NAME` and snapshot note. A name count is not a strain or genome count. A complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore UID 333952664 resolves to `JF798503.1`, a 1,250-nt partial 16S rRNA marker. Its organism matches the full record label, its qualifier is clone DV-AL 2 and its explicit cross-reference is `taxon:1035631`. The record carries ENV/environmental_sample and describes a naphthalene-enriched consortium from ship-breaking-yard sediment in Gujarat, India. The rRNA feature is partial at both ends. No strain qualifier, culture-collection, BioSample, BioProject or assembly link is supplied. [GenBank JF798503.1](https://www.ncbi.nlm.nih.gov/nuccore/JF798503.1)

The marker was submitted by Patel and Madamwar on 11 April 2011, created 30 May 2011 and updated 15 March 2012. Its publication reference names Patel, Jain and Madamwar, Bioresource Technology 107:122-130 (2012), DOI `10.1016/j.biortech.2011.12.056`, PMID `22217733`. All GenBank metadata were inspected, excluding only sequence strings and translation/transcription payloads. A marker is not a genome; environmental provenance does not prove the clone's independent phenotype.

The complete PubMed abstract verifies the paper identity and names Pseudomonas sp. DV-AL2 among four consortium members. Together with the explicit GenBank reference, this supports the target's study context rather than a bare-name match. The abstract assigns naphthalene degradation and broader hydrocarbon utilization to consortium DV-AL. It does not establish the same performance for DV-AL2 alone. The article's use of strain terminology does not turn the source's clone qualifier into a verified deposit. Full text, figures and supplements were not inspected, so no individual-isolate experiment or mechanism is inferred. [PubMed PMID 22217733](https://pubmed.ncbi.nlm.nih.gov/22217733/)

The two non-target local matches were read completely:

| Source address | Actual match and exclusion |
| --- | --- |
| `data/catalog/allthebacteria.tsv.xz:66276` | Staphylococcus aureus, SAMEA1035631, ERR083788 and ERZ3070824, with META_FAIL. Matching sample digits are not taxonomy; the filter also precludes an eligible link. |
| `data/catalog/allthebacteria.tsv.xz:551214` | Escherichia coli, SAMEA3375249, ERR1035631 and ERZ3259033. Digits occur in a run accession, not a taxon field. |

No gene, regulator, pathway, stress-response or transcriptomics assertion in the YAML requires iModulonDB. The consortium publication found during review does not justify inventing a target mechanism.

## Completeness

Zero BacDive strains and optional omissions agree with inspected source scope. A clone label and consortium membership do not supply a culture deposit or genome. Seeded records need not populate optional literature fields. The linked publication is a useful future contextual annotation, not a required missing assertion; no consequential required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs using `rg --no-ignore --hidden -n -z -i`, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The identity search used taxid 1035631 as a complete digit run, full label/slug and DV-AL 2 with case/separator variants. All five matched lines were read: three target rows and the two exclusions above. The evidence search used JF798503 with optional .1, PMID 22217733 and the exact DOI; it found zero lines. Neither stage found matching metadata values or history paths. Negative local findings include ignored files and are bounded to these roots and terms.

Web queries used the exact DOI, accession, DV-AL 2 with Pseudomonas, and article-title terms. Search snippets, unrelated DOI-tail matches and citing papers were not used as target evidence. No supported deposit/genome chain was established. Exhaustive literature retrieval and sequence similarity were not performed. The exact-taxid Assembly zero includes a phrase-not-found warning and does not exclude assemblies under another identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML within the inspected scope. Identity, lineage, provenance, zero strain count and seed history agree. Optional publication context does not warrant a phenotype inference.

## Recommended Edits

None required. Do not patch generated YAML, replace clone identity with a guessed culture strain, transfer consortium-level phenotypes, count JF798503.1 as a genome, import accession-digit matches or promote `SEEDED` to `REVIEWED`.

Optional marker/publication enrichment requires maintained-input support in `src/taxonmech/seed.py` with tests under `docs/CURATION.md`, preserving the exact organism, taxid, clone qualifier and accession. Keep consortium claims explicitly scoped. Taxonomy-source corrections would belong upstream and in an authorized refresh through `conf/ncbi_taxdump.yaml`, `scripts/extract_source_inventory.py` and guarded seeding; none is supported here.

## Follow-up Checks

- Inspect the full linked paper before asserting any DV-AL2-specific degradation, culture or mechanism result.
- Require an explicit source chain for any future deposit/genome link; preserve environmental clone and consortium scope.
- After authorized maintained-input changes, rerun both single-record validators, `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary NCBI taxonomy, Datasets, sequence-index and nucleotide reads succeeded. PubMed's web page returned a browser check; the complete abstract and identifiers were recovered through EFetch. DOI/ScienceDirect web retrieval did not supply full text. These access limitations do not establish biological absence.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date. Previously inspected guidance and maintained source state remain unchanged at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The entire YAML was reread unchanged before this report. An ignored-independent filename search found no previous report for this stem. Only this new report is added; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
