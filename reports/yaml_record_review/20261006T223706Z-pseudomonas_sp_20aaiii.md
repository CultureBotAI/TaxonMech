# YAML Record Review: Pseudomonas sp. 20AAIII

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_20aaiii.yaml`
- Started UTC: 2026-10-06T22:35:14Z
- Finished UTC: 2026-10-06T22:37:06Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read. `NCBITaxon:1035328` denotes Pseudomonas sp. 20AAIII, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`. It asserts ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graphs are asserted. The generated YAML is read-only; future changes belong in maintained inputs, extraction/seeding logic or scope decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_20aaiii.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_20aaiii.yaml --out /private/tmp/ps20-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and is header-only.
- Structured comparisons read the full backbone row, every ancestor, direct children, seven other raw inventories, PATHS, scope, source attestation and seed event. Compared assertions agree.
- Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file searches, lossless reading of all seventeen candidate rows, complete parsing of five SOURCE.json files and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows inspected before this target's external follow-ups. Listed P. aeruginosa, P. putida and P. syringae datasets do not establish exact 20AAIII coverage.
- Live NCBI taxonomy XML and Datasets taxonomy, exact Assembly/nuccore searches, complete metadata excluding bases/translations for all four nucleotide hits, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSample records were independently retrieved in full, with exact returned-set agreement.
- Both cited papers' PubMed metadata/abstracts, relevant 2011 publisher text and original Figure 1, and the 2015 publisher abstract were inspected earlier in this same turn. The target's own accession and source-feature links were independently verified.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, full 2015 article or supplementary assay tables. Bounded comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222021`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31496`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035328&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035328) agree on identifier, label, rank, parent, domain and code.

Every ancestor ID, label and normalized rank agrees: root (1); cellular organisms (131567); Bacteria (2); Pseudomonadati (3379134); Pseudomonadota (1224); Gammaproteobacteria (1236); Pseudomonadales (72274); Pseudomonadaceae (135621); Pseudomonas (286); unclassified Pseudomonas (196821). Datasets supplies root ID 1, omitted from EFetch's displayed chain.

Pinned synonym fields and live alternate-name content are empty, with no direct children in the pinned backbone. NCBI species rank does not confer formal nomenclatural standing or a type designation. Shared genus, sampling site or study membership does not identify 20AAIII with another numbered isolate or named Pseudomonas species.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14512` supplies the exact stem; `curation/seed_scope.tsv:322293` agrees with the event's scope reason. Parsed raw, ATB and StrainInfo extraction times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected seed rule; it is not human sign-off.

All four exact nucleotide hits were read:

| Accession | Record-specific evidence |
| --- | --- |
| [HQ449631.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449631.1), UID 338163873 | 809 bp partial 16S rRNA gene, W01/W02 primers |
| [HQ449647.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449647.1), UID 342316571 | 902 bp partial aoxB CDS, arsenite oxidase large-subunit annotation; AEL22181.1; codon_start 3 |
| [JQ080825.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080825.1), UID 444747198 | 646 bp partial ACR3(1) CDS, arsenite efflux pump annotation; AGE11997.1; codon_start 1 |
| [JQ080755.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080755.1), UID 444747058 | 662 bp partial arsB CDS, arsenite efflux pump annotation; AGE11927.1; codon_start 2 |

All source features explicitly identify Pseudomonas sp. 20AAIII, strain 20AAIII and taxon 1035328. All three CDS annotations use translation table 11. HQ features identify arsenic-contaminated sediment from Sainte Marie aux Mines, France, submitted 28-Oct-2010 from Strasbourg. JQ features identify sediment from that locality, submitted 25-Nov-2011 from Metz. Partial sequence submissions are not genomes, registered culture deposits or demonstrations of transport function.

The HQ records cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), PMID 21571879, PMCID PMC3127681. Figure 1 labels 20AAIII Pseudomonas sp. HQ449631 in dark blue, bold and underlined, without an activity circle. This identifies a PCR-positive group-II aoxB isolate, not an oxidation-positive entry in that figure. The observation does not prove inactivity under all conditions.

The JQ records cite [Cordi et al. (2015), DOI 10.1007/s11356-014-3840-5](https://link.springer.com/article/10.1007/s11356-014-3840-5), PMID 25721523. Its inspected abstract covers collection-level genotype/sensitivity relationships, not a 20AAIII assay row. No quantitative resistance threshold, growth value or measured transporter mechanism was inferred.

Exact-organism Assembly search returned zero items with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035328/dataset_report) returned an empty object. These are bounded service results, not global genome-absence evidence.

All ten [BioSamples SAMN10353280 through SAMN10353289](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353289%2C10353288%2C10353287%2C10353286%2C10353285%2C10353284%2C10353283%2C10353282%2C10353281%2C10353280&retmode=xml) identify human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. None establishes a link to this French sediment isolate.

## Completeness

Current seeded assertions have no consequential demonstrated omission. Zero inventoried BacDive strains does not deny the study isolate or its partial sequences. Optional gene enrichment is not required for this taxonomy record; traits, habitats and media belong in the appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035328|\b20[-_ ]?AAIII\b|pseudomonas_sp_20aaiii` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files and history filenames were checked separately.

All seventeen candidates were read losslessly: four JSON objects and thirteen TSV rows. Three are exact backbone, name and scope entries; fourteen are unrelated:

| Candidates | Exclusion evidence |
| --- | --- |
| Two run-number matches | BV-BRC 1773.18345 and ATB SAMEA3558861/ERR1035328/ERZ9334498 denote M. tuberculosis. Run-number overlap is not taxonomy identity. |
| One historical assembly accession | Suppressed GCA_010353285.1 denotes C. jejuni PNUSAC014936, taxon 197, SAMN13825141, PRJNA239251; not-live date 2022-12-06. |
| One genome-size match | GCA_001830495.1 denotes Sideroxydans sp. RIFOXYB12_FULL_59_6, taxon 1802155, SAMN04316175, PRJNA288027; genome_size 1035328 is a measurement. |
| Ten unknown ATB samples | SAMN10353280 through SAMN10353289 are NOT_PROCESSED with no FASTA, run or assembly. Independent BioSample records resolve their unrelated context above. |

The separate `HQ449631|HQ449647|AEL22181|JQ080825|AGE11997|JQ080755|AGE11927` search found zero lines across the same ignored-inclusive roots and no metadata/history-filename hits. Exact target rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. These absence findings are bounded to inspected roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, count, source attestation and seed provenance agree. No unsupported phenotype, formal nomenclature or genome linkage is asserted.

## Recommended Edits

None required.

Separately authorized enrichment should retain exact isolate/accession chains and distinguish PCR/sequence evidence from demonstrated activity. Source fixes belong in maintained extraction or `src/taxonmech/seed.py` with tests, never a generated YAML hand edit. Do not infer a culture deposit, genome, quantitative phenotype or human-reviewed status.

## Follow-up Checks

After an authorized maintained-source change, use the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect the emitted TSV and generated fields.

Functional enrichment requires exact isolate-specific assay rows and conditions. Strain/genome links require source-backed culture identity and explicit matching chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Review/curation guidance, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the review skill was reread this turn. The dedicated review branch is retained, and the other session is closed.

The original 2011 publisher figure was inspected at original resolution in this turn. The full 2015 subscription article and supplementary assay values were not inspected for this target. No paid research, access-control bypass or external message was attempted.

The YAML was byte-compared with its initial full read and remains unchanged. This report is the only new repository artifact for this target. No source inventory, generated product, history, prior report, Git/GitHub object or Eukaryota record was modified.
