# YAML Record Review: Wolbachia endosymbiont of Monomorium termitobium

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_monomorium_termitobium.yaml`
- Started UTC: 2026-10-07T12:27:42Z
- Finished UTC: 2026-10-07T12:32:38Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` for `NCBITaxon:1035894`,
Wolbachia endosymbiont of Monomorium termitobium, read before judging.
It carries SPECIES rank, BACTERIA domain, eleven lineage entries,
EXACT grounding, SEEDED status, one related synonym, genetic code 11,
strain count zero, one NCBI name attestation and an inline seed event.
It contains no strain deposits, genomes, nomenclature, alternate mappings,
literature assertions, phenotypes or causal graph.

The record denotes the bacterial taxonomy node, not the named insect host.
Source inventories and `src/taxonmech/seed.py` own generated fields;
`curation/seed_scope.tsv` owns inclusion. Generated YAML is read-only.

## Validation

- `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_monomorium_termitobium.yaml`:
  passed with no LinkML issues.
- `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_monomorium_termitobium.yaml --out /private/tmp/wol-termitobium-strict.tsv`:
  passed; one file, zero errors. The complete output TSV is header-only.
- Full target/backbone, ancestor, source-inventory, path-index, scope and
  inline-history comparisons passed.
- Live NCBI EFetch and Datasets checks agreed for the target and separately
  resolved two similarly named nodes.
- `just validate-products`: not applicable; no curator-added graph nodes.
- Standalone history validation: not applicable; ignored-inclusive history
  content and filename checks found no matching separate history record.
  The inline seed event was inspected without adding a review event.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`,
  `just validate-all`, `just provenance-check`, `just render-check`,
  `just docs-check` and `just vendored-check`.
  Focused checks do not certify corpus reproduction or the generated site.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222193`
and native names at `data/catalog/ncbi_names-0005.jsonl.gz:31687`
and line 31688 support the identifier, name and related synonym.
The ASANQ205-09 name is explicitly classified as "includes", so retaining
it as RELATED_SYNONYM rather than EXACT_SYNONYM preserves source scope.

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035894&retmode=xml)
confirms the name, species rank, bacterial division, genetic code 11,
includes-name and parent `NCBITaxon:2640676`, unclassified Wolbachia.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035894)
agrees on the eleven ancestor identifiers, including root.
Every ancestor label and rank agrees with the pinned backbone and live
lineage, including Wolbachieae at TRIBE rank.

The species-ranked NCBI node satisfies repository scope without implying
a formally named bacterial species or culture-deposited type strain.
No child, merged-ID, dropped-record or type-material rows were found
for this identifier in the checked inventories.

Two local near matches have separate identities:
[NCBI 1414273, termitobium_03](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1414273&retmode=xml)
and
[NCBI 1414274, termitobium_04](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1414274&retmode=xml).
Their full native name, backbone and scope rows were read, and both live
EFetch and Datasets responses were inspected. They remain sibling nodes
under the same parent, with space-separated equivalent names for their own
underscore names. They are neither descendants nor established synonyms
of this target. Shared host wording alone does not authorize a merge.

## Evidence

The NCBI attestation correctly counts one NAME for the exact target from
the 2026-09-13 snapshot. Full exact-target checks of BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin and BactoTraits inventories found no target rows.
With no BacDive record in the target subtree, `strain_count: 0` is the
correct upstream-record count, not a claim that no infected specimen exists.

Path-index row 14692 and scope row 322453 match the identifier, slug and
inclusion reason. Inline history correctly names NCBITAXON and the scope
reason. Its 2026-09-13T17:54:04Z timestamp is the latest of the raw,
ATB and StrainInfo manifest extraction timestamps, matching
`_seed_timestamp()`. No status promotion is warranted by this read-only review.

Exact `txid1035894[Organism:noexp]` queries returned zero NCBI Assembly
records and 42 Nuccore records; all 42 UIDs were retrieved. The Assembly
response also reported the organism phrase as not found. This is a bounded
index result, not proof of worldwide genome absence.

Full metadata, features and references were read for all 42 records,
excluding nucleotide and translation payloads. All explicitly carry
taxon 1035894. They are partial gene sequences, not assemblies:

- [KF606218.1 through KF606237.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=557638988,557638986,557638984,557638982,557638980,557638978,557638976,557638974,557638972,557638970,557638968,557638966,557638964,557638962,557638960,557638958,557638956,557638954,557638952,557638950):
  twenty hcpA partial coding sequences annotated as DUF28 protein,
  413-444 bases, with proteins AHA13951.1 through AHA13970.1.
- [KF490532.1 through KF490551.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=564283958,564283956,564283954,564283952,564283950,564283948,564283946,564283944,564283942,564283940,564283938,564283936,564283934,564283932,564283930,564283928,564283926,564283924,564283922,564283920):
  twenty COI partial coding sequences, 372-402 bases, with proteins
  AHB82893.1 through AHB82912.1.
- [JN625820.1 and JF902267.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=345645411,334191916):
  two further partial COI sequences, 624 and 657 bases, with proteins
  AEO13079.1 and AEG67025.1 respectively.

JN625820.1 explicitly records host Monomorium termitobium ASANQ205-09,
voucher ASANQ205-09.w and BOLD ASWSB030-11.COI-5P.
Its source reports a Comoros specimen from Mount Ntringui collected
24-Jan-2009. This is sequence-level support for the specimen-bearing name,
not an eligible microbial culture-deposit assertion.

JF902267.1 records voucher `BIOUG<CAN>:ASAMY628-07.w`,
BOLD ASEND058-09.COI-5P and host Monomorium termitobium, with a
Reunion collection at Les Makes on 23-May-2007.

The two twenty-record groups describe Malagasy collections in 2004,
2005 and 2009 and retain locus-specific BOLD and specimen identifiers.
Their voucher sets overlap but are not identical: JDWAM478-05.w occurs
in the inspected hcpA group, whereas JDWAM441-05.w occurs in the COI group.
Shared vouchers do not prove a clonal isolate, and 42 markers do not
establish 42 strains. No source supplies a culture-deposit join from these
markers to an assembly.

The marker references retain Tsoi/Smith/Fisher manuscript titles as
Unpublished; their publication status was not independently established
for this review. The older records cite Smith's barcoding work.
The inspected methods of
[Smith et al., Wolbachia and DNA Barcoding Insects: Patterns, Potential, and Problems](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514)
explain bacterial COI recovery from insect extracts and the ".w" label
convention. This supports identifier-type interpretation, not a
taxon-specific prevalence, host range, reproductive effect or mechanism.
The target accession-to-paper links in supplementary Table S2 were not
independently verified; its XLS was not parsed. BOLD records were not
independently checked. GenBank is the inspected authority for the
accession metadata above.

The YAML asserts no literature-based function or phenotype.
iModulonDB is not applicable to this bare taxonomic record; optional
external marker annotations do not create transcriptomic assertions.

## Completeness

Complete enough for the current minimal seeded representation.
Empty optional strain, genome, nomenclature, mapping, phenotype and graph
slots should not be populated from the marker records or shared host name.

Ignored and hidden files, including compressed text, were searched using
`rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`.
Queries included the bounded target ID, label, slug, similarly named
entries and ASANQ205-09, then every inspected accession, protein,
voucher base and BOLD process identifier.

All 13 matching source rows were read in full: three scope rows,
three backbone rows, six native name rows and one assembly-catalog row.
The expanded search returned the same addresses. Five native
`SOURCE.json` files were parsed separately and history filenames
were independently checked; neither supplied additional matches.

The assembly hit at `data/catalog/ncbi_genbank-0067.jsonl.gz:542`
is GCA_984447295.1, a Gammaproteobacteria bacterium MAG assigned to
taxon 1913989. Its genome size is 1035894. That numeric collision is
not evidence for the reviewed Wolbachia and must not supply a genome link.

No additional target source evidence, culture-deposit link or standalone
history record was found within the bounded roots and metadata files.
These results do not cover every external resource or arbitrary binary
artifact.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The source-backed identity, related-synonym scope, lineage,
attestation, inventory count and inline provenance are internally consistent.
Optional sequence and publication leads do not invalidate the minimal record.

## Recommended Edits

None required. Do not hand-edit the generated YAML, substitute sequence
counts for BacDive counts or promote SEEDED status.

Future taxonomy corrections belong at the authoritative upstream source,
followed by maintained extraction and seeding. Optional sequence enrichment
requires an authorized maintained input and explicit preservation of marker,
specimen, taxon and culture-deposit identity. Phenotype or mechanism claims
require their own narrowly scoped evidence.

## Follow-up Checks

Before optional enrichment, verify current accession assignments, exact
publication/supplement links and independent culture-deposit evidence.
Do not collapse the _03/_04 nodes based only on the shared host name.

After authorized maintained-input changes, use the documented seed dry-run
and canary workflow, both focused validators, relevant tests and full
corpus-reproduction/QC gates. No regeneration was performed here.

## Additional Notes

Reviewed on `codex/record-review-extensimonas-20261003` at
`b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
The YAML is byte-for-byte unchanged. Only this new review report was
written for this record. Source inventories, scope, statuses, history,
generated pages, existing worktrees and GitHub were not modified.

