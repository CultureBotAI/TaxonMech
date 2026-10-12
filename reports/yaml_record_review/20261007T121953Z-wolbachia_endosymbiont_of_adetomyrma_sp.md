# YAML Record Review: Wolbachia endosymbiont of Adetomyrma sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_adetomyrma_sp.yaml`
- Started UTC: 2026-10-07T12:15:48Z
- Finished UTC: 2026-10-07T12:19:53Z
- Verdict: pass

## Target

Complete generated `TaxonRecord` for `NCBITaxon:1035891`,
Wolbachia endosymbiont of Adetomyrma sp., rank SPECIES, domain BACTERIA.
The entire YAML was read. It carries eleven lineage entries, exact
grounding, seeded status, genetic code 11, strain count zero, one NCBI
name attestation and one inline seed event. It contains no strain
deposits, genome links, synonyms, nomenclature, alternate mappings,
literature assertions, phenotypes or causal graph.

This record denotes the bacterial taxonomy node, not its named host.
Generated fields are owned by the source inventories and
`src/taxonmech/seed.py`; scope is maintained in `curation/seed_scope.tsv`.
No generated YAML edit is authorized by this review.

## Validation

- `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_adetomyrma_sp.yaml`:
  passed with no LinkML issues.
- `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_adetomyrma_sp.yaml --out /private/tmp/wol-adetomyrma-strict.tsv`:
  passed; one file, zero errors. Inspected the header-only output TSV.
- Complete target/backbone, lineage, source-inventory, path-index,
  scope and inline-history comparisons passed.
- Live NCBI Taxonomy EFetch and Datasets checks passed for the target;
  a similarly named node was independently checked for disambiguation.
- `just validate-products`: not applicable; no curator-added graph nodes.
- Separate history validation: not applicable; bounded ignored-inclusive
  history content and filename searches found no matching standalone record.
  The inline seed event was checked without adding a review event.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`,
  `just validate-all`, `just provenance-check`, `just render-check`,
  `just docs-check` and `just vendored-check`. These focused checks
  do not certify the entire corpus or generated site.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222191` and
native scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31684` support the identifier,
label, species rank, parent and genetic code. Synonym columns and the
retired-into field are empty.

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035891&retmode=xml)
confirms the active node, name, species rank, parent
`NCBITaxon:2640676` (unclassified Wolbachia), bacterial division and
genetic code 11.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035891)
agrees on the full ancestor identifier chain, including root.
Every ancestor label and rank agrees with the local backbone and live
lineage, including Wolbachieae at TRIBE rank.

No local child, merged-ID, dropped-record or type-material rows were found
for this identifier. The species-ranked NCBI node satisfies repository
scope; it does not imply a formally named species or deposited type strain.
The host-bearing name is retained verbatim without inferring a host-species
identity, infection prevalence, transmission mode or reproductive effect.

A separate node, `NCBITaxon:1094250`, is named
Wolbachia endosymbiont of Adetomyrma MG01. Its full backbone, name and
scope rows and
[live NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1094250&retmode=xml)
were inspected. Both nodes currently exist under the same parent; no
synonym or merger evidence was found. Their distinct database identifiers
must not be collapsed solely because their host names overlap. This does
not assert that they are proven distinct biological species.

## Evidence

The sole NCBI attestation correctly identifies the target and counts
one NAME from the 2026-09-13 snapshot. Full exact-target checks of the
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories
found no target rows. With no BacDive record in the target subtree,
`strain_count: 0` is faithful to the source inventory, not a biological
assertion that no isolate or infection exists.

Path-index row 14690 and scope row 322451 agree with the slug, identifier
and scope reason. The inline event wording matches that reason and the
NCBITAXON source. Its 2026-09-13T17:54:04Z timestamp is the latest of
the raw, ATB and StrainInfo manifest extraction timestamps, consistent
with the seeder's timestamp rule.

Exact `txid1035891[Organism:noexp]` queries returned zero NCBI Assembly
and Nuccore records. Both responses also reported the organism phrase as
not found. This is a bounded index result, not proof that no relevant
sequence exists under another classification.

A broader `Adetomyrma[All Fields] AND Wolbachia[Organism]` query
returned one candidate, UID 334191886.
[Its complete GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=334191886)
identify JF902252.1, a 655-base partial COI coding sequence assigned
explicitly to taxon 1094250, the MG01 node. It carries host Adetomyrma sp.,
voucher `BIOUG<CAN>:ASAMI187-07.w`, BOLD identifier
`ASEND053-09.COI-5P` and protein AEG67010.1. All metadata, features and
references were read, excluding the nucleotide and translation payloads.

That accession is not assigned to the reviewed taxon. The voucher is not
an eligible microbial culture-deposit identifier; the marker is not a genome.
Neither its Madagascar collection metadata nor its host association can
be transferred to taxon 1035891 without an explicit authoritative identity
link. No such link was established. The YAML makes none of those assertions,
so this rejected candidate is not a defect in the record.

No literature or functional claim is asserted in the target YAML.
Search results were used only as leads, not as taxon-level evidence.
The excluded candidate's publication context and BOLD record were not
independently reviewed as evidence for this target. iModulonDB is not
applicable to this bare taxonomic identity record.

## Completeness

Complete enough for the current minimal source-seeded representation.
Optional synonyms, nomenclature, mappings, strain deposits, genomes,
phenotypes and causal edges should not be filled from the near-name match.

Ignored and hidden files, including compressed text, were included through
`rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`.
Queries covered the bounded numeric ID, scientific name, slug and
similarly named Wolbachia/Adetomyrma entries, then taxon 1094250,
JF902252, AEG67010, ASAMI187-07 and ASEND053-09. All seven matching
source rows were read in full. Five native `SOURCE.json` files were
parsed separately; history filenames were also checked independently.

The six relevant rows describe the two distinct NCBI nodes. The seventh
hit, `data/catalog/gtdb_genomes-0016.jsonl.gz:23463`, is an unrelated
Pyxidicoccus xibeiensis record: its contig N50 is 1094250, while its
NCBI taxon is 2906759. It supplies no Wolbachia evidence.

No additional target or marker/voucher evidence was found in those searched
roots and metadata files. This statement does not cover every external
database, unpublished source or arbitrary binary snapshot.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Current taxonomy and pinned source rows support every
material assertion. The unresolved relationship to the MG01 candidate
limits future enrichment, not the faithful present record.

## Recommended Edits

None required. Do not hand-edit the generated YAML or promote SEEDED status.

Any future merge, synonym or sequence attachment requires an explicit
authoritative identity decision. A taxonomy correction belongs upstream
at NCBI, followed by the maintained extraction/seeding workflow.
Sequence enrichment must retain its own identifier type, exact taxon,
source ownership and culture-deposit evidence where required.

## Follow-up Checks

Before future enrichment, recheck both NCBI nodes and the candidate
accession's current organism assignment. Do not use shared host wording,
voucher similarity or a partial marker as a strain-genome join key.

After any authorized maintained-input change, use the documented seed
dry-run and canary workflow, both focused validators, relevant tests and
full `just verify-corpus`/QC gates. No regeneration was performed here.

## Additional Notes

Reviewed on `codex/record-review-extensimonas-20261003` at
`b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target YAML is unchanged.
Only this new report was written. Source inventories, scope, pages,
statuses, history, existing worktrees and GitHub were not modified.

