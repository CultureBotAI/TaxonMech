# YAML Record Review: Mycobacterium sp. M1X69

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mycobacterium_sp_m1x69.yaml`
- Started UTC: 2026-10-06T18:36:21Z
- Finished UTC: 2026-10-06T18:38:44Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1035261`, Mycobacterium sp. M1X69, was read before judgement. It is a species-rank placeholder in Bacteria with parent `NCBITaxon:2642494`, genetic code 11, ten root-first lineage entries, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. It asserts no synonyms, nomenclature, taxonomy mappings, deposits, genomes, phenotype evidence or causal edges.

This YAML is generated from pinned inventories and maintained scope. Future corrections belong in `curation/seed_scope.tsv`, upstream acquisition/extraction or `src/taxonmech/seed.py`, as appropriate, not in the generated record.

## Validation

The project runner used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/mycobacterium_sp_m1x69.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/mycobacterium_sp_m1x69.yaml --out /private/tmp/mx69-strict.tsv`: exit 0; one record and zero errors. The actual TSV was read and was header-only.
- Bounded manual source comparisons matched the entire pinned lineage, rank, parent, code, attestation, path lock, scope and seed-event explanation. These are not a replacement for corpus reproduction.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, provenance and corpus-wide history gates. The reproduction script has no target selector; `--max-diffs` limits output, not scope. No invented focused gate or full-corpus pass is claimed.
- Not applicable: `just validate-products` for curator-added graph nodes; none are present. Taxonomic identifiers were checked against pinned and live authorities.
- Inline history passed schema/strict checks and matched scope. Ignored-inclusive content and filename searches found no target-specific external history entry requiring separate validation.
- Before open web follow-up, the local `culturebotai-claw` runner executed `kg-microbe-sources imodulondb datasets`. All 28 rows were inspected. `m_tuberculosis/modulome` belongs to another species; none covers M1X69. No target transcriptomic query was applicable, and this absence is not biological negative evidence.

## Identity and Grounding

The full pinned backbone row `data/raw/ncbitaxon_taxa.tsv:221970` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:31438` agree on the identifier and sole scientific name. The unique path-lock row is `data/taxa/PATHS.tsv:14461`; the maintained inclusion rationale is `curation/seed_scope.tsv:322245`.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035261&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035261) confirm the active name, species rank and parent. The root-first chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Mycobacteriales, Mycobacteriaceae, Mycobacterium and unclassified Mycobacterium. Every stored ancestor ID, label and rank agrees with the pinned backbone; live Datasets explicitly includes root. Exact checks found no pinned type-material, merged-ID or dropped row for this taxon and no immediate child.

The inspected nomenclatural portion of the [LPSN Mycobacterium page](https://lpsn.dsmz.de/genus/mycobacterium) concerns the valid genus and identifies M. tuberculosis as its type species. A whole-page M1X69 search found no match. It does not establish a formal binomial, type deposit or synonym for this placeholder. Genus-level synonymy and risk annotations must not be inherited by M1X69.

## Evidence

The sole attestation is one `NCBITAXON` `NAME` assertion with exact label/ID and snapshot date 2026-09-13. The count is not a biological strain or genome count. The `seed_from_sources` event at `2026-09-13T17:54:04Z` is `SEEDED_FROM_SOURCES`; its text agrees with maintained scope. The lifecycle remains unchanged.

Full metadata for [JF729478.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729478.1), UID 334086854, identify a 1,389-nt partial 16S rRNA sequence, strain M1X69, exact taxon 1035261 and seagrass isolation source. W. Chen submitted it on 25 March 2011; creation and update dates are 31 May and 3 June 2011. References are an unpublished comparative seagrass study and a direct submission, without PMID or DOI. No collection deposit, BioSample, BioProject, assembly, source-country qualifier or host species is supplied. The Chinese institutional address is not collection-locality evidence. Genomic-DNA provenance does not make a partial marker a genome assembly. Sequence bases were not analyzed.

A neighboring accession series is discussed in [Wu et al., DOI:10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-full-text-pdf/2A88A4617354). The available publisher PDF was searched across all eight pages for M1X69/JF729478 with no extracted-text match. The accession list, Figures 1 and 2, and Table 2 were also visually inspected; none supplied an exact target bridge. Sharing a submitter, generic source and accession series does not authorize transferring the paper's host species, locality, medium or PCR results. This rejected lead is not proof that no target publication exists.

Bounded exact designation, label and accession web searches yielded no additional inspected culture, genome or publication bridge. Search snippets, unrelated string matches and neighboring taxon pages were not used as target evidence.

## Completeness

Ignored and hidden files and compressed catalogs were included using `rg --no-ignore --hidden -n -z -i`. The identifier, full label, slug and bounded designation pattern `\bM1X[- _]?69\b` were searched across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 17 matched rows were inspected in full source-native metadata or TSV form: three target rows and fourteen numeric false matches. Five source-level `SOURCE.json` files and ignored-inclusive history filenames were checked separately.

A second compressed search for JF729478 across the same ten roots, plus separate source-metadata/history-filename checks, found no match. These are bounded snapshot searches, not claims about all external sources or every ignored directory.

Exact checks of `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` and `bactotraits_taxa.tsv` found no target rows. With no pinned descendants, zero strains agrees with the seeder's own-plus-descendant BacDive rule; it does not deny the submitted laboratory isolate.

Live exact, non-expanding NCBI searches returned zero Assembly records and one nucleotide record. Assembly reported the taxid phrase as not found; this is bounded index evidence, not worldwide genome absence. The existing CAFI-backed normalizer returned no eligible culture key for M1X69, M1X-69 or M1X 69. Bare designations, shared taxonomy and partial markers cannot establish strain-deposit-genome equivalence.

No consequential required gap was established. Optional literature evidence is not mandatory for this source-attested seeded record, and ungrounded nomenclature, phenotype, deposit and genome slots should remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored assertions. This pass is bounded to the inspected evidence, not a full-corpus reproducibility certificate. Publication linkage beyond the direct submission remains optional unresolved enrichment.

## Recommended Edits

None required. Preserve the placeholder, exact NCBI name attestation, zero BacDive count and seeded lifecycle.

Future explicit deposit/genome or literature evidence should enter through supported maintained inputs and source acquisition/extraction, then `src/taxonmech/seed.py`. A curator-owned literature overlay would need maintained support and tests. Do not manually patch this generated YAML or equate M1X69 with a named Mycobacterium species.

## Follow-up Checks

Require an exact M1X69/JF729478 bridge before attributing a publication's observations. Require an eligible whole culture accession and explicit source-specific deposit/sequence chain before adding genome associations; keep marker, sample, project, taxon and genome identities distinct.

After an authorized maintained-input change, regenerate through the validated writer, rerun target schema/strict checks and full `just verify-corpus` and `just qc`. No regeneration or lifecycle promotion occurred here.

## Additional Notes

The fourteen numeric false matches are separate source assertions, not fourteen biological genomes:

- Four Parabacteroides distasonis assertions, taxid 823, strain RTP21230st1_B10_RTP21230_210325, SAMN41035261, GCA/GCF_040924625.1 and BV-BRC 823.5234: `data/bvbrc/bvbrc-0027.jsonl.gz:26403`, `data/catalog/gtdb_genomes-0012.jsonl.gz:28209`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19981`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20835`.
- Two Mycobacterium tuberculosis assertions for run ERR1035261: BV-BRC 1773.18281 at `data/bvbrc/bvbrc-0006.jsonl.gz:6071`; ATB SAMEA3558794, ERZ9334370 at `data/catalog/allthebacteria.tsv.xz:569731`.
- Two uncultured Gammaproteobacteria bacterium assertions, NCBI taxid 86473, isolate SRP292972_co3_34, GCA_964576435.1 and SAMEA117287162, matching genome length 1035261: `data/catalog/ncbi_genbank-0063.jsonl.gz:32155` and `data/catalog/gtdb_genomes-0004.jsonl.gz:26407`. GTDB's different classification does not bridge this genome to M1X69.
- Three Burkholderia contaminans assertions, taxid 488447, LMG 23361, GCA/GCF_001758385.2 and SAMN05441496, matching length 10352616: `data/catalog/gtdb_genomes-0004.jsonl.gz:8633`, `data/catalog/ncbi_refseq-0001.jsonl.gz:7018`, `data/catalog/ncbi_genbank-0001.jsonl.gz:17906`.
- One Gammaproteobacteria bacterium assertion, taxid 1913989, isolate NOWI19-1_SAMN10351047_MAG_00000056, GCA_983015195.1 and SAMEA122307838, matching total length 1035261: `data/catalog/ncbi_genbank-0066.jsonl.gz:45179`.
- Two ATB SeqKit-sum substring matches: M. tuberculosis SAMEA7547864, ERR4814505, ERZ25379214 at `data/catalog/allthebacteria.tsv.xz:888607`; Neisseria gonorrhoeae SAMN10411800, SRR11904456, ERZ25505031 at `data/catalog/allthebacteria.tsv.xz:1509614`. All three inspected ATB rows have available FASTAs and passing filters, but none has a source chain to M1X69.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Ignored-inclusive prior-report filename searches found no report for this stem before writing. The complete target was reread byte-unchanged. Only this new report was written in the repository; diagnostics and existing PDF renderings used temporary storage. No YAML, history, lifecycle, generated site, Git or GitHub state changed, and no Eukaryota review was reopened.

