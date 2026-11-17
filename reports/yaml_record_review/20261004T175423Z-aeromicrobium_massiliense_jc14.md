# YAML Record Review: Aeromicrobium massiliense JC14

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aeromicrobium_massiliense_jc14.yaml`
- Started UTC: 2026-10-04T17:50:16Z
- Finished UTC: 2026-10-04T17:54:23Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord`, NCBITaxon:1033730, Aeromicrobium massiliense JC14. It represents one STRAIN below species NCBITaxon:1464554, not the entire species. The record is BACTERIA, EXACT grounded, SEEDED, code 11, with zero inventoried BacDive strains, a GTDB mapping/xref, two synonyms, four source attestations and a 2026-09-13T17:54:04Z seed event. No generated field was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/aeromicrobium_massiliense_jc14.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/aeromicrobium_massiliense_jc14.yaml`: passed, one file, zero errors.
- Completed ignored-inclusive exact-ID search across `data/taxa`: only the target YAML. Exact-stem report search found no prior report.
- Structured comparisons matched backbone, complete lineage, children, source inventories, PATHS, scope, NCBI attestation and seed text. Other attestation counts were checked against their individual inventory rows. Exact type-material, merged-ID and dropped-row scans completed.
- Full native GTDB catalog scan covered 901,341 rows and counted both members of the exact species cluster. This is a source check, not a newly invented validator.
- Not run: corpus-wide `just qc`, `just verify-corpus`, tests, provenance, rendering, documentation and global term/reference/history gates. No curator-added graph or citation is asserted in the target; strict validation covered embedded history shape. These focused checks do not establish whole-corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221296`, `data/catalog/ncbi_names-0005.jsonl.gz:30604` and the full synonym object on line 30605 support the NCBI identity and Aeromicrobium sp. JC14 synonym. `data/taxa/PATHS.tsv:13749` pins the slug; `curation/seed_scope.tsv:26082` records inclusion on 2026-09-12.

Live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033730&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033730) confirm STRAIN, parent 1464554, code 11 and the NCBI synonym. The entire root-first chain matches root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Actinomycetota 201174 (PHYLUM), Actinomycetes 1760 (CLASS), Propionibacteriales 85009 (ORDER), Nocardioidaceae 85015 (FAMILY), Aeromicrobium 2040 (GENUS), Aeromicrobium massiliense 1464554 (SPECIES). Datasets explicitly includes root 1. The web tool's cached [legacy taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1033730) displays no rank; this differs from both current structured responses and the pinned STRAIN inventory. It is not evidence to overwrite the record's rank.

The GTDB-derived exact species synonym and equivalent xref do not respect this strain/species distinction. This is the substantive finding below; NCBI identity itself is sound.

## Evidence

`data/raw/gtdb_mappings.tsv:1355` supplies closeMatch and genome_count 2; `gtdb_species.tsv:5526` confirms the source species count. `gold_organisms.tsv:444` supplies one ORGANISM and `madin_taxa.tsv:620` supplies four TRAIT_ASSERTIONs. These different units must not be summed as a biological count. The GOLD number is the KGX-derived inventory count, not a census of the independently retained native workbook. No direct BacDive, LPSN, MediaDive or BactoTraits row, child taxon, merged-ID or dropped row was found for the target. Type-material rows are filed under the parent species, not this strain taxid.

The exact GTDB cluster has two native accessions: representative RS_GCF_000312105.1 at `data/catalog/gtdb_genomes-0002.jsonl.gz:12007`, classified by NCBI under 1033730, and RS_GCF_902374835.1 at `gtdb_genomes-0000.jsonl.gz:35680`, classified under species 1464554 with isolate MGYG-HGUT-01418. Both full objects were inspected. The same GTDB species also maps to the parent at `data/raw/gtdb_mappings.tsv:31581`. Thus two is a verified source-cluster count, not evidence for two JC14 strains or two independent biological genomes. Similar assembly statistics do not prove cross-accession identity. The live GTDB tree/genome pages were unavailable; the complete pinned native metadata supplied the membership check.

The complete BacDive native object at `data/bacdive/records.jsonl.gz:22965` and [BacDive 23162](https://bacdive.dsmz.de/strain/23162) identify JC14, type strain, DSM 25782 / CSUR P158 / JCM 30543, but classify the entry at species taxid 1464554. `data/raw/bacdive_strains.tsv:22966` preserves that placement. The parent YAML was read in full as relationship context and contains this strain with its source-backed assembly, IMG, BV-BRC, GOLD and StrainInfo relationships. The target's zero strain count therefore follows the documented subtree rule; parent-filed strains are not copied downward by designation alone. This is not a finding of missing BacDive coverage.

[LPSN 790606](https://lpsn.dsmz.de/species/aeromicrobium-massiliense) confirms the species' valid/correct name, type designations and 16S accession JF824798. [DSMZ DSM 25782](https://www.dsmz.de/collection/catalogue/details/culture/DSM-25782) supports JC14 and its deposits. The [primary description, PMID 23408663, DOI 10.4056/sigs.3306717](https://pmc.ncbi.nlm.nih.gov/articles/PMC3569385/) was inspected for identity, provenance and genome-project sections: it connects JC14, CSUR P158 and DSM 25782, gives a Senegalese fecal specimen subsequently processed in Marseille, and links the draft genome to CAHG00000000. Its project table explicitly describes a draft despite broader wording in the abstract. The collection page gives sampling year 2011 while the paper describes isolation in December 2010. Preserve those source dates rather than silently reconciling them. The assembly's France:Marseille locality likewise must not silently replace the paper's specimen origin. No phenotype values are added to this taxon record.

Live exact-taxid searches returned one Assembly entry and 43 Nuccore records. The initial 20-item sequence page was followed by a complete 43-ID search and summaries, so pagination was not mistaken for total coverage. The entries include WGS masters/components, marker sequences and patent sequences, not 43 genomes. The separately inspected GenBank XML for [JF824798.1](https://www.ncbi.nlm.nih.gov/nuccore/JF824798.1) is a 1,468-base partial 16S sequence explicitly identifying JC14, taxon 1033730 and type material. Its references include the primary description, a culturomics publication and direct submission on 2011-04-18. The other patent texts and every sequence's full annotations were not reviewed.

[Current NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000312105.1/dataset_report), Assembly ESummary and full local objects at `data/catalog/ncbi_genbank-0000.jsonl.gz:7773` / `ncbi_refseq-0000.jsonl.gz:6672` agree on GCA/GCF_000312105.1, ASM31210v1, JC14, SAMEA2272444, GenBank project PRJEA82327, WGS CAHG00000000.1, 18 contigs and five scaffolds. Total length is 3,322,119; ungapped length 3,314,828. This is a current scaffold assembly from type material, not a complete chromosome. The Datasets ANI field reports a below-threshold comparison but explicitly explains that no match is expected for the type strain; it is not grounds to reclassify JC14 as its nearest reported species.

Historical objects at `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:2642` and `ncbi_refseq_historical-0000.jsonl.gz:1909` retain GCA/GCF_000285435.1, ASM28543v1, SAMEA2272569, WGS CAEF00000000.1, 1,274 contigs and 6,759,256 bases. Both are suppressed, with contamination/oversize flags; the GenBank and RefSeq non-live dates are 2025-04-03 and 2014-04-04 respectively. BV-BRC native objects `bvbrc-0000.jsonl.gz:3184` and line 3185 distinguish genome 1033730.3 / the old assembly from 1033730.6 / GCF_000312105.1. Preserve historical assertions and statuses; do not equate the two assemblies merely because they share a strain name.

Full GOLD objects were inspected. `organisms.jsonl.gz:13947`, `projects.jsonl.gz:13492`, `analyses.jsonl.gz:52254` connect DSM 25782, Go0016397, Gp0016397, Ga0097816, GCA_000285435.1 and IMG 2636416159. The separate objects at organism line 80159, project line 91450 and analysis line 70705 connect Go0140204, Gp0145307, Ga0123969, GCA_000312105.1 and IMG 2802429300, without an organism culture-deposit field. The native workbook has two target-taxid organisms; that does not retroactively change the KGX-derived attestation count of one. Species-level Go0614975 / JCM 30543 and Go0614976 / CSUR P158 were also inspected. GOLD's live page was unavailable; native objects supplied the evidence. Go/Gp/Ga identifiers are related records, not genomes.

The complete StrainInfo object at `data/straininfo/records.jsonl.gz:303158` is SI-ID 405269, DOI 10.60712/SI-ID405269.3, BacDive 23162, with available own deposit DSM 25782 / SI-DP 912475 at species 1464554. It has no sequence array. Its aliases do not supply extra sequence links. The species-level SeqCode native entry at `data/seqcode/names.jsonl.gz:1379` is name 1613, not an independently asserted strain mapping.

## Completeness

Ignored-inclusive compressed searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, JC14 separator forms and species name/slug searches returned 74 lines. Expanded deposit, marker, WGS and exact BioSample searches returned 48 lines. Structured SOURCE.json searches found no matching manifest evidence. Full relevant native objects, including candidate false positives, were inspected.

Mycobacterium sp. JC-14 (135013), Rhizobium sp. JC14 (1284087) and Listeria monocytogenes JC14 (including GCA_043286645.1) are separate identities. Expanded WGS matching also found longer accessions containing CAHG as a substring in Escherichia, Campylobacter, Neisseria, Salmonella and Acinetobacter objects; none is the complete CAHG accession. Their metadata supplied no target link.

ATB rows at `data/catalog/allthebacteria.tsv.xz:65098` and line 1028932 are unrelated: SAMEA1033730 / ERR068091 / ERZ3069211 is Streptococcus pneumoniae, and SAMN02415072 / SRR1033730 / ERZ4056613 is Acinetobacter baumannii 70136. BioSample and run suffixes are not taxon joins. The first has an available FASTA and CHECKM2_MAX_CONTAM HQ flag; the second has available FASTA and PASS filters. Non-HQ status alone is not the rejection reason. Species-name row 3110463 is SAMN44680574 / SRR31343532, ASM_LEN and FASTA unavailable, with no strain evidence; it is not eligible genome evidence. No exact SAMEA2272444 or SAMEA2272569 ATB match was found in the ignored-inclusive catalog search.

Optional literature, phenotype, dataset and graph fields are not required. Genome/deposit information exists in the parent record under the source's classification; its absence from the child is not corrected by a reverse taxonomic join. The parent was inspected only as context, not assigned a new review verdict here.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: species-to-strain mapping is promoted to exact identity.** Target line 43 carries a GTDB-species closeMatch, line 46 introduces the bare species as an EXACT_SYNONYM, and line 54 places the species ID in equivalence `xrefs`. The target's own rank and parent distinguish JC14 from species 1464554. Native GTDB metadata covers the species cluster across both taxids, and the species-level mapping already exists. `src/taxonmech/seed.py:451` treats every closeMatch as identity without a rank check; lines 467-469 then create the xref and exact synonym. The schema describes closeMatch here as same-species correspondence and xrefs as true equivalences. Membership/type-strain status does not make a strain and its species interchangeable. This is a semantic harmonization defect despite schema-valid, source-reproducing fields. Owners: the upstream kg-microbe GTDB species mapping consumed by `src/taxonmech/extract.py:501`, and the identity-promotion rule in `src/taxonmech/seed.py:451`. Do not patch the generated YAML or hand-change the derived TSV.

## Recommended Edits

1. Correct the upstream strain-level GTDB mapping or represent it explicitly as a non-equivalence with source-to-target direction documented. Preserve the species-level mapping at 1464554. Add a rank-aware seeder safeguard so species-to-strain mappings cannot generate exact species synonyms or equivalence xrefs. Do not blindly substitute broadMatch: its documented direction here means the NCBI target is broader, which is the opposite of this case.
2. Keep the verified GTDB count of two scoped to the source species. Do not relabel it as two JC14 genomes or reduce it to one without an explicit change to what is being counted. Retain the NCBI identity, lineage, source synonym and source-count provenance.

## Follow-up Checks

Add focused regression tests with this strain, its parent and the two native GTDB members: the parent must retain its supported species mapping, the strain must not acquire an exact species synonym/equivalence xref, and counts must retain their declared source scope. After maintained upstream changes, re-extract through `scripts/extract_source_inventory.py`, run seed dry-run and single-record canaries for both taxids, inspect emitted files, then open/strict validation and full reproduction/QC. Review wider impact of the shared identity-promotion rule before bulk regeneration. No curation or regeneration was performed here.

## Additional Notes

iModulonDB was not applicable: the YAML contains no gene, locus, regulator, pathway or expression-module assertion. No paid research, contact, GitHub mutation, history write or status promotion occurred. All work remained in the original worktree; Eukaryota was not revisited. Cached legacy-browser rank, draft/complete wording, locality/date differences and suppressed historical assemblies were preserved as source context rather than silently resolved.
