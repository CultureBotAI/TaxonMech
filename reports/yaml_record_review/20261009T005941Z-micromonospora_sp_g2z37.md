# YAML Record Review: Micromonospora sp. G2Z37

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/micromonospora_sp_g2z37.yaml`
- Started UTC: 2026-10-09T00:56:31Z
- Finished UTC: 2026-10-09T00:59:41Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036512`: species rank, Bacteria domain, parent `NCBITaxon:2617518`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Optional synonyms, nomenclature, mappings, strain/genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. This YAML is generated, not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/micromonospora_sp_g2z37.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/micromonospora_sp_g2z37.yaml --out /private/tmp/micromonosporaG2Z37-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons checked complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Own nucleotide XML consistency check: declared and actual length 1401, rRNA transcription equals DNA, no non-ACGT symbols. This is annotation consistency, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. The embedded event was read; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036512&retmode=xml) agrees with identifier, label, rank, parent, genetic code and ancestor labels/ranks. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036512) confirms all ten root-first ancestor IDs. The chain runs through Bacillati, Actinomycetota, Actinomycetes, Micromonosporales, Micromonosporaceae, Micromonospora and unclassified Micromonospora. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

Species rank for an unnamed strain-associated NCBI taxon is not proof of a formally described species. Exact grounding denotes this identifier, not equivalence to a named congener. Live EFetch has no other names and pinned synonyms are empty. Pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222512`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32056`: scientific-name object.
- `data/taxa/PATHS.tsv:15019`: identifier and slug.
- `curation/seed_scope.tsv:322759`: date and admission reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records, not the existence of a strain designation.

Exact Nuccore query `txid1036512[Organism:noexp]` returned UID 334361410. Complete [JF806665.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806665.1) XML, including both references, all features and sequence, explicitly identifies G2Z37 and taxon 1036512. It is a 1401-base partial 16S marker, partial at both ends. Source qualifiers supply organism, genomic DNA, strain and taxon cross-reference, but no host, isolation-source, country, culture-deposit or assembly qualifier. Features are source and rRNA, not CDS.

References name Chen, Wu and Li, an unpublished seagrass-associated actinobacteria study and direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. No PMID or DOI is supplied in this accession. A marker is not a genome or phenotype assay; missing source qualifiers must not be copied from neighboring accessions.

All 59 additional local candidates were fully read and excluded. Fifty-eight concern ten lactic-acid bacterial isolates under project PRJNA503586, with paired RefSeq records under PRJNA224116:

| Taxon and strain | Sample | GenBank accession | BV-BRC genomes |
| --- | --- | --- | --- |
| Lactiplantibacillus plantarum 1525, taxid 1590 | SAMN10365120 | GCA_025122595.1 | 1590.3075; 1590.3128 |
| Lactiplantibacillus plantarum 1526, taxid 1590 | SAMN10365121 | GCA_025131215.1 | 1590.3078; 1590.3131 |
| Lactiplantibacillus plantarum 1527, taxid 1590 | SAMN10365122 | GCA_025133155.1 | 1590.3080; 1590.3132 |
| Latilactobacillus curvatus 1528, taxid 28038 | SAMN10365123 | GCA_025133135.1 | 28038.213; 28038.225 |
| Lactiplantibacillus plantarum 1529, taxid 1590 | SAMN10365124 | GCA_025133105.1 | 1590.3079; 1590.3133 |
| Lactococcus lactis 752, taxid 1358 | SAMN10365125 | GCA_025133095.1 | 1358.1707; 1358.1743 |
| Lactococcus lactis 754, taxid 1358 | SAMN10365126 | GCA_025133065.1 | 1358.1706; 1358.1742 |
| Lactococcus lactis 756, taxid 1358 | SAMN10365127 | GCA_025133055.1 | 1358.1705; 1358.1740 |
| Lactococcus lactis 1031, taxid 1358 | SAMN10365128 | GCA_025133035.1 | 1358.1704; 1358.1738 |
| Lactococcus lactis 1034, taxid 1358 | SAMN10365129 | GCA_025133015.1 | 1358.1702; 1358.1741 |

The complete fifty-eight source rows are:

- `data/bvbrc/bvbrc-0004.jsonl.gz`: lines 9950, 9953, 9954, 9956, 9998, 10001, 10002 and 10003; `data/bvbrc/bvbrc-0002.jsonl.gz`: lines 41119, 41121, 41122, 41123, 41124, 41154, 41156, 41157, 41158 and 41159; `data/bvbrc/bvbrc-0015.jsonl.gz`: lines 39027 and 39039.
- `data/catalog/ncbi_genbank-0023.jsonl.gz`: lines 14364, 14795, 14885, 14886, 14887, 14888, 14889, 14890, 14891 and 14892.
- `data/catalog/ncbi_refseq-0004.jsonl.gz`: lines 25232, 25345, 25359, 25360, 25361, 25362, 25363, 25364, 25365 and 25366.
- `data/catalog/gtdb_genomes-0016.jsonl.gz`: lines 3243 and 37503; `data/catalog/gtdb_genomes-0013.jsonl.gz:6620`; `data/catalog/gtdb_genomes-0005.jsonl.gz:23549`; `data/catalog/gtdb_genomes-0002.jsonl.gz:47054`; `data/catalog/gtdb_genomes-0015.jsonl.gz:3890`; `data/catalog/gtdb_genomes-0004.jsonl.gz:15292`; `data/catalog/gtdb_genomes-0001.jsonl.gz`: lines 26449 and 39200; `data/catalog/gtdb_genomes-0000.jsonl.gz:48252`.
- `data/gold/projects.jsonl.gz`: lines 526009, 526024, 526025, 526031, 526032, 526101, 526142 and 526238. These respectively link strains 1528, 1526, 1525, 756, 752, 1527, 1034 and 1031 to Gp0700438/Go0656182, Gp0700453/Go0656197, Gp0700454/Go0656198, Gp0700460/Go0656204, Gp0700461/Go0656205, Gp0700530/Go0656274, Gp0700571/Go0656315 and Gp0700667/Go0656411.

All ten GCA/GCF pairs explicitly mark paired sequence identity and latest status, with different annotation metadata. GTDB uses the ten corresponding RS_GCF accessions as nonrepresentatives. Their food/dairy and geographic metadata do not concern G2Z37. Paired assembly assertions are distinct from the two BV-BRC IDs per isolate; common sample/strain alone does not prove genome equivalence. GOLD Go/Gp IDs are related records, not genome identifiers.

The remaining candidate, `data/catalog/allthebacteria.tsv.xz:754089`, is Salmonella enterica sample SAMEA5671496, run ERR4338745, analysis ERZ25239856. Its assembly/HQ/sylph filters all pass and supplied AWS/OSF FASTA locations were read. The matching digits are in SeqKit sum `seqkit.v0.1_DLS_k0_58ff7d2581701036512f6db6c1370971`, not a taxon identifier. This sum is not MD5, and the unrelated sample cannot support a target genome link.

[Wu et al. (2012), DOI 10.5897/AJMR11.981](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii), Table 2, gives G2Z37's closest species as M. aurantiaca, 99.79%, with PCR screening PKS-I negative, PKS-II positive and NRPS positive. Interpretation: these are comparison/screening results, not synonymy or demonstrated antimicrobial activity. Methods and the complete table/footnote were inspected as author-hosted HTML, not visually verified PDF.

The inspected [2018 review's Table 1](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2018.01767/full) lists G2Z37 as Micromonospora sp.; its broader endophyte framing is not adopted as an independent localization result. Other isolates in that row must remain distinct.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, mappings, deposits, genomes and graphs are appropriately empty without explicit identity chains. External marker/literature context does not require an invented BacDive entry or genome link.

Initial and expanded `rg --no-ignore --hidden -n -z -i` searches covered ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, G2Z37 and slug, then JF806665, UID 334361410 and the primary DOI. Both found the same 62 rows: three own taxonomy/name/scope rows and 59 unrelated candidates. All were read fully. Five `SOURCE.json` files were separately parsed without a target match, and history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query for G2Z37/JF806665/JF806665.1 returned zero with quoted-phrase warnings. Web strain/accession searches returned taxonomy listings and the literature leads described above. Neither indexed misses nor snippets establish universal genome/literature absence; direct primary records and text support this review.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no covered strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. The YAML agrees with pinned and live NCBI identity and does not import the unrelated source records or overstate optional biological evidence.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join identifiers by numeric substring, equate strains by project or name pattern, count samples/projects as genomes, or derive a formal species reassignment from marker similarity.

Future taxonomy corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression tests; scope changes belong in `curation/seed_scope.tsv`. Optional enrichment needs maintained-input and model/seeder support, not generated-YAML edits.

## Follow-up Checks

No corrective follow-up required for current claims. Any future enrichment needs an explicit strain/accession/deposit chain and original-source verification at the scope of the proposed assertion. Obtain a readable primary PDF and visually verify its relevant table/figure before transferring literature details.

After an authorized input/seeder change, run focused regression tests, `just seed-canary NCBITaxon:1036512`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

Local review, checklist and ownership guidance governed this individual review. The shared paper was inspected for this target's own row; no verdict or sequence identity was inherited from a neighboring record. PDF routes failed in the earlier G2Z35 review; accessible author-hosted HTML was used here without claiming PDF visual verification.

Before/after YAML SHA-256 was `fb5701037bc4f79d6ef508c01bcecf0dfb974504bbcd89829a59109c81778bff`. Only this new timestamped report was written for this target. No YAML, source, history, status, generated page or GitHub object changed. Eukaryota and existing worktrees remained untouched.
