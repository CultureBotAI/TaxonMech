# YAML Record Review: Nostoc linckia IBASU-EC-I-6-15-98

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nostoc_linckia_ibasu_ec_i_6_15_98.yaml`
- Started UTC: 2026-10-10T03:09:33Z
- Finished UTC: 2026-10-10T03:11:14Z
- Verdict: pass

## Target

The entire 62-line generated `TaxonRecord` was read. `NCBITaxon:1037452` denotes Nostoc linckia IBASU-EC-I-6-15-98, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:92942`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

It carries eleven ancestors, zero inventoried strains, one NCBITAXON name, one GOLD organism-count attestation and one seed event. It asserts no synonym, formal nomenclature, GTDB mapping, culture deposit, individual genome, phenotype or causal graph. Its full designation distinguishes it from IBASU-EC-I-1-2-98; neither the shared species nor collection prefix establishes strain equivalence.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nostoc_linckia_ibasu_ec_i_6_15_98.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/nostoc_linckia_ibasu_ec_i_6_15_98.yaml --out /private/tmp/taxonmech-nostoc61598-20261010-validation.tsv --workers 1`: one file, zero errors. The output was reread and contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured comparisons verified identity, genetic code, every ancestor, empty source synonyms, seven source inventories, unique index/scope resolution and the exact seed reason. A complete backbone scan found no immediate child. Own type-material, merged-ID and dropped-record inventories had no rows.
- The complete native NCBI name and all three native genome-catalog search hits were inspected. Direct NCBI EFetch/Datasets taxonomy and nucleotide-search responses were read in full. GOLD extraction/counting ownership was checked.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`.
- The GOLD count matches its committed inventory, but its original contributing GOLD organism could not be independently resolved. The native GOLD projection had no target match; an ignored-independent search of the configured kg-microbe `data` directory found no GOLD files or `edges.tsv`. The GOLD organisms web request returned an error. The NCBI browser request failed through the web reader; structured NCBI APIs succeeded.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222750`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037452&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037452) agree on the exact strain name and placement. EFetch confirms parent 92942, rank strain and genetic code 11; Datasets also supplies root 1.

The full root-first chain agrees with the pinned backbone: root, cellular organisms, Bacteria, Bacillati, Cyanobacteriota/Melainabacteria group, Cyanobacteriota, Cyanophyceae, Nostocales, Nostocaceae, Nostoc and Nostoc linckia. The intermediate group correctly retains `CLADE`. Preserve this NCBI classification without substituting another source's hierarchy.

The full native row `data/catalog/ncbi_names-0005.jsonl.gz:32388` contains the scientific name and an empty unique-name qualifier. Neither the backbone nor live EFetch supplies an alternate name. Exact grounding establishes this NCBI strain identity, not type status, culture availability or a completed genome. No Eukaryota record was opened.

## Evidence

The NCBITAXON one-NAME attestation and 2026-09-13 snapshot note exactly match the backbone. `data/raw/gold_organisms.tsv:532` contains this target with `organism_count: 1`, faithfully represented as one `ORGANISM` in the YAML.

The GOLD attestation originates from transformed organism subclass edges, not directly from the native workbook projection. `src/taxonmech/extract.py:676` counts `gold:Go` subjects of `biolink:subclass_of` edges in kg-microbe's transformed GOLD graph; the separate native projection supplies culture/genome relationships at `src/taxonmech/extract.py:827`. `conf/sources.yaml` documents these distinct inputs. A missing match in the native projection does not by itself disprove the pinned transformed count. However, the original organism identifier and mapping remain unresolved because the frozen transformed source is unavailable. This report does not claim that primary provenance check passed.

The live nucleotide query `txid1037452[Organism:exp]` returned zero with `phrasesnotfound`. This indexing-limited response is not proof that no historical, suppressed, unpublished or differently annotated sequence exists. Datasets omitted an assembly-count field; omission is not an explicit zero. No target genome accession was established from the inspected evidence.

Three catalog search hits are numeric collisions, not genome links:

- `data/catalog/gtdb_genomes-0017.jsonl.gz:23602` and `data/catalog/ncbi_genbank-0014.jsonl.gz:35790` describe `GCA_016187035.1`, Candidatus Daviesbacteria bacterium, taxon 2053542. Its total and ungapped lengths are 1,037,452 bases. The GTDB cluster is `s__JACPKL01 sp016187035`, not Nostoc.
- `data/catalog/ncbi_genbank-0065.jsonl.gz:48243` describes `GCA_982186155.1`, Gemella morbillorum, taxon 29391, with ungapped length 1,037,452 bases. Its total length is 1,038,452 bases. Neither length is a target taxon identifier.

Bounded exact-name/designation web searches did not establish a target-specific primary publication or individual GOLD organism page. The NCBI family-tree search lead lists the full strain designation, but the inspected structured taxonomy responses are the identity evidence. Broad Nostoc literature was not promoted to a strain-specific trait claim.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The pattern included bounded taxon ID, slug and complete strain designation with punctuation variants. Eight source lines matched: own backbone/name/count/scope/legacy-path rows plus the three unrelated genome-statistic hits.

Complete structured scans found no own BacDive, LPSN, GTDB, MediaDive, Madin or BactoTraits inventory row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no existing target report and no target-specific history filename. These statements describe the inspected repository surfaces, not universal biological absence.

`strain_count: 0` reflects represented culture inventory, not whether this named strain can be cultured. Empty optional nomenclature, mappings, cultures, genomes and graph slots are appropriate without exact supporting evidence. Do not borrow a genome or GOLD organism from another Nostoc linckia strain. iModulonDB is not applicable to these taxonomy/name/count assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None established within the checked assertion scope. Identity and agreement with the pinned inventories are supported. Original GOLD organism provenance remains an explicit verification limitation, not an independently verified primary claim or an established defect.

## Recommended Edits

No evidence-backed correction is established. Leave the generated YAML, `SEEDED` status and history unchanged. Do not remove the GOLD count merely because a different source surface lacks the strain, and do not replace it with a species-level or neighboring-strain organism.

Any subsequently demonstrated provenance defect belongs in the maintained kg-microbe GOLD mapping/extraction inputs and TaxonMech extraction/seeding path, not a direct YAML edit. Resolve the original source organism before revising counts or adding genome claims.

## Follow-up Checks

Restore the transformed GOLD input pinned by `data/raw/MANIFEST.yaml` at kg-microbe revision `30405b70ef762aa46c08278b2b3e06bffb0b34cd`. Resolve the exact `gold:Go` subclass edge to `NCBITaxon:1037452` and distinguish a retired/renamed organism from an incorrect mapping. This is the bounded remaining provenance check.

For separately authorized source changes, rerun extraction and the documented seed canary, then schema/strict/history validation, full corpus reproduction and QC. Verify any proposed sequence's exact strain linkage and accession version; neither an indexing warning nor an assembly-length coincidence settles that question.

## Additional Notes

- YAML SHA-256: `f62ba470aa6a4a4399c311396fe2c4777b72487f76d46531558beb83251b11c7`.
- `data/taxa/PATHS.tsv:15303` and `curation/seed_scope.tsv:57260` uniquely resolve the record. The seed event retains 2026-09-13T17:54:04Z and the exact two-source GOLD/NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed, and no review status was promoted.
