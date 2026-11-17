# YAML Record Review: Wolbachia endosymbiont of Plagiolepis sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_plagiolepis_sp.yaml`
- Started UTC: 2026-10-07T12:37:47Z
- Finished UTC: 2026-10-07T12:40:17Z
- Verdict: pass

## Target

Complete generated `TaxonRecord` for `NCBITaxon:1035896`,
Wolbachia endosymbiont of Plagiolepis sp., read in full before judging.
It carries SPECIES rank, BACTERIA domain, eleven lineage entries,
EXACT grounding, SEEDED status, genetic code 11, strain count zero,
one NCBI NAME attestation and one inline seed event.
It contains no synonyms, nomenclature, alternative mappings, strain
deposits, genomes, literature assertions, phenotypes or causal graph.

The identity is a bacterial taxonomy node, not the named insect host.
Generated fields are owned by source inventories and
`src/taxonmech/seed.py`; inclusion belongs to `curation/seed_scope.tsv`.
This review does not authorize hand-editing generated YAML.

## Validation

- `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_plagiolepis_sp.yaml`:
  passed with no LinkML issues.
- `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_plagiolepis_sp.yaml --out /private/tmp/wol-plagiolepis-strict.tsv`:
  passed; one file, zero errors. The complete TSV is header-only.
- Complete target/backbone, lineage, source-inventory, path-index,
  scope and inline-history comparisons passed.
- Live NCBI EFetch and Datasets checks agreed for the target; the
  similarly named Plagiolepis undet node was separately resolved.
- `just validate-products`: not applicable; no curator-added graph nodes.
- Standalone history validation: not applicable; ignored-inclusive history
  content and filename checks found no matching separate history record.
  The inline seed event was checked without adding a review event.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`,
  `just validate-all`, `just provenance-check`, `just render-check`,
  `just docs-check` and `just vendored-check`.
  Focused checks do not certify corpus reproduction or the generated site.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222195`
and scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31690` support the identifier,
label, rank, parent and genetic code. Synonym and retired-into fields
are empty.

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035896&retmode=xml)
confirms the active identifier, scientific name, species rank, bacterial
division, parent `NCBITaxon:2640676` (unclassified Wolbachia) and
genetic code 11, with no other names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035896)
agrees on all eleven ancestor identifiers, including root.
Ancestor labels and ranks match the pinned backbone and live lineage,
including Wolbachieae at TRIBE rank.

No target child, merged-ID, dropped-record or type-material rows were
found in the checked inventories. Species rank satisfies repository
scope; it does not establish a formally named bacterial species or a
culture-deposited type strain. The host-bearing name is retained without
inferring a host species identifier, host range or phenotype.

Eight other local nodes matched the Plagiolepis name pattern:
526625 (madecassa), 1094262 (MU01), 1414346 (MG01),
1414347 (MG05), 1414348 (alluaudi), 1414349 (undet),
1418553 (sp. MG01), and 1874325 (Lepisiota rothneyi, with a
Plagiolepis rothneyi synonym). Their full matching backbone and native
name rows were inspected. All are separate sibling identifiers, not
descendants or established synonyms of this target.

The particularly similar
[Plagiolepis undet node, NCBI 1414349](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1414349&retmode=xml),
also checked through Datasets, remains a separate active node under
the same parent. Neither authority response equates it with 1035896.
Similarity between "sp." and "undet" is not sufficient merger evidence.
This is database-identity disambiguation, not proof that each node
represents a biologically distinct species.

## Evidence

The sole NCBI attestation correctly counts one NAME for the exact target
from the 2026-09-13 snapshot. Full exact-target checks of BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found
no target rows. With no BacDive record in the target subtree,
`strain_count: 0` is the correct source-record count, not a claim that
no infected specimen or bacterial lineage exists.

Path-index row 14694 and scope row 322455 match the identifier, slug and
inclusion reason. The inline seed event correctly names NCBITAXON and
the scope reason. Its 2026-09-13T17:54:04Z timestamp is the latest of
the raw, ATB and StrainInfo extraction timestamps, consistent with
the inspected `_seed_timestamp()` implementation.

Exact `txid1035896[Organism:noexp]` queries returned zero Assembly
records and one Nuccore record. Assembly also reported the organism
phrase as not found. This is a bounded index result, not proof that
no genome exists anywhere.

[Complete GenBank metadata for KF606430.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=557639374)
identify a 444-base partial hcpA coding sequence annotated as DUF28
protein, protein AHA14163.1, explicitly assigned to taxon 1035896.
All metadata, features and references were read, excluding nucleotide
and translation payloads. The source records host Plagiolepis sp.,
voucher JDWAM474-05.w and BOLD ASFTA1406-12.hcpA.
It reports a specimen from Foret Ambato near Ambanja, Madagascar,
collected 09-Dec-2004 by B. L. Fisher, with Alex Smith as identifier.

This is a marker sequence with specimen context, not a genome assembly
or microbial culture-deposit assertion. Its collection locality and
protein annotation do not justify a taxon-level phenotype, habitat,
reproductive effect or mechanism claim. The record correctly contains
none of those assertions.

The accession cites Tsoi, Smith and Fisher's "Patterns of Intraspecific
Variation as Influenced by Dispersal in Malagasy Ants" as Unpublished,
plus a direct submission dated 30-Aug-2013. Exact-title and accession web
searches did not establish a matching primary publication. This is an
unresolved bibliography lead, not proof that no publication exists.
BOLD and the manuscript were not independently inspected; GenBank is the
authority used for the accession metadata. The YAML itself cites no
literature claim requiring them.

iModulonDB is not applicable to the bare taxonomy record. An optional
external marker annotation does not create a transcriptomic assertion
or a required gene-function field.

## Completeness

Complete enough for the current minimal seeded representation.
Optional synonyms, nomenclature, mappings, strain deposits, genomes,
phenotypes and causal edges should not be invented from the marker or
similarly named nodes.

Ignored and hidden files, including compressed text, were searched with
`rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`.
The queries covered the bounded numeric ID, scientific name, slug and
Wolbachia/Plagiolepis near names, then KF606430, AHA14163,
JDWAM474-05 and ASFTA1406-12.

All 27 matching rows were read in full: eight scope rows, nine backbone
rows, nine native name rows and one assembly-catalog row.
The expanded accession/voucher search returned the same addresses.
Five native `SOURCE.json` files were parsed separately and history
filenames were independently searched; neither supplied additional matches.

The assembly hit at `data/catalog/ncbi_genbank-0050.jsonl.gz:44430`
is GCA_055092335.1, Candidatus Nitrosopumilus sp., taxon 2024843,
isolate MF1_202108_bin_429. Its genome size and ungapped genome size
are 1035896. This numeric collision is not Wolbachia evidence and
must not supply a strain-genome link.

No additional target source evidence, eligible culture-deposit link or
matching standalone history was found within those bounded roots and
metadata files. This statement does not cover every external database
or arbitrary binary artifact.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Current authority and pinned inventories support the record's
material assertions. Optional marker and bibliography leads do not
invalidate the faithful minimal representation.

## Recommended Edits

None required. Do not hand-edit the generated YAML, substitute a marker
count for the BacDive count or promote SEEDED status.

Future taxonomy corrections belong at the authoritative upstream source,
followed by the maintained extraction/seeding workflow. Optional sequence
enrichment requires an authorized maintained input and preservation of
marker, specimen, taxon and culture-deposit identity. No unsupported
host-species or phenotype inference should be added.

## Follow-up Checks

Before optional enrichment, verify current accession assignments and any
exact publication, specimen and culture-deposit links. Recheck the separate
undet node before proposing any identity consolidation.

After authorized maintained-input changes, use the documented seed dry-run
and canary workflow, both focused validators, relevant tests and full
corpus-reproduction/QC gates. No regeneration was performed here.

## Additional Notes

Reviewed on `codex/record-review-extensimonas-20261003` at
`b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
The YAML is byte-for-byte unchanged. Only this new report was written
for this record. Source inventories, scope, statuses, history,
generated pages, existing worktrees and GitHub were not modified.

