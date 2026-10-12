# YAML Record Review: Paenibacillus marinisediminis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_marinisediminis.yaml`
- Started UTC: 2026-10-03T20:36:54Z
- Finished UTC: 2026-10-03T20:39:04Z
- Verdict: pass with minor issues

## Target

Reviewed all 103 lines of this generated `TaxonRecord`: `NCBITaxon:1031539`,
Paenibacillus marinisediminis, rank `SPECIES`, domain `BACTERIA`, grounding
`EXACT`, mapping status `SEEDED`. It has one BacDive strain and no assembly,
genome-record or related-record assertions. Empty genome links do not imply
that the species lacks a sequenced genome; the native candidate and its
join boundary were checked explicitly below.

Future corrections belong in maintained source inputs and extraction/seeding
transforms. The generated YAML remains read-only. This review creates only
its individual report and the standard validator diagnostic.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/paenibacillus_marinisediminis.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/paenibacillus_marinisediminis.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured source comparisons | Exact backbone, nine-entry lineage, related names, attestations and seed reason verified. Complete target-strain scans confirm zero assembly, genome-record and related-record rows in raw/StrainInfo inventories, matching the YAML. |
| Culture identifiers | JCM 17886 and KACC 16317 normalize under the pinned authority/template policy. Bare LHW35 does not. |
| Embedded history | Strict validation passed; seed event agrees with source inventories and scope reason. |
| Standalone history | Not applicable: identifier, label and slug searches including ignored/hidden files found no target history under `history/`. |
| Causal graph and ontology-product gates | Not applicable: the complete YAML contains no causal graph. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports and FASTA replay. Focused
checks do not replace those gates. No generator, history writer or status
promotion was run.

## Identity and Grounding

The identifier, label, species rank, parent `NCBITaxon:44249`, genetic code
11 and complete root-first lineage match
`data/raw/ncbitaxon_taxa.tsv:220744`. Live taxonomy EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1031539)
confirm them. The complete local backbone scan finds no child taxa.
`data/taxa/PATHS.tsv:13070` and `curation/seed_scope.tsv:30315` agree with
the target's identity and slug. Native name rows 29909-29912 in
`data/catalog/ncbi_names-0005.jsonl.gz` support the scientific name and
three related names; none is incorrectly promoted to an exact synonym.

The inspected [LPSN page](https://lpsn.dsmz.de/species/paenibacillus-marinisediminis)
supports identifier 791932, the 2014 authority, valid publication, current
name status, cited publications and JF748731. The effective description
appeared in 2013 and validation list 158 in 2014, so preserving both
historical NCBI authority strings does not create a date conflict. The
source's medical-name recommendation is a nomenclatural status, not a
therapeutic recommendation or a species-level pathogenicity assertion.

The generated nomenclature matches `data/raw/lpsn_names.tsv:28720`, but
that inventory omits the registered KACC type deposit documented by LPSN;
see N1. No GTDB taxonomy mapping is asserted. Complete direct mapping scans
and the ignored-inclusive native searches found no target GTDB entry in
the available snapshots, so no plausible neighboring cluster was substituted.

## Evidence

- **BacDive strain:** `data/raw/bacdive_strains.tsv:84366`, native
  `data/bacdive/records.jsonl.gz:84365` and the inspected
  [BacDive page](https://bacdive.dsmz.de/strain/162130) support the two
  registered deposits, species identity and type-strain status. The native
  strain-designation field is absent, matching its omission in the YAML;
  the historical LHW35 name is separately supported by NCBI and the paper.
  The raw one-medium count is strain-scoped, not a direct MediaDive
  species attestation. Native BacDive supplies a marker, not a genome link.
- **Culture and type inventories:** Culture rows 103377 and 113354 map
  JCM 17886 and KACC 16317 to this taxon. NCBI type-material rows 1529-1534
  explicitly support both registered deposits and LHW35. These sources
  corroborate identity; bare aliases are not promoted to culture CURIEs.
- **Original description:** The full abstract of
  [PubMed 23812811](https://pubmed.ncbi.nlm.nih.gov/23812811/) and
  [Crossref metadata](https://api.crossref.org/works/10.1007/s12275-013-3198-2)
  verify the original description, DOI, 2013 publication, volume 51 and
  pages 312-317. The abstract explicitly identifies LHW35 = KACC 16317 =
  JCM 17886. No other species' physiology or molecular comparison is
  transferred into the record.
- **Validation list:** [Crossref metadata](https://api.crossref.org/works/10.1099/ijs.0.066910-0)
  verify the second DOI, Oren and Garrity, publication in July 2014,
  volume 64 and pages 2184-2187. LPSN identifies it as validation list
  158, consistent with the nomenclatural authority. Full articles were
  not read; bibliographic metadata are not treated as experimental evidence.
- **Marker accession:** Inspected
  [JF748731.1](https://www.ncbi.nlm.nih.gov/nuccore/JF748731.1) source
  features confirm a 1,482-base partial 16S sequence, strain LHW35,
  taxon 1031539 and explicit type material. The marker is correctly kept
  under nomenclature, not counted as a genome. The source-unversioned
  accession remains unversioned; no sequence alignment was performed.
- **Genome candidate, not a joined assertion:** Native
  `data/catalog/ncbi_genbank-0050.jsonl.gz:11319` and
  `ncbi_refseq-0008.jsonl.gz:14023` identify the GCA/GCF_054343325.1 pair,
  type strain LHW35, contig assembly ASM5434332v1 and SAMN53099241.
  The GenBank project is PRJNA1358048; the pinned RefSeq row carries
  PRJNA224116. Live [NCBI genome reports](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1031539/dataset_report)
  confirm the pair, 2026-01-04 release, type material and explicit strain
  LHW35. Neither native assembly strain fields nor the inspected live
  BioSample supply a JCM/KACC culture-deposit field. This is a real genome
  with insufficient evidence for the repository's guarded deposit join.
- **Attestations:** Complete inventory scans corroborate NCBI NAME 1,
  LPSN NAME 1 and BacDive STRAIN 1. Direct scans found no target GTDB,
  GOLD, MediaDive, MADIN or BactoTraits rows in those inventories. The
  source counts and seed reason therefore agree without adding phenotype
  or genome assertions from taxonomy alone.
- **iModulonDB:** The resolved `culturebotai-claw/.venv/bin/kg-microbe-sources
  imodulondb datasets` adapter returned 28 keys, none covering
  Paenibacillus. No organism-matched query applies. Bacillus datasets are
  not substituted, and absence from iModulonDB is not negative evidence.

## Completeness

The BacDive listing is complete for the local species subtree, not capped.
Ignored-inclusive compressed searches covered native catalog, BacDive,
BV-BRC, GOLD, SeqCode and StrainInfo data using the species and historical
names, typed taxon identifier and whole culture-deposit tokens. Complete
structured scans additionally covered raw target inventories, merged IDs
and dropped rows. The NCBI pair described above was found and inspected;
no eligible own-deposit assembly/genome assertion was identified within
those source boundaries.

The current whole-culture contract deliberately excludes bare LHW35.
Knowing from literature that LHW35 is the species type does not authorize
silently joining its assembly to every type-strain deposit across sources.
The native BacDive record also lacks a direct genome assertion. Therefore
empty genome/related-record slots are consistent with the maintained
matching policy, not a demonstrated extraction loss. Future deposit-specific
evidence can be ingested through an explicitly maintained source path.

BacDive links to SI-ID 132502, but the public StrainInfo API returns HTTP
404. Ignored-inclusive searches over native and overlay StrainInfo files
using exact SI-ID, both culture identifiers, species name, slug and LHW35
found no target evidence. That cross-reference alone cannot establish
eligible deposits, DOI versions or same-deposit sequence links.

Ignored-inclusive searches over `data/atb/` and the complete compressed
`data/catalog/allthebacteria.tsv.xz` included the species, slug, LHW35,
both deposits, typed identifiers and candidate BioSample SAMN53099241.
No target ATB match was found within those sources. SeqCode's name entry
14907 corroborates the species name, not another strain or genome link.
No claim of global genome absence is made. Optional biological mechanisms
and causal graphs need not be invented for this identity record.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**N1 - Minor: the nomenclature type-deposit list omits KACC 16317.** YAML
line 48 lists only JCM 17886. The inspected LPSN text, original-description
abstract and NCBI type-material rows 1531-1532 all identify KACC 16317 as
another registered deposit of LHW35. It is already correctly listed under
the BacDive strain at YAML line 76. The omission is thus a nonblocking
nomenclatural completeness gap, not wrong species identity or type status.

Maintained owner: the LPSN source transform feeding
`data/raw/lpsn_names.tsv:28720`, which already lacks KACC.
`src/taxonmech/extract.py:420` collects transformed type-deposit edges,
and `src/taxonmech/seed.py:405` faithfully copies the inventory. Trace
the maintained upstream edge set before choosing the exact correction
site; upstream KGX edge contents were not inspected here. Do not patch
the generated YAML or mint a culture-collection identifier for bare LHW35.

## Recommended Edits

1. In a later curation change, repair the maintained LPSN evidence/transform
   so the source inventory retains KACC 16317 alongside JCM 17886.
   Inspect upstream type-deposit edges to determine whether the change
   belongs in kg-microbe or TaxonMech extraction.
2. Add focused extraction/seeding coverage for multiple registered type
   deposits. Keep the empty genome slots until an eligible direct or
   own-deposit source assertion is available; do not weaken the culture
   matching rule to make this individual record look more complete.
3. Re-extract and regenerate through the documented workflow only after an
   authorized implementation and tests. No such edits occurred here.

## Follow-up Checks

- Run the focused extraction/seeding tests and inspect
  `just seed --only NCBITaxon:1031539` before an authorized
  `just seed-canary NCBITaxon:1031539`.
- Rerun both target validators and exact source comparisons. Confirm the
  two registered type deposits appear in nomenclature while the source
  names, 2014 authority, marker accession and strain identity remain stable.
- Any new genome association needs its own inspected deposit/source chain;
  species taxonomy, the laboratory alias and type-material status alone
  do not satisfy the current join contract.
- Shared transform changes need full tests, corpus reproduction, provenance
  and generated-product checks in a separate curation workflow. Retry
  SI-ID 132502 only if later source state supplies an actual eligible record.

## Additional Notes

Live NCBI metadata report the biological assembly with both database
accessions, while the taxonomy endpoint counts one assembly. This does
not imply two independent sequencing efforts. The live RefSeq report
uses the specific sequencing project rather than the pinned RefSeq
umbrella project; neither is a YAML claim here, and no pinned source row
was rewritten to match a later API representation.

The candidate BioSample records host/context fields that differ from the
marine-sediment description in the original paper and marker record.
Those source-specific details are not in the reviewed YAML and are not
used to force a deposit match or to invent an isolation assertion.

All absence statements are bounded to named complete structured reads or
ignored-inclusive searches. One new report was created; the record,
source code, prior reports, curation status and history were not edited.
Eukaryota was left untouched.
