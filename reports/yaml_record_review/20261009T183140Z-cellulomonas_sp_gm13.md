# YAML Record Review: Cellulomonas sp. GM13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/cellulomonas_sp_gm13.yaml`
- Started UTC: 2026-10-09T18:28:14Z
- Finished UTC: 2026-10-09T18:31:40Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` for `NCBITaxon:103710` was read. It denotes Cellulomonas sp. GM13, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2620175`, genetic code 11, grounding `EXACT`, status `SEEDED`. It contains ten ancestors, one NCBI synonym, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and no prior own report. Target SHA-256: `e31509e4b6a3a7ac9760adb3eebd954839955da8bc58f87e9d9bdd73c91dee38`, unchanged after review.

## Validation

Repository commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/cellulomonas_sp_gm13.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/cellulomonas_sp_gm13.yaml --workers 1 --out /private/tmp/taxonmech-cellulo-gm13-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history and schema remained unchanged.
- Focused own-row comparisons passed for identity, the synonym, all ancestors, source attestation, PATHS/scope entries and event wording. All 20 local source candidate rows were read completely, including unrelated designation matches.
- Live NCBI taxonomy EFetch/Datasets, exact non-expanded nucleotide search, complete metadata/features/references for its three sequence records and an assembly query were inspected. Nucleotide length/alphabet/hash checks passed; CDS translations were represented by length and SHA-256.
- The NCBI Taxonomy browser webpage failed through the web tool; both public structured taxonomy APIs succeeded.
- Not checked: new functional, protein-sequence or phylogenetic analysis; detailed experimental confirmation beyond the inspected sequence annotations. None is asserted by the YAML.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and generated-site drift. `just verify-corpus` has no record selector; focused comparisons do not certify reproduction.
- Not applicable: curator-added ontology graph or iModulonDB functional-context checks. The YAML names no gene, pathway, regulator, phenotype or transcriptomic dataset. The iModulonDB catalog inspected earlier in this review session has no Cellulomonas dataset.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18549` and the native rows at `data/catalog/ncbi_names-0000.jsonl.gz:38580` and 38581 agree with the identifier, label and synonym. The alternate spelling Cellulosimonas sp. GM13 is explicitly classed as `synonym` by NCBI; it is not a reviewer-invented taxonomic correction. The repository's native-name conversion in `src/taxonmech/ncbi_taxdump.py` maps that class to `EXACT_SYNONYM`.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103710&retmode=xml) confirms the current scientific name, that exact alternate spelling under `Synonym`, parent 2620175, species rank and code 11. [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103710) independently confirms the current node and root-inclusive lineage.

The ten ancestors agree with the backbone: root 1 (`NO_RANK`), cellular organisms 131567 (`CELLULAR_ROOT`), Bacteria 2 (`DOMAIN`), Bacillati 1783272 (`KINGDOM`), Actinomycetota 201174 (`PHYLUM`), Actinomycetes 1760 (`CLASS`), Micrococcales 85006 (`ORDER`), Cellulomonadaceae 85016 (`FAMILY`), Cellulomonas 1707 (`GENUS`) and unclassified Cellulomonas 2620175 (`NO_RANK`). There is no inspected own retirement or child.

The species rank is authority-carried; it does not establish a formally named species or a type strain. A shared designation GM13 is not an identity key across unrelated genera, source collections or experiments.

## Evidence

The NCBITAXON attestation agrees with the exact source label/identifier, count one, `NAME` unit and 2026-09-13 snapshot. `strain_count: 0` reports BacDive inventory coverage, not absence of a biological strain or of sequence submissions.

The [exact-taxon nucleotide search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid103710%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned three entries. All have source organism Cellulomonas sp. GM13 and `taxon:103710`; AJ245568.1 additionally has the explicit strain qualifier GM13.

- [AJ245568.1](https://www.ncbi.nlm.nih.gov/nuccore/AJ245568.1): 1,472-nucleotide 16S rRNA record, not a genome assembly.
- [AF181718.2](https://www.ncbi.nlm.nih.gov/nuccore/AF181718.2): 2,315-nucleotide record with a Chi63 CDS and endo-63 precursor/endochitinase annotations. The CDS uses code 11; signal and mature-peptide features carry experimental qualifiers without recorded experimental details.
- [AF242587.2](https://www.ncbi.nlm.nih.gov/nuccore/AF242587.2): 2,371-nucleotide record with a nagA CDS annotated as beta-N-acetylglucosaminidase, also using code 11.

Both AF records explicitly state that their .2 sequence versions replaced .1 on 2001-02-05. The present YAML cites neither version and does not introduce a stale accession. The annotations are source-specific sequence information, not independently verified taxon-wide functional claims.

Declared and observed nucleotide lengths agree, alphabet A/C/G/T. SHA-256 of the lower-case EFetch sequences is `6ebb6ab7bf3d845e7bfc10c70676532709eeb24c96c0350a55570e801b063656` for AJ245568.1, `7acbdc70721f4ac8cb2ba9d1331951cd38f20f451014942dbda5a9e60b8f502e` for AF181718.2 and `17e8be7850a4cc18822ee124f8d49072253bf4555f75346a4e5928a7d3cc1fef` for AF242587.2.

The complete GenBank reference sets comprise unpublished or direct-submission entries involving Choi, Kim, Shin and, on the 16S entry, Park; none supplies a PMID or DOI. This is not proof that no later journal publication exists. The records do not establish a registered culture-deposit chain or whole-genome assembly. The [own assembly query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103710/dataset_report) returned an empty object, providing no positive assembly evidence rather than universal genome absence.

Several search candidates are not this taxon:

- Native NCBI and scope rows identify Rhizobium sp. GM13 as 741650, gamma proteobacterium GM13 as 936962 and Pseudomonas sp. GM13 as 1284042.
- GOLD Go0259748 is Mycoplasma capricolum GM13, taxon 2095. StrainInfo SI-ID40940 concerns Mycoplasma capricolum subsp. capricolum, taxon 40479, with deposit ATCC 35235 and alternative designation GM13. Neither supplies a Cellulomonas deposit.
- BV-BRC 993073.27, GCA/GCF_042879275.1 and GTDB RS_GCF_042879275.1 concern Microbacterium enclense, taxon 993073, sample SAMN44027483. Their matching strain shorthand does not supply a mapping or genome link for 103710.
- GOLD project Gp0662631 concerns a Chlamydomonas reinhardtii transcriptome sample whose experimental label ends in GM13, not a bacterial strain match.

These distinctions were established from complete native source records, not inferred from search snippets.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included the bounded NCBITaxon CURIE, structured numeric taxonomy/NCBI-ID fields, slug, both label spellings and bounded GM13 designation variants. All 20 candidates were read in full: 12 native JSON rows and eight TSV rows.

All five source `SOURCE.json` files were parsed without a target match. Further ignored-inclusive compressed searches for AJ245568, AF181718, AF242587 and their two CDS protein accessions found no local match in those roots. These negatives are bounded to the inspected snapshots and identifiers.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped record or child. Optional nomenclature, mapping, strain/genome, experimental-evidence and graph slots are appropriately empty for this taxonomy seed. External gene/marker references are possible later typed provenance enrichment, not missing required genome links or functional claims.

`data/taxa/PATHS.tsv:15186` agrees with the filename. `curation/seed_scope.tsv:144192` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no own external entry. Human-reviewed status is not asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. Identity, native synonym scope, lineage and source provenance are supported. Unrelated uses of GM13 do not establish missing deposits or genome links, and sequence annotations alone do not require new experimental assertions.

## Recommended Edits

None required. Preserve the authority-supplied synonym and distinguish the taxon identifier from the nonunique strain shorthand.

Any later authorized correction belongs in maintained extraction inputs, `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit the generated YAML. Future sequence enrichment should preserve accession versions and distinguish markers, coding-sequence records and whole assemblies.

## Follow-up Checks

No defect-specific repair is needed. Inspect primary experimental evidence before functional enrichment and require an explicit eligible deposit chain before linking any GM13 genome. Before authorized regeneration, run the documented corpus reproduction, provenance, schema/strict, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. The Chlamydomonas source row was disambiguation context only; no Eukaryota YAML was reviewed. No paid research was performed.
