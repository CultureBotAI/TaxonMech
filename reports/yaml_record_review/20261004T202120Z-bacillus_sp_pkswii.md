# YAML Record Review: Bacillus sp. PKSWII

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_pkswii.yaml`
- Started UTC: 2026-10-04T20:19:36Z
- Finished UTC: 2026-10-04T20:21:20Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033897`,
Bacillus sp. PKSWII. It is a bacterial SPECIES-rank placeholder under
`NCBITaxon:185979`, with ten ancestors, genetic code 11, EXACT grounding,
SEEDED status, zero inventoried BacDive strains, one NCBITAXON NAME
attestation and one seed event. No record, input, code or history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacillus_sp_pkswii.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/bacillus_sp_pkswii.yaml`; one file, zero errors. This is the `just validate-strict` implementation and emits the standard `reports/instance_validation_failures.tsv` diagnostic.
- Bounded structured comparisons passed for identity, complete lineage,
  directly mapped inventories, scope, filename lock and seed wording.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` only limits
  diagnostics, not verification scope. Bounded comparisons are not proof
  of byte-identical regeneration. Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, because no curator graph nodes
  are asserted. NCBI identifiers were checked against primary sources.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline seed event was inspected.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:221331`, full native name
object at `data/catalog/ncbi_names-0005.jsonl.gz:30671`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033897&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033897)
agree on identity, label, rank, bacterial domain, parent and genetic code.
The ten ancestor IDs match, including root 1; live expanded labels and
ranks agree where supplied. The parent is unclassified Bacillus below
Bacillus, Bacillaceae, Caryophanales, Bacilli, Bacillota and Bacillati.

SPECIES is NCBI's rank, not a claim of valid nomenclatural publication.
PKSWII is a laboratory designation, not a registered deposit accession.
PKSWIII is a distinct source concept, `NCBITaxon:1033898`; its full native
name object at line 30672 was inspected and not merged into this target.
No synonyms are supplied by the target native name object or backbone.
Complete exact-ID type-material, merged-ID and dropped-taxon scans found
no rows; live taxonomy supplies no successor or identity correction.

## Evidence

The sole attestation matches NCBI's ID and label, one NAME assertion and
snapshot `2026-09-13`. Complete directly mapped BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin and BactoTraits scans returned no target rows. A complete
backbone scan found no children, so the descendant-inclusive BacDive
strain count is also zero.

The exact-taxonomy nuccore search returned one entry. Its full metadata,
references and feature qualifiers identify
[JF768713.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768713.1&rettype=gb&retmode=xml)
as a 1,467-base partial 16S rRNA sequence for strain PKSWII,
taxon 1033897, from a uranium-rich site at Domiasiat, India. It provides
no registered culture deposit, BioSample or assembly identifier.

The marker cites [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`. Its metadata and article body were inspected
earlier in the ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes, the PKSWII row and inherited merged cells:
JF768713, 1,467 bases, closest match Bacillus thuringiensis at greater
than 99.8% similarity. This sequence-similarity context does not establish
taxonomic equivalence or a deposit. Supplementary PDF content was not
inspected; no phenotype or causal claim is imported into this record.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033897[Organism:noexp]`. This bounded result is not
global proof of genome absence. Taxonomy Browser HTML was inaccessible;
both direct NCBI taxonomy APIs succeeded.

## Completeness

Ignored-inclusive, compressed-content searches used
`rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`,
`data/atb`, `curation` and `history`, excluding only `SOURCE.json` manifests.
The taxon, label, slug and designation-variant search produced 14 matching
lines; all matching contexts were inspected. Three were the target's
backbone, scope and scientific name. Three belonged to PKSWIII. Five
matched sample SAMEA1033897 for Streptococcus pneumoniae, and three
matched a genome length of 1033897 for Mycoplasmopsis bovis. These are
not target strain/genome evidence. A separate JF768713 search across
the same ignored-inclusive roots completed with zero matches.

No eligible deposit or strain-to-genome assertion was found in that
scope. Zero BacDive inventory entries does not mean no biological isolate
exists. A partial 16S sequence is not a missing genome assembly. Empty
optional nomenclature, mapping, definition, record-level evidence and
causal-graph slots are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, strain count,
attestation, status and inline provenance are supported. Near-matching
names, samples and numeric lengths do not justify additional joins.

## Recommended Edits

None. Do not patch the generated YAML or promote its status. Future
source corrections belong in the maintained inventory pipeline,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py` as appropriate;
scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Recheck PKSWII and JF768713 on source refresh for explicit registered
deposits or primary genome evidence. Keep PKSWIII separate. After any
authorized input change, rerun focused validators and the full
`just verify-corpus` gate after regeneration. No unresolved blocker
prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13787` fixes the slug.
`curation/seed_scope.tsv:321661` supplies the September 13, 2026 scope
addition and one-source reason. The seed event at `2026-09-13T17:54:04Z`
preserves that reason and NCBITAXON source list. Ignored-inclusive
report/history/curation filename searches found no prior target report
or target-specific history artifact before this report was created.

iModulonDB is not applicable: this record asserts no gene, expression
module, regulator or mechanism. No paid research, outside contact,
GitHub mutation, generator run or history event occurred.
