# YAML Record Review: Allobosea robiniae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/allobosea_robiniae.yaml`
- Started UTC: 2026-10-09T14:58:40Z
- Finished UTC: 2026-10-09T15:07:05Z
- Verdict: pass

## Target

This review concerns one generated `TaxonRecord`: `NCBITaxon:1036780`, Allobosea robiniae, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read. Its parent is `NCBITaxon:85413` (Allobosea), grounding is `EXACT`, mapping status is `SEEDED`, and genetic code is 11. The record contains one listed BacDive strain, two GTDB mappings and eight source attestations. It is not a human-approved curation.

The target resolves uniquely in the ignored-inclusive record/report inventory. Source ownership remains with the maintained extraction/seeding code, committed inventories, source overlays and scope, not this generated YAML. SHA-256 at review: `3dd205de5a6b64f675f0a4234dc2dd4ec7e230f917343f653bf27d6aadcaf3e4`.

## Validation

Commands used the existing offline environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/allobosea_robiniae.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/allobosea_robiniae.yaml --workers 1 --out /private/tmp/taxonmech-arob-20261009-validation.tsv`: passed, one file, zero errors. The output TSV was inspected and contains only its header.
- `uv run --offline python scripts/validate_history.py history`: passed; 17 history records valid and zero invalid history links.
- Read-only structured comparisons checked the complete NCBI ancestor chain, target inventory rows, scope/path entries and every assembly, genome-record and related-record assertion. All 10 assembly assertions, seven genome-record assertions and 36 related-record assertions exactly match their source rows after the repository's StrainInfo conversion. No ATB strain-link row belongs to this strain.
- `kg-microbe-sources imodulondb datasets`, through the local `culturebotai-claw` runner: succeeded, 28 datasets. No covered Allobosea/Bosea organism matches this target; gene/component searches are not applicable. This is not negative functional evidence.
- Not checked: `just verify-corpus`, full-corpus strict validation, provenance/QC/tests and site drift were not rerun for this individual review. The documented reproduction gate has no target selector. The bounded comparisons above are not a substitute for that gate.
- Not applicable: OAK product-label validation for curator-added graph nodes. This record contains no such graph, and `conf/id_label_targets.yaml` explicitly delegates taxon identity to the NCBI inventory/corpus gate.
- Public NCBI taxonomy, nucleotide and assembly metadata, LPSN, BacDive, PubMed, Crossref and DataCite were inspected. Live GTDB representative pages were inaccessible through the web tool; pinned native GTDB rows supplied the mapping checks.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222620` agrees with the complete YAML identity and nine-entry root-first lineage. The native names at `data/catalog/ncbi_names-0005.jsonl.gz:32193` through physical row 32198 distinguish the scientific name, two authorities, historical synonym and two includes names. The YAML preserves the different NCBI and LPSN synonym scopes instead of silently collapsing them.

Live [NCBI taxonomy 1036780](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036780) and the NCBI Datasets taxonomy response agree with species rank, parent 85413, lineage and genetic code. Nine type-material assertions occur at `data/raw/ncbi_type_material.tsv:1939` through row 1947. The merged-ID row at `data/raw/ncbi_merged_ids.tsv:99833` maps 946787 to this taxon; both live NCBI interfaces independently resolve 946787 to 1036780. No own child or dropped record was found in complete relevant inventory scans.

Current [LPSN 70774](https://lpsn.dsmz.de/species/allobosea-robiniae) supports the legitimate, validly published correct name, authority, three collection designations and FR774994. [Historical LPSN 790219](https://lpsn.dsmz.de/species/bosea-robiniae) is the illegitimate homotypic synonym, not another species. Their own raw rows are `data/raw/lpsn_names.tsv:11187` and row 27199.

[PMID 41649870](https://pubmed.ncbi.nlm.nih.gov/41649870/) resolves to DOI `10.1099/ijsem.0.007072`, including the Allobosea robiniae replacement combination. Crossref independently resolves [DOI 10.1099/ijsem.0.007121](https://doi.org/10.1099/ijsem.0.007121) to the notification concerning volume 76, part 2. These support nomenclature, not genome equivalence or additional phenotypes.

## Evidence

**Strain and assembly ownership.** `data/raw/bacdive_strains.tsv:1789`, `data/bacdive/records.jsonl.gz:1788` and live [BacDive 1793](https://bacdive.dsmz.de/strain/1793) support R-46070 and deposits CCUG 61249, DSM 26672 and LMG 26381. The type flag is independently supported by NCBI, LPSN and the [original species paper, PMID 22155761](https://pubmed.ncbi.nlm.nih.gov/22155761/). The declared strain count is one and the listing is complete for its BacDive inventory; three deposits do not mean three biological strains.

The ten assembly assertions retain distinct source evidence: BacDive one, BV-BRC two, GOLD two, GTDB two, NCBI Assembly two and StrainInfo one. They do not represent ten unique genomes. Unversioned `GCA_900102525` from BacDive/StrainInfo is preserved without inventing a version; other sources explicitly supply `GCA_900102525.1` or `GCF_900102525.1`.

The [live NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_900102525.1/dataset_report) confirms the current GCF/GCA pair, DSM 26672, taxon 1036780, type material, SAMN05421844, 21 contigs, 5,279,103 bp and 66.5% GC. The paired native rows are `data/catalog/ncbi_genbank-0056.jsonl.gz:38954` and `data/catalog/ncbi_refseq-0009.jsonl.gz:26711`. BV-BRC's own `data/bvbrc/bvbrc-0000.jsonl.gz:3401` supports `patric:1036780.5`; BacDive and GOLD independently support `img.taxon:2675903146`. The seven typed genome assertions preserve these provenances rather than claiming sequence identity across systems.

**GOLD chain and project scope.** `data/gold/analyses.jsonl.gz:57115`, `data/gold/projects.jsonl.gz:75611` and `data/gold/organisms.jsonl.gz:36915` establish `Ga0104481 -> Gp0127254 -> Go0044041`, with explicit DSM 26672 evidence. They support the assembly, IMG, BioSample and project assertions. LMG and CCUG organism rows 446589 and 446590 support only their own organism references.

The record preserves PRJEB15855 from assembly/BV-BRC, PRJNA224116 from RefSeq/GTDB snapshot fields and PRJNA329846 from GOLD. Live NCBI exposes PRJEB15855 at assembly level and PRJNA329846 on the BioSample. The pinned RefSeq project is not silently overwritten with the differently scoped live value. All 36 related-record assertions exactly reproduce their evidence: BV-BRC four, NCBI four, GTDB two, GOLD 14 and StrainInfo 12.

**StrainInfo deposit restrictions.** The complete own record at `data/straininfo/records.jsonl.gz:286717` supports SI-ID 371082, BacDive 1793, three available non-erroneous type deposits and DOI [10.60712/SI-ID371082.3](https://doi.org/10.60712/SI-ID371082.3). DataCite confirms this version and three-deposit dataset. SI-DP 912905 is DSM 26672, 865464 is LMG 26381 and 873366 is CCUG 61249. The genome explicitly names only DSM's deposit; all six marker sequences explicitly name LMG's deposit. The YAML does not transfer those links merely because deposits share an SI-ID.

Live GenBank metadata, features and sequence lengths were checked independently for:
- [FR774994.1](https://www.ncbi.nlm.nih.gov/nuccore/FR774994.1): 1,439 bp 16S rRNA; source strain R-46070 = B1218, type material, taxon 1036780.
- [FR871208.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871208.1): 507 nt, source-labelled atpD, LMG 26381.
- [FR871220.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871220.1): 400 nt, source-labelled recA, LMG 26381.
- [FR871228.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871228.1): 674 nt, source-labelled gyrB, LMG 26381.
- [FR871236.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871236.1): 1,469 nt, source-labelled rpoB, LMG 26381.
- [FR871244.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871244.1): 293 nt, source-labelled dnaK, LMG 26381.
- [FR872721.1](https://www.ncbi.nlm.nih.gov/nuccore/FR872721.1): 291 nt, source-labelled nifH, LMG 26381.

All resolve to the current taxon. These are accession and deposit assertions, not independent functional validation. In particular, PMID 22155761 reports nonspecific nifH PCR products. The retained source description for FR872721 must not be promoted into nitrogen-fixation or nodulation evidence. The YAML does not do so.

**GTDB mappings.** Both raw mappings at `data/raw/gtdb_mappings.tsv:1467` and row 1468 have count five and `skos:broadMatch`; species rows 7714 and 7748 agree. All five native genomes in each cluster were inspected, not just a representative.

The preferred `s__Allobosea_robiniae` cluster includes DSM 26672, Root670, AFS039014, AK1 and the SRR18156207-derived MAG. Its representative `RS_GCF_900102525.1` is the type strain, but the cluster spans other NCBI taxa. The second cluster, `s__Allobosea_sp024655635`, contains representative `RS_GCF_024655635.1` (47.2.35) plus BE109, BE168, BE271 and this NCBI species' BE144 (`RS_GCF_031456205.1`). Its other members map to NCBI taxa 2817907, 2817908, 2818430 and 2969304. Non-equivalence and pooling are therefore material and correctly retained. The primary attestation's count five plus a note about one additional cluster is not a total of ten type-strain genomes. GTDB's historical Rhizobiales/Beijerinckiaceae lineage does not replace NCBI's carried lineage.

**ATB exclusion.** The linked BioSample's `data/atb/assemblies.tsv:4669` and native `data/catalog/allthebacteria.tsv.xz:1172799` retain SAMN05421844, SRR4233905, available FASTA and `META_FAIL` for both filters. `data/atb/exclusions.tsv:2224` explicitly gives `metadata_identity_flags:META_FAIL`. The absent ATB genome entry is intentional under repository eligibility rules, even though the BioSample has supported external assembly links. Another candidate, SAMEA3643138 / ERR1104150, has `ENA_ASM_SUBMIT_ERR` and HQ PASS but no own deposit/sample evidence chain; its source species prediction alone does not supply one. Lack of ENA submission alone was not treated as disqualifying.

## Completeness

The eight attestations match their own inventory values and units: NCBI one name, LPSN one name, primary GTDB five genomes, BacDive one strain, MediaDive one medium, GOLD six organism-source entries, Madin three trait assertions and BactoTraits six trait assertions. The relevant raw rows are NCBI 222620, LPSN 11187, GTDB 1467, BacDive 1789, MediaDive 135, GOLD 508, Madin 701 and BactoTraits 102. Counts from different sources/units are not added together. MediaDive's species-level medium 1 does not create a missing strain-level medium count where the BacDive inventory records zero.

A specific verification limit remains for GOLD's six-entry attestation. The separate primary GOLD organism catalog contains five matching entries: Go0044041, Go0553270, Go0615886, Go0615887 and Go0615888. These do not independently establish the KGX count of six. `src/taxonmech/extract.py:403` counts matching KGX edge rows, and its call at line 676 reads a different input from the primary workbook used for strain links. `data/raw/MANIFEST.yaml` pins that 83,535,194-byte edge input with SHA-256 `b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12`. The original edges were not found in an ignored-inclusive filename search of repository source/history directories and the configured sibling kg-microbe data root. A sixth unique organism, duplicate edge, or source-snapshot difference cannot be distinguished here. The generated attestation matches its maintained inventory; changing six to five from the different catalog would be unsupported.

Completeness searches included ignored/hidden files and compressed catalogs under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. They used the taxon, current/historical labels, strain/deposit aliases, merged identifier, genome/sample/project IDs and marker accessions. All candidate rows were read completely, including unrelated numeric collisions; metadata in all five source `SOURCE.json` files was parsed. Absence statements are bounded to those local sources, not global biological absence.

The own source candidates do not justify additional links on BacDive 1793:
- Non-type BE144 and HIB071 assemblies have no eligible type-deposit join. BE144's separate BV-BRC/GOLD/GTDB chain was inspected and not transferred.
- GOLD's R-46070 row lacks an eligible culture accession; the bare designation is not a join key under current rules.
- SI-ID 388205 / SI-DP 886386 is non-type LMG 26382, alternative R-46073, with no sequences or own BacDive match. It is not LMG 26381. The native inventory also retains NCBI 946788 as Allobosea sp. R-46073, a separate taxon. This cross-source classification difference does not create an additional type-strain link.
- SeqCode 3965 records the historical Bosea robiniae name; it is not a new genome assertion.

No curated causal graph, gene-function claim, experimental trait table, human sign-off or target-specific external history file is required merely because source counts or marker descriptions exist. Ignored-inclusive content and filename searches found no target-specific history item. Scope row 4051, PATHS row 15148 and the single 2026-09-13 seeding event agree with the generated status.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and inspected evidence. The unreplayed GOLD source count and inaccessible live GTDB pages are verification limits, not demonstrated record defects.

## Recommended Edits

None required for this record on present evidence. Do not edit the generated YAML, replace the GOLD count with the separate catalog count, add the excluded ATB assembly, transfer BE144/HIB071 genomes, or infer nitrogen fixation from a marker's source title.

If the GOLD count is investigated later, the owner is the configured kg-microbe `data/transformed/gold/edges.tsv` input and the extraction logic in `src/taxonmech/extract.py`, with resulting inventory changes in `data/raw/gold_organisms.tsv`. Establish the exact pinned input's rows before proposing a correction.

## Follow-up Checks

- Replay the six GOLD KGX edge rows against the manifest hash if that original input becomes available; inspect subjects, duplicates and taxonomy normalization before comparing with the primary workbook.
- Retry the two GTDB representative pages and compare source release dates with the pinned catalog, without replacing NCBI lineage.
- Run the documented full-corpus reproduction, provenance, tests and publication gates before any later authorized regeneration. This report makes no corpus-wide validation claim.
- Preserve explicit StrainInfo deposit restrictions, accession versions, source-specific project fields and the ATB META_FAIL exclusion in any future refresh.

## Additional Notes

This was an independent single-record review, not a verdict inherited from neighboring species. The only repository write for this target is this new timestamped report. No record, source inventory, history entry, review status, generated page, branch or worktree was changed; no paid research or GitHub mutation was performed. Eukaryota remains outside the active review queue because its per-record reporting is already complete.

