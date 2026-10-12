# YAML Record Review: Burkholderia sp. BSF2(21)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsf2_21.yaml`
- Started UTC: 2026-10-10T06:35:49Z
- Finished UTC: 2026-10-10T06:38:31Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037591`, Burkholderia sp. BSF2(21). It is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried strains, one NCBI name attestation, and a seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future fixes; generated YAML must not be hand-edited.

## Validation

Used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsf2_21.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsf2_21.yaml --out /private/tmp/taxonmech-bsf221-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured source comparisons passed for identity, full lineage, synonyms, genetic code, attestation, unique path, scope reason, and seed-event wording. These are not full corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph nodes or ontology-grounded causal claims. No separately documented focused term/reference validator applies; taxon references were checked directly.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and site rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222806` matches the ID, name, species rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. The full root-first lineage matches individual backbone rows: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784. All labels and ranks agree.

Complete live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037591&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037591), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037591) agree. EFetch ancestry omits root while Datasets includes it. Datasets omits an assembly count, which does not establish zero assemblies. The species-ranked placeholder is compatible with a strain-qualified sequence; neither establishes formal species nomenclature or a collection deposit. No inferred reclassification is warranted.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32442` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15359` uniquely resolves the identifier/slug; `curation/seed_scope.tsv:323021` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. No human review promotion is claimed.

## Evidence

The attestation correctly counts one NCBI `NAME`, not a strain, genome, publication, or assay. Structured comparisons found no own rows in the seven pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories. Empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains does not imply unculturability or absence of a biological isolate.

Exact live Nucleotide search `txid1037591[Organism:exp]` returned one UID, `345019017`. The complete [GenBank annotation JF779766.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779766.1) directly joins the exact organism, strain BSF2(21), and `taxon:1037591`. It is a 450-base partial 16S rRNA gene, incomplete at both ends, annotated from fertilized bulk soil in a beech forest. Actual/declared length and A/C/G/T checks passed; lowercase-sequence SHA-256 is `25a5ac0188abe00393c73d11f80a3ee78bb22170b43f91ffccd6dabc8e6a1270`. This marker is not an assembly. No collection country/date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not sampling metadata.

A fresh paired retrieval of the complete annotations for JF779766.1 and [JF779769.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779769.1) confirmed identical 450-base marker checksums and transcription sequences but different source identities. JF779769.1 carries strain BSF2(12), `taxon:1037588`, and UID 345019020; it is not BSF2(21)'s accession. Shared partial 16S sequence, habitat qualifier, and citation do not establish isolate identity, synonymy, or whole-genome equivalence. No merge or cross-transfer is justified.

The target annotation directly cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. The [HAL author deposit](https://hal.science/hal-02916138v1), whose complete requested metadata and abstract were inspected earlier in this turn, confirms DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). BSF2(21)-specific assay results remain unverified; full text was not inspected. No mineral-weathering, chitin-degradation, iron-release, or plant-growth phenotype was inferred from the citation, cohort, genus, or other isolate.

Both other local catalog hits were read completely:

- `data/catalog/ncbi_genbank-0046.jsonl.gz:41546` is Acinetobacter baumannii (`taxid 470`), strain AB30, isolate 10UC200017655, `GCA_050715935.1`, `SAMN41037591`, `PRJNA514245`, `DBIYSG000000000.1`. The match lies inside its BioSample. Its PMID 30286803 is not a target citation.
- `data/catalog/allthebacteria.tsv.xz:1716823` is Escherichia coli, `SAMN13162632`, `ERZ25668012`, run `SRR10375916`, with PASS filters and an available FASTA. The run substring is not a taxonomic or strain link to this record.

Neither supports a target-linked assembly, culture deposit, synonym, or extra attestation.

## Completeness

Ran `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, source organism/designation, and parenthesis/space/hyphen variants. An expanded pass added `JF779766`, comparison accession `JF779769`, DOI suffix `soilbio.2011.07.010`, and publisher ID `S003807171100280X`. Both returned five lines: own backbone, scope, name, and the two unrelated rows. Ignored and compressed files were included. No extra target-linked assertion, strain/genome association, or history artifact was established on these bounded surfaces.

Independently enumerated and fully parsed all five source `SOURCE.json` files for the expanded pattern; none matched. Ignored-independent filename scans found the exact target YAML and no pre-existing target report/history filename. Eukaryota YAML contents were not opened. Exact organism and accession web queries supplied taxonomy/near-name leads or no accession result; no snippet supported a scientific claim. The directly cited study's author deposit was inspected as above.

Optional source/literature enrichment does not require filling every optional slot or constructing a graph. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The taxonomy/name-only assertions agree with inspected pinned and live sources. The identical short marker on a differently designated isolate is not itself a record defect. Unverified isolate-level assays and unavailable full text limit optional enrichment, not the claims made here.

## Recommended Edits

None required. Do not hand-edit generated YAML, append a curation event, or promote status. Future verified literature/strain enrichment belongs in maintained source inputs or an explicitly supported curation overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`. Preserve BSF2(21), keep partial markers outside genome counts, and do not merge this record with BSF2(12) from marker equality alone.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and isolate-level table, explicitly resolve BSF2(21)/JF779766, and verify assay conditions/results without borrowing BSF2(12)'s results. New deposit/genome associations require an explicit source chain. After authorized maintained-input changes, rerun focused schema/strict/history validation and the documented dry run, seed canary, corpus reproduction, and full quality gates. Human sign-off is separately required for review-status promotion.

## Additional Notes

Direct taxonomy-browser retrieval succeeded and all 74 parsed text lines were read. The shared HAL metadata and abstract were inspected earlier this turn. Earlier shared-paper access checks found ScienceDirect 403 and an ISTEX redirect returning institutional-authentication HTML instead of PDF; those routes were not repeatedly retried. No login, paid access, or full-text reading occurred.

YAML SHA-256: `22867abbaa52cf243a294d578156dfec3e5f05b6759c4e145d81f682e19f2067`. Only this new report was written for the target. Maintained sources, generated data, schema, history, site, GitHub state, Eukaryota, and existing worktrees were unchanged.
