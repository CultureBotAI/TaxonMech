# YAML Record Review: Beggiatoa sp. 'Monterey Canyon'

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/beggiatoa_sp_monterey_canyon.yaml`
- Started UTC: 2026-10-10T00:22:32Z
- Finished UTC: 2026-10-10T00:24:44Z
- Verdict: pass

## Target

The complete 58-line generated `TaxonRecord` was read. `NCBITaxon:1037350` denotes Beggiatoa sp. 'Monterey Canyon', rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:76865` (Candidatus Maribeggiatoa vulgaris), genetic code 11, grounding `EXACT`, status `SEEDED`.

The record carries ten ancestors, one exact NCBI synonym, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. It is not the species-level parent or the Carmel Canyon sibling.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/beggiatoa_sp_monterey_canyon.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/beggiatoa_sp_monterey_canyon.yaml --out /private/tmp/taxonmech-monterey-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured source comparisons matched identity, every ancestor, synonym, genetic code, own attestation, PATHS/scope entries and the seed-event explanation. Complete backbone scanning found no direct child. Exact own-ID scans found no type-material, merged-ID or dropped entry.
- Native NCBI names were read completely. Live EFetch taxonomy and Datasets responses were inspected completely. Primary marker metadata and relevant publication methods/results/accession text were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused comparisons are not corpus reproduction. No curator-added causal graph is present, so `just validate-products` has no applicable nodes.
- NCBI taxonomy browser and publisher retrieval failed in the web tool; PMC returned a browser challenge. Public NCBI APIs and the author institution's paper PDF supplied the inspected evidence. No genome sequence comparison or exhaustive external sequence census was performed.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:222718` agrees with [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037350&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037350): scientific name Beggiatoa sp. 'Monterey Canyon', strain rank, parent 76865 and genetic code 11.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Thiotrichales, Thiotrichaceae, Candidatus Maribeggiatoa and Candidatus Maribeggiatoa vulgaris. All stored ancestor identifiers, labels and ranks match the pinned backbone. EFetch confirms the chain below root; Datasets also includes root 1.

`data/catalog/ncbi_names-0005.jsonl.gz:32329` is the scientific-name row; row 32330 explicitly classifies Candidatus Maribeggiatoa vulgaris (MC) as a synonym. The older generic label and newer parent placement coexist in the current authority record; this is not evidence of a wrong identity. Exact grounding identifies the NCBI concept and does not assert formal nomenclatural validity or equivalence to every population of the parent species.

## Evidence

The sole NCBITAXON attestation has source ID 1037350, the exact scientific label, count 1, unit `NAME`, and snapshot 2026-09-13. It is one name assertion, not one genome or cultured deposit.

[AF064543 primary metadata](https://www.ncbi.nlm.nih.gov/nuccore/AF064543) explicitly connects accession AF064543.1 with organism Beggiatoa sp. 'Monterey Canyon' and `taxon:1037350`. It is a 1,493-base 16S rRNA marker. GenBank calls the sequence partial, and the rRNA feature has partial endpoints. The accession is not a genome assembly, strain deposit or asserted YAML link.

[Ahmad, Barry and Nelson's 1999 paper](https://www.mbari.org/wp-content/uploads/2015/11/Ahmad-et-al-1999.pdf), Applied and Environmental Microbiology 65:270-277, describes environmental sampling at Clam Field Seep, clone-library analysis and FISH confirmation of the marker's association with the wide Monterey filaments. Its accession paragraph identifies AF064543 and distinguishes two Thiomicrospira sequences. The paper's complete-16S terminology is retained as historical wording, not substituted for GenBank's current partial annotation. The marker bibliography supplies PMID 9872789.

These sources provide supplementary identity context. The YAML asserts no nitrate phenotype, pathway, expression module or habitat mechanism. Literature about neighboring populations or other wide sulfur bacteria was not generalized into new record claims.

## Completeness

A gitignore-independent, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Search terms included bounded 1037350, Beggiatoa/Monterey label context, the exact MC synonym and the slug. Its four lines were the backbone row, two native NCBI names and the scope row. All were inspected. A follow-up search for AF064543 over these same roots returned no matches, including ignored and compressed files.

Five SOURCE.json files were parsed separately; none contained a target match. Gitignore-independent filename enumeration under the taxon corpus and report directory found the single target YAML and no prior report. History filename inspection found no target-specific filename. These are bounded repository checks, not claims that external sequences or publications do not exist.

Complete structured scans found no own-ID row in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. The backbone has no direct child to supply descendant entries. Thus zero correctly counts the inventoried BacDive strains, not whether an environmental population has been studied. No eligible repository deposit-to-genome chain was established.

Optional nomenclature, mappings, biological definition, record-level evidence and causal graphs need not be invented for this seeded record. Gene/module adapters, including iModulonDB, were not applicable to its taxonomy-only assertions; marker literature does not turn this into a transcriptomics claim. No adapter execution or global dataset absence is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, full lineage, synonym, provenance, count semantics and seeded status are supported. Skipped corpus checks remain limitations.

## Recommended Edits

None required. Preserve the authority's strain rank and scientific-name/synonym distinction. Do not rename the record merely from its parent genus, treat the marker as a genome, or transfer the Carmel Canyon sibling's identifiers.

Any future authorized correction belongs in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No such correction is established here; do not hand-edit generated YAML.

## Follow-up Checks

Future deposit/genome enrichment requires an explicit primary-source identity chain. Biological additions need population-specific evidence and should preserve differences between historical paper wording and current sequence annotations.

After an authorized source refresh, rerun schema/strict/history validation and the documented full-corpus reproduction and QC gates. The present marker confirmation does not replace those gates.

## Additional Notes

- YAML SHA-256: `068dfe8b97126426aeb450b54a01eaaf54c1594e00ac08309a23531df93171d0`.
- `data/taxa/PATHS.tsv:15265` and `curation/seed_scope.tsv:322944` uniquely resolve this target. The seed event retains 2026-09-13T17:54:04Z and the matching one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, worktree, branch or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
