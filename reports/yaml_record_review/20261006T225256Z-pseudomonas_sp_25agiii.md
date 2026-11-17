# YAML Record Review: Pseudomonas sp. 25AGIII

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_25agiii.yaml`
- Started UTC: 2026-10-06T22:48:49Z
- Finished UTC: 2026-10-06T22:52:56Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035332` denotes Pseudomonas sp. 25AGIII, rank SPECIES, domain BACTERIA, parent NCBITaxon:196821. It asserts ten root-first ancestors, genetic code 11, EXACT grounding, SEEDED mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graph are asserted. Generated records remain read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_25agiii.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_25agiii.yaml --out /private/tmp/ps25g-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and contains only its header.
- Full backbone/ancestor, direct-child, seven other raw-inventory, PATHS, scope, attestation and event comparisons passed. Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file search completed; all seventeen candidates were read losslessly. Five SOURCE.json files were parsed fully, and history filenames checked.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0, all 28 rows inspected before external follow-ups. Other Pseudomonas datasets do not establish exact 25AGIII coverage; iModulonDB was not applicable, not negative evidence.
- Live NCBI taxonomy XML and Datasets taxonomy, exact-organism Assembly/nuccore searches, full metadata excluding bases/translations for all four nucleotide hits, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSamples were independently retrieved in full, with exact requested/returned-set agreement.
- The two papers' PubMed bibliographic metadata/abstracts, relevant 2011 publisher text and original Figure 1, and the 2015 publisher abstract were inspected.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, full 2015 article or supplementary assay tables. No target-only reproduction gate was invented.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222025`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31500`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035332&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035332) agree on identifier, label, species rank, parent, domain and genetic code.

All ancestor IDs, labels and normalized ranks agree: root (1); cellular organisms (131567); Bacteria (2); Pseudomonadati (3379134); Pseudomonadota (1224); Gammaproteobacteria (1236); Pseudomonadales (72274); Pseudomonadaceae (135621); Pseudomonas (286); unclassified Pseudomonas (196821). Datasets supplies root ID 1, omitted from EFetch's displayed lineage.

Pinned synonym fields and live alternate-name content are empty; the pinned backbone has no direct children. Species rank is NCBI classification, not formal nomenclatural standing or type status. Shared genus, locality or publication does not equate 25AGIII with 25AAIII or other isolates.

## Evidence

The sole attestation correctly counts one NCBITAXON NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14516` supplies the exact stem; `curation/seed_scope.tsv:322297` agrees with the seed reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected seeding rule, without implying human review.

All four exact nucleotide hits were read:

| Accession | Exact-target metadata |
| --- | --- |
| [HQ449638.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449638.1), UID 338163880 | 809 bp partial 16S rRNA gene; W01/W02 primers |
| [HQ449653.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449653.1), UID 342316583 | 867 bp partial aoxB CDS; arsenite oxidase large-subunit annotation; AEL22187.1; codon_start 3 |
| [JQ080865.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080865.1), UID 444747278 | 644 bp partial ACR3(1) CDS; arsenite efflux pump annotation; AGE12037.1; codon_start 1 |
| [JQ080773.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080773.1), UID 444747094 | 614 bp partial arsB CDS; arsenite efflux pump annotation; AGE11945.1; codon_start 2 |

Every source feature explicitly identifies Pseudomonas sp. 25AGIII, strain 25AGIII and taxon 1035332. All three CDS annotations use translation table 11. HQ records identify arsenic-contaminated sediment from Sainte Marie aux Mines, France, submitted 28-Oct-2010 from Strasbourg. JQ records identify sediment from that locality, submitted 25-Nov-2011 from Metz. Partial genes are neither genomes nor registered culture deposits; annotations alone do not demonstrate transporter function.

The HQ records cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), PMID 21571879, PMCID PMC3127681. Original Figure 1 explicitly labels 25AGIII Pseudomonas sp. HQ449638 in dark blue, bold and underlined, with an activity circle. This supports the exact isolate's PCR-positive group-II aoxB and detected arsenite oxidation, not a quantitative threshold or constitutive phenotype.

The JQ records cite [Cordi et al. (2015), DOI 10.1007/s11356-014-3840-5](https://link.springer.com/article/10.1007/s11356-014-3840-5), PMID 25721523. The inspected abstract addresses 219 isolates and genotype/sensitivity relationships; it supplies no exact 25AGIII assay row. No resistance threshold, growth value or demonstrated transport mechanism was inferred.

Exact-organism Assembly search returned zero with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035332/dataset_report) returned an empty object. These bounded results do not prove global genome absence.

All ten [BioSamples SAMN10353320 through SAMN10353329](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353329%2C10353328%2C10353327%2C10353326%2C10353325%2C10353324%2C10353323%2C10353322%2C10353321%2C10353320&retmode=xml) identify human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. They are not evidence for this French sediment isolate.

## Completeness

No consequential omission was demonstrated in the current seeded assertions. Zero inventoried BacDive strains does not deny the study isolate or its sequences. Optional functional enrichment is not required for a seeded taxonomy record; traits, habitats and media belong to the appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035332|\b25[-_ ]?AGIII\b|pseudomonas_sp_25agiii` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files and history filenames were checked separately.

All seventeen candidates were read in full: three JSON objects and fourteen TSV rows. Three are exact backbone, name and scope entries; fourteen are unrelated:

| Candidates | Exclusion evidence |
| --- | --- |
| Two M. tuberculosis run-number matches | BV-BRC 1773.18339 and ATB SAMEA3558865/ERR1035332/ERZ9334512. The run accession is not a TaxID. |
| One GenBank accession substring | GCA_010353325.1 denotes Campylobacter jejuni PNUSAC014931, taxon 197, SAMN13825136, PRJNA239251. |
| Ten unknown ATB samples | SAMN10353320 through SAMN10353329 are NOT_PROCESSED with no FASTA, assembly or run. Independent BioSamples resolve the unrelated context above. |
| One E. coli run-number substring | ATB SAMN13135801/SRR10353325/ERZ25667002 denotes Escherichia coli str. K-12 substr. W3110, with PASS and available FASTA. Availability does not establish target identity. |

A separate `HQ449638|HQ449653|AEL22187|JQ080865|AGE12037|JQ080773|AGE11945` search found zero lines across the same ignored-inclusive roots, with no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. Absence findings are bounded to these roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, grounding, count, attestation and seed provenance agree. The record asserts no unsupported phenotype, nomenclatural status or genome linkage.

## Recommended Edits

None required.

Separately authorized enrichment must retain exact isolate/accession chains and distinguish observed oxidation from transporter annotations. Source corrections belong in maintained extraction inputs or `src/taxonmech/seed.py` with tests, not hand-edited generated YAML. Do not infer a culture deposit, genome, quantitative phenotype or human-reviewed status.

## Follow-up Checks

After an authorized maintained-source change, use the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect emitted TSV and generated fields.

Functional enrichment requires exact isolate-specific assays and conditions. Genome links require explicit source-backed identity chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Review/curation guidance, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The dedicated review branch remains in use; the other session is closed and no additional worktree was created.

The original 2011 figure was visually inspected at original resolution. The full 2015 subscription article and supplementary assay values were not inspected. No paid research, access-control bypass or external message was attempted.

The YAML was byte-compared with the initial full read and remains unchanged. This report is the only new repository artifact for this target. No source inventory, generated product, history, prior report, Git/GitHub object or Eukaryota record was modified.
