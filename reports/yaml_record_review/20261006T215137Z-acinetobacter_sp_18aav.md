# YAML Record Review: Acinetobacter sp. 18AAV

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_18aav.yaml`
- Started UTC: 2026-10-06T21:45:27Z
- Finished UTC: 2026-10-06T21:51:37Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035318` denotes Acinetobacter sp. 18AAV, `SPECIES` in `BACTERIA`, parent `NCBITaxon:196816`. It asserts ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried strains, one NCBITAXON NAME attestation, and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain entries, genomes, phenotypes, citations or causal graphs are asserted. Generated fields are read-only; future corrections belong to maintained extraction/seeding code, upstream transforms or scope decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/acinetobacter_sp_18aav.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/acinetobacter_sp_18aav.yaml --out /private/tmp/a18-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and is header-only.
- Structured comparisons read the complete backbone row, all ancestors, direct children, seven non-NCBI inventories, PATHS, scope, attestation and seed-event text. All compared fields agree.
- Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive searches, lossless native candidate reads, parsing of five SOURCE.json files and independent history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0 with network access; all 28 rows inspected before external follow-ups. `a_baumannii/precise139` is not 18AAV. No exact organism/dataset match: iModulonDB is not applicable, not negative biological evidence.
- Live NCBI taxonomy XML/JSON, exact-organism Assembly/nuccore searches, all four sequence records' complete metadata excluding bases/translations, and an independent Datasets genome query succeeded.
- All ten ambiguous ATB BioSample candidates were independently fetched and read in full at NCBI.
- Relevant publisher text and original Figure 1 were inspected for the 2011 paper. PubMed metadata/abstract and the publisher abstract were inspected for the 2015 paper. Its supplementary DOCX was retrieved and structurally parsed, but embedded EMF table images were not rendered or interpreted.
- Not checked: full-corpus `just verify-corpus`, QC/history/provenance gates, full tests, page rendering, original-taxdump regeneration, source hashes, full 2015 article, or supplementary assay-table values. No target-only reproduction gate was invented; manual source comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone `data/raw/ncbitaxon_taxa.tsv:222011`, scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31486`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035318&retmode=xml), and [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035318) agree on the exact identity, rank, parent, bacterial placement and code.

Every ancestor ID, label and normalized rank agrees: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Moraxellales; Moraxellaceae; Acinetobacter; unclassified Acinetobacter. Datasets includes root ID 1, which EFetch omits from its displayed lineage.

Pinned synonym fields and live alternate-name content are empty; the backbone has no direct children. NCBI species rank does not establish a formal binomial or type strain. 18AAV is not 16AAV, A. baumannii, or another Acinetobacter strain.

## Evidence

The NCBITAXON attestation correctly represents one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14502` maps the identifier to this stem; `curation/seed_scope.tsv:322283` supplies the exact scope reason in the event. Raw, ATB and StrainInfo extraction timestamps were parsed as 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the seed timestamp under the inspected `_seed_timestamp` rule. This is provenance, not human sign-off.

Exact nuccore search returned four records, all with explicit source strain 18AAV and taxon 1035318:

| Accession | UID | Bounded source annotation |
| --- | --- | --- |
| [HQ449642.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449642.1) | 338163884 | 636 bp partial 16S rRNA gene |
| [HQ449663.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449663.1) | 342316603 | 897 bp partial aoxB CDS; arsenite oxidase large subunit; protein AEL22197.1 |
| [JQ080890.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080890.1) | 444747328 | 670 bp partial ACR3(1) CDS; arsenite efflux pump; protein AGE12062.1 |
| [JQ080897.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080897.1) | 444747340 | 421 bp partial ACR3(2) CDS; arsenite efflux pump; protein AGE12068.1 |

All source features locate the strain in sediment from Sainte Marie aux Mines, France; the HQ records specify arsenic-contaminated sediment. CDS translation tables are 11. HQ sequences were submitted 28-Oct-2010 from Strasbourg, and JQ sequences 25-Nov-2011 from Metz. These annotations establish gene-sequence provenance, not genomes, registered deposits, measured resistance thresholds or experimentally demonstrated transport.

Both HQ sequences cite [Heinrich-Salmeron et al., AEM 77(13):4685-4692 (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), PMID 21571879, PMCID PMC3127681. Figure 1 explicitly labels 18AAV Acinetobacter sp. HQ449642, distinct from adjacent 16AAV. Its bold/underlined group-II label indicates an aoxB-PCR-positive isolate, without the circle used for demonstrated arsenite oxidation. The text reports positive activity under the tested conditions only among Pseudomonas, Bacillus and Bosea isolates. Gene detection therefore must not become a measured positive oxidation claim for 18AAV; non-detection under those conditions is not universal incapacity.

Both JQ sequences cite [Cordi et al., Environmental Science and Pollution Research 22:13753-13763 (2015), DOI 10.1007/s11356-014-3840-5](https://link.springer.com/article/10.1007/s11356-014-3840-5), independently verified as [PMID 25721523](https://pubmed.ncbi.nlm.nih.gov/25721523/). The inspected abstract describes 219 isolates, gene screening and condition-dependent sensitivity, and cautions that multiple carrier genes or aioA do not ensure high resistance. It does not provide an exact 18AAV assay row. No strain-specific sensitivity, resistance or medium-growth value is inferred from the collection-level abstract.

Exact-organism Assembly search returned count 0 with a no-items/phrase warning; the independent [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035318/dataset_report) returned an empty object. These bounded queries do not prove global genome absence.

Full [BioSample XML for SAMN10353180 through SAMN10353189](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353189%2C10353188%2C10353187%2C10353186%2C10353185%2C10353184%2C10353183%2C10353182%2C10353181%2C10353180&retmode=xml) resolves every ambiguous numeric hit to a human-associated Chinese sample collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. None names 18AAV or taxon 1035318; these are distinct from the French sediment isolate.

## Completeness

The seeded identity is complete enough. Optional gene, habitat or functional evidence is not a missing required field. Phenotypes belong in sibling resources under repository curation rules. `strain_count: 0` counts inventoried BacDive entries, not every biological isolate; a GenBank strain qualifier does not establish a registered culture deposit.

The source search used `rg --no-ignore --hidden -n -z -i` with `1035318|18[-_ ]?AAV\b|acinetobacter_sp_18aav` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files were parsed completely and history filenames searched independently.

All sixteen candidate lines were inspected losslessly: three JSON objects and thirteen TSV rows. Three are exact backbone, scientific-name and scope entries. Thirteen do not supply target evidence:

| Candidates | Why excluded |
| --- | --- |
| Two M. tuberculosis entries | BV-BRC 1773.18328 and ATB SAMEA3558851/ERZ9334479 refer to run ERR1035318, not this TaxID. ATB has PASS filters and a FASTA, but identifies M. tuberculosis, not Acinetobacter. |
| Ten unknown ATB entries | SAMN10353180 through SAMN10353189 are NOT_PROCESSED, with no FASTA, run or assembly accession. The authority records independently resolve them to the unrelated study described above. |
| One C. jejuni assembly | GCA_010353185.1, strain FSIS12027787, SAMN13828714, PRJNA287430, WGS AANOEJ000000000.1, taxon 197. Matching digits occur within the assembly accession, not an assertion about taxon 1035318. |

A separate ignored-inclusive `HQ449642|HQ449663|AEL22197|JQ080897|JQ080890|AGE12068|AGE12062` search returned zero candidate lines across the same roots and no matches in parsed SOURCE.json metadata or history filenames. No exact target rows occur in raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. These negatives are bounded to the inspected sources and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, count, attestation and seed event agree with inspected evidence. The current YAML makes none of the potentially over-scoped functional claims considered above.

## Recommended Edits

None required.

For separately authorized enrichment, retain exact sequence accessions and their distinct roles in an appropriate maintained representation. Necessary seeder changes belong in `src/taxonmech/seed.py` with tests; functional evidence should respect sibling ownership and assay conditions. Do not infer a genome, registered deposit, A. baumannii equivalence, quantitative resistance, positive arsenite oxidation, or `REVIEWED` status from this review.

## Follow-up Checks

After an authorized source change, use the documented extraction/seeding workflow and `just verify-corpus`, then schema and exact-target strict validation. Read the actual TSV and regenerated fields.

Require authority-backed culture identity for strain/genome links. For functional curation, inspect the full 2015 paper and render its supplementary table to resolve the exact 18AAV row, units and conditions; distinguish PCR/sequence annotations from assays. Full-corpus reproduction and QC remain unrun.

## Additional Notes

The review skill, curator boundaries, checklist, repository guidance, relevant schema, history documentation and source-coverage rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The 2011 publisher figure was inspected from the original JPEG in scratch space. The 2015 publisher page exposes an abstract but identifies the full article as subscription content; no purchase or institutional access was attempted. Its public [supplementary DOCX](https://static-content.springer.com/esm/art%3A10.1007%2Fs11356-014-3840-5/MediaObjects/11356_2014_3840_MOESM1_ESM.docx) was unsupported by the web fetcher, then retrieved by a read-only request. ZIP/XML parsing exposed the caption and six embedded EMF images, not native table rows. The images were extracted only to scratch space and not interpreted; this limitation is not evidence of target absence from the supplement. A verbose XML diagnostic was truncated; no uninspected portion was used for a finding.

The target was byte-compared with its initial full read and remains unchanged. This new report is the only repository artifact of this target review. No YAML, inventories, generated products, histories, prior reports, Git/GitHub objects or Eukaryota records were modified.
