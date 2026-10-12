# YAML Record Review: Bacillus sp. 21AAIII

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_21aaiii.yaml`
- Started UTC: 2026-10-06T21:59:49Z
- Finished UTC: 2026-10-06T22:02:45Z
- Verdict: pass

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:1035320` denotes Bacillus sp. 21AAIII, `SPECIES` in `BACTERIA`, parent `NCBITaxon:185979`. It carries ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graphs are asserted. Seeded YAML is read-only; source or harmonization corrections belong in maintained upstream inputs, extraction/seeding code or scope decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacillus_sp_21aaiii.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/bacillus_sp_21aaiii.yaml --out /private/tmp/bac21-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and is header-only.
- Structured comparisons read the complete backbone row, each ancestor, direct children, seven non-NCBI inventories, PATHS, scope, attestation and seed event; all compared assertions agree.
- Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive local searches, complete native candidate reads, parsing of five SOURCE.json files and independent history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0 with network access; all 28 dataset rows inspected before external follow-ups. Bacillus subtilis datasets `b_subtilis/modulome` and `b_subtilis/nicolas` do not establish coverage of 21AAIII. No exact applicable dataset; this is not negative biological evidence.
- Live NCBI taxonomy XML/JSON, exact Assembly/nuccore queries, complete metadata excluding sequence bases/translations for both nucleotide records, and an independent Datasets genome query succeeded.
- All ten ambiguous ATB BioSamples were fetched and read in full with an assertion that returned accessions exactly equal the requested complete accessions.
- The cited paper's metadata, relevant publisher text and Figure 1 were inspected during this review turn. The supplementary archive was unavailable: web fetching did not support ZIP content, and a direct read-only request returned HTTP 403.
- Not checked: full-corpus `just verify-corpus`, QC/history/provenance gates, full tests, rendering, source hashes, original-taxdump regeneration or supplementary assay rows. Manual comparisons do not replace corpus-only checks.

## Identity and Grounding

The backbone `data/raw/ncbitaxon_taxa.tsv:222013`, scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:31488`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035320&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035320) agree on exact identity, rank, parent, domain and code.

Each ancestor ID, label and normalized rank agrees: root; cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Bacillaceae; Bacillus; unclassified Bacillus (in: firmicutes). Datasets includes root ID 1, absent from EFetch's displayed lineage. Pinned synonym fields and live alternate-name content are empty; the backbone has no direct children.

Species rank does not establish a formal binomial or registered type strain. The generic Bacillus placement must not be replaced by B. subtilis, B. amyloliquefaciens or B. velezensis without source-backed identity evidence.

## Evidence

The NCBITAXON attestation counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14504` resolves this identifier to its exact stem; `curation/seed_scope.tsv:322285` supplies the seed event's scope reason. Parsed raw, ATB and StrainInfo manifest timestamps are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Their maximum matches the event under the inspected `_seed_timestamp` rule. It is provenance, not human review.

Exact nucleotide searches returned:

| Accession | Bounded annotation |
| --- | --- |
| [HQ449630.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449630.1), UID 338163872 | 765 bp partial 16S rRNA gene; W01/W02 primers noted |
| [HQ449648.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449648.1), UID 342316573 | 902 bp partial aoxB CDS, annotated arsenite oxidase large subunit; protein AEL22182.1; codon_start 3, translation table 11 |

Both source features explicitly name strain 21AAIII, taxon 1035320, arsenic-contaminated sediment from Sainte Marie aux Mines, France. Both were submitted 28-Oct-2010 from Universite de Strasbourg. These are gene records, not genome assemblies or registered culture deposits.

Both cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), verified as [PMID 21571879](https://pubmed.ncbi.nlm.nih.gov/21571879/) and PMCID PMC3127681. Figure 1 names 21AAIII/HQ449630. The text reports one assay-positive Bacillus isolate. Exact strain-level assay attribution remains pending supplementary inspection; no positive or negative phenotype is assigned here.

Exact-organism Assembly search returned zero items with a phrase warning. The independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035320/dataset_report) returned an empty object. These are bounded negative results, not global proof of genome absence.

All ten [BioSample records SAMN10353200 through SAMN10353209](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353209%2C10353208%2C10353207%2C10353206%2C10353205%2C10353204%2C10353203%2C10353202%2C10353201%2C10353200&retmode=xml) describe human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. None names 21AAIII or taxon 1035320, and their source context differs from the French sediment isolate.

## Completeness

The seeded identity is complete enough. Optional gene or assay context is not a missing required field. `strain_count: 0` counts BacDive inventory entries, not all biological isolates. GenBank strain qualifiers cannot be promoted to collection-deposit or genome evidence. Trait, habitat and medium curation belongs to sibling Mech resources.

The source search used `rg --no-ignore --hidden -n -z -i` with `1035320|21[-_ ]?AAIII\b|bacillus_sp_21aaiii` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files were parsed separately; history filenames were independently searched.

All eighteen candidate lines were read losslessly: five JSON objects and thirteen TSV rows. Three are the exact backbone, scientific-name and scope entries. Fifteen do not concern the target:

| Candidates | Exclusion evidence |
| --- | --- |
| Two run-number matches | BV-BRC 1773.18326 and ATB SAMEA3558853/ERZ9334481 identify M. tuberculosis ERR1035320, not Bacillus. |
| One assembly-accession substring | GCA_010353205.1 identifies C. jejuni PNUSAC014941, taxon 197, SAMN13825586, PRJNA239251, WGS AANOES000000000.1. |
| One N50 value | GTDB RS_GCF_028993875.1 concerns TA-1, NCBI B. amyloliquefaciens taxon 1390, GTDB B. velezensis, SAMN33406553. Both N50 values equal 1035320; neither is the target TaxID. |
| One genome-size value | GCA_977235085.1 is uncultured bacterium MarMAG_092378, taxon 77133, SAMEA120695844, PRJEB104710. Its genome_size is 1035320; that is not a taxonomic link. |
| Ten unknown ATB samples | SAMN10353200 through SAMN10353209 are NOT_PROCESSED with no FASTA, run or assembly; authority metadata independently resolves them to the unrelated samples described above. |

The separate `HQ449630|HQ449648|AEL22182` search found zero lines over the same ignored-inclusive roots and no metadata/history-filename hits. Exact target rows were absent from the raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. These absence statements are bounded to the inspected roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in existing assertions. Identity, lineage, grounding, count, attestation and seed event agree with inspected evidence. The unresolved optional assay follow-up is not an unsupported YAML claim.

## Recommended Edits

None required.

Any later authorized enrichment should preserve exact gene accessions and their limited roles. Source/harmonization changes belong in the maintained extractor or `src/taxonmech/seed.py`, with tests, not this YAML. Do not attach genomes from a related Bacillus species or promote a sample, gene, unregistered strain label or numerical match to a culture/genome link. This review does not authorize lifecycle promotion.

## Follow-up Checks

For authorized changes, follow the documented extraction/seeding workflow, run `just verify-corpus`, schema validation and exact-target strict validation, then inspect the actual TSV and regenerated fields.

Resolve the primary supplementary assay row and conditions before any functional enrichment. Supplement access remains unresolved, but no required current claim depends on it. Full-corpus QC and reproduction remain unrun.

## Additional Notes

Repository guidance, skills, checklist, relevant schema, harmonization and history documentation were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No target-only reproduction check was invented.

An initial scratch query accidentally omitted one digit from the BioSample accessions and returned zero hits. That result was discarded, not used as absence evidence. The corrected query used all ten explicit full accessions; all ten returned records were accession-checked and read.

The [public supplementary archive](https://journals.asm.org/doi/suppl/10.1128/AEM.02884-10/suppl_file/supplementary_material2.zip) could not be inspected. No access-control bypass, payment or external communication was attempted.

The target was byte-compared against its initial complete read and remains unchanged. This new report is the only repository artifact from this target review; no YAML, inventories, generated products, histories, prior reports, Git/GitHub objects or Eukaryota records were modified.
