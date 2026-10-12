# YAML Record Review: Alvinella pompejana symbiont APG1Bstab3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab3.yaml`
- Started UTC: 2026-10-07T04:06:32Z
- Finished UTC: 2026-10-07T04:08:26Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103553`, `Alvinella pompejana symbiont APG1Bstab3`. It asserts SPECIES in BACTERIA, parent `NCBITaxon:122728`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. Synonyms, nomenclature, mappings, strains, genomes, literature and graphs are not asserted.

The target denotes a bacterial symbiont taxon, not the Alvinella host or another APG1B clone. Generated YAML is read-only; maintained inventories, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future fixes.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab3.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab3.yaml --out /private/tmp/apg3-strict.tsv`: exit 0, one file, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, seven-inventory, path/scope and attestation comparisons passed. These are bounded source checks, not corpus reproduction.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, complete marker metadata except bases, independent genome Datasets and primary-source checks completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- No graph node requires `just validate-products`. Full history validation was not run; no external target history reference or lifecycle promotion applies.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:18505` matches ID, label, rank, parent, code and snapshot 2026-09-13. Synonym and retirement fields are empty. Complete native scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38513` matches and has empty unique_name.

All six pinned ancestors agree in order, ID, label and rank: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Campylobacterota 29547; unclassified Campylobacterota 122728.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103553&retmode=xml) confirms identity, lineage and code. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103553) confirms all ancestor IDs including root. Creation is 2 September 1999, update 19 January 2005. No OtherNames or type assertion appears; exact pinned type-material, merged-ID and dropped scans find no target row.

NCBI's unclassified placement is correctly carried without inferred intermediate ranks. SPECIES does not establish formal nomenclatural standing or a culture deposit. EXACT identifies this taxon, not every related community sequence.

## Evidence

`data/taxa/PATHS.tsv:14601` and `curation/seed_scope.tsv:144151` uniquely match identifier, stem and reason. The NCBITAXON attestation correctly counts one NAME.

No direct target children occur in the complete pinned backbone. Exact scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories find no target entry. Strain_count 0 is supported as an inventory count, not a biological assertion that cultivation is impossible.

All three manifests were parsed in full: raw extracted_at 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z. The newest-manifest rule at `src/taxonmech/seed.py:139` explains the seed event at 17:54:04Z. Event sources and scope reason agree. Hashes were not recomputed.

Exact nuccore search returned only UID 5901790. Complete [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=5901790) identifies `AF180317.1`, a 173-base partial 16S rRNA marker, taxon:103553 and clone APG1Bstab3. There are no strain, deposit, BioSample, BioProject, assembly, explicit host, location or isolation_source qualifiers. A host-associated name is not an independently grounded host CURIE.

The marker cites Campbell and Cary, AEM 67(1):110-117 (2001), PMID:11133434; an unpublished comparison of molecular methods; and direct submission on 24 August 1999 from the University of Delaware. The unpublished title supplies no verified experiment.

The inspected [primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC92526/), DOI:10.1128/AEM.67.1.110-117.2001, includes AF180317 in its DGGE-product accession series. This supports community provenance, not transfer of spirochete-specific observations or broad physiological claims to APG1Bstab3.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103553/dataset_report) returned an empty object. This is bounded coverage evidence, not universal genome absence; a partial 16S sequence is not a genome.

All 28 fresh `kg-microbe-sources imodulondb datasets` rows were read through `uv run --offline --project ../../culturebotai-claw` before web search. No covered organism matches and no gene/module is asserted, so component queries are not applicable. Noncoverage is not negative biological evidence.

## Completeness

No consequential gap was established. Definitions, nomenclature, taxonomy mappings, strain lists, evidence and graphs are optional here. Marker/literature context is optional enrichment. A clone designation alone is not evidence of a deposited culture.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched numeric-boundary 103553, exact label, stem and APG1Bstab3 punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 37 matched rows were fully read: three relevant identity/scope rows and 34 unrelated rows.

A separate AF180317/version scan returned zero rows in those roots. At both stages all five SOURCE.json files were parsed in full and history filenames searched independently of ignores. The initial BacDive requested-ID/URL match denotes native BacDive 103553, not NCBITaxon:103553. No target history filename was found. An ignored-inclusive report filename search found no earlier target report. Absence conclusions are limited to these repository roots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, source count and SEEDED lifecycle are supported. No missing required representation was established.

## Recommended Edits

None required. Preserve generated YAML and SEEDED status.

Future enrichment belongs in maintained sources/extractors and inventories or tested `src/taxonmech/seed.py` changes. Identity corrections belong upstream and scope corrections in `curation/seed_scope.tsv`. Do not manufacture strain/genome links from numeric overlap or grouped source entries.

## Follow-up Checks

For authorized enrichment, require whole-accession provenance and clone-specific evidence, independently ground any host, and rerun target schema/strict checks followed by documented corpus reproduction/provenance gates. Keep taxon, clone, host, strain, deposit, marker, sample, run, assembly, genome and project identities distinct. No unresolved blocker requires enrichment now.

## Additional Notes

All candidate native records and TSV columns were read losslessly. A long StrainInfo row was reread with all 153 sequence entries in a compact lossless representation after display truncation.

- BacDive 103553 is Corynebacterium pseudodiphtheriticum STI10087, taxon 37637: raw row 27687/native row 27686. This resolves the SOURCE.json request match.
- CIP 103553 is Bacillus acidovorans Pan 2, taxon 33017, BacDive 139212, ATCC 51158: raw row 61511/native 61510, culture row 43886. StrainInfo SI-ID45272/SI-DP148680 appears at native 33365, strain-links 25590, related rows 62023/62025. Its strain-level classification is broader Bacillus 1386; the CIP deposit names B. acidovorans. Neither classification is the target.
- DSM 103553 is Staphylococcus hominis H69, taxon 1290, BacDive 158003: raw row 80242/native 80241, culture row 59674; StrainInfo native 299885, strain-links 56901, related rows 133988/133989, SI-ID401996/SI-DP908968. Its unversioned GCA_001650655 and IMG 2675903233 links concern H69, not APG1Bstab3.
- StrainInfo native 26700 has KY103553, a ribosomal marker for Hanseniaspora uvarum CBS 279, taxon 29833, SI-ID38292. Native 26712 has SI-DP103553 for E. coli ATCC 23977, taxon 562, SI-ID38311.
- StrainInfo native 67609 is Prochlorococcus marinus MED4, taxon 1219, SI-ID87779. The hits are sequence number 103553 in patents EP2096177 and EP2199304, accessions HB970878 and HD028288, explicitly linked to CCMP1986/SI-DP527925. Its unversioned GCA_000011465 is also linked to CCMP1986, not all grouped deposits and certainly not this symbiont.
- CP103553 belongs to Klebsiella pneumoniae 2791, taxon 573, GCA_024918075.1, SAMN28174007: BV-BRC shard 0024 rows 37626/37881 and GOLD analysis 401969, Ga0608819/Gp0745359. GOLD IDs are related records, not target genome identifiers.
- MGBC103553 is uncultured Lachnospiraceae bacterium 297314, GCA_948793465.1, SAMEA112377495: BV-BRC shard 0018 row 177 and GenBank shard 0060 row 30358.
- ASM103553v1 denotes Pseudomonas aeruginosa Pae_CF67.09n, taxon 287, GCA/GCF_001035535.1, SAMN03566398: GTDB shard 0013 row 32517, RefSeq shard 0000 row 30460 and GenBank shard 0000 row 36055.
- GTDB shard 0007 row 14138 is Mycobacterium tuberculosis GCF_900120745.1 with contig N50 103553. Shard 0003 row 48516 is Flavobacterium psychrophilum GCF_965135645.1 with scaffold N75 103553; shard 0000 row 1243 is E. coli GCF_900481575.1 with scaffold N75 103553.
- GenBank shard 0022 row 823 is Shigella sonnei PNUSAE103553, taxon 624, GCA_023794855.1, SAMN28960690. Shard 0007 row 34804 is Salmonella enterica PNUSAS103553, taxon 28901, GCA_008795055.1, SAMN12875734. Shard 0011 row 8597 is E. coli isolate 103553, taxon 562, GCA_012448125.1, SAMN12731527.
- AllTheBacteria row 6149 is E. coli O26:H11, DRR103553, SAMD00075896, ERZ25075533. Available FASTA, PASS filters, source URLs and SeqKit sum establish no target relationship.

Only this new report was written for this target. No YAML, inventory, generated product, prior report, history or lifecycle state changed. Eukaryota reviews were not reopened. No paid research, external contact or GitHub mutation occurred.
