# YAML Record Review: Lactobacillus kefiranofaciens ZW3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lactobacillus_kefiranofaciens_zw3.yaml`
- Started UTC: 2026-10-04T19:25:34Z
- Finished UTC: 2026-10-04T19:28:17Z
- Verdict: pass

## Target

Reviewed the entire generated `TaxonRecord` for `NCBITaxon:1033837`,
Lactobacillus kefiranofaciens ZW3. It is a bacterial strain, directly parented
to the species `NCBITaxon:267818`, with `grounding_status: EXACT`,
`mapping_status: SEEDED`, genetic code 11, two NCBI exact synonyms,
`strain_count: 0`, and NCBITAXON and MADIN attestations. Its single seed event
is dated `2026-09-13T17:54:04Z`.

Only this target was reviewed. The species, subspecies and other records
mentioned below are source context, not additional completed record reviews.
All seeded fields remain read-only; this report makes no curation change.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/lactobacillus_kefiranofaciens_zw3.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/lactobacillus_kefiranofaciens_zw3.yaml`.
  One file scanned, zero files with errors, zero error rows. This is the
  implementation used by `just validate-strict`; its standard diagnostic
  output is `reports/instance_validation_failures.tsv`.
- Passed bounded, read-only structured comparisons against the complete
  backbone table and the direct source inventories: identity, all ten
  root-first ancestors, source counts, synonyms, scope, filename lock and
  seed-event wording agree with the record. No descendants were found in
  the complete backbone scan. These comparisons are not a substitute for
  the repository's byte-for-byte reproduction gate.
- Not run: `just verify-corpus`. Inspection of `scripts/verify_corpus.py`
  confirms that it rebuilds and compares the entire corpus; `--max-diffs`
  limits diagnostics, not the records checked. No focused equivalent was
  invented for this individual read-only review.
- Not applicable: `just validate-products`, which checks curator-added
  graph node identifiers and labels. This record has no causal graph.
  NCBI identity and lineage were checked directly at their authority instead.
- Not run: `just validate-history`. Ignored-inclusive history searches found
  no target-specific history artifact, and this review neither creates one
  nor promotes the record's lifecycle status. The inline seed event was
  checked. Full-corpus QC, provenance, rendering and test-suite gates were
  not run for this report-only review.

## Identity and Grounding

The pinned backbone row `data/raw/ncbitaxon_taxa.tsv:221315` agrees with the
identifier, label, STRAIN rank, BACTERIA bucket, direct species parent and
code 11. All ten ancestors match the pinned parent chain, including root,
cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli,
Lactobacillales, Lactobacillaceae, Lactobacillus and the parent species.

The live [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033837&retmode=xml)
independently confirms the strain name, rank, parent, code and both equivalent
names. The [NCBI Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033837)
confirms the same identifier and complete ancestor-ID list, including root.
The HTML taxonomy page yielded only its application shell; the structured
API responses, not that shell, support these conclusions.

The full native name objects at
`data/catalog/ncbi_names-0005.jsonl.gz:30648`, `:30649` and `:30650`
respectively identify the two equivalent names and the scientific name.
Their EXACT_SYNONYM placement is supported. Complete exact-ID scans of
`data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and
`data/raw/dropped.tsv` found no row for this taxon. This does not establish
that the strain is uncultured or universally unavailable.

A source-specific classification difference must be preserved. The strain
taxon remains directly under species `267818`, while the current assembly,
BioSample and GTDB metadata classify ZW3 under subspecies `190905`,
Lactobacillus kefiranofaciens subsp. kefiranofaciens. Assembly classification
does not authorize replacing this record's live NCBI taxon identity or
reparenting its lineage. BV-BRC and GOLD retain taxon `1033837` for their ZW3
entries. None of these source labels was silently reconciled.

## Evidence

| Record assertion | Inspected support and scope |
| --- | --- |
| NCBITAXON, one NAME | Backbone row 221315, native scientific-name object and live NCBI APIs agree. The note accurately names the pinned `2026-09-13` taxonomy snapshot. |
| MADIN, four TRAIT_ASSERTIONs | `data/raw/madin_taxa.tsv:636` contains exactly `NCBITaxon:1033837` and count 4. The YAML asserts an inventory count, not four reviewed phenotypes or experiments. |
| Zero classified BacDive strains | Complete backbone scan found no descendants; complete direct BacDive inventory scan found no row for this taxon. Native and accession searches below found no eligible culture-deposit link. |
| No GTDB mapping, synonym or attestation | The complete direct mapping scan found no mapping to `1033837`. The native ZW3 genome has `ncbi_taxid: 190905`, not this strain taxon. A bare strain name is not authority to move a mapping here. |
| Seed scope and provenance | `data/taxa/PATHS.tsv:13770` fixes this identifier-to-slug pair; `curation/seed_scope.tsv:57247` records the two-source scope reason. Inline history wording and source names match. |

The seed timestamp is supported by the newest of the three manifests used
by `src/taxonmech/seed.py:_seed_timestamp`: raw
`2026-09-13T17:50:44Z`, StrainInfo `2026-09-13T17:29:00Z`, and
AllTheBacteria `2026-09-13T17:54:04Z`. The direct MADIN attestation behavior
is implemented in `src/taxonmech/seed.py:616`; counts across unlike sources
were not added together.

Genome-source context was inspected in full, without promoting it to
unsupported strain links:

- The current [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000214785.1/dataset_report)
  identifies `GCA_000214785.1`, its current paired `GCF_000214785.1`, ZW3,
  subspecies taxon `190905`, BioSample `SAMN02603965` and project
  `PRJNA66525`. It reports a Complete Genome assembly with three component
  sequences and 2,354,088 bases. The BioSample supplies the bare strain
  designation but no registered culture-collection accession. Availability
  from a named laboratory in the assembly comment is not a culture-deposit
  identifier.
- Full native current assembly objects at
  `data/catalog/ncbi_genbank-0000.jsonl.gz:3535` and
  `data/catalog/ncbi_refseq-0000.jsonl.gz:3052` agree on these accessions,
  strain and classification. RefSeq retains its own project `PRJNA224116`.
  The exact `txid1033837[Organism:noexp]` Assembly search returned zero
  items with a phrase-not-found warning. That search is not evidence that
  ZW3 lacks a genome: the explicit accession resolves under another taxon.
- `data/catalog/gtdb_genomes-0002.jsonl.gz:21210` retains
  `RS_GCF_000214785.1`, the paired GenBank accession, the same BioSample,
  bare `ncbi_strain_identifiers: ZW3`, and the species classification
  `s__Lactobacillus kefiranofaciens`. It is not flagged as representative or
  type material. Raw GTDB species row 109335 reports 19 genomes; mapping
  rows 88908 and 206115 concern subspecies `190905` and species `267818`,
  respectively. Those aggregate species mappings were not copied to ZW3,
  and the 19-member cluster was not independently enumerated for this
  record, which asserts no GTDB count.
- The three full BV-BRC objects at
  `data/bvbrc/bvbrc-0000.jsonl.gz:3224`, `:3225` and `:3226` retain
  `patric:1033837.3` as Complete, `patric:1033837.6` as Plasmid and
  `patric:1033837.7` as Plasmid. All reference the same assembly, BioSample
  and project. The plasmid records respectively reference `CP002765` and
  `CP002766`; they must not be described as three independent complete
  genomes. No culture-collection field is supplied in these objects.
- GOLD's full organism row `data/gold/organisms.jsonl.gz:9875` retains
  `Go0011248`, ZW3 and taxon `1033837`, with an empty culture-collection
  field. Project row `data/gold/projects.jsonl.gz:9739` links `Gp0011248`
  to that organism and `PRJNA66525`. Analysis row
  `data/gold/analyses.jsonl.gz:19567` links `Ga0029202` through that project
  to `img.taxon:650716047` and the explicit assembly and three sequence
  accessions. Its analysis-organism field is empty. The catalog preserves
  this chain, but it supplies no eligible deposit match to a BacDive strain.
  The direct GOLD attestation inventory has no row for this taxon; native
  catalog presence alone does not create such an attestation.

The native assembly metadata references
[PMID 21705607](https://pubmed.ncbi.nlm.nih.gov/21705607/), the ZW3 genome
paper. Its PubMed XML was read and confirms the title, DOI
`10.1128/JB.05306-11`, and `CP002764`, `CP002765`, `CP002766` accession list.
Full text was not inspected: the Europe PMC fullTextXML endpoint returned
HTTP 500 after retries, and the PMC HTML fallback returned a browser check.
No mechanism, phenotype or detailed chromosome/plasmid conclusion is
attributed to uninspected full text. The source-specific plasmid descriptions
above are from the inspected BV-BRC objects.

## Completeness

Ignored-inclusive, compressed-content searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`,
`data/atb`, `curation` and `history`, excluding only `SOURCE.json` manifest
files. The first search covered taxon ID, slug and token-bounded `ZW3`
and completed with 33 matching lines; the follow-up covered
`SAMN02603965`, both assembly accession stems, and `CP002764`, `CP002765`,
`CP002766`, completing with seven matching lines. All returned contexts
were inspected; relevant native JSON objects were then read in full.

These bounded searches found no eligible BacDive culture-deposit match,
StrainInfo sequence/deposit assertion, or AllTheBacteria link for ZW3.
Excluded near misses include Phyllobacterium sp. ZW3-1, unrelated numeric
IMG/assembly identifiers and the unrelated sample `SAMEA1033837`.
The statement is about the inspected local snapshots and searches, not a
claim that no future or external culture deposit can exist.

An ignored-independent filename search over `data/taxa`, review reports,
`history` and `curation` found this target YAML and no pre-existing
target-stem report or history filename before this report was created.
History content was also included in the source searches above.

No consequential missing required representation was established. There
are no directly mapped LPSN nomenclature entries, GTDB mappings, MediaDive,
GOLD or BactoTraits attestations in the corresponding complete inventory
scans for this taxon. It is correct not to borrow the parent species'
nomenclature, type strain or mappings. Optional definition, literature
evidence, discussions, datasets and causal graphs need not be invented for
this seeded identity record. Source-native genome availability is not proof
of an eligible missing BacDive strain link.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed assertions. The live assembly/taxonomy
classification difference and the complete-genome versus plasmid source
records are preserved as context, not errors in fields the YAML does not
assert. The skipped full-corpus gates and unavailable paper full text limit
the checks performed; they are not reported as successful checks.

## Recommended Edits

None required for this record on the inspected evidence. Do not hand-edit
its generated YAML, infer a registered culture deposit from `ZW3`, move the
assembly's subspecies classification into its lineage, attach parent-level
GTDB identity mappings, or promote `mapping_status` to REVIEWED.

If future primary evidence supplies an eligible deposit, the maintained
source extraction and strain-matching paths own any resulting addition:
`scripts/extract_source_inventory.py`, `src/taxonmech/seed.py` and their
tests, followed by the documented inventory and seeding workflow. An
upstream classification change belongs to its source authority, not to an
ad hoc YAML override. None of these changes is authorized by this review.

## Follow-up Checks

- For a future source refresh, recheck both the strain Taxonomy response
  and the assembly's separately supplied organism classification.
- Before any future genome link, verify a whole registered culture-deposit
  identifier and its explicit source chain. Preserve the BV-BRC plasmid
  descriptions, accession versions and distinct sample/project identifiers.
- After any authorized curation or generator change, run the documented
  single-record schema and strict validators, relevant matching tests and
  the full `just verify-corpus` gate. No focused reproduction gate is claimed.
- Reopen the genome paper's full text only if future curation requires
  claims beyond the inspected metadata and abstract. It is not required
  to justify the existing name/count-only record.

## Additional Notes

This report follows the read-only review skill and its field checklist.
No taxon YAML, inventory, generated page, source transform, prior report,
history entry or lifecycle field was edited. No paid research or GitHub
mutation was performed. Eukaryota coverage was not changed.

iModulonDB is not applicable: the target asserts no gene, locus, regulator,
pathway, stress response, phenotype or transcriptomics dataset requiring a
structured expression-module cross-check. Absence from that resource is
not used as negative evidence. No causal graph is required here.
