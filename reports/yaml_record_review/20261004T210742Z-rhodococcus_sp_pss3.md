# YAML Record Review: Rhodococcus sp. PSS3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhodococcus_sp_pss3.yaml`
- Started UTC: 2026-10-04T21:06:24Z
- Finished UTC: 2026-10-04T21:07:42Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033916`,
Rhodococcus sp. PSS3. It asserts SPECIES, BACTERIA, parent
`NCBITaxon:192944`, ten ancestors, code 11, EXACT grounding, SEEDED
status, zero inventoried BacDive strains, one NCBITAXON NAME attestation
and one inline seed event. No YAML, code, input, status or history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/rhodococcus_sp_pss3.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/rhodococcus_sp_pss3.yaml`; one file, zero errors. This is the implementation of `just validate-strict`, producing `reports/instance_validation_failures.tsv`.
- Bounded identity, lineage, mapped-source, scope, filename and event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` caps diagnostics, not scope. Bounded comparisons are not byte-level reproduction. Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, as no curator graph nodes are asserted. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. The inline event was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221350`, full scientific-name object
`data/catalog/ncbi_names-0005.jsonl.gz:30690`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033916&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033916)
agree on the exact taxon, label, rank, domain, parent and genetic code.
All ten lineage IDs match; expanded labels and ranks agree where supplied.
The chain includes Bacillati, Actinomycetota, Actinomycetes,
Mycobacteriales, Nocardiaceae, Rhodococcus and the unclassified
Rhodococcus parent. SPECIES is an NCBI placeholder rank, not formal
nomenclatural validity.

Backbone and native name object supply no synonyms. Complete exact-ID
type-material, merged-ID and dropped-taxon scans returned no rows.
Live taxonomy supplies no replacement or synonym requiring a change.
The inspected target sources use PSS3 as a laboratory strain
designation, not a registered culture accession or globally unique name.

## Evidence

The sole attestation exactly matches the NCBI identifier, label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans found no target
rows. A complete backbone scan found no children, so zero is also the
descendant-inclusive BacDive count.

Exact-taxonomy nuccore search returned one entry; all metadata,
references and feature qualifiers were inspected.
[JF768732.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768732.1&rettype=gb&retmode=xml)
is a 1,429-base partial 16S rRNA sequence, explicitly assigned to
PSS3 and taxon 1033916, from a uranium-rich site in Domiasiat, India.
It supplies no registered deposit, BioSample or assembly identifier.

The entry cites [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`. Article metadata and body were inspected
earlier in this ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes and the PSS3/JF768732 row: 1,429 bases and
closest match Rhodococcus equi at 99.37% similarity. This is marker
context, not a formal merger, deposit or genome identity. No phenotype
or mechanism is asserted by the YAML or imported here; the phosphatase
footnote does not change taxon identity. The supplementary PDF was not inspected.

Exact-taxonomy Assembly search returned zero, with a `phrasesnotfound`
warning for `txid1033916[Organism:noexp]`; this is not proof of genome
absence under every possible classification.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json`. ID, label, slug and designation patterns
included Roman-III/digit-3 alternatives and caught BPSS-3 near matches.
All 24 matching line contexts were inspected. Full target and near-match
scientific-name objects and the StrainInfo near-match object were read.

Pseudomonas PsS3 (870345), Alicyclobacillus PSS3 (1401523),
Paenibacillus PSS3 (1543400), and Arthrobacter BPSS-3 (3366580;
GCA/GCF_044628475.1) are distinct. StrainInfo SI-ID 125143 assigns
PSS 3 and IFO/NBRC 32851 to Colletotrichum acutatum (27357), not this
Rhodococcus. This was a near-match identity check, not another Eukaryota
record review. Numeric matches in GCA/GCF_050490915.1's ungapped
length concern Mycoplasmopsis bovis F13559; SAMEA1033916 is a
Streptococcus pneumoniae sample. None supports a target join.

A separate JF768732 search over the same ignored-inclusive roots
completed with zero matches. No eligible deposit or strain-genome
assertion for Rhodococcus PSS3 was found in that scope. Zero BacDive
entries does not deny the isolate's existence. A partial marker is not
a genome identifier; empty optional nomenclature, mappings, definition,
evidence and graph slots are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, source
attestation, strain inventory, status and inline provenance are supported.

## Recommended Edits

None. Preserve the generated YAML and SEEDED status. Future supported
corrections belong in maintained inventory inputs and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On source refresh, recheck the exact taxon and JF768732 for explicit
deposits or primary genomes. Do not join by PSS3 alone or substitute
the closest 16S match for source taxonomy. After authorized changes,
regenerate and run focused validators plus full `just verify-corpus`.
No unresolved blocker prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13806` locks the slug;
`curation/seed_scope.tsv:321679` supplies the September 13, 2026 date
and one-source reason. The event at `2026-09-13T17:54:04Z` exactly
reproduces the source list and reason. Ignored-inclusive filename
searches found no prior target report or target-specific history artifact.

iModulonDB is not applicable: the YAML asserts no gene, regulator,
expression module or mechanism. No paid research, outside contact,
GitHub mutation, generator run, status promotion or history event occurred.
