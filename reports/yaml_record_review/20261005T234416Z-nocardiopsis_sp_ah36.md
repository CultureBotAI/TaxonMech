# YAML Record Review: Nocardiopsis sp. AH36

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah36.yaml`
- Started UTC: 2026-10-05T23:42:12Z
- Finished UTC: 2026-10-05T23:44:16Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034873`, Nocardiopsis sp. AH36, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14192` uniquely resolves the identifier and stem; `curation/seed_scope.tsv:322025` supplies inclusion. Only this new report was written for this target. Records, source inputs, scope, history and Eukaryota were left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah36.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah36.yaml --out /private/tmp/ah36-validation.tsv`, exit 0, one file, zero errors. The output TSV was read and contains only its header.
- PASS: structured comparisons checked the complete backbone row, reconstructed ancestor chain, seven source inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. The backbone supplies no children of the target.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, complete marker metadata/features, relevant primary-paper text and Figure 3, and the unrelated archaeal BacDive candidate's identity page.
- Not applicable: target-specific LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No such mapping, graph, gene/regulator assertion or expression module is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not prove corpus reproduction or publication readiness.

Required local guidance, relevant schema classes, validator definitions and seed-timestamp behavior were read earlier in this sequence. The review skill was reread this turn; guidance/schema/seeder/target diffs against the previously read HEAD were empty. The ignored-inclusive search below found no target history entry. No history entry or lifecycle promotion was made under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034873&retmode=xml) confirms identifier, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034873) confirms identifier/name/rank and all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

The informal label does not assert validly published nomenclature. A marker's strain qualifier does not change the NCBI concept's species rank. `EXACT` identifies this precise taxon, not a named-species equivalence or another AH36/Ah-36 specimen.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221722` row and both live NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Scientific name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31125`; all three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Backbone attests only ncbitaxon, snapshot 2026-09-13. Source, ID, label, count, unit and note agree; NAME is not a strain or genome count. |
| Scope and event | Scope line 322025 supplies date 2026-09-13 and the exact one-source attested-rule reason; embedded event text agrees. |
| Seed timestamp | The event's 2026-09-13T17:54:04Z is the maximum of the previously inspected raw, ATB and StrainInfo manifest extraction times, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is classified under taxon 1034873, and the backbone supplies no descendants. This source-classification count does not claim AH36 was never cultivated. |

The exact query `txid1034873[Organism:noexp]` returned one Nuccore UID, 333497023. Complete [JF777519.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497023), references and features were inspected, excluding sequence bases. This is a 1,418-base 16S rRNA marker, partial at both ends. Source qualifiers identify Nocardiopsis sp. AH36, strain AH36, taxon 1034873, Saharan soil, Algeria and collection year 2010; no culture-collection qualifier is supplied.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. No DOI or PMID is supplied in that metadata. These establish marker/specimen context, not genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternate classification or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, groups AH36 with AH44 in cluster II. Its 99.4-99.8% N. xinjiangensis similarity range covers several groups, not AH36 alone. Figure 3 pairs AH36 with JF777519. The paper's 1,529-1,544-base range differs from the accession's 1,418 bases. This unresolved discrepancy does not establish a YAML error or species equivalence.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034873. Empty optional slots agree with those inputs. Literature evidence is optional for seeded records; the paper does not establish a required missing representation.

Searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched identifier, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 12 matches were read in full as JSON or header-aware TSV.
- Three matches are target backbone/name/scope. `data/bvbrc/bvbrc-0006.jsonl.gz:6340` is Mycobacterium tuberculosis ERR1034873, taxon 1773, genome 1773.18526.
- `data/catalog/ncbi_genbank-0044.jsonl.gz:37009` and `gtdb_genomes-0005.jsonl.gz:23393` concern Gemmatimonadales bacterium GEMM-2, taxon 2448054, GCA_048499805.1 and SAMN31034873. GTDB supplies JAWXBA01 sp048499805; target-like digits occur in its BioSample.
- `data/catalog/ncbi_genbank-0033.jsonl.gz:35509` is Streptococcus pneumoniae isolate 413, taxon 1313, GCA_036052295.1, assembly name PDT001034873.1.
- `data/catalog/allthebacteria.tsv.xz:65880` supplies Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034873, run ERR085029 and ERZ3070251. Row 569343 supplies Mycobacterium tuberculosis run ERR1034873, sample SAMEA3558406 and ERZ3501015. Rows 1714989/1714990 supply Salmonella enterica runs SRR10348730/SRR10348731. Row 3092401 supplies Escherichia coli run SRR31034873, sample SAMN44338753 and ERZ27111248. No row identifies this Nocardiopsis taxon.
- A separate JF777519 search across those ten roots returned zero matches. This is bounded local absence, not a missing required genome link.
- An AH36/AH-36/AH 36/AH_36 screen of the BacDive inventory, native BacDive and StrainInfo returned three rows, all read in full; they identify an archaeal strain discussed below.
- A supplemental alias search across the ten roots returned 23 rows, all read in full: three target rows, nine other-taxon name/backbone/scope rows, three culture-source rows, two type-material rows, one GOLD object and five assembly objects.
- Before writing, an ignored-inclusive identifier/full-label/slug search of `reports/yaml_record_review` and `history` returned no matches; a filesystem search found no prior exact-stem report.

The archaeal culture match is not a Nocardiopsis association:

- `data/raw/bacdive_strains.tsv:5853` and `data/bacdive/records.jsonl.gz:5852` supply BacDive 5966, Natronococcus amylolyticus Ah-36, strain-level taxon 1227497 and species taxon 44470, type strain. Deposits include DSM 10524, JCM 9655, ATCC 51971, CGMCC 1.3840, CIP 105333 and FERM P-11024. Native sequence entries include D43628, AB663468, unversioned GCA_000337675, BV-BRC 1227497.3 and IMG 2554235477. The inspected [BacDive identity page](https://bacdive.dsmz.de/strain/5966) independently confirms the archaeal identity, designation, deposits and taxon IDs.
- `data/straininfo/records.jsonl.gz:33423` is published-online SI-ID 45332, DOI 10.60712/SI-ID45332.3, BacDive 5966, Natronococcus amylolyticus taxon 44470. Its own available type deposits include ATCC 51971, JCM 9655, CIP 105333, DSM 10524 and NCIMB 13549. It explicitly links AB663468 and AB477214 to JCM 9655/SI-DP 121739, and unversioned GCA_000337675 to DSM 10524/SI-DP 162060. These links belong to that archaeal strain, not the target.
- `data/raw/ncbi_type_material.tsv:212569` and line 212570 assign Ah-36 designations to Natronococcus amylolyticus taxon 44470. `data/gold/organisms.jsonl.gz:455051` supplies Go0624442 with that species/designation and no culture-collection field. Neither supports transfer to Nocardiopsis.

Other alias results were distinguished:

- Natronococcus sp. Ah-36, taxon 468513: scope line 217234, backbone line 104653, `data/catalog/ncbi_names-0002.jsonl.gz:45165`. Its relationship to the separate named archaeal species was not inferred or reviewed here.
- Burkholderia sp. AH36, taxon 861693: scope line 285666, backbone line 181203, `data/catalog/ncbi_names-0004.jsonl.gz:34887`. Asaia sp. VTH-AH36, taxon 1769112: scope line 524144, backbone line 462044, `ncbi_names-0010.jsonl.gz:47901`.
- Escherichia coli AH36, taxon 562: paired GCA_019369935.1/GCF_019369935.1, SAMN17183263, `data/catalog/ncbi_genbank-0017.jsonl.gz:38883` and `ncbi_refseq_historical-0000.jsonl.gz:43042`. The RefSeq record is suppressed.
- Klebsiella pneumoniae AH36, taxon 573: paired GCA_057665625.1/GCF_057665625.1, SAMN54997866, `data/catalog/ncbi_genbank-0053.jsonl.gz:16231` and `ncbi_refseq-0008.jsonl.gz:44181`. Separate AH_36 assembly GCA_053075345.1/SAMN50316221 occurs in `ncbi_genbank-0049.jsonl.gz:869`.

No inspected source supports a consequential missing target strain-to-genome relationship or required correction. Shared designations and numeric substrings were not promoted into identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The external length discrepancy remains unresolved and is not asserted by the target.

## Recommended Edits

None required on current evidence. Do not hand-edit the generated YAML, infer N. xinjiangensis equivalence, attach the archaeal Ah-36 deposits or other same-label genomes, count the 16S marker as a genome or promote the lifecycle to REVIEWED.

Any future verified source/identity correction belongs in maintained extraction inputs or `src/taxonmech/seed.py` with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not biological identity. Optional literature enrichment requires a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Resolve the paper/accession length discrepancy before literature enrichment; no author/depositor contact was made.
- Require explicit deposit-to-accession provenance for any future culture association; retain source versions and strain/sample/project/marker/assembly distinctions.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither ran here.
- Reconcile report coverage against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

Relevant primary-paper text was read live. Figure 3 was visually inspected in the cached page-6 rendering of the [published open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf), downloaded during the AH0 review. No new image or PDF was written in the repository. The paper was checked for identity context, not exhaustively curated for physiological or antimicrobial claims.

Candidate objects were inspected only as identity leads, not counted as reviews of their taxa. No exhaustive external census, all-alias search or whole-genome equivalence analysis is claimed. The complete native StrainInfo object was inspected; its live site and unrelated deposits' individual authority pages were not required to establish a target association, and were not checked.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
