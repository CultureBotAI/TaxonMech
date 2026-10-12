# YAML Record Review: Pseudomonas sp. BPTK3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_bptk3.yaml`
- Started UTC: 2026-10-04T19:39:33Z
- Finished UTC: 2026-10-04T19:40:47Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033848`,
Pseudomonas sp. BPTK3. It carries SPECIES rank, BACTERIA domain, parent
`NCBITaxon:196821`, ten lineage entries, EXACT grounding, SEEDED lifecycle
status, genetic code 11, zero classified BacDive strains, one NCBITAXON
NAME attestation and one seed event.

Only this record was reviewed. No evidence was transferred from BPTK2 or
another similarly designated isolate. There are no asserted nomenclature,
synonym, cross-taxonomy mapping, genome, literature or causal-graph entries.
The generated YAML remains unchanged.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_bptk3.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_bptk3.yaml`.
  One file scanned, zero files with errors and zero error rows. This is the
  implementation used by `just validate-strict`; it emits the standard
  `reports/instance_validation_failures.tsv` diagnostic.
- Passed bounded structured comparisons with the backbone, direct source
  inventories, PATHS lock and scope. Identifier, label, rank, code, all ten
  ancestors, sole attestation and seed-event wording agree. A complete
  backbone scan found no child taxa.
- Not run: `just verify-corpus`, the full-corpus byte-for-byte reproduction
  gate. Its `--max-diffs` option limits diagnostics, not records checked.
  The bounded comparisons above are not a focused replacement for that gate.
- Not applicable: `just validate-products`; there are no curator-added
  graph nodes. NCBI identifier/label and lineage checks used source APIs.
- Not run: `just validate-history`. Ignored-inclusive searches found no
  target-specific history artifact, and this read-only review creates no
  history or lifecycle event. The inline seed event was checked. Full-corpus
  QC, provenance, rendering and test-suite gates were not run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221319` matches the entire identity layer.
The live [NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033848&retmode=xml)
confirms the label, species rank, bacterial division, parent 196821 and
code 11. Its named lineage agrees with the record, including Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas and the unranked direct parent, unclassified Pseudomonas.
The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033848)
also confirms all ten ancestor IDs, including root.

The complete native object at
`data/catalog/ncbi_names-0005.jsonl.gz:30655` is the scientific-name entry
for this identifier. The source backbone has empty synonym fields and
the live Taxonomy response supplies no alternative names. Complete
exact-ID scans found no row in `data/raw/ncbi_type_material.tsv`,
`data/raw/ncbi_merged_ids.tsv` or `data/raw/dropped.tsv`.

The informal `sp.` label and strain designation do not override the source's
explicit SPECIES rank. Likewise, having an unranked parent does not make
this species-rank record ineligible. EXACT means exact grounding to this
NCBI concept, not a claim of valid publication under the ICNP or assignment
to a formally named Pseudomonas species.

## Evidence

The one NCBITAXON attestation has the correct ID, label, count 1, NAME unit
and `2026-09-13` snapshot note. Backbone row 221319 and native name row
30655 support precisely that assertion. A NAME count is not a genome,
phenotype, deposit or experiment count.

`data/taxa/PATHS.tsv:13774` fixes this identifier-to-slug pair.
`curation/seed_scope.tsv:321650` supplies the one-source scope reason
reproduced in the inline seed event. The event timestamp
`2026-09-13T17:54:04Z` agrees with the newest manifest used by the seeder:
raw `17:50:44Z`, StrainInfo `17:29:00Z`, and AllTheBacteria `17:54:04Z`,
all on `2026-09-13`. The standard inventory wording does not assert that
BPTK3 itself has an ATB or StrainInfo association.

An independent exact-taxonomy NCBI sequence check found one nucleotide
record. Its GenBank metadata and feature table were read through EFetch,
excluding the DNA string itself:

- [JF749815.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF749815.1&rettype=gb&retmode=xml)
  identify a 946-base partial 16S rRNA gene sequence of Pseudomonas sp.
  BPTK3. Its source feature explicitly gives strain BPTK3 and
  `taxon:1033848`; the rRNA feature is partial at both ends.
- The reference is a direct submission, and the source metadata include
  an isolation-source qualifier. Neither supplies a culture-collection
  accession, a genome assembly or a general species-level phenotype.
- The exact Assembly query `txid1033848[Organism:noexp]` returned zero
  results and a phrase-not-found warning. This is a bounded exact-index
  result, not proof that no differently classified or unsubmitted genome
  could exist. The exact nucleotide query returned one result, so all
  returned nucleotide metadata were inspected without a pagination gap.

The marker independently supports the identity but does not justify
changing the Taxonomy rank, minting a BacDive strain or adding a genome
link. No publication, quotation or mechanism claim is asserted by the YAML.
The nucleotide HTML page was inaccessible through the web tool; the
successful NCBI XML retrieval supplies the evidence, not the unviewed page.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` across
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifest files. The ID, BPTK3 token and slug
search completed with six matching lines. All returned contexts were read.
The three relevant results were scope, backbone and native scientific name.

The other matches were not identity evidence: `1033848` is a genome-length
value in unrelated GenBank and GTDB entries for `GCA_964458735.1`, and
`SAMEA1033848` is an unrelated Streptococcus pneumoniae sample. Numeric
coincidence does not link those entries to this NCBI taxon. A separate
`JF749815` search over the same ignored-inclusive roots completed with zero
matches (`rg` exit 1, a normal no-match result). That local absence does
not contradict the inspected live marker record.

Complete direct inventory scans found no BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits row for the taxon. With no descendant taxa,
there is no omitted descendant BacDive strain to gather. The broader native
source searches established no eligible culture-deposit, StrainInfo or
genome link requiring a strain entry. These findings are bounded to the
inspected local snapshots and searches, not a universal claim about all
external collections or future sequences.

An ignored-independent filename search over reports, history and curation
found no pre-existing target-stem artifact; history content was also
included in the ID/name/slug search. The unique PATHS entry and complete
YAML read establish the single target.

No consequential required-field gap was found. `strain_count: 0` means
zero classified BacDive records, not zero biological isolates. Optional
nomenclature, mappings, synonyms, definition, record-level evidence,
datasets, discussions and causal graphs can properly remain empty in this
NCBI-only seeded identity record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed assertions. The record accurately reflects its
limited source support. Neither the negative Assembly query nor the
partial marker establishes broader biological conclusions or corpus
reproducibility.

## Recommended Edits

None required on the inspected evidence. Preserve the generated rank,
lineage, source count and SEEDED status. Do not hand-edit in a named species
assignment, registered culture deposit, genome or type-material designation.

Future source corrections belong to the source authority and maintained
extraction/seeding paths, including `scripts/extract_source_inventory.py`,
`src/taxonmech/seed.py` and the relevant source-matching code and tests.
`curation/seed_scope.tsv` owns corpus inclusion. No curation change is
authorized by this report.

## Follow-up Checks

- During a future refresh, re-resolve this exact NCBI identifier and its
  full lineage before altering rank or parentage.
- Require an explicit eligible source/deposit chain for a future
  strain-genome association. Keep partial marker evidence outside genome
  counts and do not use another BPTK isolate's evidence.
- After authorized changes, run single-record schema and strict validation,
  relevant focused tests and full `just verify-corpus`. Validate a history
  artifact only if later curation actually creates one.

## Additional Notes

This review follows the local skill, write boundaries and checklist. Only
this new Markdown report was manually written. Taxon records, inventories,
code, pages, prior reports and history were left unchanged; no paid research
or GitHub mutation was performed. Eukaryota coverage was not changed.

iModulonDB is not applicable: there is no asserted gene, locus, regulator,
pathway, stress response or transcriptomics dataset requiring an expression
module check. The external marker sequence does not create such an assertion.
