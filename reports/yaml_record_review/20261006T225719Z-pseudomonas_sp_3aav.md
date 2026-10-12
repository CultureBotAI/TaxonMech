# YAML Record Review: Pseudomonas sp. 3AAV

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_3aav.yaml`
- Started UTC: 2026-10-06T22:54:55Z
- Finished UTC: 2026-10-06T22:57:19Z
- Verdict: pass

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:1035333` denotes Pseudomonas sp. 3AAV, rank SPECIES, domain BACTERIA, parent NCBITaxon:196821. The record asserts ten root-first ancestors, genetic code 11, EXACT grounding, SEEDED mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graph are asserted. Corrections belong in maintained inputs or generation logic, not this generated YAML.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_3aav.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_3aav.yaml --out /private/tmp/ps3-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and is header-only.
- Full backbone, every ancestor, direct children, seven other raw inventories, PATHS, scope, attestation and seed-event comparisons agree. Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file searches completed. All fifteen initial candidates were read losslessly; five SOURCE.json files were parsed fully and history filenames checked.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0, all 28 rows inspected before external follow-ups. P. aeruginosa, P. putida and P. syringae datasets do not establish exact 3AAV coverage. iModulonDB was not applicable, not negative evidence.
- Live NCBI taxonomy XML and Datasets taxonomy, exact Assembly/nuccore searches, full metadata excluding bases/translations for all three nucleotide hits, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSamples were independently retrieved in full with exact requested/returned-set agreement.
- Both sequence-cited papers' PubMed metadata/abstracts, relevant 2011 publisher text and original Figure 1, and the 2015 publisher abstract were inspected.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, full 2015 article or supplementary assay tables. Bounded checks do not replace corpus-only gates.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222026`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31501`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035333&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035333) agree on identifier, label, species rank, parent, domain and code.

Each ancestor ID, label and normalized rank agrees: root (1); cellular organisms (131567); Bacteria (2); Pseudomonadati (3379134); Pseudomonadota (1224); Gammaproteobacteria (1236); Pseudomonadales (72274); Pseudomonadaceae (135621); Pseudomonas (286); unclassified Pseudomonas (196821). Datasets includes root ID 1, which EFetch omits from its displayed lineage.

Pinned synonym fields and live alternate-name content are empty, with no direct children in the pinned backbone. NCBI species rank is not formal nomenclatural standing or type status. Shared genus, study membership or sampling site does not equate 3AAV with neighboring numbered isolates.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14517` supplies the exact stem; `curation/seed_scope.tsv:322298` agrees with the event's scope reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected seeding rule; it does not imply human review.

All three exact nucleotide hits were inspected:

| Accession | Record-specific metadata |
| --- | --- |
| [HQ449634.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449634.1), UID 338163876 | 809 bp partial 16S rRNA gene; W01/W02 primers |
| [HQ449658.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449658.1), UID 342316593 | 713 bp partial aoxB CDS; arsenite oxidase large-subunit annotation; AEL22192.1; codon_start 3 |
| [JQ080833.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080833.1), UID 444747214 | 596 bp partial ACR3(1) CDS; arsenite efflux pump annotation; AGE12005.1; codon_start 2 |

All source features explicitly identify Pseudomonas sp. 3AAV, strain 3AAV and taxon 1035333. Both CDS annotations use translation table 11. HQ records identify arsenic-contaminated sediment from Sainte Marie aux Mines, France, submitted 28-Oct-2010 from Strasbourg. The JQ record identifies sediment from that locality, submitted 25-Nov-2011 from Metz. These partial genes are not genomes or registered culture deposits; an efflux-pump annotation alone does not prove transport activity.

The HQ records cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), PMID 21571879, PMCID PMC3127681. Figure 1 explicitly shows 3AAV Pseudomonas sp. HQ449634 in dark blue, bold and underlined, with an activity circle. This supports PCR-positive group-II aoxB and detected arsenite oxidation in this isolate; it supplies no quantitative resistance threshold.

The JQ record cites [Cordi et al. (2015), DOI 10.1007/s11356-014-3840-5](https://link.springer.com/article/10.1007/s11356-014-3840-5), PMID 25721523. Its abstract describes 219 isolates and genotype/sensitivity relationships, not an exact 3AAV assay row. No isolate-specific resistance threshold or transporter mechanism was inferred.

Exact-organism Assembly search returned zero with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035333/dataset_report) returned an empty object. These are bounded service results, not proof of global genome absence.

All ten [BioSamples SAMN10353330 through SAMN10353339](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353339%2C10353338%2C10353337%2C10353336%2C10353335%2C10353334%2C10353333%2C10353332%2C10353331%2C10353330&retmode=xml) identify human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. They do not establish identity with this French sediment isolate.

## Completeness

No consequential omission was demonstrated in the current seeded assertions. Zero inventoried BacDive strains does not deny the named study isolate or its sequences. Optional functional enrichment is not required for this seeded taxonomy record; traits, habitats and media belong in their appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035333|\b3[-_ ]?AAV\b|pseudomonas_sp_3aav` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. SOURCE.json contents and history filenames were checked separately.

All fifteen candidates were read: two JSON objects and thirteen TSV rows. Three are exact backbone, name and scope entries; twelve are unrelated:

- BV-BRC 1773.18343 and ATB SAMEA3558866/ERR1035333/ERZ9334507 denote Mycobacterium tuberculosis. A run accession containing the target digits is not a matching TaxID.
- Ten ATB samples SAMN10353330 through SAMN10353339 are NOT_PROCESSED, have no FASTA, assembly or run, and are labeled unknown. Their independent BioSample metadata resolves the unrelated context above.

The separate `HQ449634|HQ449658|AEL22192|JQ080833|AGE12005` search found zero lines across the same ignored-inclusive roots, with no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. Absence findings are bounded to these roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current assertions. Identity, lineage, grounding, count, source attestation and seed provenance agree. The record asserts no unsupported phenotype, nomenclatural status or genome linkage.

## Recommended Edits

None required.

Separately authorized enrichment must preserve exact isolate/accession links and distinguish measured oxidation from transporter annotations. Source corrections belong in maintained extraction inputs or `src/taxonmech/seed.py` with tests, not generated YAML. Do not infer culture deposits, genomes, quantitative phenotypes or human-reviewed status.

## Follow-up Checks

After an authorized maintained-source change, use the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect the actual TSV and generated fields.

Functional enrichment requires exact isolate-specific assay rows and conditions. Genome links require explicit source-backed identity chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Repository guidance, review/curation skills, checklist, schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The dedicated review branch remains in use; the other session is closed.

The original 2011 publisher figure was visually inspected at original resolution. The full 2015 subscription article and supplementary assay values were not inspected. No paid research, access-control bypass or external message was attempted.

The YAML was byte-compared with its initial full read and remains unchanged. This report is the only new repository artifact for this target. No source inventory, generated product, history, prior report, Git/GitHub object or Eukaryota record was modified.
