# YAML Record Review: Pseudomonas sp. 24AGIII

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_24agiii.yaml`
- Started UTC: 2026-10-06T22:42:01Z
- Finished UTC: 2026-10-06T22:43:54Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read. `NCBITaxon:1035330` denotes Pseudomonas sp. 24AGIII, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`. It asserts ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graphs are asserted. Generated YAML remains read-only; future corrections belong in maintained inputs, extraction/seeding logic or scope decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_24agiii.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_24agiii.yaml --out /private/tmp/ps24g-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and is header-only.
- Structured comparisons read the full backbone row, every ancestor, direct children, seven other raw inventories, PATHS, scope, source attestation and seed event. Compared assertions agree.
- Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file searches, lossless reading of all sixteen candidates, complete parsing of five SOURCE.json files and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows inspected before this target's external follow-ups. P. aeruginosa, P. putida and P. syringae datasets do not establish exact 24AGIII coverage.
- Live NCBI taxonomy XML and Datasets taxonomy, exact Assembly/nuccore searches, complete metadata excluding bases/translations for all four nucleotide hits, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSample records were independently retrieved in full, with exact returned-set agreement.
- Both cited papers' PubMed metadata/abstracts, relevant 2011 publisher text and original Figure 1, and the 2015 publisher abstract were inspected earlier in this same turn. The target's own source-feature and accession links were independently checked.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, full 2015 article or supplementary assay tables. Bounded comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222023`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31498`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035330&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035330) agree on identifier, label, rank, parent, domain and code.

Every ancestor ID, label and normalized rank agrees: root (1); cellular organisms (131567); Bacteria (2); Pseudomonadati (3379134); Pseudomonadota (1224); Gammaproteobacteria (1236); Pseudomonadales (72274); Pseudomonadaceae (135621); Pseudomonas (286); unclassified Pseudomonas (196821). Datasets supplies root ID 1, omitted from EFetch's displayed chain.

Pinned synonym fields and live alternate-name content are empty, with no direct children in the pinned backbone. NCBI species rank is not formal nomenclatural standing or a type designation. Preserve the distinction between 24AGIII, 24AAIII and other numbered isolates; matching genus and sampling site do not establish identity.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14514` supplies the exact stem; `curation/seed_scope.tsv:322295` agrees with the event's scope reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected seed rule, not human review sign-off.

All four exact nucleotide hits were read:

| Accession | Record-specific evidence |
| --- | --- |
| [HQ449637.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449637.1), UID 338163879 | 809 bp partial 16S rRNA gene, W01/W02 primers |
| [HQ449652.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449652.1), UID 342316581 | 843 bp partial aoxB CDS, arsenite oxidase large-subunit annotation; AEL22186.1; codon_start 3 |
| [JQ080864.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080864.1), UID 444747276 | 644 bp partial ACR3(1) CDS, arsenite efflux pump annotation; AGE12036.1; codon_start 1 |
| [JQ080772.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080772.1), UID 444747092 | 661 bp partial arsB CDS, arsenite efflux pump annotation; AGE11944.1; codon_start 2 |

All source features explicitly identify Pseudomonas sp. 24AGIII, strain 24AGIII and taxon 1035330. All three CDS annotations use translation table 11. HQ features identify arsenic-contaminated sediment from Sainte Marie aux Mines, France, submitted 28-Oct-2010 from Strasbourg. JQ features identify sediment from that locality, submitted 25-Nov-2011 from Metz. These are partial sequences, not genomes or registered culture deposits; transporter annotations are not measured efflux activities.

The HQ records cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), PMID 21571879, PMCID PMC3127681. Figure 1 shows 24AGIII Pseudomonas sp. HQ449637 in dark blue, bold and underlined, with an activity circle. The exact label/accession and legend support a PCR-positive group-II aoxB isolate with detected arsenite oxidation. No quantitative or constitutive-activity claim follows.

The JQ records cite [Cordi et al. (2015), DOI 10.1007/s11356-014-3840-5](https://link.springer.com/article/10.1007/s11356-014-3840-5), PMID 25721523. The inspected abstract concerns collection-level genotype/sensitivity relationships, not a 24AGIII assay row. It does not establish a precise resistance threshold, growth value or measured transport mechanism for this isolate.

Exact-organism Assembly search returned zero items with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035330/dataset_report) returned an empty object. These bounded results do not prove genome absence everywhere.

All ten [BioSamples SAMN10353300 through SAMN10353309](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353309%2C10353308%2C10353307%2C10353306%2C10353305%2C10353304%2C10353303%2C10353302%2C10353301%2C10353300&retmode=xml) identify human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. They do not establish identity with this French sediment isolate.

## Completeness

Current seeded assertions have no consequential demonstrated omission. Zero inventoried BacDive strains does not deny the isolate or its partial sequences. Optional gene enrichment is not required for this taxonomy record; traits, habitats and media belong in the appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035330|\b24[-_ ]?AGIII\b|pseudomonas_sp_24agiii` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files and history filenames were checked separately.

All sixteen candidates were read losslessly: three JSON objects and thirteen TSV rows. Three are exact backbone, name and scope entries; thirteen are unrelated:

| Candidates | Exclusion evidence |
| --- | --- |
| Two run-number matches | BV-BRC 1773.18337 and ATB SAMEA3558863/ERR1035330/ERZ9334499 denote M. tuberculosis. A run accession is not this TaxID. |
| One assembly accession substring | GCA_010353305.1 denotes C. jejuni PNUSAC013528, taxon 197, SAMN13337922, PRJNA239251. |
| Ten unknown ATB samples | SAMN10353300 through SAMN10353309 are NOT_PROCESSED with no FASTA, run or assembly. Independent BioSample records resolve the unrelated context above. |

The separate `HQ449637|HQ449652|AEL22186|JQ080864|AGE12036|JQ080772|AGE11944` search found zero lines across the same ignored-inclusive roots and no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. Absence findings are bounded to inspected roots and snapshots.

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

Review/curation guidance, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The review skill, checklist and CLAUDE.md were reread this turn. The dedicated review branch is retained; the other session is closed.

The original 2011 publisher figure was inspected at original resolution in this turn. The full 2015 subscription article and supplementary assay values were not inspected for this target. No paid research, access-control bypass or external message was attempted.

The YAML was byte-compared with its initial full read and remains unchanged. This report is the only new repository artifact for this target. No source inventory, generated product, history, prior report, Git/GitHub object or Eukaryota record was modified.
