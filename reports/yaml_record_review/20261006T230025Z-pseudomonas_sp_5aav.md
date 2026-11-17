# YAML Record Review: Pseudomonas sp. 5AAV

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_5aav.yaml`
- Started UTC: 2026-10-06T22:58:13Z
- Finished UTC: 2026-10-06T23:00:25Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035334` denotes Pseudomonas sp. 5AAV, rank SPECIES, domain BACTERIA, parent NCBITaxon:196821. It asserts ten root-first ancestors, genetic code 11, EXACT grounding, SEEDED mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graph are asserted. This generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_5aav.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_5aav.yaml --out /private/tmp/ps5-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and is header-only.
- Full backbone, every ancestor, direct-child, seven other raw-inventory, PATHS, scope, attestation and seed-event comparisons agree. Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file searches completed. All eighteen initial candidates were read losslessly; five SOURCE.json files were parsed fully, and history filenames checked.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows inspected before external follow-ups. Covered P. aeruginosa, P. putida and P. syringae datasets do not establish exact 5AAV coverage. iModulonDB was not applicable, not negative evidence.
- Live NCBI taxonomy XML and Datasets taxonomy, exact-organism Assembly/nuccore searches, full metadata excluding bases/translations for all three nucleotide hits, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSamples were retrieved in full, with exact requested/returned-set agreement. Full stored outputs were reread separately after a combined tool display was truncated.
- Both sequence-cited papers' PubMed metadata/abstracts, relevant 2011 publisher text and original Figure 1, and the 2015 publisher abstract were inspected in this review turn.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, full 2015 article or supplementary assay tables. No target-only reproduction gate was invented.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222027`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31502`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035334&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035334) agree on identifier, label, rank, parent, domain and code.

Every ancestor ID, label and normalized rank agrees: root (1); cellular organisms (131567); Bacteria (2); Pseudomonadati (3379134); Pseudomonadota (1224); Gammaproteobacteria (1236); Pseudomonadales (72274); Pseudomonadaceae (135621); Pseudomonas (286); unclassified Pseudomonas (196821). Datasets supplies root ID 1, omitted from EFetch's displayed lineage.

Pinned synonym fields and live alternate-name content are empty, with no direct children in the pinned backbone. NCBI species rank is not formal nomenclatural standing or type status. Shared genus, sampling site or paper does not identify 5AAV with another numbered isolate.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14518` supplies the exact stem; `curation/seed_scope.tsv:322299` agrees with the event's scope reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected seed rule; it is not human sign-off.

All three exact nucleotide hits were read:

| Accession | Record-specific metadata |
| --- | --- |
| [HQ449635.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449635.1), UID 338163877 | 809 bp partial 16S rRNA gene; W01/W02 primers |
| [HQ449660.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449660.1), UID 342316597 | 820 bp partial aoxB CDS; arsenite oxidase large-subunit annotation; AEL22194.1; codon_start 3 |
| [JQ080834.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080834.1), UID 444747216 | 658 bp partial ACR3(1) CDS; arsenite efflux pump annotation; AGE12006.1; codon_start 1 |

All source features explicitly identify Pseudomonas sp. 5AAV, strain 5AAV and taxon 1035334. Both CDS annotations use translation table 11. HQ features identify arsenic-contaminated sediment from Sainte Marie aux Mines, France, submitted 28-Oct-2010 from Strasbourg. The JQ feature identifies sediment from that locality, submitted 25-Nov-2011 from Metz. These are partial genes, not genomes or registered culture deposits. An efflux-pump annotation is not a measurement of transport activity.

The HQ records cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), PMID 21571879, PMCID PMC3127681. Figure 1 shows 5AAV Pseudomonas sp. HQ449635 in dark blue, bold and underlined, without an activity circle. It supports PCR-positive group-II aoxB, not detected oxidation in the reported assay. This does not establish inability to oxidize arsenite under every condition.

The JQ record cites [Cordi et al. (2015), DOI 10.1007/s11356-014-3840-5](https://link.springer.com/article/10.1007/s11356-014-3840-5), PMID 25721523. The inspected abstract addresses 219 isolates and genotype/sensitivity relationships, not a 5AAV assay row. No quantitative threshold, growth value or experimentally demonstrated transporter mechanism was inferred.

Exact-organism Assembly search returned zero with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035334/dataset_report) returned an empty object. These bounded service results do not prove global genome absence.

All ten [BioSamples SAMN10353340 through SAMN10353349](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353349%2C10353348%2C10353347%2C10353346%2C10353345%2C10353344%2C10353343%2C10353342%2C10353341%2C10353340&retmode=xml) identify human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. They do not supply identity evidence for this French sediment isolate.

## Completeness

No consequential omission was demonstrated in the current seeded assertions. Zero inventoried BacDive strains does not deny the study isolate or its sequences. Optional functional enrichment is not required for this taxonomy record; traits, habitats and media belong in their appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035334|\b5[-_ ]?AAV\b|pseudomonas_sp_5aav` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files and history filenames were checked separately.

All eighteen candidates were read: five JSON objects and thirteen TSV rows. Three are exact backbone, name and scope entries; fifteen are unrelated:

| Candidates | Exclusion evidence |
| --- | --- |
| Two run-number matches | BV-BRC 1773.18347 and ATB SAMEA3558867/ERR1035334/ERZ9334511 denote Mycobacterium tuberculosis. A run accession is not this TaxID. |
| One GenBank accession substring | GCA_010353345.1 denotes Campylobacter jejuni strain 866379, taxon 197, SAMN13825568, PRJNA505131. |
| Two strain-name substrings | GenBank GCA_060493965.1 and historical RefSeq GCF_060493965.1 denote Salmonella enterica FZSY010301035334, taxon 28901, SAMN62529166. GenBank is latest with PRJNA995522; RefSeq is suppressed with PRJNA224116 and not-live date 2026-09-03. Neither is target evidence. |
| Ten unknown ATB samples | SAMN10353340 through SAMN10353349 are NOT_PROCESSED with no FASTA, run or assembly. Independent BioSample metadata resolves the unrelated context above. |

The separate `HQ449635|HQ449660|AEL22194|JQ080834|AGE12006` search found zero lines across the same ignored-inclusive roots, with no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. These absence findings are bounded to inspected roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, count, source attestation and seed provenance agree. No unsupported phenotype, nomenclature or genome linkage is asserted.

## Recommended Edits

None required.

Separately authorized enrichment must retain exact isolate/accession chains and assay scope. Do not turn aoxB or ACR3(1) annotations into a measured phenotype. Source fixes belong in maintained extraction inputs or `src/taxonmech/seed.py` with tests, not generated YAML. Do not infer a culture deposit, genome or human-reviewed status.

## Follow-up Checks

After an authorized maintained-source change, use the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect the actual TSV and generated fields.

Functional enrichment requires exact isolate-specific assays and conditions. Strain/genome links require explicit source-backed identity chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Repository guidance, review/curation skills, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The dedicated review branch remains in use; the other session is closed.

The original 2011 publisher figure was inspected at original resolution. The full 2015 subscription article and supplementary assay values were not inspected. No paid research, access-control bypass or external message was attempted.

The YAML was byte-compared with its initial full read and remains unchanged. This report is the only new repository artifact for this target. No source inventory, generated product, history, prior report, Git/GitHub object or Eukaryota record was modified.
