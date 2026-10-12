# YAML Record Review: Lachnospiraceae bacterium 3F21C

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lachnospiraceae_bacterium_3f21c.yaml`
- Started UTC: 2026-10-06T02:07:51Z
- Finished UTC: 2026-10-06T02:11:45Z
- Verdict: pass

## Target

Read the entire 51-line generated `TaxonRecord` for `NCBITaxon:1034925`, Lachnospiraceae bacterium 3F21C. It carries `SPECIES` rank, `BACTERIA` domain, parent `NCBITaxon:186928` (unclassified Lachnospiraceae), nine root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It represents zero BacDive strains, one NCBITAXON NAME assertion from snapshot `2026-09-13`, and an inline `SEEDED_FROM_SOURCES` event dated `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strains, evidence and causal graphs are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/lachnospiraceae_bacterium_3f21c.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/lachnospiraceae_bacterium_3f21c.yaml --out /private/tmp/f21c-validation.tsv`: exit 0, one file, zero ERROR rows. Read the complete header-only TSV.
- Structured checks read the complete target backbone row, reconstructed every ancestor ID/label/rank, and verified the unique PATHS row, scope reason, attestation and inline event. A complete backbone scan found no children. These are bounded source comparisons, not full-corpus reproduction.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. Seven supplementary source inventories also returned no exact-ID match.
- Read complete live NCBI Taxonomy EFetch/Datasets responses, exact Assembly/Nuccore search responses and the full marker metadata, references and feature annotations. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. These full gates are outside this bounded report-only review. Inline-event inspection is not history-schema validation.
- `just validate-products` and iModulonDB were not applicable without curator-added graph groundings, genes, regulators, modules or transcriptomic assertions. No LPSN/GTDB assertion required an authority-page check.

## Identity and Grounding

The complete `data/raw/ncbitaxon_taxa.tsv:221753` row agrees with the YAML. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034925&retmode=xml) confirms the exact identifier, label, species rank, parent, bacterial division and genetic code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034925) confirms all nine ordered ancestor IDs, including root.

The root-first chain is root, cellular organisms, Bacteria, Bacillati, Bacillota, Clostridia, Lachnospirales, Lachnospiraceae and unclassified Lachnospiraceae. Every label and rank agrees with the pinned backbone and dedicated live taxonomy. The marker's abbreviated GenBank taxonomy ends at the family; this does not justify deleting the final unclassified intermediate.

`data/taxa/PATHS.tsv:14224` uniquely maps this ID to the target slug; `curation/seed_scope.tsv:322055` gives its one-source inclusion reason. The full scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31156` identifies the same taxon. No alternate name is supplied by the inspected taxonomy evidence. Species rank for this provisional isolate-labelled entry does not establish formal nomenclatural validity, membership in a named genus, or identity with another isolate.

## Evidence

The source identifier, label, snapshot, assertion count of one and NAME unit match the inventory. This is an identity and provenance record; it does not assert a genome, culture deposit, phenotype or mechanism. The name count is not a strain or genome count.

Exact Nuccore search returned UID 333973513. Complete [JF781301.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF781301.1) identify a 1,404-base 16S rRNA fragment, partial at both ends, for strain 3F21C and `taxon:1034925`. Source qualifiers describe collection from the rumen of a grazing cow in Uruguay in 2007, with bovine host and collector Martin Fraga. There is no culture-collection qualifier, BioSample, BioProject or assembly link in this metadata. A bare strain designation and marker accession do not establish a deposited-culture/genome chain.

The two marker references are a 6 April 2011 direct submission by Perelmuter, Zunino and Fraga, and an in-press Annals of Microbiology paper. The [publisher page](https://link.springer.com/article/10.1007/s13213-013-0753-3) verifies the latter's title and seven authors, DOI `10.1007/s13213-013-0753-3`, online publication in November 2013 and 2014 volume 64, pages 1149-1156. Its inspected abstract uses the shorter label 21C for an in-vitro fermentation treatment. Subscription-only methods/results were not inspected; neither a formal alias nor organism-wide probiotic efficacy is inferred from that abstract.

The inspected methods, results and discussion of [Fraga et al.'s Veterinaria study, preserved by INIA](https://inia.uy/sites/default/files/publications/2024-10/teriana-ruminal-de-un-bovino-a-pastoreo-mediante-tecnicas-clasicas-e-independientes-del-cultivo.html) describe cultured rumen isolates and explicitly mention 3F21C in the discussion. The results instead print 4F21C. This unresolved text discrepancy is not an established alternate name. Family-level similarity to 3F22C does not merge their identities. Older Clostridiales/Firmicutes terminology in the study does not override the carried current NCBI lineage. Figure images and tables were not inspected, and no isolate-specific mechanism is imported from community-level results.

Exact Assembly search returned zero, with a phrase-not-found warning for `txid1034925[Organism:noexp]`. This is a bounded query result, not proof that no genome exists under another identifier or classification.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed/hidden files and excluding `SOURCE.json` manifests. Searching the taxon-ID digits, full label and slug returned 48 lines. Backbone and scope were read structurally; all 26 remaining native JSON objects and 20 complete header-aware ATB rows were read. Reconciliation found no unread or truncated candidates.

Three rows identify 3F21C: backbone, scope and scientific name. The other 45 are unrelated numeric matches:

- Four entries concern Escherichia coli PNUSAE018551: BV-BRC `562.36430`, current/replaced `GCA_003753505.2`/`.1`, sample `SAMN10349251`, and ATB analysis `ERZ9092522`. They identify taxon 562 and project `PRJNA218110`.
- Twenty-one entries are BV-BRC, GenBank and ATB assertions for seven Salmonella enterica isolates with samples `SAMN10349253` through `SAMN10349259`, taxon 28901 and project `PRJNA230403`. Two additional GOLD project rows identify PNUSAS059282 (`Gp0379925`, `Go0495871`) and PNUSAS059185 (`Gp0379936`, `Go0495882`). A sylph Salmonella houtenae classification on one ATB row is still not 3F21C evidence.
- GenBank `GCA_041034925.1` identifies Klebsiella pneumoniae zj02085; `GCA_021034925.1` identifies E. coli PP1-1. Neither identifies the target.
- GenBank `GCA_051034925.1` and the suppressed RefSeq `GCF_051034925.1` identify Vibrio parahaemolyticus VP20072, taxon 670, sample `SAMN46338806`.
- `GCA_948610555.1` identifies uncultured Anaeroplasmataceae bacterium MGBC166093, taxon 658266. Its matching number is an ungapped genome size, not a taxon identifier.
- `GCA_027161985.1` identifies Staphylococcus aureus 83280037, taxon 1280, sample `SAMEA1034925`; that sample's ATB row names S. aureus, analysis `ERZ3070326`, run `ERR086098`.
- An ATB row names Mycobacterium tuberculosis, sample `SAMEA3558458`, analysis `ERZ3501231`, run `ERR1034925`.
- Ten ATB rows name Shigella sonnei samples `SAMEA110349250` through `SAMEA110349259`, with E. coli sylph classifications, not Lachnospiraceae.

A second ignored-inclusive scan of the same ten roots for `JF781301|3[ -]?F[ -]?21[ -]?C` returned the three target rows plus 74 ATB rows. Every additional row was read in full. Structured reconciliation proves all 74 matches occur only inside `assembly_seqkit_sum`, not identity fields. Six have non-PASS HQ filters; none was rejected merely for being non-HQ. A checksum substring cannot link an assembly to a strain.

Exact-ID scans of the complete BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Within these bounded retained sources, no supported missing culture-deposit/genome association was established. Zero represented strains describes BacDive inventory coverage, not biological absence of the cultured isolate. Shared accession digits do not prove identity; a genuine shared BioSample alone would still not prove assembly equivalence.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No required missing synonym, nomenclature, mapping, evidence or causal graph was established. Optional literature enrichment is not required for this taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, carried lineage, source-count semantics, provenance and seeded status are supported. The literature-label ambiguity limits optional enrichment, but does not contradict the YAML's exact NCBI identity.

## Recommended Edits

None. Preserve the generated YAML and `SEEDED` status.

Future primary taxonomy corrections belong at NCBI, followed by the pin in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization changes belong in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope changes belong in `curation/seed_scope.tsv`. A study-context extension requires a maintained input and exact-target evidence. Do not hand-edit generated YAML or promote a marker to a genome.

## Follow-up Checks

No blocking follow-up remains. Before adding phenotype, alias or deposit assertions, inspect the complete experimental methods and resolve the 3F21C/4F21C/21C designations against explicit accession or author-supplied identity evidence. Any future genome candidate requires complete source-native inspection and a supported strain/deposit/sample/genome chain. After authorized implementation, rerun focused schema/strict validation and the documented reproduction, provenance, history and relevant full gates. Independent sequence placement was not performed.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, existing sole worktree. The other session was reported closed; no additional worktree was created. This review adds only this new report, with diagnostics under `/private/tmp`. Records, inventories, scope, history, statuses, prior reports and generated pages were preserved. No commit, GitHub mutation, external contact or paid research occurred. Eukaryota was left untouched.
