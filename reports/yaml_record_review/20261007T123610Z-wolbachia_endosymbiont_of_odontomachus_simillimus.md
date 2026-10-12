# YAML Record Review: Wolbachia endosymbiont of Odontomachus simillimus

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_odontomachus_simillimus.yaml`
- Started UTC: 2026-10-07T12:33:08Z
- Finished UTC: 2026-10-07T12:36:10Z
- Verdict: pass

## Target

Complete generated `TaxonRecord` for `NCBITaxon:1035895`,
Wolbachia endosymbiont of Odontomachus simillimus.
The entire YAML was read. It has SPECIES rank, BACTERIA domain, eleven
lineage entries, EXACT grounding, SEEDED status, genetic code 11,
strain count zero, one NCBI NAME attestation and one inline seed event.
It asserts no synonyms, nomenclature, alternative mappings, strain deposits,
genomes, literature claims, phenotypes or causal graph.

This is a bacterial taxonomy node, not the named insect host.
The generated fields are owned by source inventories and
`src/taxonmech/seed.py`; `curation/seed_scope.tsv` owns inclusion scope.
No generated YAML edit is authorized by this review.

## Validation

- `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_odontomachus_simillimus.yaml`:
  passed with no LinkML issues.
- `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_odontomachus_simillimus.yaml --out /private/tmp/wol-simillimus-strict.tsv`:
  passed; one file, zero errors. The full TSV output is header-only.
- Complete target/backbone, ancestor, source-inventory, path-index,
  scope and inline-history comparisons passed.
- Live NCBI EFetch and Datasets taxonomy agreed with the record.
- `just validate-products`: not applicable; no curator-added graph nodes.
- Standalone history validation: not applicable; bounded ignored-inclusive
  history content and filename checks found no matching separate record.
  The inline seed event was inspected without adding a review event.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`,
  `just validate-all`, `just provenance-check`, `just render-check`,
  `just docs-check` and `just vendored-check`.
  The focused checks do not certify corpus reproduction or generated pages.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222194`
and native scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31689` support the identifier,
label, species rank, parent and genetic code. All synonym columns and
the retired-into field are empty.

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035895&retmode=xml)
confirms the active identifier, name, species rank, bacterial division,
parent `NCBITaxon:2640676` (unclassified Wolbachia) and genetic code 11.
It supplies no other names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035895)
agrees on all eleven ancestor identifiers, including root.
Every ancestor label and rank agrees with the pinned backbone and live
lineage, including Wolbachieae at TRIBE rank.

No child, merged-ID, dropped-record or type-material rows were found for
this taxon in the checked inventories. NCBI's species rank makes the node
eligible under repository scope; it does not establish a formally named
bacterial species or culture-deposited type strain.
Host wording remains part of the source name without asserting a
host-taxonomy identifier, host range, prevalence or reproductive effect.

## Evidence

The sole NCBI attestation correctly counts one NAME for the exact target
from the 2026-09-13 snapshot. Full exact-target checks of BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found no target
rows. With no BacDive record in the target subtree, `strain_count: 0`
is the correct source-record count, not a claim that no infected specimen
or bacterial lineage exists.

Path-index row 14693 and scope row 322454 agree with the identifier,
slug and inclusion reason. The inline event correctly names NCBITAXON
and the scope reason. Its 2026-09-13T17:54:04Z timestamp is the latest
of the raw, ATB and StrainInfo extraction timestamps, consistent with
the inspected `_seed_timestamp()` implementation.

Exact `txid1035895[Organism:noexp]` searches returned zero Assembly
records and 21 Nuccore records, with all 21 UIDs retrieved. Assembly also
reported the organism phrase as not found. This is a bounded index result,
not evidence of worldwide genome absence.

All 21 GenBank records were read in full metadata form, including features
and references but excluding nucleotide and translation payloads.
All explicitly assign the sequence to taxon 1035895 and name host
Odontomachus simillimus. They are partial gene sequences, not assemblies:

- [KF606301.1 through KF606310.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=557639134,557639132,557639130,557639128,557639126,557639124,557639122,557639120,557639118,557639116):
  ten hcpA partial coding sequences annotated as DUF28 protein, nine
  444 bases and one 402 bases, with proteins AHA14034.1 through AHA14043.1.
- [KF490656.1 through KF490665.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=564284186,564284184,564284182,564284180,564284178,564284176,564284174,564284172,564284170,564284168):
  ten COI partial coding sequences, seven 402 bases and one each of
  384, 393 and 396 bases, with proteins AHB83017.1 through AHB83026.1.
- [JF902268.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=334191918):
  a 201-base partial COI coding sequence, protein AEG67026.1, voucher
  `BIOUG<CAN>:ASAMI168-07.w` and BOLD ASEND055-09.COI-5P.
  Its source reports a Malaysian host specimen near Kuala Lumpur collected
  08-Jun-1962, not a recent culture isolation.

The two ten-record groups share voucher bases ASAND268-10, ASAND300-10,
ASAND327-10, ASAND347-10, ASAND362-10, ASAND363-10, ASAND367-10,
ASAND535-10, ASAND564-10 and ASAND602-10, all with ".w" suffixes.
Their BOLD process identifiers are ASFTA780-12, ASFTA781-12, ASFTA785-12,
ASFTA787-12, ASFTA789-12, ASFTA790-12, ASFTA791-12, ASFTA807-12,
ASFTA808-12 and ASFTA810-12, with locus-specific suffixes.
Source collection locations are in the Seychelles in 2009 or 2010.
These are specimen/sequence annotations, not culture-collection deposits.
Shared vouchers do not prove clonal bacterial identity, and twenty marker
accessions do not establish twenty strains or genomes.

The two newer groups retain Tsoi/Smith/Fisher manuscript references as
Unpublished; their publication status was not independently established.
JF902268.1 cites Smith's barcoding work as Unpublished.
The inspected methods of
[Smith et al., Wolbachia and DNA Barcoding Insects: Patterns, Potential, and Problems](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514)
describe bacterial COI recovery from insect extracts and the ".w"
identifier convention. This informs identifier-type interpretation only.
The exact target accession-to-paper link in Table S2 was not independently
verified; its XLS was not parsed. BOLD records were not independently
checked. No target-specific functional conclusion was inferred from
the general paper or source product annotations.

There are no literature or transcriptomic claims in the YAML.
iModulonDB is not applicable to this bare taxonomy record; optional
marker leads do not create a gene-function assertion to validate.

## Completeness

Complete enough for its current minimal seeded representation.
Optional strain, genome, synonym, nomenclature, mapping, phenotype and
causal-graph fields should not be invented from the marker sequences.

Ignored and hidden files, including compressed text, were searched with
`rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`.
The searches covered the bounded numeric ID, scientific name, slug and
similarly named entries, then every inspected accession, protein identifier,
voucher base and BOLD process identifier.

All five matching source rows were read in full: the scope, backbone
and native name rows, plus two AllTheBacteria rows.
The expanded accession/voucher query returned the same addresses.
Five native `SOURCE.json` files were fully parsed separately, and history
filenames were checked independently; neither supplied additional matches.

The complete ATB rows at `data/catalog/allthebacteria.tsv.xz:82189`
and line 85948 name Staphylococcus aureus, samples SAMEA104137258
and SAMEA104152358, and analyses ERZ3063051 and ERZ3078378.
The target digits occur within their shared
`seqkit.v0.1_DLS_k0_15924b1035895cbaee6c1f951ec8df5b` checksum,
not in a taxon assignment. These rows provide no Wolbachia evidence.
No assembly equivalence or culture-deposit link is inferred from the
matching checksum or catalog co-occurrence.

No further target source evidence, culture-deposit link or matching
standalone history was found in the bounded roots and metadata files.
This is not a census of every external database or arbitrary binary artifact.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The pinned inventories and current authority support the
material assertions. Optional marker and publication leads do not make the
minimal source-seeded record incomplete.

## Recommended Edits

None required. Do not hand-edit the generated YAML, count marker sequences
as BacDive strains or promote SEEDED status.

Future taxonomy corrections belong at the authoritative upstream source,
then in the maintained extraction/seeding workflow. Optional sequence
enrichment requires an authorized maintained input and explicit preservation
of marker, specimen, taxon and culture-deposit identity. Host collection
metadata must not become unsupported bacterial phenotype assertions.

## Follow-up Checks

Before optional enrichment, verify accession assignments, exact
publication/supplement links and any independent culture-deposit evidence.
Do not use a shared taxon name, specimen label or checksum substring as
a strain-genome join key.

After authorized maintained-input changes, use the documented seed dry-run
and canary workflow, both focused validators, relevant tests and full
corpus-reproduction/QC gates. No regeneration was performed here.

## Additional Notes

Reviewed on `codex/record-review-extensimonas-20261003` at
`b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
The target YAML is byte-for-byte unchanged. Only this new report was
written for this record. Source inventories, scope, statuses, history,
generated pages, existing worktrees and GitHub were not modified.

