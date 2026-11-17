# YAML Record Review: Nocardiopsis sp. AH12

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah12.yaml`
- Started UTC: 2026-10-05T23:04:15Z
- Finished UTC: 2026-10-05T23:07:04Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034865`, Nocardiopsis sp. AH12, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. It asserts no synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph.

`data/taxa/PATHS.tsv:14184` uniquely resolves the identifier and stem. `curation/seed_scope.tsv:322017` supplies inclusion. Only this new report was written in the repository. No taxon YAML, inventory, scope, history or generated product was changed; Eukaryota was left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah12.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah12.yaml --out /private/tmp/ah12-strict-20261005.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: structured comparisons checked the full backbone row, reconstructed ancestor chain, seven source inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. The backbone supplies no children of the target.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore searches, full target-marker metadata/features, the candidate's BacDive and DSMZ pages, and relevant primary-paper text and Figure 3.
- Not applicable: target-specific LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No such mappings, graph, gene/regulator assertion or expression module is present. Candidate culture classification was checked separately without transferring it.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. The bounded comparisons do not certify corpus reproduction or publication readiness.

Required repository guidance and relevant schema classes were read earlier in this review sequence at unchanged HEAD. The review skill, checklist, validator definitions and seed-timestamp function were reread for this target; guidance/schema/seeder/target diffs were empty. No target history entry was found in the ignored-inclusive search below. No history entry, curation event, issue or lifecycle promotion was made, following the read-only review contract.

## Identity and Grounding

The [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034865&retmode=xml) confirms taxon 1034865, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, with no alternate names. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034865) confirms identifier/name/rank and all ten ancestor IDs, including root.

The root-first chain matches the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch displays the non-root ancestry; Datasets includes root explicitly.

The informal name does not assert validly published species nomenclature. A strain qualifier on a sequence does not change the NCBI concept's rank to STRAIN. `EXACT` identifies this precise NCBI taxon, not a proven equivalence to DSM 45469 or a named Nocardiopsis species.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, parent, rank and code | Full `data/raw/ncbitaxon_taxa.tsv:221714` row and both live NCBI authorities. |
| Lineage | Full reconstructed backbone chain and live authority ancestry. |
| Name without supplied synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31117` supplies the scientific-name object. All three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | The backbone lists only ncbitaxon, snapshot 2026-09-13. Source, ID, label, count, unit and note agree. NAME is not a strain or genome count. |
| Scope and seed event | Scope line 322017 gives inclusion date 2026-09-13 and the exact one-source attested-rule reason; the embedded event text agrees. |
| Seed timestamp | Raw, ATB and StrainInfo manifests give 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The event takes their maximum, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is classified under taxon 1034865, and the backbone supplies no descendants from which strains could be gathered. This is a source-classification count, not a statement that AH12 has never been cultivated. |

The exact query `txid1034865[Organism:noexp]` returned one Nuccore UID, 333497015. Its [JF777511.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497015) was inspected in full, including references and features but excluding sequence bases. It is a 1,419-base partial 16S rRNA gene with both ends partial. Source qualifiers explicitly supply Nocardiopsis sp. AH12, strain AH12, taxon 1034865, Saharan soil, Algeria and collection year 2010. No culture-collection qualifier is supplied.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. The accession metadata supply no DOI or PMID. These data establish submitted marker/specimen context, not a complete genome or a deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; genome absence under alternate indexing or classification was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, reports AH12 as a single isolate, with 98.7% 16S similarity to N. litoralis, and calls for further molecular work on taxonomic status. Figure 3 on page 6 of the [published article PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf) was visually reread: AH12 is paired with JF777511. Its reported 1,529-1,544-base sequence range differs from the current 1,419-base accession. That discrepancy remains unresolved. Neither similarity nor the figure establishes a deposit link or formal species synonymy; no phenotype or classification was transferred.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association for taxon 1034865. Empty optional slots agree with those inputs. Literature evidence is optional for seeded records; the paper does not establish a required missing field.

Bounded searches included ignored and hidden files and compressed native catalogs:

- Identifier, full-label variants and slug were searched with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All six candidate rows were read as full JSON or header-aware TSV.
- Three rows are target backbone/name/scope. `data/bvbrc/bvbrc-0006.jsonl.gz:6325` instead supplies Mycobacterium tuberculosis ERR1034865, genome 1773.18512, taxon 1773.
- `data/catalog/allthebacteria.tsv.xz:65872` is Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034865, run ERR085056, analysis ERZ3070242. Row 569335 is Mycobacterium tuberculosis run ERR1034865, sample SAMEA3558398, analysis ERZ3500977. Shared digits do not link either sample to the target.
- A separate JF777511 search across the same ten roots returned no matches. This is a bounded local absence, not a required missing genome link.
- An AH12/AH-12/AH 12 screen of the BacDive inventory, native BacDive and native StrainInfo matched four lines. The inventory row and all three native objects were read in full.
- A supplemental search for DSM 45469 and its typed culture/StrainInfo identifiers across the same ten roots returned seven rows. All were read in full, including the additional crosswalk rows described below.
- Before report creation, an ignored-inclusive identifier/full-label/slug search of `reports` and `history` returned no matches; a filesystem search found no prior exact-stem report.

The culture candidate requires explicit caution:

- `data/bacdive/records.jsonl.gz:82772` and inventory line 82773 supply BacDive 160536, Nocardiopsis xinjiangensis AH12, taxon 124285, DSM 45469, non-type flag, and an empty sequence-information object.
- `data/straininfo/records.jsonl.gz:304782` supplies SI-ID 406893, version DOI 10.60712/SI-ID406893.1, published-online status, BacDive 160536 and designation AH12. Its own available deposit DSM 45469/SI-DP 914227 is likewise classified as N. xinjiangensis taxon 124285 and is non-type. No sequence entries are supplied.
- `data/straininfo/strain_links.tsv:59925` and `related_records.tsv.gz:140835`/line 140836 preserve that exact DSM deposit chain, creating typed SI strain/deposit references under taxon 124285. `data/raw/culture_collection_strains.tsv:81469` agrees. None is a marker or assembly assertion.
- The inspected [BacDive page](https://bacdive.dsmz.de/strain/160536) supports AH12/DSM 45469, taxon 124285, Algerian Saharan soil and an N. Sabaou laboratory history. Its sequence section supplies no target accession. The native non-type flag was retained; an unqualified page heading was not treated as a type-strain assertion.
- The [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-45469) identifies the deposit as N. xinjiangensis, supplied by N. Sabaou, LPBVB, Kouba, and says it was preserved as Nocardiopsis sp. until 2014. It gives sampling year 2003, unlike the marker's 2010. The inspected catalogue text does not name JF777511 or target taxon 1034865.
- Shared designation, genus, region and laboratory context make this a plausible candidate, not a demonstrated equivalence. Different classifications and collection dates are preserved. The evidence does not prove either that the specimens are identical or that they are different. No culture link, synonym, genome or reclassification was inferred.

The remaining full native object, `data/straininfo/records.jsonl.gz:378`, is SI-ID 378, published online, Aeromonas hydrophila subsp. hydrophila taxon 196023, designation Sanyal AH-12, own deposit LMG 3767/SI-DP 1868, non-type, with no sequence entries. It supplies no Nocardiopsis identity.

No inspected source establishes a consequential missing strain-to-genome link or a required taxonomy correction. The DSM candidate remains an explicit unresolved identity lead, not negative evidence and not an authorized join.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in claims asserted by the target YAML. Its identity, lineage, provenance and source-classification count are supported. The potential DSM 45469 relationship and the paper's sequence-length discrepancy are unresolved external-source questions; neither is an error established in this generated record.

## Recommended Edits

None required on current evidence. Do not hand-edit the generated target, add DSM 45469 by name similarity, replace the NCBI parent chain with a named-species assignment, or promote the lifecycle to REVIEWED.

Before any culture-link change, obtain an explicit primary-source connection between DSM 45469 and JF777511/taxon 1034865, and reconcile the conflicting dates/classifications. A confirmed upstream correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py` with regression coverage, followed by controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature context needs a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Resolve the DSM candidate using explicit deposit-to-accession provenance or an authoritative correction. Shared names and source-region context are insufficient; preserve any remaining classification disagreement.
- Before paper-based enrichment, reconcile the marker-length discrepancy. No author/depositor contact or external mutation was made.
- After an authorized upstream/seeder change, run a validated canary and inspect its YAML, then run `just verify-corpus` and `just qc`. Neither gate was run here.
- Reconcile report coverage against actual YAML files independently of ignore rules before claiming completion. Report-file coverage is not human REVIEWED lifecycle status.

## Additional Notes

The NCBI browser HTML was inaccessible through the web reader; EFetch and Datasets succeeded. The first direct DSMZ catalogue open failed, but following its BacDive link succeeded and the substantive record text was inspected. The StrainInfo web reader did not return usable record details, and a later direct open failed; its full native snapshot was read instead. No access control was bypassed.

Figure 3 was re-inspected from the cached PDFKit rendering of the published open-access PDF downloaded during the AH0 review. No new PDF or image was written in the repository. The paper was checked for identity context, not exhaustively curated for phenotype, habitat, medium or antimicrobial evidence.

The other source objects were inspected to assess candidate identity, not counted as reviews of their taxa. No full external source census, exhaustive all-alias search, complete culture-identity resolution or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, issue or pull request was changed.
