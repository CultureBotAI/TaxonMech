# YAML Record Review: Pseudomonas sp. 8AAV

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_8aav.yaml`
- Started UTC: 2026-10-06T23:01:23Z
- Finished UTC: 2026-10-06T23:03:24Z
- Verdict: pass

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:1035335` denotes Pseudomonas sp. 8AAV, rank SPECIES, domain BACTERIA, parent NCBITaxon:196821. Assertions comprise ten root-first ancestors, genetic code 11, EXACT grounding, SEEDED mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graph are asserted. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_8aav.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_8aav.yaml --out /private/tmp/ps8-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and is header-only.
- Full backbone, every ancestor, direct children, seven other raw inventories, PATHS, scope, attestation and seed-event comparisons agree. Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file searches completed. All twenty initial candidates were read losslessly; five SOURCE.json files were parsed fully, and history filenames checked.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows inspected before external follow-ups. Other Pseudomonas datasets do not establish exact 8AAV coverage. iModulonDB was not applicable, not negative evidence.
- Live NCBI taxonomy XML and Datasets taxonomy, exact Assembly/nuccore searches, full metadata excluding bases/translations for all three nucleotide hits, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSamples were retrieved in full with exact requested/returned-set agreement.
- Both sequence-cited papers' PubMed metadata/abstracts, relevant 2011 publisher text and original Figure 1, and the 2015 publisher abstract were inspected in this review turn.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, full 2015 article or supplementary assay tables. Bounded comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222028`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31503`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035335&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035335) agree on identifier, label, rank, parent, domain and code.

Every ancestor ID, label and normalized rank agrees: root (1); cellular organisms (131567); Bacteria (2); Pseudomonadati (3379134); Pseudomonadota (1224); Gammaproteobacteria (1236); Pseudomonadales (72274); Pseudomonadaceae (135621); Pseudomonas (286); unclassified Pseudomonas (196821). Datasets supplies root ID 1, omitted from EFetch's displayed lineage.

Pinned synonym fields and live alternate-name content are empty, with no direct children in the pinned backbone. NCBI species rank is not formal nomenclatural standing or type status. Shared genus, study membership or locality does not equate 8AAV with another isolate.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14519` supplies the exact stem; `curation/seed_scope.tsv:322300` agrees with the event's scope reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected seeding rule, without implying human sign-off.

All three exact nucleotide records were inspected:

| Accession | Exact-target metadata |
| --- | --- |
| [HQ449636.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449636.1), UID 338163878 | 809 bp partial 16S rRNA gene; W01/W02 primers |
| [HQ449651.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449651.1), UID 342316579 | 902 bp partial aoxB CDS; arsenite oxidase large-subunit annotation; AEL22185.1; codon_start 3 |
| [JQ080836.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080836.1), UID 444747220 | 658 bp partial ACR3(1) CDS; arsenite efflux pump annotation; AGE12008.1; codon_start 1 |

All source features explicitly identify Pseudomonas sp. 8AAV, strain 8AAV and taxon 1035335. Both CDS annotations use translation table 11. HQ records identify arsenic-contaminated sediment from Sainte Marie aux Mines, France, submitted 28-Oct-2010 from Strasbourg. The JQ record identifies sediment from that locality, submitted 25-Nov-2011 from Metz. Partial genes are not genomes or registered deposits; an efflux-pump annotation alone does not prove transporter activity.

The HQ records cite [Heinrich-Salmeron et al. (2011)](https://journals.asm.org/doi/10.1128/aem.02884-10), DOI 10.1128/AEM.02884-10, PMID 21571879, PMCID PMC3127681. Figure 1 labels 8AAV/HQ449636 dark blue, bold and underlined, without an activity circle: PCR-positive group-II aoxB, not detected oxidation in that assay. Universal inactivity is not established.

The JQ record cites [Cordi et al. (2015)](https://link.springer.com/article/10.1007/s11356-014-3840-5), DOI 10.1007/s11356-014-3840-5, PMID 25721523. Its inspected abstract contains no exact 8AAV assay row. No quantitative resistance threshold, growth value or demonstrated transporter mechanism was inferred.

Exact-organism Assembly search returned zero with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035335/dataset_report) returned an empty object. These are bounded service results, not global genome-absence evidence.

All ten [BioSamples SAMN10353350 through SAMN10353359](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353359%2C10353358%2C10353357%2C10353356%2C10353355%2C10353354%2C10353353%2C10353352%2C10353351%2C10353350&retmode=xml) identify human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. They are not identity evidence for this French sediment isolate.

## Completeness

No consequential omission was demonstrated in the current seeded assertions. Zero inventoried BacDive strains does not deny the named study isolate or its sequences. Optional functional enrichment is not required for this seeded taxonomy record; traits, habitats and media belong in their appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035335|\b8[-_ ]?AAV\b|pseudomonas_sp_8aav` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files and history filenames were checked separately.

All twenty candidates were read: seven JSON objects and thirteen TSV rows. Three are exact backbone, name and scope entries; seventeen are unrelated:

| Candidates | Exclusion evidence |
| --- | --- |
| Two run-number matches | BV-BRC 1773.18351 and ATB SAMEA3558868/ERR1035335/ERZ9334509 denote Mycobacterium tuberculosis. A run accession is not this TaxID. |
| One metagenome assembly substring | GCA_061035335.1 denotes Evtepia gabavorous, isolate 1937_1937H_C_8, taxon 2211183, SAMN60704088, PRJNA1464738. |
| Three versions of an unrelated assembly | GCA_031035335.1 and .2 are replaced; .3 is latest. All denote Klebsiella pneumoniae isolate 1922566, taxon 573, SAMN34998276, PRJNA288601. Version history does not create a Pseudomonas identity link. |
| One ungapped-length match | GCA_977308645.1 denotes uncultured bacterium MarMAG_092299, taxon 77133, SAMEA120697363, PRJEB104710. Ungapped length 1035335 is a measurement, not a TaxID. |
| Ten unknown ATB samples | SAMN10353350 through SAMN10353359 are NOT_PROCESSED with no FASTA, assembly or run. Their independent BioSample metadata resolves the unrelated context above. |

The separate `HQ449636|HQ449651|AEL22185|JQ080836|AGE12008` search found zero lines across the same ignored-inclusive roots, with no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. Absence findings are bounded to these roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, grounding, count, attestation and seed provenance agree. The record asserts no unsupported phenotype, nomenclatural status or genome linkage.

## Recommended Edits

None required.

Separately authorized enrichment must retain exact isolate/accession chains and assay scope. Do not convert aoxB or ACR3(1) annotations into measured phenotypes. Source corrections belong in maintained extraction inputs or `src/taxonmech/seed.py` with tests, not generated YAML. Do not infer a culture deposit, genome or human-reviewed status.

## Follow-up Checks

After an authorized maintained-source change, use the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect emitted TSV and generated fields.

Functional enrichment requires exact isolate-specific assays and conditions. Genome links require explicit source-backed identity chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Repository guidance, review/curation skills, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The dedicated review branch remains in use; the other session is closed.

The original 2011 publisher figure was visually inspected at original resolution. The full 2015 subscription article and supplementary assay values were not inspected. No paid research, access-control bypass or external message was attempted.

The YAML was byte-compared with its initial full read and remains unchanged. This report is the only new repository artifact for this target. No source inventory, generated product, history, prior report, Git/GitHub object or Eukaryota record was modified.
