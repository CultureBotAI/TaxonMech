# YAML Record Review: Nocardiopsis sp. AH1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah1.yaml`
- Started UTC: 2026-10-05T22:58:44Z
- Finished UTC: 2026-10-05T23:01:47Z
- Verdict: pass

## Target

The entire 53-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034864`, Nocardiopsis sp. AH1, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. It asserts no synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph.

`data/taxa/PATHS.tsv:14183` uniquely resolves the identifier and stem; `curation/seed_scope.tsv:322016` supplies inclusion. Only this new review report was written in the repository. The target YAML, inventories, scope, history and generated products were left unchanged. Eukaryota was not reviewed again or edited.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah1.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah1.yaml --out /private/tmp/ah1-strict-20261005.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: structured comparisons checked the full backbone row, reconstructed ancestor chain, seven source inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. The backbone supplies no child taxa.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore searches, full metadata/features for the returned marker, and relevant primary-paper text and Figure 3.
- Not applicable: target-specific LPSN/GTDB/BacDive authority pages, graph-term validation and iModulonDB. The record has no corresponding mappings, strain links, graphs, gene/regulator assertions or expression modules.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. Bounded checks do not certify corpus reproduction or publication readiness.
- Supplemental lookup limitation: a full parsed StrainInfo scan found no native record with SI-ID 24942, referenced by a non-target BacDive object. Its cardinality assertion exited 1, and a separate ignored-inclusive search corroborated that bounded absence. This is not a target-validator failure or an unresolved target identity.

Required repository guidance and relevant schema classes were read in the preceding review at the same HEAD. The review skill, checklist, validator definitions and seed-timestamp function were reread for this target; guidance/schema/seeder/target diffs were empty. No target history entry was found in the ignored-inclusive search below. The read-only review contract takes precedence over guidance asking for a history entry or issue: neither was created, and no lifecycle status was promoted.

## Identity and Grounding

The [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034864&retmode=xml) confirms taxon 1034864, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, with no alternate names. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034864) confirms the identifier/name/rank and all ten ancestor IDs, including root.

The carried root-first chain matches the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch displays non-root ancestry; Datasets includes root explicitly.

The informal label does not assert validly published species nomenclature. The marker's AH1 strain qualifier does not turn this species-ranked NCBI concept into a STRAIN-ranked node. `EXACT` identifies the precise NCBI concept; it does not establish identity with a named species, another AH1 isolate or a culture deposit.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, rank, parent, code | Full `data/raw/ncbitaxon_taxa.tsv:221713` row and both live NCBI authorities. |
| Lineage | Full reconstructed ancestor chain and live authority ancestry. |
| Name without supplied synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31116` supplies the scientific-name object. All three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | The backbone lists only ncbitaxon, snapshot 2026-09-13. Source, identifier, label, count, unit and note agree. NAME is not a strain or genome count. |
| Scope and seed-event text | Scope line 322016 supplies inclusion date 2026-09-13 and the exact one-source reason; the embedded event text agrees. |
| Seed timestamp | Raw, ATB and StrainInfo manifests give 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The event takes their maximum, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is assigned to the target, and its backbone node has no children from which strains could be gathered. |

The exact query `txid1034864[Organism:noexp]` retrieved one Nuccore UID, 333497013. Its [JF777509.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497013) was read in full, including references and features but excluding sequence bases. It is a 1,421-base partial 16S rRNA gene with both ends partial. Source qualifiers explicitly identify Nocardiopsis sp. AH1, strain AH1, taxon 1034864, Saharan soil, Algeria and collection year 2010. These are marker/specimen metadata, not a complete genome, deposit equivalence or species-wide phenotype.

The accession references name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. They supply no DOI or PMID. The later paper below was located independently; it was not asserted to be present in the accession's reference fields.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved by that query; this is not proof of genome absence under alternate classification or indexing.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, groups AH1 with AH52 in cluster V and reports 16S similarity to N. litoralis and N. kunsanensis. Section 3.4 calls for further molecular work to resolve taxonomic status. Figure 3 on page 6 of the [published article PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf) was visually reread: AH1 is paired with JF777509, consistent with NCBI. The paper's 1,529-1,544-base length range differs from the current 1,421-base accession; that discrepancy remains unresolved. Similarity and cluster membership do not establish synonymy or deposit identity. No phenotype, genome link or formal species assignment was transferred.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association for taxon 1034864. Empty optional slots agree with these inputs. Record-level literature evidence is optional for seeded records; finding the paper does not establish a required missing field.

The ignored-inclusive, hidden-file and compressed-catalog searches were bounded as follows:

- Identifier, full-label variants and slug were searched using `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. A trailing label boundary avoids treating AH12 or AH15 as AH1. All seven candidate rows were read in full as JSON or header-aware TSV.
- Three rows are target backbone/name/scope. `data/bvbrc/bvbrc-0006.jsonl.gz:6328` is Mycobacterium tuberculosis ERR1034864, genome 1773.18515, taxon 1773.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:11578` is Listeria monocytogenes strain 1034864, taxon 1639, assembly GCA_015693045.1, sample SAMN16930283, project PRJNA248549. A strain designation made of the same digits is not the target taxon.
- `data/catalog/allthebacteria.tsv.xz:65871` is Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034864, run ERR084998, analysis ERZ3070244. Row 569334 is Mycobacterium tuberculosis run ERR1034864, sample SAMEA3558397, analysis ERZ3500973. Neither supplies target evidence.
- A separate JF777509 search across those ten roots returned no matches. This bounded local absence does not turn the marker into a missing genome link.
- An AH1/AH-1/AH 1 screen of the BacDive inventory, native BacDive and native StrainInfo matched 11 lines. Candidate-address enumeration recovered the sequence-description-only match omitted from the initial context display. Both inventory rows and all nine native objects were inspected in full.
- Before writing this report, an ignored-inclusive identifier/full-label/slug search of `reports` and `history` returned no matches; a filesystem search found no prior exact-stem report.

The two BacDive objects distinguish reused designations:

- BacDive 3132, native line 3030 and inventory line 3031, supplies Corynebacterium xerosis WS 1869 AH1-1, taxon 1725, deposit DSM 43607, non-type flag and no sequence information.
- BacDive 159722, native line 81958 and inventory line 81959, supplies Shinella pollutisoli AH-1, taxon 2250594, deposits KCTC 52677/CCTCC AB 2017242, type flag, marker KY054581, assemblies GCA_024609765/GCA_042643305 and BV-BRC/IMG identifiers 2250594.3/8055573482. These source associations were not transferred to Nocardiopsis, nor treated as proof that the two assemblies are identical.

The seven StrainInfo objects in `data/straininfo/records.jsonl.gz` likewise supply no target identity:

| Native line | SI-ID and inspected context |
|---|---|
| 38184 | 50372, published online, Corynebacterium xerosis taxon 1725, WS 1869 AH1-1, DSM 43607/SI-DP 168560; no sequence entries. |
| 83962 | 118489, published offline, Clostridium taxon 1485, AH-1/FERM-P 6093, ATCC 39045/SI-DP 355048; no sequence entries. |
| 88535 | 123254, published online, Thanatephorus cucumeris taxon 107832, AH-1, IFO/NBRC 30460; no sequence entries. |
| 88843 | 123565, published online, Aspergillus heterothallicus taxon 41742, ten deposits with differing type flags and historical Emericella labels. The matched Ah1.101 occurs only in AY924882's 5S description. AY924882, EF652499 and U29870 explicitly name NRRL 5096/SI-DP 688706, not target AH1. |
| 109121 | 156323, published online, Rhizoctonia solani taxon 456999, AH-1/4-0-095/IPO 04R02, CBS 101775 and ATCC 76126; no sequence entries. |
| 197792 | 255825, published online, Rhizoctonia taxon 1322061, AH-1, ATCC 38670/SI-DP 600720; no sequence entries. |
| 210998 | 269054, published online, Bacillus pumilus taxon 1408, Verdon AH1, LMG 28897/SI-DP 21396; no sequence entries. |

BacDive 159722 also references SI-ID 24942. A full parsed native StrainInfo scan found no `strain.siID == 24942`; an ignored-inclusive search for its SI-ID, typed strain identifier and JSON siID forms across `data/straininfo` found no match. That non-target pointer remains unresolved locally. It supplies no identity chain to AH1 and is not a broken reference asserted by the target YAML.

These are candidate-rejection checks, not full reviews of the other taxa. In particular, source objects for fungi were read only to exclude false joins; no eukaryotic TaxonMech records were reviewed or edited.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the target YAML. Identity, lineage, provenance and source counts are supported, and no consequential missing representation was established. The paper's length discrepancy and non-target StrainInfo pointer are external-source limitations, not errors in claims made by this record.

## Recommended Edits

None required. Do not hand-edit the generated target, add guessed culture/genome links, equate reused AH1 labels, substitute a nearest named species for the carried NCBI lineage, or promote the lifecycle to REVIEWED.

Future evidence-backed fixes belong in maintained source inventories/extraction or `src/taxonmech/seed.py` with regression coverage, followed by controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment needs a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Before future paper-based enrichment, reconcile the sequence-length discrepancy against primary sequence records or an explicit correction. No author contact or external mutation was made.
- If a culture deposit is later established, inspect the complete deposit and sequence chain; preserve strain, taxon, deposit, genome, sample and project distinctions. Reused designations alone are insufficient.
- After an authorized upstream/seeder change, run a validated canary, inspect its YAML, then run `just verify-corpus` and `just qc`. These gates were not run here.
- Reconcile report coverage against actual YAML files independently of ignore rules before claiming completion. Report coverage is not human REVIEWED lifecycle status.

## Additional Notes

The NCBI browser HTML was inaccessible through the web reader; EFetch and Datasets succeeded. Relevant publisher text was read, and Figure 3 was re-inspected from the cached PDFKit rendering of the published open-access PDF downloaded during the AH0 review. No new PDF or image was written in the repository.

The literature check was for identity context, not an exhaustive phenotype, habitat, medium or antimicrobial review. No complete external source census, all-alias search or whole-genome equivalence analysis is claimed. The inspected native objects are source snapshots, not claims of current live culture availability.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, issue or pull request was changed.
