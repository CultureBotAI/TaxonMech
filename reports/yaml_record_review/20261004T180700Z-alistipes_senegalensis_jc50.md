# YAML Record Review: Alistipes senegalensis JC50

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alistipes_senegalensis_jc50.yaml`
- Started UTC: 2026-10-04T18:04:08Z
- Finished UTC: 2026-10-04T18:07:00Z
- Verdict: needs curation

## Target

Reviewed the complete generated `TaxonRecord` for `NCBITaxon:1033732`, Alistipes senegalensis JC50. This is the bacterial strain taxon under species `NCBITaxon:1288121`, not the species itself, Exiguobacterium sp. JC50, Pedobacter sp. JC50, or Anaerococcus senegalensis. The target has genetic code 11, `EXACT` NCBI grounding, `SEEDED` lifecycle status, one GTDB mapping, two synonyms, three attestations and zero listed BacDive strains. The parent species YAML was read in full as evidence-placement context only; this report does not separately adjudicate that record.

An ignored-inclusive exact-identifier search resolved one target YAML. An ignored-inclusive exact-stem report search found no existing review before this report was written.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/alistipes_senegalensis_jc50.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/alistipes_senegalensis_jc50.yaml`: passed, one file scanned and zero error rows.
- Compared identity, the entire lineage, NCBI synonym, direct-child inventory, all seven taxon-level source inventories, all three attestation counts and units, PATHS, scope and seed-history text against committed evidence. These bounded comparisons do not prove whole-corpus reproduction.
- Full-corpus `just verify-corpus`, `just qc`, `just test`, provenance, generated-page drift, documentation-statistics and vendored-file gates were not run. No substitute focused corpus validator was invented.
- `just validate-products` was not applicable to any new graph node: this record has no curator-added causal graph. No external history file was created or validated. The record's existing seed history was inspected, not changed.
- Public NCBI taxonomy, both exact-taxid assembly summaries, full current assembly/BioSample metadata, and the selected 16S marker were inspected. GTDB browser tree/genome pages were unavailable through the web tool; the complete pinned native catalog supplied the relevant classification evidence instead. No complete nucleotide-corpus or sequence-level assembly audit is claimed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221298` identifies this strain, parent 1288121, code 11, NCBI exact synonym `Alistipes sp. JC50`, and the 2026-09-13 snapshot. The native scientific-name and synonym objects were read at `data/catalog/ncbi_names-0005.jsonl.gz:30608` and `:30609`. PATHS row 13751 fixes the target slug; scope row 36146 records admission on 2026-09-12 for the three-source attestation rule. The seed event is 2026-09-13T17:54:04Z and correctly names GTDB, MADIN and NCBITAXON.

The [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033732&retmode=xml) confirms the label, strain rank, parent, code and old name. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033732) independently confirms `STRAIN` and the root-first ancestor identifiers 1, 131567, 2, 3379134, 1783270, 68336, 976, 200643, 171549, 171550, 239759 and 1288121. Their labels and ranks agree with the stored lineage and pinned backbone.

The [legacy NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1033732) displays `no rank`, while the structured APIs and pinned dump say strain. Its older synonym rendering and rank are preserved as an interface discrepancy, not used to overwrite the supported generated identity. No direct descendants or exact target rows in the merged-ID, dropped-record and type-material tables were found. Type evidence exists at the parent species instead.

The identifier is correctly grounded. The species-level GTDB equivalence is the material defect, not the NCBI identity.

## Evidence

### Attestations and the GTDB Cluster

The source counts reproduce the inventories: NCBI one NAME, GTDB 40 GENOMEs from `data/raw/gtdb_mappings.tsv:1357`, and Madin five TRAIT_ASSERTIONs from `data/raw/madin_taxa.tsv:622`. `data/raw/gtdb_species.tsv:7155` independently gives 40 members of the source species cluster. No target taxon rows were found in the BacDive, LPSN, GOLD, MediaDive or BactoTraits taxon inventories. A GOLD organism found in the separate native workbook catalog does not establish an omitted KGX taxon attestation; the source surfaces have different documented purposes.

The full 901,341-row native GTDB catalog scan found 40 unique accessions in `s__Alistipes senegalensis`: two under 1033732, 29 under 1288121, one under 1262924, three under 1872444, one under 3077420, one under 3133172 and three under 538949. The two target-taxid objects were read in full: `data/catalog/gtdb_genomes-0001.jsonl.gz:30986`, RS_GCF_025145645.1, is representative; `gtdb_genomes-0010.jsonl.gz:20739`, RS_GCF_000312145.1, is not. Both carry bare `JC50` as `ncbi_strain_identifiers`. Neither supplies an eligible whole culture-deposit token for a GTDB deposit join. Membership in the same species cluster is not species/strain identity and does not establish assembly equivalence.

### Nomenclature and Conflicting Deposit Aliases

[LPSN 70252](https://lpsn.dsmz.de/species/alistipes-senegalensis) now lists Alistipes senegalensis Mishra et al. 2026 as a validly published correct name, with JC50, DSM 25460 and CSUR P156 as type designations; it explicitly warns against CSUR P150 and P155. The local parent-species LPSN row, `data/raw/lpsn_names.tsv:10941`, agrees on the current name/status and maps to 1288121, not this strain taxon. The quoted 2012 name in older sources is not evidence that the current 2026 nomenclature should be reverted.

[DSMZ's DSM 25460 page](https://www.dsmz.de/collection/catalogue/details/culture/DSM-25460) identifies JC50 as type material but lists CSUR P150, while [JCM 32779](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=32779) gives the succession from DSM 25460/JC50 and CSUR P156. The legacy NCBI browser likewise warns that P156 was incorrect and belongs to Anaerococcus senegalensis. These are directly conflicting source assertions. Do not choose one silently or use the disputed CSUR alias to transfer genomes between genera.

[BacDive 130658](https://bacdive.dsmz.de/strain/130658) retains both CSUR numbers, DSM 25460 and JCM 32779, and classifies the strain at species 1288121. Its current page says type strain, but the pinned full native object at `data/bacdive/records.jsonl.gz:52970` has `type strain: no`; the full StrainInfo snapshot also has a false type flag. The parent YAML's derived type flag is supported independently by its LPSN DSM-25460 designation, rather than copied from those old flags. The raw BacDive row is `data/raw/bacdive_strains.tsv:52971`.

The alias collision is concrete in local evidence: `data/raw/culture_collection_strains.tsv:57095` maps CSUR P156 to both 1288120 and 1288121. Full native BacDive 17977 at row 17785, StrainInfo SI-ID 402066 at row 299955 and GOLD Go0614536 at organisms row 445262 instead associate P156 with Anaerococcus senegalensis JC48 / DSM 25366. This is contextual uncertainty requiring source-owner resolution, not a new defect in the target's empty strain list. DSM 25460 is the consistent deposit used by the supported genome chains checked below.

### Primary Literature and Marker

The inspected classification, genome-project and species-description sections of [Mishra et al., DOI:10.4056/sigs.2625821, PMID:23407265](https://pmc.ncbi.nlm.nih.gov/articles/PMC3558963/) explicitly identify JC50 = DSM 25460 = CSUR P156. They describe a Senegal fecal specimen, March 2011 isolation in Marseille, marker JF824804 and WGS project CAHI00000000. The project table labels the genome a high-quality draft; the assembly description gives four scaffolds and 40 large contigs. Preserve that scope despite complete-genome language elsewhere and do not replace current assembly statistics with the paper's historical description.

[JF824804.1](https://www.ncbi.nlm.nih.gov/nuccore/JF824804.1) was read as GenBank XML: a 1,480-bp partial 16S sequence with strain JC50, taxon 1033732 and explicit type-material annotation. Its references identify the species-description paper, a culturomics article DOI:10.1111/1469-0691.12023 / PMID:23033984, and a direct submission dated 2011-04-18. The secondary article was not independently used to establish experimental claims. This marker is not a whole genome; no phenotype or clinical claim was added to the target.

### Assemblies and Source Chains

The exact-taxid Assembly search returned two records, and both complete summaries were inspected. Full [Datasets metadata for GCA_025145645.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_025145645.1/dataset_report) explicitly identifies BioSample SAMN20222637 as JC50_DSM_25460 from DSMZ, with `culture_collection: DSM:25460`.

- GCA/GCF_025145645.1 is current, complete, from type material, and has one 4,023,197-bp chromosome. Its BioSample is SAMN20222637 and GenBank project PRJNA746600. The native BV-BRC entries connect it to CP102252 and PATRIC 1033732.50/.51 through the DSM deposit, not simply through the strain name.
- GCA/GCF_000312145.1 is the current draft pair, ASM31214v1, with SAMEA2272561, PRJEA82331 and CAHI00000000.1. The native catalogs give 41 contigs, six scaffolds, 4,017,609 total and 3,985,109 ungapped bases. This differs from the paper's historical scaffold/large-contig counts; retain the distinction. BacDive directly supplies GCA_000312145, PATRIC 1033732.3 and IMG 2547132124.

Full GenBank/RefSeq objects were read at shards 0000:7775, 0023:15432, 0000:6674 and 0004:25505, respectively. GCA/GCF paired-accession equivalence is explicitly asserted by NCBI, but co-occurrence of other IDs in a strain record is not proof they denote identical assemblies. Native BV-BRC rows 3190-3192 in shard 0000 retain the two newer PATRIC IDs separately.

The full GOLD objects at organisms:12554, projects:12301/:604318 and analyses:11772/:448281 establish two DSM-supported chains: Go0014227 -> Gp0014227 -> Ga0019622 -> GCA_000312145.1 / IMG 2547132124, with SAMEA2272561; and Go0014227 -> Gp0818985 -> Ga0668278 -> GCA_025145645.1 / IMG 8119058418, with SAMN20222637. Go/Gp/Ga identifiers remain organism/project context, not genome counts.

The parent strain also holds FDAARGOS_1578 evidence classified under species 1288121. Its full GOLD chain, Go0644972 -> Gp0680950 -> Ga0579559, explicitly matches DSM 25460 and supplies GCA_020735725.1, CP085931, SAMN22091675 and PRJNA231221. Native objects are organisms:474661, projects:512165 and analyses:377507. BV-BRC shard 0001 rows 20108-20110 independently carry `DSM:25460`; PATRIC 1288121.42 is Complete while .43 and .44 are Deprecated. Preserve those source-status distinctions rather than counting all three as independent current biological genomes. This contextual association does not reclassify the FDAARGOS taxon or declare its assembly identical to the JC50 assembly.

StrainInfo SI-ID 397159, DOI:10.60712/SI-ID397159.3, has its own available DSM 25460 deposit SI-DP 903767. The full native object at `data/straininfo/records.jsonl.gz:295048` contains no sequence array. The parent correctly carries SI strain/deposit related records without inventing StrainInfo genome links from BacDive cross-references or aliases.

ATB has two eligible sample associations on that parent strain: SAMN20222637 (catalog row 2095220, overlap row 8298, SRR15171219, ERZ25973751, SeqKit sum ending `ca342aeaeeaf36c3a48d22a38245e695`) and SAMN22091675 (catalog row 2161515, overlap row 8477, SRR17133871, ERZ26022327, sum ending `46ee8d380484251c1224d24b937811d2`). Both have available FASTA and PASS assembly/HQ filters. The parent preserves three prior BioSample assertions for the first and four for the second; strain-link rows 550-551 and genome-link rows 2397-2404 distinguish the two chains. These are snapshot-scoped `shares_biosample` relationships, not proof of identical sequence. The full SeqKit values, batch-95 archive links and mutable AWS URLs remain in the source and YAML. No FASTA or archive was downloaded.

## Completeness

The strain record's zero BacDive count is consistent with the classification-based seeding contract: BacDive files JC50 under parent 1288121, and this taxon has no children. The parent already contains BacDive 130658 with its supported genome, ATB and SI evidence. A species taxon can gather descendant strains; a strain taxon must not inherit every strain filed under its parent. Missing narrative definitions, record-level citations or causal graphs are not missing required seeded fields.

All local absence/collision searches included ignored and hidden files, plus compressed source catalogs. The primary command used `rg --no-ignore --hidden -n -z -i` across raw inventories, native catalogs, BacDive, BV-BRC, GOLD, SeqCode, StrainInfo, ATB, curation and history. The target-id/name/designation search completed with 69 matching lines; the expanded DSM/JCM/CSUR/marker/BioSample search completed with 82. Source manifests were queried separately. Additional exact FDAARGOS-chain and ATB-sample searches resolved the objects cited above.

Excluded unrelated matches include Exiguobacterium sp. JC50 (660995), Pedobacter sp. JC50 (1284017), a Muribaculaceae MAG GCA_948940335.1 whose size is 1033732, and ATB SAMEA1033732 / SRR1033732 hits for Streptococcus pneumoniae and Acinetobacter sp. 742879, respectively. Whole typed identifiers, not numeric overlap, establish identity. iModulonDB was not applicable to the taxonomic claims reviewed here.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species is asserted equivalent to the JC50 strain taxon.** The target's `skos:closeMatch` at line 49 is promoted to the exact species-name synonym at line 52 and equivalence xref at line 60; the attestation repeats the predicate at line 73. The schema reserves xrefs for true equivalence, while a strain and its containing species are different concepts. The 40-accession cluster spans seven NCBI taxa, with only two accessions carrying 1033732. The source count is numerically supported but does not mean 40 JC50 strains or genomes. The inherited edge is `data/raw/gtdb_mappings.tsv:1357`; the distinct parent-species edge is row 16606. The maintained upstream owner is kg-microbe's GTDB mapping transform, imported by `src/taxonmech/extract.py:501`. Locally, `src/taxonmech/seed.py:451` makes every closeMatch an identity and lines 467-469 emit the unsupported exact synonym and xref without a rank guard. Passing schema validation does not establish that semantic equivalence.

## Recommended Edits

Correct the maintained upstream GTDB mapping semantics, and add a rank-aware defensive identity rule and regression tests in TaxonMech's seeder. Through authorized regeneration, stop emitting the species name as an exact synonym or true-equivalence xref of JC50. Keep the NCBI identity, lineage and old NCBI synonym, the source classification evidence, and parent-held deposit/genome links.

Do not blindly change the predicate to `skos:broadMatch`: the schema defines it from the source taxon's side when the NCBI target is broader, not narrower. Do not silently substitute two for the documented 40-member source-cluster count. The CSUR contradiction is a separate source-owner follow-up; do not merge Anaerococcus records, manufacture an alias resolution, or copy disputed links onto the target. No generated record, inventory, scope, source alias or historical report was edited here.

## Follow-up Checks

After an authorized maintained-source correction, re-extract, run the seed dry-run and JC50 seed canary, inspect the resulting YAML, and rerun both record validators. Test species-to-strain mapping guards, genuine species equivalence, pooled mappings, count semantics and unchanged DSM-supported evidence placement. Run `just verify-corpus` and `just qc` before claiming global correctness. Resolve the CSUR P150/P156 disagreement at the primary collections/nomenclatural authorities before using either disputed alias for new joins; the present report leaves that conflict open without blocking the supported NCBI identity.

## Additional Notes

This was one independently evidenced record review, not a verdict copied from an adjacent strain. The parent species and Anaerococcus objects were supporting context, not additional completed reviews. Only this new timestamped report and the validator's standard output artifact were written. No lifecycle status was promoted, no history entry or GitHub mutation was made, and no paid service or contact was used. Eukaryota remains outside the remaining review work. The all-record review goal is still incomplete.
