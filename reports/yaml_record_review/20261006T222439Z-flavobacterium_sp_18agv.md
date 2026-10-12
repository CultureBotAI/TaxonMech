# YAML Record Review: Flavobacterium sp. 18AGV

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/flavobacterium_sp_18agv.yaml`
- Started UTC: 2026-10-06T22:22:11Z
- Finished UTC: 2026-10-06T22:24:39Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035325` denotes Flavobacterium sp. 18AGV, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196869`. It asserts twelve root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, mappings, strain listing, genomes, phenotypes, citations or causal graphs are asserted. The YAML is generated and read-only; future changes belong in maintained source inputs, extraction/seeding code or scope decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/flavobacterium_sp_18agv.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/flavobacterium_sp_18agv.yaml --out /private/tmp/fl18-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Structured comparisons read the full backbone row, all ancestors, direct children, seven other raw inventories, PATHS, scope, source attestation and seed event. All compared assertions agree.
- Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file searches, lossless reads of all twenty-eight native candidates, complete parsing of five SOURCE.json files and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows inspected before external follow-ups. No applicable Flavobacterium dataset; absence is not negative biological evidence.
- Live NCBI taxonomy XML and Datasets taxonomy, exact Assembly/nuccore searches, full metadata excluding bases/translations for both nucleotide hits, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSamples were independently retrieved in full and checked against the complete requested accession set.
- The cited paper's PubMed metadata/abstract, relevant publisher text and original Figure 1 were inspected, including the exact 18AGV label/accession.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration or supplementary assay tables. Bounded comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222018`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31493`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035325&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035325) agree on identifier, label, rank, parent, domain and genetic code.

All ancestor IDs, labels and normalized ranks agree: root; cellular organisms; Bacteria; Pseudomonadati; FCB group; Bacteroidota/Chlorobiota group; Bacteroidota; Flavobacteriia; Flavobacteriales; Flavobacteriaceae; Flavobacterium; unclassified Flavobacterium. Both intermediate group nodes correctly have CLADE rank. Datasets includes root ID 1, omitted from EFetch's displayed chain.

Pinned synonym fields and live alternate-name content are empty, and there are no direct children in the pinned backbone. NCBI species rank here does not assert a formally named species or type strain. Keep 18AGV separate from Flavobacterium 16AGV, 19AAV and similarly named isolates in other genera.

## Evidence

The NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14509` maps the exact stem; `curation/seed_scope.tsv:322290` agrees with the seed-event reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected seed-timestamp rule, not human sign-off.

Both exact nuccore hits were read:

| Accession | Evidence |
| --- | --- |
| [HQ449644.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449644.1), UID 338163886 | 793 bp partial 16S rRNA gene, W01/W02 primers |
| [HQ449657.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449657.1), UID 342316591 | 699 bp partial aoxB CDS, arsenite oxidase large-subunit annotation; AEL22191.1; codon_start 1; translation table 11 |

Both explicitly identify Flavobacterium sp. 18AGV, strain 18AGV and taxon 1035325. Source features identify arsenic-contaminated sediment from Sainte Marie aux Mines, France; direct submissions are dated 28-Oct-2010 from Strasbourg. These are partial gene sequences, not genomes, culture-collection deposits or direct activity measurements.

Both cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), verified as PMID 21571879 and PMCID PMC3127681. Figure 1 marks 18AGV Flavobacterium sp. HQ449644 in dark blue, bold and underlined, without an activity circle: a PCR-positive group-II aoxB isolate, not an oxidation-positive isolate in that figure. This is not a universal negative phenotype assertion or proof of a specific transfer mechanism.

Exact-organism Assembly search returned zero items with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035325/dataset_report) returned an empty object. These are bounded negatives, not proof that no genome exists anywhere.

All ten [BioSamples SAMN10353250 through SAMN10353259](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353259%2C10353258%2C10353257%2C10353256%2C10353255%2C10353254%2C10353253%2C10353252%2C10353251%2C10353250&retmode=xml) independently resolve to human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. None establishes identity with this French sediment isolate.

## Completeness

Current seeded assertions have no consequential demonstrated omission. Zero inventoried BacDive strains does not deny the named isolate or its gene sequences. Optional sequence enrichment is not a required-field omission; traits, habitats and media belong to the appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035325|\b18[-_ ]?AGV\b|flavobacterium_sp_18agv` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included; five SOURCE.json files and history filenames were checked separately.

All twenty-eight candidates were read losslessly: fifteen JSON objects and thirteen TSV rows. Three are exact backbone, name and scope entries. Twenty-five are unrelated:

| Candidates | Exclusion evidence |
| --- | --- |
| Two run-number matches | BV-BRC 1773.18342 and ATB SAMEA3558858/ERR1035325/ERZ9334494 denote M. tuberculosis. The run number is not this TaxID. |
| Five Pseudomonas accession matches | GOLD Ga0158546/Gp0189777, BV-BRC 287.1618, GTDB RS_GCF_001035325.1 and paired GCA/GCF_001035325.1 denote P. aeruginosa Pae_CF67.09c, taxon 287, SAMN03566387. GenBank/BV-BRC list PRJNA282164; RefSeq/GTDB list PRJNA224116. GOLD's organism ID is empty; no target culture chain is supplied. |
| One Klebsiella accession match | GCA_041035325.1 is K. pneumoniae zj01246, taxon 573, SAMN37542634, PRJNA1021041. |
| One Enterobacter accession match | GCA_021035325.1 is E. hormaechei PS439, taxon 158836, SAMEA8581646, PRJNA514245. |
| Two Vibrio accession matches | GCA/GCF_051035325.1 are V. parahaemolyticus VP20045, taxon 670, SAMN46338788. RefSeq is suppressed; GenBank remains latest. Their projects are respectively PRJNA1213288 and PRJNA224116. |
| Four genome-size matches | GenBank and GTDB representations of GCA_002779965.1 identify Candidatus Roizmanbacteria CG03_land_8_20_14_0_80_36_21, taxon 1974846, SAMN06659200, PRJNA362739. The two representations of GCA_001871285.1 identify Candidatus Gottesmanbacteria CG1_02_37_22, taxon 1805209, SAMN04328229, PRJNA297582. Both MAGs have ungapped length 1035325, not this taxonomy. |
| Ten unknown ATB samples | SAMN10353250 through SAMN10353259 are NOT_PROCESSED with no FASTA, run or assembly. Independent BioSample records resolve their unrelated context above. |

The separate `HQ449644|HQ449657|AEL22191` search found zero lines across the same ignored-inclusive roots and no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. These absence findings apply only to the inspected roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, strain count, attestation and seed provenance agree. The YAML asserts no unsupported phenotype, formal nomenclature or genome linkage.

## Recommended Edits

None required.

For separately authorized enrichment, preserve the isolate-specific accession chain and distinguish gene annotation from activity. Source fixes belong in maintained extraction or `src/taxonmech/seed.py` with focused tests. Do not hand-edit the YAML, infer a deposit/genome link or promote the record to human-reviewed status.

## Follow-up Checks

After an authorized maintained-input change, use the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect the emitted TSV and generated fields.

Functional enrichment requires exact isolate-specific assay rows and conditions. Strain/genome linking requires source-backed culture identity and explicit matching chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Review/curation guidance, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the review skill was reread this turn. The dedicated review branch is retained, and the other session is closed.

The original 2011 publisher figure was viewed at original resolution. Supplementary quantitative assay rows were not inspected for this target. No paid research, access-control bypass or external message was attempted.

The YAML was byte-compared with its initial full read and remains unchanged. This report is the only new repository artifact for this target. No source inventories, generated products, histories, prior reports, Git/GitHub objects or Eukaryota records were modified.
