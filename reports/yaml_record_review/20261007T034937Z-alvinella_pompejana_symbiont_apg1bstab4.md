# YAML Record Review: Alvinella pompejana symbiont APG1Bstab4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab4.yaml`
- Started UTC: 2026-10-07T03:47:25Z
- Finished UTC: 2026-10-07T03:49:37Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103549`, `Alvinella pompejana symbiont APG1Bstab4`: SPECIES in BACTERIA, parent `NCBITaxon:122728`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. Synonyms, nomenclature, mappings, deposits, genomes, literature, discussions and graphs are not asserted.

This is a bacterial taxon, not the Alvinella host. Its clone label does not make it interchangeable with other APG1B clones. Generated YAML is read-only; maintained source inputs, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future changes.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab4.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab4.yaml --out /private/tmp/apg4-strict.tsv`: exit 0, one file scanned, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, seven-inventory, path/scope and attestation comparisons passed. These checks do not reproduce the corpus.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, full marker metadata except bases and independent genome Datasets reads completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable graph node and was not run. Full history validation was not run. No external target history reference, history write or lifecycle promotion applies.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:18501` agrees on identity, rank, parent, code and snapshot 2026-09-13; synonym and retirement fields are empty. Complete native name row `data/catalog/ncbi_names-0000.jsonl.gz:38509` agrees, including scientific-name class and empty unique_name.

All six pinned ancestors match exactly in order, label and rank: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Campylobacterota 29547; unclassified Campylobacterota 122728.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103549&retmode=xml) agrees on identity, named lineage and code. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103549) confirms all ancestor IDs including root. The node was created 2 September 1999 and updated 19 January 2005; no OtherNames or type-material assertion is supplied. Exact pinned type-material, merged-ID and dropped scans found no target row.

The unclassified parent is carried from NCBI, not inferred. Missing intermediate ranks are not defects. SPECIES is NCBI's rank, not proof of valid nomenclature, culture availability or genome sequencing. EXACT grounding identifies this node only.

## Evidence

`data/taxa/PATHS.tsv:14597` and `curation/seed_scope.tsv:144147` uniquely match ID, stem and reason. The attestation correctly counts one NAME, not a strain or genome.

There are no direct children in the complete pinned backbone. Complete exact scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Strain_count 0 agrees with the source inventory and subtree; it does not assert biological unculturability.

All three manifests were parsed in full during this turn: raw extracted_at 2026-09-13T17:50:44Z, ATB 17:54:04Z, StrainInfo 17:29:00Z. The inspected newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed event. Its source list and scope reason agree. Hashes were not recomputed.

Exact nuccore search returned one UID, 5901786. Complete [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=5901786) identifies `AF180313.1`, a 172-base partial 16S rRNA marker, taxon:103549, clone APG1Bstab4. No strain, culture deposit, BioSample, BioProject, assembly, explicit host, location or isolation_source qualifier is supplied. The name itself indicates the host association, without grounding a host CURIE.

The marker cites Campbell and Cary, AEM 67(1):110-117 (2001), PMID:11133434; an unpublished methodological comparison; and direct submission on 24 August 1999 from the University of Delaware. No independent experiment is inferred from the unpublished title.

The [primary paper](https://journals.asm.org/doi/full/10.1128/aem.67.1.110-117.2001), DOI:10.1128/AEM.67.1.110-117.2001, was inspected this turn. Its accession section places AF180313 within the DGGE-product series; the study distinguishes community members. This supports marker provenance, not transfer of its spirochete findings to APG1Bstab4. Host-associated sampling does not establish this clone's metabolism or growth-temperature range.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103549/dataset_report) returned an empty object. These bounded queries do not prove universal genome absence. The 172-base marker is not a genome.

Before web search, read all 28 rows from the fresh `kg-microbe-sources imodulondb datasets` response through `uv run --offline --project ../../culturebotai-claw`. The target is not a covered organism, and no gene or expression module is asserted. No component query applies; noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, taxonomy mappings, cultures and graphs need not be populated without support. Marker/paper enrichment is optional and would require a maintained representation, not a hand edit of generated YAML. A clone qualifier is not an inventoried culture deposit.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched numeric-boundary 103549, exact label, stem and APG1Bstab4 punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 31 matched rows were read losslessly: three applicable identity/scope rows and 28 unrelated rows.

A separate AF180313/version scan returned zero rows in these roots. Both stages also parsed all five SOURCE.json files in full and searched history filenames without ignore filtering. Initial metadata matches were native BacDive requested ID 103549 and a StrainInfo response size of 103549 bytes; neither supplies taxon identity. No target history filename was found. These statements are bounded repository results, not universal absence claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Current identity, source counts and lifecycle state are supported. No consequential missing representation was established.

## Recommended Edits

None required. Preserve generated YAML and SEEDED state.

Any future enrichment belongs in a maintained source/extractor and inventory or tested `src/taxonmech/seed.py` change. Route source/kg-microbe identity fixes upstream and scope changes to `curation/seed_scope.tsv`. Keep taxon, host, clone, strain, deposit, marker, sample, run, assembly, genome and project identities distinct.

## Follow-up Checks

For later authorized enrichment, establish explicit whole-accession source chains, validate the single record with documented schema/strict commands, then run documented full-corpus reproduction/provenance gates. Independently resolve host groundings and require clone-specific evidence for phenotype claims. No unresolved blocker requires enrichment now.

## Additional Notes

All unrelated candidates were fully read, including native fields and every TSV column. Row addresses are decompressed logical lines where applicable.

- BacDive native ID 103549 is Agromyces sp. ST001848, taxon 51513: raw row 27683 and native row 27682. This resolves the SOURCE.json requested-ID match.
- CIP 103549 is unrelated Salmonella material: BacDive 136220, raw row 58525, native row 58524; culture row 43882; strain-related rows 105359/105360; GOLD Go0151787 at organism row 90103. Those inventories classify it as S. enterica, taxon 28901.
- StrainInfo native row 29470 instead carries the Salmonella genus, taxon 590, on SI-ID 41216, with the CIP deposit SI-DP 154803 lacking its own taxon. Strain-links row 19903 and related rows 48996/48997 accordingly have empty taxon_id. That source granularity is retained, not silently reconciled, and is not evidence for APG1Bstab4.
- StrainInfo native row 46494 concerns Hanseniaspora uvarum CBS 5914, taxon 29833, SI-ID 58825, SI-DP 282427, marker KY103549. Its unrelated fungal synonyms and deposit list do not affect this bacterial record or reopen Eukaryota reviews.
- CP103549 occurs in Klebsiella pneumoniae 3987, GCA_024918055.1, SAMN28174045, taxon 573: BV-BRC shard 0024 rows 37625/37880 and GOLD analysis row 401968. GOLD Ga0608818/Gp0745311 are related IDs, not target genomes.
- MGBC103549 is an uncultured Bacteroidales MAG, taxon 194843, GCA_948807495.1, SAMEA112377491: BV-BRC shard 0009 row 2429, GTDB shard 0017 row 10838 and GenBank shard 0060 row 31761.
- ASM103549v1 denotes Pseudomonas aeruginosa Pae_CF67.09l, taxon 287, GCA/GCF_001035495.1, SAMN03566396: GTDB shard 0004 row 10068, RefSeq shard 0000 row 30458 and GenBank shard 0000 row 36053.
- GenBank shard 0007 row 34586 is Salmonella enterica PNUSAS103549, taxon 28901, GCA_008789665.1, SAMN12875738.
- Three GTDB rows match assembly statistics, not identity: shard 0005 row 31168 (GCF_963977585.1, contig N50 103549); shard 0014 row 23378 (GCA_031979685.1, scaffold N75 103549); shard 0009 row 48276 (GCF_006233105.1, scaffold N75 103549).
- AllTheBacteria row 6145 is E. coli O26:H11, run DRR103549, sample SAMD00075892, analysis ERZ25075528. Row 2747897 is E. coli, sample SAMN38224734, run SRR26804220, analysis ERZ26643130, matching only its SeqKit sum. Both have available FASTAs and PASS filters; neither establishes a target link.

Only this new review report was written for this target. No YAML, inventory, generated product, earlier report, history or lifecycle state was modified. No paid research, external contact or GitHub mutation occurred.
