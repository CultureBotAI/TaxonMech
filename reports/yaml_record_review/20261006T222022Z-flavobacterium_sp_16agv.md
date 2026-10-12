# YAML Record Review: Flavobacterium sp. 16AGV

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/flavobacterium_sp_16agv.yaml`
- Started UTC: 2026-10-06T22:18:27Z
- Finished UTC: 2026-10-06T22:20:22Z
- Verdict: pass

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:1035324` denotes Flavobacterium sp. 16AGV, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196869`. Assertions comprise twelve root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

There are no asserted synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graphs. Generated YAML is read-only; future corrections belong in maintained source inputs, extraction/seeding logic or scope decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/flavobacterium_sp_16agv.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/flavobacterium_sp_16agv.yaml --out /private/tmp/fl16-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and is header-only.
- Structured comparisons read the complete backbone row, all ancestors, direct children, seven other raw inventories, PATHS, scope, attestation and seed event. Compared assertions agree.
- Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file searches, lossless reading of all twenty-one native candidates, full parsing of five SOURCE.json files and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows inspected before external follow-ups. No Flavobacterium dataset applies, which is not negative biological evidence.
- Live NCBI taxonomy XML and Datasets taxonomy, exact Assembly/nuccore searches, complete metadata excluding bases/translations for both nucleotide hits, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSamples were retrieved in full and checked for exact agreement with the requested accessions.
- The cited 2011 paper's PubMed metadata/abstract, relevant publisher text and original Figure 1 were inspected this turn, including the exact 16AGV label/accession.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration or supplementary assay tables. Bounded comparisons do not substitute for corpus-only gates.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222017`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31492`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035324&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035324) agree on identifier, label, species rank, parent, bacterial domain and code 11.

All ancestor IDs, labels and normalized ranks agree: root; cellular organisms; Bacteria; Pseudomonadati; FCB group; Bacteroidota/Chlorobiota group; Bacteroidota; Flavobacteriia; Flavobacteriales; Flavobacteriaceae; Flavobacterium; unclassified Flavobacterium. Both intermediate group nodes are correctly represented as CLADE. Datasets includes root ID 1, which EFetch omits from its displayed chain.

Pinned synonym fields and live alternate-name content are empty; the pinned backbone has no direct children. The label identifies an incompletely named isolate at NCBI's species rank, not a claim of formal species nomenclature or a designated type strain. Flavobacterium sp. 18AGV and 19AAV and similarly named isolates in other genera remain distinct.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14508` supplies the exact slug; `curation/seed_scope.tsv:322289` agrees with the event's scope reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected seed-timestamp rule; it is not a human-review timestamp.

Both exact nucleotide hits were inspected:

| Accession | Exact evidence |
| --- | --- |
| [HQ449643.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449643.1), UID 338163885 | 793 bp partial 16S rRNA gene, with W01/W02 primers |
| [HQ449656.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449656.1), UID 342316589 | 705 bp partial aoxB CDS, annotated arsenite oxidase large subunit, protein AEL22190.1; codon_start 3; translation table 11 |

Both source features explicitly name Flavobacterium sp. 16AGV, strain 16AGV and taxon 1035324, with arsenic-contaminated sediment from Sainte Marie aux Mines, France. Direct submissions are dated 28-Oct-2010 from Strasbourg. These are partial gene sequences, not genomes, registered culture deposits or direct assay measurements.

Both cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), verified as PMID 21571879 and PMCID PMC3127681. Figure 1 labels 16AGV Flavobacterium sp. HQ449643 in dark blue, bold and underlined, without an activity circle: a PCR-positive group-II aoxB isolate, not a demonstrated oxidation-positive isolate in that figure. This is not universal negative phenotype evidence.

Exact-organism Assembly search returned zero items with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035324/dataset_report) returned an empty object. No genome absence claim beyond these bounded services is warranted.

All ten [BioSamples SAMN10353240 through SAMN10353249](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353249%2C10353248%2C10353247%2C10353246%2C10353245%2C10353244%2C10353243%2C10353242%2C10353241%2C10353240&retmode=xml) independently identify human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. Their source metadata do not establish an association with this French sediment isolate.

## Completeness

Current seeded assertions have no consequential demonstrated omission. Zero inventoried BacDive strains does not deny the named isolate or its partial sequences. Optional sequence enrichment is not required to pass this seeded taxonomic record. Traits, habitats and media belong to the appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035324|\b16[-_ ]?AGV\b|flavobacterium_sp_16agv` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included; five SOURCE.json files and history filenames were independently checked.

All twenty-one candidates were read losslessly: eight JSON objects and thirteen TSV rows. Three are exact backbone, scientific-name and scope entries. Eighteen supply no target evidence:

| Candidates | Exclusion evidence |
| --- | --- |
| Two run-number matches | BV-BRC 1773.18338 and ATB SAMEA3558857/ERR1035324/ERZ9334497 denote M. tuberculosis. The run accession is not this TaxID. |
| Three genome-size substrings | GTDB RS_GCF_042732015.1 and paired GenBank/RefSeq GCA/GCF_042732015.1 denote Streptomyces sp. NPDC059802, taxon 3346952, SAMN43798230. Ungapped length 10353241 contains the query digits. GenBank's project is PRJNA1106891; RefSeq/GTDB list PRJNA224116. |
| Two genome-size matches | GCA/GCF_054355615.1 denote Mesomycoplasma ovipneumoniae MoS11L23A, taxon 29562, SAMN54369268, length 1035324. GenBank lists PRJNA1395673; RefSeq lists PRJNA224116. Length is not taxonomy. |
| One accession substring | GCA_010353245.1 denotes C. jejuni PNUSAC013537, taxon 197, SAMN13337911, PRJNA239251. |
| Ten unknown ATB samples | SAMN10353240 through SAMN10353249 are NOT_PROCESSED with no FASTA, run or assembly. The independent authority records resolve their unrelated context above. |

The separate `HQ449643|HQ449656|AEL22190` search found zero lines across the same ignored-inclusive roots, and no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. These absence claims are bounded to the inspected roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, count, source attestation and seed provenance agree. No unsupported phenotype, formal nomenclature or genome linkage is asserted.

## Recommended Edits

None required.

For separately authorized enrichment, preserve the exact isolate/accession connection and keep partial CDS annotation separate from assay evidence. Source/harmonization fixes belong in maintained extraction or `src/taxonmech/seed.py` with tests; no generated YAML hand edit, invented culture deposit, inferred genome or human-reviewed promotion is justified.

## Follow-up Checks

After an authorized maintained-source change, follow the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect the emitted TSV and generated fields.

Functional enrichment needs exact isolate-specific assay rows and conditions; strain/genome linking needs source-backed culture identity and explicit matching chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Review/curation guidance, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The review skill, curation skill, checklist and justfile were reread this turn. The dedicated review branch is retained and the other session is closed.

The original 2011 publisher figure was inspected at original resolution. Supplementary quantitative assay rows were not inspected for this target. No paid research, access-control bypass or external message was attempted.

The full YAML was byte-compared with the initial read and remains unchanged. This report is the only new repository artifact for this target. No source inventories, generated products, histories, prior reports, Git/GitHub objects or Eukaryota records were modified.
