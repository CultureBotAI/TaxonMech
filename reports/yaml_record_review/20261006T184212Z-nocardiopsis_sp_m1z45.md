# YAML Record Review: Nocardiopsis sp. M1Z45

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_m1z45.yaml`
- Started UTC: 2026-10-06T18:39:57Z
- Finished UTC: 2026-10-06T18:42:12Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1035262`, Nocardiopsis sp. M1Z45, was read before judgement. It is a species-rank placeholder in Bacteria, parent `NCBITaxon:2649073`, genetic code 11, with ten lineage entries, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. It stores no synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, phenotype evidence or causal edges.

The record is generated from maintained scope and pinned inventories. Future fixes belong in `curation/seed_scope.tsv`, source acquisition/extraction or `src/taxonmech/seed.py`, as appropriate, not in the YAML.

## Validation

The offline runner used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nocardiopsis_sp_m1z45.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/nocardiopsis_sp_m1z45.yaml --out /private/tmp/nz45-strict.tsv`: exit 0; one record, zero errors. The actual TSV was read and was header-only.
- Bounded manual comparisons matched the entire pinned parent chain, rank, parent, code, attestation, path lock, scope and seed explanation. These do not replace the documented reproduction gate.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, provenance and corpus-wide history gates. Reproduction has no target selector; `--max-diffs` limits diagnostics, not scope. No invented focused reproduction gate or full-corpus success is claimed.
- Not applicable: `just validate-products` for curator-added graph nodes; none are present. NCBITaxon identifiers were checked at pinned and live authorities.
- Inline history passed schema/strict checks and matches scope. Ignored-inclusive content and filename searches found no target-specific external history entry requiring separate validation.
- Before web follow-up, the local `culturebotai-claw` runner executed `kg-microbe-sources imodulondb datasets`. All 28 rows were inspected; none covers Nocardiopsis. No applicable transcriptomic query was found, and this absence is not negative biological evidence.

## Identity and Grounding

The pinned backbone `data/raw/ncbitaxon_taxa.tsv:221971` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31439` agree on the sole name and exact identifier. The unique path-lock row is `data/taxa/PATHS.tsv:14462`; `curation/seed_scope.tsv:322246` supplies the one-source inclusion rationale.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035262&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035262) agree on the active placeholder, species rank and lineage. The root-first chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Streptosporangiales, Nocardiopsidaceae, Nocardiopsis and unclassified Nocardiopsis. All ten stored ancestor IDs, names and ranks match pinned rows, and live Datasets includes root. Exact pinned type-material, merged-ID and dropped checks found no target row; there is no immediate child in the backbone.

The inspected [LPSN Nocardiopsis page](https://lpsn.dsmz.de/genus/nocardiopsis), record 516184, treats the genus as validly published with N. dassonvillei as its type species. Its child listing and whole-page M1Z45 search supply no formal target name or deposit identity. NCBI species rank does not itself establish a valid binomial, and genus risk annotations or neighboring species' deposits cannot be inherited.

## Evidence

The sole attestation is one `NAME` assertion from `NCBITAXON`, with exact ID/label and snapshot date 2026-09-13. Its unit is not a biological isolate or genome count. The `seed_from_sources` `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` matches the maintained scope explanation. This review does not change that lifecycle.

Complete metadata for [JF729477.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729477.1), UID 334086853, identify a 1,415-nt partial 16S rRNA sequence, strain M1Z45, exact taxon 1035262, and seagrass isolation source. W. Chen submitted it on 25 March 2011; creation and update dates are 31 May and 3 June 2011. References are an unpublished comparative seagrass study and direct submission, with no PMID or DOI. No culture deposit, BioSample, BioProject, assembly, source-country qualifier or host species is supplied. The submitter's institutional address is not collection-locality evidence. Genomic-DNA provenance does not turn a partial marker into an assembly; bases were not analyzed.

The publisher PDF of [Wu et al., DOI:10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-full-text-pdf/2A88A4617354) explicitly pairs M1Z45 with JF729477 on printed page 88. Methods identify Thalassia hemprichii from Nancun Port, China, October 2010. Relevant methods/results were read, and Figure 1 and Table 2 were visually inspected. Table 2 reports N. composta as the most similar published species at 97.52%, with positive PKS-I, PKS-II and NRPS PCR screens. The discussion treats M1Z45 as a possible novel species, not a formally named one. Figure 1 instead places the separate M1Z45 tip beside a comparator printed as Nocardiopsis trehalos, AF105972. Preserve these distinct source presentations; neither comparator supplies exact species, strain or deposit identity. The PCR observations establish neither complete biosynthetic clusters nor demonstrated antimicrobial activity.

Secondary-review search results were used only to locate the primary paper, not to replace its comparator language with species equivalence. Bounded exact label/designation/accession searches supplied no additional inspected deposit or genome bridge.

## Completeness

The identifier, full label, slug and bounded designation pattern `\bM1Z[- _]?45\b` were searched using `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed source files were included. All ten matching rows were inspected in complete source-native metadata or TSV form: three target rows and seven numeric false matches. Five source-level `SOURCE.json` files and ignored-inclusive history filenames were checked separately.

A second compressed JF729477 search over the same ten roots, plus separate source-metadata and history-filename checks, found no match. This is bounded snapshot evidence, not worldwide absence or an exhaustive search of every ignored directory.

Exact checks of `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` and `bactotraits_taxa.tsv` found no target row. No pinned descendants can contribute BacDive entries. Zero strains therefore matches the own-plus-descendant rule, rather than denying the submitted laboratory isolate.

Live exact, non-expanding NCBI queries returned zero Assembly records and one nucleotide record. Assembly reported the taxid phrase as not found; that is an index limit, not proof that no genome exists anywhere. The existing CAFI-backed normalizer returned no eligible culture key for M1Z45, M1Z-45 or M1Z 45. Bare isolate names, related taxa and marker similarity are not deposit/genome join keys.

No consequential required omission was established. Literature enrichment is optional for this source-attested seeded record; it should not be achieved by inventing exact nomenclature, deposit, genome or phenotype claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the assertions actually stored. The pass is bounded to inspected sources and is not a full-corpus reproduction certificate. The paper's different comparator presentations are retained as source context, not a defect in this placeholder record.

## Recommended Edits

None required. Preserve the exact NCBI placeholder, name-attestation unit, zero BacDive strain count and seeded lifecycle. Do not replace the label with N. composta or the tree comparator, or import their type deposits or genomes.

Any future explicit deposit/genome bridge should enter maintained source acquisition/extraction and `src/taxonmech/seed.py`. Literature enrichment would require supported maintained inputs or a tested curator-owned overlay; do not patch generated YAML.

## Follow-up Checks

For proposed literature enrichment, preserve the exact M1Z45/JF729477 link and distinguish PCR screens, similarity comparisons and possible novelty from species naming or biochemical activity. Resolve the table/tree comparator difference before making a precise taxonomic interpretation.

Require an eligible whole culture accession and explicit source-specific deposit/sequence chain for genome associations. After an authorized maintained-input change, regenerate through the validated writer, rerun this target's schema/strict checks and full `just verify-corpus` and `just qc`.

## Additional Notes

The seven numeric false matches are separate source assertions:

- Four Parabacteroides distasonis assertions, taxid 823, strain RTP21230st1_D10_RTP21230_210325, SAMN41035262, GCA/GCF_040924565.1 and BV-BRC 823.5231: `data/catalog/ncbi_genbank-0037.jsonl.gz:20832`, `data/bvbrc/bvbrc-0027.jsonl.gz:26400`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19978`, `data/catalog/gtdb_genomes-0001.jsonl.gz:28798`.
- One Campylobacter jejuni assertion, taxid 197, PNUSAC013530, GCA_010352625.1 and SAMN13337914 at `data/catalog/ncbi_genbank-0009.jsonl.gz:6465`; assembly digits do not establish taxon identity.
- One Staphylococcus aureus assertion, taxid 1280, isolate 1035262, GCA_031876795.1 and SAMEA113541661 at `data/catalog/ncbi_genbank-0029.jsonl.gz:31056`; this isolate label is not NCBITaxon:1035262.
- One ATB M. tuberculosis assertion, SAMEA3558795, ERR1035262, ERZ9334371 at `data/catalog/allthebacteria.tsv.xz:569732`. Its FASTA is available and filters pass, but its source organism/run chain does not concern M1Z45.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Ignored-inclusive prior-report filename searches found no report for this stem before writing. The complete YAML was reread byte-unchanged. Only this new report was written in the repository; diagnostics and publisher-PDF inspection used temporary storage. No generated record, history, lifecycle, site, Git or GitHub state changed, and no Eukaryota record was reopened.

