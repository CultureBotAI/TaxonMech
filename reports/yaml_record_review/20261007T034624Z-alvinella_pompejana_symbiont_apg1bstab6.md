# YAML Record Review: Alvinella pompejana symbiont APG1Bstab6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab6.yaml`
- Started UTC: 2026-10-07T03:43:37Z
- Finished UTC: 2026-10-07T03:46:24Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103548`: SPECIES in BACTERIA, parent `NCBITaxon:122728`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, literature, discussions or graphs are asserted.

This record denotes a bacterial symbiont, not the Alvinella host, and is distinct from APG1Bstab5. The YAML is generated and remains read-only; maintained inventories, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future changes.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab6.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab6.yaml --out /private/tmp/apg6-strict.tsv`: exit 0, one file scanned, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestors, seven source inventories, path/scope and attestation comparisons passed. These bounded checks are not a reproduction of the corpus.
- Live NCBI taxonomy XML/Datasets, exact Assembly/nuccore queries, full marker metadata except sequence bases, and independent genome Datasets reads completed.
- The structured iModulonDB request initially failed DNS in the sandbox; the network-enabled retry completed. No unresolved adapter failure remains.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable graph node and was not run. Full history validation was not run. No target external history reference, new history event or lifecycle promotion applies.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:18500` agrees on ID, label, SPECIES rank, parent, code and snapshot 2026-09-13. Synonyms and retirement are empty. Native scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38508` independently agrees and has an empty unique_name.

All six pinned ancestors match in order, ID, label and rank: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Campylobacterota 29547; unclassified Campylobacterota 122728.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103548&retmode=xml) agrees with the identity, code and named lineage. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103548) confirms all ancestor IDs including root. The node was created 2 September 1999 and updated 19 January 2005; no OtherNames or type-material assertion is supplied. Exact pinned type-material, merged-ID and dropped scans found no target row.

The short lineage faithfully carries NCBI's unclassified placement; missing class/order/family/genus entries are not invented gaps. NCBI species rank does not establish valid nomenclatural standing, a cultured strain or a genome. EXACT identifies this taxonomic node, not the host or neighboring clone.

## Evidence

`data/taxa/PATHS.tsv:14596` and `curation/seed_scope.tsv:144146` uniquely match ID, stem and seed reason. The one NAME attestation is supported by the backbone, not a count of strains or genomes.

There are no direct children in the complete pinned backbone. Complete exact scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found no target row. Strain_count 0 agrees with the BacDive inventory and target subtree; it is an upstream count, not a biological impossibility claim.

All three complete manifests were parsed this turn: raw extracted_at 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z. The inspected newest-manifest rule at `src/taxonmech/seed.py:139` explains the seed event's 17:54:04Z timestamp. Source list and scope reason match. Hashes were not recomputed.

Exact nuccore search returned only UID 5901784. Complete [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=5901784) identifies `AF180311.1`, a 172-base partial 16S rRNA marker, taxon:103548, clone APG1Bstab6. It supplies no strain, culture deposit, BioSample, BioProject, assembly, explicit host, location or isolation_source qualifier. The organism label names the association; the clone qualifier is not a culture-deposit identity.

The marker cites Campbell and Cary, AEM 67(1):110-117 (2001), PMID:11133434, plus an unpublished methodological comparison and a direct submission dated 24 August 1999 from the University of Delaware. The unpublished item is not inspected independent experimental evidence.

Inspected the [publisher's primary paper](https://journals.asm.org/doi/full/10.1128/aem.67.1.110-117.2001), DOI:10.1128/AEM.67.1.110-117.2001. Its accession section assigns AF180311-AF180319 to DGGE products. Methods place sample APG1B at Elsa vent in 1991; results distinguish epsilon-proteobacterial community bands from spirochete band 5. Thus a paper centered on spirochetes can validly cite this different community member. Neither the paper title nor community-level findings establish a spirochete identity, fermentative phenotype, abundance, thermotolerance or sulfur metabolism for APG1Bstab6.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103548/dataset_report) returned an empty object. These bounded checks do not prove universal genome absence, and the short marker must not enter genome counts.

Before web search, the successful `kg-microbe-sources imodulondb datasets` retry through `uv run --offline --project ../../culturebotai-claw` supplied 28 rows, all inspected. No target organism is covered and no expression module is asserted. iModulonDB is not applicable; noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, mappings, cultures and graphs need not be invented. The marker/paper is possible enrichment, not a missing required representation. Similar names and shared sampling context do not support equivalence to APG1Bstab5, APG10 or another epibiont.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched numeric-boundary 103548, exact label, stem and APG1Bstab6 punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed files. All 35 matched rows were read losslessly: three applicable identity/scope rows and 32 unrelated rows.

A separate AF180311/version search returned zero rows in these roots. At both stages all five SOURCE.json files were parsed separately in full and history filenames searched without ignore filtering. The initial BacDive requested-ID/URL match is native BacDive 103548, not NCBITaxon:103548. No matching target history filename was found. Absence statements are bounded to these checked sources.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The source classification and counts are internally consistent and supported; no consequential missing representation was established.

## Recommended Edits

None required. Preserve generated YAML and SEEDED state.

Future enrichment belongs in a maintained source/extractor and inventory, or tested seeder changes; source/kg-microbe identity corrections belong upstream, and scope changes belong in `curation/seed_scope.tsv`. Keep taxon, host, clone, strain, deposit, marker, sample, run, assembly, genome and project identities separate.

## Follow-up Checks

For later authorized enrichment, require explicit whole-accession source chains and clone-specific support, rerun the target schema/strict validators, then run documented full-corpus reproduction/provenance gates. Independently resolve host groundings. No unresolved blocker currently requires enrichment.

## Additional Notes

Unrelated candidates were read in full, including all TSV columns and native JSON fields; decompressed row addresses follow.

- CIP 103548 is Proteus mirabilis, taxon 584: raw BacDive row 4950, culture row 43881, strain-related rows 371510/371511; BacDive native row 4949; StrainInfo native row 9361, strain-links row 91038 and related rows 221117/221121. Its chain is BacDive 5059, SI-ID 9361, SI-DP 153966, GOLD Go0195955; GOLD organism row 134164 confirms the different identity.
- BacDive native ID 103548 is Agromyces sp. ST001862, taxon 51513: raw row 27682 and native row 27681. This resolves the SOURCE.json collision.
- StrainInfo native rows 26710, 60373 and 78023 concern, respectively, Pseudomonas putida ATCC 23975 with SI-DP 103548; Sclerotium wakkeri IMI 103548; and Pycnoporus sanguineus designation FP 103548-Sp. These provide no target culture evidence or reason to reopen completed Eukaryota reviews.
- BV-BRC shard 0024 rows 37625/37880 and GOLD analysis row 401968 contain CP103548 within Klebsiella pneumoniae 3987, taxon 573, GCA_024918055.1, SAMN28174045. Ga0608818/Gp0745311 are related GOLD IDs, not target genome IDs.
- MGBC103548 is Muribaculum intestinale taxon 1796646, GCA/GCF_948819415.1, SAMEA112377490: BV-BRC shard 0006 row 36735, GTDB shard 0001 row 14038, GenBank shard 0060 row 32953 and RefSeq shard 0010 row 9389.
- ASM103548v1 is Pseudomonas aeruginosa Pae_CF67.09k, taxon 287, GCA/GCF_001035485.1, SAMN03566395: GTDB shard 0003 row 19343, GenBank shard 0000 row 36052 and RefSeq shard 0000 row 30457.
- GenBank shard 0007 row 34773 is Salmonella enterica PNUSAS103548, taxon 28901, GCA_008794435.1, SAMN12875731.
- Four GTDB matches are assembly statistics equal to 103548, not IDs: shard 0005 row 3387 (GCA_948687905.1, scaffold N75); shard 0015 row 40765 (GCA_049281975.1, contig N50); shard 0000 row 40160 (GCF_019721995.1, contig N50); shard 0006 row 20046 (GCA_034122145.1, contig N50).
- AllTheBacteria row 6144 is E. coli O26:H11, run DRR103548, sample SAMD00075891, analysis ERZ25075529. Row 3209221 is S. aureus, sample SAMN47244108, run SRR32595955, analysis ERZ27147446, with 103548 embedded in its SeqKit sum. Both have available FASTAs and PASS filters; neither supports this target.

Only this new report was written. No YAML, inventory, generated product, earlier report, history, lifecycle state or GitHub item changed; no paid research or external contact occurred.
