# YAML Record Review: Paenibacillus polymyxa ATCC 842

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_polymyxa_atcc_842.yaml`
- Started UTC: 2026-10-08T00:29:01Z
- Finished UTC: 2026-10-08T00:49:51Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1036171`, labelled `Paenibacillus polymyxa ATCC 842`, rank `STRAIN`, domain `BACTERIA`. The entire 4,293-line YAML was read before judgment. Its parent is the species `NCBITaxon:1406`; these are not interchangeable targets. The species record encountered during resolution aggregates this strain and was not separately reviewed.

The record is `EXACT`/`SEEDED`, with one BacDive strain, 27 deposit identifiers, 39 assembly assertions, 31 genome-record assertions, 220 related-record assertions, seven source attestations and one seed event. Repeated identifiers represent separately attributed paths, not necessarily duplicate assertions. This review makes no curation or lifecycle change.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/paenibacillus_polymyxa_atcc_842.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/paenibacillus_polymyxa_atcc_842.yaml --out /private/tmp/pp842-strict.tsv` | Passed; one file, zero errors; output TSV contained only its header. |
| Structured comparison with pinned backbone, source inventories, scope and path index | ID, label, rank, parent, code, all ten ancestors, both NCBI synonyms, counts and source rows agree. |
| Read-only comparison of every assembly, genome and related-record field | Passed: raw inventories supply 34/30/122 assertions, StrainInfo adds 5/0/98, and the maintained ATB converter supplies 0/1/0, yielding exactly 39/31/220. StrainInfo rows were checked through its maintained link validator. |
| Current NCBI Taxonomy EFetch and Datasets | Identity, lineage and code agree with the pinned record. |
| Current NCBI assembly and nucleotide metadata | Five assembly accessions and all 46 cited nucleotide accessions resolved; relevant identity, deposit, sample and project metadata inspected. |
| Current StrainInfo and DataCite | Every field in the pinned native StrainInfo projection agrees with the live object; the cited versioned DOI is registered and findable. |

These bounded comparisons are not a full source replay or corpus reproduction test. Not run: full-corpus `just verify-corpus`, QC, product-label checks, rendering checks, documentation checks, or complete source-provenance gates. The inline seed event was checked structurally; no target-specific external history artifact was found in the bounded ignored-inclusive search, so no external history file was submitted to its validator. No standalone focused ontology/history gate was invented.

The live GTDB taxon and genome pages were inaccessible through the web tool. GTDB conclusions below distinguish the inspected pinned source data from an unverified current live release. Genome FASTA archives were not downloaded, reassembled or compared by sequence.

## Identity and Grounding

The primary NCBI identity is sound. The two NCBI exact synonyms retain the ATCC 842 designation; the ten root-first ancestors terminate at species 1406, and genetic code 11 is consistent. Exact-key scans found no merged or dropped status for this ID. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036171)

The GTDB portion has a different scope. `GTDB:s__Paenibacillus_polymyxa` denotes a species, whereas the reviewed NCBI record denotes a strain. The pinned `gtdb_mappings.tsv:1451` supplies `skos:closeMatch` and 90 genomes. The generator promotes that mapping to an exact species-name synonym and an identity-oriented xref without checking the target rank. Faithful copying does not establish strain/species equivalence. The pinned GTDB genome catalog identifies DSM 36 as the representative of this species and also contains the separately accessioned ATCC 842 assemblies. The count is the upstream species genome count, not 90 independently supported ATCC 842 genomes.

LPSN name 779092 belongs to the parent species, not to a separately validly published strain name. Its type designations include ATCC 842 and DSM 36. This supports a bounded type-strain flag, not copying all species nomenclature into this strain record. [LPSN species entry](https://lpsn.dsmz.de/species/paenibacillus-polymyxa)

## Evidence

The native BacDive 11487 object and live page support the 27 listed deposit identifiers and five explicit genome cross-link groups. The designation field is empty in the inventory; the record does not invent one. BacDive identifies the culture as a type strain. [BacDive 11487](https://bacdive.dsmz.de/strain/11487)

Native GTDB, NCBI, BV-BRC and GOLD objects were inspected for their own deposit fields and explicit project relationships. The five GOLD analysis-project chains resolve through their own sequencing projects and organisms. The 26 linked GOLD organism IDs have eligible deposit evidence; the BUCSAV-only candidate lacks an eligible normalized join and is correctly excluded. This does not make all species-1406 organisms members of the strain.

The current NCBI assembly metadata preserves these associations:

| Assembly | Strain or isolate field | BioSample | BioProject |
| --- | --- | --- | --- |
| [GCA_000217775.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000217775.1/) | ATCC 842 | SAMN02470189 | PRJNA67165 |
| [GCA_015710975.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_015710975.1/) | DSM 36 | SAMN14247784 | PRJNA609344 |
| [GCA_022811565.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_022811565.1/) | ATCC 842 | SAMN07972645 | PRJNA416965 |
| [GCA_900454525.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_900454525.1/) | NCTC10343 | SAMEA4076715 | PRJEB6403 |
| [GCA_903797665.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_903797665.1/) | isolate 2 | SAMEA6854744 | PRJEB38476 |

All five are current and have RefSeq partners. The last two lack eligible direct strain identifiers in the pinned NCBI/GTDB/BV-BRC join fields; explicit BacDive, GOLD and StrainInfo paths still support their represented links. Missing direct-source assertions should not be filled by matching a taxon label or silently normalizing an ineligible field. Unversioned source accessions remain unversioned rather than acquiring an invented version.

StrainInfo 92295 supplies 26 eligible deposit matches, five assembly links and 46 nucleotide links with the same deposit ID on each sequence and its matching deposit. Its other two sequences, AB767251 and KR109256, belong to NCIM 2539, outside this record's BacDive deposit list, and are correctly excluded. The 40-deposit native object is not permission to copy every sequence onto every deposit. The DOI identifies version 3 of this strain resource, not a research paper. [StrainInfo API](https://api.straininfo.dsmz.de/v2/data/strain/max/92295), [versioned DOI](https://doi.org/10.60712/SI-ID92295.3), [DataCite registration](https://api.datacite.org/dois/10.60712/SI-ID92295.3)

All 46 nucleotide accessions were checked through NCBI EFetch, including their source qualifiers and non-sequence feature metadata. Their deposit grouping is consistent: ATCC 842 has AJ223997, D11421, U36234 and X57094; CECT 155 has U89716; IAM 13419 has AB006947, AB042063, AB464839, D16276 and OK001701; NBRC 15309 has AB271758 and OK001703; DSM 36 has AJ320493, ON878182, X57308 and OK001709; NCDO 1774 has X60632; KCTC 3627 has AY359636, HE972654 and HE981766 through HE981792. The latter range represents 27 separately accessioned 16S clones, not 27 different strains. Example authority records: [AJ223997](https://www.ncbi.nlm.nih.gov/nuccore/AJ223997), [HE981766](https://www.ncbi.nlm.nih.gov/nuccore/HE981766), [U89716](https://www.ncbi.nlm.nih.gov/nuccore/U89716), [X57094](https://www.ncbi.nlm.nih.gov/nuccore/X57094).

Gene names in these accession descriptions are metadata, not additional mechanistic assertions by the YAML. No nitrogen-fixation, enzyme-activity, host, habitat or resistance phenotype is inferred from them. In particular, ON878182's submitted hand/host metadata is not generalized to the culture's original isolation source. [ON878182](https://www.ncbi.nlm.nih.gov/nuccore/ON878182)

ATB's 202505 record matches the pinned catalog entry for SAMN02470189, including run, analysis, checksum, quality fields and download locations. Its eight source-to-strain evidence paths and five genome relationships retain `shares_biosample`, not genome identity. Live ENA confirms SRR6439295 belongs to SAMN02470189/PRJNA67165, and ERZ4057800 references that run and sample under its own reassembly study PRJEB45982. These distinct studies are not conflated. [ENA run](https://www.ebi.ac.uk/ena/browser/view/SRR6439295), [ENA analysis metadata](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ4057800)

The seven attestations match their inventories: NCBI 1 NAME, GTDB 90 GENOME, BacDive 1 STRAIN, MediaDive 2 MEDIUM, GOLD 1 ORGANISM, Madin 4 TRAIT_ASSERTION and BactoTraits 1 TRAIT_ASSERTION. Counts are not summed across units. They are source-coverage statements, not evidence that every catalog property applies to every genome. The GTDB scope caveat remains the major finding.

## Completeness

The missing type-strain flag is the consequential bounded gap described below. Empty optional discussion, evidence and causal-graph slots do not require invented biology. Absence of a strain-level LPSN nomenclature entry is appropriate because the available name maps to the parent species. The single BacDive entry is not truncated by the listing cap. Its absent medium count follows inventory zero and does not negate the separate two-medium MediaDive attestation.

Ignored-inclusive searches used the ID, full label, slug, deposit variants, BacDive/StrainInfo IDs and cited assembly/nucleotide accessions across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`; compressed inputs were included. Record/report resolution also included `data/taxa` and `reports`. These bounded searches found no prior report or separate target history artifact. They do not claim that no further evidence exists on the internet or in every ignored directory on disk.

The 510 candidate addresses included unrelated BacDive ID prefixes, StrainInfo DOI-number collisions, ATB checksum substrings and an unrelated genome whose length happened to equal this taxon ID. Native candidate objects were inspected and those false matches were not joined. Reading such source candidates did not constitute additional taxon reviews; Eukaryota records were left untouched.

## Findings

Counts: 0 blocker, 1 major, 1 minor.

1. **Major: a GTDB species is promoted to an exact synonym of a strain.** The mapping predicate at YAML line 43 and synonym at line 46 are source-attributed but biologically over-scoped. `src/taxonmech/seed.py:451` treats any `skos:closeMatch` as identity, and line 468 creates an `EXACT_SYNONYM` from it. The paired xref and GTDB attestation inherit the same ambiguity. The record's primary NCBI identity remains correct, so this is not a wrong-target blocker. Maintained owner: `src/taxonmech/seed.py`, with upstream mapping semantics reviewed through `src/taxonmech/extract.py:501` and the kg-microbe GTDB transform identified by `conf/sources.yaml`. The extracted mapping TSV and generated YAML are not the authoritative place to hand-patch a fix.

2. **Minor: the supported type-strain flag is omitted.** The BacDive entry starting at YAML line 61 lacks `is_type_strain`, despite matching ATCC 842/DSM 36 designations in LPSN 779092 and the native BacDive type assertion. The raw BacDive row already provides that LPSN ID. `src/taxonmech/seed.py:390` collects type designations only for LPSN names mapped to the exact record ID; those names map to species 1406, so the later intersection at line 514 receives an empty set for strain 1036171. This is optional-field incompleteness, not an asserted false value. Maintained owner: the type-designation resolution in `src/taxonmech/seed.py`, using the existing exact deposit and LPSN provenance rather than indiscriminate inheritance from an ancestor.

## Recommended Edits

1. In `src/taxonmech/seed.py`, make GTDB identity promotion rank-aware. Preserve provenance for species membership without emitting a species name as an exact strain synonym or an unqualified identity xref. Review the mapping and attestation representation together. Do not simply replace `closeMatch` with `broadMatch`: this repository currently uses the latter as a particular upstream pooling signal. A changed predicate requires an explicit, tested semantic contract in the maintained extraction/mapping path.
2. Resolve type status using the strain row's verified LPSN name/deposit relationship, with compatible species ancestry and exact culture identifiers. Mark only this supported BacDive strain entry as type material. Keep species nomenclature at species scope, and do not turn every strain below a type-bearing species into a type strain.
3. Add focused fixtures in `tests/test_seed.py` for species-to-strain GTDB mappings and parent-species LPSN type designations. Preserve the supported source-specific genome/deposit paths and versionless accessions. No curation, source refresh or regeneration was performed here.

## Follow-up Checks

After an authorized maintained-source change, run the focused seed tests and a dry-run seed. Use the documented `just seed-canary NCBITaxon:1036171` workflow to regenerate and validate this one record; inspect the biological diff, then rerun both focused validators above. Explicitly assert that the species label is no longer an exact strain synonym, the mapping and attestation remain honestly scoped, and the type flag has an auditable deposit/LPSN basis.

Because the proposed change affects shared generation, also test an ordinary species identity mapping, a pooled mapping, a non-type strain and a strain with conflicting or missing deposit evidence. Before publishing regenerated corpus/products, run the documented corpus, QC, product, rendering, documentation and provenance gates. Recheck live GTDB when accessible; do not recalculate a historical inventory count from an unrelated current release.

## Additional Notes

StrainInfo marks IAM 13419 as non-type in its deposit object, whereas the matching NCBI nucleotide entries identify type material. This source discrepancy is preserved as a qualification; it does not erase the direct ATCC 842/DSM 36 evidence, and no per-deposit type assertion is invented in the YAML. Other extra StrainInfo deposits also have differing flags and were not transferred wholesale.

iModulonDB was not applicable to this identity/linkage verdict: the named genes occur in sequence descriptions, not asserted expression modules, pathways or phenotypes. Structured NCBI/StrainInfo metadata was used first; no absence from an expression database was treated as negative biological evidence. Papers listed only in upstream metadata were not promoted to YAML claims or treated as independently reviewed experimental support.

The seed event remains `2026-09-13T17:54:04Z`; scope admission remains `2026-09-12`. No review status, history event, inventory, generated page, GitHub object or branch/worktree was changed. Only this new report was added.

Reviewed HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target retained SHA256 `b3d0b2a0d685a2cc2633c4b433f61bf85f172bfba67887b6983dd5d849e56420` before report creation.
