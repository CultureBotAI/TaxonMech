# YAML Record Review: 'Sabal palmetto' wilt phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sabal_palmetto_wilt_phytoplasma.yaml`
- Started UTC: 2026-10-07T11:39:49Z
- Finished UTC: 2026-10-07T11:46:19Z
- Verdict: pass

## Target

Reviewed the complete generated `TaxonRecord` for `NCBITaxon:1035886`,
label `'Sabal palmetto' wilt phytoplasma`, rank `SPECIES`, domain
`BACTERIA`. It is `EXACT`-grounded and `SEEDED`, with parent
`NCBITaxon:3048141`, ten ancestor entries, genetic code 11, one related
synonym, zero source-counted strains, one NCBI name attestation, and one seed
event. There are no asserted genomes, literature-backed traits, nomenclature
entries, taxonomy mappings, or causal edges to assess.

Generated YAML is not a maintained editing surface. Source corrections belong
upstream in the pinned inputs and their extraction logic; emission corrections
belong in `src/taxonmech/seed.py`; scope changes belong in
`curation/seed_scope.tsv`. This review changes none of them.

## Validation

- `just validate data/taxa/bacteria/sabal_palmetto_wilt_phytoplasma.yaml`:
  passed, no issues.
- `just validate-strict data/taxa/bacteria/sabal_palmetto_wilt_phytoplasma.yaml --out /private/tmp/sabalWilt-strict.tsv`:
  passed, one file scanned, zero error rows; the output TSV was header-only.
  Validation used the existing environment with offline uv resolution and a
  temporary uv cache.
- Structured pinned-source checks: passed for identity, all ten ancestor
  IDs/labels/ranks, synonym scope, genetic code, attestation, scope membership,
  and seed-history wording. These are bounded comparisons, not a replacement
  for corpus reproduction.
- Live NCBI Taxonomy EFetch and Datasets checks: passed for the target node,
  parent, lineage, rank, bacterial placement, and relevant name metadata.
- OAK `just validate-products`: not applicable to this bare taxonomy record;
  no curator-added graph grounding is asserted.
- `just validate-history`: not run for this target because bounded,
  ignored-inclusive history content and filename searches found no separate
  target history artifact. The inline seed event was inspected.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`,
  `just validate-all`, provenance, generated-site, documentation-statistics,
  and vendored-sync gates. This is a focused record review, not a claim that
  every repository gate passes.

## Identity and Grounding

Pinned backbone row 222186 in `data/raw/ncbitaxon_taxa.tsv` and live
[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035886&retmode=xml)
agree on the exact name, taxon ID, species rank, genetic code 11, and parent
`NCBITaxon:3048141` (16SrIV, Coconut lethal yellows group).
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035886)
also returns the same species and the root-inclusive ancestor ID chain.

All ten YAML ancestors match the pinned backbone: root, cellular organisms,
Bacteria, Bacillati, Mycoplasmatota, Mollicutes, Acholeplasmatales,
Acholeplasmataceae, Candidatus Phytoplasma, and the 16SrIV species group.
Lineage is carried from NCBI, not reconciled against disease terminology.

The NCBI native name rows in `data/catalog/ncbi_names-0005.jsonl.gz`,
lines 31676-31677, retain both the scientific name and the PD179 includes name.
The YAML correctly represents `'Sabal palmetto' wilt phytoplasma PD179` as
`RELATED_SYNONYM`, source `NCBITaxon`, not as species-wide exact equivalence.
This follows the name-class handling in `src/taxonmech/ncbi_taxdump.py`.

The record is not any of the separately indexed Sabal-associated nodes
`NCBITaxon:1004767` (lethal yellowing), `NCBITaxon:1035885` (decline),
`NCBITaxon:1035887` (lethal decline), `NCBITaxon:2051676` (phytoplasma),
or `NCBITaxon:2461345` (Sab4). Their complete matched source rows were read.
Similar host names and disease wording do not establish identity between nodes.

## Evidence

The sole attestation is supported by the backbone's NCBI source:
`NCBITAXON`, `NCBITaxon:1035886`, the exact source label, count 1,
unit `NAME`, snapshot 2026-09-13. It counts source identity support, not
isolates, experiments, or the number of alternative names.

`data/taxa/PATHS.tsv` row 14685 maps this ID to the reviewed slug.
`curation/seed_scope.tsv` row 322447 records its 2026-09-13 inclusion with
one source including NCBI. The inline seed event reproduces that scope reason.
Its timestamp, 2026-09-13T17:54:04Z, is the newest extraction timestamp among
the raw, ATB, and StrainInfo manifests, as selected by `_seed_timestamp`.
It does not represent human review or promotion to `REVIEWED`.

Exact `txid1035886[Organism:noexp]` searches returned zero Assembly entries
and two Nuccore entries. The Assembly response includes a phrase-not-found
notice; this is an exact-index search result, not proof that no relevant
assembly could exist under another taxon or metadata representation.
All feature and reference metadata for both Nuccore entries were read,
excluding nucleotide payloads and protein translations:

| Accession | Inspected metadata | Scope retained |
| --- | --- | --- |
| [MF491871.1](https://www.ncbi.nlm.nih.gov/nuccore/MF491871.1) | 1,535 nt partial 16S/spacer sequence; clone PD179; host Sabal palmetto; Orleans Parish, Louisiana; collected 17-Dec-2015; source note subgroup 16SrIV-D | An explicitly host- and location-qualified clone sequence, not a genome or culture-deposit accession |
| [HQ613885.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ613885.1) | 649 nt partial gcp CDS; isolate Awka; protein AEH05548.1; translation table 11; source taxon 1035886 | Sequence annotation and submitted isolate label, not proof that Awka is PD179 or that this sequence represents an eligible deposited strain |

Neither inspected sequence record supplies an assembly, BioSample, BioProject,
or registered culture-deposit accession. HQ613885.1 supplies no explicit host
or locality qualifier; its Florida submission address is not an isolation
locality. Its unpublished genetic-characterization reference is not direct
experimental validation of a protein function.

The [LSU author-repository abstract and citation](https://repository.lsu.edu/plantcrop_pubs/391/)
confirm a 2020 Louisiana lethal-bronzing study including Sabal palmetto and
subgroup 16SrIV-D, DOI 10.1094/PHP-06-20-0046-S. The abstract does not establish
an exact accession-to-paper link for MF491871.1. Publisher full text returned
403; search-result text was not treated as inspected primary full text.

There is a bounded unresolved provenance issue around the isolate word
Awka, not an established defect in this minimal YAML. The pinned inventory
separately represents `NCBITaxon:1775909`, Awka wilt phytoplasma, under
`NCBITaxon:1775905`. Its complete backbone, scope, and native-name rows were
read. The [Harrison et al. primary abstract](https://pubmed.ncbi.nlm.nih.gov/24585372/)
(PMID 24585372; DOI 10.1099/ijs.0.060053-0) discusses Nigerian coconut Awka
wilt in the context of palmicola and group 16SrXXII. Neither that abstract nor
the inspected target sequence metadata establishes that its Nigerian strain
is the isolate named Awka in HQ613885.1. Do not transfer that classification,
host, locality, or isolate equivalence to taxon 1035886 without an explicit
accession-level chain. The full 2014 paper was not inspected.

iModulonDB is not applicable to the record's present claims: it asserts a
taxonomic identity, not a gene, regulator, expression module, or phenotype.
Optional sequence leads do not turn the current YAML into a gene-function claim.

## Completeness

Zero strains is supported by the pinned BacDive inventory and the absence of
target descendants in the checked backbone. It is a count of source records,
not a biological claim that no isolates exist.

Exact target checks found no matching enrichment rows in the seven raw
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories.
Type-material, merged-ID, and dropped-ID tables also had no target rows.

Absence checks included ignored, hidden, and compressed files:
`rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation`, and `history`.
Queries covered the taxon number, Sabal/phytoplasma names, exact slug, PD179
variants, both nucleotide accessions, the protein accession, and Awka.
All five source-level `SOURCE.json` files were separately parsed completely;
none supplied a target match. History filenames were also checked independently
of ignore rules.

The bounded query yielded 36 candidate lines, all read in full through
structured TSV or native JSON parsing. A broader Awka substring query yielded
249 lines. Match-field and identity projections excluded 213 additional lines
whose matches were WGS accession strings or accession-derived GTDB names;
these irrelevant rows were not claimed as complete record reads.
The eight additions to the initial 28-line search comprised three rows for the
separate Awka taxon and five geographic matches for unrelated enterobacteria.
No matching local sequence-accession row was found in the searched roots.

Other excluded matches included Pseudomonas savastanoi PD179 in GOLD and
StrainInfo, Clostridium sp. COPD179, and numeric genome-length collisions with
1035886. Pseudomonas deposit identifiers belong to their own strain records;
they cannot supply deposits or genomes for this phytoplasma through PD179.
Optional fields are correctly left empty given the inspected evidence.
These negative results are bounded to the named snapshots and queries.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's current identity, lineage, synonym, source-count,
attestation, or seed-history claims. Passing this record does not certify
the biological equivalence of its two external sequence isolates.
The Awka provenance question remains unresolved for any future enrichment.

## Recommended Edits

None required for the current record.

Do not hand-edit the generated YAML, replace its NCBI label with a disease
name, merge neighboring Sabal taxa, promote PD179 to an exact species synonym,
or add genomes through a shared name or taxon ID.

If future work resolves the external Awka correspondence, preserve the
accession-level source evidence and route any upstream taxonomy correction
through NCBI and the pinned source refresh. Any newly supported enrichment
must enter through maintained source inputs and the seeder, not this report
or a direct YAML patch.

## Follow-up Checks

Before adding isolate-specific phenotype, taxonomy, or sequence links, inspect
primary accession-linked evidence distinguishing PD179, HQ613885.1 Awka,
and the independently indexed Awka wilt taxon. Retrieve the primary full
papers if paper-level attribution or experimental claims are proposed.

For an authorized maintained-input correction, inspect a generated canary
with `just seed-canary NCBITaxon:1035886`, rerun the two focused validators,
then run `just verify-corpus` and `just qc` before publication.
These are future curation checks and were not run as writes in this review.

## Additional Notes

Read-only review on branch `codex/record-review-extensimonas-20261003`,
HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
The already-closed parallel session's worktrees were preserved.
The target was byte-compared with the initial complete read before this report
was written. No YAML, source, scope, history, status, generated page,
GitHub item, or existing report was changed.
