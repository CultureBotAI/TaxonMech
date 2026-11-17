# YAML Record Review: Actinoallomurus sp. KLBMP 03562

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/actinoallomurus_sp_klbmp_03562.yaml`
- Started UTC: 2026-10-08T21:49:04Z
- Finished UTC: 2026-10-08T21:52:19Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036473`, Actinoallomurus sp. KLBMP 03562. It asserts species rank, Bacteria domain, parent `NCBITaxon:2624323`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero BacDive strain records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/actinoallomurus_sp_klbmp_03562.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/actinoallomurus_sp_klbmp_03562.yaml --out /private/tmp/klbmp03562-strict.tsv`: passed, one file and zero errors. Complete diagnostic TSV was header-only.
- Structured comparisons checked the complete backbone row, all ten ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing confirmed declared versus actual sequence length, equality with its submitted rRNA transcription annotation and absence of non-ACGT symbols. This is annotation consistency, not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused replacement was invented for a corpus-wide gate.

## Identity and Grounding

The complete [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036473&retmode=xml) agrees with the ID, label, species rank, parent 2624323 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036473) confirms all ten root-first ancestor IDs. Labels and ranks agree with the pinned lineage through Bacillati, Actinomycetota, Actinomycetes, Streptosporangiales, Thermomonosporaceae, Actinoallomurus and unclassified Actinoallomurus. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

Species rank here is the authority's rank for an unnamed strain-associated taxon, not evidence of a formally described species. Exact grounding means this precise NCBI identity, not equivalence with a named congener. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete native source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222475`: identity, rank, parent, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32019`: exact scientific-name object, empty unique-name field.
- `data/taxa/PATHS.tsv:14982`: ID and slug.
- `curation/seed_scope.tsv:322722`: date and one-source admission reason matching the seed event.

The attestation unit is `NAME`, not strain, assembly or experiment. Full exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. The schema's `strain_count` definition and the seeder's BacDive collection logic were read: zero means zero represented BacDive records, not a denial that a named strain exists.

Two additional catalog search matches were inspected completely and excluded:

- `data/catalog/gtdb_genomes-0012.jsonl.gz:30723` is `RS_GCF_028623165.1`, Nostoc sp. UHCC 0926, taxid/species taxid 3025190. Only scaffold N90 equals 1036473; total and ungapped length are 8314159. Neither this assembly nor its `GCA_028623165.1`, `SAMN33005007` or `PRJNA224116` references establish a target link.
- `data/catalog/ncbi_genbank-0050.jsonl.gz:47139` is `GCA_055149635.1`, Candidatus Altimarinota bacterium, taxid/species taxid 2044595, isolate PMN_IN_RPW1_bin.13. Genome size and ungapped size equal 1036473. Its `SAMN50305468`, `PRJNA308326` and `JBSRLS000000000.1` identifiers likewise belong to that unrelated record.

Exact non-expanded Nuccore query `txid1036473[Organism:noexp]` returned one record, UID 334303289. The complete [JF803765.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803765.1) identifies this taxon and strain KLBMP 03562. It is a 671-base partial 16S rRNA sequence, with both ends marked partial, from rhizosphere associated with Pinus massoniana in China: Panzhihua. No culture-deposit qualifier or assembly cross-reference is supplied. Its source and rRNA features were read fully; there is no CDS feature. The actual sequence length and submitted transcription agree, without ambiguous nucleotide symbols.

The sequence cites an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin, plus a direct submission dated 11-APR-2011, with no study PMID or DOI. A study title does not demonstrate that this strain successfully controls disease. A partial ribosomal marker is not a genome, functional-gene assay or basis for reassignment to a named species.

Web searches covered the spaced/compact strain designation, genus plus strain number, both accession forms and the unpublished study title. They surfaced taxonomy listings and unrelated antioxidant/biocontrol material, not an inspected exact-strain experiment. The [Genome.jp taxonomy summary](https://www.genome.jp/tools-bin/taxsummary?col=species&id=85012) contains the label; its link was followed to [NCBI taxon 1036473](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036473). This is an NCBI link-out, not independent genomic or functional evidence. Search snippets about other KLBMP strains were not adopted as evidence.

## Completeness

Complete enough for its supported taxonomy-seed scope. Optional nomenclature, synonyms, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. The external strain designation and ribosomal sequence do not require inventing a BacDive entry or adding a genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain-designation variants and JF803765 with optional version. The five matched rows were read completely: three identity/scope rows and the two numerical collisions above. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. The PubMed query `"KLBMP 03562"[All Fields] OR "JF803765"[All Fields]` returned zero with quoted-phrase warnings. These are bounded query outcomes, not universal genome or literature absence. No strain-genome chain was established.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. The external ribosomal marker does not establish such coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. Limited external characterization and unsupported candidate joins do not make the taxonomy seed incorrect.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not import the two catalog collisions, infer strain equivalence from the KLBMP prefix, assign a formal species from a partial marker, or promote the unpublished study title into a biocontrol phenotype.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence or source-context enrichment requires maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Before optional enrichment, inspect primary evidence explicitly linking this strain to a proposed deposit, genome or experiment, keeping sequence, sample, project and genome identifiers distinct.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036473`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The single-record skill and checklist governed the review. CLAUDE.md, justfile and curation ownership guidance were reread at the unchanged HEAD. Before/after YAML SHA-256 was `7ff3b0e9e8eca56263862e7a9835c01cd583ae190ca5f8ecdac20b6f7f20799c`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
