# YAML Record Review: Cutibacterium acnes 6609

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/cutibacterium_acnes_6609.yaml`
- Started UTC: 2026-10-03T08:27:01Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:29:19Z
- Verdict: needs curation

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1031709` denotes
Cutibacterium acnes 6609, beneath species `NCBITaxon:1747`. It declares
`STRAIN`, `BACTERIA`, `EXACT` grounding and `SEEDED` mapping status. It has
ten ancestor entries, one GTDB mapping, four exact synonyms, one GTDB xref,
genetic code 11, zero attached BacDive strains, three source attestations and
one 2026-09-13 seeding event. The target is at `data/taxa/PATHS.tsv:13121`.

## Validation

- `just validate data/taxa/bacteria/cutibacterium_acnes_6609.yaml`: passed,
  no issues found.
- `just validate-strict data/taxa/bacteria/cutibacterium_acnes_6609.yaml`:
  passed, one file scanned and zero errors.
- Structured YAML/TSV comparisons confirmed identity, stored rank, parent,
  genetic code and every ancestor ID, label, rank and parent link. A complete
  taxonomy-inventory scan found zero direct children.
- A structured parse of native GTDB JSONL rows counted exactly 544 members of
  `s__Cutibacterium acnes`; only one has `ncbi_taxid=1031709`. An independent
  parse of `data/raw/gtdb_mappings.tsv` found 137 distinct NCBI targets for the
  species cluster: 134 closeMatch and three broadMatch rows. These checks
  establish a scope problem despite syntactic validation passing.
- `just verify-corpus` was not rerun: it is full-corpus-only. Focused checks
  are not a new reproduction pass. Full catalog hashes/censuses and rendered
  pages were not revalidated.
- `just validate-products` was not run: this record has no causal graph.
  `just validate-history` was not run: the ignored-file-inclusive target
  search found no separate history artifact. The embedded event was inspected
  and covered by strict validation; no history record was created.
- `git diff --exit-code -- data/taxa/bacteria/cutibacterium_acnes_6609.yaml`
  passed before writing this report. No record or source was changed.

## Identity and Grounding

The inspected [NCBI 6609 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1031709)
agrees on ID, name, code 11 and lineage. The [species tree](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1747)
places 6609 beneath Cutibacterium acnes alongside distinct infraspecific taxa.
The primary NCBI grounding and parentage are sound. The browser reports
`no rank`, while the pinned inventory says `STRAIN`; this remains unresolved.

The GTDB species concept is not identical to this one strain-level taxon.
The generated exact synonym `Cutibacterium acnes` and equivalence-style xref
therefore overstate what the source metadata establish. The 544-genome count
is the species-cluster count, not 544 genomes identified as strain 6609.

## Evidence

| Claim group | Inspected evidence and interpretation |
| --- | --- |
| NCBI identity and lineage | `data/raw/ncbitaxon_taxa.tsv:220778` agrees with the YAML's label, parent, stored rank, code and snapshot. All ten ancestor rows were separately compared. The accessible browser supports identity and placement but differs on rank. |
| NCBI synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:29959` through the following three rows retain the scientific name, the Propionibacterium acnes 6609 synonym, and the `str. 6609`/`strain 6609` equivalent names. Their exact-synonym treatment follows the documented importer rule. These are distinguishable from the unsupported species-only GTDB synonym. |
| GTDB mapping and count | `data/raw/gtdb_mappings.tsv:1314` supplies the closeMatch to 1031709 and count 544; `data/raw/gtdb_species.tsv:47767` supplies the same species total. Native `data/catalog/gtdb_genomes-*.jsonl.gz` rows confirm 544 genomes in that exact species cluster, spread over 137 NCBI taxon IDs. Thus reproduction of the mapping row is not proof of equivalence. |
| Exact 6609 GTDB member | `RS_GCF_000217615.1` has NCBI taxon 1031709, organism name Cutibacterium acnes 6609, bare strain identifier 6609, GenBank assembly GCA_000217615.1, BioSample SAMN02602996 and RefSeq project PRJNA224116. It is not the GTDB representative. |
| GTDB representative and broader membership | `RS_GCF_003030305.1` is the representative, with NCBI taxon 1747 and strain identifier ATCC 6919. There are 371 cluster genomes filed at 1747, plus genomes assigned to many other infraspecific taxa. These are not all 6609. |
| Native NCBI assemblies | Current GenBank and RefSeq catalog rows identify GCA_000217615.1 and GCF_000217615.1 with taxon 1031709, species taxon 1747, `strain=6609`, sample SAMN02602996 and latest status. Their projects are PRJNA66845 and PRJNA224116 respectively. These remain catalog evidence, not invented BacDive deposit links. |
| Native BV-BRC and GOLD | BV-BRC genome 1031709.3 reports the same strain, GenBank assembly, BioSample and PRJNA66845. GOLD Go0011108 -> Gp0011108 -> Ga0029930 supplies the matching organism/project chain, GCA_000217615.1 and IMG 651053059. The GOLD culture-collection field is empty; its strain field is the bare designation 6609. |
| Attestations and scope | The NCBI row supports one name assertion; `data/raw/madin_taxa.tsv:584` supports five trait assertions, not five newly verified phenotypes. `curation/seed_scope.tsv:36134` supplies the 2026-09-12 three-source rationale preserved by the seeding event. The GTDB attestation faithfully reports the cluster total but needs the same scope qualification as the mapping. |

The species-level LPSN inventory row (`lpsn:794765`,
`data/raw/lpsn_names.tsv:31232`) maps to parent taxon 1747, not 1031709. It does
not justify copying the species name or its type deposits onto 6609. The
record itself cites no LPSN name, DOI or PMID. The NCBI browser's linked genome
paper was a follow-up lead; PubMed did not expose usable content, so the paper
was not used to establish additional claims.

## Completeness

Identifier, current label, former Propionibacterium label and slug were
searched with `rg --no-ignore --hidden` in the raw/ATB/StrainInfo inventories,
curation tables, history and review reports. The taxonomy, GTDB mapping,
Madin, seed-scope and legacy-page rows matched; no previous target report or
separate history artifact was found. Compressed JSONL.GZ and TSV.GZ surfaces
in `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/` and
`data/straininfo/` were searched with decompression, including exact numeric
taxonomy fields and the older name variants. The native matches are described
above, not dismissed because they are absent from the attached-strain list.

A separate complete structured scan of `data/raw/bacdive_strains.tsv` for
the exact taxon and standalone designation 6609 returned no candidates.
The native BacDive projection likewise contained no strain-designation match.
These searches included ignored files and were bounded to these committed
source surfaces. They do not assert that 6609 has no genome: several native
catalogs explicitly show one.

Under the current schema, genome associations attach to supported BacDive
strain identities through direct source or registered culture-deposit evidence.
Bare 6609 is not such a deposit. Zero attached strains is consistent with
that boundary; do not mint a deposit or attach the species type strain to fill
the record. Exposing the native taxon-to-genome association more directly is
a future representation question, separate from correcting the false synonym.
The GOLD attestation is derived from the maintained KGX inventory rather than
the complete native workbook, so its omission must not be described as absence
of GOLD evidence.

## Findings

- **Blocker:** None found in the primary NCBI identity or file structure.
- **Major (1): Species-cluster membership promoted to strain equivalence.**
  `taxonomy_mappings[0]` carries a GTDB-species closeMatch, and
  `src/taxonmech/seed.py:451` treats any closeMatch as an identity mapping.
  Lines 467-469 then add an equivalence-style xref and an `EXACT_SYNONYM`.
  For this target that yields the species-only name Cutibacterium acnes as
  an exact synonym of strain 6609, although the inspected 544-member cluster
  has only one genome assigned to 1031709. This is an unsupported scope
  promotion. The upstream predicate comes from the kg-microbe GTDB transform,
  consumed by `src/taxonmech/extract.py:extract_gtdb`; the local synonym/xref
  promotion is owned by `src/taxonmech/seed.py:build_document`. Both ownership
  boundaries need attention; hand-editing the generated record would not fix it.
- **Minor (1): Unresolved NCBI rank discrepancy.** The accessible browser says
  `no rank`; the pinned inventory says `STRAIN`. The importer directly
  normalizes the source rank rather than inferring it from the name.
  The original archive pinned in `conf/ncbi_taxdump.yaml` is unavailable in
  this checkout, so source-version divergence versus import error remains
  unresolved. Parentage, identity and species-and-below scope are unaffected.

## Recommended Edits

1. In a separately authorized curation change, stop
   `src/taxonmech/seed.py:build_document` from promoting a species-cluster
   association to an exact synonym/xref for an infraspecific taxon merely
   because the imported predicate is closeMatch. Preserve source provenance
   and represent the supported association without asserting identity.
2. Review the owning kg-microbe GTDB mapping rule using the exact 6609 example.
   Reconcile the predicate's scope and direction from evidence, then
   re-extract through `src/taxonmech/extract.py:extract_gtdb`. Do not mechanically
   replace it with broadMatch or narrowMatch, or change 544 to 1 while the
   field still denotes the GTDB species-cluster total.
3. Add a regression case in `tests/test_seed.py` for a GTDB species mapping
   to a strain/unranked child of an NCBI species. Preserve the three supported
   NCBI synonyms and prevent a species-only exact synonym/equivalence xref.
   Existing species-level and pooled-mapping cases should continue to pass.
4. Resolve the rank discrepancy against the hash-verified pinned taxonomy
   source before changing the NCBI input or importer. Do not alter the generated
   YAML or silently reparent the strain to make it resemble the GTDB cluster.

## Follow-up Checks

- Run the new and existing `tests/test_seed.py` cases for a code correction.
  Confirm the regenerated target keeps ID 1031709, parent 1747 and its three
  NCBI synonyms while no longer presenting the species as an exact strain
  synonym or equivalent identifier.
- Recheck the exact-species GTDB native count of 544 and the single genome
  with taxon 1031709. Keep genome identifiers, taxon IDs and culture deposits
  distinct in any future representation.
- Recover the NCBI archive pinned by `conf/ncbi_taxdump.yaml` (SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`)
  and inspect taxon 1031709's original `nodes.dmp` rank.
- After an authorized correction and source reconciliation, use the normal
  extraction/seeding workflow, including `just seed-canary NCBITaxon:1031709`,
  both target validators and the full `just verify-corpus`.

## Additional Notes

The live GTDB tree request failed. Native RS232 catalog records, not search
snippets, supported the cluster-scope finding. The NCBI-linked GOLD query
returned a request-processing error; native organism/project/analysis rows
supported the GOLD discussion. No genome sequences or live archive payloads
were downloaded. Full source-catalog hashes were not revalidated.

The repository-wide, ignored-file-inclusive taxdump/nodes filename search
earlier in this review session found no archive or `nodes.dmp`, and the
configured snapshot directory was unavailable. No assertion is made about
copies outside this checkout. iModulonDB is not applicable: aggregate trait
counts do not assert a specific gene, regulator or expression module. No
paid research, external messages, GitHub mutation, history addition or
review-status promotion was performed.
