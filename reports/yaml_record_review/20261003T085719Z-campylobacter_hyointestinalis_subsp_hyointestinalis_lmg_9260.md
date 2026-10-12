# YAML Record Review: Campylobacter hyointestinalis subsp. hyointestinalis LMG 9260

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_hyointestinalis_subsp_hyointestinalis_lmg_9260.yaml`
- Started UTC: 2026-10-03T08:55:54Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:57:19Z
- Verdict: needs curation

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1031746` denotes
LMG 9260 beneath subspecies `NCBITaxon:91352` and species `NCBITaxon:198`.
It declares `STRAIN`, `BACTERIA`, `EXACT` grounding and `SEEDED` mapping
status, with eleven ancestors, one GTDB mapping, three exact synonyms,
one GTDB xref, code 11, zero attached strains, four attestations and one
seed event. Its index entry is `data/taxa/PATHS.tsv:13131`.

## Validation

- `just validate data/taxa/bacteria/campylobacter_hyointestinalis_subsp_hyointestinalis_lmg_9260.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/campylobacter_hyointestinalis_subsp_hyointestinalis_lmg_9260.yaml`:
  passed, one file scanned and zero errors.
- Structured YAML/TSV checks confirmed identifier, label, stored rank, parent,
  code and all eleven ancestor IDs, labels, ranks and parent links. A full
  taxonomy-inventory scan found zero direct children.
- A structured native GTDB scan counted 54 members of the exact species
  cluster across four NCBI taxon IDs; one member has target taxon 1031746.
  The mapping inventory has four targets, two closeMatch and two broadMatch.
- A structured lookup confirmed that BacDive 144674 and its genome links
  are published in the species record `data/taxa/bacteria/campylobacter_hyointestinalis.yaml`,
  under source classification 198. That was a location/content check of
  the relevant strain entry, not a full review of the species record.
- The target-only `git diff --exit-code --` check passed. No record or
  maintained source was edited.
- `just verify-corpus` was not rerun: it is full-corpus-only. Full catalog
  hashes/censuses, ATB source replay and generated pages were not checked.
  `just validate-products` is not applicable without graph nodes.
  `just validate-history` was not run: the ignored-file-inclusive target
  search found no separate history artifact. The embedded event was inspected
  and covered by strict validation.

## Identity and Grounding

The inspected [NCBI LMG 9260 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1031746)
supports identifier, label, two strain-name equivalents, code 11 and lineage
through the hyointestinalis subspecies. It reports `no rank`, unlike the
pinned inventory's `STRAIN`. Identity and species-and-below scope are supported;
the rank-source difference remains unresolved.

The GTDB species concept is not identical to LMG 9260. Its species-only name
is incorrectly promoted to an exact synonym of this strain. The retained
54-genome count describes the cluster, not 54 LMG 9260 genomes. GTDB's
classification remains separate from the carried NCBI lineage.

## Evidence

| Claim group | Inspected evidence and interpretation |
| --- | --- |
| NCBI identity and synonyms | `data/raw/ncbitaxon_taxa.tsv:220784` supports the stored target fields. `data/catalog/ncbi_names-0005.jsonl.gz:29974` and the next two rows retain the scientific name and the `strain LMG 9260`/`str. LMG 9260` equivalents. All ancestor rows were compared separately. |
| GTDB mapping/count | `data/raw/gtdb_mappings.tsv:1318` supplies closeMatch and 54; `data/raw/gtdb_species.tsv:40564` supplies the same total. Native cluster membership comprises 18 genomes at taxon 198, 32 at 91352, three at 1977087 and one at target 1031746. |
| Target member versus representative | RS_GCF_001643955.1 has taxon 1031746 and designation LMG 9260; it is not the representative. RS_GCF_013372145.1 is representative and carries taxon 91352/designation CCUG 14169. The latter is an explicit non-target member. |
| Native assemblies | GenBank GCA_001643955.1 and RefSeq GCF_001643955.1 have latest status, reciprocal pair fields, taxon 1031746, species 198, strain LMG 9260 and BioSample SAMN03737973. Their projects are PRJNA66795 and PRJNA224116 respectively. The native rows are `ncbi_genbank-0001.jsonl.gz:13758` and `ncbi_refseq-0001.jsonl.gz:3374` under `data/catalog/`. |
| BacDive and source classification | `data/raw/bacdive_strains.tsv:66957` files BacDive 144674 at species 198, with CCUG-26150 and LMG-9260. The native row `data/bacdive/records.jsonl.gz:66956` preserves that species classification while its genome entry explicitly identifies target 1031746, unversioned GCA_001643955, BV-BRC 1031746.3 and IMG 2687453147. These roles are not contradictory. |
| BV-BRC | Native genome 1031746.3 supplies GCF_001643955.1, sample SAMN03737973, project PRJNA66795, nucleotide CP015575 and both LMG 9260 and LMG:9260 source identifier fields. |
| GOLD | Go0011316 explicitly carries LMG 9260 in both organism strain and collection fields and taxon 1031746. Gp0011316 points to that organism, PRJNA66795 and SAMN03737973. Ga0129146 points to that project, IMG 2687453147 and GCA_001643955.1 through nucleotide CP015575. These native rows occur in `data/gold/organisms.jsonl.gz:9940`, `projects.jsonl.gz:9801` and `analyses.jsonl.gz:75502`. |
| StrainInfo context | `data/straininfo/records.jsonl.gz:1487` retains SI-ID1487/DOI 10.60712/SI-ID1487.2 and two own deposits: LMG 9260 (SI-DP6270) and CCUG 26150 (SI-DP130121). Its unversioned GCA_001643955 genome assertion explicitly names only SI-DP6270. It must not be transferred to the other deposit or assigned an invented version suffix. |
| Attestations/history | `data/raw/gold_organisms.tsv:410` supports one ORGANISM assertion and `data/raw/madin_taxa.tsv:589` supports two TRAIT_ASSERTION rows. NCBI supplies one NAME. `curation/seed_scope.tsv:26074` supplies the dated four-source rationale preserved in the seed event. GTDB's 54 GENOME assertions require the cluster-scope qualification above. |

The inspected [BacDive page](https://bacdive.dsmz.de/strain/144674) independently
supports the deposits, species filing and genome identifiers. The target
does not itself cite LPSN nomenclature or a paper. Its NCBI-linked genome
publication, PMID 27417840, did not return usable PubMed content, and the
LMG collection link returned a loading shell. Neither failed request was
used to establish additional claims.

## Completeness

Identifier, exact name and slug were searched with
`rg --no-ignore --hidden` in reports, history, curation, raw, ATB and
StrainInfo inventories. No prior target report or separate history artifact
was found before this report. Numerous strain-genome and related-record
matches were inspected rather than incorrectly dismissed because the target
has zero attached strains. Decompressed JSONL.GZ/TSV.GZ searches of
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/` and
`data/straininfo/` also checked exact taxon fields and LMG 9260 separator
variants, including ignored files.

The source-classified BacDive entry is already present under species 198
in `data/taxa/bacteria/campylobacter_hyointestinalis.yaml`. Its attached
assemblies include the source-supplied unversioned GCA_001643955 and versioned
GCA_001643955.1/GCF_001643955.1, and its typed genome records include GTDB,
IMG and BV-BRC. Thus the target's zero strain count reflects the documented
classification boundary, not lost deposit/genome evidence. Do not reclassify
BacDive from the genome taxon, duplicate its entry into the target, or report
that LMG 9260 lacks a genome. Improved cross-navigation is a separate design
question from correcting the false exact synonym.

The inspected species/subspecies LPSN inventory rows (783590/783591) do not
make this strain the name-bearing type. Their designations include LMG 7817
and CCUG 14169, not LMG 9260. Empty nomenclature/type slots are appropriate.
The native BacDive type value is no; an unqualified heading in extracted web
text was not treated as evidence to override explicit source fields.

## Findings

- **Blocker:** None found in primary identity or structure.
- **Major (1): Species-cluster membership promoted to strain identity.**
  `src/taxonmech/seed.py:451` treats the imported closeMatch as identity and
  lines 467-469 generate a species-only exact synonym and xref. The native
  cluster includes many non-LMG-9260 genomes, so that promotion is unsupported.
  The upstream predicate belongs to the kg-microbe GTDB transform consumed
  by `src/taxonmech/extract.py:extract_gtdb`; the local identity promotion
  belongs to `src/taxonmech/seed.py:build_document`.
- **Minor (1): Unresolved source-rank discrepancy.** The accessible NCBI
  browser says `no rank`; the pinned inventory says `STRAIN`.
  `src/taxonmech/ncbi_taxdump.py` normalizes the supplied source rank. The
  unavailable original archive prevents distinguishing source-version
  divergence from an import error. Parentage and eligibility are unaffected.

## Recommended Edits

1. In a separately authorized correction, prevent species-cluster closeMatch
   from automatically creating strain-level exact synonyms/equivalence xrefs.
   Preserve the two supported NCBI synonyms and source provenance.
2. Review the owning upstream mapping rule and its direction before refreshing
   `src/taxonmech/extract.py:extract_gtdb` inputs. Do not mechanically replace
   the predicate or change the supported species total 54 to one.
3. Add an infraspecific mapping regression to `tests/test_seed.py`, including
   a subspecies ancestor, while preserving supported species-level behavior.
   Keep the BacDive entry filed under its source-classified species.
4. Inspect the pinned taxonomy rank before modifying source/importer behavior.
   Generated YAML and NCBI lineage are not manual correction surfaces.

## Follow-up Checks

- Confirm regenerated ID 1031746 retains parent 91352 and both NCBI synonyms
  while dropping unsupported species-wide exact equivalence.
- Recheck the 54-member cluster and single target member. Preserve distinct
  source identities, accessions and versions on the species-owned strain entry.
- Recover the archive pinned in `conf/ncbi_taxdump.yaml`, SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`,
  and inspect the exact 1031746 `nodes.dmp` rank.
- After an authorized fix, run seeder regressions, the normal refresh,
  `just seed-canary NCBITaxon:1031746`, both target validators and the full
  `just verify-corpus`.

## Additional Notes

The live GTDB tree failed; native RS232 metadata support the scope finding.
The accessible NCBI response was cached eight months earlier, not proof of
an importer defect. No focused StrainInfo query or full ATB scan was run for
this target: those links are context on another record, and only their
inspected source/location facts are reported here. iModulonDB is not applicable
to these taxonomy and aggregate-count claims. No paid research, external
messages, GitHub mutation, history addition or review-status promotion occurred.
