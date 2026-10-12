# YAML Record Review: Afipia carboxidovorans OM4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/afipia_carboxidovorans_om4.yaml`
- Started UTC: 2026-10-03T08:33:07Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:38:34Z
- Verdict: needs curation

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1031710` denotes
Afipia carboxidovorans OM4, beneath species `NCBITaxon:40137`. It declares
`STRAIN`, `BACTERIA`, `EXACT` grounding and `SEEDED` mapping status. It has
ten ancestors, one GTDB mapping, two exact synonyms, one GTDB xref, genetic
code 11, zero attached strains, three source attestations and one seeding
event. The target is indexed at `data/taxa/PATHS.tsv:13123`.

## Validation

- `just validate data/taxa/bacteria/afipia_carboxidovorans_om4.yaml`: passed,
  no issues found.
- `just validate-strict data/taxa/bacteria/afipia_carboxidovorans_om4.yaml`:
  passed, one file scanned and zero errors. Both validators were repeated
  successfully before writing this report.
- Structured YAML/TSV comparisons confirmed the stored identifier, label,
  rank, parent and genetic code, plus all ten ancestor IDs, labels, ranks
  and parent links. The full taxonomy-inventory scan found zero direct
  children.
- A structured scan of native GTDB metadata found four members of the exact
  species cluster, distributed across three NCBI taxon IDs. Only one member
  is assigned to this target. Syntax validation does not detect the identity
  inflation described below.
- `just verify-corpus` was not rerun: the repository exposes a full-corpus
  check, not a focused reproduction command. Full source hashes, catalog
  censuses and rendered pages were not revalidated.
- `just validate-products` was not run: there are no causal-graph nodes.
  `just validate-history` was not run: the ignored-file-inclusive target
  search found no separate history artifact. The embedded event was inspected
  and covered by strict validation.
- `git diff --exit-code -- data/taxa/bacteria/afipia_carboxidovorans_om4.yaml`
  passed before report creation. No generated record or maintained input was
  changed.

## Identity and Grounding

The inspected [NCBI OM4 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1031710)
supports the identifier, current name, former Oligotropha name, code 11 and
lineage. Its rank is `no rank`, unlike the stored `STRAIN`. The primary
identity and species-and-below scope are sound; the rank discrepancy remains
unresolved against the pinned source version.

The GTDB species cluster includes OM4, OM5 and SH5. Its species-only name is
not an exact synonym for OM4. Membership in that cluster does not establish
equivalence between this strain-level taxon and the entire species concept.

## Evidence

| Claim group | Inspected evidence and interpretation |
| --- | --- |
| NCBI identity and ancestry | `data/raw/ncbitaxon_taxa.tsv:220779` supplies the target name, stored rank, parent, code and snapshot. All ten ancestor rows were separately compared. The browser agrees on identity and placement but differs on rank. |
| NCBI synonym | The scientific-name and equivalent-name rows in `data/catalog/ncbi_names-0005.jsonl.gz:29963` and the following row support Afipia carboxidovorans OM4 and Oligotropha carboxidovorans OM4. The latter is a supported exact synonym, unlike the species-only GTDB name. |
| GTDB mapping and count | `data/raw/gtdb_mappings.tsv:1315` supplies closeMatch and count 4; `data/raw/gtdb_species.tsv:5886` supplies the same cluster total. This GTDB species maps to NCBI targets 1031710, 40137 and 504832 in the mapping inventory, all with closeMatch and count 4. |
| Native OM4 genome | GTDB `RS_GCF_000218585.1` has taxon 1031710, designation OM4, GenBank assembly GCA_000218585.1, BioSample SAMN02603268 and project PRJNA224116. It is not the representative. |
| Other cluster members | `RS_GCF_000218565.1` is the OM5 representative; `RS_GCF_000021365.1` also denotes OM5, with ATCC 49405. Both have taxon 504832. `RS_GCF_037076585.1` has species taxon 40137 and designation SH5. The count of four is therefore not four OM4 genomes. |
| Native assembly catalogs | Current GenBank GCA_000218585.1 and RefSeq GCF_000218585.1 rows have taxon 1031710, species taxon 40137, strain OM4, latest status and sample SAMN02603268. Their project IDs are PRJNA66839 and PRJNA224116 respectively. They explicitly pair the GenBank and RefSeq accessions. |
| Native BV-BRC | Records 1031710.3, 1031710.4, 1031710.5 and 1031710.6 retain the Oligotropha OM4 name, the same GenBank assembly and sample, and PRJNA66839. Four database records must not be interpreted as four distinct assemblies. |
| Native GOLD | Go0005676 identifies OM4 and taxon 1031710 with no culture-collection value. Gp0005676 points to that organism and PRJNA66839. Ga0029685 points to that project and IMG 651053055; its three nucleotide entries CP002823, CP002821 and CP002822 all refer to GCA_000218585.1. Those are not three assemblies, and the GOLD IDs remain organism/project records. |
| Attestations and scope | The NCBI row supports one name assertion. `data/raw/madin_taxa.tsv:585` supports two trait-assertion rows, not two independently verified phenotypes. `curation/seed_scope.tsv:36135` supports the dated three-source rationale. The GTDB attestation repeats the supported species-cluster total but needs scope qualification. |

The parent-species LPSN inventory entry, `lpsn:11076` at
`data/raw/lpsn_names.tsv:2245`, maps to 40137, not OM4. Its type designations
must not be copied onto this target. The target cites no LPSN name, DOI or
PMID requiring separate claim verification. Native GTDB order/family labels
differ from NCBI's; they do not authorize changing the carried NCBI lineage.

## Completeness

The identifier, current name and slug were searched with
`rg --no-ignore --hidden` across review reports, history, curation and
raw/ATB/StrainInfo inventories. Before this report, matches were limited to
the taxonomy, GTDB mapping, Madin, seed-scope and legacy-page rows. No prior
target report or separate history artifact was found in those surfaces.
Compressed JSONL.GZ and TSV.GZ catalogs under `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/` and `data/straininfo/` were also searched with
decompression for the exact taxon fields, current/former name and slug.
The native matches are described above. No matching Afipia OM4 BacDive or
StrainInfo record was found in that bounded scan.

An older NCBI browser response supplied a BacDive type-strain link-out, but
the inspected [BacDive 1797 page](https://bacdive.dsmz.de/strain/1797)
identifies OM5, taxon 504832, with DSM 1227, ATCC 49405 and KCTC 32145.
It is not evidence that those deposits belong to OM4. The raw BacDive
inventory agrees. A separate standalone-OM4 search found BacDive 169715,
but its taxon 2775404 is Mesorhizobium onobrychidis, not Afipia. This is a
name collision, not a missing target association.

Zero attached strains is consistent with the present model's requirement
for supported BacDive identities and direct or registered culture-deposit
evidence. Bare OM4 is not a collection accession. The catalog genomes must
not be discarded or misreported as absent, but neither may they be attached
to OM5's deposits. More direct exposure of native taxon-to-genome links is
a separate representation question. The absence of a GOLD attestation here
does not mean absence from the native GOLD workbook: that attestation is
derived from the maintained KGX inventory. No additional phenotype,
nomenclature or causal-graph assertions should be invented to fill optional
slots.

## Findings

- **Blocker:** None found in the primary NCBI identity or file structure.
- **Major (1): Species-cluster association promoted to strain identity.**
  `src/taxonmech/seed.py:451` treats every imported closeMatch as identity,
  and lines 467-469 generate the xref and exact synonym. This produces
  `Afipia carboxidovorans` as an exact synonym of OM4 despite the inspected
  cluster including distinct OM5 and SH5 genomes. The mapping and its
  attestation need explicit scope treatment; count 4 is the correct cluster
  total, not evidence of strain equivalence. The imported predicate belongs
  to the kg-microbe GTDB transform, consumed by
  `src/taxonmech/extract.py:extract_gtdb`; the local identity promotion belongs
  to `src/taxonmech/seed.py:build_document`.
- **Minor (1): Unresolved NCBI rank discrepancy.** The browser reports
  `no rank`, whereas the pinned inventory stores `STRAIN`. The importer in
  `src/taxonmech/ncbi_taxdump.py` normalizes the supplied rank rather than
  inferring it from the organism name. The pinned archive is unavailable
  in this checkout, so source-version divergence versus import error is
  unresolved. This does not invalidate the identity or parentage.

## Recommended Edits

1. In a separately authorized correction, make
   `src/taxonmech/seed.py:build_document` distinguish an infraspecific taxon's
   species-cluster membership from identity before adding exact synonyms
   and equivalence-style xrefs. Preserve the supported Oligotropha OM4 name.
2. Review the owning upstream GTDB mapping rule with this concrete example,
   then re-extract through `src/taxonmech/extract.py:extract_gtdb` as needed.
   Determine predicate scope and direction from evidence; do not mechanically
   flip closeMatch to broadMatch/narrowMatch or change the cluster count
   from four to one.
3. Add a regression case in `tests/test_seed.py` for a species-level GTDB
   association on a strain/unranked child while retaining supported
   species-level mappings. Do not add OM5 deposits or the unrelated
   Mesorhizobium OM4 record.
4. Recover and inspect the hash-verified NCBI snapshot before changing rank
   inputs or importer behavior. Generated YAML and carried lineage are not
   manual correction surfaces.

## Follow-up Checks

- Run the focused seeder regression and existing `tests/test_seed.py` cases.
  Confirm ID 1031710, parent 40137 and the supported NCBI synonym remain,
  without asserting equivalence to the GTDB species.
- Recheck the four native GTDB cluster members and the single member with
  taxon 1031710. Preserve assembly/sample/project distinctions and reject
  unsupported deposit joins.
- Inspect taxon 1031710 in the original `nodes.dmp` from the snapshot pinned
  in `conf/ncbi_taxdump.yaml`, SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- After an authorized fix, use the normal extraction/seeding workflow,
  `just seed-canary NCBITaxon:1031710`, both target validators and the full
  `just verify-corpus`.

## Additional Notes

The live GTDB tree request failed; pinned native RS232 metadata support the
cluster finding. A later NCBI parameterized request failed, but the plain
taxon URL returned usable current text. The ignored-file-inclusive repository
filename search found no taxdump archive or `nodes.dmp`; this says nothing
about copies outside the checkout. The compressed ATB full TSV.XZ was not
scanned, and no full source-hash verification or sequence download was run.

iModulonDB is not applicable: the record has no specific gene, regulator or
expression-module claim. No paid research, outbound messages, GitHub
mutation, history addition or status promotion was performed. This report
does not mark the record reviewed by a human or resolve its findings.
