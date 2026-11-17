# YAML Record Review: Alvinella pompejana symbiont APG1Bstab5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab5.yaml`
- Started UTC: 2026-10-07T03:36:18Z
- Finished UTC: 2026-10-07T03:41:04Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103547`, `Alvinella pompejana symbiont APG1Bstab5`: SPECIES in BACTERIA, parent `NCBITaxon:38780`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, literature, discussions or graphs are asserted.

This is the bacterial symbiont taxon, not its eukaryotic host. The YAML remains read-only. Maintained source inputs, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future changes.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab5.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab5.yaml --out /private/tmp/apg5-strict.tsv`: exit 0, one file scanned, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, path/scope, seven-inventory and attestation comparisons passed. These bounded comparisons are not corpus reproduction.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, complete marker metadata excluding bases and independent genome Datasets reads completed.
- Inspected the primary paper's publisher text, including accession section, methods, results and discussion. PMC and direct PubMed web opens returned browser challenges; publisher text supplied the applicable paper content.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable graph node and was not run. Full history validation was not run; no external target history reference, history event or lifecycle promotion applies.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:18499` agrees on ID, label, rank, parent, code and snapshot 2026-09-13; synonyms and retirement are empty. Complete native scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38507` agrees and has no unique-name qualifier.

All nine pinned ancestor IDs, labels and ranks match: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Spirochaetota 203691; Spirochaetia 203692; Spirochaetales 136; Spirochaetaceae 137; unclassified Spirochaetaceae 38780.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103547&retmode=xml) agrees on identity, code and named lineage. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103547) confirms all ancestor IDs including root. Taxonomy creation is 2 September 1999 and update is 19 January 2005. No OtherNames or type-material assertion is supplied. Complete exact scans of pinned merged-ID, dropped and type-material tables found no target row.

NCBI species rank does not establish formal nomenclatural standing, a cultured isolate, or a genome. EXACT grounding identifies this NCBI node; it does not make host, clone, strain and taxon interchangeable. No host CURIE or equivalence to another bacterial phylotype is inferred.

## Evidence

Path row `data/taxa/PATHS.tsv:14595` and scope row `curation/seed_scope.tsv:144145` uniquely match the ID, stem and seed reason. The attestation correctly counts one NAME.

There are no direct children in the complete pinned backbone. Full exact scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Strain_count 0 agrees with the BacDive inventory and target subtree; it is an upstream record count, not a claim that this organism can never be cultured.

Fresh structured reads of all three complete manifests give extracted_at values raw 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z. The inspected newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed event. Source list and scope reason agree. Hashes were not recomputed.

Exact nuccore search returned one UID, 5901785. Complete [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=5901785) identifies `AF180312.1`, a 197-base partial 16S rRNA marker, taxon:103547, with clone qualifier APG1Bstab5. It does not supply a strain qualifier, culture deposit, BioSample, BioProject or assembly link, nor an explicit host, location or isolation_source qualifier. The organism label itself names the association.

The sequence cites Campbell and Cary, AEM 67(1):110-117 (2001), PMID:11133434, plus an unpublished comparison of molecular methods and a direct submission dated 24 August 1999 from the University of Delaware. The unpublished item is not independent inspected experimental evidence.

The [primary paper](https://journals.asm.org/doi/full/10.1128/aem.67.1.110-117.2001), DOI:10.1128/AEM.67.1.110-117.2001, assigns AF180311-AF180319 to DGGE amplification products, distinct from APG10's AF180309. Its APG1B sample came from the Elsa vent in 1991. The study distinguishes spirochetes A and B and reports method-dependent community frequencies. Its proposed fermentative role remains an interpretation, not a demonstrated APG1Bstab5 phenotype. This supports marker provenance without merging NCBI nodes, imposing the paper's historical genus placement, or transferring host/community properties to the target.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103547/dataset_report) returned an empty object. These bounded results do not prove universal genome absence; the partial marker is not a genome.

Before web search, read all 28 rows of the current-turn `kg-microbe-sources imodulondb datasets` response through `uv run --offline --project ../../culturebotai-claw`. No covered organism matches this target, and no gene/module is asserted. iModulonDB is not applicable; no component query applies, and noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, mappings, deposits and graphs need not be populated without applicable support. The marker and paper are possible future enrichment, not missing required fields. A clone qualifier alone does not establish a source-inventoried culture or strain-genome relationship.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched numeric-boundary 103547, the full label, stem and APG1Bstab5 punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 32 matched lines were read losslessly, not judged from projections.

A separate AF180312/version scan returned zero lines in those roots. At both stages all five SOURCE.json documents were parsed separately in full and history filenames searched without ignore filtering. The initial metadata match is a BacDive fetch of native ID 103547, resolved below; it is not NCBITaxon:103547. No target history filename was found. These are bounded repository checks, not global absence claims.

No consequential omission was established. Eukaryota records were not re-reviewed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Database-number collisions do not supply target identity or enrichment evidence.

## Recommended Edits

None required. Preserve generated YAML and SEEDED state.

Future enrichment belongs in a maintained source/extractor and inventory, or tested harmonization changes in `src/taxonmech/seed.py`; scope changes belong in `curation/seed_scope.tsv`. Correct source/kg-microbe mappings upstream. Preserve taxon, host, clone, strain, deposit, marker, sample, assembly, genome, run and project distinctions. Do not add APG10 or another community member as an exact synonym solely from this literature context.

## Follow-up Checks

For later authorized curation, establish whole-accession source chains, rerun target schema/strict validators and then documented full-corpus reproduction/provenance gates. Any host grounding requires independent authority resolution; any clone-to-strain or genome link requires explicit source evidence. A marker accession must remain outside genome counts. No unresolved blocker requires enrichment now.

## Additional Notes

All unrelated candidate rows were fully read. Row addresses below refer to decompressed logical lines where applicable.

- CIP 103547 belongs to Citrobacter freundii taxon 546: raw BacDive row 4222, culture-collection row 43880, strain-related rows 363365-363366; BacDive native row 4221, StrainInfo native row 30320, strain-links row 89001 and related-record rows 215120/215130. The chain is BacDive 4326, SI-ID 42090, SI-DP 149876 and GOLD Go0203562; GOLD organism row 141760 confirms the different taxon.
- Native BacDive 103547 is Agromyces sp. ST001850, taxon 51513: raw row 27681 and native row 27680. This resolves the SOURCE.json requested-ID/URL match independently of the NCBI namespace.
- DSM 103547 belongs to Massilia buxea A9, taxon 1949069: raw BacDive row 80915, native row 80914, culture-collection row 59670, type-material rows 74185-74186 and LPSN rows 5616/32383. Its Pseudoduganella synonym, type deposits and genomes are unrelated.
- StrainInfo native row 131764 contains marker KY103547 for Hanseniaspora pseudoguilliermondii CBS 8772, SI-ID 179715, SI-DP 457032. It is neither the bacterial target nor grounds to reopen Eukaryota reviews.
- BV-BRC shard 0022 rows 3818/4269 and GOLD analysis row 401967 contain CP103547 within Escherichia coli 3036 assembly GCA_024918035.1, taxon 562. GOLD Ga0608817/Gp0745324 are related identifiers, not target genomes.
- BV-BRC shard 0013 row 46950, GTDB genome shard 0017 row 19075 and NCBI GenBank shard 0060 row 32232 identify MGBC103547, GCA_948812205.1, SAMEA112377489 and taxon 2301481, an uncultured Muribaculaceae MAG. GTDB's UBA3263 classification is not a target mapping.
- BV-BRC shard 0027 row 2808 and NCBI GenBank shard 0065 row 11094 identify MarMAG_103547, GCA_977624755.1, SAMEA120729206 and taxon 77133, a different metagenomic record.
- AllTheBacteria row 6143 contains run DRR103547 for E. coli O26:H11, sample SAMD00075890 and analysis ERZ25075523. Its available FASTA and PASS filters do not establish a target association.

Only this new report was written. No YAML, inventory, generated product, earlier report, history or lifecycle state was changed. No paid research, external contact or GitHub mutation occurred.
