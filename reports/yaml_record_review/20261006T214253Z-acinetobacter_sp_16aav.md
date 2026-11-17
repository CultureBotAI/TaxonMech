# YAML Record Review: Acinetobacter sp. 16AAV

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_16aav.yaml`
- Started UTC: 2026-10-06T21:38:25Z
- Finished UTC: 2026-10-06T21:42:53Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035317` is Acinetobacter sp. 16AAV, `SPECIES` in `BACTERIA`, parent `NCBITaxon:196816`. It asserts ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried strains, one NCBITAXON NAME attestation, and a seed event.

No synonyms, nomenclature, taxonomy mappings, strains, genomes, phenotypes, citations or causal graphs are asserted. Generated fields are read-only. Future corrections belong in maintained extraction/seeding code, upstream transforms or scope decisions, not the YAML or generated pages.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/acinetobacter_sp_16aav.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/acinetobacter_sp_16aav.yaml --out /private/tmp/a16-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and is header-only.
- Structured comparisons read the full backbone row, every ancestor, direct children, seven non-NCBI inventories, PATHS, scope, attestation and event text. All compared fields agree.
- Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive searches, full native candidate reads, parsing of five SOURCE.json files and independent history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0 with network access; all 28 rows inspected before external follow-ups. `a_baumannii/precise139` is not 16AAV. No exact organism/dataset match: iModulonDB is not applicable, not negative biological evidence.
- Live NCBI taxonomy XML/JSON, exact-organism Assembly/nuccore searches, full metadata for both returned sequences excluding nucleotide/protein bases, and an independent Datasets genome query succeeded.
- All ten unknown-labeled ATB numeric BioSample candidates were fetched and read in full at NCBI.
- The cited publication's PubMed metadata and abstract were read, then relevant publisher text and Figure 1 were inspected. The original publisher JPEG was downloaded to scratch space and viewed at original resolution.
- Not checked: full-corpus `just verify-corpus`, QC/history/provenance gates, full tests, page rendering, original-taxdump regeneration, source hashes or publication supplementary files. Manual comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone `data/raw/ncbitaxon_taxa.tsv:222010`, scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31485`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035317&retmode=xml), and [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035317) agree on exact identity, rank, parent, bacterial placement and code.

Every ancestor ID, label and normalized rank agrees: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Moraxellales; Moraxellaceae; Acinetobacter; unclassified Acinetobacter. Order 2887326, family 468 and genus 469 agree. Datasets includes root ID 1, which EFetch omits from its displayed lineage.

Pinned synonym fields and live alternate-name content are empty; the backbone has no direct children. Species rank does not establish a formal binomial or type strain. 16AAV is not 18AAV, A. baumannii, or another Acinetobacter strain.

## Evidence

- The NCBITAXON attestation correctly represents one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14501` maps the identifier to this stem; `curation/seed_scope.tsv:322282` supplies the exact scope reason in the event.
- Raw, ATB and StrainInfo extraction timestamps were parsed as 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the seed timestamp under the inspected `_seed_timestamp` rule. This is source provenance, not human sign-off.
- Exact nuccore search returned UID 338163883, [HQ449641.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449641.1), a 636 bp partial 16S rRNA gene, and UID 342316601, [HQ449662.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449662.1), an 850 bp partial aoxB coding sequence annotated as arsenite oxidase large subunit. The latter CDS names protein AEL22196.1 and translation table 11. Both source features explicitly name strain 16AAV, taxon 1035317, arsenic-contaminated sediment from Sainte Marie aux Mines, and France; both were submitted 28-Oct-2010 from Universite de Strasbourg. These are gene sequences, not genomes or culture deposits.
- Both sequences cite [Heinrich-Salmeron et al., AEM 77(13):4685-4692 (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), verified as PMID 21571879 and PMCID PMC3127681. Publisher Figure 1 explicitly labels 16AAV Acinetobacter sp. HQ449641. It is bold/underlined among the study's aoxB-PCR-positive isolates, coloured for group II, without the circle used for demonstrated arsenite oxidation. The text reports positive activity under the tested conditions only among Pseudomonas, Bacillus and Bosea isolates. Thus gene detection must not be promoted to a measured positive oxidation phenotype for 16AAV; non-detection under those conditions is not universal incapacity.
- Exact-organism Assembly searching returned count 0 with a no-items/phrase warning. The independent [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035317/dataset_report) returned an empty object. These bounded queries do not prove global genome absence.
- Full [NCBI BioSample XML for SAMN10353170 through SAMN10353179](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353179%2C10353178%2C10353177%2C10353176%2C10353175%2C10353174%2C10353173%2C10353172%2C10353171%2C10353170&retmode=xml) describes human-associated Chinese samples collected 2018-07-11, taxon 1869227 (bacterium), project PRJNA503135. Their sample names in accession order are FC1944, FC1194, FC1701, FC1711, FC1853, FC1854, FC1863, FC2133, FC2144 and FC2223. None names 16AAV or taxon 1035317; their source context differs from the French sediment isolate.

## Completeness

The seeded identity is complete enough. Optional sequence, habitat or functional evidence is not a missing required field. Phenotypes belong in sibling resources under the repository's curation rules. `strain_count: 0` counts inventoried BacDive entries, not every biological isolate; a GenBank strain qualifier does not establish a registered culture deposit.

The source search used `rg --no-ignore --hidden -n -z -i` with `1035317|16[-_ ]?AAV\b|acinetobacter_sp_16aav` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files were parsed completely, and history filenames were searched independently.

All sixteen candidate lines were inspected losslessly: two JSON objects and fourteen TSV rows. Three are exact backbone, scientific-name and scope entries. Thirteen do not supply target evidence:

| Candidates | Why excluded |
| --- | --- |
| Two M. tuberculosis entries | BV-BRC 1773.18324 and ATB SAMEA3558850/ERZ9334487 refer to run ERR1035317, not this TaxID. ATB retains a scientific name of M. tuberculosis but current Sylph unknown/SYLPH_RESULTS_FAIL; neither label supplies an Acinetobacter identity. |
| Ten unknown ATB entries | SAMN10353170 through SAMN10353179 are NOT_PROCESSED, with no FASTA, run or assembly accession. The authority records resolve them to the distinct human-associated study described above. |
| One Salmonella entry | SAMN35669641, SRR28997780, ERZ26497443 is S. enterica serovar Typhimurium, with S. enterica Sylph classification. The target digits occur within the SeqKit sum, not a taxonomic assertion. |

A separate ignored-inclusive `HQ449641|HQ449662|AEL22196` search returned zero lines across the same roots and no matches in parsed SOURCE.json metadata or history filenames. No exact target rows occur in raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. These negatives are bounded to the inspected sources and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, count, attestation and seed event agree with inspected evidence. The current record does not make the potentially over-scoped arsenite-oxidation claim.

## Recommended Edits

None required.

For separately authorized enrichment, preserve both sequence accessions and their narrow roles in an appropriate maintained representation. Any necessary seeder changes belong in `src/taxonmech/seed.py` with tests; functional evidence should respect sibling ownership and assay conditions. Do not infer a genome, registered deposit, A. baumannii equivalence, experimentally positive oxidation, or `REVIEWED` status from this review.

## Follow-up Checks

After an authorized source change, use the documented extraction/seeding workflow and `just verify-corpus`, then schema and exact-target strict validation. Read the actual TSV and regenerated fields.

Require explicit authority-backed culture identity for strain/genome links. For any functional curation, inspect the relevant supplementary assay data and experimental conditions; distinguish an aoxB sequence from demonstrated oxidation. Full-corpus reproduction and QC remain unrun.

## Additional Notes

The review skill, curator boundaries, checklist, repository guidance, relevant schema, history documentation and source-coverage rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

PMC web access returned a browser check, and its EUtils response supplied metadata without usable body passages. A public PDF mirror timed out. Publisher HTML and the original Figure 1 JPEG were accessible and supply the inspected primary text/visual evidence. This is a bounded identity/assay-context inspection, not a full-paper or supplementary-data audit.

The target was byte-compared with its initial full read and remains unchanged. This new report is the only repository artifact of this target review; the figure is in scratch space. No YAML, inventories, generated products, histories, prior reports, Git/GitHub objects or Eukaryota records were modified.
