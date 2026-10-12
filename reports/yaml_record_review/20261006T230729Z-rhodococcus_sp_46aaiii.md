# YAML Record Review: Rhodococcus sp. 46AAIII

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhodococcus_sp_46aaiii.yaml`
- Started UTC: 2026-10-06T23:05:13Z
- Finished UTC: 2026-10-06T23:07:29Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035336` denotes Rhodococcus sp. 46AAIII, rank SPECIES, domain BACTERIA, parent NCBITaxon:192944. It asserts ten root-first ancestors, genetic code 11, EXACT grounding, SEEDED mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graph are asserted. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/rhodococcus_sp_46aaiii.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/rhodococcus_sp_46aaiii.yaml --out /private/tmp/rh46-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and is header-only.
- Full backbone, every ancestor, direct children, seven other raw inventories, PATHS, scope, attestation and seed-event comparisons agree. Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file searches completed. All sixteen initial candidates were read losslessly; five SOURCE.json files were parsed fully, and history filenames checked.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows inspected before external follow-ups. No covered organism/dataset matches Rhodococcus sp. 46AAIII. iModulonDB was not applicable, not negative evidence.
- Live NCBI taxonomy XML and Datasets taxonomy, exact Assembly/nuccore searches, full metadata excluding bases/translations for both nucleotide hits, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSamples were retrieved in full, with exact requested/returned-set agreement.
- The sequence-cited paper's PubMed metadata/abstract, relevant publisher text and original Figure 1 were inspected.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration or supplementary assay tables. Bounded comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222029`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31504`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035336&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035336) agree on identifier, label, rank, parent, domain and code.

Every ancestor ID, label and normalized rank agrees: root (1); cellular organisms (131567); Bacteria (2); Bacillati (1783272); Actinomycetota (201174); Actinomycetes (1760); Mycobacteriales (85007); Nocardiaceae (85025); Rhodococcus (1827); unclassified Rhodococcus (in: high G+C Gram-positive bacteria) (192944). Datasets supplies root ID 1, omitted from EFetch's displayed lineage.

Pinned synonym fields and live alternate-name content are empty; the pinned backbone has no direct children. NCBI species rank is not formal nomenclatural standing or type status. Shared genus, sampling site, study membership or a matching numeric substring does not equate this isolate with another taxon.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14520` supplies the exact stem; `curation/seed_scope.tsv:322301` agrees with the event's scope reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected seed rule; this is not human sign-off.

Both exact nucleotide records were read:

| Accession | Exact-target metadata |
| --- | --- |
| [HQ449640.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449640.1), UID 338163882 | 804 bp partial 16S rRNA gene; W01/W02 primers |
| [HQ449659.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449659.1), UID 342316595 | 519 bp partial aoxB CDS; arsenite oxidase large-subunit annotation; AEL22193.1; codon_start 3; translation table 11 |

Both source features explicitly identify Rhodococcus sp. 46AAIII, strain 46AAIII and taxon 1035336. They identify arsenic-contaminated sediment from Sainte Marie aux Mines, France, with direct submission on 28-Oct-2010 from Strasbourg. Partial genes are not genomes or registered culture deposits; the CDS annotation alone does not establish enzyme activity or a quantitative resistance phenotype.

Both records cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), PMID 21571879, PMCID PMC3127681. Original Figure 1 explicitly labels 46AAIII Rhodococcus sp. HQ449640 in dark blue, bold and underlined, without an activity circle. It supports PCR-positive group-II aoxB, without detected oxidation in the reported assay. This does not establish universal inability to oxidize arsenite. No quantitative resistance threshold or growth value was inferred.

Exact-organism Assembly search returned zero with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035336/dataset_report) returned an empty object. These bounded service results do not prove global genome absence.

All ten [BioSamples SAMN10353360 through SAMN10353369](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353369%2C10353368%2C10353367%2C10353366%2C10353365%2C10353364%2C10353363%2C10353362%2C10353361%2C10353360&retmode=xml) identify human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. They are not identity evidence for this French sediment isolate.

## Completeness

No consequential omission was demonstrated in the current seeded assertions. Zero inventoried BacDive strains does not deny the named study isolate or its sequences. Optional functional enrichment is not required for this taxonomy record; traits, habitats and media belong to appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035336|\b46[-_ ]?AAIII\b|rhodococcus_sp_46aaiii` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files and history filenames were checked separately.

All sixteen candidates were read: three JSON objects and thirteen TSV rows. Three are exact backbone, name and scope entries; thirteen are unrelated:

| Candidates | Exclusion evidence |
| --- | --- |
| Two run-number matches | BV-BRC 1773.18353 and ATB SAMEA3558869/ERR1035336/ERZ9334510 denote Mycobacterium tuberculosis. A run accession is not this TaxID. |
| One GenBank accession substring | GCA_010353365.1 denotes Campylobacter jejuni PNUSAC014925, taxon 197, SAMN13821809, PRJNA239251. |
| Ten unknown ATB samples | SAMN10353360 through SAMN10353369 are NOT_PROCESSED with no FASTA, assembly or run. Their independent BioSample metadata resolves the unrelated context above. |

The separate `HQ449640|HQ449659|AEL22193` search found zero lines across the same ignored-inclusive roots, with no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. Absence findings are bounded to these roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, grounding, count, attestation and seed provenance agree. The record asserts no unsupported phenotype, nomenclatural status or genome linkage.

## Recommended Edits

None required.

Separately authorized enrichment must retain exact isolate/accession chains and assay scope. Do not convert an aoxB annotation into a measured phenotype. Source corrections belong in maintained extraction inputs or `src/taxonmech/seed.py` with tests, not generated YAML. Do not infer a culture deposit, genome or human-reviewed status.

## Follow-up Checks

After an authorized maintained-source change, use the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect emitted TSV and generated fields.

Functional enrichment requires exact isolate-specific assays and conditions. Genome links require explicit source-backed identity chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Repository guidance, review/curation skills, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the review skill was reread this turn. The dedicated review branch remains in use; the other session is closed.

The original publisher figure was visually inspected at original resolution. Supplementary assay values were not inspected. No paid research, access-control bypass or external message was attempted.

The YAML was byte-compared with its initial full read and remains unchanged. This report is the only new repository artifact for this target. No source inventory, generated product, history, prior report, Git/GitHub object or Eukaryota record was modified.
