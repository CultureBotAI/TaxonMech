# YAML Record Review: Dyadobacter sp. MSK121

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/dyadobacter_sp_msk121.yaml`
- Started UTC: 2026-10-06T20:18:49Z
- Finished UTC: 2026-10-06T20:21:55Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035290`, Dyadobacter sp. MSK121. It has species rank, BACTERIA domain, parent unclassified Dyadobacter (`NCBITaxon:2625061`), twelve root-first ancestors, genetic code 11, EXACT grounding, SEEDED lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. No synonyms, nomenclature, mappings, genome links, phenotypes or causal graph are asserted.

MSK121 is a strain designation, not a globally unique identity. This target is not Corynebacterium accolens MSK121. Generated YAML is read-only; future changes belong to maintained source inputs, extraction, scope or seeding.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/dyadobacter_sp_msk121.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/dyadobacter_sp_msk121.yaml --out /private/tmp/d121-strict.tsv`: exit 0, one record, zero errors. The actual TSV was read and contains only its header.
- Bounded comparisons checked every lineage field, inventories, path lock, scope, attestation and seed event. These are not a target-level reproduction validator.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, full provenance, original-taxdump and history gates. Reproduction has no target selector; `--max-diffs` limits diagnostics only. `just validate-products` is not applicable because no curator-added graph nodes exist.
- Before external follow-up, the local `culturebotai-claw` iModulonDB dataset adapter exited 0. All 28 rows were read, with no Dyadobacter coverage. No component query applied, and absent coverage is not biological evidence.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221991`, path lock `data/taxa/PATHS.tsv:14482`, scope `curation/seed_scope.tsv:322265` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31467` agree on the exact taxon. Exact type-material, merged-ID and dropped-record scans found no target entry. The pinned backbone has no descendants.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035290&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035290) confirm active identity, label, species rank, parent and genetic code. Every ancestor agrees: root, cellular organisms, Bacteria, Pseudomonadati, FCB group, Bacteroidota/Chlorobiota group, Bacteroidota, Cytophagia, Cytophagales, Spirosomataceae, Dyadobacter and unclassified Dyadobacter. Datasets confirms the root ID omitted from the XML lineage display.

NCBI species rank makes this strain-labelled taxon eligible under repository scope rules, but does not establish a formally described species or type strain. EXACT grounding denotes the exact NCBI target, not equivalence to another Dyadobacter species or another organism named MSK121. The inspected XML supplies no alternate name, consistent with the pinned name catalog and empty synonyms.

## Evidence

The NCBITAXON attestation correctly counts one pinned name and states the 2026-09-13 snapshot. Exact inventory comparisons found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive strains; it does not contradict MSK121 appearing as a strain qualifier on a nucleotide submission.

An exact nonexpanded nucleotide query returned one sequence, [JF807996.1](https://www.ncbi.nlm.nih.gov/nuccore/JF807996.1), UID 333826804. Full GenBank metadata were read, excluding bases. It is a 1,288-base partial 16S rRNA marker with organism Dyadobacter sp. MSK121, strain MSK121 and taxon xref 1035290. The source is Jeju Island soil, collected 17-Jan-2011, with direct submission on 13-Apr-2011 by Park and Kim at Korea University.

The accession labels its study reference, A microbial cell retrieved from Jeju island soil, as unpublished and supplies no DOI or PMID. The submitter reports chimera screening with mothur 1.10.0; that is submission metadata, not an independently repeated sequence-quality test. No phylogenetic reconstruction, chimera screening, experimental phenotype or literature conclusion is inferred here. This marker is not a genome assembly, culture-collection deposit or proof of a pure culture.

An exact nonexpanded Assembly ESearch returned zero hits with a phrases-not-found warning. An independent [NCBI Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035290/dataset_report) succeeded with an empty object. These are bounded query results, not a claim that no genome could exist in any resource.

Scope and seed-event wording agree. The seed timestamp 2026-09-13T17:54:04Z matches the newest raw/ATB/StrainInfo manifest extraction time used by `_seed_timestamp` in `src/taxonmech/seed.py:139`. Lifecycle remains SEEDED.

## Completeness

Ignored-inclusive compressed-content searches used `rg --no-ignore --hidden -n -z -i` for identifier, MSK121 with optional separator, and full slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The MSK121 search also covers the full record label. All 59 candidate rows were read in full native form: 47 JSON rows and 12 TSV rows, including nested content. Only backbone, scientific name and scope concern this target.

The 56 exclusions were established from native identity fields:

- Four Corynebacterium accolens rows use the same bare strain name MSK121: BV-BRC 38284.63, the GCA/GCF_030229025.1 pair and its GTDB record. They identify taxon 38284 and BioSample SAMN35346736; the GTDB metadata describe a Botswana nasopharyngeal sample. This is not the Jeju soil Dyadobacter.
- Seven Klebsiella pneumoniae rows concern literal strain designation 1035290, taxon 573, assembly GCA/GCF_003687865.1, BioSample SAMN10252254 and GOLD chain Go0508769/Gp0393482/Ga0368851. A strain number equal to the target's NCBI local ID is not identity evidence.
- Thirty-one Escherichia coli rows concern BioSamples SAMN10352900, SAMN10352901, SAMN10352902, SAMN10352905, SAMN10352906, SAMN10352907, SAMN10352908 and SAMN10352909. These include current/historical assemblies, BV-BRC and ATB records; versions are not merged or transferred.
- Four Rhodococcus sp. WS1 rows concern BioSample SAMN10352903 and GCA/GCF_003797745.1, including a GTDB Rhodococcus_F erythropolis assignment.
- Three Streptomyces sp. FXJ1.4098 rows contain BioProject PRJNA1035290, taxon 3090669 and GCA_033542285.1.
- Three Amycolatopsis sp. YIM 10 rows match the numeric genome size 10352908, not a taxon identifier.
- Two Mycobacterium tuberculosis rows concern run ERR1035290, BV-BRC 1773.18305 and ATB sample SAMEA3558823/analysis ERZ9334423.
- One Campylobacter jejuni row contains assembly GCA_010352905.1.
- One ATB Elizabethkingia anophelis row matches digits inside its SeqKit checksum, with sample SAMEA115411215 and analysis ERZ26934636.

These are name or numeric collisions, not missing target relationships. Neither source taxonomy differences for these other organisms nor assembly quality/status metadata supplies evidence for MSK121.

An additional ignored-inclusive JF807996 search found no rows in the same ten roots. All five SOURCE.json files and history filenames were separately inspected for identity and accession queries, with no additional target evidence or external history. Ignored-inclusive report-filename discovery found no earlier report for this stem.

No supported missing nomenclature entry, attestation, deposit or strain-genome join was found within these bounds. Marker citations, habitat annotation and causal graphs are optional for this seeded NCBI-only record; empty optional slots are appropriate. No broad literature-absence claim is made from the unpublished submission.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, name coverage, attestation, strain count and seed event agree with the inspected sources. Target validation and bounded comparisons do not prove full-corpus reproduction or biological characterization.

## Recommended Edits

None required. Preserve the exact Dyadobacter identity and do not join MSK121 to Corynebacterium genomes by bare strain name, or 1035290 to Klebsiella strains and unrelated project/sample identifiers by digits.

Any future enrichment belongs to maintained source acquisition/projection or an explicitly modeled curator overlay, followed by `src/taxonmech/seed.py`. A deposit or genome association must have an explicit source identity chain. The 16S marker must remain outside genome counts. Do not hand-edit generated YAML or promote lifecycle through this report.

## Follow-up Checks

No immediate corrective check is required. After authorized maintained-input changes, rerun the two target validators, then full `just verify-corpus` and `just qc`. Before adding physiological or ecological claims, inspect primary evidence at this strain's scope; submission origin alone does not establish general habitat preference or a phenotype.

## Additional Notes

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The target was reread byte-for-byte unchanged. Only this new report was written for this target; records, history, lifecycle, generated site and Git/GitHub state were not changed. Eukaryota remained untouched.
