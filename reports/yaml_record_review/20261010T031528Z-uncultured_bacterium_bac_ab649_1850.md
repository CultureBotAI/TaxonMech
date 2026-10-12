# YAML Record Review: uncultured bacterium BAC AB649/1850

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_bacterium_bac_ab649_1850.yaml`
- Started UTC: 2026-10-10T03:12:01Z
- Finished UTC: 2026-10-10T03:15:28Z
- Verdict: pass

## Target

The entire 36-line generated `TaxonRecord` was read. `NCBITaxon:1037453` denotes uncultured bacterium BAC AB649/1850, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:48479` environmental samples, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

It contains four ancestors, zero inventoried culture strains, one NCBITAXON name attestation and one seed event. It makes no nomenclature, synonym, GTDB, strain-deposit, genome, phenotype or causal-graph assertion. The environmental clone designation must not be interpreted as an independently cultured species or culture-collection accession.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_bacterium_bac_ab649_1850.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/uncultured_bacterium_bac_ab649_1850.yaml --out /private/tmp/taxonmech-bacAB649-20261010-validation.tsv --workers 1`: one file, zero errors. The output was reread and is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured scans verified identity, every ancestor, genetic code, empty source synonyms, the seven inventories, unique index/scope resolution and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Full native NCBI name, GOLD organism/project and unrelated GTDB hit were inspected. Live NCBI browser, EFetch taxonomy, Datasets, nucleotide search and complete nucleotide annotations were read. Nucleotide length and sequence hash were checked; protein translations were reduced to lengths/hashes, without protein-function adjudication.
- PubMed metadata and abstract were read, together with the primary paper's two-page extracted text. PDF screenshot retrieval was not reliable, so no figure-level validation is claimed. The MIBiG page was unavailable and was not needed for the verdict.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`.
- Live GOLD organism/project pages failed through the web reader and returned HTTP 403 to direct read requests. GOLD evidence below is from the pinned native projection, not independently verified current website content.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222751` and the [NCBI taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037453) agree on the exact name, species rank and code 11. [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037453&retmode=xml) confirms parent 48479; [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037453) supplies the complete ID chain including root 1.

The four ancestors are root, cellular organisms, Bacteria and environmental samples. The last is correctly `NO_RANK`; it is not a named genus or a habitat ontology assertion. The bacterial domain follows ancestry even though EFetch's sequence division is Environmental samples. Preserve this short NCBI chain instead of inventing phylum, class or genus placements.

`data/catalog/ncbi_names-0005.jsonl.gz:32389` is the full scientific-name row with an empty unique-name qualifier. No source synonym is asserted. NCBI's species-rank placeholder is eligible under the repository scope rule; it does not imply a validly published binomial, type strain or recovered organism. Exact grounding is limited to that taxonomic entity.

## Evidence

The NCBITAXON one-NAME assertion and 2026-09-13 snapshot note agree with the pinned backbone. The source-count inventories contain no additional own attestation. Zero inventoried strains does not imply zero sequence evidence.

The live nucleotide search returns one record, UID 332380581, [HM193369.1](https://www.ncbi.nlm.nih.gov/nuccore/HM193369.1). Its 66,898-base linear sequence is annotated as a complete fluostatin biosynthetic gene cluster, not a complete organism genome. The source feature explicitly links `taxon:1037453` and clone `BAC AB649/1850`, with environmental-sample and soil annotations from southern California's Anzo Borrego Desert. Declared and observed sequence lengths agree, with alphabet `acgt`. The record's references retain an unpublished cluster entry and a 2010 direct submission; they are not themselves a PMID citation.

The independently located [primary paper](https://bradylab.rockefeller.edu/wp-content/uploads/2022/11/77.pdf), DOI [10.1021/ja104550p](https://doi.org/10.1021/ja104550p), is linked by [PMID 20690632](https://pubmed.ncbi.nlm.nih.gov/20690632/). Its text explicitly identifies HM193369 and describes reconstruction of overlapping environmental clones AB649 and AB1850 followed by heterologous expression in Streptomyces albus. This supports the clone provenance, not identity of the uncultured donor with the expression host or a cultured donor phenotype. Its description of a greater-than-70-kb BAC and the deposited 66,898-base sequence concern different reported objects; neither establishes a whole genome, and they should not be silently equated.

The complete native GOLD rows provide an exact source-specific organism/project chain:

- `data/gold/organisms.jsonl.gz:56470`: `Go0098472`, Uncultured bacterium BAC AB649/1850, NCBI taxon 1037453, source strain text `BAC AB649/1850`, empty culture-collection field.
- `data/gold/projects.jsonl.gz:57295`: `Gp0098472`, the same project name, linked to `Go0098472`, with empty NCBI BioSample and BioProject fields.

No analysis row matching these IDs was found in the ignored-inclusive compressed search. These rows do not provide a culture deposit or genome accession. The organism and project IDs are not genomes. Their presence in the native catalog does not contradict the empty transformed `gold_organisms.tsv` count inventory: `src/taxonmech/extract.py:676` builds that count from a separate kg-microbe graph input, while the native projection feeds deposit-linked relationships. This is a source-coverage distinction, not evidence that the YAML omitted a required strain-genome join.

The only GTDB numeric hit, `data/catalog/gtdb_genomes-0015.jsonl.gz:42854`, is `RS_GCF_001953715.1`, Enterococcus faecium ISMMS_VRE_6, taxon 1352. Its contig N50 is 1,037,453 bases. That number is not this record's taxon identifier and supplies no GTDB mapping.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial pattern included bounded taxon ID, slug and clone designation with punctuation variants. An expanded search included `Go0098472`, `Gp0098472`, `HM193369`, PMID 20690632, DOI suffix `ja104550p` and the MIBiG search lead `BGC0000223`. Both searches returned the same six lines: backbone, scope, name, native GOLD organism/project and unrelated GTDB statistic.

Complete source-inventory scans found no own BacDive, LPSN, GTDB, GOLD-count, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements are bounded to the inspected repository sources.

`src/taxonmech/gold_genomes.py:105` and `docs/STRAIN_GENOMES.md` require an existing, eligible culture-deposit match before emitting native GOLD strain relationships; the extractor deliberately skips organisms with no match. An environmental BAC name and a taxon match do not satisfy that contract. The current schema places these source relationships under actual strain entries, not an invented strain container. Leaving strains/genomes empty is therefore appropriate.

The gene-cluster accession and paper are useful future taxon-level context, not required genome fields. No causal graph or individual functional-gene assertion is present to adjudicate. iModulonDB is not applicable to the reviewed taxonomy/name assertion; the heterologous-expression host is not a substitute organism for this record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None established. Identity, lineage, scope, source count and seed audit agree with the checked sources. The environmental sequence and native GOLD records add context but do not establish a missing required culture or genome link. Live GOLD status and any broader primary-source enrichment remain outside the verified scope.

## Recommended Edits

No correction to the generated YAML is justified. Preserve the NCBI name/rank, environmental lineage, zero represented culture count, `SEEDED` status and existing history. Do not turn the BAC into a culture deposit, a full-genome assembly or an exact synonym of Streptomyces albus.

If taxon-level non-genome sequence and bibliographic enrichment is separately requested, it needs an explicit maintained schema/extraction/seeding design with provenance and regression tests. Do not force HM193369.1 or the GOLD organism/project IDs into genome slots or manufacture a BacDive strain. Any change to the transformed GOLD count belongs in the upstream mapping/extraction inputs, not a hand-edited record.

## Follow-up Checks

Resolve the GOLD pages when accessible and reconcile their native projection with the frozen transformed graph only if extending the source-count coverage. Preserve the explicit organism/project chain and distinguish no linked analysis from a universal claim that none exists.

For any authorized enrichment, verify the exact clone/accession version, separate reconstructed cluster, BAC construct, heterologous host and uncultured source taxon, and retain the primary paper's evidence scope. Run focused schema/strict/history checks, the documented seed canary and then full corpus reproduction and QC. Supporting-information and individual protein-function review would be additional work, not checks completed here.

## Additional Notes

- YAML SHA-256: `4a718fdf639eb1f2c01b2b30f445eccaa650e08da4717728b00bffe33324f3dc`.
- HM193369.1 lowercase nucleotide-sequence SHA-256: `ad9df95fa3d9c59bab2125e7eaa24a703aa3ccc1b995bbf9a3bb7bfaa521acda`.
- `data/taxa/PATHS.tsv:15304` and `curation/seed_scope.tsv:322968` uniquely resolve the record. The scope was added 2026-09-13; the seed event retains 2026-09-13T17:54:04Z and the exact one-source NCBITAXON reason.
- The GOLD projection's workbook SHA-256 is `7d22ea3f2c9ac40d513cd4af1410f7d19f3525347eb272787ba1c20525340370`. Its SOURCE.json describes all-row identity/strain/taxon/project/genome projection; it is not the transformed count inventory.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was written for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened and no status was promoted.
