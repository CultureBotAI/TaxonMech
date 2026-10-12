# YAML Record Review: Nocardiopsis sp. AH33

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah33.yaml`
- Started UTC: 2026-10-05T23:38:26Z
- Finished UTC: 2026-10-05T23:40:06Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034872`, Nocardiopsis sp. AH33, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14191` uniquely resolves the identifier and stem; `curation/seed_scope.tsv:322024` supplies inclusion. Only this new report was written for this target. Records, source inputs, scope, history and Eukaryota were left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah33.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah33.yaml --out /private/tmp/ah33-validation.tsv`, exit 0, one file, zero errors. The output TSV was read and contains only its header.
- PASS: structured comparisons checked the complete backbone row, reconstructed ancestor chain, seven source inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. The backbone supplies no children of the target.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, complete marker metadata/features and relevant primary-paper text and Figure 3.
- Not applicable: target-specific LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No such mapping, graph, gene/regulator assertion or expression module is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. Bounded checks do not certify corpus reproduction or publication readiness.

Required guidance and relevant schema classes were read earlier in this sequence. CLAUDE.md, both record skills, the checklist, justfile, seed-timestamp function and manifest timestamps were reread this turn. HEAD remained unchanged; guidance/schema/seeder/target diffs were empty. The ignored-inclusive search below found no target history entry; none was created under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034872&retmode=xml) confirms identifier, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034872) confirms identifier/name/rank and all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

The informal label does not assert validly published nomenclature. A marker's strain qualifier does not change the NCBI concept's species rank. `EXACT` identifies this precise taxon, not equivalence to Nocardiopsis xinjiangensis or another AH33-labeled specimen.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221721` row and both live NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Scientific name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31124`; all three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Backbone attests only ncbitaxon, snapshot 2026-09-13. Source, ID, label, count, unit and note agree; NAME is not a strain or genome count. |
| Scope and event | Scope line 322024 supplies date 2026-09-13 and the exact one-source attested-rule reason; embedded event text agrees. |
| Seed timestamp | Raw, ATB and StrainInfo manifests give 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The event uses their maximum, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is classified under taxon 1034872, and the backbone supplies no descendants. This source-classification count does not claim AH33 was never cultivated. |

The exact query `txid1034872[Organism:noexp]` returned one Nuccore UID, 333497022. Complete [JF777518.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497022), references and features were inspected, excluding sequence bases. This is a 1,418-base 16S rRNA marker, partial at both ends. Source qualifiers identify Nocardiopsis sp. AH33, strain AH33, taxon 1034872, Saharan soil, Algeria and collection year 2010; no culture-collection qualifier is supplied.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. No DOI or PMID is supplied in the metadata. These establish marker/specimen context, not genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternate classification or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, places AH33 in cluster I. Its 99.4-99.8% N. xinjiangensis similarity range covers several groups, not AH33 alone. Figure 3 pairs AH33 with JF777518. The paper's 1,529-1,544-base range differs from the accession's 1,418 bases. That unresolved discrepancy does not establish a YAML error or species equivalence.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034872. Empty optional slots agree with those inputs. Literature evidence is optional for seeded records; the paper does not establish a required missing representation.

Searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched identifier, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 13 matches were read in full as JSON or header-aware TSV.
- Three matches are target backbone/name/scope. `data/bvbrc/bvbrc-0006.jsonl.gz:6342` is Mycobacterium tuberculosis ERR1034872, taxon 1773, genome 1773.18528.
- `data/catalog/ncbi_genbank-0044.jsonl.gz:37007` and `gtdb_genomes-0015.jsonl.gz:39618` concern bacterium OLB16-1, NCBI taxon 1869227, GCA_048499775.1 and SAMN31034872. GTDB supplies OLB16 sp001567115, not Nocardiopsis. The target-like digits occur in its BioSample.
- `data/catalog/ncbi_genbank-0033.jsonl.gz:35510` is Streptococcus pneumoniae isolate 416, taxon 1313, GCA_036052315.1, assembly name PDT001034872.1.
- `data/catalog/allthebacteria.tsv.xz:65879` supplies Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034872, run ERR085062 and ERZ3070257. Row 569342 supplies Mycobacterium tuberculosis run ERR1034872, sample SAMEA3558405 and ERZ3501013.
- Further ATB rows 1714970, 1714973 and 1714988 contain runs SRR10348728, SRR10348722 and SRR10348729 for Campylobacter jejuni or Salmonella enterica. Row 3092402 supplies run SRR31034872, sample SAMN44338754 and ERZ27111252, source scientific name Shigella boydii with a separate Sylph Escherichia coli classification. No row identifies this Nocardiopsis taxon.
- A separate JF777518 search across those ten roots returned zero matches. An AH33/AH-33/AH 33/AH_33 screen of the BacDive inventory, native BacDive and StrainInfo returned zero matches. These are bounded local absences, not proof that no deposit exists elsewhere.
- A supplemental alias search across the same ten roots returned 12 rows, all read in full: three target rows, six other-taxon name/backbone/scope rows and three assembly objects.
- Before writing, an ignored-inclusive identifier/full-label/slug search of `reports/yaml_record_review` and `history` returned no matches; a filesystem search found no prior exact-stem report.

The supplemental aliases do not establish target associations:

- Burkholderia sp. AH33, taxon 861691: scope line 285664, backbone line 181201 and `data/catalog/ncbi_names-0004.jsonl.gz:34885`.
- Gluconobacter sp. VTH-AH33, taxon 1769126: scope line 524158, backbone line 462058 and `data/catalog/ncbi_names-0010.jsonl.gz:47915`.
- Klebsiella pneumoniae AH33, taxon 573: paired GCA_057664925.1/GCF_057664925.1, SAMN54997887, `data/catalog/ncbi_genbank-0053.jsonl.gz:16197` and `ncbi_refseq-0008.jsonl.gz:44159`. A separate AH_33 assembly, GCA_053075365.1/SAMN50316220, occurs in `ncbi_genbank-0049.jsonl.gz:870`.

No inspected source supports a consequential missing strain-to-genome relationship or required correction. Shared labels, numeric substrings and marker sequences were not promoted into culture or genome identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The external length discrepancy remains unresolved and is not asserted by the target.

## Recommended Edits

None required on current evidence. Do not hand-edit the generated YAML, infer N. xinjiangensis equivalence, attach another AH33 specimen by label, count the marker as a genome or promote the lifecycle to REVIEWED.

Any future verified identity/source correction belongs in maintained extraction inputs or `src/taxonmech/seed.py` with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment requires a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Resolve the paper/accession length discrepancy before literature enrichment; no author/depositor contact was made.
- Require explicit deposit-to-accession provenance for any future culture association. Keep strain, sample, project, marker and assembly identities separate.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither ran here.
- Reconcile report coverage against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

Relevant primary-paper text and Figure 3 were inspected during this turn, including the cached rendering of page 6 of the [published open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf), downloaded during the AH0 review. No new image or PDF was written in the repository. The paper was checked for identity context, not exhaustively curated for phenotype or antimicrobial claims. Search-result leads without inspected source text were not used as evidence.

Candidate objects were inspected as identity leads, not counted as reviews of their taxa. No exhaustive external census, all-alias search or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
