# YAML Record Review: Advenella sp. SLODRJ-01

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/advenella_sp_slodrj_01.yaml`
- Started UTC: 2026-10-10T02:19:28Z
- Finished UTC: 2026-10-10T02:22:11Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037397` denotes Advenella sp. SLODRJ-01, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2685285`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. It asserts no formal nomenclature, culture deposit, genome, phenotype, mechanism or causal graph.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/advenella_sp_slodrj_01.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/advenella_sp_slodrj_01.yaml --out /private/tmp/taxonmech-advenella-slodrj01-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified the identity, complete lineage, code, empty synonym columns, own source inventories, unique index/scope resolution, attestation and exact seed reason. Complete backbone scanning found no immediate child. Own type-material, merged-ID and dropped-record inventories had no rows.
- Live EFetch and Datasets taxonomy responses and the single exact-taxonomy nucleotide record were inspected. The native NCBI name row was read in full. PubMed and publisher-deposited abstract metadata and relevant methods, table and results of a primary open-access paper were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, source replay, rendering and publication gates. The graph ID/label gate `just validate-products` is inapplicable without a graph. Focused checks do not establish corpus reproduction.
- The target's NCBI browser page and both sequence-linked DOI landing pages failed through the web reader. Taxonomy APIs, PubMed and Crossref supplied the stated checks; the two sequence-linked papers' full texts were not read. The additional Frontiers primary paper was accessible directly; its supplement was not inspected.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222740`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037397&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037397) agree on the target identity, rank and lineage; EFetch also confirms parent 2685285 and code 11.

The complete root-first chain matches the backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Alcaligenaceae, Advenella and unclassified Advenella. EFetch confirms the chain below root; Datasets includes root 1. Retain the unclassified `NO_RANK` parent, not a shortened genus-only parent.

The complete native name row `data/catalog/ncbi_names-0005.jsonl.gz:32371` is a scientific name with an empty unique-name qualifier. EFetch supplies no alternate names. NCBI's species rank for this strain-labelled taxon is not a validly published species name or proof of equivalence to Advenella kashmirensis.

`EXACT` denotes grounding to this identifier. The one-NAME attestation correctly reflects the 2026-09-13 NCBI snapshot rather than an experimental count. The seed timestamp and scope reason agree with the maintained inventory.

## Evidence

The live query `txid1037397[Organism:exp]` returned one record: [JF815694.2](https://www.ncbi.nlm.nih.gov/nuccore/JF815694.2), a 1,209-base partial 16S rRNA sequence. Its source names SLODRJ-01, taxon 1037397, contaminated soil and Spain. Declared and actual lengths agree and its sequence alphabet is A/C/G/T. The annotation explicitly says version .2 replaced .1 on 2019-01-17; preserve .2 when citing the current sequence.

This marker is not a genome, and its existence does not require inventing a culture-deposit or assembly join. The Datasets taxonomy response omits an assembly-count field, which is not an explicit zero-assembly result.

The sequence cites DOI [10.1002/clen.201300247](https://doi.org/10.1002/clen.201300247). Publisher-deposited Crossref metadata verifies the title and distinguishes 2013 online publication from the 2014 print issue. Its abstract attributes demonstrated phenanthrene degradation to Pseudomonas xanthomarina under the studied conditions, not automatically to every isolate in the contaminated-soil collection.

The second reference, [PMID:28011373](https://pubmed.ncbi.nlm.nih.gov/28011373/), DOI `10.1016/j.jenvman.2016.12.020`, describes a diuron-degrading consortium containing Advenella sp. JRO, Arthrobacter sulfonivorans and Variovorax soli. The abstract explicitly distinguishes consortium mineralization from the failure of each strain alone to mineralize diuron in the specified medium. It does not justify assigning the consortium's mineralization outcome to SLODRJ-01 alone.

Table 2 of [the primary 2019 Frontiers paper](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.02588/full), DOI `10.3389/fmicb.2019.02588`, explicitly associates JRO with unversioned JF815694. This supports an accession-linked literature designation, not a new formal taxonomic synonym. Its 99% partial-marker match to A. kashmirensis WT001 is not exact strain identity or a species reassignment. The inspected methods and results distinguish six tested isolates from the two with significant fluorene/pyrene degradation, Achromobacter 2BC8 and Stenotrophomonas JR62; JRO must not inherit their outcomes. These observations are bounded to the reported assays, not universal negative phenotypes.

No biological-activity assertion is present in the YAML. These papers provide follow-up context, not evidence of a defect in the current taxonomy-only representation.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded taxon ID, label, slug and SLODRJ-01 variants. Exactly three lines matched: the backbone, scope and native NCBI name row.

Complete structured scans of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no own-taxonomy row. Follow-up ignored-inclusive searches across the same roots found no JF815694, PMID 28011373, either sequence-linked DOI, or exact Advenella sp. JRO phrase. These are bounded repository results, not claims of global absence.

Five independently enumerated SOURCE.json files were parsed, with no target match. Gitignore-independent filename enumeration found the unique YAML and no prior target report; history filenames had no target match.

`strain_count: 0` measures inventory coverage, not absence of the biological isolate or of sequence evidence. Optional nomenclature, mappings, literature aliases, deposits, definitions and graphs need not be invented to fill empty slots. iModulonDB is not applicable to the taxonomy/name assertions or the partial ribosomal marker here.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertion scope. Identity and complete lineage agree with pinned and live taxonomy. The record does not inflate a marker into a genome, marker similarity into identity, or consortium activity into a single-strain phenotype.

## Recommended Edits

None required. Keep the generated YAML, seed status and curation history unchanged.

If separately authorized, literature enrichment should preserve the JRO/JF815694/SLODRJ-01 source chain and exact experimental scope. Maintained source inputs or a supported extraction/harmonization extension would own such enrichment; do not patch this generated YAML or introduce an unsupported exact synonym or genome link.

## Follow-up Checks

For future phenotype curation, inspect the full diuron paper and relevant supplements, resolve the accession-linked designation, and retain individual-versus-consortium and tested-condition distinctions. Do not replace the NCBI label using the 99% partial-marker match.

If maintained inputs change, rerun the documented canary, schema/strict/history checks and full-corpus reproduction/QC gates. The current NCBI-only record requires no curator correction.

## Additional Notes

- YAML SHA-256: `b974ddf0ef5d9b3d95a38280f2b87f6194d53bef94172ad0ff7809fa2eb31805`.
- `data/taxa/PATHS.tsv:15291` and `curation/seed_scope.tsv:322962` uniquely resolve the target; the seed event is 2026-09-13T17:54:04Z.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No tracked record, source, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
