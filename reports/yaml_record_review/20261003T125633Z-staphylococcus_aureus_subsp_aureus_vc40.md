# YAML Record Review: Staphylococcus aureus subsp. aureus VC40

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_vc40.yaml`
- Started UTC: 2026-10-03T12:54:06Z
- Finished UTC: 2026-10-03T12:56:33Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1028799`, Staphylococcus aureus subsp.
aureus VC40, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:1280`
(Staphylococcus aureus). Grounding is `EXACT`; mapping status remains `SEEDED`.

Read the entire 89-line YAML. It contains one GTDB species mapping, three
synonyms, one xref, zero BacDive strain entries and four source attestations.
There is no record-level publication, sequence accession or genome link.
The principal finding concerns species-to-strain equivalence, not the
correctly identified NCBI taxon or valid YAML shape.

This is a read-only review. No source, generated record, history, status or
page was changed; only this review report was manually written.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_vc40.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_vc40.yaml` | PASS; one file, zero errors. |
| Full identity, lineage and subtree | PASS; label, rank, parent, code and all ten ancestor objects match the raw taxonomy; subtree contains only this taxon. |
| Complete BacDive subtree membership | PASS; no classified BacDive strain exists in the raw subtree; zero matches the YAML. |
| Complete native GTDB species census | PASS for the source count: 19,502 distinct genome accessions, 4,209 NCBI taxids, one VC40 genome. This does not validate M1's equivalence. |
| Complete GTDB mapping-target check | PASS for inventory fidelity: 4,209 target rows for this species; the target's row carries `skos:closeMatch` and count 19,502. |
| `just verify-corpus` | Not run: full-corpus reproduction check, not a focused record validator. Target checks do not substitute for it. |
| `just validate-history` | Not run: ignored-inclusive identifier/name/slug searches found no standalone target history. Strict validation checked the embedded seed event. |
| Graph and generated products | Not run: no graph is asserted; generated pages and other products were outside this review. |

The live GTDB species and genome pages were unavailable. The native catalog
and raw inventories support the snapshot-specific checks. No archive sequence
payload or full article body was reassessed.

## Identity and Grounding

The inspected [NCBI Taxonomy summary](https://www.ncbi.nlm.nih.gov/taxonomy/1028799)
identifies VC40 as a strain. The complete raw taxon row at
`data/raw/ncbitaxon_taxa.tsv:219204` supplies the same identity and direct
species parent. The text `subsp. aureus` in the label does not authorize
inserting an unrecorded subspecies node into its NCBI lineage.

The retrieved [legacy NCBI browser page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028799)
confirms the identifier and both VC40-specific equivalent names, but its
older served version says `no rank` and uses Bacillales. The current Entrez
summary says strain; the inspected BioSample/BioProject pages and pinned
taxonomy use Caryophanales. `data/raw/ncbitaxon_taxa.tsv:1076` retains
Bacillales as an exact synonym of the same order ID 1385. This is a
source-version difference, not evidence to overwrite the pinned lineage.

All three native name rows at
`data/catalog/ncbi_names-0005.jsonl.gz:28252` onward were inspected. They
support the two NCBI exact variants containing `str. VC40` and `strain VC40`.
They do not support bare Staphylococcus aureus as an exact strain name.

VC40 also occurs in unrelated Vibrio, Enterobacter and Sphingomonas source
records. Those hits were rejected by source taxid and organism context;
a bare designation is not a cross-genus identity key.

## Evidence

**Raw provenance.** `data/raw/gtdb_mappings.tsv:1238` supplies the species
mapping and `data/raw/gtdb_species.tsv:168198` supplies its 19,502-genome
count. `data/raw/gold_organisms.tsv:352` and `data/raw/madin_taxa.tsv:531`
support one organism and one trait assertion. The scope row at
`curation/seed_scope.tsv:26051`, legacy-page entry and embedded seed event
agree on four sources. Source units are not summed or turned into phenotype
claims.

**Species membership is not strain identity.** Read the complete native
VC40 GTDB object at `data/catalog/gtdb_genomes-0014.jsonl.gz:3156`.
RS_GCF_000245495.1 is classified in GTDB species Staphylococcus aureus,
with `ncbi_taxid: 1028799`, `ncbi_species_taxid: 1280` and strain VC40.
A streaming structured census of every native GTDB genome shard found
19,502 distinct members of exactly that species, covering 4,209 NCBI taxids.
Only one of those members carries target taxid 1028799. No member sampling
or substring count was substituted for the full species census.

The raw mapping table likewise contains 4,209 target rows for this species.
Its target-specific closeMatch is therefore not evidence that the species
and VC40 have identical scope. The count 19,502 is correct for the source
species cluster, not a count of VC40 genomes. The count should not simply
be changed to one while still purporting to describe that source species.

**Native genome context exists.** Complete target objects were inspected
in NCBI GenBank, NCBI RefSeq, GTDB, BV-BRC and all three GOLD catalogs:

| Source | Target evidence |
| --- | --- |
| GenBank | `data/catalog/ncbi_genbank-0000.jsonl.gz:4774`: GCA_000245495.1, VC40, taxid 1028799, SAMN02603393 and PRJNA66591. |
| RefSeq | `data/catalog/ncbi_refseq-0000.jsonl.gz:4060`: GCF_000245495.1, same strain/taxid/sample, project PRJNA224116. |
| GTDB | RS_GCF_000245495.1; explicit GenBank accession, target taxid, strain, sample and RefSeq project. |
| BV-BRC | `data/bvbrc/bvbrc-0000.jsonl.gz:2985`: 1028799.3, VC40, GCA_000245495.1, SAMN02603393 and PRJNA66591. |
| GOLD | Go0011759 -> Gp0011759 -> Ga0009441; explicit project/sample chain, structured GenBank accession GCA_000245495.1 and IMG 2511231175. |

Both NCBI assembly rows are current complete-genome records with an explicit
paired accession. The differing GenBank and RefSeq project identifiers are
preserved source provenance. GOLD's analysis has an empty direct organism
field but its single project resolves to Go0011759. That organism's culture
field is empty and its strain field is only VC40. The whole-culture parser
rejects VC40 as a registered deposit identifier.

The inspected [NCBI BioProject](https://www.ncbi.nlm.nih.gov/bioproject/66591)
independently connects target taxid 1028799 to GCA_000245495.1 and
SAMN02603393. The inspected [BioSample](https://www.ncbi.nlm.nih.gov/biosample/SAMN02603393)
names VC40, identifies CP003033 as the sample name and links PRJNA66591.
These support taxon/genome context, not a fabricated BacDive or collection
deposit identity.

The project cites the genome announcement. Its inspected
[PubMed record](https://pubmed.ncbi.nlm.nih.gov/22461548/)
confirms PMID 22461548, DOI 10.1128/JB.06631-11, Sass et al., April 2012
metadata and the VC40 genome abstract. It also lists CP003033 as associated
data. This is additional review evidence, not a citation already asserted
by the YAML. No functional mechanism, resistance-development method or
experimental phenotype was curated from that publication.

## Completeness

`strain_count: 0` means no BacDive entries gathered for this taxon's subtree,
not that VC40 lacks a genome. Complete raw BacDive membership and native
BacDive searches found no target taxid or VC40 identity. The legacy NCBI
browser's external BacDive/StrainInfo links are labelled as the species type
strain, not VC40; they do not authorize borrowing those collection identities.

Current genome-link fields are nested under BacDive strain entries. The native
VC40 objects above have no eligible existing collection deposit through which
the documented pipeline can attach them. Their absence from this YAML is a
model/source-coverage limitation, not a failed join or proof of genome absence.
A taxon-native genome representation would require a separately authorized
schema/extractor/seeder design; do not fabricate a BacDive strain or relax
the whole-deposit rule to populate these optional fields.

Ignored-inclusive searches covered raw inventories, curation, history,
prior-report filenames and decompressed native BacDive, NCBI current/historical
assembly/name, GTDB, BV-BRC, GOLD, StrainInfo and ATB catalogs. Target ID,
name/slug, VC40 spellings and discovered sample/genome identifiers were used.
No target-specific LPSN row, StrainInfo overlay, standalone history or prior
report was found. A species nomenclature entry is not automatically a
strain-level nomenclature assertion.

An exact ignored-inclusive decompressed ATB search found no SAMN02603393
in the overlay or complete native table. Earlier broad numeric hits were
different sample/run identifiers, not the NCBI taxon. No ATB association
is established. These searches do not claim worldwide or future absence.

## Findings

Counts: **0 blocker, 1 major, 0 minor**.

**M1 - Major: species membership is promoted to strain equivalence.**
YAML lines 39-44 retain a species-level closeMatch to this strain; lines
46-49 add the bare species as an `EXACT_SYNONYM`, and lines 56-57 promote
the species to an identity xref. The GTDB attestation repeats the mapping
at lines 67-72 without explaining its species-wide scope. Native source
evidence distinguishes target taxid 1028799 from species taxid 1280 and
shows VC40 as one member of a much broader species cluster.

The NCBI identifier, VC40-specific synonyms and lineage remain supported,
so this is a major semantic mapping defect rather than a wrong-target
blocker. The four source counts are inventory-faithful; the numerical
GTDB count is not independently erroneous.

Owners: `src/taxonmech/seed.py:451` treats any closeMatch as identity without
a rank guard; lines 467-469 promote it to xref and exact synonym. The raw
predicate originates upstream, consumed from KG-Microbe's GTDB edges by
`src/taxonmech/extract.py:516`. Review that maintained upstream transform
and its species-to-infraspecific mapping policy as well. Do not silently
replace it with the opposite directional predicate or hand-edit generated
inventories/YAML.

## Recommended Edits

1. In separate authorized curation, make GTDB identity promotion rank-aware
   in `src/taxonmech/seed.py`. For this strain, remove the species-derived
   exact synonym and identity promotion while retaining both NCBI exact
   VC40 variants and the supported source classification as non-equivalence
   context under an explicit, reviewed mapping policy.
2. Review the upstream GTDB transform's closeMatch policy for infraspecific
   NCBI targets. Preserve raw source provenance; represent the species-to-strain
   direction explicitly rather than guessing a replacement relation. Keep
   the 19,502 count labelled as source-species coverage, not VC40 coverage.
3. Add regressions in `tests/test_seed.py` for strain, subspecies and eligible
   unranked-below-species targets, plus a positive same-species identity case.
   Re-extract only after an upstream change; dry-run `just seed`, then use
   `just seed-canary NCBITaxon:1028799` for the focused regeneration.

## Follow-up Checks

- Verify that VC40-specific identity and NCBI synonyms are unchanged while
  the species no longer appears as its exact synonym/identity equivalent.
- Test mapping direction and source-count scope explicitly; the native
  19,502-member species and single VC40 member are a concrete regression case.
- Run focused seeder tests, both exact record validators and
  `just verify-corpus` before merging a curation change. Full-corpus
  reproduction was skipped in this read-only review.
- Retry live GTDB access for release-specific classification confirmation.
  Do not transfer species-type BacDive/StrainInfo records or join bare VC40.
- Treat taxon-native genome presentation as separate model work, preserving
  explicit source identifiers and keeping sample/project entities distinct.

## Additional Notes

iModulonDB was not applicable: the YAML asserts no named gene, regulator,
pathway, stress-response mechanism or transcriptomic dataset. A literature
or search lead alone was not expanded into an unrelated functional review.

No paid research, source refresh, catalog rebuild, sequence download,
history event, GitHub mutation or review-status promotion was performed.
This report does not certify other records or the published site.
