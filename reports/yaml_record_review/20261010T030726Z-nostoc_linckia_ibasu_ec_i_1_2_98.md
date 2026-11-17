# YAML Record Review: Nostoc linckia IBASU-EC-I-1-2-98

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nostoc_linckia_ibasu_ec_i_1_2_98.yaml`
- Started UTC: 2026-10-10T03:05:13Z
- Finished UTC: 2026-10-10T03:07:26Z
- Verdict: pass

## Target

The entire 62-line generated `TaxonRecord` was read. `NCBITaxon:1037412` denotes Nostoc linckia IBASU-EC-I-1-2-98, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:92942`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

It contains eleven ancestors, zero inventoried strains, one NCBITAXON name attestation, a one-ORGANISM GOLD attestation and one seed event. It asserts no formal nomenclature, synonym, GTDB mapping, culture deposit, individual genome, phenotype or causal graph. Preserve the complete hyphenated designation rather than treating its numeric suffix as incidental punctuation.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nostoc_linckia_ibasu_ec_i_1_2_98.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/nostoc_linckia_ibasu_ec_i_1_2_98.yaml --out /private/tmp/taxonmech-nostoc1298-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, all ancestors, code, empty source synonyms, source inventories, unique index/scope resolution, both attestation counts and exact seed reason. Complete backbone scanning found no immediate child. Own type-material, merged-ID and dropped-record inventories had no rows.
- The complete native NCBI name row and the full unrelated assembly-search hit were inspected. Direct NCBI EFetch/Datasets and nucleotide-search responses were read. GOLD extraction/counting code and the distinction between transformed counts and native workbook projections were checked.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`.
- The GOLD count is verified against the committed inventory, not independently back to its original individual GOLD organism. The configured kg-microbe `data` directory had no GOLD files or `edges.tsv` in an ignored-independent filename search. The current native GOLD projection also had no matching target row. The GOLD web request returned an error, and the NCBI browser page was unavailable through the web reader; structured NCBI taxonomy APIs succeeded.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222749`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037412&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037412) agree on the exact name, strain rank and placement. EFetch confirms parent 92942 and code 11. Datasets includes root 1.

The complete root-first chain matches the backbone: root, cellular organisms, Bacteria, Bacillati, Cyanobacteriota/Melainabacteria group, Cyanobacteriota, Cyanophyceae, Nostocales, Nostocaceae, Nostoc and Nostoc linckia. The intermediate group correctly retains `CLADE`. This is a bacterial cyanobacterial strain, not an Eukaryota record to reopen.

The full native row `data/catalog/ncbi_names-0005.jsonl.gz:32387` is the scientific name with an empty unique-name qualifier. The backbone and EFetch provide no alternate name. `EXACT` means identity with this NCBI strain, not a type-strain designation, completed genome or independent confirmation of every property of the parent species.

## Evidence

The NCBITAXON one-NAME assertion and 2026-09-13 snapshot note exactly match the pinned backbone. `data/raw/gold_organisms.tsv:531` contains the target and `organism_count: 1`; the YAML's one-ORGANISM attestation faithfully copies it.

That GOLD count has a different provenance from `data/gold/organisms.jsonl.gz`. `src/taxonmech/extract.py:676` counts GOLD organism subclass edges from kg-microbe's transformed GOLD graph; `src/taxonmech/extract.py:827` separately uses the native workbook projection for culture/genome links. `conf/sources.yaml` documents the two sources. Failure to find this target in the native projection does not, by itself, falsify the separately pinned graph count. However, without the original transformed edge, its contributing GOLD identifier and identity could not be independently established in this review. This remains an explicit verification limitation, not a claim that GOLD currently has exactly one retrievable organism for the strain.

The live nucleotide query `txid1037412[Organism:exp]` returned zero and included a `phrasesnotfound` entry. That indexing-limited result is not proof that no historical, unpublished, suppressed or differently annotated sequence exists. Datasets omitted an assembly-count field; omission is not an explicit zero-assembly response. No target accession was established by the inspected sources.

The only assembly-catalog numeric hit, `data/catalog/ncbi_genbank-0066.jsonl.gz:5028`, is `GCA_982276965.1`, a Desulfovibrionales bacterium, taxon 2448050. Its genome length is 1,037,412 bases. That coincidental number is not the target taxon ID and does not support a Nostoc genome link.

Bounded exact-name/designation web searches did not establish a strain-specific primary paper or an individual GOLD organism page. Broad species literature and taxonomic search leads were not used to infer this strain's physiology, habitat, genome or culture availability.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon ID, slug and full designation with punctuation variants. Six source lines matched: own backbone/name/count/scope/legacy-path evidence and the unrelated assembly-size collision.

A broader ignored-inclusive compressed search of `data/gold` for IBASU or linckia found records for other Nostoc linckia strains, including CCAP, UTEX, NIES, z-numbered and FACHB designations, but none for this IBASU strain. Their identities were inspected; the species name alone does not authorize reusing their GOLD identifiers or assemblies. These are repository source-coverage results, not universal absence claims.

Complete structured scans found no own BacDive, LPSN, GTDB, MediaDive, Madin or BactoTraits inventory row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly one target YAML, no prior target report and no target-specific history filename.

`strain_count: 0` reflects represented culture inventory, not whether this named strain is culturable. Empty optional nomenclature, mappings, culture, genome and graph slots are appropriate without exact supporting joins. iModulonDB is not applicable to these taxonomy/name/count assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None established within the inspected assertion scope. NCBI identity and generated inventory agreement are supported. The GOLD original-record provenance remains unresolved because the original transformed source was unavailable; this pass does not claim that check succeeded or that the native projection corroborated the count.

## Recommended Edits

No evidence-backed correction to the generated record is established. Leave the YAML, seed status and history unchanged. In particular, do not delete the GOLD count merely because a different source surface lacks the target, or replace it with an unrelated species-level organism.

Any future provenance repair belongs in the maintained kg-microbe GOLD mapping/extraction input and TaxonMech extraction/seeding path, not a hand-edited YAML. Resolve the original contributing GOLD organism before changing the count or adding a genomic assertion.

## Follow-up Checks

Restore the pinned GOLD transformed edges identified by `data/raw/MANIFEST.yaml`, whose kg-microbe revision is `30405b70ef762aa46c08278b2b3e06bffb0b34cd`. Locate the exact `gold:Go` subclass edge to `NCBITaxon:1037412`, resolve the organism at GOLD, and distinguish a retired/renamed source object from an erroneous mapping. Only that evidence can settle the current provenance limitation.

For separately authorized source changes, rerun extraction and the documented seed canary, then schema/strict/history checks, full corpus reproduction and QC. Verify exact strain linkage and accession versions for any proposed sequence; do not treat the nucleotide-search warning as proof of absence.

## Additional Notes

- YAML SHA-256: `45878ece4067d9bdf82a30f6ddea7c2a5bd22788b40c53bfd178cbbeadcf8ec3`.
- `data/taxa/PATHS.tsv:15302` and `curation/seed_scope.tsv:57259` uniquely resolve the target. The seed event retains 2026-09-13T17:54:04Z and the exact GOLD/NCBITAXON scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
