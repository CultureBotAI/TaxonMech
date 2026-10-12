# YAML Record Review: Nocardiopsis sp. AH65

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah65.yaml`
- Started UTC: 2026-10-06T00:37:15Z
- Finished UTC: 2026-10-06T00:39:03Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034884`, Nocardiopsis sp. AH65, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It asserts ten ancestors, code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence or graph are asserted.

`data/taxa/PATHS.tsv:14203` uniquely resolves this ID and stem; `curation/seed_scope.tsv:322036` supplies inclusion. Only a new review report was written; records, scope, history and Eukaryota were untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah65.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah65.yaml --out /private/tmp/ah65-validation.tsv`, exit 0, one file, zero errors. The output TSV was read and is header-only.
- PASS: full backbone row, reconstructed lineage, seven inventories, PATHS, scope, attestation and seed-event text agree. The backbone has no target children.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, full target/conflicting-accession metadata, references and features, and primary-paper text/Figure 3.
- Not applicable: graph-term, LPSN/GTDB mapping and iModulonDB checks; no corresponding graph, mapping, gene/regulator or expression-module assertion exists.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. Bounded checks do not prove corpus reproduction or publication readiness.

Required guidance/schema/seeder behavior were fully read in preceding reviews at this HEAD. The review skill, checklist and seed-timestamp implementation were reread this turn; relevant guidance/schema/seeder/target diffs were empty. Source timestamps were verified in the YAML manifests after an initial lookup at the wrong SOURCE.json paths failed. No lifecycle promotion or history entry was made.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034884&retmode=xml) confirms exact ID, label, species rank, bacterial division, parent and genetic code 11. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034884) agrees and supplies all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

This informal name does not assert validly published nomenclature. A marker strain qualifier does not change the taxon's rank. `EXACT` grounds this concept, not N. xinjiangensis or another AH65 organism.

## Evidence

| Assertion | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221733` and live NCBI authorities. |
| Lineage | Full reconstructed backbone chain and live ancestry. |
| Scientific name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31136`; backbone synonyms and live alternate names are empty. |
| NCBITAXON NAME count 1 | Source, ID, label, unit, count and snapshot note agree with the backbone. This is not a specimen/genome count. |
| Inclusion and event | Scope line 322036 provides 2026-09-13 and the exact one-source attested-rule reason; event text agrees. |
| Seed timestamp | 2026-09-13T17:54:04Z is the maximum of raw 17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z extraction times on that date, following `src/taxonmech/seed.py:139`. |
| Zero strains | No BacDive inventory association under this taxon and no backbone descendants. This classification count is not evidence that AH65 was never cultivated. |

The exact `txid1034884[Organism:noexp]` queries returned zero Assembly items with phrase-not-found/no-items messages and one Nuccore UID, 333497033. Complete [JF777529.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497033), references and features were read, excluding bases. It is a 1,418-base partial 16S marker, with source qualifiers AH65, taxon 1034884, Algeria, Saharan soil and collection year 2010, without a culture-collection qualifier.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished study and direct submission on 2011-03-07, with no DOI/PMID. This supports submitted specimen context, not culture-deposit or genome identity. The exact Assembly query is not an exhaustive search under every classification.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, includes AH65 in cluster I within a pooled 99.4-99.8% similarity range to N. xinjiangensis. It does not provide an individual AH65 value there or establish species equivalence. Figure 3 labels AH65 as JF777530, conflicting with NCBI's JF777529. The reported 1,529-1,544-base range differs from 1,418. Both discrepancies remain unresolved.

Complete [JF777530.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=JF777530) identifies AH67, taxon 1034885, and a 1,420-base partial 16S marker. It must not silently replace AH65's accession. These accession/length claims are external and not asserted by the YAML.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034884. Empty optional slots agree with the source inputs; optional literature evidence is not required for a seeded record.

Bounded searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched ID, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding SOURCE.json manifests. All 16 matches were read fully: three target backbone/name/scope rows and thirteen numeric substring matches.
- AH65/AH-65/AH 65/AH_65 returned 27 rows: three target, three other-NCBI-concept, thirteen GOLD, two StrainInfo and six genome rows. All were read as complete native JSON or header-aware TSV, with address reconciliation. No BacDive inventory/native record matched this alias screen.
- JF777529/JF777530 returned no local matches across those ten roots. This includes ignored files, but is not a global external absence claim.
- An ignored-inclusive ID/full-label/slug search of reports/history found only AH65 as conflicting-accession context in the AH63 report, not a prior target review. `find` found no prior exact-stem AH65 report.

Same-designation culture/genome objects below concern different taxa. No consequential missing target strain-to-genome relationship was established. No exhaustive culture census, all-alias search or name-only identity join is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, source provenance and classification count are supported. External paper/NCBI accession and length conflicts remain explicit and constrain future enrichment.

## Recommended Edits

None required on current evidence. Do not hand-edit generated YAML, transfer another AH65's culture/genome, substitute AH67's marker, infer N. xinjiangensis equivalence or promote status to REVIEWED.

A future verified source/link correction belongs in maintained source/extraction inputs or `src/taxonmech/seed.py`, with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not biological identity. Optional literature enrichment needs a persistent supported curation mechanism rather than direct generated-YAML edits.

## Follow-up Checks

- Resolve figure-accession and length discrepancies before reusing those details. No author/depositor contact was made.
- Require explicit target/deposit/sequence provenance for any proposed link; preserve accession versions and entity types.
- Following an authorized upstream change, validate an inspected canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile reports with actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

All alias objects were read and kept separate:

- Achromobacter sp. AH65, taxon 861670: scope 285643, backbone 181180, names shard 0004 line 34864, parent 2626865.
- StrainInfo native row 9540: SI-ID 9540, DOI 10.60712/SI-ID9540.2, Aeromonas bestiarum/taxon 105751, LMG 13673/SI-DP 37706, aliases Altwegg A1722 and Carnahan AH 65, non-type.
- StrainInfo native row 48410: SI-ID 60806, DOI 10.60712/SI-ID60806.1, Aeromonas hydrophila subsp. hydrophila/taxon 196023, NCIMB 13190/SI-DP 211213, alias AH65, non-type. No equivalence between these two Aeromonas records was inferred.
- GOLD organism row 141234: Go0203036, Aeromonas hydrophila AH65, taxon 644, no supplied deposit ID. It is not a Nocardiopsis culture link.
- Four bovine-coronavirus chains: Go/Gp0081503, R-AH65-TC/taxon 422215, PRJNA18581, Ga0057968, EF424618, IMG 2588253600; Go/Gp0081504, E-AH65/taxon 422217, PRJNA18587, Ga0057964, EF424615, IMG 2588253569; Go/Gp0081505, E-AH65-TC/taxon 422218, PRJNA18589, Ga0057965, EF424616, IMG 2588253645; Go/Gp0081509, R-AH65/taxon 422214, PRJNA18573, Ga0057967, EF424617, IMG 2588253613. Full GOLD organism rows 48421/48422/48423/48427, project rows 47643/47644/47645/47649 and analysis rows 36971/36972/36974/36975 were inspected. Entity types remain distinct.
- E. coli AH65, taxon 562: GCA/GCF_013389695.1, SAMN15229516, BV-BRC 562.62728, GTDB RS_GCF_013389695.1. Full rows: BV-BRC shard 0023 line 45660; GenBank 0012 line 2816; RefSeq 0003 line 825; GTDB 0014 line 20358. GTDB supplies China: Fuyang; Anhui, not the target's Algerian context.
- K. pneumoniae AH65, taxon 573: GCA/GCF_057664805.1, SAMN54997893, GenBank 0053 line 16191 and RefSeq 0008 line 44153.

The thirteen numeric substring matches were inspected in full:

- E. coli PNUSAE017633/taxon 562: SAMN10348849, GCA_003753925.1 in BV-BRC 562.36435 (shard 0023 line 36291) and historical GenBank 0000 line 10424; current GCA_003753925.2 in GenBank 0002 line 48022.
- E. coli PNUSAE017482/taxon 562: SAMN10348847, GCA_003767085.1 in BV-BRC 562.36593 (shard 0023 line 36440) and historical GenBank 0000 line 10588; current GCA_003767085.2 in GenBank 0002 line 48675. Historical versions are marked replaced, not conflated with current versions.
- Planctomycetota bacterium PLAN-6/taxon 2026780: GCA_048499555.1, SAMN31034884, GenBank 0044 line 36996 and GTDB 0002 line 26242; GTDB calls it H3-PLA7 sp015075515.
- C. jejuni PNUSAC013714/taxon 197: GCA_010348845.1, SAMN13384289, GenBank 0009 line 6280.
- ATB row 65891: S. dysgalactiae subsp. equisimilis/SAMEA1034884/ERR084996/ERZ3070269; row 569354: M. tuberculosis/SAMEA3558417/ERR1034884/ERZ3501061; rows 1502180/1502181: E. coli/SAMN10348847/SRR8136878/ERZ9092408 and E. coli/SAMN10348849/SRR8136872/ERZ9092410. These sample/run/analysis identifiers do not establish target taxonomy.

Catalog shards are under `data/catalog/`, BV-BRC shards under `data/bvbrc/`, GOLD/StrainInfo rows in their native JSONL files and ATB rows in `data/catalog/allthebacteria.tsv.xz`. Candidate objects and the AH67 marker were identity checks, not separate record reviews.

Primary-paper text and Figure 3 were inspected this turn, including the cached page-6 rendering of the [open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf). No new PDF/image was written in the repository. Phenotype and antimicrobial claims were not exhaustively curated.

Review performed on `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, scope, history, lifecycle, GitHub item or external source was changed.
