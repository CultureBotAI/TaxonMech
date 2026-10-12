# YAML Record Review: Methylobacterium sp. T34

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_t34.yaml`
- Started UTC: 2026-10-06T17:35:04Z
- Finished UTC: 2026-10-06T17:37:16Z
- Verdict: pass

## Target

The fully read generated `TaxonRecord` denotes `NCBITaxon:1035239`, Methylobacterium sp. T34, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT and status SEEDED. It asserts ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, host/phenotype claim, discussion or graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14451`; scope is `curation/seed_scope.tsv:322235`. Seeded fields are generated from maintained inputs and logic. HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

The review skill and checklist were re-read; curation guidance, repository instructions, documentation, schema, seeder and commands had been inspected at this unchanged revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_t34.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_t34.yaml --out /private/tmp/mt34-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Bounded source comparisons confirmed identity, every ancestor, path/scope rows, attestation and event text. They are manual checks, not a focused corpus-reproduction validator.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates or global `just validate-history`. The reproduction gate has no target selector. No corpus-wide reproducibility or reference-integrity claim is made.
- `just validate-products` was not run: its configuration targets curator-added graph grounding, absent here, and skips NCBITaxon. Pinned and live NCBI were used for taxonomic identifiers.
- Ignored-inclusive content/path searches found no target external history artifact. No history event or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were inspected; none covers Methylobacterium/Methylorubrum. Not applicable, not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221960` supports the identity, rank, parent, code 11, empty synonyms and 2026-09-13 snapshot. The complete scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31428`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035239&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035239) agree. All stored ancestor labels and ranks agree with the pinned chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), unclassified Methylobacterium (2615210). XML LineageEx omits root; Datasets includes it.

EXACT identifies this NCBI concept, not valid nomenclature or a culture deposit. The [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), fully inspected in the recent T26 review and specifically searched for T34 here, supplies no target identity bridge. Genus properties and nomenclature must not be transferred. The legacy NCBI browser failed through the web tool; both authority APIs succeeded.

## Evidence

The sole NCBITAXON attestation matches identifier, label, count 1, unit NAME and snapshot. It counts one source-name assertion, not strains or genomes. The event at 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree.

No exact target rows occur in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone child has this target as parent. Zero BacDive records agrees with the own/subtree gathering rule in `src/taxonmech/seed.py`; it does not deny that T34 was cultivated.

The exact live query `txid1035239[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 347300736. Full [FR869835.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869835.1), excluding bases, was read: a 1335-nt partial 16S rRNA gene, strain T34, explicit `taxon:1035239`, host Trifolium repens and isolation source host leaf surface. Submission was 18 May 2011, creation 18 September, update 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. Genomic DNA describes the molecule source, not a genome assembly.

The marker cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The bibliography and complete abstract fetched during the recent C54b review were re-read for T34. Community-level comparisons across hosts, locations and land-use conditions do not establish named T34-specific growth, phenotype or collection locality. Its host comes from its own marker metadata. Full text and supplements were not inspected.

## Completeness

Ignored and compressed content was included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug produced nine rows, all fully inspected: three genuine taxonomy/name/scope rows and six unrelated numeric hits. Five discovered `SOURCE.json` files were separately parsed without a target value; ignored-independent history filename enumeration found no target artifact.

The same-root expanded query `(Methylobacterium|Methylorubrum).*\bT[- _]?34\b|\bT[- _]?34\b.*(Methylobacterium|Methylorubrum)` returned only the three genuine rows. Variants were leads, not asserted aliases. FR869835 produced no local accession hit in these roots. These are bounded local-catalog and exact live-query results, not universal absence claims.

`normalize_culture_identifier` returned empty for T34, T-34 and T 34. No eligible own-deposit/owning-strain bridge or required missing genome link was established. The marker is optional identity evidence, not an owning BacDive strain or same-deposit StrainInfo assertion. Empty optional definition, evidence and graph slots need not be filled without supported claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertions and bounded completeness checks. Pass does not certify unrun corpus gates or uninspected full text.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future supported additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Scope edits belong in `curation/seed_scope.tsv`; upstream mapping corrections belong in kg-microbe. Do not patch generated YAML or pages.

## Follow-up Checks

Require T34's own eligible whole culture accession and source chain before adding links. StrainInfo sequences must name the matched SI-DP; GOLD must resolve a consistent own-organism/project/analysis chain; ATB requires exact existing BioSample evidence and an eligible available FASTA. Preserve taxon, strain, deposit, sample, project, marker and genome identities separately; a shared sample is not genome equivalence.

After an authorized maintained-input change, run target schema/strict checks and relevant join tests, then `just verify-corpus` and `just qc`. Read full text or supplements before asserting isolate-specific growth, phenotype or locality.

## Additional Notes

- Four excluded Lacticaseibacillus rhamnosus rows identify taxid 47715, strain 1001216st2_C2_RTP21198_201120, GCA/GCF_040925045.1, BV-BRC 47715.1903 and SAMN41035239: `data/bvbrc/bvbrc-0020.jsonl.gz:45792`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20002`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20856`, `data/catalog/gtdb_genomes-0002.jsonl.gz:38183`.
- `data/catalog/ncbi_genbank-0066.jsonl.gz:33813` is Puniceispirillum sp. (SeqCode), taxid 2026719, MAG KRUG19-1_SAMN06266119_MAG_00000020, GCA_982735085.1 and SAMEA122294997. Its genome size is 1035239; that number is not T34's taxid in this row.
- `data/catalog/allthebacteria.tsv.xz:569709` is ERR1035239, SAMEA3558772, ERZ3502606. Its scientific_name is Mycobacterium tuberculosis whereas current and previous sylph_species are Mycobacterium avium. This source discrepancy is preserved, not resolved into a preferred label. Despite an available FASTA and PASS filters, neither name identifies T34; no sample or genome link is transferred.
- Candidate fields were read losslessly. The target was re-read byte-identical. Only this report was written for T34; no YAML, history, status, generated product, Git or GitHub mutation was made.

