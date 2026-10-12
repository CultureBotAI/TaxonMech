# YAML Record Review: Burkholderia sp. BSF3(9)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsf3_9.yaml`
- Started UTC: 2026-10-10T06:55:59Z
- Finished UTC: 2026-10-10T06:59:26Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1037595`, Burkholderia sp. BSF3(9). It is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried strains, one NCBI name attestation, and a seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future fixes; the generated YAML must not be hand-edited.

## Validation

Used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsf3_9.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsf3_9.yaml --out /private/tmp/taxonmech-bsf39-20261010-validation.tsv --workers 1`: one file, zero errors; inspected output TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured source comparisons passed for identity, the complete lineage labels/ranks, synonyms, code, attestation, unique path, scope reason, and seed-event wording. They do not replace corpus reproduction.
- `just validate-products`: not applicable because there are no curator-added graph nodes or causal claims. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. These full-corpus checks were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222810` matches the ID, label, species rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. All ancestors match their own backbone rows in root-first order: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784. Labels and ranks agree throughout.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037595&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037595), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037595) agree. All 74 parsed browser text lines were read. EFetch omits root from ancestry; Datasets includes it. An assembly count is omitted in Datasets, not reported as zero. The marker's strain qualifier is compatible with the species-ranked placeholder and does not establish formal species nomenclature or a culture deposit.

The complete native name row at `data/catalog/ncbi_names-0005.jsonl.gz:32446` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15363` uniquely resolves the identifier/slug. `curation/seed_scope.tsv:323025` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event. Read-only review does not promote the mapping status.

## Evidence

The attestation correctly counts one NCBI `NAME`, not a strain, genome, assay, or publication. Exact structured scans found no own rows in the pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain, nomenclature, and mapping sections match those inputs. Zero inventoried strains is not a claim of unculturability or absence of an isolate.

Exact Nucleotide search `txid1037595[Organism:exp]` returned one UID, `345019012`. Complete [GenBank annotation JF779761.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779761.1) joins the exact organism, strain BSF3(9), and `taxon:1037595`. It describes a 450-base 16S rRNA fragment incomplete at both ends, annotated from fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `7ea337baea5e1efbca3000e969cd643ca6b770c606bab35be5cf15182ba302d8`. It is not a genome assembly. No collection country/date, coordinates, or deposit qualifier is present. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

GenBank cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. The complete requested [HAL author-deposit metadata and abstract](https://hal.science/hal-02916138v1), inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). No full text or BSF3(9)-specific assay result was verified. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was transferred from the citation, cohort, genus, or neighboring accession.

All 23 non-target matched rows were read completely, including full GTDB metadata and compressed TSV rows. They resolve as follows:

- Enterobacter sp. BWH63, taxid 1686387: `data/catalog/ncbi_genbank-0000.jsonl.gz:36159` and `data/catalog/ncbi_refseq-0000.jsonl.gz:30559` are `GCA_001037595.1` / `GCF_001037595.1`, `SAMN03280179`, WGS `LETC00000000.1`. `data/catalog/gtdb_genomes-0003.jsonl.gz:16128` carries `RS_GCF_001037595.1`, classified as Enterobacter hormaechei_C. `data/bvbrc/bvbrc-0005.jsonl.gz:15494` is genome `1686387.3`; `data/gold/analyses.jsonl.gz:58787` is analysis `Ga0106771`, project `Gp0131102`, IMG `2671180845`, empty organism GOLD ID. These five entries match the assembly number, not target taxonomy.
- Klebsiella pneumoniae P40, taxid 573: `data/catalog/ncbi_genbank-0009.jsonl.gz:40285` and `data/catalog/ncbi_refseq-0002.jsonl.gz:42594` are `GCA_011037595.1` / `GCF_011037595.1`, `SAMN10592688`, WGS `SBCS00000000.1`. `data/catalog/gtdb_genomes-0017.jsonl.gz:25352` is `RS_GCF_011037595.1`; `data/bvbrc/bvbrc-0024.jsonl.gz:28627` is genome `573.30928`. All four are unrelated assembly-number matches.
- Bacteroidales bacterium SMBSF39, taxid 2030927: `data/catalog/ncbi_genbank-0019.jsonl.gz:22526` is metagenome-derived `GCA_021107685.1`, `SAMN21083267`, `PRJNA758896`, WGS `JAIOSH000000000.1`. `data/catalog/gtdb_genomes-0002.jsonl.gz:31976` is representative `GB_GCA_021107685.1`, classified in Bacteroidota/Bacteroidia/Bacteroidales, species SMBSF39 sp021107685. `data/raw/gtdb_mappings.tsv:144950` is a one-genome `skos:broadMatch` to `NCBITaxon:2030927`; `data/raw/gtdb_species.tsv:160404` supplies its GTDB species count. `data/bvbrc/bvbrc-0011.jsonl.gz:38548` and `:38620` are genomes `2030927.2279` (WGS) and `2030927.2343` (Deprecated). All six concern SMBSF39, not BSF3(9); neither its seep-sediment provenance nor its GTDB mapping transfers to this record.
- Klebsiella pneumoniae isolate 2005491, taxid 573: `data/catalog/ncbi_genbank-0028.jsonl.gz:43568` is current `GCA_031037595.3`, `SAMN34589458`, `PRJNA288601`, `ABLWLB000000000.3`. `data/catalog/ncbi_genbank_historical-0001.jsonl.gz:21390` and `:21391` retain replaced versions `.1` and `.2`. These three assembly identifiers are numeric false matches.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:20455` is Salmonella enterica subsp. enterica serovar Stanleyville, taxid 286782/species 28901, strain `1037595`, `GCA_015873775.1`, `SAMN16972202`, `PRJNA248792`, `AAXRQM000000000.1`.
- `data/catalog/ncbi_genbank-0032.jsonl.gz:46890` is metagenome-derived Aliarcobacter sp., taxid 2321116, isolate SMAG_U9087, `GCA_035271105.1`, `SAMN37964228`, `PRJNA983538`, `DATERY000000000.1`. Its length is `1037595`; PMID 37951952 is not a target citation.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41460` is Acinetobacter baumannii, taxid 470, strain AB20, isolate 10RC200008443, `GCA_050714215.1`, `SAMN41037595`, `PRJNA514245`, `DBIYQA000000000.1`. The match is in its BioSample; PMID 30286803 is not target evidence.
- `data/catalog/ncbi_genbank-0056.jsonl.gz:27407` is metagenome-derived Blautia hydrogenotrophica, taxid 53443, isolate 1909_1909I_C_19, `GCA_061037595.1`, `SAMN60703974`, `PRJNA1464738`, `JCDDIP000000000.1`. Its assembly number matches the pattern.
- `data/catalog/allthebacteria.tsv.xz:2946122` concerns Salmonella sp. 1208_ZJQZ20_0154, classified by Sylph as Salmonella enterica, with PASS filters and available FASTA: `SAMN41679532`, `ERZ26942419`, `SRR30613081`. The match occurs inside SeqKit sum `seqkit.v0.1_DLS_k0_8817197f25ae11169d1037595f809c24`; it supplies no identity bridge.

None supplies a target-linked genome, culture deposit, synonym, or extra attestation.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered ID, exact slug, organism/designation, and punctuation/space/hyphen variants. The expanded pass added `JF779761`, `soilbio.2011.07.010`, and `S003807171100280X`. Both yielded 26 lines: own backbone, scope, scientific name, and the 23 non-target rows above. Ignored and compressed files were included; no additional target assertion, strain/genome association, or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed; none matched. Ignored-independent filename searches found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism web search returned taxonomy/near-name leads; accession search returned no result. Search snippets supported no scientific claims.

Unfilled optional slots do not by themselves indicate a defect, and no causal graph is required. iModulonDB is not applicable because this record contains no gene, regulator, expression-module, or stress-response claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected pinned and live sources support the record's taxonomy/name-only assertions. Unverified isolate-level assay outcomes and inaccessible article full text limit enrichment research but do not contradict a recorded claim.

## Recommended Edits

None required. Keep BSF3(9) distinct from SMBSF39 and partial markers outside genome counts. Do not edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay; extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules. Scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and isolate-level table, resolve BSF3(9)/JF779761 explicitly, and inspect assay conditions/results. Any genome/deposit association requires an explicit source chain. After authorized input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Human sign-off is separately required for promotion to reviewed status.

## Additional Notes

Full primary taxonomy API responses, browser text, and GenBank annotation were inspected for this target. The shared HAL metadata and abstract were inspected earlier this turn. Previous access attempts for the same study encountered ScienceDirect 403 and an ISTEX redirect to institutional-authentication HTML rather than a PDF; those routes were not retried per isolate. No login, paid access, or article full-text reading occurred.

YAML SHA-256: `5d05d2f1d224ebd3458773db031818cd2b57342c37069b7cb39b85ff6f76564b`. Only this new report was written for the target. Maintained inputs, generated YAML, schema, history, pages, GitHub state, Eukaryota, and worktrees were left unchanged.
