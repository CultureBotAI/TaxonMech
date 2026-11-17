# YAML Record Review: Pseudomonas sp. 25AAIII

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_25aaiii.yaml`
- Started UTC: 2026-10-06T22:45:44Z
- Finished UTC: 2026-10-06T22:47:53Z
- Verdict: pass

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:1035331` denotes Pseudomonas sp. 25AAIII, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`. Assertions comprise ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graphs are asserted. The generated YAML remains read-only; corrections belong in maintained source inputs, extraction/seeding logic or scope decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_25aaiii.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_25aaiii.yaml --out /private/tmp/ps25a-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and is header-only.
- Structured comparisons read the full backbone row, every ancestor, direct children, seven other raw inventories, PATHS, scope, source attestation and seed event. Compared assertions agree.
- Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file searches, lossless reading of all eighteen candidates, complete parsing of five SOURCE.json files and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows inspected before external follow-ups. P. aeruginosa, P. putida and P. syringae datasets do not establish exact 25AAIII coverage.
- Live NCBI taxonomy XML and Datasets taxonomy, exact Assembly/nuccore searches, complete metadata excluding bases/translations for all three nucleotide hits, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSample records were independently retrieved in full, with exact returned-set agreement.
- Both cited papers' PubMed metadata/abstracts, relevant 2011 publisher text and original Figure 1, and the 2015 publisher abstract were inspected.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, full 2015 article or supplementary assay tables. Bounded checks do not replace corpus-only gates.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222024`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31499`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035331&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035331) agree on identifier, label, rank, parent, domain and code.

Every ancestor ID, label and normalized rank agrees: root (1); cellular organisms (131567); Bacteria (2); Pseudomonadati (3379134); Pseudomonadota (1224); Gammaproteobacteria (1236); Pseudomonadales (72274); Pseudomonadaceae (135621); Pseudomonas (286); unclassified Pseudomonas (196821). Datasets supplies root ID 1, omitted from EFetch's displayed lineage.

Pinned synonym fields and live alternate-name content are empty, with no direct children in the pinned backbone. Species rank is NCBI classification, not formal nomenclatural standing or a type designation. Do not identify 25AAIII with 25AGIII or another numbered isolate through shared genus, sampling site or study membership.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14515` supplies the exact stem; `curation/seed_scope.tsv:322296` agrees with the event's scope reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected seed rule; it is not human sign-off.

All three exact nucleotide hits were read:

| Accession | Record-specific evidence |
| --- | --- |
| [HQ449633.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449633.1), UID 338163875 | 809 bp partial 16S rRNA gene, W01/W02 primers |
| [HQ449650.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449650.1), UID 342316577 | 902 bp partial aoxB CDS, arsenite oxidase large-subunit annotation; AEL22184.1; codon_start 3 |
| [JQ080756.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080756.1), UID 444747060 | 421 bp partial arsB CDS, arsenite efflux pump annotation; AGE11928.1; codon_start 1 |

All source features explicitly identify Pseudomonas sp. 25AAIII, strain 25AAIII and taxon 1035331. Both CDS annotations use translation table 11. HQ features identify arsenic-contaminated sediment from Sainte Marie aux Mines, France, submitted 28-Oct-2010 from Strasbourg. The JQ feature names sediment from that locality, submitted 25-Nov-2011 from Metz. These are partial sequences, not genomes or registered deposits. An arsB annotation is not a measurement of transport function, and the retrieved set does not prove absence of other genes.

The HQ records cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), PMID 21571879, PMCID PMC3127681. Figure 1 shows 25AAIII Pseudomonas sp. HQ449633 in dark blue, bold and underlined, with an activity circle. This exact label/accession link supports a PCR-positive group-II aoxB isolate with detected arsenite oxidation, not a quantitative threshold or constitutive-activity claim.

The JQ record cites [Cordi et al. (2015), DOI 10.1007/s11356-014-3840-5](https://link.springer.com/article/10.1007/s11356-014-3840-5), PMID 25721523. The inspected abstract discusses 219 isolates and genotype/sensitivity relationships, not a 25AAIII assay row. No exact resistance threshold, growth value or demonstrated transporter mechanism was inferred.

Exact-organism Assembly search returned zero items with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035331/dataset_report) returned an empty object. These are bounded service results, not global genome-absence evidence.

All ten [BioSamples SAMN10353310 through SAMN10353319](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353319%2C10353318%2C10353317%2C10353316%2C10353315%2C10353314%2C10353313%2C10353312%2C10353311%2C10353310&retmode=xml) identify human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. None establishes identity with this French sediment isolate.

## Completeness

Current seeded assertions have no consequential demonstrated omission. Zero inventoried BacDive strains does not deny the study isolate or its partial sequences. Optional functional enrichment is not required for this taxonomy record; traits, habitats and media belong to the appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035331|\b25[-_ ]?AAIII\b|pseudomonas_sp_25aaiii` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files and history filenames were checked separately.

All eighteen candidates were read losslessly: five JSON objects and thirteen TSV rows. Three are exact backbone, name and scope entries; fifteen are unrelated:

| Candidates | Exclusion evidence |
| --- | --- |
| One IMG-number substring in GOLD | Analysis Ga0653400 names Salmonella enterica enterica sv. Augustenborg 310198, links project Gp0811429, IMG 8103533194 and GCA_007161845.1/AAHEOQ000000000, and has an empty organism GOLD ID. It supplies no 25AAIII culture-identity chain. |
| Two run-number matches | BV-BRC 1773.18340 and ATB SAMEA3558864/ERR1035331/ERZ9334500 denote M. tuberculosis. A run accession is not this TaxID. |
| Two ungapped-length matches | GenBank GCA_000994545.1 and GTDB GB_GCA_000994545.1 denote Candidatus Daviesbacteria bacterium GW2011_GWA2_40_9, taxon 1618424, SAMN03319558, PRJNA273161. Ungapped length 1035331 is a measurement. |
| Ten unknown ATB samples | SAMN10353310 through SAMN10353319 are NOT_PROCESSED with no FASTA, run or assembly. Independent BioSample records resolve the unrelated context above. |

The separate `HQ449633|HQ449650|AEL22184|JQ080756|AGE11928` search found zero lines across the same ignored-inclusive roots and no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. These absence findings are bounded to inspected roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, count, source attestation and seed provenance agree. No unsupported phenotype, formal nomenclature or genome linkage is asserted.

## Recommended Edits

None required.

Separately authorized enrichment should retain exact isolate/accession chains and distinguish observed oxidation from transporter annotations. Source fixes belong in maintained extraction or `src/taxonmech/seed.py` with tests, never a generated YAML hand edit. Do not infer a culture deposit, genome, quantitative phenotype or human-reviewed status.

## Follow-up Checks

After an authorized maintained-source change, use the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect the emitted TSV and generated fields.

Functional enrichment requires exact isolate-specific assay rows and conditions. Strain/genome links require source-backed culture identity and explicit matching chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Review/curation guidance, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the review skill was reread this turn. The dedicated review branch is retained; the other session is closed.

The original 2011 publisher figure was inspected at original resolution. The full 2015 subscription article and supplementary assay values were not inspected for this target. No paid research, access-control bypass or external message was attempted.

The YAML was byte-compared with its initial full read and remains unchanged. This report is the only new repository artifact for this target. No source inventory, generated product, history, prior report, Git/GitHub object or Eukaryota record was modified.
