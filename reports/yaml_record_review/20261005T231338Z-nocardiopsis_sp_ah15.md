# YAML Record Review: Nocardiopsis sp. AH15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah15.yaml`
- Started UTC: 2026-10-05T23:09:36Z
- Finished UTC: 2026-10-05T23:13:38Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034866`, Nocardiopsis sp. AH15, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It has ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. It asserts no synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph.

`data/taxa/PATHS.tsv:14185` uniquely resolves the identifier and stem. `curation/seed_scope.tsv:322018` supplies inclusion. Only this new report was written in the repository; no taxon YAML, inventory, scope, history or generated product was changed. Eukaryota was left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah15.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah15.yaml --out /private/tmp/ah15-strict-20261005.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: structured comparisons checked the complete backbone row, reconstructed ancestor chain, seven source inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. The backbone supplies no children of the target.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore searches, full target-marker metadata/features, and relevant primary-paper text and Figure 3.
- Not applicable: target-specific LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No such mappings, graph, gene/regulator assertion or expression module is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. The bounded comparisons do not certify corpus reproduction or publication readiness.

Required repository guidance and relevant schema classes were read earlier in this review sequence at unchanged HEAD. The review skill, checklist, validator definitions and seed-timestamp function were reread for this target; guidance/schema/seeder/target diffs were empty. The ignored-inclusive search below found no target history entry. No history entry, curation event, issue or lifecycle promotion was made, following the read-only review contract.

## Identity and Grounding

The [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034866&retmode=xml) confirms taxon 1034866, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, with no alternate names. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034866) confirms identifier/name/rank and all ten ancestor IDs, including root.

The root-first chain matches the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies the non-root ancestry; Datasets includes root explicitly.

The informal label does not assert validly published species nomenclature. A strain qualifier on a sequence does not change the NCBI concept's rank to STRAIN. `EXACT` identifies this precise NCBI taxon, not a proven equivalence to a named species or to other specimens called AH15.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221715` row and both live NCBI authorities. |
| Lineage | Full reconstructed backbone chain and live authority ancestry. |
| Name without supplied synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31118` supplies the scientific-name object. All three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | The backbone lists only ncbitaxon, snapshot 2026-09-13. Source, ID, label, count, unit and note agree. NAME is not a strain or genome count. |
| Scope and seed event | Scope line 322018 gives inclusion date 2026-09-13 and the exact one-source attested-rule reason; the embedded event text agrees. |
| Seed timestamp | Raw, ATB and StrainInfo manifests give 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The event takes their maximum, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is classified under taxon 1034866, and the backbone supplies no descendants from which strains could be gathered. This is a source-classification count, not a claim that AH15 has never been cultivated. |

The exact query `txid1034866[Organism:noexp]` returned one Nuccore UID, 333497016. Its [JF777512.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497016) was inspected in full, including references and features but excluding sequence bases. It is a 1,418-base partial 16S rRNA gene with both ends partial. Source qualifiers explicitly supply Nocardiopsis sp. AH15, strain AH15, taxon 1034866, Saharan soil, Algeria and collection year 2010. No culture-collection qualifier is supplied.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. The accession metadata supply no DOI or PMID. These data establish submitted marker/specimen context, not a complete genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternate indexing or classification was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, places AH15 in cluster I, with AH17, AH33, AH47, AH57 and AH65. Its 99.4-99.8% similarity range to N. xinjiangensis covers multiple clusters and AH4, not a measured percentage uniquely assigned to AH15. The authors call for further molecular classification work. Figure 3 on page 6 of the [published article PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf) was visually reread and pairs AH15 with JF777512. The reported 1,529-1,544-base sequence range differs from this accession's 1,418 bases; that discrepancy remains unresolved. Neither similarity nor the figure establishes formal synonymy or deposit equivalence. No phenotype or species assignment was transferred.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association for taxon 1034866. Empty optional slots agree with those inputs. Literature evidence is optional for seeded records; the paper does not establish a required missing field.

Bounded searches included ignored and hidden files and compressed native catalogs:

- Identifier, full-label variants and slug were searched with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All six candidate rows were read as complete JSON or header-aware TSV.
- Three rows are target backbone/name/scope. `data/bvbrc/bvbrc-0006.jsonl.gz:6334` instead supplies Mycobacterium tuberculosis ERR1034866, genome 1773.18520, taxon 1773.
- `data/catalog/allthebacteria.tsv.xz:65873` is Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034866, run ERR085019, analysis ERZ3070239. Row 569336 is Mycobacterium tuberculosis run ERR1034866, sample SAMEA3558399, analysis ERZ3500993. Shared digits do not link either sample to the target.
- A separate JF777512 search across the same ten roots returned no matches. This is a bounded local absence, not a required missing genome link.
- An AH15/AH-15/AH 15 screen of the BacDive inventory, native BacDive and native StrainInfo returned no matches. This does not establish global absence of a deposit.
- A supplemental JF777512 or AH15/AH-15/AH 15 search across the same ten roots returned 18 rows. All were read in full. They comprise the three target rows, six rows for other named taxa, two GOLD project/analysis objects and seven assembly objects described below.
- Before report creation, an ignored-inclusive identifier/full-label/slug search of `reports` and `history` returned no matches; a filesystem search found no prior exact-stem report.

The supplemental results preserve taxon/specimen/project boundaries:

- Marinobacter sp. AH15 is taxon 1142072, supported by scope line 343477, backbone line 248264 and `ncbi_names-0006.jsonl.gz:13630`. Flavobacterium sp. AH15 is taxon 1672694, supported by scope line 501187, backbone line 435817 and `ncbi_names-0010.jsonl.gz:19659`. Neither identifies this Nocardiopsis concept.
- `data/gold/projects.jsonl.gz:385444` supplies Gp0528456, PRJNA533779, SAMN11466674, an Iowa agricultural drainage-water community sample named SC45_AH15_S19_L002. `data/gold/analyses.jsonl.gz:297754` supplies its metagenome analysis Ga0468799, without an organism identifier or GenBank accession. AH15 here is part of a sample label, not this taxon.
- `ncbi_refseq-0008.jsonl.gz:44187` and `ncbi_genbank-0053.jsonl.gz:16245` supply paired GCF/GCA_057665905.1, Klebsiella pneumoniae taxon 573, strain AH15, BioSample SAMN54997860.
- `ncbi_genbank-0042.jsonl.gz:32148` supplies GCA_046242015.1, Neisseria gonorrhoeae taxon 485, isolate ah15, BioSample SAMEA114004406.
- `ncbi_genbank-0017.jsonl.gz:38891` and `ncbi_refseq_historical-0000.jsonl.gz:43050` supply paired GCA/GCF_019370105.1, Escherichia coli taxon 562, strain AH15, BioSample SAMN17183254. The RefSeq object is suppressed.
- `ncbi_genbank-0023.jsonl.gz:20004` and `ncbi_refseq_historical-0001.jsonl.gz:5463` supply paired GCA/GCF_025242415.1, Escherichia coli taxon 562, strain AH15, BioSample SAMN26939943. This RefSeq object is also suppressed. All assembly paths in this list are beneath `data/catalog/`.

These objects were inspected as identity leads; no shared strain string was treated as taxon or genome equivalence. No inspected source establishes a consequential missing strain-to-genome link or required taxonomy correction.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in claims asserted by the target YAML. Its identity, lineage, provenance and source-classification count are supported. The paper/accession length discrepancy is an unresolved external-source question, not an error established in this generated record.

## Recommended Edits

None required on current evidence. Do not hand-edit the generated target, attach similarly named cultures/genomes, replace the NCBI parent chain with a named-species assignment or promote the lifecycle to REVIEWED.

A future verified source correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py` with regression coverage, followed by controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature context needs a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Before paper-based enrichment, reconcile the marker-length discrepancy and obtain claim-specific support. No author/depositor contact or external mutation was made.
- Before a culture/genome join, require an explicit accession-to-deposit or accession-to-taxon connection; a shared AH15 designation is insufficient.
- After an authorized upstream/seeder change, run a validated canary and inspect its YAML, then run `just verify-corpus` and `just qc`. Neither gate was run here.
- Reconcile report coverage against actual YAML files independently of ignore rules before claiming completion. Report-file coverage is not human REVIEWED lifecycle status.

## Additional Notes

The NCBI browser HTML was inaccessible through the web reader; EFetch and Datasets succeeded. Figure 3 was re-inspected from the cached PDFKit rendering of the published open-access PDF downloaded during the AH0 review. No new PDF or image was written in the repository. The paper was checked for identity context, not exhaustively curated for phenotype, habitat, medium or antimicrobial evidence.

Other source objects were inspected to assess candidate identity, not counted as reviews of their taxa. No full external source census, exhaustive all-alias search or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The other session is closed; no additional worktree was needed. No record, history, scope, lifecycle, issue or pull request was changed.
