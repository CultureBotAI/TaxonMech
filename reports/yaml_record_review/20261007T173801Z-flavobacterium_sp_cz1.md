# YAML Record Review: Flavobacterium sp. cz1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/flavobacterium_sp_cz1.yaml`
- Started UTC: 2026-10-07T17:31:41Z
- Finished UTC: 2026-10-07T17:38:01Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036019`,
Flavobacterium sp. cz1: species rank, bacterial domain, parent 196869,
twelve root-first ancestors, genetic code 11, `EXACT` grounding,
`SEEDED` lifecycle, zero inventoried BacDive strains, one NCBITAXON
attestation and one inline seed event. No synonyms, nomenclature,
mappings, strain/genome objects, literature evidence, phenotype,
gene, expression dataset or causal graph are asserted.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/flavobacterium_sp_cz1.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/flavobacterium_sp_cz1.yaml --out /private/tmp/cz1-strict.tsv`: passed, one file, zero errors; complete header-only diagnostics read.
- Structured backbone, parent-chain, scope, path, attestation and seed-wording comparisons passed. These bounded checks do not reproduce the corpus.
- Live NCBI taxonomy XML, Datasets JSON, exact Assembly/Nuccore searches and complete nucleotide metadata read.
- `just validate-products`: not applicable, no curator-added graph terms. Taxonomic identifiers were checked against NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent target content/path searches. Inline history passed schema, strict and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- Not checked: independent sequence alignment, authenticated culture equivalence, the unpublished fermentation manuscript or a patent sequence-listing comparison.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036019&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036019)
confirm active identity, the exact lower-case strain designation
`cz1`, species rank and bacterial domain. EFetch confirms parent
`NCBITaxon:196869`, unclassified Flavobacterium, and code 11.
A strain-like species-rank label is not a formally named species
or a type-strain designation.

Pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222257`,
`data/catalog/ncbi_names-0005.jsonl.gz:31770`,
`data/taxa/PATHS.tsv:14755` and `curation/seed_scope.tsv:322514`.
The native scientific-name row has an empty unique name.
Source synonym columns, live alternate-name fields and retirement
are empty. The snapshot is 2026-09-13.

All twelve ancestors agree in order, labels, ranks and parent links:
root, cellular organisms, Bacteria, Pseudomonadati, FCB group,
Bacteroidota/Chlorobiota group, Bacteroidota, Flavobacteriia,
Flavobacteriales, Flavobacteriaceae, Flavobacterium and unclassified
Flavobacterium. The two intermediate groups have clade rank.
Parsed inventories contain no target children, type-material,
merged-ID or dropped rows. Exact grounding is not lifecycle promotion.

## Evidence

The attestation counts one NCBITAXON `NAME`, not isolates or genomes.
Exact-target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits
inventories contain no rows. With no descendants, `strain_count: 0`
correctly describes the BacDive inventory, not biological absence.

Scope and attestation reproduce the seed event wording.
The reread `src/taxonmech/seed.py::_seed_timestamp` selects the
latest extraction time among the raw, ATB and StrainInfo manifests.
Their 2026-09-13 times are respectively 17:50:44, 17:54:04 and 17:29:00
UTC, supporting the inline 17:54:04Z event. This is not review time.

Exact Nuccore query `txid1036019[Organism:noexp]` returns UID
334361895, [JF815372.1](https://www.ncbi.nlm.nih.gov/nuccore/JF815372.1).
Complete metadata identifies a 1,310-nt partial 16S rRNA sequence,
strain cz1, taxon 1036019 and China: Xiamen Harbor.
It includes PCR primer sequences and an rRNA feature partial at both ends.
Direct submission by Chen, Z. was on 14 April 2011 from Xiamen
University's College of Chemistry and Chemical Engineering.
Creation and update are both 6 June 2011.

The other reference is an unpublished fermentation-optimization
study by Chen, Z.; no DOI or PMID is supplied. No culture-collection,
BioSample or BioProject field occurs in the complete metadata.
The reference title alone does not verify a production phenotype,
yield, fermentation conditions or enzyme mechanism.
The marker is neither a whole-genome assembly nor independent
experimental verification of translation code 11.

Exact Assembly search returned zero with phrase-not-found/no-items
warnings. This bounded result does not exclude assemblies filed under
another name or identifier.

A broader fermentation search led to
[primary patent CN102492732A](https://patents.google.com/patent/CN102492732A/en).
Its inspected organism/deposit and identification sections concern
ch20-1, called Flavobacterium halmsphilum in that source, with
CGMCC No.5207. The retrieved HTML has no cz1 or JF815372 match.
This is not an authenticated identity chain to the target:
neither its deposit nor its experimental phenotype was transferred.
The patent's sequence appendix was not compared, and equivalence
was not inferred from research topic or institution.

## Completeness

Complete enough for the generated NCBI-only identity assertions.
Literature, marker and strain enrichment remain optional; the
record is not required to invent deposits, genomes or a graph.

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/` and `history/`. The taxid, full name, slug and bounded
CZ1/CZ-1/CZ_1/CZ 1 variants were searched. An expanded search added
JF815372 and the exact unpublished study title, returning the same
237 rows. All were read as complete TSV rows or native JSON objects;
lossless common-field/value-column grouping reduced repetition:

- Forty-five native scientific-name rows and their 45 backbone and 45 scope rows describe the target plus 44 other CZ1-containing taxa. These include Pseudomonas, Rhodopseudomonas, Bradyrhizobium/Sinorhizobium nodule isolates, Lysinibacillus, Enterobacter, Leptolyngbya and Psychrobacter. Their identifiers and classifications do not establish target identity.
- Three Escherichia records are the raw BacDive row, native BacDive 160359 and StrainInfo SI-ID 407911. They concern Cla-CZ-1/DSM 109009, not Flavobacterium. The native evidence includes taxon 2779353, GCA_014982845, BV-BRC 2779353.3, IMG 8035699417 and marker MN055927.1; StrainInfo's own deposit is SI-DP 915326. No link transfers.
- Three GOLD records connect Enterobacter sp. CZ-1, taxon 2516874, through Go0519900 and Gp0444069 to Ga0399550, GCA_004193715.1 and IMG 2869841491. They name PRJNA520972 and SAMN10872819, with an empty culture-collection field. The chain concerns Enterobacter, not this taxon.
- Ninety-six genome-catalog candidates comprise 27 BV-BRC, 27 GTDB and 42 GenBank/RefSeq rows. Of these, 34 are pig-metagenome records for SAMEA110360190 through SAMEA110360199 under PRJEB52643 or the RefSeq umbrella project. Their numeric sample fragments are not taxon identifiers.
- Two of those 96 rows are GTDB/GenBank records for Parcubacteria group bacterium GW2011_GWA2_38_13, taxon 1618811, GCA_000992395.1 and SAMN03319403. Its ungapped genome length is 1036019, causing the numeric match.
- The remaining 60 genome-catalog rows concern other CZ1-designated organisms: Enterobacter cloacae CZ-1, Leptolyngbya boryana CZ1, two Acinetobacter lwoffii cz-1 sample chains, and AOP5-CZ1 isolates/metagenome bins. Complete source metadata, native status, taxonomy, assemblies, projects and samples were retained during inspection. A shared short name does not bridge them to Flavobacterium sp. cz1.

Five native `SOURCE.json` objects were fully parsed at both search
stages; history filenames were independently searched. No additional
applicable local assertion, deposit, strain-genome link or target
standalone history artifact was found in these bounded roots,
including ignored/hidden/compressed files. No global absence is claimed.

Public full-name, accession, reference-title and fermentation searches
did not verify an exact-target published article. That is a search
limitation, not evidence that no publication exists.
iModulonDB is not applicable: no gene, regulator, expression module
or transcriptomic dataset is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, omitted synonyms, source attestation,
inventory count and seed provenance are supported. An unpublished
external study and unrelated short-name hits do not create a required
representation gap in the YAML.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
Future corrections belong to maintained upstream inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes
belong to `curation/seed_scope.tsv`. Do not patch generated YAML/pages
or create a lifecycle/history change from this review.

## Follow-up Checks

Optional fermentation enrichment needs the actual exact-strain study,
not its GenBank title or a differently designated patent strain.
Any deposit/genome enrichment needs an explicit identity chain.
After authorized maintained-input changes, rerun the owning generator,
per-file schema/strict checks and applicable corpus gates.
New history requires `just validate-history`; new graph terms
and evidence require `just validate-products`.

## Additional Notes

The full YAML was reread and remained byte-identical before report
creation. All target-specific reads and retrievals reached terminal
outcomes. Only this new report is added; no record, source, history,
lifecycle, page, GitHub, branch or worktree was changed.
Eukaryota was not re-reviewed.
