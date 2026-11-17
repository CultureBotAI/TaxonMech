# YAML Record Review: Mycobacterium sp. G2Z43

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mycobacterium_sp_g2z43.yaml`
- Started UTC: 2026-10-06T18:28:23Z
- Finished UTC: 2026-10-06T18:34:19Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1035260`, Mycobacterium sp. G2Z43, was read before judgement. It is a species-rank NCBI placeholder in Bacteria, with parent `NCBITaxon:2642494`, genetic code 11, `EXACT` grounding and `SEEDED` lifecycle. It carries ten lineage entries, zero BacDive strains, one NCBITAXON name attestation and one seed event. It asserts no synonyms, LPSN nomenclature, GTDB mappings, culture deposits, genomes, phenotype evidence or causal edges.

The generated record is owned by maintained scope and pinned source inventories. Future corrections belong in `curation/seed_scope.tsv`, upstream source acquisition/extraction or `src/taxonmech/seed.py`, as appropriate, not in this YAML.

## Validation

The offline project runner used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/mycobacterium_sp_g2z43.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/mycobacterium_sp_g2z43.yaml --out /private/tmp/mg2-strict.tsv`: exit 0; one record, zero errors. The actual diagnostic TSV was read and was header-only.
- Bounded read-only source comparisons matched the complete pinned lineage, rank, parent, code, name attestation, path lock, scope and scope-derived seed-event text. These are manual source checks, not a focused reproduction validator.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, provenance and corpus-wide history gates. The reproduction script has no target selector; `--max-diffs` limits diagnostics, not scope. No full-corpus success or invented focused gate is claimed.
- Not applicable: `just validate-products` for curator-added ontology graph nodes; none are present. NCBITaxon identity was checked against pinned and live authorities.
- Inline history passed schema/strict validation and matched the scope explanation. Ignored-inclusive content and history-filename searches found no target-specific external history entry requiring separate validation.
- The local `culturebotai-claw` runner executed `kg-microbe-sources imodulondb datasets` before web follow-up. All 28 dataset rows were inspected. The listed `m_tuberculosis/modulome` dataset concerns another species, not G2Z43; no applicable target dataset was found. This is not negative biological evidence.

## Identity and Grounding

The pinned backbone row `data/raw/ncbitaxon_taxa.tsv:221969` and scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31437` agree on the exact identifier and sole name. The path lock `data/taxa/PATHS.tsv:14460` uniquely resolves this file; `curation/seed_scope.tsv:322244` supplies its one-source inclusion rationale.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035260&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035260) confirm the active species-rank placeholder. The root-first lineage is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Mycobacteriales, Mycobacteriaceae, Mycobacterium and unclassified Mycobacterium. All ten stored ancestor IDs, labels and ranks match the pinned inventory, and the live chain agrees. Exact pinned type-material, merged-ID and dropped-table checks found no target row; the backbone contains no immediate child.

The inspected nomenclatural portion of the [LPSN Mycobacterium genus page](https://lpsn.dsmz.de/genus/mycobacterium) describes the validly published genus and its type species M. tuberculosis. A whole-page G2Z43 search found no match. This provides no formal species-name or deposit bridge for the placeholder. Genus-level synonymy and risk annotations must not be inherited by G2Z43, and NCBI species rank is not evidence of a validly published binomial.

## Evidence

The single attestation is one `NAME` assertion from `NCBITAXON`, with the exact identifier and label and snapshot date 2026-09-13. That count does not represent biological isolates or genomes. The `SEEDED_FROM_SOURCES` event by `seed_from_sources` at `2026-09-13T17:54:04Z` matches the scope text. This read-only review does not promote the stored lifecycle.

Full metadata for [JF729474.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729474.1), UID 334086850, identify a 1,388-nt partial 16S rRNA sequence, strain G2Z43, exact taxon 1035260, and seagrass isolation source. W. Chen submitted it on 25 March 2011; creation and update dates are 31 May and 3 June 2011. The references are an unpublished comparative seagrass study and a direct submission, without PMID or DOI. No culture deposit, BioSample, BioProject, assembly, geographic source qualifier or host species is supplied. The submitter's institutional address is not a collection locality, and the partial marker is not a genome assembly. Sequence bases were not analyzed.

The publisher PDF of [Wu et al., DOI:10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-full-text-pdf/2A88A4617354) explicitly links G2Z43 to JF729474 on printed page 88. Its methods identify Thalassia hemprichii collected at Nancun Port, China, in October 2010. Figure 1 and Table 2 were visually inspected. The G2Z43 row reports M. holsaticum as the closest published species at 98.70% similarity and PCR results PKS-I negative, PKS-II positive and NRPS positive. These are bounded marker-comparison and PCR observations, not species equivalence, assembled biosynthetic clusters or demonstrated antimicrobial activity. G2Z43 is not among the four isolates singled out as possible novel species.

A later [Minas-cheese study, DOI:10.11606/issn.1678-4456.bjvras.2018.146525](https://revistas.usp.br/bjvras/article/download/e146525/150058) was a search lead. Its inspected methods/results describe study sequences compared with GenBank references; its own reported accessions are KY522830-KY522837, KY522841-KY522845, KY522849, KY522850 and KY522853. The possible JF729474/GZ243 label occurs in an image-based figure, not the searchable text. Screenshot attempts and direct PDF retrieval failed, including a connection timeout. That exact figure label remains unverified and is not adopted as a synonym, source of isolation, phenotype or strain identity. No cheese, Brazilian locality or pathogenicity claim is transferred to G2Z43.

## Completeness

The identifier, full label, slug and bounded designation pattern `\bG2Z[- _]?43\b` were searched with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The search includes ignored, hidden and compressed source files. All twelve matched rows were inspected in full source-native metadata or TSV form: three target rows and nine numeric false matches. Five source-level `SOURCE.json` files and ignored-inclusive history filenames were checked separately.

A second search for JF729474 and the bounded, unverified figure-label lead GZ243 covered the same ten roots and separate source metadata/history filenames. It returned one GenBank catalog row, inspected in full: Streptococcus agalactiae strain GZ243, taxid 1311, GCA_047386825.1, SAMN38514615, PRJNA1046429, at `data/catalog/ncbi_genbank-0043.jsonl.gz:34896`. It is not this Mycobacterium isolate. No JF729474 source-row bridge was found within those bounded snapshot roots; this is not a worldwide absence claim.

Exact transformed-table checks of `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` and `bactotraits_taxa.tsv` found no target rows. With no pinned descendants, zero BacDive strains agrees with the seeder's own-plus-descendant rule. It does not deny the laboratory isolate documented by the marker submission.

Live exact, non-expanding NCBI queries returned zero Assembly records and one nucleotide record. Assembly reported the taxid phrase as not found; that is bounded index evidence. The existing CAFI-backed normalizer returned no eligible culture key for G2Z43, G2Z-43, G2Z 43 or GZ243. Bare isolate strings and phylogenetic proximity cannot establish a culture-deposit-genome chain.

No consequential missing required representation was established. Literature enrichment remains optional for this source-attested seeded record. The inspected primary study supports bounded additional context, not an obligation to fill nomenclature, deposit, genome or phenotype slots through inference.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the assertions actually stored. This pass is limited to the inspected sources and is not a full-corpus reproducibility certificate. The later paper's image-based label remains an unverified optional lead, not a blocker for the existing record.

## Recommended Edits

None required. Preserve the NCBI placeholder, one-name source unit, zero BacDive strain count and seeded lifecycle. Do not rename G2Z43 to M. holsaticum or import another Mycobacterium species' datasets, safety annotations or culture deposits.

Future explicit source-backed enrichment belongs in maintained acquisition/extraction inputs and `src/taxonmech/seed.py`; a curator-owned literature overlay would require supported maintained inputs and tests. Do not patch the generated YAML to add these observations.

## Follow-up Checks

Before using the later study, retrieve and visually inspect its actual Figure 1, determine whether JF729474 is a reference or study isolate, and resolve any designation discrepancy against the accession authority. Do not add GZ243 as a synonym from the unverified search lead.

For any proposed genome link, require an eligible whole culture accession and a source-specific sequence/deposit chain, preserving marker, taxon, sample, project and assembly distinctions. After an authorized maintained-input change, regenerate through the validated writer, rerun the target schema/strict validators and full `just verify-corpus` and `just qc`.

## Additional Notes

The nine initial numeric false matches are separate source assertions, not nine biological genomes:

- Four Parabacteroides distasonis assertions, taxid 823, strain RTP21002st1_D10_RTP21002_201210, sample SAMN41035260, GCA/GCF_040924585.1 and BV-BRC 823.5232: `data/catalog/ncbi_genbank-0037.jsonl.gz:20833`, `data/bvbrc/bvbrc-0027.jsonl.gz:26401`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19979` and `data/catalog/gtdb_genomes-0006.jsonl.gz:45395`.
- Two Mycobacterium tuberculosis assertions for run ERR1035260: BV-BRC 1773.18287 at `data/bvbrc/bvbrc-0006.jsonl.gz:6077`, and ATB sample SAMEA3558793, analysis ERZ9334366, at `data/catalog/allthebacteria.tsv.xz:569730`. The ATB row has an available FASTA and passing filters, but its organism and source chain are not G2Z43.
- Two Actinomycetota bacterium assertions, taxid 2900548, isolate UFOp-RE-20APR16-217, GCA_009704135.1, SAMN12745006, PRJNA449258: `data/catalog/gtdb_genomes-0007.jsonl.gz:36104` and `data/catalog/ncbi_genbank-0008.jsonl.gz:28181`. The matched digits are genome lengths; this freshwater genome is not the reviewed isolate.
- One Campylobacter jejuni assertion, taxid 197, strain PNUSAC013487, GCA_010352605.1, SAMN13337448, at `data/catalog/ncbi_genbank-0009.jsonl.gz:6464`.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. An ignored-inclusive prior-report filename search found no report for this stem before writing. The complete YAML was reread byte-unchanged. The review's only repository write is this new report; temporary diagnostics and existing publisher-PDF renderings were used for verification. No generated record, history, lifecycle, site, Git or GitHub state was changed. No Eukaryota record was reopened.

