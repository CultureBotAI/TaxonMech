# YAML Record Review: Psychrobacter sp. MF2-10b2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/psychrobacter_sp_mf2_10b2.yaml`
- Started UTC: 2026-10-06T17:38:07Z
- Finished UTC: 2026-10-06T17:45:26Z
- Verdict: needs curation

## Target

The fully read generated `TaxonRecord` denotes `NCBITaxon:1035242`, Psychrobacter sp. MF2-10b2, rank SPECIES, domain BACTERIA, parent `NCBITaxon:196806`, genetic code 11, grounding EXACT and status SEEDED. It carries ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. Synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, discussion and causal graphs are absent from this file.

The unique path-lock row is `data/taxa/PATHS.tsv:14452`; scope is `curation/seed_scope.tsv:322236`. HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. This review identifies a source-coverage/model completeness gap, not a wrong NCBI identity or a demonstrated failure to reproduce existing inputs.

## Validation

The review skill, checklist, curation guidance, CLAUDE.md, justfile, CURATION, HARMONIZATION, SCHEMA, SOURCE_COVERAGE, history guidance, relevant schema and seeding/source code were inspected at the unchanged revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/psychrobacter_sp_mf2_10b2.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/psychrobacter_sp_mf2_10b2.yaml --out /private/tmp/pmf2-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Bounded manual comparisons checked every identity/lineage field, path/scope, attestation and event against pinned rows. These are not a focused corpus-reproduction validator.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates or global `just validate-history`. `scripts/verify_corpus.py` has no target selector. Corpus-wide reproduction and reference integrity are not certified.
- `just validate-products` was not run: its configured curator-added graph grounding is absent here; NCBITaxon is skipped by that gate. Authority and inventory checks cover the taxonomic identifiers instead.
- Ignored-inclusive content and path searches found no target external history artifact in the searched history tree. No review event or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were inspected; none covers Psychrobacter. Not applicable, not negative biological evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221961` supports the identity, rank, parent, genetic code, empty synonyms and 2026-09-13 snapshot. The scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31429`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035242&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035242) agree. All stored ancestor labels and ranks match the pinned chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Gammaproteobacteria (1236), Moraxellales (2887326), Moraxellaceae (468), Psychrobacter (497), unclassified Psychrobacter (196806). XML omits root in LineageEx; Datasets includes it.

EXACT identifies the NCBI concept, not a validly published binomial or a deposit. The fully inspected [LPSN genus page](https://lpsn.dsmz.de/genus/psychrobacter) lists Pseudomonadales rather than NCBI's Moraxellales. This is retained as an external hierarchy disagreement, not a YAML defect: `docs/HARMONIZATION.md` requires carrying NCBI's lineage, without reconciliation. The genus page contains neither the exact strain nor pisciculus. The attempted LPSN species URL was inaccessible, which alone proves no absence. LPSN's separate piscatorii entry is not a spelling correction or identity match for pisciculus.

The external collection name discussed below does not authorize renaming this taxon or setting LPSN-derived nomenclature/type flags. An exact NCBI scientific-name search for Psychrobacter pisciculus returned zero with quoted-phrase-not-found diagnostics. Nomenclatural standing remains unresolved, not proven invalid.

## Evidence

The NCBITAXON attestation exactly matches identifier, label, count 1, unit NAME and snapshot. The seed event at 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree. One NAME assertion is not a biological strain or genome count.

No exact target rows occur in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone child has this target as parent. The zero count correctly follows the BacDive own/subtree rule in `src/taxonmech/seed.py:488`; it must not be interpreted as absence of a cultivated strain.

The exact live query `txid1035242[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 333827856. Complete [JF800153.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF800153.1), excluding bases, describes a 1408-nt partial 16S rRNA gene with strain MF2-10b2 and explicit `taxon:1035242`. Its source qualifiers give Long Island Sound, host Fundulus heteroclitus, USA and identifier C. Fricano. Submitted 25 March 2011; created/updated 29 May 2011. No culture collection, BioSample, BioProject or assembly identifier is supplied in this nucleotide record. Genomic DNA is not an assembly assertion.

The marker bibliography names Boucaud and Fricano and an unpublished study of two Psychrobacter isolates from this host's scales. It supplies no PMID or DOI. Exact-strain/title web follow-up found the collection resources below. A PubMed query for the exact strain or collection binomial returned zero and quoted-phrase-not-found warnings; its translated query was inspected. This bounded result does not establish that no publication exists. Full text or supplements for the unpublished submission were not available for inspection.

The inspected [ATCC product record](https://www.atcc.org/products/baa-2286) explicitly associates deposit BAA-2286 with designation MF2-10b2 and cross-references JF800153. It uses Psychrobacter pisciculus, flags the deposit as a type strain, names D. Boucaud as depositor and reports origin in 2009. Its fish-scale/Long Island Sound provenance agrees with the marker; it additionally specifies Connecticut. This is a direct deposit-to-marker-to-taxon chain, not merely a name match. The collection's type designation is source-specific, not verified LPSN nomenclature.

That product's genome link resolves to the inspected [ATCC genome record 8dc642072f90499d](https://genomes.atcc.org/genomes/8dc642072f90499d), identifying the same deposit and strain. It reports publication on 26 November 2024, a 3,262,008-nt hybrid assembly with three circularized contigs. The public metadata inspected supplies no GCA/GCF accession or BioSample bridge. This proves a source-reported genome relationship, not equivalence to an NCBI assembly or independent sequence-quality validation. No genome download, purchase, login or contact was attempted.

## Completeness

Ignored and compressed content was searched with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug produced 16 rows, all read losslessly: three genuine taxonomy/name/scope rows and 13 unrelated numeric matches. Five discovered SOURCE.json documents were parsed in full, with no target value; history filenames were enumerated independently of ignore rules.

The expanded same-root regex `\bMF[- _]?2[- _]?10[- _]?b[- _]?2\b` returned only the three genuine rows. Separate JF800153 and `pisciculus|BAA[- _]?2286` searches returned zero. Source metadata and history filenames were also rechecked for these newly observed identifiers without a match. These statements concern the named input roots, not every remote resource or ignored original snapshot elsewhere.

`normalize_culture_identifier` rejects bare MF2-10b2 but accepts ATCC BAA-2286 as ATCC-BAA-2286. Eligibility of the deposit's syntax does not manufacture an existing BacDive owner or authorize a name-based join. The exact external chain nevertheless establishes consequential missing strain/genome context for the repository's primary use case.

The boundary is explicit in `conf/source_coverage.yaml:73` and `docs/SOURCE_COVERAGE.md`: collection coverage is captured crosslinks, not independent complete collection crawls. `src/taxonmech/seed.py:488` constructs BacDive-owned strains; `TaxonSourceEnum` has no ATCC value, and `GenomeRecordLink` admits only GTDB, PATRIC, IMG and AllTheBacteria identifiers. The new relationship cannot be faithfully inserted into these generated fields without an authorized maintained-source/model extension. Optional phenotype, host, definition and graph slots need not be filled; phenotype/media/habitat curation belongs in sibling repositories.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**Major M1: Material strain-to-genome completeness gap outside the current source boundary.** The direct collection/deposit/marker chain and collection-hosted genome in Evidence are missing from the record and searched input inventories. This prevents this taxon from supporting the documented strain-to-genome use case despite primary evidence. It is not a false NCBI label, a wrong BacDive count, a dropped existing inventory row or a claim that the present source census is incorrectly advertised.

Maintained owners: the source inclusion contract in `conf/source_coverage.yaml` and `conf/sources.yaml`; a versioned primary-source capture/projection integrated through `src/taxonmech/source_catalog.py` and `src/taxonmech/extract.py`; and evidence-preserving representation in `src/taxonmech/schema/taxonmech.yaml` and `src/taxonmech/seed.py`. The exact new adapter/input design requires an authorized curation change. No generated YAML patch or fabricated BacDive/NCBI identifier is an acceptable fix.

No blocker or minor finding was established in the existing seeded assertions. NCBI/LPSN hierarchy disagreement and unresolved collection-name standing remain visible uncertainties, not grounds for silent replacement.

## Recommended Edits

1. Address M1 through a reviewed source/model extension: pin the primary collection metadata with provenance and terms, represent the explicit deposit-to-marker-to-taxon and deposit-to-genome chains, and define the collection genome identifier's scope. Preserve the marker as a nucleotide reference, not a genome. If collection-only strains need new ownership/count semantics, document and test those semantics before changing the seeder; do not increment a BacDive count ad hoc.
2. Keep the current NCBI identity/lineage and SEEDED status. Preserve source-specific alternative naming and type assertions as such; do not assert valid publication, taxon equivalence or an LPSN-derived type flag without the appropriate authority evidence.
3. Do not invent a GCA/GCF, SI-ID, SI-DP or BioSample bridge. No supported NCBI assembly equivalence was established. Future strain/genome links need their own explicit source chains, not co-occurrence or bare designation matching.

## Follow-up Checks

Recheck the exact source chain in Evidence when capturing a pinned primary snapshot. Confirm source terms and stable genome-record/version semantics before ingestion. Resolve nomenclatural standing at LPSN or a primary naming publication before any nomenclature assertion; lack of a search result is insufficient.

Add focused regression tests for collection-only strain ownership, the exact marker bridge, typed genome identity, provenance, and rejection of unrelated near-names or unsupported assembly equivalence. After an authorized maintained-input/model change, run target schema/strict validation, relevant adapter/seeder tests, `just verify-corpus` and `just qc`; regenerate through the validated writer and inspect the actual target. These are recommendations, not commands executed by this review.

## Additional Notes

- Four excluded Lacticaseibacillus rhamnosus rows identify taxid 47715, strain 1001216st2_G2_RTP21198_201120, GCA/GCF_040924995.1, BV-BRC 47715.1901 and SAMN41035242: `data/bvbrc/bvbrc-0020.jsonl.gz:45790`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20855`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20001`, `data/catalog/gtdb_genomes-0002.jsonl.gz:14290`.
- Five rows concern Muribaculaceae bacterium Isolate-002 (NCI), taxid 2489215, GCA_004102805.1, suppressed historical GCF_004102805.1, BV-BRC 2489215.3, SAMN10352428 and PRJNA503102: `data/gold/projects.jsonl.gz:404868`, `data/bvbrc/bvbrc-0014.jsonl.gz:31095`, `data/catalog/ncbi_genbank-0003.jsonl.gz:9034`, `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:19162`, `data/catalog/gtdb_genomes-0001.jsonl.gz:37436`. GOLD supplies Gp0551103/Go0576350; GTDB labels its cluster JAGBWK01 sp004102805. None is Psychrobacter.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6265` is Mycobacterium tuberculosis, taxid 1773, BV-BRC 1773.18458, run/strain ERR1035242. `data/catalog/allthebacteria.tsv.xz:569712` concerns that run, SAMEA3558775 and ERZ3502623, also Mycobacterium tuberculosis. Available FASTA/PASS filters do not transfer it to this target.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6455` is Campylobacter jejuni, taxid 197, strain 91273, GCA_010352425.1 and SAMN13326922. `data/catalog/ncbi_genbank-0066.jsonl.gz:33860` is Candidatus Pelagibacteraceae bacterium, taxid 2026775, MAG HAWL17-1_SAMN05224536_MAG_00000166, GCA_982736315.1 and SAMEA122259738; 1035242 is its genome size, not its taxid.
- The legacy NCBI taxonomy browser failed; the marker browser link reached a browser-check page. Public NCBI taxonomy/Datasets and nucleotide metadata APIs succeeded. The collection species URL at LPSN was inaccessible; the complete genus page was inspected.
- The target was re-read byte-identical. Only this new review report was written; no YAML, source inventory, history, status, generated product, Git or GitHub mutation was made.

