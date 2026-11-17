# YAML Record Review: Pontixanthobacter gangjinensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pontixanthobacter_gangjinensis.yaml`
- Started UTC: 2026-10-03T12:09:52Z
- Finished UTC: 2026-10-03T12:14:40Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:1028742`, Pontixanthobacter gangjinensis,
rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2792075` (Pontixanthobacter).
Grounding is `EXACT`; mapping status is `SEEDED`.

Read the entire 585-line YAML, including all source/evidence fields. It contains
one BacDive strain, 12 assembly assertions, eight genome-record assertions,
24 related-record assertions and six source attestations. Repeated accessions
retain distinct source or matching-field evidence; assertion counts are not
counts of unique genomes. This review did not modify the generated record,
maintained inputs, source snapshots, history, status or pages.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pontixanthobacter_gangjinensis.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pontixanthobacter_gangjinensis.yaml` | PASS; one file, zero errors. |
| Full lineage and BacDive subtree comparison | PASS; all nine ancestor objects, complete strain membership and all strain scalars agree with the inventories. |
| Full raw strain-link equality | PASS; all 12 assembly, eight genome and 24 related-record objects match the raw tables, not merely their IDs. |
| Native GTDB species-cluster census | PASS; one member, RS_GCF_009827545.1, with NCBI taxid/species-taxid 1028742. |
| Native GOLD field and chain checks | PASS; all 14 GOLD assertions match their source field, name, deposit, taxid and organism/project chain. |
| `just verify-corpus` | Not run: documented full-corpus reproduction check. The focused comparisons above are not a replacement. |
| `just validate-history` | Not run: ignored-inclusive identifier/label/slug search found no standalone target history. Strict validation checked the embedded seed event. |
| Graph and generated-product checks | Not run: no graph is asserted; generated pages and other products were outside this record review. |

External references were checked against native snapshots and inspected pages
below. Live independent resolution was incomplete for several references;
access failures are not evidence that an accession or citation is invalid.

## Identity and Grounding

The inspected [NCBI Taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028742)
supports the current species name, rank, parent, lineage, genetic code 11 and
type material. The complete local taxonomy subtree contains only this taxon.
Native NCBI name records support the exact former-name synonym and related
authority/includes names; no broader includes-name was promoted to exact.

The [current LPSN name](https://lpsn.dsmz.de/species/pontixanthobacter-gangjinensis)
supports the 2020 combination, authority, correct-name status and JF751048.
The [basionym page](https://lpsn.dsmz.de/species/altererythrobacter-gangjinensis)
resolves `lpsn:790594` and identifies the former name as a homotypic synonym.
The YAML's source-specific LPSN related synonym is conservative; NCBI's exact
synonym is separately retained. This does not equate unrelated species.

GTDB's single representative is JCM 17802 and supports the species-scoped
`skos:closeMatch` and genome count of one. Native GTDB uses Sphingomonadaceae,
whereas the NCBI lineage uses Erythrobacteraceae. The record preserves NCBI's
lineage rather than silently merging those classifications. Other taxa named
gangjinensis, including Polaribacter and Alteraurantiacibacter, were excluded
by exact full-species and identifier checks.

## Evidence

**Nomenclature.** All root identity and nomenclature values trace to
`data/raw/ncbitaxon_taxa.tsv:219192` and `data/raw/lpsn_names.tsv:2518`.
The inspected LPSN type list includes JCM 17802, KACC 16190 and designation KJ7.
The YAML retains both collection deposits on BacDive 133814 but only JCM 17802
in the nomenclature list; finding M1 addresses that bounded discrepancy.
KJ7 remains a strain designation, not a fabricated registered collection ID.

**Publications and marker.** The inspected
[Xu et al. publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.004293?crawler=true)
provides the DOI, authors, date, title and abstract of the genomic classification
paper. Its abstract supports the genus-level reclassification context; LPSN
supplies the precise species combination. The NCBI taxonomy reference links
to PMID 32726199, but the PubMed page exposed only its footer. The notification
DOI 10.1099/ijsem.0.004464 is present in the raw nomenclature row and search
metadata agrees with the listed notification; publisher/Crossref fetches failed.
That independent DOI check remains partial, not a verified broken citation.
The paper's full text and notification list were not read.

JF751048 is supported by LPSN and the native/live BacDive sequence metadata as
the KJ7 16S marker. BacDive retains its source's UNVERIFIED_ORG qualifier.
The live nucleotide page was unavailable, so sequence identity/quality was not
independently reassessed or elevated beyond a source-linked accession.

**BacDive.** Read the full relevant native identity, literature and sequence
objects, and the [BacDive 133814 page](https://bacdive.dsmz.de/strain/133814).
Designation KJ7, taxid 1028742, both deposits and type-strain status agree.
The native objects support unversioned GCA_009827545 and GCA_039540935,
source references 67770 and 124043, BV-BRC 1028742.5 and IMG 2989223851.
The second native assembly does not supply a BV-BRC/IMG accession; the YAML
does not invent a BacDive assertion for either. Its separate BV-BRC .6 link
has its own explicit source evidence.

**Native assembly and project chains.** Complete taxid searches of the native
current/historical NCBI catalogs found exactly three assembly rows, BV-BRC
found two genomes and GOLD found one organism. Read all of those native rows
plus the linked GOLD project and analysis, including their source metadata.

| Assembly group | Explicit strain evidence | Sample/project chain |
| --- | --- | --- |
| GCA_009827545.1 / GCF_009827545.1 | JCM 17802 in NCBI, BV-BRC .5, GTDB and GOLD | SAMN13631579; PRJNA481858 in GenBank/BV-BRC/GOLD, PRJNA224116 in RefSeq/GTDB. |
| GCA_039540935.1 | JCM 17802 in NCBI and BV-BRC .6; BV-BRC also has JCM:17802 | SAMD00645708; PRJDB10510. |

The native NCBI pairing explicitly supports the first GCA/GCF pair. No GCF
counterpart was inferred for the second. Source names using Altererythrobacter
in BV-BRC .5 are retained verbatim and refer to the supported former name.
Whole-culture parser checks accept JCM 17802, JCM:17802 and KACC 16190, while
rejecting bare KJ7. Every non-BacDive genome join uses the matching JCM deposit.

GOLD's chain is Go0044483 -> Gp0551130 -> Ga0488941. The analysis lacks an
explicit organism ID but its project resolves unambiguously to that organism.
The assembly and IMG assertions come from the analysis; BioSample/BioProject
assertions come from the project. Both organism culture and strain fields
independently support the repeated JCM deposit assertions.

**Counts and optional overlays.** The inventory supports one NCBI name, one
LPSN name, one GTDB genome, one BacDive strain, one GOLD organism and six MADIN
trait assertions. `medium_count: 1` is the strain-level MediaDive count in
the BacDive inventory, not a species-level MediaDive attestation. Counts alone
do not assert a phenotype or a medium recipe.

Ignored-inclusive, decompressed searches found no matching native StrainInfo
record or committed overlay for exact SI-ID 28016, BacDive 133814, either
species name or the two deposits. BacDive does link SI-ID 28016, but its live
page was unavailable. The source manifest declares an all-records snapshot;
the absence of that particular record remains a snapshot/access limitation,
not justification to synthesize an own-deposit assertion from the BacDive link.
Neither SAMN13631579 nor SAMD00645708 occurs in the full native ATB table or
the committed ATB overlap. No ATB assertion is therefore required by those
inspected inputs; this is not a claim of absence from future releases.

## Completeness

The complete local subtree supplies one BacDive strain, and it is included.
All represented assembly, genome and related-record objects are accounted for.
M1 is the only confirmed record-level gap. Optional phenotype, mechanism,
experimental evidence and causal-graph fields need not be invented for this seed.

Raw, curation and history searches included ignored/hidden files and the
identifier, label and slug. Scope and legacy-path rows exist. No prior report
or standalone target history was found. Compressed source searches included
native data rather than relying on an ignored-aware repository search.

## Findings

Counts: **0 blocker, 0 major, 1 minor**.

**M1 - Minor: KACC 16190 is omitted from the LPSN type-deposit list.**
YAML lines 48-49 list only JCM 17802, although the inspected LPSN page includes
KACC 16190. NCBI's native type-material inventory independently retains KACC
16190 at `data/raw/ncbi_type_material.tsv:1430`. The deposit already exists in
the same strain's `culture_collection_ids` at YAML line 92, and the existing
JCM overlap correctly establishes `is_type_strain: true`.

The incomplete list is already present in `data/raw/lpsn_names.tsv:2518`.
`src/taxonmech/seed.py:405` faithfully projects it. The future fix belongs in
the maintained upstream KG-Microbe LPSN transform supplying type-deposit
edges, consumed by `src/taxonmech/extract.py:445`; the exact upstream loss stage
was not established. Do not hand-edit the generated YAML or raw row.

## Recommended Edits

1. In a separate authorized curation change, inspect the upstream LPSN input
   and transform for 13078 and preserve the supported KACC 16190 type deposit.
   Keep JCM 17802 and the existing true type-strain flag. Do not turn KJ7 into
   an eligible culture identifier or change unrelated strain/genome joins.
2. After correcting the maintained source/transform, run `just extract-inventory`
   with its configured checkout, dry-run `just seed`, then use
   `just seed-canary NCBITaxon:1028742` to regenerate the target.

## Follow-up Checks

- Verify both registered type deposits against LPSN and the revised inventory;
  add a focused regression at the upstream extraction boundary.
- Rerun the two exact record validators and compare all source-link objects
  to ensure that this nomenclature fix did not alter genome provenance.
- Run `just verify-corpus` before merging a curation change; it was not run here.
- Retry the notification DOI, PubMed, nucleotide and StrainInfo pages when
  accessible. Check SI-ID 28016's own deposits before proposing any overlay.

## Additional Notes

The newer assembly GCA_039540935.1 has native NCBI
`excluded_from_refseq: contaminated; not used as type`, no paired RefSeq
accession and no affirmative assembly-from-type-material status. This is
important source-quality context, not a reason to silently delete its supported
strain link. `GenomeAssemblyLink` at schema line 870 denotes a source-reported
relationship, not taxonomic classification, quality certification or sequence
equivalence. The strain's type flag is not an assertion that every linked
assembly is suitable type material. The older GCA/GCF_009827545.1 group does
have an affirmative native type-material designation. No suitability claim
for comparative genomics is made by this review.

The GTDB live taxon page, JCM page and several reference endpoints failed;
native snapshots and the successfully inspected authority pages supplied the
bounded checks described above. The initial NCBI detail URL failed, but the
alternate taxid URL returned the species page. PMC presented a browser check;
it was not bypassed. iModulonDB was not applicable: the YAML asserts no named
functional gene, regulator, pathway or transcriptomic claim. No source refresh,
catalog rebuild, curation event or review-status promotion was performed.
