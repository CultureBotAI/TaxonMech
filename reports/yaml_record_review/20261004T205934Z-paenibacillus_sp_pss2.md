# YAML Record Review: Paenibacillus sp. PSS2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_pss2.yaml`
- Started UTC: 2026-10-04T20:58:12Z
- Finished UTC: 2026-10-04T20:59:34Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033912`,
Paenibacillus sp. PSS2. It asserts SPECIES, BACTERIA, parent
`NCBITaxon:185978`, ten ancestors, code 11, EXACT grounding, SEEDED
status, zero inventoried BacDive strains, one NCBITAXON NAME attestation
and one inline seed event. No YAML, code, input, status or history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_sp_pss2.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_sp_pss2.yaml`; one file, zero errors. This is the implementation of `just validate-strict`, producing `reports/instance_validation_failures.tsv`.
- Bounded identity, lineage, mapped-source, scope, filename and event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` caps diagnostics, not scope. Bounded comparisons are not byte-level reproduction. Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, as no curator graph nodes are asserted. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. The inline event was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221346`, full scientific-name object
`data/catalog/ncbi_names-0005.jsonl.gz:30686`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033912&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033912)
agree on the exact taxon, label, rank, domain, parent and genetic code.
All ten lineage IDs match; expanded labels and ranks agree where supplied.
The chain includes Bacillati, Bacillota, Bacilli, Caryophanales,
Paenibacillaceae, Paenibacillus and unclassified Paenibacillus.
SPECIES is an NCBI placeholder rank, not formal nomenclatural validity.

Backbone and native name object supply no synonyms. Complete exact-ID
type-material, merged-ID and dropped-taxon scans returned no rows.
Live taxonomy supplies no replacement or synonym requiring a change.
PSS2 alone is not a registered culture accession or a globally unique name.

## Evidence

The sole attestation exactly matches the NCBI identifier, label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans found no target
rows. A complete backbone scan found no children, so zero is also the
descendant-inclusive BacDive count.

Exact-taxonomy nuccore search returned two entries; all metadata,
references and feature qualifiers were inspected:

- [JF768727.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768727.1&rettype=gb&retmode=xml): 1,469-base partial 16S rRNA, strain PSS2, taxon 1033912, uranium-rich site in Domiasiat, India.
- [JN034435.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JN034435.1&rettype=gb&retmode=xml): 621-base partial CDS assigned to the same strain and taxon, annotated as a heavy-metal-transporting P-type ATPase with similarity to zntA/cadA, protein qualifier `AEI91705.1`, code 11. Its references are an unpublished study and a May 18, 2011 direct submission. Annotation alone is not direct causal proof.

Neither entry supplies a registered deposit, BioSample or assembly.
The 16S entry cites [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`. Article metadata and body were inspected
earlier in this ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes and the PSS2/JF768727 row: 1,469 bases and
closest match Paenibacillus pabuli at greater than 99.3% similarity.
This is marker context, not a formal merger, deposit or genome identity.
No phenotype or mechanism is asserted by the YAML or imported here.
The supplementary PDF was not inspected.

Exact-taxonomy Assembly search returned zero, with a `phrasesnotfound`
warning for `txid1033912[Organism:noexp]`; this is not proof of genome
absence under every possible classification.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json`. ID, label, slug and designation patterns
included Roman-II/digit-2 alternatives. All 40 matching line contexts
were inspected. Full target and near-match scientific-name objects and
the GOLD Geobacillus organism object were read separately.

The search distinguished Pseudomonas PsS2 (870339), Geobacillus sp.
PSS2 (1401537), and Geobacillus subterraneus PSS2 (1382357), whose
GCA/GCF_000744755.1 and SAMN02744825 evidence is not this record's.
GOLD's Geobacillus icigianus PSS2 (1430331), Cyanophage PSS2, and
Escherichia coli PSS2-suffixed isolates are likewise not valid joins.
Numeric matches in unrelated genome lengths and SAMEA1033912
(Streptococcus pneumoniae) were excluded.

A separate JF768727/JN034435/AEI91705 search over the same ignored-inclusive
roots completed with zero matches. No eligible deposit or strain-genome
assertion for this Paenibacillus PSS2 was found in that scope.
Zero BacDive entries does not deny the isolate's existence. Partial
sequences are not genome identifiers; empty optional nomenclature,
mappings, definition, evidence and graph slots are appropriate for this seed.

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

On source refresh, recheck the exact taxon and both nucleotide accessions
for explicit deposits or primary genomes. Do not join by PSS2 alone or
promote ATPase similarity to a demonstrated mechanism. After authorized
changes, regenerate and run focused validators plus full `just verify-corpus`.
No unresolved blocker prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13802` locks the slug;
`curation/seed_scope.tsv:321675` supplies the September 13, 2026 date
and one-source reason. The event at `2026-09-13T17:54:04Z` exactly
reproduces the source list and reason. Ignored-inclusive filename
searches found no prior target report or target-specific history artifact.

iModulonDB is not applicable: the YAML asserts no gene, regulator,
expression module or mechanism. No paid research, outside contact,
GitHub mutation, generator run, status promotion or history event occurred.
