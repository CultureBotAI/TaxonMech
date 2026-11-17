# YAML Record Review: Nocardiopsis sp. AH26

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah26.yaml`
- Started UTC: 2026-10-05T23:34:34Z
- Finished UTC: 2026-10-05T23:37:14Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034871`, Nocardiopsis sp. AH26, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14190` uniquely resolves the identifier and stem; `curation/seed_scope.tsv:322023` supplies inclusion. An ignore-independent filesystem search resolved one target file. Only this new report was written for this target. Records, source inputs, scope, history and Eukaryota were left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah26.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah26.yaml --out /private/tmp/ah26-validation.tsv`, exit 0, one file, zero errors. The output TSV was read and contains only its header.
- PASS: structured comparisons checked the complete backbone row, reconstructed ancestor chain, seven source inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. There are no children of the target in the backbone.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, complete marker metadata/features and relevant primary-paper text and Figure 3.
- Not applicable: target-specific LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No such mapping, graph, gene/regulator assertion or expression module is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not prove corpus reproduction or publication readiness.

Required guidance and relevant schema classes were read earlier in this sequence. CLAUDE.md, both record skills, the checklist, justfile, seed-timestamp function and manifest timestamps were reread this turn. Guidance/schema/target diffs against the previously read HEAD were empty. The ignored-inclusive search below found no target history entry; none was created under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034871&retmode=xml) confirms identifier, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034871) confirms identifier/name/rank and all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies the non-root ancestry; Datasets includes root explicitly.

The informal label is not a validly published species-name assertion. A marker's strain qualifier does not change the rank of this NCBI concept. `EXACT` identifies this taxon, not equivalence to Nocardiopsis salina or another AH26-labeled specimen.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221720` row and both live NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Scientific name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31123`; all three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Backbone attests only ncbitaxon, snapshot 2026-09-13. Source, ID, label, count, unit and note agree; NAME is not a strain or genome count. |
| Scope and event | Scope line 322023 supplies date 2026-09-13 and the exact one-source attested-rule reason; embedded event text agrees. |
| Seed timestamp | Raw, ATB and StrainInfo manifests give 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The event uses their maximum, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is classified under taxon 1034871, and the backbone supplies no descendants. This is a source-classification count, not a claim that AH26 was never cultivated. |

The exact query `txid1034871[Organism:noexp]` returned one Nuccore UID, 333497021. Complete [JF777517.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497021), references and features were inspected, excluding sequence bases. This is a 1,422-base 16S rRNA marker, partial at both ends. Source qualifiers identify Nocardiopsis sp. AH26, strain AH26, taxon 1034871, Saharan soil, Algeria and collection year 2010; no culture-collection qualifier is supplied.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. No DOI or PMID is supplied in that metadata. These are marker/specimen context, not genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternate classification or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, treats AH26 as a single isolate and reports 98.8% similarity to N. salina. Figure 3 pairs AH26 with JF777517. The authors call for further molecular work to resolve species status. Their 1,529-1,544-base range differs from the accession's 1,422 bases. This discrepancy remains unresolved; neither similarity nor the tree establishes species equivalence or an error in this YAML.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034871. Empty optional slots agree with these inputs. Literature evidence is optional for a seeded record; the marker and paper do not establish a required missing representation.

Searches included ignored/hidden files and compressed catalogs:

- `rg --no-ignore --hidden -n -z -i` searched identifier, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 19 matches were read in full as JSON or header-aware TSV.
- Three matches are target backbone/name/scope. BV-BRC row `data/bvbrc/bvbrc-0006.jsonl.gz:6324` is Mycobacterium tuberculosis ERR1034871, taxon 1773, genome 1773.18511.
- `data/catalog/ncbi_genbank-0044.jsonl.gz:37010` and `gtdb_genomes-0013.jsonl.gz:39684` concern Microgenomates group bacterium PATE-3, taxon 2461418, GCA_048499835.1 and SAMN31034871. The digits occur in its BioSample, not the target taxonomy.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6274` is Campylobacter jejuni PNUSAC013670, taxon 197, GCA_010348715.1. `ncbi_genbank-0033.jsonl.gz:35511` is Streptococcus pneumoniae isolate 415, taxon 1313, GCA_036052335.1, assembly name PDT001034871.1.
- `data/catalog/allthebacteria.tsv.xz:65878` supplies Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034871, run ERR085033 and ERZ3070253. Row 569341 supplies Mycobacterium tuberculosis run ERR1034871, sample SAMEA3558404 and ERZ3501009. Nine further matches, rows 1714964, 1714966, 1714968, 1714975, 1714978, 1714979, 1714980, 1714983 and 1714987, contain SRR1034871-prefixed run identifiers for Campylobacter jejuni or Listeria monocytogenes. None identifies the target.
- A separate JF777517 search across those ten roots returned zero matches. An AH26/AH-26/AH 26/AH_26 screen of the BacDive inventory, native BacDive and StrainInfo returned zero matches. These are bounded local absences, not proof that no deposit exists elsewhere.
- A supplemental alias search across the ten roots returned 32 rows, all read in full: three target rows, nine other-taxon name/backbone/scope rows, six GOLD objects, two BV-BRC objects, ten assembly objects and two GTDB objects.
- Before writing, an ignored-inclusive identifier/full-label/slug search of `reports/yaml_record_review` and `history` returned no matches; a filesystem search found no prior exact-stem report.

The supplemental alias results were separated as follows:

- Burkholderia sp. AH26, taxon 861689: scope line 285662, backbone line 181199, `data/catalog/ncbi_names-0004.jsonl.gz:34883`. Viridibacillus sp. AH26, taxon 1167429: scope line 351152, backbone line 257861, `ncbi_names-0006.jsonl.gz:24869`. Bacteroidetes bacterium AH26, taxon 1208694: scope line 364108, backbone line 273254, `ncbi_names-0006.jsonl.gz:42222`.
- GOLD organism lines 81031/81059 identify Mycobacterium tuberculosis AH26_26663/AH26_28866, taxon 1773, Go0141079/Go0141107, with empty culture-collection fields. Project lines 92388/92416 supply Gp0146246/Gp0146274 and SAMN03813778/SAMN03813779; analysis lines 71465/72492 supply Ga0124737/Ga0125875, GCA_001282575.1/GCA_001445535.1 and IMG 2713896839/2724678959. BV-BRC lines 33594/10116 in shard 0006 supply genomes 1773.844/1773.2348. Complete paired GenBank/RefSeq and GTDB records retain those distinct M. tuberculosis identities. These are not Nocardiopsis links.
- Flavobacterium tagetis AH26, taxon 2801336: paired GCA_060434185.1/GCF_060434185.1, SAMN62578543, `ncbi_genbank-0055.jsonl.gz:48551` and `ncbi_refseq-0009.jsonl.gz:14958`.
- Klebsiella pneumoniae AH26, taxon 573: paired GCA_057665745.1/GCF_057665745.1, SAMN54997864, `ncbi_genbank-0053.jsonl.gz:16237` and `ncbi_refseq-0008.jsonl.gz:44184`. A separate AH_26 assembly, GCA_053068545.1/SAMN50315165, occurs in `ncbi_genbank-0049.jsonl.gz:529`.
- Neisseria gonorrhoeae ah26, taxon 485: GCA_046242415.1, SAMEA114004433, `ncbi_genbank-0042.jsonl.gz:32168`.

No inspected source supports a consequential missing strain-to-genome relationship or required correction. Shared labels, numeric substrings and marker sequences were not promoted into culture or genome identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The external length discrepancy is unresolved and is not asserted by the target.

## Recommended Edits

None required on current evidence. Do not hand-edit the generated YAML, rename it to N. salina, attach another AH26 specimen by label, count the 16S marker as a genome or promote its lifecycle to REVIEWED.

Any future verified identity/source correction belongs in maintained extraction inputs or `src/taxonmech/seed.py` with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not biological identity. Optional literature enrichment requires a supported persistent curation mechanism, not direct YAML edits.

## Follow-up Checks

- Resolve the paper/accession length discrepancy before literature enrichment; no author/depositor contact was made.
- Require explicit deposit-to-accession provenance for any future culture association, and preserve strain, sample, project, marker and assembly distinctions.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither ran here.
- Reconcile report coverage against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

Relevant primary-paper text was inspected live. Figure 3 was visually inspected in the cached rendering of page 6 of the [published open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf), downloaded during the AH0 review. No new image or PDF was written in the repository. The paper was checked for identity context, not exhaustively curated for physiological or antimicrobial claims. Search-result leads without inspected source text were not used as evidence.

Candidate objects were inspected only as identity leads, not counted as reviews of their taxa. No exhaustive external census, all-alias search or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
