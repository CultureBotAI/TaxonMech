# YAML Record Review: Nocardiopsis sp. AH0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah0.yaml`
- Started UTC: 2026-10-05T22:52:41Z
- Finished UTC: 2026-10-05T22:56:37Z
- Verdict: pass

## Target

The full 53-line generated `TaxonRecord` was read. Its identifier is `NCBITaxon:1034863`, label Nocardiopsis sp. AH0, rank `SPECIES`, domain `BACTERIA`, and parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. It asserts no synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph.

`data/taxa/PATHS.tsv:14182` uniquely resolves its identifier and stem. `curation/seed_scope.tsv:322015` supplies inclusion. Only this new report was written in the repository; the target YAML, inventories, scope, history and generated products remain unchanged. Eukaryota was left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah0.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah0.yaml --out /private/tmp/ah0-strict-20261005.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: structured comparisons checked the entire backbone row, reconstructed ancestor chain, seven source inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. The backbone supplies no children of this taxon.
- PASS: exact-ID checks of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy responses, exact Assembly/Nuccore queries, full target sequence metadata/features, and relevant primary-paper text and Figure 3 were inspected.
- Not applicable: target-specific LPSN/GTDB/BacDive authority-page checks, graph-term validation and iModulonDB. The record has no corresponding mapping, strain link, graph, gene, regulator or expression module.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These corpus-wide checks were not rerun for this bounded review. The local comparisons do not certify corpus reproduction or publication readiness.

The review and curation skills, checklist, CLAUDE guidance, justfile, curation/harmonization/schema guides, history guidance, relevant schema classes and seed-timestamp function were read. Their working-tree diffs and the target diff were empty at unchanged HEAD. No target history entry was found in the ignored-inclusive search below. No history entry, curation event or lifecycle promotion was written, following the read-only review contract.

## Identity and Grounding

The [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034863&retmode=xml) confirms the identifier, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, with no alternate names. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034863) confirms the identifier, name, rank and all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), and unclassified Nocardiopsis (`NO_RANK`). EFetch displays the non-root chain; Datasets includes root explicitly.

This is an informal species-level NCBI concept, not an assertion of validly published species nomenclature. A sequence's strain qualifier does not change the taxonomy node's rank to STRAIN. `EXACT` concerns identity with this NCBI concept, not resolution to a named species or culture deposit.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, parent, rank and genetic code | Full `data/raw/ncbitaxon_taxa.tsv:221712` row and both live NCBI authorities. |
| Lineage | Full reconstructed backbone chain and the live authority ancestry. |
| Scientific name without supplied synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31115` is the scientific-name object; all three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | The backbone lists only ncbitaxon, snapshot 2026-09-13. Source ID, label, count, unit and note agree. NAME is not a strain or genome count. |
| Scope and seed event | Scope line 322015 supplies inclusion date 2026-09-13 and the exact one-source attested-rule reason; the embedded event text agrees. |
| Seed timestamp | Raw, ATB and StrainInfo manifests give 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The event uses their maximum, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is assigned to taxon 1034863, and the backbone has no child taxa from which strains could be gathered. |

The exact query `txid1034863[Organism:noexp]` retrieved one Nuccore UID, 333497012. Its [JF777508.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497012) was read in full, including references and features but excluding sequence bases. It is a 1,420-base partial 16S rRNA gene with both ends marked partial. The source explicitly identifies Nocardiopsis sp. AH0, strain AH0, taxon 1034863, Saharan soil, Algeria and collection year 2010. These are submitted specimen/marker metadata, not proof of a complete genome, deposit equivalence or species-wide phenotype.

The accession references name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished study on halophilic Nocardiopsis from Algerian Sahara soils, and a direct submission dated 2011-03-07. The accession metadata supply no DOI or PMID; a separately inspected later publication is discussed below.

The exact Assembly query returned zero items with a phrase-not-found/no-items response. No assembly was retrieved under that query; this does not establish genome absence under alternate indexing or reclassification.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, discusses AH0 with AH67 in cluster IV and reports close 16S similarity to N. litoralis and N. kunsanensis. Section 3.4 calls for additional molecular work to resolve taxonomic status; similarity is not synonymy. The [article PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf), Figure 3 on page 6, was visually inspected: JF777508 is printed beside both AH0 and AH37. The text also reports 1,529-1,544-base sequences, whereas the current AH0 accession is 1,420 bases. These source discrepancies remain unresolved; the figure does not establish AH0/AH37 equivalence. No phenotype, accession reassignment, formal species identification or culture-deposit link was transferred from this paper.

## Completeness

Exact target lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits inventory associations. The corresponding empty optional slots agree with those inputs. Record-level literature evidence is optional for seeded records; the inspected paper does not create a required missing taxonomic assertion.

Bounded searches included ignored and hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched the identifier, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All seven candidate rows were read as full JSON objects or header-aware TSV rows.
- Three matches are the target backbone, name and scope. `data/bvbrc/bvbrc-0006.jsonl.gz:6327` instead supplies Mycobacterium tuberculosis ERR1034863, genome 1773.18514, taxon 1773.
- `data/catalog/ncbi_genbank-0054.jsonl.gz:17298` supplies Streptococcus pneumoniae isolate 1034863, taxon 1313, assembly GCA_058711765.1, sample SAMEA120831635 and project PRJNA514245. The isolate's digits are not an NCBI taxon identity.
- `data/catalog/allthebacteria.tsv.xz:65870` is Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034863, run ERR084982, analysis ERZ3070243. Row 569333 is Mycobacterium tuberculosis run ERR1034863, sample SAMEA3558396, analysis ERZ3500976. Neither supplies AH0 evidence.
- A supplemental AH0/AH-0/AH 0 alias plus JF777508 search across the same ten roots produced six matches: the three target rows and three GOLD project objects. All three GOLD objects were read in full at `data/gold/projects.jsonl.gz:546528`, line 546529 and line 546530. They describe freshwater-sediment microbial communities from Aha Reservoir, China, labeled AH 0-2-1 through AH 0-2-3, projects Gp0730093 through Gp0730095, BioSamples SAMN16189263 through SAMN16189265, under PRJNA663930. Their organism GOLD ID fields are empty. The prefix match does not identify the Algerian isolate or an individual genome.
- A separate JF777508 search across those ten roots returned no matches. An AH0/AH-0/AH 0 screen of the BacDive inventory, native BacDive and native StrainInfo inputs also returned no matches. These are bounded local absences, not a claim that the strain has never been deposited elsewhere.
- Before report creation, an ignored-inclusive identifier/full-label/slug search of `reports` and `history` found no matches; a filesystem search found no prior report with this exact stem.

No inspected source establishes a consequential missing strain-to-genome link. Partial-marker metadata and unrelated numeric/name matches must not be promoted into genome, culture or synonym assertions. Broader strain/deposit aliases not evidenced by these sources were not inferred.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the target YAML. Its identity, lineage, attestation and seed provenance are supported, and no required representation gap was established. The paper's accession/length discrepancies are external-source cautions, not faults in this record, which does not assert those claims.

## Recommended Edits

None required. Do not hand-edit the generated target, add guessed culture/genome links, replace the carried NCBI placement with a nearest named species, or promote `mapping_status` to REVIEWED.

Any later evidence-backed change belongs in maintained upstream inventories/extraction or `src/taxonmech/seed.py` with a regression test, followed by controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not biological identity. Optional literature enrichment requires a supported persistent curation mechanism; it should not be inserted directly into generated YAML.

## Follow-up Checks

- For future paper-based enrichment, resolve the accession/length discrepancies against primary sequence records or an explicit correction before using them to identify specimens. No author contact or external mutation was made.
- If an explicit culture deposit is established later, inspect the full native deposit and sequence evidence, preserve taxon/strain/deposit/genome/sample/project distinctions, and rerun schema and strict validation.
- After an authorized upstream or seeder change, run a validated canary, inspect the resulting YAML, then run `just verify-corpus` and `just qc`. Those gates were not run here.
- Before publication, reconcile report coverage against actual YAML files independently of ignore rules; report-file coverage is separate from human REVIEWED lifecycle status.

## Additional Notes

The NCBI browser HTML was inaccessible through the web reader; EFetch and Datasets succeeded. The PMC and HAL article endpoints presented access challenges, but publisher text and a copy of the published open-access PDF were inspected. Web screenshot calls did not expose image pixels in the tool result, so the PDF was downloaded to `/private/tmp/ah0-1061176.pdf` and pages 5-6 were rendered with macOS PDFKit and visually read. Poppler was unavailable at the checked executable paths. No access control was bypassed.

The paper was inspected for identity context, not exhaustively curated for phenotype, media, habitat or antimicrobial evidence. The unrelated BV-BRC, GenBank, ATB and GOLD objects were inspected to reject false joins, not counted as reviews of their taxa. No complete external source census or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, issue or pull request was changed.
