# YAML Record Review: Burkholderia sp. BSF2(18)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsf2_18.yaml`
- Started UTC: 2026-10-10T06:32:22Z
- Finished UTC: 2026-10-10T06:34:33Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037590`, Burkholderia sp. BSF2(18). This is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried strains, one NCBI name attestation, and a seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future fixes; do not hand-edit generated YAML.

## Validation

Used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsf2_18.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsf2_18.yaml --out /private/tmp/taxonmech-bsf218-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured source comparisons passed for identity, complete lineage, synonyms, code, attestation, unique path, scope reason, and seed-event wording. They do not prove full corpus reproduction.
- `just validate-products`: not applicable; there are no curator-added graph nodes or ontology-grounded causal claims. No separately documented focused term/reference validator applies; taxon references were checked directly.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and site rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222805` agrees on ID, exact name, species rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. The full root-first lineage matches individual backbone rows: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784. Every label and rank agrees.

Complete live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037590&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037590), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037590) agree. EFetch ancestry omits root while Datasets includes it. Datasets omits an assembly count, which is not evidence of zero assemblies. A strain-qualified sequence is compatible with this species-ranked placeholder; neither establishes a formally named species or culture deposit. No inferred reclassification is warranted.

The complete native name row at `data/catalog/ncbi_names-0005.jsonl.gz:32441` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15358` uniquely resolves the identifier and slug; `curation/seed_scope.tsv:323020` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. The record claims no human review promotion.

## Evidence

The attestation correctly counts one NCBI `NAME`, not a strain, assembly, paper, or assay. Structured comparisons found no own rows in the seven pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories. Empty optional strain/nomenclature/mapping sections agree with those inputs. Zero inventoried strains does not imply unculturability or absence of a biological isolate.

Exact live Nucleotide search `txid1037590[Organism:exp]` returned one UID, `345019018`. The complete [GenBank annotation JF779767.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779767.1) directly joins the exact organism, strain BSF2(18), and `taxon:1037590`. It describes a 450-base partial 16S rRNA gene, incomplete at both ends, annotated from fertilized bulk soil in a beech forest. Actual/declared length and A/C/G/T checks passed; lowercase-sequence SHA-256 is `091897b1fa0581af48fcd4149a7e7477044bfd5e36ec6d2a51b929aad47dc39c`. This marker is not a genome assembly. The annotation has no collection country/date, coordinate, or deposit qualifier. The 5 April 2011 submission and INRA Champenoux address are not sampling metadata.

The sequence directly cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. Complete requested [HAL author-deposit metadata and abstract](https://hal.science/hal-02916138v1), retrieved and read earlier in this same turn, independently confirm the exact citation and DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). BSF2(18)'s individual assay result remains unverified; full text was not inspected. No mineral-weathering, chitin-degradation, iron-release, or plant-growth phenotype was transferred from the paper title, cohort, genus, or neighboring accession.

All six non-target catalog rows were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7604` is Francisella tularensis subsp. holarctica (`taxid 119857`, species 263), strain 14T0097, `GCA_010375905.1`, `SAMN12576347`, `PRJNA560345`, `JAAGIS000000000.1`. The matching number is assembly name `ASM1037590v1`.
- `data/catalog/ncbi_genbank-0017.jsonl.gz:47023` is Escherichia coli (`taxid 562`), strain `1037590`, `GCA_019538775.1`, `SAMN20550919`, `PRJNA315192`, `ABBUED000000000.1`.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41513` is Acinetobacter baumannii (`taxid 470`), strain AB16, isolate 10RC190002689, `GCA_050715275.1`, `SAMN41037590`, `PRJNA514245`, `DBIYRI000000000.1`. Its PMID 30286803 is not a target citation; the match lies within its BioSample.
- `data/catalog/ncbi_genbank-0051.jsonl.gz:17611` and `data/catalog/ncbi_refseq-0008.jsonl.gz:23607` concern Streptomyces avermitilis (`taxid 33903`), strain NPDC034003, paired `GCA_055575835.1` / `GCF_055575835.1`, `SAMN55300887`, `JBVIRV000000000.1`. The match is a substring of ungapped genome length `10375904`, not a taxon link.
- `data/catalog/ncbi_genbank-0059.jsonl.gz:21385` is uncultured Clostridia bacterium (`taxid 244328`), isolate SRR11551377_bin.3_metaWRAP_v1.3_MAG, `GCA_946056945.1`, `SAMEA110446536`, `PRJEB53634`, `CAMGLF000000000.1`. Its genome length and ungapped length are both `1037590`; it is metagenome-derived, not this Burkholderia isolate.

These matches do not support a target-linked assembly, deposit, synonym, or extra attestation.

## Completeness

Ran `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered ID, exact slug, source organism/designation, and parenthesis/space/hyphen variants. An expanded pass added `JF779767`, DOI suffix `soilbio.2011.07.010`, and publisher ID `S003807171100280X`. Both returned nine lines: own backbone, scope, scientific name, and six unrelated rows. Ignored and compressed files were included. No extra target-linked assertion, strain/genome association, or history artifact was established on these bounded surfaces.

Independently enumerated and fully parsed the five source `SOURCE.json` files for the expanded pattern; none matched. Ignored-independent filename scans found the exact YAML and no pre-existing target report/history filename. Eukaryota YAML contents were not opened. Exact organism and accession web queries supplied taxonomy/near-name leads or no accession result; no snippet supported a scientific claim. The directly cited paper's author deposit was inspected as above.

Optional literature/source enrichment does not require filling every optional field or creating a graph. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The taxonomy/name-only assertions agree with inspected pinned and live sources. Unverified isolate-level assays and unavailable full text are review limitations, not defects in claims the record does not make.

## Recommended Edits

None required. Do not hand-edit generated YAML, append a history event, or promote status. Verified future literature/strain enrichment belongs in maintained source inputs or an explicitly supported curation overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`. Preserve BSF2(18) and keep marker sequences outside genome counts.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and isolate-level table, explicitly resolve BSF2(18)/JF779767, and verify assay conditions/results. A future genome/deposit association requires an explicit source chain. After authorized maintained-input edits, rerun focused schema/strict/history validation and the documented dry run, seed canary, corpus reproduction, and full quality gates. Human sign-off is separately required for review-status promotion.

## Additional Notes

Direct taxonomy-browser retrieval succeeded and all 74 parsed text lines were read. The shared HAL metadata/abstract were inspected earlier this turn. Earlier shared-paper access checks found ScienceDirect 403 and an ISTEX redirect returning institutional-authentication HTML instead of PDF; those routes were not repeatedly retried. No login, paid access, or full-text reading occurred.

YAML SHA-256: `53147f411f4f774564d231cf77ca86525ff5d86ab392d7501f83f14bfda2a26e`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, site, GitHub state, Eukaryota, and existing worktrees were unchanged.
