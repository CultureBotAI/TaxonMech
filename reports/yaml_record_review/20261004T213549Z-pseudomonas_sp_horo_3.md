# YAML Record Review: Pseudomonas sp. Horo_3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_horo_3.yaml`
- Started UTC: 2026-10-04T21:34:53Z
- Finished UTC: 2026-10-04T21:35:49Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033925`,
Pseudomonas sp. Horo_3. It asserts SPECIES, BACTERIA, parent
`NCBITaxon:196821`, ten ancestors, code 11, EXACT grounding, SEEDED
status, zero inventoried strains, one NCBITAXON NAME attestation and
one inline seed event. No record, code, input, status or history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_horo_3.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_horo_3.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded identity, full lineage, mapped-source, filename, scope and inline-event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` limits diagnostic output, not scope. Bounded checks are not byte-level reproduction. Full QC, tests and rendering were not run.
- Not applicable: `just validate-products`; no curator graph nodes are asserted. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. Inline provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221359`, the full scientific-name
object `data/catalog/ncbi_names-0005.jsonl.gz:30699`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033925&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033925)
agree on the exact identifier, underscore-bearing label, species rank,
bacterial domain, parent and code 11. All ten root-first lineage IDs
match; expanded ancestor labels and ranks match where supplied.
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales,
Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas are preserved.

SPECIES is an NCBI placeholder rank, not evidence of a validly published
species name. Backbone and native names have no synonyms. Complete
exact-ID type-material, merged-ID and dropped-taxon scans returned no
rows; live taxonomy supplies no alias or replacement requiring a change.

## Evidence

The sole attestation agrees exactly with NCBI identity, label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans returned no
target rows. A complete backbone scan found no children; zero is also
the descendant-inclusive BacDive count.

Exact-taxonomy nuccore search returned one entry. All metadata,
references and feature qualifiers were inspected:
[AB627865.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB627865.1&rettype=gb&retmode=xml),
a 628-base partial 16S rRNA sequence explicitly assigned to Horo_3 and
taxon 1033925. It records groundwater in Horonobe, Hokkaido, Japan,
Sakurai and Yoshikawa as authors, an unpublished biofilm-study
reference and direct submission on April 30, 2011. It supplies no
registered culture accession, BioSample or assembly identifier.
A partial marker is not a genome; Horo_3 is a laboratory designation.

Exact-taxonomy Assembly search returned zero with a
`phrasesnotfound` warning for `txid1033925[Organism:noexp]`.
That does not establish genome absence under every classification.

The later-paper lead is retained only as a lead:
[JAEA metadata](https://jopss.jaea.go.jp/search/servlet/search?5030464=),
DOI `10.1080/00223131.2012.660015`, was inspected earlier this turn.
It does not provide Horo_3's exact table row. Direct publisher access
returned 403 during Horo_1 review; full paper, table and assay values
were not verified. No phenotype or species identity was inferred from
cohort-level evidence or search excerpts.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
Patterns included the ID, label, slug, separator alternatives and
Horo-III. All six matching line contexts were inspected: three target
identity/scope rows and three numeric near matches.
GCA_045635125.1 is an Alphaproteobacteria MAG whose genome length
matches the taxon digits in both GenBank and GTDB catalogs.
SAMEA1033925 is a Streptococcus pneumoniae sample. Neither is Horo_3.

A separate AB627865 search over the same ignored-inclusive roots
completed with zero matches. The native scientific-name object was
read in full. No eligible strain, deposit or strain-genome assertion
was found in that scope. Zero BacDive entries does not deny the
isolate's existence. Empty optional nomenclature, mappings, definition,
evidence and graph slots are appropriate for the source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, attestation,
strain inventory and audit metadata are supported.

## Recommended Edits

None. Preserve the generated YAML and SEEDED status. Future supported
corrections belong in maintained inventory inputs and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On refresh, recheck the exact taxon and AB627865 for explicit deposits
or primary genomes. Before importing any later-paper claim, inspect
the exact isolate row and keep neighboring Horo designations separate.
After authorized changes, regenerate and run focused validators plus
full `just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13815` locks the slug;
`curation/seed_scope.tsv:321687` supplies the September 13, 2026 date
and one-source reason. The event at `2026-09-13T17:54:04Z` matches
the source list and scope wording. Ignored-inclusive filename and
history-content searches found no prior target report or history artifact.

iModulonDB is not applicable: no gene, regulator, expression module or
mechanism is asserted. No paid research, outside contact, GitHub mutation,
generator run, status promotion or history event occurred.

