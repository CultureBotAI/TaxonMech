# YAML Record Review: Nocardiopsis sp. AH17

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah17.yaml`
- Started UTC: 2026-10-05T23:15:43Z
- Finished UTC: 2026-10-05T23:17:45Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034867`, Nocardiopsis sp. AH17, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It has ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. It asserts no synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph.

`data/taxa/PATHS.tsv:14186` uniquely resolves the identifier and stem; `curation/seed_scope.tsv:322019` supplies inclusion. Only this new report was written in the repository. No record, inventory, scope, history or generated product was changed; Eukaryota was left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah17.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah17.yaml --out /private/tmp/ah17-strict-20261005.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: structured comparisons checked the complete backbone row, reconstructed ancestor chain, seven source inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. The backbone supplies no children of this target.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, full target-marker metadata/features, and relevant primary-paper text and Figure 3.
- Not applicable: target-specific LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No such mappings, graph, gene/regulator assertion or expression module is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. The bounded checks do not certify corpus reproduction or publication readiness.

Required guidance and relevant schema classes were read earlier in this sequence at unchanged HEAD. CLAUDE.md, both record skills, the checklist, validator definitions and seed-timestamp function were reread for this target; guidance/schema/seeder/target diffs were empty. No target history entry was found in the ignored-inclusive search below. No history entry or lifecycle promotion was made, following the read-only review contract.

## Identity and Grounding

The [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034867&retmode=xml) confirms taxon 1034867, the exact label, species rank, bacterial division, parent 2649073 and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034867) confirms identifier/name/rank and all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

An informal name does not assert validly published nomenclature. A sequence's strain qualifier does not change the NCBI concept's species rank. `EXACT` identifies this NCBI taxon, not a proven equivalence to a named Nocardiopsis species or other specimens called AH17.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221716` row and both live NCBI authorities. |
| Lineage | Complete reconstructed backbone chain and authority ancestry. |
| Name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31119` is the scientific-name object; all three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | The backbone lists only ncbitaxon, snapshot 2026-09-13. Source, ID, label, count, unit and note agree. NAME is not a strain or genome count. |
| Scope and seed event | Scope line 322019 gives date 2026-09-13 and the exact one-source attested-rule reason; embedded event text agrees. |
| Seed timestamp | Raw, ATB and StrainInfo manifests give 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The event takes their maximum, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is classified under taxon 1034867, and the backbone supplies no descendants. This is a source-classification count, not a statement that AH17 has never been cultivated. |

The exact query `txid1034867[Organism:noexp]` returned one Nuccore UID, 333497017. Its [JF777513.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497017) was read in full, including references and features but excluding sequence bases. It is a 1,419-base partial 16S rRNA gene, partial at both ends. Source qualifiers supply Nocardiopsis sp. AH17, strain AH17, taxon 1034867, Saharan soil, Algeria and collection year 2010. No culture-collection qualifier is supplied.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. The metadata supply no DOI or PMID. These establish submitted marker/specimen context, not a complete genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternative indexing or classification was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, places AH17 in cluster I alongside AH15, AH33, AH47, AH57 and AH65. Its 99.4-99.8% similarity range to N. xinjiangensis covers several clusters and AH4, not a value uniquely assigned to AH17. Further molecular classification work is recommended. Figure 3, page 6 of the [published article PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf), was visually reread and pairs AH17 with JF777513. The reported 1,529-1,544-base sequence range differs from this accession's 1,419 bases; that discrepancy remains unresolved. No phenotype, formal species synonymy or deposit equivalence was inferred.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association for taxon 1034867. Empty optional fields agree with these inputs. Literature evidence is optional for seeded records; the paper does not establish a required missing field.

Bounded searches included ignored and hidden files and compressed native catalogs:

- Identifier, full-label variants and slug were searched with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All six matching rows were read in full as JSON or header-aware TSV.
- Three are target backbone/name/scope. `data/bvbrc/bvbrc-0006.jsonl.gz:6332` supplies Mycobacterium tuberculosis ERR1034867, genome 1773.18519, taxon 1773.
- `data/catalog/allthebacteria.tsv.xz:65874` supplies Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034867, run ERR084974, analysis ERZ3070250. Row 569337 supplies Mycobacterium tuberculosis run ERR1034867, sample SAMEA3558400, analysis ERZ3500994. Shared digits do not link these to the target.
- A separate JF777513 search across the same ten roots returned no matches. This is bounded local absence, not a missing required genome assertion.
- An AH17/AH-17/AH 17 screen of the BacDive inventory, native BacDive and native StrainInfo returned one object, read in full: `data/straininfo/records.jsonl.gz:380`. SI-ID 380, version DOI 10.60712/SI-ID380.2, is published online and denotes Aeromonas hydrophila subsp. hydrophila taxon 196023, designation Sanyal AH-17, with own available deposit LMG 3770/SI-DP 1872, non-type. It supplies no sequence entries or Nocardiopsis identity.
- A supplemental JF777513 or AH17/AH-17/AH 17 search across the same ten roots returned 19 rows, all read in full. These comprise three target rows, nine other-taxon name/backbone/scope rows, the StrainInfo object, three GOLD objects and three assembly objects.
- Before writing, an ignored-inclusive identifier/full-label/slug search of `reports` and `history` returned no matches; a filesystem search found no prior exact-stem report.

The supplemental source objects were distinguished as follows:

- Marinobacter sp. AH17, taxon 1142074: scope line 343479, backbone line 248266, `data/catalog/ncbi_names-0006.jsonl.gz:13632`.
- Streptomyces sp. AH17-3, taxon 1156352: scope line 347587, backbone line 253303, `data/catalog/ncbi_names-0006.jsonl.gz:19465`. The regex also captures this suffixed label; it is not an alias of the target.
- Halomonas sp. AH17, taxon 1857918: scope line 543135, backbone line 485737, `data/catalog/ncbi_names-0011.jsonl.gz:24328`.
- `data/gold/organisms.jsonl.gz:142898`: Go0204704, Aeromonas hydrophila Sanyal AH-17, taxon 644, no culture accession. It is not this Nocardiopsis taxon; no cross-source strain equivalence was inferred.
- `data/gold/projects.jsonl.gz:385446`: Gp0528458, PRJNA533779, SAMN11466676, an Iowa agricultural-soil community sample SC47_AH17_S17_L006. `data/gold/analyses.jsonl.gz:298318` supplies linked metagenome analysis Ga0469391 with no organism identifier or GenBank accession. Sample-label reuse is not a target identity link.
- `data/catalog/ncbi_genbank-0023.jsonl.gz:20003` and `ncbi_refseq_historical-0001.jsonl.gz:5462` supply paired GCA_025242405.1/GCF_025242405.1, Escherichia coli taxon 562, strain AH17, BioSample SAMN26939945. The RefSeq object is suppressed.
- `data/catalog/ncbi_genbank-0042.jsonl.gz:32123` supplies GCA_046241515.1, Neisseria gonorrhoeae taxon 485, isolate ah17, BioSample SAMEA114004342.

No inspected source establishes a consequential missing strain-to-genome relationship or a required taxonomy correction. A repeated designation alone does not establish identity, and marker DNA is not a whole-genome assembly.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the target YAML's assertions. Its identity, lineage, provenance and source-classification count are supported. The paper/accession length discrepancy is unresolved external evidence, not an error established in this generated record.

## Recommended Edits

None required on current evidence. Do not hand-edit the generated target, attach similarly named cultures/genomes, replace its NCBI parent chain with a named-species assignment or promote it to REVIEWED.

A future verified correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py` with regression coverage, followed by controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment needs a supported persistent curation mechanism rather than a direct YAML edit.

## Follow-up Checks

- Reconcile the marker-length discrepancy before paper-based enrichment and require claim-specific support.
- Require explicit accession-to-deposit or accession-to-taxon provenance before any culture/genome join; AH17 name similarity is insufficient.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile report coverage against actual YAML files independently of ignore rules. Report-file coverage is not human REVIEWED lifecycle status.

## Additional Notes

NCBI browser HTML was inaccessible through the web reader; EFetch and Datasets succeeded. Figure 3 was inspected using the cached PDFKit rendering of the published open-access PDF downloaded during the AH0 review. No new PDF or image was written in the repository. The paper was checked for identity context, not exhaustively curated for phenotype, habitat, medium or antimicrobial evidence.

Candidate objects were inspected to assess identity, not counted as reviews of their taxa. No exhaustive external-source census, all-alias search or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, issue, pull request or external source was changed.
