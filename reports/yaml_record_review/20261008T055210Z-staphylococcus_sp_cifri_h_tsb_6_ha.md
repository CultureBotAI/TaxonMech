# YAML Record Review: Staphylococcus sp. CIFRI H-TSB-6-HA

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_6_ha.yaml`
- Started UTC: 2026-10-08T05:47:01Z
- Finished UTC: 2026-10-08T05:52:10Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1036323`, label `Staphylococcus sp. CIFRI H-TSB-6-HA`. The complete 54-line YAML was read before judgment. It carries species rank, BACTERIA domain, parent `NCBITaxon:91994`, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event dated `2026-09-13T17:54:04Z`. No taxon, source, history or lifecycle field was changed.

## Validation

Validation used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_6_ha.yaml` | Passed; no issues found. |
| `just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_6_ha.yaml --out /private/tmp/sh6-strict.tsv` | Passed; one file, zero ERROR rows. Header-only TSV inspected. |
| Structured source comparison | Identity, parent, genetic code, all ten ancestors, synonyms, attestation, PATHS entry and scope-derived seed text match pinned inputs. |
| Type/lifecycle lookup | No exact target row in `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` or `dropped.tsv`. |
| Authority/reference verification | Live NCBI Taxonomy EFetch and Datasets checked; exact nucleotide source and reference metadata inspected. No record DOI, PMID, LPSN, GTDB, graph or strain reference requires another authority check. |
| History | Embedded seed event checked. Ignored-inclusive history content and filename searches found no target history artifact. No history was created; full `just validate-history` not run. |
| `just validate-products` | Not applicable: no curator-added graph nodes. |
| Primary-literature limits | Fish-paper text was accessible, including the complete relevant identification/discussion pages. PDF download returned HTTP 403 and page-image requests failed, so no visual audit is claimed. Thesis PDF download returned HTTP 403; full-text and handle opens failed. Thesis content remains unverified. |
| Full-corpus gates | Not run: `just verify-corpus`, provenance, render/site drift, documentation statistics, full tests, vendored checks or `just qc`. Focused checks do not establish whole-corpus reproduction. |

## Identity and Grounding

The exact pinned row is `data/raw/ncbitaxon_taxa.tsv:222327`; the scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31871`. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036323&retmode=xml) agrees with the scientific name, species rank, parent 91994, Bacteria division, genetic code 11 and labeled ancestry. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036323) confirms its root-inclusive identifier chain and rank.

All ten ancestors were checked: root (1), cellular organisms (131567), Bacteria (2), Bacillati (1783272), Bacillota (1239), Bacilli (91061), Caryophanales (1385), Staphylococcaceae (90964), Staphylococcus (1279), and unclassified Staphylococcus (91994). IDs, labels, ranks and ordering agree with the pinned backbone; the live labeled chain agrees too. Inspected pinned synonym fields and live OtherNames supply no alternative name. This is an isolate-designated species-rank NCBI concept, not a registered deposit, another similarly named isolate or a formally established species epithet. Exact grounding does not independently determine biological species identity.

The unique slug mapping is `data/taxa/PATHS.tsv:14834`; the scope row is `curation/seed_scope.tsv:322574`. The reason is reproduced correctly in the seed event. Species rank is eligible under repository policy, and a complete pinned-backbone scan found no direct children.

## Evidence

The NCBITAXON attestation agrees with the exact source row: the same ID and label, one `NAME`, snapshot `2026-09-13`. A mapping predicate is unnecessary because the record is the source concept. The count is not evidence of a phenotype, genome or total biological strains.

Exact-taxon Nuccore search returned UID 334303348. [GenBank JF799910.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799910.1) is a 1,438-base partial 16S rRNA sequence. Its organism, strain `CIFRI H-TSB-6-HA` and `taxon:1036323` match. Source qualifiers state marine water and `India: W.B.`. References name Behera, Sharma, Das, Chanda and Patra, an unpublished salt-tolerant-bacteria study and their 11 April 2011 direct submission. Creation and update dates are 5 June 2011. Complete top-level, source-feature and reference metadata were read; sequence bases and non-source features were not audited. No culture deposit or assembly occurs in that inspected source metadata. The marker is not a genome or a quantitative salt-tolerance result.

Sarkar and Ghosh's 2014 [primary fish-microbiota paper](https://www.fisheriesjournal.com/archives/2014/vol2issue2/PartB/13.pdf), International Journal of Fisheries and Aquatic Studies 2(2):78-88, was inspected in text: title/authors, sampling and identification methods, section 3.7, Table 8 and discussion on pages 84-86. Table 8 reports OmM3 as 100% similar to the reference sequence JF799910; the discussion names CIFRI H-TSB-6-HA as that reference. OmM3 is a newly studied fish-gut isolate, not an explicitly linked deposit of the CIFRI isolate. Sequence similarity does not establish culture identity. Therefore the enzyme, gut-association and possible probiotic observations cannot transfer to this target. A discussion sentence switches to Streptococcus despite the Staphylococcus comparison; it supplies no reliable target pathogenicity claim. This is a source-text caution, not a defect in this YAML, which asserts none of those phenotypes. No quantitative assay or micrograph audit was performed.

The related [Behera paper, DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was inspected earlier in this continuing session using publisher metadata/abstract and [author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). The complete Tables 1 and 2 do not list H-TSB-6-HA or JF799910. Neighboring CIFRI designations cannot substitute for this isolate.

Search also surfaced a [Walmsley thesis lead](https://core.ac.uk/download/pdf/145049917.pdf) about South African sponge-associated bacteria. The primary thesis body could not be opened or downloaded, and the handle route was inaccessible. Search-snippet content was not accepted as evidence. No sponge association, interaction, metabolite or sequence-similarity value from that lead informs the record verdict.

## Completeness

Complete raw BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin and BactoTraits taxon inventories yielded no exact target row. No pinned descendants provide an alternate BacDive inheritance path. Zero strains and the empty listing therefore agree with this inventory, not an assertion that no biological isolate exists. No supported omission was established for synonyms, nomenclature, mappings, xrefs or strain/genome links. Optional definition, literature evidence, discussions and mechanisms need not be manufactured.

Absence searches included ignored and hidden files using `rg --no-ignore --hidden -n -z -i`. Numeric ID, slug and flexible name variants were searched across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 16 candidate rows were read as complete parsed JSON or TSV objects. Three concern this target; thirteen are unrelated numeric collisions: ten fungal GOLD sample IDs, one E. coli assembly sample, its ATB sample row and a Salmonella ATB SeqKit checksum. None supplies a target culture/deposit/genome chain. All five `SOURCE.json` files were parsed separately and history filenames were searched independently of ignore rules. Expanded accession, literature-title/DOI/handle and name searches found only the same three target rows. Ignored-inclusive filename search over records, reports and history found the one target YAML and no prior report for its stem.

The exact-taxon Assembly query returned zero with a phrase-not-found warning; this is bounded evidence, not global genome absence. Web searches covered the exact designation, accession and identified literature leads, not an exhaustive bibliography. iModulonDB was not applicable: this record contains no gene, regulator, transcriptomic dataset or mechanism claim, and near-relative enzyme observations do not create one.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in this YAML. Inaccessible thesis text and missing PDF visual checks limit external-literature assessment; they do not establish wrong grounding or a supported omission in the reviewed record.

## Recommended Edits

None required. Do not equate OmM3 with the CIFRI culture, transfer phenotypes from a closest-reference match, treat the marker as a genome, infer a registered culture deposit, hand-edit generated YAML or promote its review status.

Future accepted NCBI corrections belong upstream, then through the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Proven harmonization errors belong in `src/taxonmech/seed.py` with tests; scope decisions belong in `curation/seed_scope.tsv`. No such owner defect was established. Any enrichment requires a separately authorized curation workflow.

## Follow-up Checks

No mandatory record repair is outstanding. Before using the thesis, obtain readable primary text and inspect the exact comparison and experimental scope. Before phenotype or strain/genome enrichment, require an explicit exact-isolate/deposit/source chain; a sequence-reference match is insufficient. After an authorized input or seeder correction, run the documented dry-run seed, single-record canary, focused validators, full reproduction, provenance, relevant tests, generated-product and QC gates. Human sign-off owns review-status promotion.

## Additional Notes

Baseline HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`. Initial and pre-report YAML SHA-256 agree: `62f043696aa3642aa463fefacef12443db0cf28e4f0fe42f7743e83779029a19`.

The review skill and PDF read-only guidance were reread; local validator/ownership guidance and relevant schema classes were read earlier in this continuing unchanged-HEAD session. No PDF authoring, paid research, source refresh, YAML/source/history change, record regeneration, outreach, GitHub mutation or Eukaryota review occurred. Existing worktrees were preserved. The review contract overrides history scaffolding, and this report does not promote `mapping_status`.
