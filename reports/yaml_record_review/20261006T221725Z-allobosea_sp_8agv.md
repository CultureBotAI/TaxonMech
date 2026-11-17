# YAML Record Review: Allobosea sp. 8AGV

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/allobosea_sp_8agv.yaml`
- Started UTC: 2026-10-06T22:14:52Z
- Finished UTC: 2026-10-06T22:17:25Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read. `NCBITaxon:1035323` denotes Allobosea sp. 8AGV, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2653178`. It asserts ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graphs are asserted. Future changes belong in maintained source inputs, extraction/seeding code or scope decisions, never this generated YAML directly.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/allobosea_sp_8agv.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/allobosea_sp_8agv.yaml --out /private/tmp/ab8-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and is header-only.
- Structured comparisons read the full backbone row, every ancestor, direct children, seven other raw inventories, PATHS, scope, attestation and seed event. Compared assertions agree.
- Exact type-material, merged-ID and dropped-ID searches found no target entries.
- Ignored-inclusive compressed-file searches, lossless reads of all fifteen native candidate rows, complete parsing of five SOURCE.json files and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 dataset rows inspected before external follow-ups. No Allobosea/Bosea dataset applies; absence is not negative biological evidence.
- Live NCBI taxonomy XML and Datasets taxonomy, exact Assembly/nuccore searches, all three nucleotide metadata records excluding bases/translations, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSample accessions were independently retrieved in full and checked for exact returned-set agreement.
- LPSN genus context, both cited papers' PubMed metadata/abstracts, relevant 2011 publisher text and original Figure 1, and the 2015 publisher abstract were inspected.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, full 2015 article or supplementary assay tables. These bounded checks do not replace corpus-only gates.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222016`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31491`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035323&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035323) agree on identifier, label, rank, parent, domain and code.

Every ancestor ID, label and normalized rank agrees: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria; Hyphomicrobiales; Alloboseaceae; Allobosea; unclassified Allobosea. Datasets supplies root ID 1, omitted from EFetch's displayed chain. Pinned synonym fields and live alternate-name content are empty, and the pinned backbone has no direct children.

[LPSN's Allobosea entry](https://lpsn.dsmz.de/genus/allobosea) identifies Allobosea Deshmukh and Oren 2026 as the correct genus name and Bosea as an illegitimate homotypic synonym, under Alloboseaceae. This is genus context, not species-level LPSN attestation or equivalence to the genus type species.

The exact sequences establish name continuity: descriptions retain Bosea sp. 8AGV, while current organism/source features explicitly identify Allobosea sp. 8AGV, strain 8AGV and taxon 1035323. This isolate remains distinct from 7AGV and 43AGV.

## Evidence

The NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14507` maps the identifier to this stem; `curation/seed_scope.tsv:322288` agrees with the event's scope reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the seed timestamp under the inspected seed rule, not human sign-off.

All three exact sequence records were inspected:

| Accession | Record-specific evidence |
| --- | --- |
| [HQ449628.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449628.1), UID 338163870 | 833 bp partial 16S rRNA gene, W01/W02 primers |
| [HQ449666.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449666.1), UID 342316565 | 903 bp partial aoxB CDS, arsenite oxidase large subunit annotation, AEL22178.1 |
| [JQ080903.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080903.1), UID 444747352 | 423 bp partial ACR3(2) CDS, arsenite efflux pump annotation, AGE12074.1 |

Both CDS annotations have codon_start 1 and translation table 11. HQ source features name arsenic-contaminated sediment from Sainte Marie aux Mines, France, submitted 28-Oct-2010 from Strasbourg. JQ080903 identifies sediment from the same locality, submitted 25-Nov-2011 from Metz. These are partial gene sequences, not assemblies or registered deposits; ACR3(2) annotation alone is not a measured efflux assay.

The HQ records cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), verified as PMID 21571879 and PMCID PMC3127681. Figure 1 explicitly labels 8AGV Bosea sp. HQ449628 in pink, bold and underlined, with an activity circle: a PCR-positive study isolate carrying group-I aoxB and experimentally positive arsenite oxidation. The text identifies AgNO3 testing with a positive control. This supports a condition-bounded positive observation for 8AGV, not its neighboring isolates, an exact resistance threshold, or a general species-wide mechanism.

JQ080903 cites [Cordi et al. (2015), DOI 10.1007/s11356-014-3840-5](https://link.springer.com/article/10.1007/s11356-014-3840-5), verified as PMID 25721523. The inspected abstract describes 219 isolates and genotype/sensitivity relationships; it supplies no exact 8AGV assay row. No resistance threshold or growth value is inferred from collection-level results.

Exact-organism Assembly search returned zero items with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035323/dataset_report) returned an empty object. These negatives are bounded to those services, not proof that no genome exists anywhere.

All ten [BioSamples SAMN10353230 through SAMN10353239](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353239%2C10353238%2C10353237%2C10353236%2C10353235%2C10353234%2C10353233%2C10353232%2C10353231%2C10353230&retmode=xml) concern human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. Their exact metadata do not link them to this French sediment isolate.

## Completeness

Current seeded assertions are complete enough. Optional historical-name or sequence enrichment is not a required-field omission. Zero inventoried BacDive strains does not deny the isolate's existence or its partial gene records. Traits, habitats and media belong to the appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035323|\b8[-_ ]?AGV\b|(?:allo)?bosea_sp_8agv` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files and history filenames were checked separately.

All fifteen candidates were read losslessly: two JSON objects and thirteen TSV rows. Three are exact backbone, name and scope entries. Twelve are unrelated:

| Candidates | Exclusion evidence |
| --- | --- |
| Two run-number matches | BV-BRC 1773.18335 and ATB SAMEA3558856/ERR1035323/ERZ9334486 denote M. tuberculosis, not Allobosea. A run accession is not a TaxID. |
| Ten unknown ATB samples | SAMN10353230 through SAMN10353239 are NOT_PROCESSED, with no FASTA, run or assembly. The independent BioSample records resolve their distinct context above. |

The separate `HQ449628|HQ449666|AEL22178|JQ080903|AGE12074` search returned zero lines across the same ignored-inclusive roots, with no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. These absence claims apply only to inspected roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, count, attestation and seed provenance agree. The record asserts no unsupported phenotype or genome links.

## Recommended Edits

None required.

Separately authorized enrichment should preserve exact accession and historical-name links and keep the positive 8AGV oxidation observation isolate- and condition-specific. Source fixes belong in maintained extraction or `src/taxonmech/seed.py` with tests. Do not invent a culture deposit, genome, species-level LPSN link or human-reviewed status.

## Follow-up Checks

After an authorized maintained-input change, use the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect the actual emitted TSV and generated fields.

Any quantitative phenotype enrichment requires exact supplementary isolate rows and conditions. Strain/genome links require source-backed culture identity and explicit matching chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Review/curation guidance, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the review skill, curation skill, checklist and justfile were reread this turn. The existing review branch is retained; the other session is closed.

The original 2011 publisher figure was viewed at original resolution. The full 2015 subscription article and supplementary assay values were not inspected for this target. No payment, access-control bypass or external message was attempted.

The YAML was byte-compared with the initial full read and remains unchanged. This report is the only new repository artifact for this target. No source inventory, generated product, history, prior report, Git/GitHub object or Eukaryota record was modified.
