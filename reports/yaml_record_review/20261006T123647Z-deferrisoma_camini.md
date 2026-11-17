# YAML Record Review: Deferrisoma camini

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/deferrisoma_camini.yaml`
- Started UTC: 2026-10-06T12:29:50Z
- Finished UTC: 2026-10-06T12:36:47Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035120`, Deferrisoma camini. It has SPECIES rank, BACTERIA domain, parent 1125862, nine root-first ancestors, EXACT grounding, SEEDED status and genetic code 11. It contains one LPSN nomenclature entry, one authority synonym, two xrefs, one BacDive strain with two assembly assertions, three genome-record assertions and nine related-record assertions, seven source attestations and one seed event.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/deferrisoma_camini.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/deferrisoma_camini.yaml --out /private/tmp/dcamini-validation.tsv`: passed, one file and zero errors. The output TSV was read and contains only its header.
- Structured source comparisons inspected the complete backbone row and ancestor chain, seven other imported taxon tables, PATHS/scope, synonyms, attestations and seed provenance.
- Exact-ID reads inspected seven type-material rows; no exact target entry was found in the merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant sequence searches, five complete assembly summaries, marker/WGS metadata and the PubMed citation were inspected. The StrainInfo live API and relevant primary source pages were also checked.
- Repository culture-identifier normalization was exercised read-only for DSM 24185, VKM B-2672 and S3R1 against the inspected CAFI patterns.
- `just validate-products` is inapplicable: no curator-added graph nodes. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history content and filename searches found no separate target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221896` supports the exact label, species identity, parent, genetic code and authority synonym. `data/taxa/PATHS.tsv:14384` resolves the file, and `curation/seed_scope.tsv:7210` supplies its 2026-09-12 seven-source scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035120&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035120) agree with the species concept and all nine ancestors: 1, 131567, 2, 3379134, 200940, 3031652, 2814222, 3031670 and 1125862. The last is the genus Deferrisoma. The backbone separately represents S3R1 as child strain 1125863; retaining that child taxid on strain-specific genome evidence does not misidentify this species record.

[LPSN](https://lpsn.dsmz.de/species/deferrisoma-camini) supports name ID 790210, Slobodkina et al. 2012, the validly published and legitimate correct name, the type-strain equivalence S3R1 = DSM 24185 = VKM B-2672, and marker JF802205. The imported LPSN row at `data/raw/lpsn_names.tsv:27190` contains DSM-24185 in its type-designation subset; both culture deposits are nevertheless preserved on the record's strain. This is not a missing type-strain identity.

The GTDB species xref is carried from that LPSN row. There is no exact species-taxid row in `data/raw/gtdb_mappings.tsv`; the inspected mapping belongs to child 1125863. The YAML does not falsely claim an explicit GTDB species mapping or copy the species name into a strain synonym. GTDB's inspected native classification uses Desulfobacterota, while the record carries NCBI's Thermodesulfobacteriota. These source classifications were not silently reconciled.

## Evidence

The nomenclatural [2012 publication](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.038372-0) and [PMID 22140176](https://pubmed.ncbi.nlm.nih.gov/22140176/) agree on the authors, species description, type-strain equivalence and DOI 10.1099/ijs.0.038372-0. The complete PubMed abstract was read; the full experimental paper was not. The second DOI, [10.1099/ijs.0.049288-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.049288-0), resolves to the 2013 notification publication identified by LPSN, not a second independent experimental study. Publisher metadata and abstract were inspected; its complete notification table could not be retrieved.

[JF802205.1](https://www.ncbi.nlm.nih.gov/nuccore/JF802205.1) is a 1,503-base partial 16S rRNA sequence with strain S3R1, type-material annotation, child taxid 1125863 and the same publication. It supports the unversioned INSDC accession in the nomenclature entry, not a genome assembly. Its source metadata places the isolate at a deep-sea hydrothermal vent; no species-wide habitat assertion was inferred.

[BacDive 18151](https://bacdive.dsmz.de/strain/18151) and its complete pinned native row support the one type strain, both culture deposits, and reference 66792 for the GenBank, IMG and BV-BRC assertions. The raw normalized strain row is `data/raw/bacdive_strains.tsv:17958`. GCA_000526155 is preserved unversioned from BacDive, whereas GOLD explicitly supplies GCA_000526155.1. IMG 2517093047 appears twice with different source provenance; PATRIC/BV-BRC 1125863.3 is also confirmed in the inspected native BV-BRC row. These are source assertions, not counts of independent genomes.

The pinned GOLD rows establish DSM 24185 on Go0015937, its explicit project Gp0015937, and analysis Ga0026649. The project supplies PRJNA160107 and SAMN02584914; the analysis supplies GCA_000526155.1 and IMG 2517093047. Its empty direct organism field is resolved through the explicit project-to-organism chain, not a name-only join. Go0613550 separately identifies VKM B-2672 at the species taxid. The two assertions for Go0613550 retain different source fields, ORGANISM CULTURE COLLECTION ID and ORGANISM STRAIN; they are not identical duplicate provenance.

The [live NCBI assembly summary](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&id=95891&retmode=json) verifies GCA_000526155.1 and its identical RefSeq pair GCF_000526155.1, S3R1, child taxid 1125863, species 1035120, Contig level, one contig, 4,236,551 bases, PRJNA160107 and SAMN02584914. The current summary marks it a reference genome without an exclusion. [JAFN00000000.1](https://www.ncbi.nlm.nih.gov/nuccore/JAFN00000000.1) independently confirms the type-strain WGS project and component JAFN01000001. A WGS master is not itself a one-base genome.

The full [StrainInfo API response](https://api.straininfo.dsmz.de/v2/data/strain/max/399396) confirms strain 399396, its versioned DOI 10.60712/SI-ID399396.3, published-online status, BacDive 18151 and its own available DSM 24185 deposit 906182. The stored deposit evidence matches the pinned native record. VKM B-2672 is a related designation there, not a second own deposit that can be fabricated into a sequence join. The inspected StrainInfo record supplies no sequence assertion.

All seven attestations match the imported tables: NCBI one NAME, LPSN one NAME with closeMatch, BacDive one STRAIN, MediaDive one MEDIUM, GOLD one directly assigned ORGANISM, MADIN five TRAIT_ASSERTIONs and BactoTraits twenty TRAIT_ASSERTIONs. The latter four explicitly exclude descendant aggregation. The GOLD count therefore need not equal the number of strain-level related-record assertions. Trait counts do not establish phenotype values. The single 2026-09-13T17:54:04Z seed event matches the seven-source inventory and does not claim human review.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered the target's identity and strain identifiers across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included. All 90 initial candidate rows were read in full: 43 TSV and 47 native JSONL rows.

Expanded searches for the assembly, marker, WGS master, BioProject, BioSample, IMG/PATRIC, GOLD, StrainInfo and publication identifiers returned 93 addresses, 28 previously inspected and 65 new. All 58 new TSV and seven new native rows were read in full, giving 155 unique inspected candidate rows. Lossless common-field reconstruction and address reconciliation were checked. The five SOURCE.json files were separately fully traversed for the identity pattern with no hit. History content and filenames had no target artifact in the checked roots.

The native GTDB row for RS_GCF_000526155.1 gives only S3R1 as its strain identifier. The repository's whole-token culture matching accepts DSM 24185 and VKM B-2672 but not bare S3R1. Omitting a GTDB strain-genome assertion therefore follows the current importer contract. The optional paired RefSeq accession is supported by NCBI, but no rule requires inventing a new imported assertion absent its supported source route.

The ATB row for SAMN02584914 has a FASTA but fails metadata identity filtering. `data/atb/exclusions.tsv:1703` explicitly records metadata_identity_flags:META_FAIL, consistent with the native ATB row's META_FAIL and SYLPH_RESULTS_FAIL. It is correctly absent from published strain genome assertions.

Exact non-descendant Assembly searches returned four items for species 1035120 and one for child strain 1125863. All five assembly summaries were read. Besides the type-strain genome, they identify UBOCC_M_3608 (GCA/GCF_060535955.1) and three metagenomic SZUA assemblies (GCA_003251655.1, GCA_003251215.1 and GCA_003246115.1). None supplies an established DSM/VKM join to this BacDive strain. The three MAGs are flagged as metagenome-derived and fragmented; the recent UBOCC assembly has no type claim and an inconclusive taxonomy check. Shared species assignment is insufficient to attach any of them to S3R1.

Exact Nuccore searches returned 125 species-direct and six strain-direct accessions; all returned IDs were inspected, but only the cited marker and type-strain WGS master's full metadata were read. This was not an annotation audit of every nucleotide record. The native SeqCode entry for name 6093 was inspected as a source pointer, not treated as a missing mandatory xref.

No material missing representation was established. Optional phenotype, habitat and graph slots may remain empty. iModulonDB is inapplicable because the YAML names no functional gene, regulator, pathway or expression module.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed identity, nomenclature, evidence provenance, strain joins, counts or status. Inaccessible optional endpoints and unrun corpus gates are limitations, not demonstrated YAML defects.

## Recommended Edits

None required. Do not hand-edit the generated YAML, merge distinct provenance assertions, turn JF802205 into a genome, attach species-level MAGs to the type strain, or bypass ATB/registered-culture identity checks.

Any later source refresh belongs in the maintained inventories and extraction pipeline, including `src/taxonmech/extract.py`. Changes to culture matching or genome provenance belong in `src/taxonmech/genome_sources.py`; generated representation changes belong in `src/taxonmech/seed.py`. Regenerate only after the maintained inputs and rules have been reviewed.

## Follow-up Checks

For a future refresh, recheck species 1035120, child 1125863, both culture deposits, the GOLD project/analysis chain and StrainInfo's own-deposit/versioned evidence. A newly eligible genome assertion must retain explicit source fields and identity provenance.

Run both focused validators on any regenerated record and corpus reproduction/full QC before release. Retrieve the notification table or full original paper before making claims that require their uninspected contents.

## Additional Notes

The expanded LPSN hits mostly share the same notification DOI; the genus Deferrisoma row also shares the species-description publication. They are not additional names for this species. Other expanded hits contain longer WGS prefixes such as JAJAFN, DBJAFN, DAJAFN, ABJAFN, AAJAFN or CAJAFN and concern unrelated taxa.

Initial numeric near-misses include Staphylococcus haemolyticus with SAMEA1035120, Mycobacterium tuberculosis ERR1035120, Bifidobacterium with SAMN41035120, community BioSamples SAMN10351200-09, a Campylobacter assembly containing the digits 010351205, and unrelated genome-size/hash substrings. None establishes target identity.

The live GTDB browser page and StrainInfo DOI/UI endpoints were unavailable; inspected pinned GTDB data and the successful live StrainInfo API provided the stated bounded checks. The LPSN page was a cached rendering, not claimed to be a fresh database export. Live GOLD/IMG UI retrieval, complete experimental full text, independent sequence analysis and release-wide certification were not performed.

Only this new report was written for this target. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
