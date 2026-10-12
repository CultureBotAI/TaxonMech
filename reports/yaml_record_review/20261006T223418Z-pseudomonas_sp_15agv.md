# YAML Record Review: Pseudomonas sp. 15AGV

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_15agv.yaml`
- Started UTC: 2026-10-06T22:29:56Z
- Finished UTC: 2026-10-06T22:34:18Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read. `NCBITaxon:1035327` denotes Pseudomonas sp. 15AGV, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`. Assertions comprise ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graphs are asserted. Seeded YAML remains read-only; changes belong in maintained source inputs, extraction/seeding logic or scope decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_15agv.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_15agv.yaml --out /private/tmp/ps15-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Structured comparisons read the full backbone row, every ancestor, direct children, seven other raw inventories, PATHS, scope, source attestation and seed event. Compared assertions agree.
- Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file searches, lossless reading of all seventeen candidate rows, complete parsing of five SOURCE.json files and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows inspected before external follow-ups. Listed P. aeruginosa, P. putida and P. syringae datasets do not establish exact 15AGV coverage.
- Live NCBI taxonomy XML and Datasets taxonomy, exact Assembly/nuccore searches, complete metadata excluding bases/translations for all four nucleotide hits, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSample records were independently retrieved in full, with exact returned-set agreement.
- Both cited papers' PubMed metadata/abstracts, relevant 2011 publisher text and original Figure 1, and the 2015 publisher abstract were inspected.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, full 2015 article or supplementary assay tables. Bounded checks do not replace corpus-only gates.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222020`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31495`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035327&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035327) agree on identifier, label, rank, parent, domain and code.

Every ancestor ID, label and normalized rank agrees: root (1); cellular organisms (131567); Bacteria (2); Pseudomonadati (3379134); Pseudomonadota (1224); Gammaproteobacteria (1236); Pseudomonadales (72274); Pseudomonadaceae (135621); Pseudomonas (286); unclassified Pseudomonas (196821). Datasets supplies root ID 1, omitted from EFetch's displayed chain.

Pinned synonym fields and live alternate-name content are empty; the pinned backbone has no direct children. Species rank reflects NCBI classification, not formal species nomenclature or type-strain designation. Neither shared genus nor study membership licenses a merge with a named Pseudomonas species or another numbered isolate.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14511` supplies the exact stem; `curation/seed_scope.tsv:322292` agrees with the event's scope reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected seed rule, not human sign-off.

All four exact nucleotide hits were read:

| Accession | Record-specific evidence |
| --- | --- |
| [HQ449639.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449639.1), UID 338163881 | 809 bp partial 16S rRNA gene, W01/W02 primers |
| [HQ449655.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449655.1), UID 342316587 | 900 bp partial aoxB CDS, arsenite oxidase large-subunit annotation; AEL22189.1; codon_start 1 |
| [JQ080882.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080882.1), UID 444747312 | 644 bp partial ACR3(1) CDS, arsenite efflux pump annotation; AGE12054.1; codon_start 1 |
| [JQ080780.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080780.1), UID 444747108 | 556 bp partial arsB CDS, arsenite efflux pump annotation; AGE11952.1; codon_start 3 |

All source features explicitly identify Pseudomonas sp. 15AGV, strain 15AGV and taxon 1035327. All three CDS annotations use translation table 11. HQ features identify arsenic-contaminated sediment from Sainte Marie aux Mines, France, submitted 28-Oct-2010 from Strasbourg. JQ features name sediment from that locality, submitted 25-Nov-2011 from Metz. These are partial sequences, not genomes or registered deposits. Transporter annotations are not measured efflux activities.

The HQ records cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), verified as PMID 21571879 and PMCID PMC3127681. Figure 1 shows 15AGV Pseudomonas sp. HQ449639 in dark blue, bold and underlined, with an activity circle. The legend and text support a PCR-positive group-II aoxB isolate with experimentally detected arsenite oxidation. This exact label/accession link supports the activity observation, but no quantitative threshold or constitutive activity claim.

The JQ records cite [Cordi et al. (2015), DOI 10.1007/s11356-014-3840-5](https://link.springer.com/article/10.1007/s11356-014-3840-5), verified as PMID 25721523. The inspected abstract discusses 219 isolates and genotype/sensitivity relationships; it does not supply a 15AGV assay row. Multiple carrier genes do not by themselves establish high resistance. No exact threshold, transport mechanism or growth rate was inferred.

Exact-organism Assembly search returned zero items with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035327/dataset_report) returned an empty object. These bounded service results do not prove genome absence everywhere.

All ten [BioSamples SAMN10353270 through SAMN10353279](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353279%2C10353278%2C10353277%2C10353276%2C10353275%2C10353274%2C10353273%2C10353272%2C10353271%2C10353270&retmode=xml) identify human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. They do not establish identity with this French sediment isolate.

## Completeness

Current seeded assertions have no consequential demonstrated omission. Zero inventoried BacDive strains does not deny the isolate or its partial sequences. Optional functional enrichment is not required for this taxonomy record; traits, habitats and media belong to the appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035327|Pseudomonas[ _]sp\.?[ _]15AGV|15AGV` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files and history filenames were checked separately.

All seventeen candidates were read losslessly: three JSON objects and fourteen TSV rows. Three are exact backbone, name and scope entries; fourteen are unrelated:

| Candidates | Exclusion evidence |
| --- | --- |
| Two run-number matches | BV-BRC 1773.18344 and ATB SAMEA3558860/ERR1035327/ERZ9334491 denote M. tuberculosis. A run accession is not this TaxID. |
| One genome-size match | GCA_983736825.1 is Bacteroidota bacterium, taxon 1898104, isolate TARA_SAMEA2622690_MAG_00000179, SAMEA122621997, PRJEB103742; genome_size 1035327 is a measurement. |
| One checksum substring | ATB SAMN04093971/SRR2451875/ERZ4173156 denotes Streptococcus agalactiae; the digits occur inside assembly_seqkit_sum. |
| Ten unknown ATB samples | SAMN10353270 through SAMN10353279 are NOT_PROCESSED with no FASTA, run or assembly. Independent BioSample records identify the unrelated context above. |

The separate `HQ449639|HQ449655|AEL22189|JQ080882|AGE12054|JQ080780|AGE11952` search found zero lines across the same ignored-inclusive roots and no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. Absence findings are bounded to inspected roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, count, source attestation and seed provenance agree. No unsupported phenotype, formal nomenclature or genome linkage is asserted.

## Recommended Edits

None required.

Separately authorized enrichment should retain exact isolate/accession chains and distinguish measured oxidation from transporter annotations. Source fixes belong in maintained extraction or `src/taxonmech/seed.py` with tests, never a generated YAML hand edit. Do not infer a culture deposit, genome, quantitative phenotype or human-reviewed status.

## Follow-up Checks

After an authorized maintained-source change, use the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect the emitted TSV and generated fields.

Functional enrichment requires exact isolate-specific assay rows and conditions. Strain/genome links require source-backed culture identity and explicit matching chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Review/curation guidance, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the review skill was reread this turn. The dedicated review branch is retained, and the other session is closed.

The original 2011 publisher figure was inspected at original resolution. The full 2015 subscription article and supplementary assay values were not inspected for this target. No paid research, access-control bypass or external message was attempted.

The YAML was byte-compared with its initial full read and remains unchanged. This report is the only new repository artifact for this target. No source inventory, generated product, history, prior report, Git/GitHub object or Eukaryota record was modified.
