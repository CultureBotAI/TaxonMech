# YAML Record Review: Burkholderia sp. BSF1(25)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsf1_25.yaml`
- Started UTC: 2026-10-10T06:21:24Z
- Finished UTC: 2026-10-10T06:23:38Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037587`, Burkholderia sp. BSF1(25). It is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` mapping status, genetic code 11, zero inventoried strains, one NCBI name attestation, and a seed event. Future fixes belong in maintained inventories or `curation/seed_scope.tsv`, interpreted by extraction/seeding code, not in the generated YAML.

## Validation

Used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsf1_25.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsf1_25.yaml --out /private/tmp/taxonmech-bsf125-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured source comparisons passed for identity, complete lineage, synonyms, code, attestation, unique path, scope reason, and seed-event wording. These do not prove corpus reproduction.
- `just validate-products`: not applicable; the record has no curator-added graph nodes or ontology-grounded causal claims. No separately documented focused term/reference validator applies; taxon references were checked directly.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and site rendering. Full-corpus gates were not run for this read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222802` matches the ID, exact name, species rank, parent, code, and 2026-09-13 snapshot. Synonym and retirement fields are empty. Individual backbone rows agree with every root-first lineage entry: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784. All labels and ranks match.

The complete live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037587&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037587), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037587) agree. EFetch ancestry omits root; Datasets includes it. Datasets omits an assembly count, which is not a zero count. Species rank and a strain-qualified sequence are compatible here; neither proves a formally named species or collection deposit. No inferred reclassification is needed.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32438` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15355` uniquely resolves the identifier/slug; `curation/seed_scope.tsv:323017` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. No human review promotion is claimed.

## Evidence

The source attestation correctly counts one NCBI `NAME`, not a strain, assembly, publication, or assay. The seven pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories contain no own rows in structured comparisons. Empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains does not imply that no isolate exists or that it is unculturable.

Exact live Nucleotide search `txid1037587[Organism:exp]` returned one UID, `345019019`. The complete [GenBank annotation JF779768.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779768.1) directly joins the exact organism label, strain BSF1(25), and `taxon:1037587`. It is a 450-base partial 16S rRNA gene, incomplete at both ends, annotated from fertilized bulk soil in a beech forest. Actual/declared length and A/C/G/T checks passed; lowercase-sequence SHA-256 is `2d6200b8cf759484e1e0441ab0647cc904950c45b2e846a1902e37f350c1e0f8`. This marker is not a genome assembly. The annotation supplies no collection country/date, coordinates, or deposit qualifier. Its 5 April 2011 submission date and INRA Champenoux address are not collection metadata.

The sequence directly cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study in Soil Biology and Biochemistry 43(11):2275-2282. The [HAL author deposit](https://hal.science/hal-02916138v1), whose complete requested metadata and abstract were read through its public API earlier this turn, confirms DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). No BSF1(25)-specific assay result was verified. Full text was not inspected. The citation supports literature provenance, not an inferred mineral-weathering, chitin-degradation, iron-release, or plant-growth phenotype for this isolate.

The only other catalog hit, `data/catalog/ncbi_genbank-0016.jsonl.gz:23704`, was read completely. It describes Gemmiger sp. (`taxid/species_taxid 2049027`), metagenomic isolate Go_UH_bin_215, `GCA_017996195.1`, `SAMN18120173`, `PRJNA524094`, `JAGOHI000000000.1`, with exclusion reasons indicating a fragmented metagenome-derived assembly. The match is `genome_size_ungapped: 1037587`; total genome size is 1038797. The number is a length, not a taxonomic link. This row supplies no target assembly, deposit, synonym, or additional attestation.

## Completeness

Ran `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, source name/designation, and parenthesis/space/hyphen variants. An expanded pass added `JF779768`, DOI suffix `soilbio.2011.07.010`, and publisher ID `S003807171100280X`. Both passes returned four lines: own backbone, scope, scientific name, and the excluded Gemmiger row. Ignored and compressed files were included. No additional target-linked assertion or strain/genome/history association was established on these bounded surfaces.

Independently enumerated and fully parsed all five source `SOURCE.json` files for the expanded pattern; none matched. Ignored-independent filename scans found the exact YAML and no pre-existing target report/history filename. Eukaryota YAML contents were not opened. Exact-name and accession web searches returned taxonomy/near-name leads or no accession result; no search snippet supplied a scientific claim. The directly cited study was checked against the inspected author deposit as above.

Optional literature/source-context enrichment does not require filling every optional field or constructing a graph. iModulonDB is not applicable because this record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The current taxonomy/name-only assertions agree with the inspected pinned and live evidence. Unverified isolate-specific assays and unavailable full text are review limitations, not defects in claims the record does not make.

## Recommended Edits

None required. Do not hand-edit generated YAML, append a curation event, or promote status. Future verified literature/strain enrichment belongs in maintained source inputs or an explicitly supported curation overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`. Preserve BSF1(25) and do not count the partial marker as an assembly.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and any isolate-level table, resolve BSF1(25)/JF779768 explicitly, and verify assay conditions/results. A new genome/deposit association requires an explicit source chain. After authorized maintained-input changes, rerun focused schema/strict/history validation and the documented dry run, seed canary, corpus reproduction, and full quality gates. Human sign-off remains separate from this report.

## Additional Notes

Direct taxonomy-browser retrieval succeeded and all 74 parsed text lines were read. HAL metadata/abstract were inspected earlier in this turn. Earlier shared-paper access checks found ScienceDirect 403 and an ISTEX redirect returning institutional-authentication HTML instead of PDF; these routes were not repeatedly retried. No login, paid access, or full-text reading occurred.

YAML SHA-256: `f4385773adbe001d55a736252f7d1096b8effa1b2467e06505969904921218b2`. Only this new report was written for this target. Maintained inputs, generated data, schema, history, site, GitHub state, Eukaryota, and existing worktrees were unchanged.
