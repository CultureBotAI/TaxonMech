# YAML Record Review: Micromonospora sp. HCZ42

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/micromonospora_sp_hcz42.yaml`
- Started UTC: 2026-10-09T01:19:26Z
- Finished UTC: 2026-10-09T01:22:19Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036515`: species rank, Bacteria domain, parent `NCBITaxon:2617518`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has zero BacDive entries, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior target report. The YAML is generated and is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/micromonospora_sp_hcz42.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/micromonospora_sp_hcz42.yaml --out /private/tmp/micromonosporaHCZ42-strict.tsv`: passed, one file and zero errors. Complete TSV was header-only.
- Structured comparison checked full backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Exact target identifiers were checked in seven supplementary inventories and the type-material, merged-ID and dropped tables.
- Own marker consistency passed: declared and actual sequence length 1396, submitted rRNA transcription equals DNA, no non-ACGT symbols. This is annotation consistency, not a taxonomic alignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, tests, `just qc`, vendored synchronization, generated-site drift and publication builds. Individual checks are not corpus reproduction. Embedded history was read; ignored-inclusive inventory found no separate target history artifact. Graph-product validation is inapplicable without graph nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036515&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036515) match identifier, label, rank, parent, genetic code and lineage. Datasets includes root in all ten ancestor IDs; EFetch's displayed chain omits root but supplies matching ancestor labels/ranks.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Micromonosporales, Micromonosporaceae, Micromonospora and unclassified Micromonospora. Live EFetch has no other names and pinned synonyms are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children.

Species rank for an unnamed strain-associated NCBI taxon is not a formal species description. `EXACT` grounds the supplied identifier, not equivalence to a named comparison species.

## Evidence

The following complete rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222515`: identity, rank, parent, code, synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32059`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15022`: identifier/slug.
- `curation/seed_scope.tsv:322762`: admission date and reason matching the event.

The attestation counts one `NAME`, not an experiment or genome. No exact target row was found in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw inventories. Schema semantics make `strain_count: 0` a BacDive coverage count, not a denial of the strain designation.

Exact Nuccore query `txid1036515[Organism:noexp]` returned UID 334361390. Complete [JF806645.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806645.1) XML was read, including both references, every feature and the sequence. It is a 1396-base partial 16S marker, partial at both ends. Source qualifiers explicitly identify HCZ42 and taxon 1036515 alongside organism and genomic DNA. They supply no host, isolation-source, geographic, deposit or assembly qualifier. Source and rRNA are the only features.

References name Chen, Wu and Li, an unpublished seagrass-associated study and direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. The accession supplies no PMID or DOI. A marker does not establish a genome or phenotype, and missing source qualifiers cannot be inherited from nearby records.

A broader HCZ42 phrase search found 72 Nuccore records. All 71 additional ESummary objects were read completely using lossless common-fields/column-values output. They identify Vibrio hepatarius, taxid 171383, strain HF70, SAMN14444629 and RefSeq project 224116. Their source describes seawater inoculated into a synthetic phycosphere, collected in November 2017 in Athens, Georgia. The records span NZ_JAATOO010000001.1 through NZ_JAATOO010000073.1 excluding 070 and 071. Different organism and strain identities exclude these candidates; no full-genome feature audit or explanation of the phrase match is claimed.

[Wu et al. (2012), Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii) lists HCZ42's nearest species as Micromonospora siamensis, 98.85%, with PKS-I negative, PKS-II positive and NRPS positive PCR screens. These are comparison/screening results, not synonymy or an antimicrobial phenotype. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981. No literature assertion was imported.

## Completeness

Complete enough for its supported taxonomy-seed claims. Optional nomenclature, deposits, genome links, citations and graphs are appropriately unasserted without explicit evidence chains. A source marker is not a missing BacDive strain or genome.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` scans covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded taxid 1036515, HCZ42 and slug; expansion added JF806645 and word-bounded UID 334361390. Both found the same three own taxonomy/name/scope rows, all fully read. Numeric boundaries prevent treating another identifier's embedded digits as this taxon. Five SOURCE.json files were separately fully parsed without a target match, and history filenames independently inventoried.

Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. PubMed HCZ42/JF806645/JF806645.1 search returned zero with quoted-phrase warnings. Exact-accession web search was empty; strain searches yielded taxonomy and paper leads. These bounded searches do not prove universal genome or literature absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Pinned and live authorities support the identity and lineage; stored evidence does not misrepresent comparison species or unrelated sequences.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Authoritative taxonomy corrections belong first at NCBI and then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection changes belong in `src/taxonmech/seed.py` with regression tests; admission changes belong in `curation/seed_scope.tsv`. Optional enrichment requires supported maintained-input/model behavior, not hand-edited output.

## Follow-up Checks

No corrective follow-up for current claims. Any literature enrichment should establish an explicit strain/accession/deposit chain and visually verify the original table/figure. The inspected author-hosted HTML is not visual verification of the original PDF; prior related-record PDF/figure requests were inaccessible.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036515`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The review skill and field checklist governed this individual review. No verdict or sequence identity was inherited from an adjacent record.

Before/after SHA-256: `f4b7c06788df7983ac8fb6fc828d981bfad843dcb9e0476f76a8f3bfb62087ec`. Only this new report was written for this target. YAML, source inventories, history, status, generated pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
