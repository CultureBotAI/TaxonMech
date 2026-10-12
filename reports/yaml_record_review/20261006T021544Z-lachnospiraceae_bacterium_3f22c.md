# YAML Record Review: Lachnospiraceae bacterium 3F22C

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lachnospiraceae_bacterium_3f22c.yaml`
- Started UTC: 2026-10-06T02:13:01Z
- Finished UTC: 2026-10-06T02:15:44Z
- Verdict: pass

## Target

Read all 51 lines of the generated `TaxonRecord` for `NCBITaxon:1034926`, Lachnospiraceae bacterium 3F22C. It has `SPECIES` rank, `BACTERIA` domain, parent `NCBITaxon:186928` (unclassified Lachnospiraceae), nine root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status and zero represented strains. Its sole source attestation is an NCBITAXON NAME assertion from snapshot `2026-09-13`. The inline `SEEDED_FROM_SOURCES` event is dated `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strain entries, evidence and graphs are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/lachnospiraceae_bacterium_3f22c.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/lachnospiraceae_bacterium_3f22c.yaml --out /private/tmp/f22c-validation.tsv`: exit 0, one file, zero ERROR rows. Read the complete header-only TSV.
- Structured comparisons checked the complete backbone row, every ancestor ID/label/rank, unique PATHS entry, scope reason, source attestation and inline event. A full backbone scan found no children. This bounded comparison does not substitute for corpus reproduction.
- Exact-ID scans found no matching row in `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` or `data/raw/dropped.tsv`; seven supplementary source inventories also returned no exact-ID row.
- Read complete live NCBI Taxonomy EFetch/Datasets responses, exact non-expanding Assembly/Nuccore search responses, and full nucleotide metadata, references and feature annotations. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget and vendored synchronization. These full gates are outside this bounded report-only review. Inline-event inspection is not history-schema validation.
- `just validate-products` and iModulonDB were not applicable without curator-added graph grounding, genes, regulators, modules or transcriptomic claims. No LPSN/GTDB assertion required an authority-page check.

## Identity and Grounding

The complete `data/raw/ncbitaxon_taxa.tsv:221754` row matches the record. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034926&retmode=xml) confirms exact identifier, label, species rank, parent, bacterial division and genetic code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034926) confirms all nine ordered ancestors, including root.

The root-first chain is root, cellular organisms, Bacteria, Bacillati, Bacillota, Clostridia, Lachnospirales, Lachnospiraceae and unclassified Lachnospiraceae. Ancestor labels and ranks agree with the pinned backbone and dedicated live taxonomy. The marker's abbreviated GenBank taxonomy ends at the family; that omission does not invalidate the unclassified intermediate in the dedicated taxonomy chain.

`data/taxa/PATHS.tsv:14225` uniquely maps this identifier to the target slug; `curation/seed_scope.tsv:322056` supplies its one-source inclusion reason. The complete object at `data/catalog/ncbi_names-0005.jsonl.gz:31157` names this same taxon. No alternate target name is supplied by the inspected taxonomy evidence. NCBI species rank for a provisional isolate-labelled entry does not establish formal nomenclatural validity. 3F21C is a separately identified isolate, not an inferred synonym.

## Evidence

The attestation identifier, label, snapshot, assertion count of one and NAME unit match the inventory. The YAML asserts identity, lineage and provenance, not a culture deposit, assembly, phenotype or mechanism. One source name is not one genome or one BacDive strain.

Exact Nuccore search returned UID 333973514. Full [JF781302.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF781302.1) identify a 1,398-base 16S rRNA fragment, partial at both ends, for strain 3F22C with `taxon:1034926`. Qualifiers describe rumen isolation from a grazing cow in Uruguay in 2007, bovine host and collector Martin Fraga. There is no culture-collection qualifier, BioSample, BioProject or assembly link. The marker and bare strain designation do not establish a deposited-culture/genome chain.

The two references are a 6 April 2011 direct submission by Perelmuter, Zunino and Fraga, and an in-press Annals of Microbiology paper. The inspected [publisher page](https://link.springer.com/article/10.1007/s13213-013-0753-3) verifies its matching title/authors, DOI `10.1007/s13213-013-0753-3`, November 2013 online publication and 2014 volume 64, pages 1149-1156. The abstract's specific 21C treatment result cannot be transferred to 3F22C. Subscription-only methods/results were not inspected, so no target-specific fermentation mechanism or efficacy is inferred.

The inspected [Veterinaria study preserved by INIA](https://inia.uy/sites/default/files/publications/2024-10/teriana-ruminal-de-un-bovino-a-pastoreo-mediante-tecnicas-clasicas-e-independientes-del-cultivo.html) explicitly mentions 3F22C among cultured rumen isolates and discusses its family-level similarity to other isolates. This does not establish culture-deposit identity, genome equivalence or formal new-genus nomenclature. Its older taxonomy terminology does not override current NCBI lineage. Figure images and tables were not inspected; community results were not promoted to isolate-specific claims.

Exact Assembly search returned zero with a phrase-not-found warning for `txid1034926[Organism:noexp]`. This bounded result does not prove genome absence under every other identifier or classification.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including hidden/compressed files and excluding `SOURCE.json` manifests. The ID digits, full label and slug yielded 40 lines. Backbone and scope were read structurally; all 18 remaining native JSON objects and 20 complete header-aware ATB rows were read. Reconciliation found no unread or truncated candidate.

Three rows identify the target: backbone, scope and scientific name. The other 37 are unrelated numeric matches:

- Twelve entries are BV-BRC, GenBank and ATB assertions for Salmonella enterica PNUSAS059538, PNUSAS059536, PNUSAS059284 and PNUSAS059283, with samples `SAMN10349260`, `SAMN10349262`, `SAMN10349263` and `SAMN10349264`. Their GenBank accessions are `GCA_003770305.1`, `GCA_003754905.1`, `GCA_003760685.1` and `GCA_003768785.1`, respectively. All identify taxon 28901 and project `PRJNA230403`. An additional GOLD row identifies PNUSAS059284 through `Gp0379924`, `Go0495870` and `SAMN10349263`.
- Three entries concern Escherichia coli PNUSAE017634: BV-BRC `562.36452`, `GCA_003754925.1`, sample `SAMN10349261`, project `PRJNA218110`, and ATB analysis `ERZ9092539`. Two more concern E. coli OH-18-20225-2-E: `GCA_013046665.1`, sample `SAMN10349269`, project `PRJNA338676`, and ATB `ERZ9092548`.
- Four entries are GenBank/ATB assertions for Salmonella enterica Z-172 (`GCA_005578815.1`, `SAMN10349265`, `PRJNA377900`, `ERZ9092544`) and OH-18-21628 (`GCA_005578835.1`, `SAMN10349268`, `PRJNA338674`, `ERZ9092546`).
- BV-BRC `1773.20377` identifies Mycobacterium tuberculosis ERR1034926, taxon 1773. Its ATB run row names sample `SAMEA3558459`, analysis `ERZ3501248` and run `ERR1034926`.
- `GCA_010349265.1` identifies Campylobacter jejuni FSIS11926480, taxon 197, sample `SAMN13447821`, project `PRJNA287430`.
- `GCA_027159455.1` identifies Staphylococcus aureus 9-183-193, taxon 1280, sample `SAMEA1034926`, project `PRJNA514245`. Its ATB row names S. aureus, analysis `ERZ3070333`, run `ERR086140`.
- Ten ATB rows name Shigella sonnei samples `SAMEA110349260` through `SAMEA110349269`, with E. coli sylph classifications, not Lachnospiraceae.

These complete native rows establish unrelated identities, not merely low-scoring search hits. Shared digits do not link strains, samples or assemblies; a genuine shared BioSample would still not establish assembly equivalence.

A second ignored-inclusive scan of the same ten roots used `JF781302|(^|[^A-Za-z0-9])3[ -]?F[ -]?22[ -]?C([^A-Za-z0-9]|$)`. It returned only the same three target rows. Alphanumeric boundaries keep incidental checksum substrings from being treated as strain tokens. Exact-ID scans of the complete BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Within these retained sources, no supported missing culture-deposit/genome association was established. Zero represented strains describes BacDive inventory coverage, not biological absence of the isolate.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No required missing synonym, nomenclature, mapping, evidence or causal graph was established. Optional study-context enrichment is not a condition of passing this taxonomy-only record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record's exact identity, carried lineage, source-count semantics, provenance and seeded status are supported. The marker and unrelated catalog rows do not establish an omitted genome or culture deposit.

## Recommended Edits

None. Preserve the generated YAML and `SEEDED` status.

Future primary taxonomy corrections belong at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization belongs in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope changes belong in `curation/seed_scope.tsv`. Any literature extension needs a maintained input and exact-target evidence. Do not hand-edit generated YAML or count the marker as a genome.

## Follow-up Checks

No blocking follow-up remains. A future genome/deposit candidate requires full native evidence and an explicit strain/deposit/sample/genome linkage chain. Optional phenotype enrichment needs the full experimental text and target-specific results, without transferring 21C findings to 3F22C. After authorized implementation, rerun focused schema/strict checks and the documented reproduction, provenance, history and relevant full gates. Independent marker-sequence placement was outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, existing sole worktree. The other session was reported closed; no new worktree was created. This target review adds only this report; diagnostics are under `/private/tmp`. Records, inventories, scope, history, statuses, prior reports and generated pages were preserved. No commit, GitHub mutation, external contact or paid research occurred. Eukaryota was left untouched.
