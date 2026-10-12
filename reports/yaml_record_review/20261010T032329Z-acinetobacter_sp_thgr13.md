# YAML Record Review: Acinetobacter sp. THGR13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_thgr13.yaml`
- Started UTC: 2026-10-10T03:21:43Z
- Finished UTC: 2026-10-10T03:23:29Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037481` denotes Acinetobacter sp. THGR13, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196816`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. It asserts no synonym, nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph. The complete THGR13 designation is essential to identity; neither the genus alone nor a similar isolate code supports a join.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/acinetobacter_sp_thgr13.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/acinetobacter_sp_thgr13.yaml --out /private/tmp/taxonmech-thgr13-20261010-validation.tsv --workers 1`: one file, zero errors. The output was reread and contains only the header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Complete structured comparisons verified identity, code, every ancestor, empty source synonyms, seven source inventories, unique index/scope resolution and exact seed reason. A full backbone scan found no immediate child; own type-material, merged-ID and dropped-record inventories had no rows.
- The complete native scientific-name row, live NCBI browser, EFetch/Datasets taxonomy, nucleotide search and complete nucleotide annotations were inspected. The marker's declared/observed length and sequence hash were checked.
- The short NCBI browser URL initially failed through the web reader; its full node URL succeeded. No cited DOI or PMID is present in the YAML or marker submission to validate.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222753` and the [NCBI taxonomy browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037481&lvl=3&mode=node) agree on the name, species rank and code 11. [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037481&retmode=xml) confirms parent 196816, and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037481) includes root 1.

The complete root-first chain matches the pinned backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Moraxellales, Moraxellaceae, Acinetobacter and unclassified Acinetobacter. The terminal grouping node correctly retains `NO_RANK`. Preserve Moraxellales and the current NCBI chain rather than substituting an older or inferred classification.

`data/catalog/ncbi_names-0005.jsonl.gz:32391` contains the scientific name with an empty unique-name qualifier. Neither the backbone nor live EFetch supplies an alternate name. NCBI assigns `SPECIES` to this placeholder even though the nucleotide source uses strain THGR13; those are different kinds of metadata, not a rank conflict. Exact grounding does not imply a formally published binomial or a type-strain designation.

## Evidence

The NCBITAXON one-NAME assertion and 2026-09-13 snapshot note faithfully copy the pinned backbone. No additional source-count inventory row was found.

The nucleotide search returns one record, UID 334361448, [JF799816.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799816.1). Its 761-base sequence is a partial 16S rRNA gene with both ends marked partial. The source explicitly gives Acinetobacter sp. THGR13, strain THGR13, `taxon:1037481` and wetland soil. Declared and observed lengths agree with alphabet `acgt`. This is marker-to-taxon evidence, not a whole-genome assembly or a culture-deposit accession.

The only sequence reference is a direct submission dated 10-Apr-2011, attributed to Li, Liu, Shao and Sun at Hebei University. The source feature supplies no collection country or coordinates. The submitters' institutional address must not be repurposed as the specimen's collection location, and the submission date is not a collection date.

Bounded exact-designation and accession web searches did not establish a THGR13-specific primary paper. Unrelated uses of the same alphanumeric string were excluded. This is a search limitation, not proof that no publication exists. The taxonomy browser's generic NCBI database citation is not a strain-specific experimental citation.

Datasets omits an assembly-count field; that is not an explicit zero-assembly response. Neither the public marker nor the repository searches established a target genome accession. No pathogenicity, resistance, growth, metabolism or other trait is inferred from the genus or isolation-source phrase.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon ID, slug and designation. A second search added JF799816. Both returned exactly three source lines: own backbone, native name and scope.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These statements are bounded to the inspected repository surfaces.

`strain_count: 0` counts represented culture inventory, not whether an isolate named THGR13 existed or could be cultured. Empty optional nomenclature, synonyms, mappings, deposits, genomes and graph slots are appropriate without exact supporting evidence. The marker is optional taxon-level context, not a missing required genome field. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. NCBI identity, lineage, source count and seed audit are supported. The bounded searches do not establish a culture deposit, genome, publication or phenotype that the record is required to contain.

## Recommended Edits

No generated-record correction is justified. Preserve THGR13, NCBI species rank, its full lineage, `SEEDED` status and history. Do not add the marker as a genome, manufacture a deposit, infer sampling geography from an institutional address or promote broad Acinetobacter traits to this isolate.

Any future source correction belongs in the maintained upstream evidence and TaxonMech extraction/seeding path. Optional taxon-level marker or bibliographic enrichment requires an explicitly supported maintained representation, not a direct YAML edit or an invented strain container.

## Follow-up Checks

For separately requested enrichment, resolve exact THGR13 evidence, retain JF799816.1's version and distinguish collection metadata from submission metadata. A future genome link requires a genuine assembly identifier and exact organism/strain linkage, not only a partial 16S match.

For authorized changes, run the documented seed canary, focused schema/strict/history checks, full corpus reproduction and QC. A stable primary publication could support narrower future biological claims, but its existence and contents were not established here.

## Additional Notes

- YAML SHA-256: `5bb8a0e5b9aa64b50626efaec5589f36dac65c7b1126e93716086e905537478f`.
- JF799816.1 lowercase nucleotide-sequence SHA-256: `5af147a98b1931dda5ac0f182ae7ff1b47224ad2c805dd2e1a018edef253c70f`.
- `data/taxa/PATHS.tsv:15306` and `curation/seed_scope.tsv:322970` uniquely resolve the record. Scope addition is 2026-09-13; the seed event retains 2026-09-13T17:54:04Z and the exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
