# YAML Record Review: Paenibacillus sp. KMS2U3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_kms2u3.yaml`
- Started UTC: 2026-10-04T20:42:42Z
- Finished UTC: 2026-10-04T20:43:53Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033906`,
Paenibacillus sp. KMS2U3: SPECIES, BACTERIA, parent `NCBITaxon:185978`,
ten root-first ancestors, code 11, EXACT grounding and SEEDED status.
It has zero inventoried BacDive strains, one NCBITAXON NAME attestation
and one seed event. No record, input, code, status or history entry was
edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_sp_kms2u3.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_sp_kms2u3.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded structured comparisons passed for identity, every ancestor,
  directly mapped inventories, filename lock, scope and seed wording.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` limits
  diagnostics, not scope. Bounded comparisons do not establish byte-level
  reproduction. Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, because no curator graph nodes
  are asserted. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221340`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30680`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033906&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033906)
agree on ID, label, rank, bacterial domain, parent and code 11.
All ten ancestor IDs match, including root; live expanded labels and
ranks agree where supplied. The chain includes Bacillati, Bacillota,
Bacilli, Caryophanales, Paenibacillaceae, Paenibacillus and unclassified
Paenibacillus.

SPECIES is NCBI's operational rank for this placeholder, not a claim of
valid nomenclatural publication or a resolved named-species identity.
KMS2U3 is not a registered culture accession. The native name object
and backbone supply no synonyms. Complete exact-ID type-material,
merged-ID and dropped-taxon scans returned no rows, and live taxonomy
supplies no successor or synonym requiring a change.

## Evidence

The sole attestation matches the exact NCBI identifier and label, one
NAME assertion and snapshot `2026-09-13`. Complete directly mapped
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans found
no target rows. A complete backbone scan found no children, so zero
is also the full descendant-inclusive BacDive count.

Exact-taxonomy nuccore search returned one entry. Its metadata,
references and all feature qualifiers were inspected:
[JF768722.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768722.1&rettype=gb&retmode=xml)
is a 1,461-base partial 16S rRNA sequence explicitly assigned to
KMS2U3 and taxon 1033906, from a uranium-rich site at Domiasiat, India.
It supplies no registered deposit, BioSample or assembly identifier.

The marker cites [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`, whose metadata and article body were
inspected earlier in the ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes and the complete KMS2U3/JF768722 row:
1,461 bases and closest match Paenibacillus taichungensis at 98.69%
similarity. The attached footnote d explicitly cautions that this
similarity may not justify species-level affiliation. The paper does
not establish identity with P. taichungensis, and the YAML correctly
retains the NCBI placeholder. The supplementary PDF was not inspected.
No phenotype or mechanism is asserted by the YAML or imported here.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033906[Organism:noexp]`. This bounded result is not
proof of genome absence under every possible classification.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. ID, label, slug and designation
spelling searches produced eight matching lines, all inspected in
source context. Three were target backbone, scope and scientific name.
Five matched the unrelated Streptococcus pneumoniae sample SAMEA1033906
in BV-BRC, GenBank, RefSeq, GTDB and AllTheBacteria. Those rows concern
D48490/GCA/GCF_900052035.1, not this Paenibacillus isolate.

The target native name object was read in full. A separate JF768722
search across the same ignored-inclusive roots completed with zero
matches. No eligible deposit or strain-genome assertion for KMS2U3 was
found in that scope.

Zero BacDive entries is an inventory count, not absence of a biological
isolate. A partial 16S marker is not a missing genome identifier.
Empty optional nomenclature, mappings, definition, record-level evidence
and causal graphs are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected evidence scope. Identity, lineage,
attestation, strain count, status and inline provenance are supported.
The record preserves the uncertainty in named-species identification
instead of promoting a closest 16S match into equivalence.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future supported
corrections belong in the maintained inventory pipeline and, as
appropriate, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`;
scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On source refresh, recheck the exact taxon, KMS2U3 and JF768722 for
explicit deposits or primary genomes. Preserve the paper's species-
identification caveat and do not transfer other isolates' accessions.
After authorized changes, rerun focused validators and the full
`just verify-corpus` gate after regeneration. No unresolved blocker
prevents the current taxon-record verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13796` locks the slug.
`curation/seed_scope.tsv:321669` supplies the September 13, 2026 addition
and one-source reason. The event at `2026-09-13T17:54:04Z` reproduces
that reason and the NCBITAXON source list. Ignored-inclusive filename
searches in reports/history/curation found no prior target report or
target-specific history artifact before creation.

iModulonDB is not applicable to this taxonomic record, which asserts no
gene, regulator, expression module or mechanism. No paid research,
outside contact, GitHub mutation, generator run, status promotion or
history event occurred.
