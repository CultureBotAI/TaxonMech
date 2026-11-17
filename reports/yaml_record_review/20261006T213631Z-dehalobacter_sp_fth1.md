# YAML Record Review: Dehalobacter sp. FTH1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/dehalobacter_sp_fth1.yaml`
- Started UTC: 2026-10-06T21:30:03Z
- Finished UTC: 2026-10-06T21:36:31Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035308` denotes Dehalobacter sp. FTH1, `SPECIES` in `BACTERIA`, parent `NCBITaxon:2635733`. It carries ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried strains, one NCBITAXON NAME attestation and four MADIN TRAIT_ASSERTIONs, plus a seed event.

No synonyms, nomenclature, taxonomy mappings, strains, genomes, phenotypes, citations, or causal graphs are asserted. Generated fields are read-only. Future changes belong in upstream transforms, maintained extraction/seeding code, or scope decisions, not the YAML or generated site.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/dehalobacter_sp_fth1.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/dehalobacter_sp_fth1.yaml --out /private/tmp/dfth-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and is header-only.
- Structured comparisons read the complete backbone row, all ancestors, direct children, seven non-NCBI inventories, PATHS, scope, both attestations, and seed-event text. Values agree.
- Exact type-material, merged-ID, and dropped-ID checks found no target rows.
- Ignored-inclusive source searches, complete native candidate reads, full parsing of five SOURCE.json files, and history-filename searches completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0 with network access. All 28 rows were read before external follow-ups; no Dehalobacter dataset matches. iModulonDB is not applicable, not negative biological evidence.
- Live taxonomy XML/JSON, exact-organism Assembly/nuccore searches, complete sequence metadata excluding bases, and Datasets genome queries succeeded.
- Ten ambiguous BioSamples were resolved by accession-specific search and full XML inspection.
- Primary-publication abstract/metadata and relevant PMC identity/culture passages were inspected. The JGI project page was read.
- Not checked: full-corpus `just verify-corpus`, QC/history/provenance gates, full tests, page rendering, original-taxdump regeneration, or source-file hashes. No invented target-only reproduction gate was used.
- The configured upstream Madin edge file could not be opened. An ignored-inclusive fallback filename search under the KG-Microbe parent encountered permission-denied subdirectories, so that search is incomplete. The four assertions were verified against the committed inventory and extraction rule, not independently recounted from the upstream edge payload.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222006`, scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31482`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035308&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035308) agree on the target identity, rank, parent and code.

All ancestor IDs, labels and normalized ranks agree: root; cellular organisms; Bacteria; Bacillati; Bacillota; Clostridia; Eubacteriales; Desulfitobacteriaceae; Dehalobacter; unclassified Dehalobacter. Family 2937909 and genus 56112 agree. Datasets includes root ID 1, which EFetch omits from its displayed lineage.

No synonyms or direct children occur in the inspected backbone. Species rank does not establish a formal binomial, type strain, or registered deposit. FTH1 is distinct from FTH2, D. restrictus TEA, Blautia glucerasea HFTH-1 (taxon 536633), and Malus domestica HFTH1 (taxon 3750).

## Evidence

- NCBITAXON supplies one NAME at snapshot 2026-09-13. `data/raw/madin_taxa.tsv:674` explicitly supplies count 4 for this exact taxon. `count_taxon_subjects` in `src/taxonmech/extract.py:412` counts transformed edges whose subject is an NCBITaxon; the seeder uses that count directly as TRAIT_ASSERTION. This is not four independently validated phenotypes or four strains, and it must not be added to the NAME count.
- The source configuration resolves Madin to [Madin et al. (2020), DOI 10.1038/s41597-020-0497-4](https://www.nature.com/articles/s41597-020-0497-4). The inspected primary data descriptor explains trait compilation and provenance; it does not by itself establish the target's four transformed edges. The raw manifest pins the upstream edge file at SHA-256 `3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f`; that hash was not recomputed.
- `data/taxa/PATHS.tsv:14497`, `curation/seed_scope.tsv:57254`, and `curation/legacy_page_paths.tsv:872` agree on identifier, scope reason and legacy path. The raw/ATB/StrainInfo manifest times are 2026-09-13T17:50:44Z, 17:54:04Z, and 17:29:00Z; their maximum matches the seed event. This is reproducible seeding provenance, not human review.
- BV-BRC `1035308.3` explicitly names FTH1 and references `GCA_000372005.1`, `SAMN02256502`, `PRJNA165241`, and WGS `AQYY00000000`. Both native historical assembly rows, `GCA_000372005.1` and `GCF_000372005.1`, are marked suppressed, not live since 2020-07-09, with 33 contigs and length 6,329,361. The RefSeq project is PRJNA224116. These are cataloged historical identities, not eligible current deposit-linked genomes. No reason for suppression was inferred.
- GOLD organism `Go0018654` explicitly names this taxon and FTH1 but has no culture-collection identifier. Project `Gp0095960` and analysis `Ga0049941` name an FTH1-plus-unknown-organism coculture. The analysis is a Metagenome Analysis with IMG ID `3300002859`, empty organism link, and no GenBank entries. There is no explicit Go-to-project-to-analysis identity chain supporting a pure-strain genome link.
- The [JGI FTH1 project page](https://genome.jgi.doe.gov/portal/DehspFTH1_FD/DehspFTH1_FD.info.html) labels project 1077666 as a metagenome annotated standard draft, with sequencing project 402030. A project label does not repair the missing GOLD organism chain or reverse NCBI suppression.
- Exact-organism Assembly search returned 0 with a no-items warning; [Datasets genome-by-taxon](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035308/dataset_report) and accession-specific queries for both historical assemblies returned empty objects. These live negatives do not mean that FTH1 has never been sequenced.
- Exact nuccore search returned one record, UID 2896806678, [PD237271.1](https://www.ncbi.nlm.nih.gov/nuccore/PD237271.1). Its 1533 bp sequence is in the PAT division, tied to JP2022529421-A sequence 3122, with taxon cross-reference 1035308 and molecule qualifier unassigned DNA. This is a patent sequence listing, not an assembly, culture deposit, or demonstrated plant-benefit phenotype.
- [Yoshida et al., AEM 75:2400-2405, DOI 10.1128/AEM.02112-08, PMID 19218402](https://pmc.ncbi.nlm.nih.gov/articles/PMC2675204/) identifies FTH1 and FTH2 as distinct phylotypes in the KFL enrichment derived from paddy soil. Population changes supported involvement in fthalide dechlorination. The inspected evidence concerns a community, not an independently deposited pure strain. The paper's closest-relative accession U84497 is D. restrictus TEA, not an FTH1 identifier.

## Completeness

Current assertions are complete enough for a seeded taxon record. Phenotype details belong in the sibling Mech resources, and record-level citations are optional here. Zero inventoried BacDive strains is not zero biological organisms or an assertion of no sequencing.

The native GOLD organism is a genuine additional catalog occurrence. The record's GOLD attestation is absent because `src/taxonmech/extract.py:676` counts exact Go-to-taxon edges in the pinned kg-microbe transform, not all native workbook rows. The inspected direct GOLD inventory has no target row. This is a documented source-layer boundary and an optional completeness follow-up, not evidence that the two existing attestations are wrong. Do not conflate the organism occurrence with the unlinked coculture analysis.

The initial search used `rg --no-ignore --hidden -n -z -i` with `1035308|FTH[-_ ]?1\b|dehalobacter_sp_fth1` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden and compressed files were included. All 34 candidate lines were inspected losslessly: 15 JSON objects and 19 TSV rows. Eleven are exact target identity/provenance, historical sequencing, or named coculture context. The remaining 23 are not target evidence:

| Candidates | Exclusion basis |
| --- | --- |
| Eight Blautia rows | HFTH-1 is Blautia glucerasea, taxon 536633. BacDive 18076, StrainInfo SI-ID 397345/SI-DP 903964, DSM 22028, JCM 17039, NBRC 104932, KCTC 15131, LPSN 788483 and GOLD Go0610958 remain with that identity. Its includes-name Clostridium sp. HFTH-1 and two type-material designations do not belong to FTH1. |
| Two Malus rows | Go0518148/Gp0442218 concern M. domestica HFTH1, taxon 3750, PRJNA482033/SAMN09744170. |
| One Campylobacter row | GCA_010353085.1 is C. jejuni FSIS12027773, taxon 197, SAMN13828700, PRJNA287430. Matching accession digits are not a taxon match. |
| Two M. tuberculosis rows | BV-BRC 1773.18314 and ATB SAMEA3558841/ERZ9334458 share run ERR1035308, not the target TaxID. |
| Ten unknown ATB rows | SAMN10353080 through SAMN10353089 have NOT_PROCESSED status, no FASTA, run or assembly. Full NCBI BioSample XML identifies distinct human-associated Chinese samples collected 2018-07-11, taxon 1869227, project PRJNA503135; none names FTH1 or taxon 1035308. |

An accession follow-up across the same roots searched PD237271, the AQYY sequence family, the explicit historical assembly pair, SAMN02256502, PRJNA165241, and the named GOLD/IMG identifiers. All 20 returned rows were inspected: six already-reviewed target/context rows and fourteen additional WGS-substring collisions. The latter concern Streptococcus pneumoniae GPSC24 (GCA_901255865.1), Pseudomonas fragi WS 5087 (GCA/GCF_012986835.1), Listeria monocytogenes (GCA_004515885.1), three Salmonella assemblies (GCA_044304985.1, GCA_010294365.1, GCA_018600795.1), Candidatus Dormiibacterota (GCA_049790415.1), and Acinetobacter baumannii (GCA_052626265.1), including their duplicated source rows. Longer WGS prefixes such as JAAQYY are not AQYY.

No exact target entries occur in the inspected raw BacDive, LPSN, GTDB, GOLD, MediaDive or BactoTraits inventories, target type/merged/dropped rows, or history filenames. No additional target bridge was found in the five fully parsed SOURCE.json files. These negatives are bounded to the named sources and snapshots, not global absence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in existing assertions. Identity, lineage, grounding, inventory count/unit pairs and seed provenance agree. The unverified upstream Madin edge payload and absent full-corpus gates limit the review; they are not silently reported as passing.

## Recommended Edits

None required for the current record.

For separately authorized source enrichment, investigate the exact Go0018654-to-1035308 occurrence in the kg-microbe GOLD transform or deliberately extend `src/taxonmech/extract.py` with tests defining native-organism attestation policy. Re-extract and seed through the documented workflow. Do not hand-add a GOLD attestation, genome or strain to generated YAML.

Do not convert suppressed assemblies into live links, treat the coculture IMG analysis as a pure FTH1 genome, borrow HFTH-1 culture deposits, or infer phenotype evidence from a patent listing. Any functional enrichment must preserve the community/phylotype scope and be routed to the appropriate maintained representation.

## Follow-up Checks

With the pinned upstream Madin edge file available, recompute its manifest hash, inspect all exact-subject edges and independently recount them using the extractor's rule. The configured path is `~/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv`; no claim of absence outside the checked location is made.

For authorized GOLD enrichment, inspect explicit primary taxon/organism links and test count/unit provenance independently of genome eligibility. Require a supported culture-deposit identity chain for strain/genome links. Keep historical NCBI status and mixed-culture scope intact.

After any upstream change, run documented extraction/seeding, `just verify-corpus`, schema and exact-target strict validation; read emitted TSV and regenerated fields. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Local review/curation guidance, schema and source-coverage rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. A preliminary broad numeric accession search was narrowed before evidence use; its 190 hits were not individually reviewed and support no completeness claim. The 34 initial and 20 narrower follow-up candidates were fully read.

The configured upstream edge lookup failed, and the wider ignored-inclusive filename search exited 2 with permission errors. Live GOLD and NCBI assembly web pages were inaccessible; the report distinguishes inspected pinned metadata from successful live taxonomy/Datasets responses. The PMC article was available after publisher/PubMed web access failed.

The target was byte-compared with the initial full read and remains unchanged. This report is the only repository artifact of this review. No YAML, inventories, generated pages, histories, prior reports, Git/GitHub state, or Eukaryota records were modified.
