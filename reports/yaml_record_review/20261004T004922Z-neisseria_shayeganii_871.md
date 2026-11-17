# YAML Record Review: Neisseria shayeganii 871

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/neisseria_shayeganii_871.yaml`
- Started UTC: 2026-10-04T00:45:57Z
- Finished UTC: 2026-10-04T00:49:22Z
- Verdict: needs curation

## Target

Read all 87 lines of generated `TaxonRecord` NCBITaxon:1032488,
Neisseria shayeganii 871. It is a `STRAIN` under species
NCBITaxon:607712, with `BACTERIA`, `EXACT`, `SEEDED`, genetic code11,
one GTDB mapping, four synonyms, three attestations and `strain_count: 0`.
No strain listing, genome assertion, nomenclature, general evidence,
phenotype assertion or causal graph is carried. No YAML, source, history
or status was edited.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/neisseria_shayeganii_871.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/neisseria_shayeganii_871.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, full lineage, NCBI names, path, scope and seed event agree. GTDB/Madin fields reproduce their inventories; the GTDB semantic scope finding remains. |
| History | Embedded event matches the maintained scope; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, pages, exports, sequence alignment, complete ATB FASTA eligibility
or a complete review of the parent species. Focused comparisons do not
prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220863`, live
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032488&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032488)
agree on identity, strain rank, parent607712 and code11. The full ten
root-first ancestors agree through Pseudomonadati, Pseudomonadota,
Betaproteobacteria, Neisseriales, Neisseriaceae, Neisseria and
N. shayeganii. Complete backbone scans found no children.

Native names0005:30149-30152 support the scientific label and all three
NCBI synonyms, retaining 871 or WC 08-871. `data/taxa/PATHS.tsv:13235`,
`curation/seed_scope.tsv:36141` and legacy page row774 agree. The
September13 seed event reproduces the September12 scope reason.

GTDB instead uses Eikenella, Gammaproteobacteria and Burkholderiales for
this species cluster. That source-classification disagreement is distinct
from the species-to-strain synonym inflation below. Preserve the NCBI
backbone and GTDB provenance; do not rewrite the lineage to force agreement.

## Evidence

- NCBI contributes one NAME, GTDB two GENOMEs and Madin five
  TRAIT_ASSERTIONs (`data/raw/madin_taxa.tsv:609`). These are separate
  source units, not additive counts or five asserted phenotype values.
- `data/raw/gtdb_mappings.tsv:1347` maps GTDB species
  `s__Eikenella_shayeganii` to strain1032488 with `closeMatch` and count2.
  Row299643 maps the same species to parent607712;
  `gtdb_species.tsv:57679` confirms the species-wide count. A complete
  native GTDB species search found exactly these members:

  | Genome | NCBI taxon | Source strain and sample |
  | --- | --- | --- |
  | RS_GCF_000226875.1 | 1032488 | 871; SAMN02299457; representative |
  | RS_GCF_014054965.1 | 607712 | DSM 22244; SAMN15603183; nonrepresentative |

  Native positions are GTDB0001:32977 and GTDB0010:49899. DSM22244
  is not DSM22246, the type deposit associated with871. Two genomes
  in this species cluster are not two assemblies of871. Native structured
  metadata supplied the usable GTDB evidence; the public genome page
  attempt did not supply usable text.
- [LPSN788999](https://lpsn.dsmz.de/species/neisseria-shayeganii)
  treats Neisseria shayeganii as the validly published species and links
  its type to871, WC08-871, CIP109933 and DSM22246. This concerns the
  parent species and does not make every species member identical to871.
- [BacDive10496](https://bacdive.dsmz.de/strain/10496), native row10356,
  identifies871/WC08-871, collections CCUG59856, DSM22246 and CIP109933,
  and type status. Its classification taxon is parent607712, while its
  genome and partial16S sequence entries identify child1032488.
  FJ654664 is a1463bp partial16S sequence, not a genome.
- Native NCBI GenBank0000:3993 and RefSeq0000:3430 explicitly pair
  GCA_000226875.1 with GCF_000226875.1 as identical assemblies of871,
  taxon1032488, species607712, sample SAMN02299457. The scaffold
  assembly has111contigs,26scaffolds and2,354,550bp. GenBank project
  PRJNA66915 and RefSeq project PRJNA224116 are retained as their
  own source metadata. BV-BRC0000:3168 identifies1032488.3 and
  GCA_000226875.1 with the same sample. Bare871 is not a CAFI
  collection identifier and does not independently authorize a deposit join.
- GOLD Go0005917 explicitly identifies DSM22246; Gp0005917 identifies
  that organism, PRJNA66915 and SAMN02299457; Ga0009624 points to
  that project, GCA_000226875.1 and IMG2513237270. Native positions
  are organism5263, project5271 and analysis4404. The analysis has
  no direct organism field; the inspected project supplies that connection.
  Go0611213 instead uses bareWC08-871 at parent607712 without a
  collection identifier and is not a new deposit join.
- These BacDive10496 and GOLD genome assertions are already carried
  in `data/taxa/bacteria/neisseria_shayeganii.yaml`. The parent preserves
  BacDive's unversioned GCA_000226875 and distinct IMG/BV-BRC IDs,
  plus the independently versioned GOLD assembly chain. Go/Gp/Ga stay
  related records rather than genome identifiers. This contextual read
  is not a full review of the parent or its other strains.
- Native StrainInfo row286885 describes SI-ID371496, DOI
  `10.60712/SI-ID371496.3`, and three own deposits: CIP109933/DP857636,
  DSM22246/DP857637 and CCUG59856/DP918326. All use parent607712;
  no sequences are listed on these deposits. The parent record carries
  their exact-deposit relationships. Group identity or bare871 cannot
  supply new sequence ownership for the child.
- Exact target raw scans found no BacDive, LPSN, GOLD aggregate,
  MediaDive or BactoTraits row at1032488. Native GOLD and BacDive
  genome evidence is nevertheless present. An absent aggregate
  attestation is not whole-database absence. No gene, regulator, pathway
  or transcriptomic claim is carried; iModulonDB was not applicable.

## Completeness

The material issue is unsupported synonym scope, not proven missing
genome evidence. `strain_count: 0` reflects source-classified listings on
this child; it is not a claim that the named isolate or its genome is absent.
Parent-owned BacDive and StrainInfo relationships must not be duplicated
onto this child merely because they denote the same named type isolate.
No additional ATB or culture-deposit link was inferred from taxon identity.

Ignored-inclusive searches covered identifier, label and slug across raw
tables, native catalog shards, BacDive, BV-BRC, GOLD, SeqCode, StrainInfo,
curation and history. Additional searches included WC08-871/WC 08-871
in StrainInfo, ATB inventories and curation/history. SOURCE.json files
were completely JSON-traversed for these identifiers and aliases without
a match. Structured scans found no own type-material, merged-ID or
dropped row. The WC08-871 type-material row241467 belongs to607712.
These bounded misses are not a global source absence claim or a complete
ATB sample/FASTA audit. Optional nomenclature, definition, general
evidence and graph slots need not be invented for this seeded strain.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a whole GTDB species is promoted to an exact synonym of
   strain871.** YAML lines46-49 assert `Eikenella shayeganii` as an
   `EXACT_SYNONYM` of NCBITaxon:1032488. The source is a species
   cluster containing871 and distinct DSM22244; its `closeMatch` and
   count2 do not establish whole-species/strain name equivalence. This
   problem remains even though GTDB and NCBI use different genera.
   The three NCBI strain synonyms are supported.

   Maintained owner: `src/taxonmech/seed.py:451` treats GTDB
   `closeMatch` as identity, and line468 emits the exact synonym without
   a rank guard. `src/taxonmech/extract.py:501` preserves the upstream
   kg-microbe mapping into `data/raw/gtdb_mappings.tsv`; the mapping
   owner must clarify predicate and count scope. The source fields
   reproduce correctly, so this is a semantic seeding issue, not schema
   failure or generated drift. No arbitrary predicate replacement follows
   from this review alone.

## Recommended Edits

1. Add a rank-aware guard in the maintained seeder so a GTDB species
   label cannot become an exact strain synonym solely from `closeMatch`.
   Preserve the mapping as qualified source context and review the xref's
   identity semantics at the same boundary. Retain the NCBI strain names.
2. Resolve the upstream GTDB mapping/count contract. Count2 currently
   denotes the species cluster, only one member of which is assigned to
   target1032488. Do not simply change it to1 or rewrite the predicate
   in generated YAML. Preserve the Neisseria/Eikenella classification
   disagreement explicitly.
3. Leave parent-owned BacDive10496 genome/StrainInfo evidence and the
   exact collection IDs intact. Do not infer missing child strain rows,
   upgrade unversioned accessions or promote `SEEDED` automatically.

## Follow-up Checks

- Extend `tests/test_seed.py` with a strain child mapped to a GTDB
  species containing another deposited strain. Assert no whole-species
  exact synonym is emitted, while NCBI strain names and supported
  species-level mapping behavior remain intact.
- Following authorized maintained changes, run extraction/seed dry
  runs and the NCBITaxon:1032488 canary; inspect the full result and
  rerun both focused validators, `just verify-corpus` and `just qc`.
- Check that presentation still exposes parent-owned BacDive10496
  genome evidence without merging DSM22244 and DSM22246, treating
  related GOLD records as genomes or asserting cross-database identity
  beyond the explicitly supported NCBI assembly pair.

## Additional Notes

The initial supplemental search used nonexistent `data/curation` and
`data/history` paths and exited2; it was rerun successfully against the
actual `curation` and `history` directories before drawing absence
conclusions. Live taxonomy evidence came from EFetch/Datasets because
the browser-page attempt did not supply usable text. No live genome
assembly re-fetch or primary-description full-text review was performed;
genome context above is bounded to the inspected pinned native records.
No phenotype values or clinical attributes were transferred from the
second GTDB strain, joint species paper or database predictions.
All checks were read-only except this new report and validator diagnostic.
Completed Eukaryota coverage was untouched.
