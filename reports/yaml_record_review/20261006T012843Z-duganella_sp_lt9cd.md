# YAML Record Review: Duganella sp. LT9CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_lt9cd.yaml`
- Started UTC: 2026-10-06T01:26:35Z
- Finished UTC: 2026-10-06T01:28:43Z
- Verdict: pass

## Target

Read all 56 lines of the generated `TaxonRecord` for `NCBITaxon:1034916`, Duganella sp. LT9CD. Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2636909` (unclassified Duganella). It carries eleven root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and zero represented strains. The sole attestation is one NCBITAXON NAME at snapshot `2026-09-13`; the sole inline history event is `SEEDED_FROM_SOURCES` at `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strain entries, evidence objects, discussions and causal graph are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_lt9cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_lt9cd.yaml --out /private/tmp/lt9cd-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the complete header-only TSV.
- Structured comparisons checked the complete target backbone row, every ancestor ID/label/rank, unique PATHS mapping, exact scope row, attestation and inline seed-event description. The backbone scan returned no children. These comparisons are bounded, not a proof of complete corpus reproduction.
- Exact-ID scans of the complete `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no matching row. Seven supplementary inventories also returned no exact target-ID match.
- Read complete live NCBI Taxonomy EFetch/Datasets responses, exact non-expanding Assembly/Nuccore query results, and full metadata, references and feature annotations of the sole nucleotide hit. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. No such full gate is claimed by this bounded report-only review; inline-event inspection is not a history-schema run.
- `just validate-products` and iModulonDB were not applicable without curator-added graph grounding, genes, regulators, expression modules or transcriptomic claims. No target LPSN/GTDB assertion required an authority-page check.

## Identity and Grounding

The entire backbone row at `data/raw/ncbitaxon_taxa.tsv:221744` agrees with the YAML. The inspected [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034916&retmode=xml) confirms exact ID/label, species rank, parent, bacterial division and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034916) confirms the taxon and the complete ordered ancestor IDs, including root.

The ancestors are root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group, Duganella and unclassified Duganella. All labels and ranks agree with the pinned inventory and inspected taxonomy evidence. Telluria group (`NCBITaxon:2895353`) is a no-rank ancestor, not an LT9CD synonym or alternate genus assignment. GenBank's abbreviated lineage omits the final unclassified intermediate; the dedicated taxonomy endpoints confirm it.

`data/taxa/PATHS.tsv:14214` uniquely maps the ID to `duganella_sp_lt9cd`. `curation/seed_scope.tsv:322046` gives the one-source NCBI inclusion rule. The complete scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31147` identifies this same taxon. No alternate target name is supplied by the inspected taxonomy evidence. A provisional isolate-labelled NCBI species-rank entity is not thereby a validly published formal species, nor equivalent to another LT-labelled isolate.

## Evidence

The asserted NCBI identity and carried lineage are supported at the stated snapshot. Source ID, label, snapshot, count of one and NAME unit agree with the inventory; name-assertion counts are not strain or genome totals. The YAML asserts no phenotype, medium, ecological mechanism, type strain or genome.

The exact Nuccore search returned UID 333496491. Its complete [JF778660.1 record](https://www.ncbi.nlm.nih.gov/nuccore/JF778660.1) is a 906-base partial 16S rRNA gene, partial at both ends, annotated with Duganella sp. LT9CD, strain LT9CD, freshwater-lake isolation source and `taxon:1034916`. The only reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter reports Bellerophon chimera screening; it was not independently repeated here. The full metadata supply no culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID. This partial marker and bare strain designation are not a culture-deposit/genome chain.

The inspected main text of [Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4) includes JF778660 within JF778652-JF778667. That range and matching authors support a Lake Tawani(P), East Antarctica study association. Community observations and study conditions do not establish LT9CD-specific physiology, growth optima or deposit identity. Supplements and figure images were not inspected.

Exact Assembly search returned zero with a phrase-not-found warning for `txid1034916[Organism:noexp]`. That bounded result does not prove that no genome could exist under any other identifier or taxon.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i`, including hidden/compressed files and excluding `SOURCE.json` manifests, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The ID digits, full label and slug query found 18 lines. Backbone and scope were read structurally; all other four native JSON objects and twelve complete header-aware AllTheBacteria rows were read. Reconciliation found no unread or truncated candidate.

Three rows identify the target: backbone, scope and scientific name. The fifteen other numeric matches belong to different organisms:

- BV-BRC `1773.20368` is Mycobacterium tuberculosis ERR1034916, taxon 1773, with no GenBank accession in that object. The AllTheBacteria row for run `ERR1034916` is Mycobacterium tuberculosis sample `SAMEA3558449`, analysis `ERZ3501197`.
- GenBank `GCA_010349165.1` is Campylobacter jejuni PNUSAC013997, taxon 197, sample `SAMN13542294`, project `PRJNA239251`. The matching digits occur in the assembly accession, not its taxonomy.
- GenBank `GCA_027162725.1` is Staphylococcus aureus 8-308-250, taxon 1280, sample `SAMEA1034916`, project `PRJNA514245`. Its AllTheBacteria sample match is also Staphylococcus aureus, analysis `ERZ3070318`, run `ERR086072`.
- Ten AllTheBacteria rows are Shigella sonnei samples `SAMEA110349160` through `SAMEA110349169`.

A separate ignored-inclusive search across the same ten roots for `JF778660|LT[ -]?9[ -]?CD` returned only the same three target rows. Exact-ID structured scans of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Within those bounded retained sources, no eligible missing strain/deposit/genome association is supported. Zero represented strains describes inventory evidence, not the biological nonexistence of the LT9CD isolate.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No required missing synonym, nomenclature, mapping, graph or evidence object was established. Optional study-context enrichment is not a prerequisite for this taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, carried lineage, source count, provenance and seeded status are supported. The marker and unrelated accession substrings do not justify adding an LT9CD genome or deposit association.

## Recommended Edits

None. Keep the generated YAML and `SEEDED` status unchanged.

Future primary taxonomy corrections belong at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization belongs in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope policy belongs in `curation/seed_scope.tsv`. Any future study-context addition needs a maintained input and narrow target-specific evidence. Do not hand-edit generated YAML or treat this rRNA marker as a genome.

## Follow-up Checks

No blocking follow-up remains. New deposit/genome candidates require full source-native inspection and an explicit identity/linkage chain before any authorized regeneration. Rerun focused schema/strict validation and the documented reproduction, provenance, history and relevant full gates after implementation. Recheck live taxonomy on a pinned refresh. Independent sequence placement and chimera analysis were outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, existing worktree. The other session was reported closed; no additional worktree was created. This target review adds only this report, with validation diagnostics under `/private/tmp`. Records, source inventories, scope, history, statuses, prior reports and generated pages were preserved. No commits, GitHub mutations, external contacts or paid research occurred. Eukaryota was left untouched.
