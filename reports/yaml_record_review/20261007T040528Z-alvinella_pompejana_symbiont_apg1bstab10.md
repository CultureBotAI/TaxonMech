# YAML Record Review: Alvinella pompejana symbiont APG1Bstab10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab10.yaml`
- Started UTC: 2026-10-07T04:03:35Z
- Finished UTC: 2026-10-07T04:05:28Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103552`, `Alvinella pompejana symbiont APG1Bstab10`: SPECIES, BACTERIA, parent `NCBITaxon:122728`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, strains, genomes, literature or causal graphs are asserted.

This bacterial symbiont taxon is not the host, APG1Bstab1, or the similarly numbered spirochete clone APG10. Generated YAML is read-only. Maintained inventories, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future corrections.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab10.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab10.yaml --out /private/tmp/apg10-strict.tsv`: exit 0, one file, zero errors. Read the actual header-only TSV.
- Complete backbone, lineage, seven-inventory, path/scope and attestation comparisons passed; these are bounded checks, not corpus reproduction.
- Live taxonomy XML/Datasets, exact Assembly/nuccore queries, complete marker metadata except bases, independent genome Datasets and primary-paper checks completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` is not applicable without graph nodes. Full history validation was not run. No external target history reference or lifecycle promotion applies.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:18504` agrees on ID, label, rank, parent, genetic code and snapshot 2026-09-13; synonym and retirement columns are empty. Complete native scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38512` agrees and has empty unique_name.

All six pinned ancestors match in order, ID, label and rank: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Campylobacterota 29547; unclassified Campylobacterota 122728.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103552&retmode=xml) confirms the identity, rank, lineage and code. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103552) confirms the ancestor IDs including root. Creation is 2 September 1999 and update 19 January 2005. No OtherNames or type-material claim appears; pinned type-material, merged-ID and dropped scans find no exact target row.

The unclassified position is NCBI's carried hierarchy, not a missing inferred placement. SPECIES is a taxonomic rank, not evidence of formal nomenclatural standing or a deposited strain. EXACT grounds this taxon, not other organisms in the same source community.

## Evidence

`data/taxa/PATHS.tsv:14600` and `curation/seed_scope.tsv:144150` uniquely agree on identifier, stem and scope reason. The one NCBITAXON attestation correctly counts one NAME.

The complete pinned backbone has no direct target children. Exact scans of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found no target entries. Strain_count 0 is consistent with inventory and subtree, not a claim of biological unculturability.

All three source manifests were parsed in full: raw extracted_at 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z. The newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed event. Scope reason and attested source match. Hashes were not recomputed.

Exact nuccore search returned only UID 5901789. Complete [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=5901789) identifies `AF180316.1`, a 171-base partial 16S rRNA marker, taxon:103552 and clone APG1Bstab10. No strain, deposit, BioSample, BioProject, assembly, explicit host, location or isolation_source qualifier is supplied. The host association in the name is not an independently grounded host CURIE.

The marker references Campbell and Cary, AEM 67(1):110-117 (2001), PMID:11133434; an unpublished comparison of molecular methods; and direct submission on 24 August 1999 from the University of Delaware. No experimental claim is inferred from the unpublished title.

The inspected [primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC92526/), DOI:10.1128/AEM.67.1.110-117.2001, places AF180316 in its DGGE-product series. Its spirochete A is APG10/AF180309, not APG1Bstab10. The paper supplies community provenance, not target-specific phenotype or genome evidence.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103552/dataset_report) returned an empty object. These bounded queries do not establish universal genome absence; a short marker is not a genome.

Before web search, all 28 rows from fresh `kg-microbe-sources imodulondb datasets` output were read using `uv run --offline --project ../../culturebotai-claw`. No covered organism matches; no gene or module is asserted. Component queries are not applicable, and noncoverage is not negative biological evidence.

## Completeness

Optional definitions, nomenclature, mappings, strain/deposit links, evidence and graphs need not be invented. Marker/literature context is optional enrichment, not a missing required field. A clone designation does not imply a culture collection.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched numeric-boundary 103552, exact label, stem and APG1Bstab10 punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 44 matched rows were read losslessly: three applicable identity/scope rows and 41 unrelated rows.

A separate AF180316/version scan found zero rows in those roots. At both stages all five SOURCE.json files were parsed in full and history filenames searched independently of ignore rules. The initial BacDive requested-ID/URL match is native ID 103552, not NCBITaxon:103552. No target history filename was found. An ignored-inclusive report filename search found no earlier target report. These are bounded repository searches, not global absence assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, source attestation, inventory count and SEEDED lifecycle are supported. No consequential omission was established.

## Recommended Edits

None required. Preserve generated YAML and SEEDED status.

Future enrichment belongs in maintained sources/extractors and inventories or tested `src/taxonmech/seed.py` changes. Upstream identity corrections belong at their source; scope changes belong in `curation/seed_scope.tsv`. Do not equate APG10 with APG1Bstab10 or use numeric collisions to create strain/genome relationships.

## Follow-up Checks

For authorized enrichment, verify whole-accession source chains and any host grounding, and require clone-specific support for phenotypes. Rerun target schema/strict checks and then documented corpus reproduction/provenance gates. Preserve distinctions among taxon, host, clone, strain, deposit, marker, sample, run, assembly, genome and project. No unresolved blocker requires enrichment now.

## Additional Notes

All unrelated rows were fully inspected. Logical decompressed row addresses follow.

- Native BacDive 103552 is Corynebacterium pseudodiphtheriticum, taxon 37637, STI10128(IMET), CPAg: raw row 27686/native 27685. This resolves the SOURCE.json request match.
- CIP 103552 is Bacillus acidovorans 33017, Pro 1, BacDive 135136, ATCC 51159: raw row 57442/native 57441, culture row 43885. StrainInfo SI-ID42835/SI-DP148679 occurs at native 31038, strain-links 17829 and related rows 43878/43880. StrainInfo's strain-level classification is the broader Bacillus 1386, while the CIP deposit names B. acidovorans. Its X77789 marker explicitly names ATCC 51159, not the CIP deposit. These are unrelated identities, not target support.
- DSM 103552 is Tidjanibacter massiliensis 1871003, Marseille-P3084, BacDive 159906: raw row 82143/native 82142, culture row 59673; StrainInfo SI-ID400831/SI-DP907719, native 298720, strain-links 58881 and related rows 138570/138571. NCBI type-material rows 66203/66204 classify DSM 103552 as type material, but BacDive and StrainInfo carry negative type flags. Preserve that unrelated conflict. LT598563, unversioned GCA_900104605 and IMG 2788499931 concern Marseille-P3084, not APG1Bstab10.
- StrainInfo native 129859 contains KY103552, a Hanseniaspora uvarum CBS 2588 ribosomal marker, taxon 29833, SI-ID177790. Reading this collision did not reopen a Eukaryota taxon review.
- CP103552 belongs to Klebsiella pneumoniae 2791, taxon 573, GCA_024918075.1, SAMN28174007: BV-BRC shard 0024 rows 37626/37881 and GOLD analysis 401969. Ga0608819/Gp0745359 are related GOLD records, not target genome IDs.
- MGBC103552 is uncultured Prevotellamassilia 1926676, GCA_948814945.1, SAMEA112377494: BV-BRC shard 0008 row 38260, GTDB shard 0015 row 48101 and GenBank shard 0060 row 32506. GTDB's Alloprevotella placement is not a target mapping.
- MarMAG_103552 is uncultured bacterium 77133, SAMEA120729219: BV-BRC shard 0027 row 2095 and GenBank shard 0065 row 8810. GenBank supplies GCA_977601875.1; the native BV-BRC row has no assembly_accession field.
- ASM103552v1 denotes Pseudomonas aeruginosa Pae_CF67.09m, taxon 287, GCA/GCF_001035525.1, SAMN03566397: GTDB shard 0007 row 14096, RefSeq shard 0000 row 30459 and GenBank shard 0000 row 36054.
- Six GTDB matches are contig/scaffold N50 values, not identifiers: shard 0004 row 26998, GCF_001482795.1 (Elizabethkingia); shard 0003 row 22958, GCF_036990845.1 (Aeromonas); shard 0007 row 27246, GCF_004766955.1 (E. coli); shard 0014 row 6856, GCF_002001105.1 (Rhodanobacter); shard 0008 row 7553, GCF_042746285.1 (Streptomyces); shard 0011 row 42525, GCF_028128955.1 (Bradyrhizobium).
- GenBank shard 0007 row 34670 is Salmonella enterica PNUSAS103552, taxon 28901, GCA_008791345.1, SAMN12875682. Shard 0024 rows 6566/6586 are Shigella flexneri 103552_I/103552_II, taxon 623, GCA_026021235.1/GCA_026021655.1, SAMEA8901042/SAMEA8901043.
- AllTheBacteria row 6148 is E. coli O26:H11, DRR103552, SAMD00075895, ERZ25075532. Row 1199902 is Shigella boydii, SRR4897332, SAMN05980536, ERZ9479129; 103552 occurs inside its SeqKit sum. Available FASTA and PASS filters do not establish a target relationship.

Only this new report was written for this target. No YAML, inventory, generated product, prior report, history or lifecycle state changed. Eukaryota records remain untouched. No paid research, contact or GitHub mutation occurred.
