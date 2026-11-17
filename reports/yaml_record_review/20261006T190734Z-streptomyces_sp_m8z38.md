# YAML Record Review: Streptomyces sp. M8Z38

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_m8z38.yaml`
- Started UTC: 2026-10-06T19:05:29Z
- Finished UTC: 2026-10-06T19:07:34Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035268`, Streptomyces sp. M8Z38, species-rank Bacteria placeholder, parent `NCBITaxon:2593676`, genetic code 11 and ten root-first ancestors. It stores `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, phenotypes or causal edges are asserted.

Maintained scope, acquisition/extraction and `src/taxonmech/seed.py` own future corrections; this generated YAML is not a curation input.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_sp_m8z38.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptomyces_sp_m8z38.yaml --out /private/tmp/mz38-strict.tsv`: exit 0, one record, zero errors. The actual diagnostic TSV was read and was header-only.
- Bounded manual comparisons matched complete pinned identity, lineage, path lock, scope, attestation and seed history. They are not a focused reproduction validator.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, provenance and corpus-wide history gates. The reproduction script has no target selector; `--max-diffs` only limits output.
- Not applicable: `just validate-products` for added graph nodes; none exist in this record. NCBITaxon references were checked at pinned and live authorities.
- Inline history passed target validation and matched scope. Ignored-inclusive content and history-filename searches found no target-specific external history entry.
- The local `kg-microbe-sources imodulondb datasets` adapter ran before web follow-up. All 28 rows were inspected. The covered S. albidoflavus and S. coelicolor datasets do not identify M8Z38; no target query was applicable. Absence is not negative biological evidence.

## Identity and Grounding

The full pinned backbone `data/raw/ncbitaxon_taxa.tsv:221977`, name `data/catalog/ncbi_names-0005.jsonl.gz:31445`, unique path lock `data/taxa/PATHS.tsv:14468` and scope `curation/seed_scope.tsv:322252` agree with the record.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035268&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035268) confirm the active species-rank label, parent and lineage. The root-first chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. All stored ancestor IDs, labels and ranks match the pinned source. Exact checks found no type-material, merged-ID or dropped row, and no child.

The inspected nomenclatural section of [LPSN's Streptomyces genus page](https://lpsn.dsmz.de/genus/streptomyces) identifies a validly published correct genus name with S. albus as type species. Whole-page search found no M8Z38. Genus synonymy, risk annotations and neighboring species' deposits cannot supply target-specific nomenclature or equivalence.

## Evidence

The single `NCBITAXON` `NAME` attestation has the exact ID/label and snapshot date 2026-09-13. Its count is not a biological strain or genome count. The `seed_from_sources` `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` agrees with the one-source scope explanation.

Full metadata for [JF729472.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729472.1), UID 334086848, identify a 1,533-nt partial 16S rRNA marker, strain M8Z38, exact taxon 1035268 and seagrass isolation source. W. Chen submitted it on 24 March 2011; creation and update dates are 31 May and 3 June 2011. Its unpublished-study and direct-submission references carry no PMID or DOI. No culture deposit, BioSample, BioProject, assembly, host species or collection-country qualifier is supplied. Institutional address is not collection locality; genomic DNA is not an assembly. Sequence bases were not analyzed.

[Wu et al., DOI:10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-full-text-pdf/2A88A4617354), page 88, links M8Z38/JF729472. Figure 2 shows M8Z38 separately. Table 2 gives S. cacaoi subsp. cacaoi, 96.31% similarity, PKS-I negative, PKS-II positive and NRPS positive. The discussion treats M8Z38 as a possible novel species. Relevant methods, discussion, figure and table were inspected.

These observations do not formally identify a species, equate strains, provide a whole genome or assembled biosynthetic cluster, or demonstrate antimicrobial activity. No target biological claim was imported into the record.

Exact designation and accession web searches supplied no additional inspected deposit or genome bridge. A paper mirror was only a lead; the publisher PDF was inspected.

## Completeness

Searches used `rg --no-ignore --hidden -n -z -i`, including ignored, hidden and compressed files, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier, label, slug and bounded designation pattern `\bM8Z[- _]?38\b` yielded nine rows: three target rows and six false numeric matches. All were read in full native metadata or TSV form. Five source-level `SOURCE.json` files and history filenames were checked separately.

A second JF729472 search across those roots, plus metadata/history filenames, returned no match. These are bounded snapshot results, not worldwide absence claims.

Exact checks found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. With no pinned descendants, zero BacDive strains agrees with the own-plus-descendant seeder rule; it does not deny the laboratory isolate.

Live non-expanding NCBI searches returned zero Assembly records and one nucleotide record. Assembly reported the taxid phrase not found, a bounded index result. The CAFI-backed normalizer returned no eligible culture key for M8Z38, M8Z-38 or M8Z 38. No valid deposit/genome chain was established.

No consequential required omission was found. Optional literature context is not mandatory for this source-attested seed. Unsupported nomenclature, deposit, genome and phenotype fields should remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored assertions. This pass is not a full-corpus reproducibility certificate.

## Recommended Edits

None required. Preserve exact NCBI placeholder identity, one-name attestation, zero BacDive count and seeded lifecycle. Do not replace the placeholder with the paper's nearest named comparator or promote a novelty suggestion to a formal name.

Future authorized enrichment belongs in maintained acquisition/extraction and `src/taxonmech/seed.py`. A literature representation requires supported inputs and tests; do not hand-edit generated YAML.

## Follow-up Checks

For literature enrichment, preserve the exact isolate/accession relation and assay scope. Genome association requires a whole eligible culture accession and an explicit source-specific sequence relationship. Keep taxon, strain, deposit, marker, sample, project and assembly identities distinct.

After authorized upstream changes, regenerate through the validated writer and rerun target schema/strict checks and full `just verify-corpus` and `just qc`. No regeneration or lifecycle promotion occurred.

## Additional Notes

The six numeric false matches were:

- Four Parabacteroides merdae assertions, taxid 46503, RTP21002st1_G2_RTP21002_201210, SAMN41035268, GCA/GCF_040924465.1, BV-BRC 46503.3054: `data/bvbrc/bvbrc-0020.jsonl.gz:25657`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20827`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19973`, `data/catalog/gtdb_genomes-0002.jsonl.gz:8714`.
- Two Mycobacterium tuberculosis assertions for ERR1035268: BV-BRC 1773.18298 at `data/bvbrc/bvbrc-0006.jsonl.gz:6089`; ATB SAMEA3558801, ERZ9334383 at `data/catalog/allthebacteria.tsv.xz:569738`. Its available FASTA and passing filters do not overcome the organism mismatch.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Ignored-inclusive filename checks found no prior report for this stem. The complete YAML was reread byte-unchanged. Only this new report was written for this target; validation diagnostics and publisher-PDF renderings used temporary storage. No record, history, lifecycle, site, Git or GitHub state changed, and Eukaryota was not reopened.

