# YAML Record Review: Alloprevotella sp. oral taxon 473 str. F0040

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alloprevotella_sp_oral_taxon_473_str_f0040.yaml`
- Started UTC: 2026-10-06T14:52:11Z
- Finished UTC: 2026-10-06T14:54:45Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1035197`, label `Alloprevotella sp. oral taxon 473 str. F0040`, rank STRAIN, domain BACTERIA. The complete YAML was read before judging it and checked byte-for-byte unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED with twelve root-first ancestors, one GTDB mapping, three synonyms, one equivalent xref, genetic code 11, zero listed strains, four source attestations and one inline seed event. No nested genome links, nomenclature, definition, publication citations or causal graph are present. Only this new report is written.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alloprevotella_sp_oral_taxon_473_str_f0040.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/alloprevotella_sp_oral_taxon_473_str_f0040.yaml --out /private/tmp/af0040-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: pinned identity, all twelve ancestors, aliases, code, source counts, scope and seed provenance agree. This is not a focused corpus-reproduction validator.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- No curator-added ontology graph requires term validation. The product checker excludes taxonomy fields and delegates them to corpus reproduction.
- No separate target history artifact was found by the ignored-independent history filename search. Inline history passed schema validation; no external history validator was run against an invented artifact.
- The YAML has no DOI, PMID or quoted evidence. No additional record-specific citation validator is documented in the inspected commands.

## Identity and Grounding

Pinned backbone `data/raw/ncbitaxon_taxa.tsv:221920`, [live NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035197&retmode=xml), and [NCBI taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035197) agree on the strain, parent species `NCBITaxon:712469`, both Prevotella aliases and code 11. All twelve root-inclusive ancestor identifiers agree. No children, exact type-material row, merged-ID row or dropped row were found in their pinned structured tables.

The [legacy NCBI browser page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1035197), returned from a month-old crawl, displays no rank. Both live APIs and the pinned backbone supply STRAIN. Preserve this source/time discrepancy instead of changing the record to the cached browser value.

The [LPSN Alloprevotella page](https://lpsn.dsmz.de/genus/alloprevotella), record 518330, concerns the genus and lists A. rava and A. tannerae as its named children. It does not establish a species-name equivalence for F0040. No exact target or parent-name LPSN row was found in the inspected raw inventory. The [HOMD taxon page](https://homd.org/taxa/tax_description?otid=473), returned as taxonomy V4.2, calls HMT-473 unnamed and cultivated and lists F0040 as its type/reference strain. That combined label is not proof of nomenclatural type status for a valid species name. Its NCBI link is genus taxid 1283313, not this strain.

GTDB uses Bacteroidaceae for this genome while the carried NCBI lineage uses Prevotellaceae. These are source-specific classifications, not a reason to replace the NCBI chain locally. The species-versus-strain equivalence is the major finding below.

## Evidence

- Complete native NCBI rows `data/catalog/ncbi_names-0005.jsonl.gz:31386` through 31388 support the scientific name, the Prevotella homotypic synonym and the equivalent spelling with "strain". The NCBI attestation counts one NAME, not three aliases.
- `data/raw/gtdb_species.tsv:7970` and `data/raw/gtdb_mappings.tsv:1424` support six genomes in `GTDB:s__Alloprevotella_sp000318095`. Mapping line 16325 also links that cluster to taxid 1283315 with broadMatch. Six is a species-cluster count, not a count of F0040 genomes. The extraction owner at `src/taxonmech/extract.py:501` counts genome-to-species edges.
- `data/raw/gold_organisms.tsv:481` supports one ORGANISM assertion; `data/raw/madin_taxa.tsv:673` supports two TRAIT_ASSERTIONs. Neither aggregate establishes an experimental phenotype.
- `data/taxa/PATHS.tsv:14411`, `curation/seed_scope.tsv:26087` and `curation/legacy_page_paths.tsv:870` identify this record. The four-source scope reason and 2026-09-12 scope date agree with the 2026-09-13T17:54:04Z seed event.

Complete genome-source metadata were inspected for completeness, without treating source identifiers as interchangeable:

- `data/catalog/gtdb_genomes-0004.jsonl.gz:14410` identifies representative genome RS_GCF_000318095.2, strain F0040, taxid 1035197 and SAMN02436797 in the six-genome cluster. Representative status does not collapse strain and species identity.
- Current GenBank `data/catalog/ncbi_genbank-0000.jsonl.gz:8017` and RefSeq `data/catalog/ncbi_refseq-0000.jsonl.gz:6883` identify GCA_000318095.2 and GCF_000318095.2, 89 contigs, 24 scaffolds and 2,553,017 bp. Their annotation dates and gene counts differ; these are not extra biological genomes.
- Historical GenBank row `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:3036` and RefSeq row `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:2417` preserve the replaced .1 assemblies, 90 contigs, 25 scaffolds and 2,553,588 bp. The not-live date is 2015-10-19.
- `data/bvbrc/bvbrc-0000.jsonl.gz:3319` identifies PATRIC 1035197.3 and retains GCA_000318095.1, PRJNA67205, SAMN02436797 and AMEK00000000. Its collection field is blank and strain is bare F0040. Do not silently upgrade this source's accession version.
- GOLD's complete chain is `Go0010898 -> Gp0010898 -> Ga0016258`, inspected at `data/gold/organisms.jsonl.gz:9568`, `data/gold/projects.jsonl.gz:9433` and `data/gold/analyses.jsonl.gz:9787`. It identifies F0040, exact taxid 1035197, BEI HM-756, IMG 2537561949, unversioned GCA_000318095, PRJNA67205 and SAMN02436797. The analysis organism field is empty, not conflicting with its explicit project chain.

The [live NCBI assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000318095.2/dataset_report) confirms current GCA/GCF .2 accessions, size, strain, taxid, project, sample and AMEK01. Its ANI result is Inconclusive / below_threshold_mismatch, with no submitted-species type assembly and a best listed match to Ihuprevotella massiliensis at 87.51%. This does not justify relabeling F0040 as that species. The report retains the uncertainty; assembly annotation is not experimental phenotype evidence.

Complete [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN02436797&retmode=xml) identifies F0040, human host and oral-cavity source, with no culture-collection attribute. The [BioProject page](https://www.ncbi.nlm.nih.gov/bioproject/67205) independently links its monoisolate project to the .2 assembly, AMEK, BioSample, GOLD Gp0010898 and IMG 2537561949. These source/sample/project identities remain distinct.

## Completeness

Ignored-inclusive searches found no F0040 BacDive or StrainInfo candidate. Similar F040 / F040-2G hits belong to Pseudomonas aeruginosa or Aliarcobacter cryaerophilus and were rejected after complete native-row inspection. No exact BacDive row and no descendants explain `strain_count: 0` under `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`. This does not mean that no physical culture or genome exists.

No exact target rows occur in the inspected LPSN, MediaDive or BactoTraits transformed tables. The accession-expanded search found no exact SAMN02436797 ATB entry, including ignored/compressed sources. No unsupported ATB, species-type or similar-name strain link should be supplied to fill an empty slot.

GOLD's BEI HM-756 is a source assertion, but an ignored-independent search found no BEI authority in `src/taxonmech/data/cafi_acronyms.json`. The existing normalizer returns empty for BEI HM-756, HM-756 and F0040. Current NCBI assembly-summary, GTDB and BV-BRC fields supply only bare F0040. Thus no eligible existing whole-deposit key was established, and absent nested genome links are not independently classified as a required-representation defect under the current contract.

Two attempted BEI product routes were unavailable, and the bounded search did not produce an inspected BEI authority page. Authority-level confirmation and registry representation remain unresolved enrichment work, not evidence that the deposit does not exist. Preserve the explicit GOLD chain for that follow-up.

The structured iModulonDB dataset adapter initially failed because of network resolution in the sandbox, then succeeded with approved public network access and returned 28 datasets. No Alloprevotella or Prevotella dataset matched. It is not applicable here; absence is not negative biological evidence. Optional definition, phenotype and causal-graph fields can remain empty.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species concept is promoted to exact strain identity.** `GTDB:s__Alloprevotella_sp000318095` is emitted as an equivalent xref and its species label as an EXACT_SYNONYM on strain taxid 1035197. Native metadata support genome membership and representative status in a six-genome species cluster, not identity of that cluster with F0040. Parent taxid 712469 remains a distinct species concept. This violates `src/taxonmech/schema/taxonmech.yaml:180`. Maintained owner: rank-insensitive promotion at `src/taxonmech/seed.py:449`, with regression coverage in `tests/test_seed.py`; the upstream kg-microbe closeMatch producer also needs rank- and direction-aware review. Mapping, synonym and xref manifestations are one finding.

Blockers: None found. Minor findings: None found. Cached browser rank, family classification, historical assembly version and inconclusive ANI are preserved as scoped source qualifications rather than silently reconciled.

## Recommended Edits

1. Make GTDB identity promotion in `src/taxonmech/seed.py` rank-aware. Preserve supported classification and cluster counts without an equivalent species xref or exact species synonym on a strain.
2. Review upstream kg-microbe mapping rank and direction rather than guessing a replacement broad/narrow predicate. Preserve the NCBI lineage.
3. Add regression coverage in `tests/test_seed.py` for representative genomes of unnamed species, retaining genuine species-level equivalence. Regenerate from maintained inputs after an authorized fix; do not patch this generated YAML or raw inventories.
4. For later genome enrichment, resolve BEI HM-756 at its authority and establish supported registry/inventory identity. Registry changes belong in the maintained source/import process for `src/taxonmech/data/cafi_acronyms.json`, not a permissive name-based bypass in `src/taxonmech/genome_sources.py`.
5. Retain GOLD's unversioned accession, BV-BRC's historical .1 and NCBI/GTDB's current .2 as source-specific assertions. Do not conflate project, sample, IMG, PATRIC and assembly identities.

## Follow-up Checks

- After an authorized fix, run `uv run pytest tests/test_seed.py` and this target's schema and strict commands.
- Confirm removal of the unsupported species synonym/xref while retaining NCBI identity, twelve ancestors, two NCBI aliases, code 11, four attestations and source-scoped classification/count.
- After regeneration, run actual full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`. Manual comparisons do not replace them.
- Retry the GTDB page and record its release before updating classification. Its browser route was unavailable; pinned native metadata support this bounded review.
- Resolve BEI authority identity before introducing a culture/genome join. Do not use HOMD's genus link, taxon-wide genome list or its combined type/reference label as exact-strain evidence.
- Recheck assembly versions and unresolved taxonomy evidence before analytical reuse. Phenotype or mechanism assertions require separately inspected strain-specific evidence.

## Additional Notes

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, F0040/F040 separator variants, names and slug produced 31 candidates. Expansion using observed assemblies, BioSample, project, WGS, GOLD, IMG, PATRIC and HM-756 identifiers produced twelve rows, adding two cluster rows. All 33 distinct candidates were read in full with lossless decoding. Separate exact scans covered lineage/status, cluster mappings, LPSN and scope. Five SOURCE.json files were searched structurally and history filenames separately checked. Absence findings are bounded to these sources and include ignored files.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. NCBI APIs/browser, BioProject, LPSN genus and HOMD taxon page were inspected. The HOMD genome-detail page timed out; its search snippet was not used as evidence. Two BEI routes and the GTDB tree route were unavailable.

No YAML/code/generated-page edits, history events, review-status promotions, paid research, outbound contact or Git/GitHub mutations were performed. Eukaryota reviews were not reopened.

