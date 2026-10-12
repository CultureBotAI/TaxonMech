# YAML Record Review: Pseudomonas sp. Horo_5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_horo_5.yaml`
- Started UTC: 2026-10-04T21:38:26Z
- Finished UTC: 2026-10-04T21:39:13Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033927`,
Pseudomonas sp. Horo_5. It asserts SPECIES, BACTERIA, parent
`NCBITaxon:196821`, ten root-first ancestors, code 11, EXACT grounding,
SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation
and one inline seed event. No record, code, input, status or history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_horo_5.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_horo_5.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded identity, full lineage, mapped-source, filename, scope and event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` limits diagnostics, not scope. Bounded comparisons are not byte-level reproduction. Full QC, tests and rendering were not run.
- Not applicable: `just validate-products`, as there are no curator graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. Inline provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221361`, full native
scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:30701`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033927&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033927)
agree on exact identifier, label, rank, domain, parent and code 11.
All ten lineage IDs match, including root; expanded labels and ranks
match where supplied. The chain includes Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas and its unclassified parent.

The underscore-bearing label is preserved. SPECIES is an NCBI placeholder
rank, not formal species-name validity. Backbone and native names have
no synonyms. Complete exact-ID type-material, merged-ID and dropped-taxon
scans returned no rows. Live taxonomy supplies no alias, type designation
or replacement requiring a change.

## Evidence

The sole attestation matches NCBI identity, label, one NAME assertion and
snapshot `2026-09-13`. Complete directly mapped BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin and BactoTraits scans returned no target rows.
The complete backbone scan found no children, so zero is also the
descendant-inclusive BacDive strain count.

Exact-taxonomy nuccore search returned one entry. Complete metadata,
references and feature qualifiers were inspected:
[AB627867.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB627867.1&rettype=gb&retmode=xml),
a 628-base partial 16S rRNA sequence explicitly assigned to Horo_5 and
taxon 1033927. Source qualifiers identify groundwater in Horonobe,
Hokkaido, Japan. It lists Sakurai and Yoshikawa, an unpublished
biofilm-study reference, and direct submission dated April 30, 2011.
No registered culture deposit, BioSample or assembly identifier is
supplied. This sequence is a marker, not a genome; Horo_5 is a
laboratory designation rather than a registered deposit.

Exact-taxonomy Assembly search returned zero with a
`phrasesnotfound` warning for `txid1033927[Organism:noexp]`.
This bounded result does not prove genome absence under all classifications.

[JAEA metadata](https://jopss.jaea.go.jp/search/servlet/search?5030464=)
for DOI `10.1080/00223131.2012.660015` was inspected earlier this turn,
but does not expose Horo_5's row. Direct publisher access returned
403 during Horo_1 review. No full-paper, isolate-table or figure
verification is claimed here. No phenotype or species reassignment
was inferred from that lead or from search excerpts.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
Patterns included ID, label, slug, separator alternatives and Horo-V.
All eight matching contexts were inspected: three target identity/scope
rows and five unrelated numeric matches.

The numeric matches are Salmonella enterica FDA1033927-S001-001
(GCA_006202105.1 historical and GCA_006202105.2 current),
Salmonella FDA1033927-S001-013 (GCA_005438195.1), the genome length
of uncultured bacterium GCA_982607845.1, and Streptococcus pneumoniae
sample SAMEA1033927. None is evidence of Horo_5 identity or a genome join.

A separate AB627867 search across those ignored-inclusive roots
completed with zero matches. The native scientific-name object was
read in full. No eligible strain, deposit or strain-genome assertion
was found within that scope. Zero inventoried BacDive strains does not
deny the isolate's existence. Empty optional nomenclature, mappings,
definition, evidence and graph slots are appropriate for the seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, source
attestation, strain inventory, status and inline provenance are supported.

## Recommended Edits

None. Preserve the generated YAML and SEEDED status. Future supported
corrections belong in maintained source inputs and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On refresh, recheck the exact taxon and AB627867 for explicit deposits
or primary genomes. Before using the later paper for a new claim,
inspect the exact isolate row and keep neighboring Horo designations
separate. After authorized changes, regenerate and run focused
validators plus full `just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13817` locks the slug;
`curation/seed_scope.tsv:321689` supplies the September 13, 2026 date
and one-source reason. The event at `2026-09-13T17:54:04Z` matches
the source list and scope wording. Ignored-inclusive filename and
history-content searches found no prior target report or history artifact.

iModulonDB is not applicable: no gene, regulator, expression module or
mechanism is asserted. No paid research, outside contact, GitHub mutation,
generator run, status promotion or history event occurred.

