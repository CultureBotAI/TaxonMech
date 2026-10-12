# YAML Record Review: uncultured marine bacterium D009

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d009.yaml`
- Started UTC: 2026-10-09T05:33:42Z
- Finished UTC: 2026-10-09T05:38:43Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:103664`: species rank, Bacteria, parent 150608, five root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has one NCBITAXON name attestation and one 2026-09-13T17:54:04Z seed event. Zero represented BacDive strains is not an assertion that all organisms in the environmental community are unculturable.

Ignored-inclusive filename inventory under `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved the YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genome links, phenotypes and graphs are unasserted. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d009.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d009.yaml --out /private/tmp/taxonmech-marine-d009-review-strict.tsv`: passed, one file and zero errors; the full TSV was header-only.
- Structured comparisons matched identity, all ancestors, attestation, PATHS, scope and seed wording. Exact scans covered seven supplementary raw inventories, type material, merged IDs and dropped taxa.
- Marker consistency passed: declared/actual length 559, submitted rRNA transcription equals DNA, and no non-ACGT symbols. This is annotation consistency, not independent alignment or species inference.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift or publication builds. Focused checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive content and filename searches found no separate target history artifact in the stated roots. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103664&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103664) agree with ID, label, rank and ancestry. EFetch confirms parent and code 11; Datasets includes root. The five ancestors are root, cellular organisms, Bacteria, environmental samples and marine bacteria D ensemble.

Live taxonomy supplies no other names; pinned synonym fields are empty. Exact scans found no type-material, merged-ID or dropped row and no backbone children. NCBI species rank does not establish a formally named species or cultured isolate. Acinetobacter sp. D009 is a separate taxon, not a supported replacement identity.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:18529`, `data/catalog/ncbi_names-0000.jsonl.gz:38545`, `data/taxa/PATHS.tsv:15059` and `curation/seed_scope.tsv:144173`. Snapshot 2026-09-13 and scope wording match the attestation and seed event. The `NAME` count is not a strain, genome or experimental count. Exact raw scans found no target row in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits.

Exact Nuccore query `txid103664[Organism:noexp]` returned UID 5882266 only. Complete [AF177551.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177551.1) XML was read, including references, features and sequence. This 559-base partial 16S carries clone D009, taxon 103664, an environmental-sample flag and a surface-associated marine context. It supplies no strain deposit, genome or collection locality. References identify Dang and Lovell and a 13-AUG-1999 University of South Carolina submission; that submission address is not a collection location.

Complete [PMID 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/) abstract/metadata verifies [DOI 10.1128/AEM.66.2.467-475.2000](https://doi.org/10.1128/AEM.66.2.467-475.2000) and PMC91850. The study examined early marine surface colonization using cultivation-independent methods. Its community-level phylogenetic results are not a D009-specific reclassification. PMC returned a browser challenge and Europe PMC returned HTTP 403; full text and clone-specific tables were not inspected in this review.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional enrichment would require clone-specific source text. No additional target deposit or genome relationship was established.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded 103664, label/slug and D009 with optional hyphen, space or underscore. Expansion added AF177551 and UID 5882266. Both returned the same 33 rows, all read completely in native form with common fields and lossless differences. Five SOURCE.json files were separately parsed in full for both term sets; history filenames were independently inventoried.

Three rows concern the own taxon. The thirty excluded rows include:

- BacDive 103664 is Rhodococcus sp. ST030089, taxon 194249. SOURCE.json mentions 103664 as a requested BacDive ID, not this NCBI taxon.
- CIP 103664 is Micrococcus luteus, taxon 1270, BacDive 135321, StrainInfo SI-ID 42646 / SI-DP 152801 and GOLD Go0215641. Native StrainInfo lists ATCC 49732 and ACM 4755; the projected links consistently concern Micrococcus, not the marine clone.
- StrainInfo SI-DP 103664 denotes ATCC 25115, Mycobacterium intracellulare, taxon 1767, in SI-ID 38362. The equal integer does not imply taxon identity.
- IMI 103664 belongs to the fungal SI-ID 176110 group, labelled Xepicula leucotricha at strain level. Its CBS 131.64 sequence links and differently named deposits do not establish any relationship to marine D009. This source read is not a new Eukaryota record review or a verdict on that group's internal equivalences.
- Acinetobacter sp. D009, taxon 3138069, has GCA/GCF_038562025.1, SAMN40861309, chromosome CP151886 and BV-BRC entries 3138069.3, .4 and .5. GTDB calls its genome Acinetobacter pittii. Neither placement is evidence for reclassifying taxon 103664.
- Escherichia coli d009-48.1 is GCA_014082045.1 / SAMN11319305. Salmonella Kentucky strain 103664 is GCA_010957415.1 / SAMN08100325. Klebsiella variicola isolate k_variicola_5 has assembly name KLP-ELB-HUB-103664, GCA/GCF_901521545.1 / SAMEA5605372. These are strain or assembly-name collisions.
- GCA_977870805.1 is a Gammaproteobacteria metagenome-derived genome whose isolate UUID contains d009. GTDB's GCA_046328925.1, an Anaerolineales genome classified as Villigracilis sp046328925, has contig N50 103664. Neither match is in the target taxon field.

The broad bacterial D009 Nuccore query returned 653 hits, with the first 100 IDs returned; these were not exhaustively audited. Narrowing to bacterial 16S titles returned four records, all fully inspected at ESummary metadata level: the own marker, [PX063573.1](https://www.ncbi.nlm.nih.gov/nuccore/PX063573.1), Phreatobacter NEC-D009 from Japanese soil in 2025; [GQ413547.1](https://www.ncbi.nlm.nih.gov/nuccore/GQ413547.1), coral-community clone 1FT1c8_D009 from Bolinao, Philippines; and [AY985767.1](https://www.ncbi.nlm.nih.gov/nuccore/AY985767.1), a 1,365-base D009 clone from human stool. None supplies an identity link to AF177551.1. These metadata reads are not full sequence comparisons.

Exact Assembly search returned zero with missing-phrase/no-items diagnostics, not proof of global genome absence. PubMed accession search returned zero despite the explicit GenBank PMID. The broad D009/bacteria literature query returned [PMID 18677737](https://pubmed.ncbi.nlm.nih.gov/18677737/), an endohexosaminidase-mutant glycosylation paper. Its complete returned metadata contains no abstract and establishes no target identity link; its full text was not inspected. Neither query proves literature absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted, and no applicable strain/dataset was established. Optional empty fields are not automatically defects. All absence conclusions are bounded to stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. The record agrees with pinned and live taxonomy and does not conflate clone names, culture identifiers, source-specific numeric IDs, genome statistics or assembly names.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Never join on bare D009 or 103664 without namespace and field meaning.

## Follow-up Checks

Optional enrichment requires inspected D009-specific results tied to AF177551.1. Do not convert paper-wide colonization or phylogenetic observations into clone-specific traits. Deposit and genome links require explicit relationships. No independent alignment, genome comparison, experimental reanalysis or PDF/figure visual verification was performed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:103664`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Independent review followed the local skill and checklist. Full YAML, own source rows, all 33 local candidates, live taxonomy, complete own marker, four sequence summaries, the linked paper's abstract/metadata and the namesake paper's metadata were inspected. No neighboring verdict was inherited.

Before/after YAML SHA-256: `12ebc157894b8ab0fab72d10a6e7e7511c3f4474704ee7e318c0f9369d5c5512`. Only this new report was written for this target. YAML, sources, status, history, pages, Eukaryota, GitHub objects and worktrees were untouched.
