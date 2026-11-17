# YAML Record Review: Paenibacillus sp. Hs2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_hs2.yaml`
- Started UTC: 2026-10-09T08:17:32Z
- Finished UTC: 2026-10-09T08:22:45Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036661`, Paenibacillus sp. Hs2. It asserts species rank, Bacteria, parent 185978, ten root-first ancestors, code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive strains and one NCBITAXON name attestation. Its seed event is dated 2026-09-13T17:54:04Z.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved this YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genomes, phenotypes, discussion and graphs are unasserted. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_sp_hs2.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_sp_hs2.yaml --out /private/tmp/taxonmech-paenibacillus-hs2-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched own identity, every ancestor, PATHS, scope reason, attestation and seed wording. Exact scans covered seven supplemental raw inventories, type material, merged IDs and dropped taxa.
- Own-marker annotation consistency passed: declared and actual length 891, rRNA transcription identical to DNA, no non-ACGT symbols. This is not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused comparisons do not prove corpus reproduction. Embedded history was read; ignored-inclusive content and filename searches found no separate target history artifact within the stated roots. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036661&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036661) responses agree with label, species rank and lineage. EFetch confirms parent 185978 and code 11; Datasets includes root. Ancestors are root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Paenibacillaceae, Paenibacillus and unclassified Paenibacillus.

Live taxonomy has no other names; pinned synonym fields are empty. No own type-material, merged-ID or dropped-taxon row, or backbone child, was found. Species rank does not establish formal nomenclatural standing or a particular named Paenibacillus species. Bacillus sp. HS-2 (1368300) and Pseudovibrio sp. Hs2 (989451) are separate source identities, not aliases supplied for this record.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:222566`, `data/catalog/ncbi_names-0005.jsonl.gz:32110`, `data/taxa/PATHS.tsv:15083` and `curation/seed_scope.tsv:322813`. Snapshot 2026-09-13, one-name unit and admission reason support the attestation and seed event. Exact target scans found no row in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw inventories. A name count is not a genome or experiment count.

Exact Nuccore taxon query returned UID 334361615 alone. Complete [JF803847.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803847.1) XML, references, features and sequence were read. This 891-base partial 16S marker is incomplete at both ends. Its six source qualifiers identify Paenibacillus sp. Hs2, genomic DNA, strain Hs2, host Haliclona simulans, taxon 1036661 and Ireland: Gurraig Sound Kilkieran Bay, Galway. No deposit or genome qualifier is present. References identify Phelan and colleagues and a 13-APR-2011 University College Cork direct submission. Creation/update dates are 31-DEC-2011 and 20-NOV-2013.

Exact JF803847 PubMed search retrieves [PMID 21985154](https://pubmed.ncbi.nlm.nih.gov/21985154/). Its complete abstract and selected bibliographic metadata (title, journal, date and publication identifiers, not author affiliations) verify [DOI 10.1111/j.1365-2672.2011.05173.x](https://doi.org/10.1111/j.1365-2672.2011.05173.x). Cohort findings do not establish this isolate's specific genes or phenotypes. The DOI/publisher page was inaccessible through the web tool during this review; isolate-level full-text tables remain unverified. No experimental claim was imported.

## Completeness

Complete enough for supported taxonomy-seed claims. Zero represented BacDive strains does not deny the cultured isolate's existence. No additional target deposit or genome link was established within the inspected evidence.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms were word-bounded 1036661, the exact slug and HS2 with an optional space, hyphen or underscore. Expansion added word-bounded JF803847 with optional .1 and UID 334361615. Both searches returned the same 116 rows; all were read completely in native form using lossless common fields and differences: 24 TSV and 92 JSON rows.

Three rows concern the target; 113 have other identities. Important exclusions include:

- HS2/HS-2 names assigned to Desulfovibrio, Rhodococcus, Vibrio, Pseudomonas, Serratia, Pseudovibrio, Chromohalobacter, Bacillus, Microvirga and an enrichment-culture clone, with distinct NCBI IDs.
- Helicobacter suis HS2, GCA/GCF_900196835.1/SAMEA104141503; Escherichia coli HS2-1, GCA/GCF_015731245.1/SAMN16274494; Pseudomonas carnis HS2, GCA/GCF_013522615.1/SAMN14085467; Cutibacterium avidum HS2, GCA/GCF_024105095.1/SAMN19186351; Microvirga HS2, GCA/GCF_055792805.1/SAMN50292947.
- Candidatus Halichondribacter symbioticus HS2, GCA_008973675.1/SAMN10711867, retains a fragmented-assembly exclusion. Pseudomonas sp. HS-2, GCA_004369025.1/SAMN11046846, retains a contamination exclusion and a historical RefSeq suppression dated 2024-10-13. Pseudomonas aeruginosa HS_2, GCA_025235875.1/SAMN24547488, retains a large-multi-isolate-project exclusion and historical RefSeq suppression dated 2022-09-20. These are non-target source flags, not defects in this Paenibacillus record.
- StrainInfo SI-ID 51538 maps HS2 to Actinomyces viscosus/CCUG 35451. SI-ID 257154 maps Hs-2 to the fungus Nakataea oryzae, with an older Magnaporthe salvinii deposit label and ATCC 44756. Neither supplies a target deposit.
- GOLD entries concern a Pseudoalteromonas phage and 39 Pseudoalteromonas transcriptome projects, other named bacteria, Neurospora expression conditions and two soil-community samples. Their organism/project/sample identifiers are not Paenibacillus strain-genome links.

GTDB/NCBI classification differences in non-target rows were retained, including Aquipseudomonas paracarnis versus Pseudomonas carnis. They are outside this record's identity and are not a reason to alter its lineage. Five SOURCE.json files were separately parsed in full for both term sets, with no matches; history filenames were independently inventoried.

A Paenibacillus-or-Bacillus Nuccore query for HS2 and separator variants returned 15 records; all full ESummary objects were inspected. The query also expanded HS2 to Hirudo sulukii in an OR term, still intersected with the bacterial-genus condition. This is not an outside-genus sequence census.

Beyond the full own marker, three close candidates received complete GenBank XML reads:

- [MN733208.1](https://www.ncbi.nlm.nih.gov/nuccore/MN733208.1), 713 bases, is Paenibacillus alvei AUG6, taxon 44250, isolated from industrial effluent. HS2 occurs in its unpublished reference title. Its authors and 26-NOV-2019 Indian submission differ from the target.
- [KC893657.1](https://www.ncbi.nlm.nih.gov/nuccore/KC893657.1), 1,394 bases, is Bacillus sp. HS-2, taxon 1368300, from production water, submitted by Geng on 08-APR-2013 from China.
- [JQ929074.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ929074.1), 498 bases, is Bacillus subtilis HS2, taxon 1423, collected from Egyptian marine sponges in 2010 and submitted by the Alexandria group in April 2012. A shared sponge association and label are insufficient to identify it with the Irish isolate.

Other summary-level candidates concern Chinese lake or plant-associated Bacillus, Indian rice-rhizosphere Bacillus, Thai termite-gut Hs-2 genes/16S, HS2-8, Hs2-17 and Yellowstone clone hs2_43. Their full feature/sequence bodies were not inspected. No independent sequence alignment or equivalence inference was made.

Exact Assembly query returned zero with missing-phrase/no-items diagnostics, not proof of global genome absence. The Paenibacillus/HS2 PubMed name query returned zero, while the exact marker query retrieved the primary study. Query translations and diagnostics were inspected; index misses do not prove absent literature. No full-text literature census was performed.

iModulonDB was not run: no gene, regulator or expression claim is asserted, and no applicable target strain/dataset was established. Unrelated GOLD transcriptomes do not change that. Optional empty fields are not automatic defects; absence conclusions remain bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, source attestation and admission agree with pinned and live authorities. Name collisions and near-match sequences do not establish missing target deposit/genome relationships.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Do not join sources on the bare HS2 code.

## Follow-up Checks

Optional enrichment requires isolate-specific primary text explicitly linked to Paenibacillus Hs2/JF803847 and independent deposit/genome provenance. Reassess named-species assignments only with direct provenance and appropriate sequence evidence. No genome comparison, experimental reanalysis or PDF/figure visual verification was performed.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:1036661`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Independent review followed the local skill/checklist; no neighboring verdict was inherited. Entire YAML, own source rows, all 116 local candidates, live taxonomy, own marker, 15 full sequence summaries, three full near-match markers and primary abstract with the metadata scope above were inspected.

Before/after YAML SHA-256: `1f8828443e1c5afdf418b9713541a4f1f5b0fdc07c37504073f389cae63f63a5`. Only this new report was written for the target. YAML, sources, status, history, pages, Eukaryota, GitHub objects and worktrees were unchanged.
