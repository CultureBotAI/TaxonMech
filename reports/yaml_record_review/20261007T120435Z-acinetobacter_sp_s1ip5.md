# YAML Record Review: Acinetobacter sp. S1IP5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_s1ip5.yaml`
- Started UTC: 2026-10-07T11:59:36Z
- Finished UTC: 2026-10-07T12:04:35Z
- Verdict: pass

## Target

Complete generated `TaxonRecord` for `NCBITaxon:1035889`, label
`Acinetobacter sp. S1IP5`, rank `SPECIES`, domain `BACTERIA`.
Read the entire YAML. It has ten lineage entries, exact grounding, seeded
mapping status, genetic code 11, strain count zero, one NCBI name
attestation and one inline seed event. It carries no phenotype, genome,
culture-deposit, nomenclature, mapping, literature or causal-graph claims.

Generated values are owned by committed source inventories and
`scripts/seed_from_sources.py`; scope is owned by
`curation/seed_scope.tsv`. The YAML is not a maintained editing surface.

## Validation

- `just validate data/taxa/bacteria/acinetobacter_sp_s1ip5.yaml`: passed;
  LinkML reported no issues.
- `just validate-strict data/taxa/bacteria/acinetobacter_sp_s1ip5.yaml --out /private/tmp/s1ip5-strict.tsv`:
  passed; one file, zero errors. Inspected the header-only output TSV.
- Complete local target-row, lineage, scope, path-index, attestation and
  inline-history comparisons passed. These manual source checks are not a
  substitute for full-corpus reproduction.
- Live NCBI Taxonomy EFetch and Datasets identity/reference checks passed.
- `just validate-products`: not applicable; no curator-added graph nodes.
- Separate history validation: not applicable; the bounded ignored-inclusive
  content and filename searches found no matching standalone history record.
  The inline event was checked against the source manifests and scope.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`,
  `just validate-all`, `just provenance-check`, `just render-check`,
  `just docs-check` and `just vendored-check`. This is an individual
  read-only review, not certification of the entire corpus or generated site.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222189` and
native name row at `data/catalog/ncbi_names-0005.jsonl.gz:31680` agree on
the identifier and scientific name. The parent is
`NCBITaxon:196816`, unclassified Acinetobacter.

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035889&retmode=xml)
confirms the name, species rank, parent, bacterial division and genetic code 11.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035889)
independently agrees on the name, rank and full ancestor identifier list.

Every ancestor identifier, label and rank matches the local backbone and
live lineage: root, cellular organisms, Bacteria, Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Moraxellales, Moraxellaceae,
Acinetobacter and unclassified Acinetobacter. Root is retained in the local
and Datasets chains; EFetch's displayed lineage starts at cellular organisms.
This is a carried NCBI placement, not a reconciled taxonomy.

The source has no synonyms or retired-into value for this node. Exact
type-material, merged-ID and dropped-record inventory checks found no target
rows. No local child nodes were found. Species rank makes this node eligible
for the repository even though its scientific name uses an isolate label;
it does not establish a formally named species or deposited type strain.

Expanded searches also found S1IP11 (`NCBITaxon:1031574`) and S1IP14
(`NCBITaxon:1031575`). Their complete backbone, native-name and scope rows
were inspected. These are different NCBI nodes, not aliases of S1IP5;
similar prefixes do not justify transferring their evidence.

## Evidence

The NCBI attestation correctly counts one `NAME`, not a strain or genome.
The snapshot date is 2026-09-13. Scope row 322450 and path-index row 14688
agree with the identifier, slug and inline event wording. The seed timestamp
2026-09-13T17:54:04Z agrees with the latest applicable extraction timestamp
under the seeder's manifest rule.

No exact target rows were found in the seven inspected raw inventories for
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. With no BacDive
subtree records, `strain_count: 0` is faithful to this inventory. It is not
a claim that the biological isolate never existed.

Exact `txid1035889[Organism:noexp]` NCBI searches returned one nucleotide
record and no assembly records. The assembly response also reported the
organism phrase as not found; this is a bounded database-query result, not
proof that no assembly exists under another classification.

The complete metadata, features and references for
[GenBank JF743669.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333973150)
were inspected, excluding the sequence payload. This is a 727-base partial
16S rRNA sequence explicitly assigned to taxon 1035889 and strain S1IP5.
Its source qualifiers identify intestine and host Salmo salar. It supplies
no culture-collection deposit, assembly, BioSample or BioProject identifier.
The submission address is not an isolation-locality assertion. A partial
rRNA marker is not a genome and cannot establish genome equivalence.

GenBank cites Godoy and colleagues' 2015 study. The
[publisher's abstract and bibliographic metadata](https://link.springer.com/article/10.1007/s13213-015-1076-3)
confirm DOI `10.1007/s13213-015-1076-3`, Annals of Microbiology volume 65,
pages 2343-2353, and publication on 16 April 2015. The study concerns salmon
intestinal microbiota examined by culture and culture-independent methods.
The inspected abstract does not name S1IP5 or its accession; GenBank supplies
the sequence-to-publication association. Full methods, results and figures
were not retrieved because the publisher offered subscription-only full text.
No strain-specific medium, phenotype, abundance, pathogenicity or resistance
claim is inferred from the abstract or from properties of the genus.

These are optional external enrichment leads, not unsupported assertions
already present in the YAML. iModulonDB is not applicable to this bare
taxonomic record: it names no expression dataset, regulator, functional
gene claim or causal mechanism requiring that adapter.

## Completeness

Complete enough for the current minimal, source-seeded record. Optional
synonyms, nomenclature, mappings, strain deposits, genome links and causal
claims are appropriately unpopulated given the inspected evidence.

Absence checks included ignored and hidden files and compressed text through
`rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`.
Queries used the bounded numeric taxon ID, scientific name, slug and
S1IP5 separator variants, then added JF743669 and similarly named
Acinetobacter S1IP isolates. All nine matching source rows were read in full,
including the six near-name rows. The five source-native `SOURCE.json`
files were parsed separately in full; no matching metadata values were found.
History filenames were independently checked with ignored files included.

Within those searched roots there was no additional target source evidence
or accession-specific match. This does not inventory all external databases,
arbitrary binary snapshots or the unpublished/full-text literature.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The YAML faithfully represents the pinned evidence and agrees
with current primary taxonomy. Full-text access limits optional enrichment;
it does not undermine the existing taxonomic assertions.

## Recommended Edits

None required. Do not hand-edit this generated YAML or promote its mapping
status on the basis of this review.

Future sequence or host enrichment should first define a supported maintained
source representation and explicit provenance. A bare strain label or shared
taxon ID must not become a culture-deposit or strain-genome join key. Keep a
partial rRNA accession outside genome counts. Future seed behavior would be
owned by the maintained source adapter and `scripts/seed_from_sources.py`,
with tests; source identity corrections belong upstream at NCBI.

## Follow-up Checks

For any later enrichment, inspect the full primary paper and isolate-specific
support before assigning culture conditions or phenotypes. Verify the exact
accession, source taxon, strain ownership and identifier type. Require an
eligible culture-deposit match and explicit source chain for genome links.

After an authorized maintained-input change, use the documented dry-run and
canary workflow, rerun both focused validators and the relevant tests, then
run full `just verify-corpus` and publication/QC gates as appropriate.
No regeneration or curation mutation was performed in this review.

## Additional Notes

Review conducted on `codex/record-review-extensimonas-20261003` at
`b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Existing worktrees were preserved.
The report is the only new repository artifact from this individual review;
the target YAML, source inventories, scope, generated site, statuses,
history and GitHub state were not changed.

