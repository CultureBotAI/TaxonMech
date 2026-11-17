# YAML Record Review: Streptococcus constellatus subsp. pharyngis SK1060 = CCUG 46377

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptococcus_constellatus_subsp_pharyngis_sk1060_ccug_46377.yaml`
- Started UTC: 2026-10-06T13:25:59Z
- Finished UTC: 2026-10-06T13:36:49Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1035184`, rank STRAIN, domain BACTERIA, parent `NCBITaxon:184250`. The full 46,765-byte YAML was read, then checked byte-for-byte against the current file. It is EXACT-grounded and SEEDED, with genetic code 11, twelve lineage entries, four synonyms, one GTDB mapping/xref, one BacDive strain, seven source attestations and one seed event.

The listed strain is `kgmicrobe.strain:bacdive_14826`, designation MM9889a, with CCUG 46377, DSM 17475 and NCTC 13122. It carries thirteen assembly assertions representing seven accession strings, twelve other-genome assertions representing eight identifiers including ATB, and fifty-four related-record assertions representing forty-one identifiers. These are assertion/identifier counts, not independent biological genomes.

## Validation

- Passed: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptococcus_constellatus_subsp_pharyngis_sk1060_ccug_46377.yaml`; exit 0, no issues.
- Passed: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptococcus_constellatus_subsp_pharyngis_sk1060_ccug_46377.yaml --out /private/tmp/scsk1060-strict.tsv`; one file, zero ERROR rows. Read the resulting header-only TSV.
- Manual structured comparisons passed for the complete NCBI parent chain, label/rank/code, synonyms, unique PATHS/scope entries and seed-event wording. Exact multiset comparisons matched all thirteen assembly, eleven non-ATB genome and fifty-four related assertions to their raw/StrainInfo inventories, including nested StrainInfo evidence. This is not a substitute for corpus reproduction.
- The existing CAFI matcher accepts all three deposits, their source spellings and `CCUG:46377`. It correctly rejects bare SS1740, SK1060, FDAARGOS_1208 and 13-11-14 as cross-source deposit keys.
- Ran the installed claw runner: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. No S. constellatus dataset is listed; S. pneumoniae and S. pyogenes are different organisms. No search/summarize transfer was made.
- Not run: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, provenance, rendering, statistics and test-suite gates. This individual read-only review does not certify the corpus or publication products. No causal graph is present for the OAK product-label gate; no target-specific history artifact was found in the ignored-inclusive history search. No focused reference/history validator was invented.
- Live NCBI Taxonomy, Datasets, nucleotide metadata, StrainInfo API/DOI, BacDive, LPSN and collection pages were inspected. GTDB pages could not be read; GOLD's organism page returned HTTP 403. ENA analysis XML timed out twice, and its browser page and the SRA run page were inaccessible through the web reader. Those availability checks remain unresolved, not proof of invalid identifiers. IMG/BV-BRC identifiers were checked through complete pinned asserting-source rows, not live detail-page availability.

## Identity and Grounding

[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1035184) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035184) agree with the strain label, rank, parent and code. The root-first lineage agrees exactly with `data/raw/ncbitaxon_taxa.tsv:221909` and the live chain, with root included by Datasets. All three NCBI alternate names are true synonym/equivalent-name entries in `data/catalog/ncbi_names-0005.jsonl.gz:31349` and the following three rows. No exact target entry was found in merged-ID, dropped or type-material tables; the subspecies, rather than this strain taxid, owns the type-material rows.

[BacDive 14826](https://bacdive.dsmz.de/strain/14826), [CCUG 46377](https://www.ccug.se/strain?id=46377), [DSM 17475](https://www.dsmz.de/collection/catalogue/details/culture/DSM-17475), [StrainInfo SI-ID13146](https://api.straininfo.dsmz.de/v2/data/strain/max/13146) and [LPSN 781309](https://lpsn.dsmz.de/subspecies/streptococcus-constellatus-pharyngis) support MM9889a and the listed culture deposits. LPSN names these deposits as the type strain of subsp. pharyngis, not of all S. constellatus. The [1999 description](https://pubmed.ncbi.nlm.nih.gov/10555325/) explicitly identifies MM9889a/NCTC 13122 as that type.

The absent nomenclature/type flag is not treated as an assertion that this is a non-type strain. The current schema defines `is_type_strain` relative to an LPSN name of the record's taxon; the available LPSN entry denotes the parent subspecies and has no mapped NCBI ID in the imported table. Do not repair that limitation by making the subspecies name equivalent to its individual type-strain taxon.

## Evidence

**GTDB scope.** `data/raw/gtdb_species.tsv:168734` contains fifty-one genomes for the species cluster. All seventeen mapping rows for this GTDB ID were inspected; the target row at `data/raw/gtdb_mappings.tsv:1413` repeats that species total with closeMatch. The native `RS_GCF_000474135.1` row explicitly distinguishes strain taxid 1035184 from species taxid 76860 and classifies its genome in S. constellatus. These support species membership, not species/strain equivalence. Fifty-one is the pinned transformed cluster total, not a current or strain-specific genome census.

**Supported assembly chains.** Native BacDive 14826 retains source reference 66792 for unversioned GCA_000223295, GCA_000474135 and GCA_016889885 and its PATRIC/IMG assertions. The public BacDive page identifies 66792 as automated DiASPora annotation; it is source provenance, not a primary experimental publication.

GOLD's Go0048460 -> Gp0010324 -> Ga0009508 chain supplies unversioned GCA_000223295 and IMG 2512047071; Go0048460 -> Gp0048460 -> Ga0035252 supplies GCA_000474135.1 and IMG 2602041609. Both use the explicit CCUG 46377 deposit. GTDB, NCBI assembly and BV-BRC metadata independently support the latter assembly/sample chain. Related BioProjects and BioSamples retain their own types.

[NCBI Datasets assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000223295.2,GCA_000474135.1,GCF_000474135.1,GCA_008633025.1,GCA_016889885.1/dataset_report) confirms current GCA_000223295.2 and the GCA/GCF_000474135.1 pair. GCF_000223295.1 is suppressed; GCA_000223295.1 is historical in the pinned catalog. Do not append a version to either unversioned BacDive/GOLD assertion, or present the suppressed RefSeq as current. Bare SK1060 in GTDB/BV-BRC is not an eligible deposit join by itself.

**FDAARGOS and ATB.** The FDAARGOS_1208 BioSample SAMN16357350 explicitly gives DSM:17475. This supports BV-BRC 76860.29 and Go0594476 -> Gp0608421 -> Ga0521939 -> GCA_016889885.1 despite their broader species taxid. The non-genomic GOLD context Go0194163/Go0194166 also explicitly names DSM 17475/NCTC 13122.

The ATB assertion preserves both eligible BioSample evidence paths, SRR13181645, ERZ25832697, the source SeqKit sum and native download/archive URLs. The full native row and overlap row agree: assembly filter PASS, FASTA available, HQ/Sylph status SYLPH_RESULTS_FAIL. Non-HQ status alone is not an identity exclusion. The FASTA URL returned HTTP 200 to HEAD with a 628,263-byte content length; no genome was downloaded or sequence-equivalence claim made. The two genome crosslinks in `data/atb/genome_links.tsv:8917` and the next row are shares_biosample links only. SAMN00621704 is correctly excluded because its ATB assembly is unavailable/NOT_PROCESSED.

**Conflicting GOLD chain.** `data/gold/organisms.jsonl.gz:9068` names Go0010324 as S. constellatus constellatus 13-11-14 but supplies CCUG 46377. Its project Gp0496192 and analysis Ga0443358 consistently point to that same organism, GCA_008633025.1, IMG 2900306251, SAMD00149545 and PRJDB7095. Thus the extractor has not mixed project IDs; the problematic evidence is the organism-to-culture assertion itself.

The [primary BioSample](https://www.ncbi.nlm.nih.gov/biosample/SAMD00149545) identifies a clinical isolate collected on 2013-11-14 from pyothorax pus in Himeji, Japan. CCUG's own record documents its type-strain deposit in 2002 and an origin in a London throat specimen. Combined with the 1999 type description, these are incompatible source histories, not merely different taxonomic opinions. The GOLD-only association to CCUG 46377 is not defensible as an accepted strain-genome link.

**StrainInfo nucleotide evidence.** The live API agrees with the full pinned SI-ID13146 record and [version DOI](https://doi.org/10.60712/SI-ID13146.3). SI-DP331087, 49400 and 662019 are the three matched eligible deposits. Every imported nucleotide explicitly names SI-DP331087/CCUG 46377; LMG 19538's three sequences were correctly not transferred through group membership.

All fifteen imported accessions resolved in NCBI nucleotide metadata. Inspected accession versions, definitions, lengths, dates, source/gene/CDS/rRNA qualifiers and bibliography for each:
- AB199342 (ddl, 292 bp), AB199455 (gdh, 431 bp), AB199924 (rpoB, 517 bp), AB200049 (sodA, 390 bp).
- AB441089 (gyrB, 509 bp), AB441157 (rodA, 367 bp), DQ204524 (16S-23S spacer, 319 bp).
- JN787149 (16S, 1404 bp), JN787248 (tuf, 426 bp), JN787352 (sodA, 378 bp), JN787456 (rpoB, 516 bp), JN787560 (pyk, 492 bp), JN787664 (ppaC, 552 bp), JN787768 (map, 348 bp), JN787873 (pfl, 351 bp).

All currently resolve to version .1 and source taxid 1035184, with CCUG 46377/SK1060 strain qualifiers. The record correctly preserves unversioned source accessions and keeps these partial markers outside genome counts. PubMed bibliography and full abstracts for [Hoshino 2005](https://pubmed.ncbi.nlm.nih.gov/16333101/), [Tung 2006](https://pubmed.ncbi.nlm.nih.gov/17065265/) and [Jensen 2013](https://pubmed.ncbi.nlm.nih.gov/23223817/) were inspected as sequence context, not as proof that the reference strain was a clinical isolate from each study. No mechanism, expression-module or phenotype claim is inferred.

**Attestations.** The exact inventory rows support NCBI 1 NAME, BacDive 1 STRAIN, MediaDive 2 MEDIUM, GOLD 1 ORGANISM, Madin 1 TRAIT_ASSERTION and BactoTraits 2 TRAIT_ASSERTION. GTDB 51 GENOME retains its species scope problem described above. Counts are not summed. MediaDive's two medium IDs are 693 and 92, independently displayed by DSMZ; neither count asserts a novel strain phenotype. The seven-source seed event matches `curation/seed_scope.tsv:7211`.

## Completeness

Ignored-inclusive, compressed-content searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. They used the taxid, SK1060, all three deposits, MM9889a, then the observed assembly/genome, sample, GOLD, StrainInfo and nucleotide identifiers. All 134 initial candidate rows and 95 new rows from the 200-row expansion were read in full with reconstruction-checked common-field factoring. Candidate-address reconciliation found no missed/extra rows. All five SOURCE.json documents were searched structurally, separately from the large content scan. These are bounded source-inventory searches, not claims about all external databases.

A further NCBI candidate is a consequential omission: [GCA_053207125.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_053207125.1/dataset_report), strain SS1740, BioSample SAMN52092857, explicitly lists culture_collection CCUG:46377 and biomaterial provider CCUG. It is a current 11-contig, 1,952,328-bp assembly, released 2025-10-25, with explicit paired GCF_053207125.1 and project PRJNA1273177. Both assembly rows already exist in the pinned native catalog at `data/catalog/ncbi_genbank-0049.jsonl.gz:7329` and `data/catalog/ncbi_refseq-0008.jsonl.gz:3491`.

Ignored-inclusive searches for both accessions and then SS1740/SAMN52092857/JBRUIB returned only those two native rows in the checked roots. Neither assembly is present in the target or its imported strain inventories. The missing bridge is the primary BioSample culture field, not a guessed alias or ANI match. Capturing that bridge would also provide explicit versioned support for other assemblies whose summary strain field is a bare laboratory name; no broad alias join is justified.

Empty optional definition, causal graph and mechanistic evidence slots are appropriate for this identity record. Native cultureless MM9889a GOLD rows do not independently justify extra genome links. LMG-specific StrainInfo sequences and unavailable ATB data are not omissions under current import rules.

## Findings

Counts: 0 blocker, 3 major, 0 minor.

1. **Major: an individual strain is made equivalent to a GTDB species cluster.** The GTDB exact synonym and equivalent xref conflate S. constellatus with SK1060/CCUG 46377. The source closeMatch and fifty-one-genome attestation are also over-scoped at this rank. Maintained owners: kg-microbe's transformed GTDB mapping, `src/taxonmech/extract.py:501` for imported mapping/count handling, and `src/taxonmech/seed.py:449` for rank-blind promotion to synonym/xref. The correctly evidenced GTDB genome link must remain separate.

2. **Major: GOLD supplies a contradicted culture-to-genome association.** Go0010324's CCUG 46377 field imports GCA_008633025.1/IMG 2900306251 and five related assertions from the distinct 13-11-14 clinical isolate. The complete source chain is mechanically consistent but contradicted by collection and sample histories. Maintained owners: GOLD's organism metadata; locally, `src/taxonmech/gold_genomes.py` and the source-capture/extraction path need a maintained, evidence-backed correction or exclusion before regeneration. Do not erase the native source assertion or reject every differing taxid.

3. **Major: a directly evidenced CCUG 46377 assembly pair is missing.** GCA/GCF_053207125.1 is present in the native catalog and its primary BioSample names the existing deposit, but it is absent from the record's assembly associations. `src/taxonmech/ncbi_assemblies.py:90` only matches summary infraspecific_name; SS1740 therefore cannot join. Maintained owners: the NCBI source capture/configuration beginning with `conf/ncbi_assemblies.yaml`, plus `src/taxonmech/ncbi_assemblies.py` and its extraction integration. Preserve a pinned BioSample-to-assembly-to-deposit chain rather than widening bare-name matching.

No blocker was found in the record's own NCBI identity or YAML structure. The unresolved live ENA/GTDB/GOLD access checks do not independently establish additional data errors.

## Recommended Edits

1. Correct or explicitly quarantine Go0010324's CCUG assertion in maintained source handling. Remove its unsupported derived assembly, IMG, organism, project, analysis, BioSample and BioProject associations from this strain on regeneration; retain the raw conflict for audit. Keep the supported Go0048460 and Go0594476 chains.
2. Make GTDB identity promotion rank-aware in the maintained seeder and correct the upstream mapping semantics. Do not emit species exact synonyms/equivalent xrefs for strain concepts. Preserve explicit species classification and its cluster-scoped count without presenting it as a strain census.
3. Add pinned primary BioSample deposit evidence to NCBI capture/import and attach the explicitly supported GCA/GCF_053207125.1 pair to BacDive 14826. Retain SAMN52092857, source field/value, original assembly versions and accession-specific provenance. Do not rewrite existing unversioned assertions.
4. Regenerate only through the documented extractor/overlay/seed workflow after a separately authorized curation change. Never manually edit this YAML, its generated page or an earlier report.

## Follow-up Checks

- Add regression cases in `tests/test_gold_genomes.py` for the documented Go0010324 contradiction while preserving valid cross-rank FDAARGOS/DSM links and internally consistent Go0048460 chains.
- Add rank-scope regressions in `tests/test_seed.py` and mapping extraction coverage: no GTDB species equivalence for this strain, correct classifier genome link retained, no species-total count relabeled as strain-specific.
- Extend the primary NCBI cases in `tests/test_source_expansion.py` with SS1740/SAMN52092857/CCUG:46377, explicit pairing and negative controls for bare aliases, mismatched samples and historical versions.
- Run those focused test files, then the documented extraction dry run and authorized refresh. Rebuild dependent ATB/StrainInfo inventories when their inputs change. Use `just seed-canary NCBITaxon:1035184` only in that later write-authorized task; inspect its complete output.
- Re-run single-record schema/strict validation and manual source-chain checks, then `just verify-corpus`, history validation as applicable and `just qc` for release-wide proof. Refresh pages/statistics through their generators, not hand edits.
- Recheck live ENA ERZ25832697/SRR13181645 and inaccessible source detail pages before representing them as currently reachable. The reviewed snapshot remains evidence of the recorded assertions.

## Additional Notes

The initial search also found unrelated numeric matches: Collinsella aerofaciens SAMN41035184/GCA_040926145.1, Campylobacter GCA_010351845.1, and Mycobacterium tuberculosis run ERR1035184/SAMEA3558717/ATB ERZ3502386. The expansion matched BacDive IDs 148260-148269 by prefix; their complete rows were disambiguated and not transferred.

BacDive 142309/CCUG 11578 contains a conflicting JN787149 description among many SK1320-labelled marker rows. Its own strain identity is different. The target's exact StrainInfo deposit assertion and direct NCBI record support CCUG 46377; that collateral BacDive text does not override them.

StrainInfo's NCTC deposit currently has typeStrain false while the group, CCUG/DSM deposits and primary nomenclatural sources identify the parent subspecies' type strain. This source-local discrepancy is preserved as context, not used to change lineage or transfer identifiers.

No source data, taxon YAML, code, page, scope, curation event, history artifact or prior report was changed. No review-status promotion, paid research or external mutation was performed. Eukaryota was not reopened.

