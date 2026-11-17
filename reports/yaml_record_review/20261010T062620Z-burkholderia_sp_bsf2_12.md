# YAML Record Review: Burkholderia sp. BSF2(12)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsf2_12.yaml`
- Started UTC: 2026-10-10T06:24:25Z
- Finished UTC: 2026-10-10T06:26:20Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1037588`, Burkholderia sp. BSF2(12). This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried strains, one NCBI name attestation, and a seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML must not be hand-edited.

## Validation

Used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsf2_12.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsf2_12.yaml --out /private/tmp/taxonmech-bsf212-20261010-validation.tsv --workers 1`: one file, zero errors; the inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured source comparisons passed for identity, every lineage label/rank, synonyms, genetic code, name attestation, unique path, scope reason, and seed-event wording. These are not full corpus reproduction.
- `just validate-products`: not applicable; there are no curator-added graph nodes or ontology-grounded causal claims. No separately documented focused term/reference validator applies; taxon references were checked directly.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and site rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222803` agrees on ID, exact label, species rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. The complete root-first chain matches individual backbone rows: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784. All labels and ranks match.

Complete live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037588&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037588), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037588) agree. EFetch ancestry omits root while Datasets includes it. Datasets omits an assembly count; it does not establish zero assemblies. A strain-qualified sequence is compatible with this species-ranked placeholder, but neither proves formal species nomenclature or a culture deposit. No hierarchy inference or genus reassignment is warranted.

The complete scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32439` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15356` uniquely resolves the identifier and slug; `curation/seed_scope.tsv:323018` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event. The record claims no human review promotion.

## Evidence

The attestation correctly counts one NCBI `NAME`, not a strain, genome, publication, or assay. Structured comparisons found no own rows in the seven pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories. Empty optional strain, nomenclature, and mapping fields are consistent with those inputs. Zero inventoried strains does not imply unculturability or absence of a biological isolate.

Exact live Nucleotide search `txid1037588[Organism:exp]` returned one UID, `345019020`. The complete [GenBank annotation JF779769.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779769.1) directly joins the exact organism name, strain BSF2(12), and `taxon:1037588`. It describes a 450-base partial 16S rRNA gene, incomplete at both ends, annotated from fertilized bulk soil in a beech forest. Actual/declared length and A/C/G/T checks passed; lowercase-sequence SHA-256 is `25a5ac0188abe00393c73d11f80a3ee78bb22170b43f91ffccd6dabc8e6a1270`. This is a marker, not a genome assembly. No collection country/date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission date and INRA Champenoux address are not sampling metadata.

The annotation directly cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. The [HAL author deposit](https://hal.science/hal-02916138v1), whose complete requested metadata and abstract were inspected through its public API earlier in this turn, confirms DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). BSF2(12)-specific assay results remain unverified; full text was not inspected. No mineral-weathering, iron-release, chitin-degradation, or plant-growth trait is inferred for this isolate from the citation, cohort, genus, or neighboring accession.

Both other native catalog hits were read completely:

- `data/catalog/ncbi_genbank-0014.jsonl.gz:13892` is Salmonella enterica subsp. enterica serovar Agama (`taxid 399581`, species 28901), strain `1037588`, `GCA_015740565.1`, `PDT000902040.1`, `SAMN16983212`, `PRJNA248792`, `AAXMIG000000000.1`.
- `data/catalog/ncbi_genbank-0054.jsonl.gz:17229` is Streptococcus pneumoniae (`taxid 1313`), isolate `1037588`, `GCA_058710385.1`, `PDT003121248.1`, `SAMEA120831692`, `PRJNA514245`, `DBOTCD000000000.1`. Its PMID 30286803 is not a target citation.

The matching strain/isolate numerals are not taxonomy links. Neither row supports a target genome, deposit, synonym, or extra attestation.

## Completeness

Ran `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns included numeric ID, exact slug, source organism/designation, and parenthesis/space/hyphen variants. The expanded pass added `JF779769`, DOI suffix `soilbio.2011.07.010`, and publisher ID `S003807171100280X`. Both returned five lines: own backbone, scope, name, and the two excluded genome rows. Ignored and compressed files were included. No extra target-linked assertion, strain/genome association, or history artifact was established on these bounded surfaces.

Independently enumerated and fully parsed all five source `SOURCE.json` files for the expanded pattern; none matched. Ignored-independent filename scans found the exact target YAML and no pre-existing target report/history filename. Eukaryota YAML contents were not opened. Exact organism and accession web queries supplied taxonomy and near-name leads or no accession result; no snippet was treated as scientific evidence. The directly linked study's author deposit was inspected as above.

Optional source-context enrichment is possible, but the checklist does not require every optional slot or a causal graph. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The taxonomy/name-only record agrees with inspected pinned and live sources. Unverified isolate-level assays and unavailable full text are review limitations, not defects in claims absent from the YAML.

## Recommended Edits

None required. Do not hand-edit generated YAML, append a history event, or promote status. Future verified literature/strain enrichment belongs in maintained source inputs or an explicitly supported curation overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`. Preserve BSF2(12) and keep partial marker sequences outside assembly counts.

## Follow-up Checks

Before adding functional claims, obtain the cited paper and isolate-level table, explicitly resolve BSF2(12)/JF779769, and verify assay conditions/results. Any later genome/deposit association requires an explicit source chain. After authorized maintained-input edits, rerun focused schema/strict/history validation and the documented dry run, seed canary, corpus reproduction, and full quality gates. Human sign-off is separately required for review-status promotion.

## Additional Notes

Direct taxonomy-browser retrieval succeeded and all 74 parsed text lines were read. HAL metadata and abstract were inspected earlier this turn. Earlier shared-paper access checks found ScienceDirect 403 and an ISTEX redirect returning institutional-authentication HTML instead of PDF; those failed routes were not repeatedly retried. No authentication, paid access, or full-text reading occurred.

YAML SHA-256: `3b5d5fec881c84d5950dff880acec70b13395018d5d302e2ae1d01e6c454b9e7`. Only this new report was written for this target. Maintained inputs, generated data, schema, history, site, GitHub state, Eukaryota, and existing worktrees were unchanged.
