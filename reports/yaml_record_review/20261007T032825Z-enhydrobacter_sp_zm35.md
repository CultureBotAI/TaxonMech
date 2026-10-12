# YAML Record Review: Enhydrobacter sp. ZM35

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enhydrobacter_sp_zm35.yaml`
- Started UTC: 2026-10-07T03:26:01Z
- Finished UTC: 2026-10-07T03:28:25Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035439`, `Enhydrobacter sp. ZM35`: SPECIES in BACTERIA, parent `NCBITaxon:2632691`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, literature, discussions or graphs are asserted.

The YAML stays read-only. Maintained source inputs, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future changes, not generated artifacts.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/enhydrobacter_sp_zm35.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/enhydrobacter_sp_zm35.yaml --out /private/tmp/ez35-strict.tsv`: exit 0, one file scanned, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, path/scope, seven-inventory and attestation comparisons passed. These bounded checks do not reproduce the corpus.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, full marker metadata excluding bases and independent genome Datasets reads completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable target graph node and was not run. No target DOI/PMID or external history reference applies. Full history validation was not run; no history event or lifecycle promotion occurred.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:222101` agrees on ID, label, rank, parent, code and snapshot 2026-09-13; synonyms and retirement are empty. Complete native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31581` agrees with no unique-name qualifier.

All ten pinned ancestor IDs, labels and ranks match: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Hyphomicrobiales 356; Hyphomicrobiales incertae sedis 119042; Enhydrobacter 212791; unclassified Enhydrobacter 2632691.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035439&retmode=xml) agrees on identity and named lineage. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035439) confirms all ancestor IDs including root. Creation is 23 May 2011, update 28 May 2011; no OtherNames/type-material assertion is supplied. Complete exact scans of pinned merged-ID, dropped and type-material tables found no target row.

NCBI species rank is not formal nomenclatural standing. EXACT grounding identifies this taxonomic node. The ZM35 type strain of Mediterraneibacter glycyrrhizinilyticus, taxid 342942, is a different organism; its DSM/JCM deposits must not be transferred here.

## Evidence

Path row `data/taxa/PATHS.tsv:14592` and scope row `curation/seed_scope.tsv:322372` uniquely match the ID, stem and seed reason. The attestation correctly counts one NAME.

There are no direct children in the pinned backbone. Full exact scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Strain_count 0 agrees with the BacDive inventory and target subtree, despite the unrelated homonymous BacDive strain.

Fresh structured reads of all three complete manifests give extracted_at values raw 2026-09-13T17:50:44Z, ATB 17:54:04Z, StrainInfo 17:29:00Z. The inspected newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed event. Source list and scope reason agree. Hashes were not recomputed.

Exact nuccore search returned only UID 333797941. Full [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333797941) identifies `JF792358.1`, a 1,359-base partial 16S rRNA marker, strain ZM35, taxon:1035439. Its literal host is Zea mays and its geographic qualifier is China. No independently resolved host CURIE is asserted here.

The Luo/Sui reference concerns nitrogen levels and maize-rhizosphere bacterial diversity, but is marked unpublished and supplies no DOI/PMID or inspected ZM35 response result. A separate direct submission dates to 7 April 2011, China Agricultural University. No isolation_source, tissue, culture deposit, BioSample, BioProject or assembly link appears in the complete marker metadata. The title is context, not proof of nitrogen fixation, nitrogen-response phenotype or a specific root compartment.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035439/dataset_report) returned an empty object. These bounded checks do not establish universal genome absence; the partial marker is not a genome.

Before web search, read all 28 rows of the fresh `kg-microbe-sources imodulondb datasets` response through `uv run --offline --project ../../culturebotai-claw`. Enhydrobacter is not covered and no gene/module is asserted. No component query applies; noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, mappings, deposits and graphs need not be populated without applicable support. Marker host/location metadata is optional enrichment, not a missing required representation. Its strain qualifier is not an inventoried culture deposit.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched ID, full label, stem and strain punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 59 matched lines were read fully: three applicable rows, three unrelated raw inventory/type rows, twenty-one unrelated GOLD rows, one unrelated BacDive row, two unrelated StrainInfo rows, ten unrelated NCBI assembly rows and nineteen unrelated ATB rows.

A separate JF792358/version scan returned zero lines in those roots. At both stages all five SOURCE.json documents were parsed separately in full and history filenames searched without ignore filtering, with no additional match. These are bounded repository checks, not global absence claims.

Exact-label, accession and strain/author web searches did not establish an applicable experiment or deposit chain. A supplementary-table search lead was examined and bounded as described below. No consequential omission was established.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. A shared strain label or embedded sample-number substring does not identify this taxon.

## Recommended Edits

None required. Preserve generated YAML and SEEDED state.

Future enrichment belongs in a maintained source/extractor and inventory, or tested harmonization changes in `src/taxonmech/seed.py`; scope changes belong in `curation/seed_scope.tsv`. Correct source/kg-microbe mappings upstream. Keep taxon, host, strain, deposit, marker, sample, assembly, genome, run and project identities distinct.

## Follow-up Checks

For later authorized curation, establish whole-accession source chains, rerun target schema/strict validators and then documented full-corpus reproduction/provenance gates. Resolve host CURIEs independently and require actual ZM35 experiments before nitrogen-related claims. Any future literature enrichment must distinguish the Enhydrobacter marker JF792358 from the Mediterraneibacter marker AB233029. No unresolved blocker requires enrichment now.

## Additional Notes

All unrelated repository candidates were read losslessly.

`data/raw/bacdive_strains.tsv:2735` and `data/bacdive/records.jsonl.gz:2734` identify BacDive 2835, taxid 342942, ZM35, DSM 17593/JCM 13368, LPSN 798371 and marker AB233029. The native record calls it Mediterraneibacter glycyrrhizinilyticus, with Clostridium glycyrrhizinilyticum as synonym. `data/raw/ncbi_type_material.tsv:188244-188245` likewise concerns taxid 342942, not the target.

`data/straininfo/records.jsonl.gz:291895` is SI-ID 389269 with the same two type deposits and taxid 342942; row 8962 is Pediococcus pentosaceus, taxid 1255, LMG 17236, designation Devriese TZM 35. Their source DOIs and deposit history do not support this record.

In `data/gold/organisms.jsonl.gz`, row 175654 is Go0237516, Pediococcus/1255; row 459648 is Go0629083, Clostridium glycyrrhizinilyticum/342942. Rows 526880-526883 are Go0707232-Go0707235, Zostera marina/29655, samples zm_350, zm_352, zm_356 and zm_357. `data/gold/projects.jsonl.gz:617124-617138` contains their fifteen transcriptome projects Gp0844386-Gp0844400, with empty BioProject/BioSample accessions. These are not Enhydrobacter cultures.

Nine NCBI assembly rows are N. gonorrhoeae taxid 485, PRJNA317462. In `data/catalog/ncbi_genbank-0038.jsonl.gz`, rows 28743, 28745, 28785, 28788, 28863, 28864 and 49627 respectively identify GCA_042129485.1, GCA_042129525.1, GCA_042130325.1, GCA_042130385.1, GCA_042131885.1, GCA_042131905.1 and GCA_042551785.1; their BioSamples are SAMN10354397, 98, 99, 96, 92, 90 and 93 respectively. In `data/catalog/ncbi_genbank-0039.jsonl.gz`, rows 67 and 88 are GCA_042560585.1/SAMN10354394 and GCA_042561005.1/SAMN10354395.

`data/catalog/ncbi_genbank-0054.jsonl.gz:24504` is E. coli/562 isolate ECZM35P, GCA_058856525.1, SAMEA117693513, PRJNA514245. Its PMID 30286803 is not a citation for the target.

All columns of nineteen `data/catalog/allthebacteria.tsv.xz` rows were read: 141956-141964 are E. coli samples SAMEA110354390-398 with assorted contamination, contig-count or sylph flags; 1503452-1503460 are N. gonorrhoeae samples SAMN10354390 and 92-99; 1557652 is Salmonella sample SAMN11035439, run SRR8655889, no ENA assembly accession and an assembly-submission-error flag. Their runs, analyses, filters, checksums and URLs do not supply target provenance.

The indexed [Table S1 mirror](https://www.researchgate.net/publication/294080768_Additional_file_1_Table_S1) contains a Clostridium glycyrrhizinilyticum/ZM35/AB233029 label and a separate Enhydrobacter genus label. Searches within its fetched text found neither the full target label nor JF792358. The inspected [primary paper's methods](https://link.springer.com/article/10.1186/1746-6148-9-30) use community 16S amplicons and RDP Seqmatch with a 97% OTU threshold; this is not an Enhydrobacter ZM35 culture or susceptibility experiment. No target phenotype was imported from that lead. PMC presented a browser challenge; publisher methods were accessible. The original supplementary XLS was not independently downloaded or analyzed.

Only this new report was written. No YAML, inventory, generated product, prior report, history or lifecycle state was changed. No paid research, external contact or GitHub mutation occurred.
