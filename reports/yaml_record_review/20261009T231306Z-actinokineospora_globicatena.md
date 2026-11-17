# YAML Record Review: Actinokineospora globicatena

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/actinokineospora_globicatena.yaml`
- Started UTC: 2026-10-09T23:07:41Z
- Finished UTC: 2026-10-09T23:13:06Z
- Verdict: pass

## Target

Entire 1,806-line generated `TaxonRecord` read. `NCBITaxon:103729` denotes Actinokineospora globicatena, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:39845`, code 11, grounding `EXACT`, status `SEEDED`. All nine ancestors, nomenclature, GTDB mapping, authority synonym, xrefs, two BacDive strains, eight attestations and complete seed event were inspected. The two strain entries contain 29 assembly assertions, 17 genome-record assertions and 92 related-record assertions. These 138 source/field-specific assertions are not 138 independent genomes or cultures.

HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; YAML SHA-256 `0f38ba42b5e67b0db0da411cc579aa33550ee91af944a02c83ba6c00a5790109`. Ignored-inclusive filename resolution found exactly one target and no prior report. Current guidance/checklist, validator commands and relevant source-eligibility rules were inspected; tracked guidance and implementation remained unchanged from their preceding complete reads.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/actinokineospora_globicatena.yaml`: passed.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/actinokineospora_globicatena.yaml --out /private/tmp/taxonmech-actinokineospora-globicatena-20261009-validation.tsv --workers 1`: one file, zero errors; header-only TSV read.
- `uv run --offline python scripts/validate_history.py history`: 17 records valid, zero invalid links.
- Complete own-ID source, nine-ancestor, scope, slug and type/status comparisons passed. Full-field own-link comparisons found exactly 19/10/66 assembly/genome/related assertions for BacDive 13200 and 10/7/26 for BacDive 13201, with no missing or extra assertion. Whole-deposit normalization agreed. These are bounded comparisons, not full-corpus reproduction or a substitute for independent native-source inspection.
- Public NCBI taxonomy, six focused assembly responses, marker metadata, Crossref, focused DataCite metadata and PubMed bibliography/abstract reads succeeded. LPSN, BacDive and the cited publisher pages were inspected within the limits below. Two GTDB genome page opens and both StrainInfo browser opens failed; native catalog evidence and successful authority APIs independently support the relevant claims.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18555`, native scientific/authority names at `data/catalog/ncbi_names-0000.jsonl.gz:38593` and the following row, `data/taxa/PATHS.tsv:15254`, scope `curation/seed_scope.tsv:1219` and legacy page mapping row 915 agree. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103729&retmode=xml) independently confirms label, species rank, parent, code and authority. [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103729) confirms all nine ancestor IDs including root and reports five assemblies.

The complete root-first chain matches the pinned backbone in labels and ranks: root; cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; Pseudonocardiales; Pseudonocardiaceae; Actinokineospora. Complete own-ID scans found no child, merged-ID or dropped-ID row. Seventeen own type-material rows beginning at `data/raw/ncbi_type_material.tsv:1997` were read, including VKM formatting variants and YU6-1. A repeated equivalent type designation in live NCBI is not another biological strain.

`data/raw/lpsn_names.tsv:14917` supports `lpsn:772681`, the combined Tamura et al. 1995 emend. Nouioui et al. 2018 authority, legitimate/valid/correct-name flags, five type-designation CURIEs, two publications and AF114798. The [LPSN page](https://lpsn.dsmz.de/species/actinokineospora-globicatena) confirms record 772681, ICNP publication, correct-name status, the original authority and the separately listed emendation. Its returned print date is 2026-07-30; this is not an independently dated October snapshot. It additionally lists VKM Ac-1981 and YU6-1; VKM is already a strain collection identifier, and YU6-1 has independent native and primary-publication support. The authority-bearing NCBI synonym is correctly `RELATED_SYNONYM`.

GTDB mapping `data/raw/gtdb_mappings.tsv:1480` and species inventory `data/raw/gtdb_species.tsv:4704` agree on this exact species label, `skos:closeMatch` and five genomes. The pinned LPSN inventory explicitly links that GTDB identifier. Five complete native GTDB rows independently support the species membership and count. GTDB uses Mycobacteriales for these genomes while their NCBI taxonomy uses Pseudonocardiales. This source hierarchy difference is preserved; TaxonMech does not reconcile it by changing the NCBI lineage.

## Evidence

All eight source-attestation counts and units match complete own-ID inventory rows:

| Source | Count and unit | Inventory |
| --- | --- | --- |
| NCBITAXON | 1 NAME | `data/raw/ncbitaxon_taxa.tsv:18555` |
| LPSN | 1 NAME | `data/raw/lpsn_names.tsv:14917` |
| GTDB | 5 GENOME | `data/raw/gtdb_species.tsv:4704` |
| BACDIVE | 2 STRAIN | `data/raw/bacdive_strains.tsv:13041`, next row |
| MEDIADIVE | 2 MEDIUM | `data/raw/mediadive_taxa.tsv:139`, media 65 and J43 |
| GOLD | 8 ORGANISM | `data/raw/gold_organisms.tsv:519` |
| MADIN | 1 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:705` |
| BACTOTRAITS | 6 TRAIT_ASSERTION | `data/raw/bactotraits_taxa.tsv:104` |

Counts remain source-specific, not abundance estimates. Trait-attestation counts do not assert particular phenotypes. The complete seed sentence matches all eight sources and the admission reason. Current manifest timestamps are raw extraction 17:50:44Z, StrainInfo 17:29:00Z and ATB 17:54:04Z on 2026-09-13. The inspected `src/taxonmech/seed.py:_seed_timestamp` takes the latest, supporting `2026-09-13T17:54:04Z`. `SEEDED` is not human approval.

Complete native BacDive `data/bacdive/records.jsonl.gz:13040` supports strain 13200, taxon 103729, type status and all nine collection identifiers: DSM 44256, IFO 15664, JCM 9922, KCTC 9570, MTCC 2686, NBRC 15664, NCIMB 13658, NRRL B-24048 and VKM Ac-1981. The next native row supports strain 13201, the same species, explicit non-type status, and DSM 44257/IFO 15667/NBRC 15667. The YAML correctly asserts type status only for 13200. Inspected identity/deposit sections of the [13200 page](https://bacdive.dsmz.de/strain/13200) and [13201 page](https://bacdive.dsmz.de/strain/13201) corroborate the distinct entries. A generic Type strain heading in rendered page text was not substituted for the native Boolean or the explicit identification of 13200 as the type strain. The entire 13200 web page was not read; both complete local native records were.

BacDive reference 66792 links DSM 44256 to unversioned GCA_024171945, IMG 2596583621 and BV-BRC 103729.3. Reference 124043 links JCM 9922 to unversioned GCA_039534325, and separately links NBRC 15667 to unversioned GCA_030268905, IMG 8046760343 and BV-BRC 103729.6. Unversioned source accessions remain unversioned. These associations have independent deposit-specific BV-BRC, GOLD, GTDB and NCBI evidence:

| Deposit | GenBank / RefSeq | BioSample | Organism project | Native assembly size |
| --- | --- | --- | --- | --- |
| DSM 44256 | GCA_024171945.1 / GCF_024171945.1 | SAMN03080607 | PRJNA262062 | 11 contigs, 10 scaffolds, 7,638,937 total bases |
| JCM 9922 | GCA_039534325.1 / GCF_039534325.1 | SAMD00645421 | PRJDB10510 | 47 contigs, 44 scaffolds, 7,651,545 total bases |
| NBRC 15667 | GCA_030268905.1 / GCF_030268905.1 | SAMD00538865 | PRJDB14606 | 24 contigs, 22 scaffolds, 7,641,567 total bases |

Complete NCBI native assembly records were read at `data/catalog/ncbi_genbank-0022.jsonl.gz:19159`, `ncbi_refseq-0004.jsonl.gz:19026`, `ncbi_genbank-0036.jsonl.gz:4936`, `ncbi_refseq-0006.jsonl.gz:2966`, `ncbi_genbank-0028.jsonl.gz:8704` and `ncbi_refseq-0005.jsonl.gz:6984`, all under `data/catalog`. All three pairs are scaffold-level, paired identical, latest in the pinned inventory. DSM and JCM derive from type material; NBRC 15667 is not marked type material. Their ungapped lengths are 7,638,927, 7,651,344 and 7,641,377 bases, respectively. WGS identifiers are JAMTCR000000000.1, BAAAVC000000000.1 and BSSB00000000.1.

Focused public [DSM GenBank](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_024171945.1/dataset_report), [DSM RefSeq](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_024171945.1/dataset_report), [JCM GenBank](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_039534325.1/dataset_report), [JCM RefSeq](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_039534325.1/dataset_report), [NBRC GenBank](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_030268905.1/dataset_report) and [NBRC RefSeq](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_030268905.1/dataset_report) responses independently confirm current accessions, paired assemblies, exact deposits, species and sample/project identities. PRJDB9057 is the JCM project's parent. The pinned RefSeq/GTDB project PRJNA224116 is retained as source-specific evidence, not overwritten by live organism-project projections.

Complete BV-BRC native rows `data/bvbrc/bvbrc-0000.jsonl.gz:3426` through row 3430 distinguish all five species genomes. DSM is genome 103729.3, NBRC 15667 is 103729.6 and JCM is 103729.7, with explicit whole-deposit strain/culture fields. The other two rows are NBRC 15670/103729.4 and NBRC 15669/103729.5, not aliases of either represented BacDive strain.

Five native GTDB records were inspected completely: `data/catalog/gtdb_genomes-0006.jsonl.gz:711` (DSM), `gtdb_genomes-0008.jsonl.gz:45950` (JCM), `gtdb_genomes-0013.jsonl.gz:6962` (NBRC 15667), `gtdb_genomes-0009.jsonl.gz:43029` (NBRC 15669) and `gtdb_genomes-0016.jsonl.gz:5103` (NBRC 15670), all under `data/catalog`. DSM alone is the representative. The last two genomes are GCA/GCF_030268925.1 and GCA/GCF_030268945.1, samples SAMD00538867 and SAMD00538868. Their complete native NCBI records agree. Five GTDB genome records do not imply five BacDive entries or authorize transferring these two additional genomes to the listed deposits.

All eight own GOLD organism rows were inspected: Go0028504 explicitly relates YU6-1 to NRRL B-24048; Go0103585 is DSM 44256; Go0606209 through Go0606213 are IFO 15664, JCM 9922, KCTC 9570, MTCC 2686 and NBRC 15664; Go0670714 is NBRC 15667. Full native project/analysis records support `Ga0056967 -> Gp0103585 -> Go0103585`, `Ga0682030 -> Gp0854939 -> Go0606210` and `Ga0615997 -> Gp0761038 -> Go0670714`. The analyses have empty direct-organism fields but explicit project links with inspected organism IDs. Their assembly/sample/project and IMG associations agree with the table and BacDive evidence; no shared-taxon-only inference or cross-deposit IMG transfer was used.

Complete native StrainInfo `data/straininfo/records.jsonl.gz:38340` supports SI-ID 50538, BacDive 13200, published-online status, version 3 and eight available type deposits: DSM 44256/169370, IFO 15664/169371, JCM 9922/169372, KCTC 9570/169373, NCIMB 13658/211648, VKM Ac-1981/211649, NRRL B-24048/221599 and NBRC 15664/335999. GCA_024171945 explicitly names only DSM deposit 169370; AF114798 names only NRRL deposit 221599. MTCC 2686 and YU6-1 are relation designations, not extra SI-DP records.

The next native StrainInfo row supports SI-ID 50539, BacDive 13201, published-online status, version 2 and three available non-type deposits: DSM 44257/169375, IFO 15667/169376 and NBRC 15667/489242. Its genome GCA_030268905 explicitly names NBRC deposit 489242; the sequence is not transferred to the DSM/IFO deposits by grouping alone. Focused [DataCite 50538.3](https://api.datacite.org/dois/10.60712/si-id50538.3) and [DataCite 50539.2](https://api.datacite.org/dois/10.60712/si-id50539.2) metadata independently confirm active/findable status, expected version/title/species, eight versus three deposit counts and issue date 2025-02-25. Native records, not the DOI deposit counts alone, establish the individual deposit associations.

The full own-link inventories agree with the YAML: raw assemblies start at `data/raw/strain_assemblies.tsv:22366` (18 rows) and row 22411 (nine); StrainInfo adds rows 2078 and 2080 of `data/straininfo/assemblies.tsv`. Raw genome records start at `data/raw/strain_genome_records.tsv:17747` (ten) and row 17778 (seven). Raw related records start at `data/raw/strain_related_records.tsv:62769` (49) and row 62901 (20); StrainInfo related records start at `data/straininfo/related_records.tsv.gz:31833` (17) and row 31898 (six). Full source fields and deposit evidence were compared, not only identifier sets. Repeated identifiers from different source/field assertions retain legitimate provenance. NCBI snapshot reference names resolve to the inspected maintained raw manifest entries; source hashes were not recomputed and extraction was not replayed.

Crossref and the [original species-description page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-45-2-371) agree on Tamura et al., April 1995, volume 45(2), pages 371-378, DOI `10.1099/00207713-45-2-371`. The inspected abstract explicitly distinguishes five A. globicatena isolates and names YU6-1/IFO 15664 as the type, rather than YU6-2. The [notification page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-45-3-621) and Crossref agree on July 1995, volume 45(3), page 621, DOI `10.1099/00207713-45-3-621`. Full articles and the notification's full name table were not inspected.

[GenBank AF114798.1](https://www.ncbi.nlm.nih.gov/nuccore/AF114798.1), GI 5915958, explicitly identifies taxon 103729 and type strain NRRL B-24048T. Complete features and bibliography were read. The partial 16S marker has 1,510 declared and returned bases, alphabet acgnt, and lowercase sequence SHA-256 `3e5e0c9378fcd6303b00d57129510b19fdacc36bcb01e7d1ec7c1c3eabc465ae`. It is not a genome. The source's unversioned AF114798 is correctly preserved in YAML.

The marker-associated [PMID 10826820](https://pubmed.ncbi.nlm.nih.gov/10826820/), DOI `10.1099/00207713-50-1-331`, concerns partial-16S phylogeny and a historical Actinosynnemataceae proposal. Its inspected abstract is not used to overwrite current NCBI's family. The JCM assembly's [PMID 30832757](https://pubmed.ncbi.nlm.nih.gov/30832757/), DOI `10.1099/ijsem.0.003276`, describes the GCM type-strain sequencing program, not every phenotype of this genome. Both bibliographies and abstracts were read, not full articles.

## Completeness

An initial `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon 103729, the full species name/slug, all twelve collection designations with separator variants, and AF114798. All 274 candidate rows were read completely using raw rows or lossless common-field/delta views. A large initially truncated grouped output was reread in smaller groups before judging it. Five SOURCE.json files and history filenames were separately parsed/searched. The BacDive requested-ID metadata hit is a source-namespace number, not a taxon match. No own history filename was found.

A supplementary ignored/hidden/compressed search used all five known BioSamples, NBRC/IFO 15669 and 15670, HUT 6567 and YU designation variants. It returned 102 rows, 47 new to the initial search; all were read. The permissive YU pattern also matched longer unrelated names, whose actual identities were checked rather than treated as exact matches. Metadata files and history filenames were checked again with these keys.

The DSM BioSample has an ATB candidate at `data/atb/assemblies.tsv:3707` and `data/catalog/allthebacteria.tsv.xz:1062389`, run SRR4136507, FASTA available, no assembly accession, with both assembly/HQ filters `META_FAIL` and Sylph species matching. `data/atb/exclusions.tsv:2038` explicitly records `metadata_identity_flags:META_FAIL`. Current `src/taxonmech/atb_catalog.py:82`, `CLAUDE.md` and strain-genome guidance reject identity-quality failures even when FASTA exists. Its exclusion is correct; absence of an ENA analysis or non-HQ status alone would not establish the same exclusion.

Additional conspecific StrainInfo records 62211 and 62212, at native rows 49752 and 49753, retain NBRC/IFO 15669 and 15670, explicit deposit-linked GCA_030268925 and GCA_030268945, and no BacDive cross-reference. HUT 6567/SI-ID 218709 at row 161325 is published offline, non-type, without a sequence or BacDive link. These are retained source knowledge, not evidence to invent extra BacDive entries or attach their genomes to the two represented strains. SeqCode name 1289 at `data/seqcode/names.jsonl.gz:1055` is a minimal name/URI record, not independent nomenclatural validation or functional evidence.

False positives were kept separate: BacDive 103729 is Rhodococcus ST002162; CIP 103729 is Exiguobacterium aurantiacum/BacDive 139099/SI-ID 42614; DSM 103729 is Echinicola sediminis/BacDive 140384/SI-ID 397295; SI-DP 103729 is Stigmatella erecta ATCC 25192. CP103729 belongs to Klebsiella strain 197/GCA_024918855.1. MGBC103729 is an uncultured Eubacteriales genome, GCA_948927995.1. Other hits are unrelated Salmonella, Escherichia and Campylobacter identifiers, six non-target GTDB rows with unrelated identifiers or assembly statistics, and an ATB checksum for Escherichia sample SAMN14417573/run SRR11361692/ERZ25736816.

The broader YU search additionally found Cryptosporangium YU 629-21, Sporichthya YU720-21, an Actinomycetota MAG YU_71_112, Hydrococcus Yu-52, Ryu-named cyanobacteria and Pseudomonas, and unrelated eukaryotic culture designations in source-native StrainInfo rows. Those rows were read only to disambiguate candidates; no eukaryotic YAML was reopened or reviewed. None supplies an A. globicatena deposit association.

No consequential missing required representation was established. Optional definition, functional evidence and graph slots may remain empty. iModulonDB is inapplicable because the YAML asserts no gene, regulator, pathway, functional trait identity or expression dataset. All absence and completeness conclusions are bounded to inspected roots, snapshots, query keys, responses and the current model; no claim is made to cover all possible biological knowledge.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source-scoped nomenclature and mapping, two distinct strain entries, deposit-specific sequence/genome links, attestations and seed history are supported. The five-genome/two-strain count difference and ATB exclusion are explained by the inspected source model, not defects.

## Recommended Edits

None required for the represented claims. Future source refreshes should update maintained inventories/transforms and regenerate through the seeder and validated writer, not hand-edit this YAML. Preserve whole-deposit identity, supplied accession versions, StrainInfo sequence-to-deposit scope and separate source assertions. Do not transfer the NBRC 15669/15670 genomes to another deposit or admit the ATB record without resolving its upstream identity-quality flags.

## Follow-up Checks

For later enrichment, verify explicit deposit and source-native sequence associations, then re-run schema/strict validation, history validation when history changes, and full corpus/QC gates after maintained inputs change. Retry unavailable GTDB/StrainInfo browser pages when useful; successful authority APIs and complete native catalog rows already support the represented claims. No unresolved blocker remains.

## Additional Notes

Only NCBITaxon:103729 is judged using its entire YAML and independently inspected evidence. No adjacent-record verdict was inherited. The new report is the only repository write for this target; records, source data, scope, history, generated products, statuses, branches, worktrees and GitHub remain unchanged. The other session was not contacted. No paid research was used. DataCite identity/status checks used a focused reread after a duplicate XML payload made the initial output too large; full XML inspection is not claimed. Full-corpus and public-page limitations above remain explicit.
