# YAML Record Review: Neorhizobium galegae bv. officinalis bv. officinalis str. HAMBI 1141

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/neorhizobium_galegae_bv_officinalis_bv_officinalis_str_hambi_1141.yaml`
- Started UTC: 2026-10-03T13:05:09Z
- Finished UTC: 2026-10-03T13:07:08Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1028801`, Neorhizobium galegae bv.
officinalis bv. officinalis str. HAMBI 1141. Rank `STRAIN`, domain `BACTERIA`,
parent `NCBITaxon:323656`, grounding `EXACT`, mapping status `SEEDED`.

Read all 96 YAML lines, including 12 lineage entries, one GTDB mapping,
three synonyms, one xref, zero BacDive strain entries, four attestations
and the embedded seed event. No publication, sequence or genome accession
is directly asserted in the target. Source genome metadata were checked
to establish mapping scope and distinguish missing evidence from a model
boundary.

Read-only review: no source, YAML, history, status or generated page was
edited; only this report was manually written. Eukaryota was excluded.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/neorhizobium_galegae_bv_officinalis_bv_officinalis_str_hambi_1141.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/neorhizobium_galegae_bv_officinalis_bv_officinalis_str_hambi_1141.yaml` | PASS; one file, zero errors. |
| Complete identity and lineage comparison | PASS; label, rank, parent, code and all 12 ancestor objects match the raw taxonomy. |
| Complete BacDive subtree check | PASS; subtree contains only taxon 1028801; zero classified strains matches the YAML. |
| Complete GTDB species census and mapping-target check | PASS for source fidelity: four distinct accessions and four taxids match four raw mapping rows. Only one genome is HAMBI 1141. |
| Source-attestation counts | PASS against raw inventories: one NCBI name, four GTDB genomes, two GOLD organisms, five Madin assertions. GOLD reconstruction limitation is below. |
| `just verify-corpus` | Not run: full-corpus reproduction check; no focused substitute was invented. |
| `just validate-history` | Not run: ignored-inclusive target searches found no standalone history. Strict validation checked the embedded seed event. |
| Graph and products | No graph asserted; graph grounding is not applicable. Generated pages and exports were not checked. |

The live GTDB taxon page failed to load. StrainInfo's web page returned only
an application shell, so the complete native record was used. Initial NCBI
fetch failures were resolved through linked Taxonomy, BioSample and
BioProject pages. PubMed metadata, abstract and figure captions were read;
the PMC full text was blocked by a browser challenge and was not treated
as inspected full text.

## Identity and Grounding

The [current NCBI summary](https://www.ncbi.nlm.nih.gov/taxonomy/1028801)
identifies this taxon as a strain. The repeated `bv. officinalis` text is
present in that source and in all three native target name objects at
`data/catalog/ncbi_names-0005.jsonl.gz:28258` onward. It was not introduced
by the YAML emitter and should not be silently removed locally.

The [legacy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028801&mode=Info)
agrees on taxid, label, biovar parent, lineage and code 11, but its served
version says `no rank` and labels the older Rhizobium strain name a
heterotypic synonym. The current summary supports `STRAIN`; the pinned
native names classify the older name as a generic synonym. Preserve this
name-class difference pending source reconciliation. The two NCBI exact
synonyms match the pinned inventory and the generic/equivalent-name policy
in `src/taxonmech/ncbi_taxdump.py`.

`data/raw/ncbitaxon_taxa.tsv:219206` supplies the complete identity. The
record distinguishes species 399, biovar 323656 and strain 1028801. Bare
GTDB species Neorhizobium sp023006505 is not an exact name for that strain
(M1). NCBI's lineage is retained separately from GTDB's Rhizobiales
classification; no reconciliation of those source hierarchies was inferred.

## Evidence

**Raw provenance.** `data/raw/gtdb_species.tsv:125817` and
`data/raw/gtdb_mappings.tsv:1240` support the species identifier, count four
and imported closeMatch. `data/raw/gold_organisms.tsv:354` and
`data/raw/madin_taxa.tsv:533` support two organisms and five trait assertions.
`curation/seed_scope.tsv:26053` supports the four-source seed selection.
The embedded event is a seed event, not a review or human approval.

**Full GTDB membership.** Read all four matching native genome objects and
independently streamed every GTDB shard to verify exact species membership:

| Accession | Native strain | NCBI taxid | Native object |
| --- | --- | --- | --- |
| RS_GCF_000731295.1 | HAMBI 1141 | 1028801 | `data/catalog/gtdb_genomes-0013.jsonl.gz:13077` |
| RS_GCF_023006505.1 | SHOUNA12A | 2908923 | `data/catalog/gtdb_genomes-0008.jsonl.gz:36626` |
| RS_GCF_023006485.1 | BETTINA12A | 2908924 | `data/catalog/gtdb_genomes-0010.jsonl.gz:11285` |
| RS_GCF_023006405.1 | SHOUNA12B | 2908928 | `data/catalog/gtdb_genomes-0007.jsonl.gz:1119` |

SHOUNA12A is the representative; HAMBI 1141 is not. SHOUNA12B retains
source metadata indicating metagenome derivation and non-axenic culture;
the count is a count of source genomes, not four equivalent pure cultures.
All four raw mapping targets carry closeMatch, at lines 1240, 232670,
232671 and 232675. Thus this predicate is not proof of one-to-one
species/strain identity. Retain four as the source-cluster count; it is
not four HAMBI 1141 genomes.

**Target genome context.** Read complete native objects in the following
sources, without treating their presence as permission for an unsupported
BacDive join:

| Source | Checked context |
| --- | --- |
| GenBank | `data/catalog/ncbi_genbank-0000.jsonl.gz:27122`: GCA_000731295.1, HAMBI 1141, taxid 1028801/species 399, SAMEA3139072, PRJEB1951, complete three-replicon assembly. |
| RefSeq | `data/catalog/ncbi_refseq-0000.jsonl.gz:23558`: GCF_000731295.1, same strain/sample, project PRJNA224116, explicitly identical paired GenBank assembly. |
| BV-BRC | `data/bvbrc/bvbrc-0000.jsonl.gz:2988` onward: 1028801.10 and 1028801.11 are plasmid records for HG938356 and HG938357; 1028801.3 is the complete record containing three accessions. |
| GOLD | `data/gold/organisms.jsonl.gz:48376`, `projects.jsonl.gz:47594`, `analyses.jsonl.gz:35727`: Go0081454 -> Gp0081454 -> Ga0056505, HAMBI 1141, taxid 1028801, PRJEB1951, GCA_000731295.1 and IMG 2585427633. The project's BioSample field is empty; do not fill it from another source. |

The inspected [BioSample record](https://www.ncbi.nlm.nih.gov/biosample/?term=txid1028801%5BOrganism%3Anoexp%5D)
confirms SAMEA3139072, strain HAMBI 1141 and PRJEB1951. The
[BioProject record](https://www.ncbi.nlm.nih.gov/bioproject/212246)
explicitly links that sample to GCA_000731295.1 and taxid 1028801.

[PMID 24948393](https://pubmed.ncbi.nlm.nih.gov/24948393/) resolves to the
genome study identified in native assembly metadata. Its figure captions
distinguish orientalis HAMBI 540 type strain from officinalis HAMBI 1141.
This is identity context, not a new phenotype, gene or mechanism assertion
on the reviewed record.

**StrainInfo is a distinct source record.** Read the complete object at
`data/straininfo/records.jsonl.gz:12149`: SI-ID12149 includes LMG 15146,
HAMBI 1141 and ATCC 51627, each explicitly not type strain. Its unversioned
GCA_000731295 genome assertion names HAMBI deposit SI-DP46138. Do not append
`.1` to the source accession or equate marker sequences with whole genomes.

`data/straininfo/exclusions.tsv:13956` explicitly records
`no_eligible_own_deposit_match` for exactly `straininfo.strain:12149`.
Ignored-inclusive checks of the local BacDive deposit inventory and native
BacDive capture found no HAMBI 1141, ATCC 51627 or LMG 15146 match. No
target link was found in the uncapped StrainInfo overlap tables, including
compressed related records. The overlap is not the full source catalog.

The legacy NCBI LinkOuts to BacDive 13626 and StrainInfo 4763 name the
species' type strain, not HAMBI 1141. They must not be used as identity
joins. The target BioSample instead links SI-ID12149, consistent with the
native deposit record. No BacDive identity was invented from those links.

**GOLD count remains partly unresolved.** The raw count is two, while a
full structured scan of the native GOLD organism catalog finds one exact
taxid match, Go0081454. These are different provenance routes under
`docs/HARMONIZATION.md`: KGX attestations versus the native workbook.
The configured KG-Microbe `data/transformed/gold/edges.tsv` is unavailable;
its manifest pin is SHA-256
`b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12`.
The two underlying KGX organisms were not independently reconstructed.
This limitation does not establish that the YAML count should become one.

## Completeness

The identity, lineage, code and seed audit are complete for the pinned
record. Zero BacDive strains is correct under current classification and
join rules. The absent genome links are a BacDive-dependent representation
boundary, not proof that the strain has no sequenced genome or deposit.
No target-specific LPSN nomenclature is asserted; the species type must
not be transferred from HAMBI 540 to this strain.

Ignored-inclusive identifier/name/slug and exact culture/sample searches
covered `history/`, `data/raw/`, `data/bacdive/`, `data/atb/` and
`data/straininfo/`, using decompression where needed. No standalone target
history or target ATB match was found in these bounded locations. Native
StrainInfo evidence and its explicit exclusion were retained in the review.
These are local-snapshot findings, not worldwide absence claims.

No phenotype, gene, regulator, transcriptomics or causal graph is asserted
in the YAML. iModulonDB is not applicable; publication mentions in source
metadata do not create a transcriptomic claim requiring an adapter query.

## Findings

Blocker: 0. Major: 1. Minor: 0.

**M1 (major): a GTDB species is promoted to exact strain identity.** YAML
lines 56-59 label Neorhizobium sp023006505 an `EXACT_SYNONYM` of HAMBI 1141;
lines 63-64 add the species identity xref. The complete four-genome census
contains three other named isolates and four NCBI taxids. CloseMatch does
not support biological equivalence between this strain and the cluster.

Maintained owner: `src/taxonmech/seed.py:451` promotes any closeMatch to
identity without a rank/scope check; lines 467-469 emit the xref and exact
synonym. `src/taxonmech/extract.py` carries upstream mapping predicates,
and `docs/HARMONIZATION.md` explains the promotion policy. Neither the
generated YAML nor the raw TSV should be manually patched.

## Recommended Edits

1. In a separately authorized change, add rank/scope-aware GTDB identity
   handling in `src/taxonmech/seed.py`. Omit this broader species exact
   synonym and identity xref while preserving the NCBI strain aliases and
   source classification evidence.
2. Review the source-predicate policy and document source-cluster counts
   clearly in `docs/HARMONIZATION.md`. Do not change four to one while
   retaining species-count semantics, or guess a replacement predicate.
3. Add `tests/test_seed.py` regression coverage for strain, subspecies and
   unranked below-species targets receiving species closeMatch rows, plus
   a valid same-scope species identity case. Re-seed only through the
   documented dry-run and canary workflow after authorization.

## Follow-up Checks

Run focused seed tests, both target validators, dry `just seed`, then
`just seed-canary NCBITaxon:1028801` after the maintained fix. Inspect the
actual result: no broader exact synonym/xref, retained source mapping/count
context and unchanged NCBI strain aliases. Run full `just verify-corpus`
before accepting a corpus-wide regeneration.

Reconcile the legacy NCBI synonym class against a current authority view
and the pinned native names without silently preferring one. Recover the
manifest-matching GOLD KGX input to explain its two-organism count. A future
proposal to expose non-BacDive strain-genome evidence needs an explicit
schema/join design; it must not fabricate a BacDive match for SI-ID12149.

## Additional Notes

Schema success does not detect M1's biological scope error. No review
status, curation event or standalone history was added. The duplicated
biovar wording is source-derived and is separate from the demonstrated
GTDB identity defect. No report-quality claim is inferred solely from the
existence of a matching filename.
