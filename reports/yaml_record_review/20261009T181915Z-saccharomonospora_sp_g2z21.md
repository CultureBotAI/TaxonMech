# YAML Record Review: Saccharomonospora sp. G2Z21

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/saccharomonospora_sp_g2z21.yaml`
- Started UTC: 2026-10-09T18:16:35Z
- Finished UTC: 2026-10-09T18:19:15Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` for `NCBITaxon:1036966` was read. It denotes Saccharomonospora sp. G2Z21, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2634184`, genetic code 11, grounding `EXACT`, status `SEEDED`. It contains ten lineage entries, no synonyms, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved exactly this YAML and no prior own report. Target SHA-256: `1315d32974b19a824758d8c70ee1e326b941ee54f95d8cac43641730c98a69e8`; unchanged after the review.

## Validation

Repository commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/saccharomonospora_sp_g2z21.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/saccharomonospora_sp_g2z21.yaml --workers 1 --out /private/tmp/taxonmech-saccharo-g2z21-20261009-validation.tsv`: passed, one file and zero errors; the inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier in this review session, 17 valid records and zero invalid links. History and schema files remained unchanged.
- Focused own-row comparisons passed for identity, all ancestors, source attestation, PATHS/scope entries and generated event wording. All three local source candidates were read completely.
- Live NCBI taxonomy EFetch and Datasets responses, an exact non-expanded nucleotide search, the complete returned GenBank record metadata/features/references and an assembly query were inspected. Sequence length/alphabet/hash checks passed; no new phylogenetic analysis is claimed.
- The NCBI Taxonomy browser page failed through the web tool; both structured taxonomy APIs succeeded.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and generated-site drift. `just verify-corpus` has no record selector; focused comparisons do not certify reproduction.
- Not applicable: curator-added ontology graph or iModulonDB functional-context checks. The YAML asserts no graph, gene, pathway, regulator, phenotype or transcriptomic result.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222651` and the complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32250` agree with the identifier, label, rank, parent, code and 2026-09-13 snapshot. Neither supplies an alias or retirement.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036966&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036966) independently identify the same taxon. The complete root-first lineage agrees with the backbone: root 1 (`NO_RANK`), cellular organisms 131567 (`CELLULAR_ROOT`), Bacteria 2 (`DOMAIN`), Bacillati 1783272 (`KINGDOM`), Actinomycetota 201174 (`PHYLUM`), Actinomycetes 1760 (`CLASS`), Pseudonocardiales 85010 (`ORDER`), Pseudonocardiaceae 2070 (`FAMILY`), Saccharomonospora 1851 (`GENUS`) and unclassified Saccharomonospora 2634184 (`NO_RANK`). EFetch lists the ancestors after root; Datasets includes root 1.

The species rank is NCBI's treatment of this strain-designated taxon. It is not a claim that G2Z21 is a formally named species or a nomenclatural type. No sibling species identity is inferred from the genus or strain abbreviation.

## Evidence

The sole NCBITAXON attestation agrees with the source identifier, exact label, count one, `NAME` unit and dated snapshot note. `strain_count: 0` describes BacDive inventory coverage, not an assertion that the organism is unculturable or lacks a strain designation.

The [exact-taxon nucleotide search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036966%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one record, [JF806667.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806667.1), GI 334361412. Its structured source names Saccharomonospora sp. G2Z21, strain G2Z21 and `taxon:1036966`.

JF806667.1 is a partial 16S rRNA sequence, not an assembly. Declared and actual length agree at 1,405 nucleotides; the sequence alphabet is A/C/G/T and its SHA-256, computed on the lower-case EFetch sequence string, is `3c5686797170e50e1ce00ed854ec8156fbbd55eba7cad793b13abf1a4e1fb4ad`. The rRNA feature is partial at both ends. No whole-genome content, culture-collection identifier or protein-coding experiment is supplied by that marker record.

The complete GenBank references include an unpublished study by Chen, Wu and Li concerning culturable actinobacteria from seagrass, and a direct submission dated 2011-04-13. No PMID or DOI is supplied there. That bibliographic title is not sufficient to assign a precise habitat, isolation protocol, growth requirement or measured phenotype to G2Z21; the YAML asserts none. No claim is made that an eventual journal publication does not exist.

The [own assembly query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036966/dataset_report) returned an empty object. It provides no positive current assembly evidence, not proof of universal genome absence. No inspected source establishes the explicit eligible culture-deposit chain required for a strain-level genome link.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded numeric ID, full label/slug and G2Z21 designation. They returned only three own candidates: the backbone, native scientific-name and seed-scope rows, all inspected in full.

All five local source `SOURCE.json` files were parsed without a target match. Further ignored-inclusive compressed searches for JF806667 and the distinctive unpublished-study title found no match in those roots. These negatives concern the inspected local snapshots and exact identifiers, not all external evidence.

Complete own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory assertion, type-material row, merged-ID row, dropped record or child. The empty optional synonym, nomenclature, mapping, strain/genome, experimental-evidence and graph slots are appropriate for the supported taxonomy seed. The external marker is a possible later typed nucleotide cross-reference, not a missing required whole-genome assembly.

`data/taxa/PATHS.tsv:15184` agrees with the filename. `curation/seed_scope.tsv:322884` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z agrees with the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry. Human-reviewed status is not asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. Identity, lineage and provenance are supported. The partial marker and an unpublished-study title do not establish omitted culture-deposit, genome or experimental claims.

## Recommended Edits

None required. Keep the distinction between the NCBI taxon, the strain designation G2Z21, a registered culture deposit and a whole-genome assembly.

Any later authorized correction belongs in maintained extraction inputs, `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit generated YAML. Any future JF806667 cross-reference should preserve its nucleotide-marker type and exact source provenance.

## Follow-up Checks

No defect-specific repair is needed. Inspect strain-specific primary evidence before habitat or phenotype enrichment; do not transfer a study-wide statement solely from its title. Genome links require an explicit eligible culture-deposit chain. Before authorized regeneration, run the documented corpus reproduction, provenance, schema/strict, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. No Eukaryota record was reviewed. No paid research was performed.
