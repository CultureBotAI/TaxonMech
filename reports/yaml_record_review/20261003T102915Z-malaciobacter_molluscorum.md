# YAML Record Review: Malaciobacter molluscorum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/malaciobacter_molluscorum.yaml`
- Started UTC: 2026-10-03T10:25:00Z
- Finished UTC: 2026-10-03T10:29:15Z
- Verdict: pass with minor issues

## Target

One complete generated `TaxonRecord`, `NCBITaxon:1032072`, label
Malaciobacter molluscorum, rank SPECIES, domain BACTERIA. Parent is
`NCBITaxon:2321114`; nine root-first lineage entries and genetic code 11
are retained. Status is EXACT / SEEDED, not a human-reviewed promotion.
The entire YAML was read, including all nested strain assertions and the
2026-09-13T17:54:04Z seed event. Scope is recorded at
`curation/seed_scope.tsv` row 10791 and the slug in `data/taxa/PATHS.tsv`.

The record lists one BacDive strain, two culture deposits, eleven assembly
assertions, seven other genome assertions and twenty-two related-record
assertions. These are assertion counts, not forty distinct genomes.
Eukaryota and all generated records remain untouched.

## Validation

- `just validate data/taxa/bacteria/malaciobacter_molluscorum.yaml`: PASS,
  no issues.
- `just validate-strict data/taxa/bacteria/malaciobacter_molluscorum.yaml`:
  PASS, one file, zero ERROR rows. Embedded curation history passed with it.
- `just straininfo-query --strain SI-ID369523 --evidence --limit 10`: PASS,
  two matched deposit paths. Source configuration and inventory hash checks
  ran. Inspection of `src/taxonmech/straininfo_query.py` confirms
  `reproduce=False`; this is not full source re-extraction.
- Structured CSV/YAML comparisons: all ancestor labels, ranks and parent
  links agree with the complete raw taxonomy; the subtree contains this
  species and child `NCBITaxon:870501`. Exact assertion-multiset comparisons
  agree for all eleven assemblies (eight raw plus three StrainInfo), seven
  genome records and twenty-two related records (thirteen raw plus nine
  StrainInfo), including every decoded nested evidence field.
- `git diff --exit-code -- data/taxa/bacteria/malaciobacter_molluscorum.yaml`:
  PASS, no target modification.
- `just verify-corpus`: not run. The documented implementation verifies the
  entire corpus and has no single-record selector; the checks above do not
  substitute for full byte-for-byte reproduction.
- `just validate-history`: not run. An ignored-inclusive search of
  `history/` for the target ID, label, slug, child ID and BacDive ID found no
  separate target history artifact. No history record was added.
- `just validate-products`: not applicable, no curator-added causal graph.
  Full QC, rendering, full catalog provenance replay and unit tests were not
  run for this read-only review.

## Identity and Grounding

The inspected [NCBI species page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032072&lvl=0)
supports the species identity, rank, code and lineage. The separate
[LMG 25693 taxon](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=870501)
is an infraspecific child, not an alternative species identifier. Genome
metadata classified under that child are compatible with a strain listed
on this species record. BacDive itself classifies the strain directly under
the species, so an absent `classified_as` override is correct.

[LPSN 798496](https://lpsn.dsmz.de/species/malaciobacter-molluscorum)
supports the validly published combination, synonym status and type culture.
[LPSN 789233](https://lpsn.dsmz.de/species/arcobacter-molluscorum)
identifies Arcobacter molluscorum as its correct name;
[LPSN 798495](https://lpsn.dsmz.de/species/malacobacter-molluscorum)
identifies Malacobacter molluscorum as an inaccurate spelling. These are
source-scoped nomenclatural relationships, not permission to replace the
NCBI label or parent chain. Finding m1 concerns their explanation only.

The GTDB mapping is species-to-species and linked explicitly by the raw LPSN
name row. Its count of three is independently supported by the complete
native GTDB shard search. Unlike a strain-level taxon, this species can
legitimately carry the species mapping and corresponding xref. No suffix
is lost here. The live GTDB taxon page failed to load; the pinned native
classification, not an unseen current web page, supports this assessment.

## Evidence

- **NCBI baseline and names:** `data/raw/ncbitaxon_taxa.tsv` row 220795
  supplies the target; row 184427 supplies the child. Native
  `data/catalog/ncbi_names-0005.jsonl.gz` rows 30011-30017 preserve the
  scientific name, two plain synonyms, authority and three `includes`
  names. The basionym/current-name exact synonyms are supported by the
  inspected NCBI/LPSN pages. CECT 7737, F101-1 and F91 remain related names,
  not extra type deposits. Native type-material rows 1564-1570 in
  `data/raw/ncbi_type_material.tsv` support F98-3, CECT 7696 and LMG 25693.
- **Nomenclature provenance:** `data/raw/lpsn_names.tsv` rows 33604-33605
  and 26291 reproduce the three name identities and source status flags.
  Only 798496 has this NCBI mapping; 789233 and 798495 have no direct NCBI
  target in that inventory. The retained LMG type designation is supported;
  live LPSN also lists CECT 7696 and F98-3, both already represented in the
  strain entry as a deposit or designation. No type strain is missing.
- **Publications:** the inspected
  [2018 primary article](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2018.02077/full)
  explicitly proposes the combination under Malacobacter and identifies
  F98-3 = CECT 7696 = LMG 25693 in its species-description section. LPSN
  separately identifies the later validation list. DOI
  `10.1099/ijsem.0.003174` resolves to the expected publisher title on one
  fetch, but subsequent body retrieval failed. PMID 30233547 is retained
  in the native LPSN row; direct PubMed fetches returned no usable article
  text, so its live bibliographic record was not independently validated.
  No phenotype or expression claim was inferred from these citations.
- **BacDive:** `data/raw/bacdive_strains.tsv` row 88874 and the complete
  native `data/bacdive/records.jsonl.gz` row 88873 agree on BacDive 166638,
  designation F98-3, the two deposits and direct species classification.
  Native DOI is `10.13145/bacdive166638.20260601.11`; source type flag is
  yes. The inspected [BacDive page](https://bacdive.dsmz.de/strain/166638)
  also supports this identity and genome accessions, though the returned
  page represents an older source version. Native reference 66792 explicitly
  supplies unversioned GCA_002701265 and GCA_003544935, IMG 2871071908 and
  2847252029, and PATRIC 870501.3 and 870501.8. No genome equivalence was
  inferred from their co-occurrence.
- **GTDB cluster:** `data/catalog/gtdb_genomes-0000.jsonl.gz` row 4144 is
  RS_GCF_004116685.1, F91, taxon 1032072. Shard 0014 row 22341 is
  RS_GCF_002701265.1, F98-3, taxon 870501. Shard 0012 row 40848 is the
  representative RS_GCF_003544935.1, CECT 7696, taxon 870501. All three have
  the exact species classification and NCBI species ID 1032072. Only the
  CECT 7696 whole-deposit token supplies a GTDB strain link. Raw mapping
  row 1337 retains count three; this is not three distinct culture deposits.
- **Primary assemblies and BV-BRC:** `data/catalog/ncbi_genbank-0002.jsonl.gz`
  row 40030 and `data/catalog/ncbi_refseq-0002.jsonl.gz` row 2126 support
  GCA/GCF_003544935.1, complete genome, strain=CECT 7696 and BioSample
  SAMN03737954. GenBank project is PRJNA66821; RefSeq retains PRJNA224116.
  `data/bvbrc/bvbrc-0027.jsonl.gz` row 41319 independently supplies
  PATRIC 870501.8, the GCA, same sample, PRJNA66821 and CP032098. Whole
  culture evidence is preserved separately for each asserting source.
  The inspected [USDA author-institution abstract](https://www.ars.usda.gov/research/publications/publication/?seqNo115=355955)
  for DOI 10.1128/MRA.01293-18 corroborates the type-culture aliases and
  genome-study identity. PMC presented a browser challenge and ASM failed;
  an unseen full-paper accession table was not used.
- **GOLD chain:** `data/gold/organisms.jsonl.gz` row 9807 is Go0011161,
  taxon 870501, with CECT 7696 in ORGANISM STRAIN. Project row 9671 is
  Gp0011161, explicitly referring to Go0011161, SAMN03737954 and PRJNA66821.
  Analysis row 194978 is Ga0334714, explicitly referring to Gp0011161,
  IMG 2847252029 and GCA_003544935.1; its GenBank sequence is CP032098.
  The empty AP organism field does not contradict the unambiguous project
  chain. Go/Gp/Ga and the sample/project IDs correctly remain related records.
- **StrainInfo:** the entire native `data/straininfo/records.jsonl.gz` row
  286534 was read. SI-ID369523.3 has exactly two own, available,
  non-erroneous deposits: SI-DP854063 LMG 25693 and SI-DP866306 CECT 7696.
  Both explicitly own GCA_003544935; only LMG owns GCA_002701265 and
  KC108678. Only CECT owns FR675874, FR675877, FR675880 and FR675883.
  These are preserved as three unversioned assembly assertions and five
  typed nucleotide references, plus four strain/deposit references. Each
  sequence names the same SI-DP used for its culture match. Source taxon
  1032072, BacDive 166638, archive DOI, statuses and native sequence types
  are preserved; no conflicting BacDive reference or cross-deposit transfer
  was found. The DOI denotes the source strain-record version, not a paper.
- **Other counts:** GOLD one ORGANISM and Madin two TRAIT_ASSERTIONs
  agree with `data/raw/gold_organisms.tsv` row 416 and
  `data/raw/madin_taxa.tsv` row 599. The native GOLD species-level organism
  is Go0519067 F91, row 365091; the two type-strain organisms are filed under
  child 870501, not this direct-taxon count. NCBI/LPSN NAME counts and the
  BacDive STRAIN count are supported. Individual transformed Madin trait
  edges were not replayed; the count is not evidence for two specific traits.

## Completeness

The ignored-inclusive raw BacDive search over the species and its complete
two-node subtree found exactly the one listed strain. All accepted raw and
StrainInfo assertion rows for that strain occur in the YAML, without a cap.
No direct MediaDive/BactoTraits target rows or separate history entry were
found in the named inventories and history tree, including ignored files.
Optional record-level evidence, causal graphs and phenotype definitions are
not required for this seeded identity record. No mechanism was invented.

Two apparent genome gaps have defensible source boundaries:

- Native GenBank shard 0002 row 6851, RefSeq shard 0001 row 31309, GTDB
  shard 0014 row 22341 and BV-BRC shard 0027 row 41318 retain the F98-3
  GCA/GCF_002701265.1 assembly and SAMN07701800. Their match field is the
  bare designation F98-3, not a registered collection accession. GOLD
  Go0489194 -> Gp0373009 -> Ga0337145 likewise has bare F98-3.
  The repository's actual CAFI normalizer accepts CECT 7696 and LMG 25693,
  but rejects F98-3 and F91. Do not bypass that rule by matching organism
  titles or taxon IDs. BacDive/StrainInfo already preserve the explicit
  unversioned GCA and BacDive IMG/PATRIC links. An ignored-inclusive search
  of accepted raw assembly/genome/related and ATB TSVs found no additional
  accepted versioned F98-3 path; this is not a claim the native genome is absent.
- `data/atb/assemblies.tsv` row 3783 contains SAMN03737954, ERZ4158332,
  three SRA runs, native FASTA/archive metadata and a SeqKit sum, but both
  relevant filters include META_FAIL. Calling the actual
  `crosslink_exclusion_reason` returned `metadata_identity_flags:META_FAIL`,
  matching `data/atb/exclusions.tsv` row 2070. No accepted ATB strain/genome
  link exists for this strain in those ignored-inclusive TSV searches.
  Exclusion is correct even though a FASTA exists. SAMN07701800 and
  SAMN07767224 had no rows in the committed ATB overlap; the full compressed
  ATB catalog was not searched and global absence is not asserted.

## Findings

Blocker: none found. Major: none found.

1. **Minor (m1): nomenclatural note implies the wrong temporal direction and
   does not identify the preferred-name relationship explicitly.** The
   generated note calls this a synonym of a "later correct name", but the
   LPSN correct name is Arcobacter molluscorum Figueras et al. 2011, earlier
   than the 2019 combination. The YAML retains that name only as a generic
   related LPSN synonym, alongside a correct false `is_correct_name` flag
   for Malaciobacter. Identity and validity are not wrong, but the reader
   cannot recover the preferred-name relation from those fields alone.
   Owner: the LPSN projection/note logic in `src/taxonmech/seed.py`, with
   regression coverage in `tests/test_seed.py`; upstream kg-microbe LPSN
   relationship extraction consumed by `src/taxonmech/extract.py` owns any
   expanded structured relationship input. Preserve the NCBI backbone.

## Recommended Edits

1. Replace the unconditional temporal wording in `src/taxonmech/seed.py`
   with source-neutral wording. When the inventory's explicit `synonym_of`
   target resolves, identify LPSN 789233 and its source-scoped correct name
   in the generated note or a maintained relationship representation. Do
   not manufacture a direct NCBI mapping for that name or silently choose
   an LPSN lineage over NCBI. Add a regression test for this earlier-basionym
   case in `tests/test_seed.py`.
2. Retain the species GTDB mapping, complete type-strain links, deposit-specific
   StrainInfo evidence and META_FAIL exclusion. No record hand-edit, identity
   merge, imported phenotype or forced assembly-version completion is justified.

## Follow-up Checks

After an authorized seeder change, run `just test tests/test_seed.py`, then
`just seed` and `just seed-canary NCBITaxon:1032072`; inspect the actual
canary YAML before any wider write. Re-run both single-record validators,
the exact inventory assertion comparisons and the StrainInfo query. Confirm
the note no longer implies chronological priority while the NCBI label,
GTDB count three, one strain, all deposit-specific links and ATB exclusion
remain unchanged. Run `just verify-corpus` after the approved full regeneration.

Revisit the publisher validation-list text and PubMed record when accessible.
Live NCBI nucleotide attempts for FR675874, FR675877, FR675880, FR675883 and
KC108678 failed, as did the attempted ENA FR675874 page. Those identifiers
and their deposit scopes were verified against native StrainInfo, with
FR675874 independently corroborated by LPSN/BacDive, not against newly
fetched sequence records. Live SI and GTDB pages were unavailable. These
are disclosed verification limits, not evidence of invalid accessions.

## Additional Notes

The record names marker genes only inside source sequence descriptions.
`command -v kg-microbe-sources` found no installed runner. An ignored-inclusive
sibling-tree pyproject inventory, excluding Git internals, virtual environments
and node_modules, and inspection of the repository project names found no
culturebotai-claw runner there. This is a bounded search, not a machine-wide
absence claim. The inspected iModulonDB homepage returned no usable text;
no covered organism/dataset/component was established. No expression or
phenotype inference depends on iModulonDB or on the marker-gene titles.

Native catalogs are projections of source metadata, not fresh authority
responses for every accession. Direct links were checked field by field;
no complete external database census or sequence-content equivalence was
claimed. Broad exploratory text matches from unrelated molluscorum species
were rejected by the exact taxon, species and culture identities.

Two exploratory CSV checks initially used wrong column names. The taxonomy
parent check was corrected to `parent_id` and passed; the BacDive membership
check was replaced by an ignored-inclusive exact subtree-ID search using
the inspected `taxon_ids` inventory header. Failed exploratory commands
were not treated as successful completeness checks.

No generated YAML, source inventory, curation status, standalone history,
site output, Eukaryota record or GitHub object was changed by this review.
