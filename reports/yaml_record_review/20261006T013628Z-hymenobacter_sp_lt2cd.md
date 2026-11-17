# YAML Record Review: Hymenobacter sp. LT2CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/hymenobacter_sp_lt2cd.yaml`
- Started UTC: 2026-10-06T01:34:11Z
- Finished UTC: 2026-10-06T01:36:28Z
- Verdict: pass

## Target

Read the entire 60-line generated `TaxonRecord` for `NCBITaxon:1034918`, Hymenobacter sp. LT2CD. It is a `SPECIES` in `BACTERIA`, parent `NCBITaxon:2615202` (unclassified Hymenobacter), with twelve root-first lineage entries, genetic code 11, `EXACT` grounding and `SEEDED` mapping status. It has zero represented strains, one NCBITAXON NAME assertion at snapshot `2026-09-13`, and one inline `SEEDED_FROM_SOURCES` event dated `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strain entries, evidence, discussions and causal graph are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/hymenobacter_sp_lt2cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/hymenobacter_sp_lt2cd.yaml --out /private/tmp/lt2cd-validation.tsv`: exit 0, one file, zero ERROR rows. Read the full header-only TSV.
- Structured comparisons checked the complete target backbone and scope rows, every ancestor ID/label/rank, unique PATHS entry, source attestation and inline seed-event description. The backbone scan returned no children. These bounded comparisons are not a substitute for full-corpus reproduction.
- Exact-ID scans of the complete `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` returned no matching row. Seven supplementary source inventories likewise returned no exact target-ID match.
- Complete live NCBI Taxonomy EFetch/Datasets responses, exact non-expanding Assembly/Nuccore search results, and full nucleotide metadata, references and feature annotations were inspected. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. No full gate is claimed by this bounded report-only review. Inline-event inspection is not a history-schema validation run.
- `just validate-products` and iModulonDB were not applicable without curator-added graph grounding, genes, regulators, expression modules or transcriptomic claims. No target LPSN/GTDB assertion required an authority-page check.

## Identity and Grounding

The complete `data/raw/ncbitaxon_taxa.tsv:221746` row agrees with the YAML. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034918&retmode=xml) confirms exact ID/label, species rank, parent, bacterial division and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034918) confirms the target and all twelve ordered ancestor IDs, including root.

The lineage is root, cellular organisms, Bacteria, Pseudomonadati, FCB group, Bacteroidota/Chlorobiota group, Bacteroidota, Cytophagia, Cytophagales, Hymenobacteraceae, Hymenobacter and unclassified Hymenobacter. Every label and rank agrees. FCB group (`NCBITaxon:1783270`) and Bacteroidota/Chlorobiota group (`NCBITaxon:68336`) are carried `CLADE` entries. The GenBank lineage omits those clades and the final unclassified intermediate; dedicated taxonomy responses confirm the full chain. This is abbreviation, not evidence for reparenting.

`data/taxa/PATHS.tsv:14216` uniquely maps the ID to `hymenobacter_sp_lt2cd`; `curation/seed_scope.tsv:322048` supplies the one-source NCBI inclusion rule. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31149` identifies the same taxon. No alternate target name is supplied by the inspected taxonomy evidence. NCBI species rank for this provisional isolate-labelled entity does not prove formal nomenclatural validity or equivalence with other LT-labelled isolates.

## Evidence

The record asserts source-backed NCBI identity and carried lineage. Source ID, label, snapshot, count of one and NAME unit match the inventory. A name assertion is not a biological strain or genome count. No phenotype, medium, ecological mechanism, genome or type-strain claim appears in the YAML.

The exact Nuccore query returned UID 333496484. The complete [JF778653.1 record](https://www.ncbi.nlm.nih.gov/nuccore/JF778653.1) is an 843-base partial 16S rRNA gene, partial at both ends, with Hymenobacter sp. LT2CD, strain LT2CD, freshwater-lake isolation source and `taxon:1034918` qualifiers. Its only reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter's Bellerophon-screening statement was not independently tested here. The metadata have no culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID. A partial marker and bare strain name do not establish a deposited-culture/genome chain.

The inspected main text of [Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4) includes JF778653 within JF778652-JF778667. That range and matching authors support a Lake Tawani(P), East Antarctica study association, not LT2CD-specific physiology, growth optima or deposit identity. Supplements and figure images were not inspected.

Exact Assembly search returned zero with a phrase-not-found warning for `txid1034918[Organism:noexp]`. This bounded result is not proof of genome absence under all other identifiers or taxa.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i`, including hidden/compressed files and excluding `SOURCE.json` manifests, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The ID digits, full label and slug search yielded 25 lines. Backbone and scope were read structurally; all other eight native JSON objects and fifteen complete header-aware AllTheBacteria rows were read. Reconciliation found no unread or truncated candidate.

Three rows identify LT2CD: backbone, scope and native scientific name. The other 22 are numeric collisions with different organisms:

- Five objects concern Escherichia coli PNUSAE018546, taxon 562, sample `SAMN10349189`: BV-BRC `562.36428`, GOLD project `Gp0386993` naming organism `Go0502716` and project `PRJNA218110`, current GenBank `GCA_003752795.2`, replaced `GCA_003752795.1`, and AllTheBacteria analysis `ERZ9092469` with run `SRR8136889`. GOLD project/organism IDs are not genome IDs, and the explicit E. coli source chain cannot transfer to LT2CD.
- GenBank `GCA_010349185.1` is Campylobacter jejuni PNUSAC013676, taxon 197, sample `SAMN13353461`, project `PRJNA239251`.
- GenBank `GCA_027162465.1` is Staphylococcus aureus 8-315-236, taxon 1280, sample `SAMEA1034918`, project `PRJNA514245`; the corresponding AllTheBacteria sample row is also Staphylococcus aureus, analysis `ERZ3070317`, run `ERR086082`.
- BV-BRC `1773.20366` is Mycobacterium tuberculosis ERR1034918, taxon 1773; the AllTheBacteria row for that run is Mycobacterium tuberculosis sample `SAMEA3558451`, analysis `ERZ3501209`.
- Two further AllTheBacteria Mycobacterium tuberculosis rows, samples `SAMN13814076` and `SAMN41421963`, match digits inside a SeqKit sum. They name analyses `ERZ25703653` and `ERZ26762457`, respectively. A checksum substring is not a taxon identifier.
- Ten AllTheBacteria entries identify Shigella sonnei samples `SAMEA110349180` through `SAMEA110349189`.

A separate ignored-inclusive scan of the same ten roots for `JF778653|LT[ -]?2[ -]?CD` returned only the same three target rows. Exact-ID structured scans of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. No eligible missing strain/deposit/genome association is supported within these bounded retained sources. Zero represented strains describes inventory evidence, not the named isolate's biological nonexistence.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No required missing synonym, nomenclature, mapping, graph or evidence object was established. Optional study-context enrichment is not required for a taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, carried lineage, provenance, source-count semantics and seeded status are supported. The E. coli source chain and other numeric collisions do not supply an LT2CD genome or deposit relationship.

## Recommended Edits

None. Preserve the generated YAML and `SEEDED` status.

Future primary taxonomy corrections belong at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization belongs in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope policy belongs in `curation/seed_scope.tsv`. Any study-context extension needs a maintained input and explicit target-specific evidence. Do not hand-edit generated YAML or count the marker as a genome.

## Follow-up Checks

No blocking follow-up remains. Any future deposit/genome candidate requires full source-native inspection and an explicit identity/linkage chain before authorized regeneration. Rerun focused schema/strict validation and the documented reproduction, provenance, history and relevant full gates after implementation. Recheck live taxonomy when refreshing the pinned dump. Independent sequence placement and chimera analysis were outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, existing worktree; the other session was reported closed and no additional worktree was created. This target review adds only this report, with diagnostics under `/private/tmp`. Records, inventories, scope, history, statuses, prior reports and generated pages were preserved. No commits, GitHub mutations, external contacts or paid research occurred. Eukaryota was left untouched.
