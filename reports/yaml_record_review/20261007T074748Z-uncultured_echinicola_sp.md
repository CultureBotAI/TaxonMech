# YAML Record Review: uncultured Echinicola sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_echinicola_sp.yaml`
- Started UTC: 2026-10-07T07:44:46Z
- Finished UTC: 2026-10-07T07:47:48Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035616`, uncultured Echinicola sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:1035615`, twelve root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. This is an environmental taxon, not one cultured isolate. Generated YAML is read-only; maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes. Scope and slug ownership are in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/uncultured_echinicola_sp.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/uncultured_echinicola_sp.yaml --out /private/tmp/ec-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/ec-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven source inventories, path, scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 5, all metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. There are no literature/internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact; none is created here.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222144` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31624` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14644` and `curation/seed_scope.tsv:322411`.

All twelve ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms species rank, parent 1035615, genetic code 11, no alternate names and eleven non-root ancestors; Datasets confirms the same chain including root. Cytophagia/Cytophagales/Cyclobacteriaceae/Echinicola and the environmental-samples parent agree. NCBI's Environmental samples division does not change the bacterial domain. No retirement or replacement was found in the inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035616&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035616)

`EXACT` grounds the NCBI concept, not a validly published binomial, a single biological species or identity among all environmental sequences filed here.

## Evidence

The sole `NCBITAXON` attestation agrees on exact ID and label, count 1, unit `NAME` and snapshot note. It is not a count of sequences or strains. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

All five exact-taxid nuccore results were read as complete GenBank metadata, omitting only sequence strings and translation/transcription payloads. Every record explicitly names the target and `taxon:1035616`, marks environmental sampling, and carries a partial 16S rRNA feature with both ends incomplete.

| Accession | Length | Source identity/context |
| --- | --- | --- |
| `KT943983.1` | 763 nt | Clone BB57; Baiyanggou mud volcano. |
| `JX193133.1` | 990 nt | Clone AS_I_75; mangrove soil, India: Sundarban. |
| `JX007819.1` | 426 nt | Clone AS_I_75; mangrove soil, India: Sundarban. |
| `JQ040624.1` | 615 nt | Clone AS_11; Sundarban mangrove soil, India. |
| `JF729941.1` | 312 nt | DGGE gel band 1B735; bioremediated high-arctic soil from a diesel-spill area, collected 2005. |

These are marker accessions, not genomes or culture-collection deposits. The two AS_I_75 accessions remain distinct records; a shared clone name does not prove identical sequences. No culture-collection, BioSample, BioProject or assembly linkage is supplied in the inspected metadata. Each has an unpublished study citation and a direct submission, with no linked DOI or PMID. No taxon-wide habitat, metabolism or diesel-degradation claim follows from sample context. [KT943983.1](https://www.ncbi.nlm.nih.gov/nuccore/KT943983.1), [JX193133.1](https://www.ncbi.nlm.nih.gov/nuccore/JX193133.1), [JX007819.1](https://www.ncbi.nlm.nih.gov/nuccore/JX007819.1), [JQ040624.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ040624.1), [JF729941.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729941.1)

The complete native assembly row at `data/catalog/ncbi_genbank-0063.jsonl.gz:17929` is a numeric collision: `genome_size_ungapped: 1035616`. It describes GCA_964433765.1, an uncultured Candidatus Bathyarchaeia archaeon with taxid/species_taxid 3037984 and BioSample SAMEA117124792. It supplies no Echinicola genome link and was not joined to this record.

No gene, regulator, pathway, stress-response or transcriptomics assertion in this YAML requires an iModulonDB lookup. The adapter is not applicable; its absence is not negative biological evidence.

## Completeness

Zero BacDive strains and the optional omissions agree with inspected source scope. Environmental clones and a DGGE band do not establish missing cultured strains. Record-level literature evidence is optional for seeded records. No required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The identity stage used taxid 1035616, exact label and slug, finding four lines: backbone, scope, native name and the unrelated assembly row. All were read completely. The expanded stage searched all five marker accessions with optional .1 versions and found no lines. Neither stage found matching source-metadata values or history paths. These negative findings include ignored files and are bounded to the specified roots and terms.

The exact-taxid Assembly zero carries a phrase-not-found warning and does not exclude genomes filed under another identity. The exact-label/taxid web search returned no result; this is not independent proof of absence. Study publications beyond the inspected GenBank references and nucleotide sequence similarity were not investigated.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, full lineage, source attestation, zero strain count and seed history agree. The five environmental markers and the unrelated numeric catalog hit do not justify additional strain/genome links.

## Recommended Edits

None required. Do not patch generated YAML, treat environmental clone labels as culture accessions, count markers as genomes, or promote `SEEDED` to `REVIEWED`.

A later authorized taxonomy-source refresh belongs in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, followed by guarded seeding. Optional literature or provenance annotations require maintained-input support merged by `src/taxonmech/seed.py` with tests under `docs/CURATION.md`. Habitat and phenotype assertions belong in their corresponding sibling corpora with claim-specific evidence.

## Follow-up Checks

- Require an exact culture-deposit and genome-source chain before adding strain/genome identifiers; do not match taxids against arbitrary numeric fields.
- Preserve the five marker accessions as distinct nucleotide records unless direct evidence establishes a relationship.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

The NCBI browser page was inaccessible through the web tool; primary EFetch and Datasets reads succeeded. No failure was treated as negative identity evidence.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date; all three manifest timestamps and the selection code were inspected.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new repository report is added for this review; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
