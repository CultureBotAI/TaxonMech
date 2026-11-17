# YAML Record Review: Sphingomonas sp. LT4CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sphingomonas_sp_lt4cd.yaml`
- Started UTC: 2026-10-06T01:53:08Z
- Finished UTC: 2026-10-06T01:55:13Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1034922`, Sphingomonas sp. LT4CD. It is a `SPECIES` in `BACTERIA`, parent `NCBITaxon:196159` (unclassified Sphingomonas), with ten root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, zero represented strains, one NCBITAXON NAME assertion from snapshot `2026-09-13`, and one inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strains, evidence, discussions and causal graphs are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/sphingomonas_sp_lt4cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/sphingomonas_sp_lt4cd.yaml --out /private/tmp/lt4cd-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the full header-only TSV.
- Structured comparisons checked the complete target backbone and scope rows, every ancestor ID/label/rank, unique PATHS entry, NCBI attestation and inline seed-event description. The complete backbone scan returned no children. These bounded checks are not full-corpus reproduction.
- Exact-ID scans of complete `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` returned no matching row. Seven supplementary source inventories likewise returned no exact target-ID match.
- Read complete live NCBI Taxonomy EFetch/Datasets responses, exact non-expanding Assembly/Nuccore search responses, and full nucleotide metadata, references and feature annotations. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. These full gates are outside this bounded report-only review. Inline-event inspection is not history-schema validation.
- `just validate-products` and iModulonDB were not applicable without curator-added graph grounding, genes, regulators, modules or transcriptomic assertions. No LPSN/GTDB assertion required an authority-page check.

## Identity and Grounding

The complete `data/raw/ncbitaxon_taxa.tsv:221750` row matches the YAML. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034922&retmode=xml) confirms exact ID/label, species rank, parent, bacterial division and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034922) confirms all ten ordered ancestor IDs, including root.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Sphingomonadales, Sphingomonadaceae, Sphingomonas and unclassified Sphingomonas. Labels and ranks agree with the pinned backbone and dedicated taxonomy evidence. The marker's abbreviated GenBank taxonomy ends at the genus; it does not override the full parent chain.

`data/taxa/PATHS.tsv:14221` uniquely maps the target to `sphingomonas_sp_lt4cd`; `curation/seed_scope.tsv:322052` supplies the one-source inclusion rule. The complete scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31153` identifies the same taxon. No alternate target name is supplied by the inspected taxonomy evidence. Species rank for this provisional isolate-labelled entry does not establish formal nomenclatural validity or equivalence with another Sphingomonas isolate.

## Evidence

Source ID, label, snapshot, count of one and NAME unit agree with the inventory. The YAML asserts identity, carried lineage and provenance, not a phenotype, genome, culture deposit, medium or mechanism. A name assertion is not a biological strain or genome count.

Exact Nuccore search returned UID 333496486. The full [JF778655.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF778655.1) describe an 891-base 16S rRNA fragment, partial at both ends, with Sphingomonas sp. LT4CD, strain LT4CD, freshwater-lake isolation source and `taxon:1034922`. The sole reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter's Bellerophon-screening comment was not independently tested. No culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID appears in this metadata. A marker and bare strain designation do not establish a deposited-culture/genome chain.

The inspected main text of [Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4) includes JF778655 within JF778652-JF778667. The accession range and matching authors support a Lake Tawani(P), East Antarctica study association, not isolate-specific physiology, growth optima or deposit identity. Supplements and figure images were not inspected.

Exact Assembly search returned zero with a phrase-not-found warning for `txid1034922[Organism:noexp]`. This bounded result does not prove genome absence under other identifiers or classifications.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including hidden/compressed files and excluding `SOURCE.json` manifests. The ID digits, full label and slug yielded 30 lines. Backbone and scope were read structurally; all eleven remaining native JSON objects and seventeen complete header-aware AllTheBacteria rows were read. Reconciliation found no unread or truncated candidate.

Three rows identify LT4CD: backbone, scope and scientific name. The other 27 are unrelated numeric matches:

- Four objects describe Escherichia coli PNUSAE017611: BV-BRC `562.36515`, current `GCA_003760195.2`, replaced `GCA_003760195.1`, and ATB analysis `ERZ9092498`. The genome metadata identify taxon 562, sample `SAMN10349220`, project `PRJNA218110`.
- E. coli OSF087066 has GenBank `GCA_012068955.1`, taxon 562, sample `SAMN10349225`, project `PRJNA230969`, and ATB analysis `ERZ9092497`.
- Listeria monocytogenes PNUSAL004489 has BV-BRC `1639.5797`, GenBank `GCA_003767845.1`, taxon 1639, sample `SAMN10349227`, project `PRJNA212117`, and ATB analysis `ERZ9092496`. The ATB scientific name is L. monocytogenes and sylph species is L. monocytogenes_B, neither identifying LT4CD.
- GenBank `GCA_010349225.1` identifies Campylobacter jejuni PNUSAC013843, taxon 197, sample `SAMN13471355`, project `PRJNA239251`.
- GenBank `GCA_964863275.1` is a metagenome-derived Rickettsiales bacterium UBA1997 assembly, taxon 1951236, sample `SAMEA117461597`, project `PRJEB75477`. It matches the digits through its genome length of 1,034,922 bases, not its taxon ID.
- Staphylococcus aureus 83430188 has GenBank `GCA_027161825.1`, taxon 1280, sample `SAMEA1034922`, project `PRJNA514245`, and ATB analysis `ERZ3070329`, run `ERR086106`.
- BV-BRC `1773.20367` identifies Mycobacterium tuberculosis ERR1034922, taxon 1773. Its ATB run row identifies Mycobacterium tuberculosis sample `SAMEA3558455`, analysis `ERZ3501226`.
- Ten ATB rows identify Shigella sonnei samples `SAMEA110349220` through `SAMEA110349229`, with E. coli in the sylph species field. Neither classification is Sphingomonas.
- Two ATB rows match the ID digits inside SeqKit sums: Salmonella enterica subsp. enterica sample `SAMN03469085`, analysis `ERZ4111211`, run `SRR1960351`; and Salmonella enterica sample `SAMN07135099`, analysis `ERZ5099315`, run `SRR5584613`. A checksum substring is not a taxon identifier.

All candidate source-native objects were read, not just snippets. Shared sample/run/accession digits do not supply identity, and even a genuine shared BioSample would not establish assembly equivalence.

A second ignored-inclusive search of the same ten roots for `JF778655|LT[ -]?4[ -]?CD` returned only the same three target rows. Exact-ID scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. No eligible missing strain/deposit/genome association was established within these bounded retained sources. Zero represented strains describes inventory coverage, not biological absence of the named isolate.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No required missing synonym, nomenclature, mapping, graph or evidence representation was established. Optional study-context enrichment is not required for this taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, provenance, source-count semantics and seeded status are supported. The marker and unrelated catalog matches do not supply an omitted LT4CD genome or deposit link.

## Recommended Edits

None. Preserve the generated YAML and `SEEDED` status.

Future primary taxonomy corrections belong at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization belongs in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope changes belong in `curation/seed_scope.tsv`. Any study-context extension needs a maintained input and target-specific evidence. Do not hand-edit generated YAML or count the marker as a genome.

## Follow-up Checks

No blocking follow-up remains. Future deposit/genome candidates require complete source-native inspection and an explicit identity/linkage chain before authorized regeneration. Rerun focused schema/strict validation plus the documented reproduction, provenance, history and relevant full gates after implementation. Recheck live taxonomy on a pinned-dump refresh. Independent sequence placement and chimera analysis were outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, existing worktree. The other session was reported closed; no additional worktree was created. This review adds only this report, with diagnostics under `/private/tmp`. Records, inventories, scope, history, statuses, prior reports and generated pages were preserved. No commit, GitHub mutation, external contact or paid research occurred. Eukaryota was left untouched.
