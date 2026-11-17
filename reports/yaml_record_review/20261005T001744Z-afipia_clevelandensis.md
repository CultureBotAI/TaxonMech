# YAML Record Review: Afipia clevelandensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/afipia_clevelandensis.yaml`
- Started UTC: 2026-10-05T00:09:27Z
- Finished UTC: 2026-10-05T00:17:44Z
- Verdict: pass

## Target

Read the entire 573-line generated TaxonRecord for NCBITaxon:1034, Afipia clevelandensis, SPECIES, BACTERIA. The target is the species, not its descendant strain NCBITaxon:883079, Afipia clevelandensis ATCC 49720. Grounding is EXACT, mapping status is SEEDED, and the single inline event is the 2026-09-13 source-seeding event. Review only: no record, maintained input, status or history changes.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/afipia_clevelandensis.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/afipia_clevelandensis.yaml --out /private/tmp/afipia-clevelandensis-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: structured comparison of the complete NCBI ancestor chain, target backbone row, source inventories, PATHS entry, seed-scope row and inline event. This is a bounded source check, not corpus reproduction.
- PASS: structured multiset equality of all 8 assembly, 5 genome-record and 23 related-record assertions against the raw and StrainInfo crosswalks, including decoded nested StrainInfo evidence. No missing or extra assertions.
- PASS: whole culture-identifier checks using `culture_curie_key` and `normalize_culture_identifier` from `src/taxonmech/genome_sources.py`; all four inventoried deposits and every explicit source join match.
- PASS: descendant-inclusive backbone and BacDive scans establish one child, no further descendants, and one eligible BacDive strain.
- SKIPPED: `just verify-corpus`; the documented command verifies the full corpus and has no target-record mode. Its diagnostic limit is not a scope limit.
- NOT APPLICABLE: `just validate-products`, because this record has no causal-graph nodes or corresponding product labels.
- SKIPPED: `just validate-history`; target identifier, label and slug searches of `history/`, including ignored and hidden files, found no external target history record. The inline seed event was checked directly.
- No separate documented single-record term/reference validator was substituted. External identifiers and local source references were checked individually below.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:804` agrees on the identifier, label, species rank, parent NCBITaxon:1033 and genetic code 11. All nine root-first ancestors agree by identifier, label and rank, ending at Afipia. Live NCBI Taxonomy EFetch and Datasets responses for 1034 and 883079 independently support that species/strain distinction and lineage. The authority-bearing NCBI name is correctly a RELATED_SYNONYM, not an exact identity alias. The type-material inventory has 15 target rows; target merged/dropped-row checks were negative.

LPSN 772930 identifies this species and supports its legitimate, validly published, correct-name status, the authority and the five nomenclatural type-deposit identifiers. The source retains the 1992 validation authority and 2020 emendation separately from the 1991 effective description. The YAML's LPSN mapping remains `skos:closeMatch`. [LPSN species entry](https://lpsn.dsmz.de/species/afipia-clevelandensis).

The GTDB species xref comes from the LPSN inventory's named-species association, `data/raw/lpsn_names.tsv:15099`. There is no direct GTDB mapping row for NCBITaxon:1034 and no invented GTDB genome-count attestation in this species record. The type-strain genome is the GTDB representative; a second cluster member, SG-6C, has a different NCBI taxon and no matching inventoried deposit. Neither its assembly nor its name is transferred onto this strain.

## Evidence

- Nomenclature: the complete LPSN row matches all represented authority, status, type-deposit, citation, sequence and xref fields. The primary publisher identifies DOI:10.1099/00207713-42-2-327 as Validation List No. 41, volume 42(2), pages 327-328, April 1992, citing the Brenner description. The list's full-text loader and preview were unavailable; its individual row was not independently read. [Publisher record](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-42-2-327).
- Original description: PMID:1774249 and DOI:10.1128/jcm.29.11.2450-2460.1991 resolve to the same 1991 Brenner et al. article proposing the named species. PubMed XML and the PMC article metadata/abstract were inspected. The scanned methods and tables were not comprehensively reviewed; no phenotype claim is inferred from them. [Original publication](https://pmc.ncbi.nlm.nih.gov/articles/PMC270354/).
- Emendation: the Europe PMC full-text XML for PMID:32373076, DOI:10.3389/fmicb.2020.00468, includes a specific Afipia clevelandensis emended-description section. It retains the earlier description while adding type-strain genomic measurements, supporting the 2020 authority suffix. Only the relevant section and article metadata were inspected, not every species treatment. [Primary emendation XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7179689/fullTextXML).
- Type-strain identity: `data/raw/bacdive_strains.tsv:1773` and the complete retained native record, `data/bacdive/records.jsonl.gz:1772`, agree on BacDive 1777, its designation, four culture deposits and strain classification 883079. The live BacDive entry confirms the type flag and reference 66792 for the unversioned assembly, IMG and BV-BRC links. That reference is an automatically generated source association, not an experimental study proving genomic equivalence. [BacDive 1777](https://bacdive.dsmz.de/strain/1777).
- Deposit authorities independently agree: CIP 103516 is a type deposit associated with ATCC 49720 and DSM 7315; NCTC 12721 lists the same type strain and additional collection designations. The NCTC page's older family placement is not used to replace the current NCBI backbone. [CIP catalogue](https://catalogue-crbip.pasteur.fr/fiche_catalogue.xhtml?crbip=CIP+103516), [NCTC catalogue](https://www.culturecollections.org.uk/nop/product/afipia-clevelandensis).
- Marker accession: live GenBank XML resolves the supplied unversioned M69186 to M69186.1, a 1425-base partial 16S record with strain B-91-007353, taxon 883079 and explicit type-material annotation. Its references include PMID:1774249. The unversioned source accession in the YAML should remain unversioned. [GenBank M69186.1](https://www.ncbi.nlm.nih.gov/nuccore/M69186.1).
- Assembly identity: complete current GenBank/RefSeq native rows and live NCBI Datasets/Assembly metadata support GCA_000336555.1 and GCF_000336555.1 as a current, identical pair for ATCC 49720, with BioSample SAMN02463899. They have scaffold-level status, one scaffold and 19 contigs. Their source-specific BioProjects, PRJNA52157 and PRJNA224116, remain separate assertions. Suppressed historical GCA/GCF_000314695.1 entries share the sample but are not additional current assemblies. [NCBI assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000336555.1/).
- Primary genome-source chains: native BV-BRC 883079.3, GTDB RS_GCF_000336555.1, and GOLD Go0008054 -> Gp0008054 -> Ga0016215 support the explicit ATCC deposit joins, assembly, sample and project IDs. GOLD's IMG field supports img.taxon:2537561906. Ga0016215 has no direct organism field; the retained sequencing-project chain supplies it. Go0623656 separately supports the DSM 7315 organism associations, not another genome. Native source locators are listed below.
- StrainInfo: complete pinned record 12657 and the live official maximum-detail API agree on version DOI:10.60712/SI-ID12657.3, published status, BacDive cross-reference, nonerroneous deposit relationships and the relevant available deposits. Assembly GCA_000336555 explicitly names SI-DP 47716, ATCC 49720. Each of the four eligible deposits has its own SI-DP and SI-ID association; these are source assertions, not extra biological strains. [Official StrainInfo API](https://api.straininfo.dsmz.de/v2/data/strain/max/12657).
- Attestation units are preserved: NCBI 1 NAME, LPSN 1 NAME, BacDive 1 STRAIN gathered from the descendant, GOLD 6 directly filed ORGANISM records, and Madin 3 directly filed TRAIT_ASSERTION records. All six native direct GOLD objects were inspected; several are different source records for strain aliases, not evidence for six distinct strains. The Madin inventory count is not itself verification of individual phenotypes.

## Completeness

The sole BacDive strain is fully represented, not a capped listing. Eight assembly assertions do not mean eight distinct assemblies; five genome-record assertions do not mean five independently sequenced genomes. Repeated database identifiers preserve different source paths. GOLD organism/project/analysis and StrainInfo deposit/strain identifiers correctly remain related records.

LMG 18883 and NCTC 12721 appear in other authoritative deposit lists but not the pinned BacDive four-deposit inventory. NCTC is correctly retained in nomenclature without being fabricated as a BacDive deposit. StrainInfo's AJ534610 rRNA-operon sequence explicitly names only LMG SI-DP 47715; it is correctly not transferred to the four eligible deposits by SI-ID grouping.

The ignored-inclusive, compressed-file-aware identifier/name/slug/deposit search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All 97 matching row contexts were inspected, then native evidence objects were read in full. A second search for exact BioSamples, assembly and genome IDs and the GOLD chain returned 38 row contexts.

The ATB catalog's similarly named entry is for SAMN00630398, not the supported sample SAMN02463899, and carries META_FAIL. Name resemblance cannot establish the required whole-BioSample join, and META_FAIL independently makes it ineligible under the documented filter. Both ATB link tables contain zero rows for this strain. No missing eligible ATB association was established by these bounded searches.

There are no direct MediaDive or BactoTraits inventory rows for species 1034. Descendant source coverage is not automatically a species-level attestation. SeqCode's retained name 1740 is an additional identity lead, not a missing required curated overlay. No causal graph, functional-gene or transcriptomic assertion requires invention; iModulonDB is not applicable.

The PATHS entry at line 13872 and seed-scope row at line 23282 agree with the target. The seed-scope rationale counts four directly attesting sources before descendant BacDive aggregation; the resulting five-source inline event is consistent with that source chain. No external target history or previous target review was found in ignored-inclusive searches.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The represented identities, scoped source assertions, count units and deposit-specific joins are supported within the checked evidence. Access limitations below do not establish a defect in the record.

## Recommended Edits

None required. Do not patch this generated YAML or promote its status as a consequence of this read-only review.

Future source corrections, if established, belong to the maintained inventories under `data/raw/`, `data/straininfo/` or `data/atb/`, with the applicable source importer or `src/taxonmech/genome_sources.py` / StrainInfo matching implementation owning transform changes. Regenerate through `scripts/seed_from_sources.py` only in a separately authorized curation task.

## Follow-up Checks

- After any later curation change, rerun the two focused validators, the complete 36-assertion comparison and the deposit-specific source-chain checks.
- Run documented full-corpus `just verify-corpus` separately before claiming corpus-wide reproducibility; it was not run here.
- Live GTDB genome/tree pages were unavailable through the web tool. Recheck them when accessible; this review used the retained complete metadata objects and mapped inventories, not search snippets.
- The validation-list individual row and the original description's full scanned text remain uninspected. Inspect them directly if a nomenclatural dispute or additional phenotype claim makes that necessary.
- Live NCBI assembly metadata reports CheckM completeness 67.35% and contamination 18.4%. These are relevant caveats for downstream genomic interpretation, not evidence that the recorded deposit/assembly association is wrong. The YAML makes no high-quality-genome claim. NCBI's type-strain ANI comment also must not be read as a failed identity assignment.

## Additional Notes

Native and crosswalk locators inspected:

- `data/catalog/ncbi_genbank-0000.jsonl.gz:8801`, `data/catalog/ncbi_refseq-0000.jsonl.gz:7578`; suppressed historical counterparts at lines 2992 and 2361.
- `data/catalog/gtdb_genomes-0016.jsonl.gz:14105` for the representative, and `data/catalog/gtdb_genomes-0014.jsonl.gz:21410` for SG-6C. GTDB uses Rhizobiales/Xanthobacteraceae while the NCBI backbone uses Hyphomicrobiales/Nitrobacteraceae; these classifications are not silently conflated.
- `data/bvbrc/bvbrc-0027.jsonl.gz:45424`; `data/gold/organisms.jsonl.gz:7196`, direct species objects at lines 454267-454272; `data/gold/projects.jsonl.gz:7144`; `data/gold/analyses.jsonl.gz:9744`.
- `data/raw/strain_assemblies.tsv:101193` through 101199, `data/raw/strain_genome_records.tsv:81457` through 81461, `data/raw/strain_related_records.tsv:293365` through 293379.
- `data/straininfo/records.jsonl.gz:12657`, `data/straininfo/assemblies.tsv:7231`, `data/straininfo/related_records.tsv.gz:184709` through 184716.
- `data/raw/gold_organisms.tsv:461`, `data/raw/madin_taxa.tsv:644`, `data/catalog/allthebacteria.tsv.xz:1004350`, `data/seqcode/names.jsonl.gz:1504`.

Some initial DOI/StrainInfo page routes and the original article's Europe PMC full-text endpoint failed. The official StrainInfo API succeeded and verified the version DOI and explicit sequence-deposit relationship; PubMed and the PMC article page supplied the original-description citation check. The 2020 emendation was verified through Europe PMC XML after publisher/PMC-page access failed. No unavailable endpoint is presented as an inspected source.

This review is limited to one resolved species record. It is not a review of the descendant YAML, an audit of every genome base or annotation, verification of all source phenotypes, or a certification of the entire corpus. Only this new report was written.

