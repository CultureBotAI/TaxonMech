# YAML Record Review: Allobosea sp. 7AGV

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/allobosea_sp_7agv.yaml`
- Started UTC: 2026-10-06T22:08:34Z
- Finished UTC: 2026-10-06T22:12:43Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read. `NCBITaxon:1035322` denotes Allobosea sp. 7AGV, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2653178`. Its assertions comprise ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotypes, citations or causal graphs are asserted. This generated YAML is read-only; future fixes belong in maintained source inputs, extraction/seeding code or scope decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/allobosea_sp_7agv.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/allobosea_sp_7agv.yaml --out /private/tmp/ab7-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and contains only its header.
- Structured source comparisons read the entire backbone row, all ancestors, direct children, seven other raw inventories, PATHS, scope, attestation and seed event. All compared assertions agree.
- Exact type-material, merged-ID and dropped-ID checks found no target entries.
- Ignored-inclusive compressed-file searches, lossless reads of all nineteen candidate rows, complete parsing of five SOURCE.json files and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 dataset rows inspected before external follow-ups. No applicable Allobosea/Bosea dataset. This is not negative biological evidence.
- Live NCBI taxonomy XML and Datasets taxonomy, exact Assembly/nuccore searches, all three sequence metadata records excluding bases/translations, and independent Datasets genome lookup succeeded.
- All ten ambiguous BioSamples were independently retrieved in full; returned accessions exactly match the requested set.
- The inspected primary-source context includes LPSN's genus page, both papers' PubMed metadata/abstracts, relevant 2011 publisher text and its original Figure 1, and the 2015 publisher abstract. The exact 7AGV row in Figure 1 was checked.
- Not checked: corpus-only reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, full 2015 article or supplementary assay tables. Bounded comparisons do not replace these gates.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222015`, scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31490`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035322&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035322) agree on current identity, label, rank, parent, domain and code.

Every lineage ID, label and normalized rank agrees: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria; Hyphomicrobiales; Alloboseaceae; Allobosea; unclassified Allobosea. Datasets includes root ID 1, omitted from EFetch's displayed chain. Pinned synonym fields and live alternate-name content are empty. No direct children occur in the pinned backbone.

[LPSN's Allobosea page](https://lpsn.dsmz.de/genus/allobosea) records Allobosea Deshmukh and Oren 2026 as the correct genus name and Bosea as an illegitimate homotypic synonym, under Alloboseaceae. This is genus context, not species-level attestation or a link to the genus type species.

Historical name continuity is directly evidenced by this isolate's sequence records: descriptions retain Bosea sp. 7AGV, whereas current source/organism features explicitly name Allobosea sp. 7AGV, strain 7AGV and taxon 1035322. Shared genus and study membership do not merge this isolate with 43AGV or 8AGV.

## Evidence

The sole source attestation correctly counts one NCBITAXON NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14506` supplies the exact slug, and `curation/seed_scope.tsv:322287` agrees with the event's scope reason. Parsed raw, ATB and StrainInfo manifests have extraction times 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z; their maximum matches the event under the inspected seed-timestamp rule. This is seeding provenance, not human review.

All three exact nuccore results were read:

| Accession | Record-specific evidence |
| --- | --- |
| [HQ449627.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449627.1), UID 338163869 | 833 bp partial 16S rRNA gene; W01/W02 primers |
| [HQ449665.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ449665.1), UID 342316563 | 903 bp partial aoxB CDS, annotated arsenite oxidase large subunit; AEL22177.1; codon_start 1 |
| [JQ080902.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ080902.1), UID 444747350 | 423 bp partial ACR3(2) CDS, annotated arsenite efflux pump; AGE12073.1; codon_start 1 |

Both CDS annotations use translation table 11. HQ source features specify arsenic-contaminated sediment at Sainte Marie aux Mines, France, with submission on 28-Oct-2010 from Strasbourg. JQ080902 specifies sediment from the same locality and submission on 25-Nov-2011 from Metz. These are gene sequences, not genomes or registered culture deposits. In particular, 7AGV's efflux accession is ACR3(2), not 43AGV's arsB record.

The HQ records cite [Heinrich-Salmeron et al. (2011), DOI 10.1128/AEM.02884-10](https://journals.asm.org/doi/10.1128/aem.02884-10), verified as PMID 21571879 and PMCID PMC3127681. Figure 1 identifies 7AGV Bosea sp. HQ449627 in pink, bold and underlined: group-I aoxB and a study PCR-positive isolate. Its row lacks the activity circle shown for 8AGV. This does not establish universal inability to oxidize arsenite or justify transferring 8AGV's activity.

JQ080902 cites [Cordi et al. (2015), DOI 10.1007/s11356-014-3840-5](https://link.springer.com/article/10.1007/s11356-014-3840-5), verified as PMID 25721523. The inspected abstract describes 219 isolates and genotype/sensitivity relationships, not an exact 7AGV assay row. No resistance threshold, medium-growth value or demonstrated efflux mechanism is assigned from the collection-level abstract.

Exact-organism Assembly search returned zero items with a phrase warning. Independent [Datasets genome lookup](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035322/dataset_report) returned an empty object. Neither bounded negative proves genome absence everywhere.

The ten [BioSamples SAMN10353220 through SAMN10353229](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353229%2C10353228%2C10353227%2C10353226%2C10353225%2C10353224%2C10353223%2C10353222%2C10353221%2C10353220&retmode=xml) independently resolve to human-associated Chinese samples collected in 2018, taxon 1869227 (bacterium), project PRJNA503135. None establishes identity with this French sediment isolate.

## Completeness

The current seeded assertions have no consequential demonstrated omission. Zero inventoried BacDive strains does not deny that a named isolate or partial sequences exist. Historical-name/gene enrichment is optional; traits, habitats and media belong to the appropriate sibling Mech resources.

The bounded search used `rg --no-ignore --hidden -n -z -i` with `1035322|\b7[-_ ]?AGV\b|(?:allo)?bosea_sp_7agv` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. Five SOURCE.json files and history filenames were checked separately.

All nineteen candidates were read losslessly: five JSON objects and fourteen TSV rows. Three are the exact backbone, scientific-name and scope entries. Sixteen are unrelated matches:

| Candidates | Exclusion evidence |
| --- | --- |
| Two run-number matches | BV-BRC 1773.18333 and ATB SAMEA3558855/ERR1035322/ERZ9334485 denote M. tuberculosis. The run number is not this TaxID. |
| One SeqKit substring | ATB SAMEA115750369/ERR13291222/ERZ26367082 denotes M. tuberculosis; the matching digits occur in a SeqKit sum. |
| Two assembly-size matches | GTDB GB_GCA_027040785.1 and GenBank GCA_027040785.1 describe bacterium S144_metabat2_scaf2bin.204, NCBI taxon 1869227, SAMN27359389, PRJNA821212, from a marine hydrothermal vent. Ungapped length 1035322 is not taxonomy. |
| One accession substring | GCA_010353225.1 denotes C. jejuni PNUSAC014903, taxon 197, SAMN13763547, PRJNA239251. |
| Ten unknown ATB samples | SAMN10353220 through SAMN10353229 are NOT_PROCESSED with no FASTA, run or assembly; authority records identify the unrelated samples described above. |

The separate `HQ449627|HQ449665|AEL22177|JQ080902|AGE12073` search found zero lines across the same ignored-inclusive roots, and no SOURCE.json/history-filename hits. Exact rows were absent from raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. These absence claims are limited to inspected roots and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, count, source attestation and seed provenance agree. The record makes no unsupported phenotype or genome claim.

## Recommended Edits

None required.

For separately authorized enrichment, retain the exact historical name and sequence identities without inferring a registered deposit, genome, species-level LPSN link or activity assay. Changes belong in maintained source extraction or `src/taxonmech/seed.py` with focused tests, never a hand edit to this YAML. No review-status promotion is warranted.

## Follow-up Checks

After an authorized maintained-source change, use the documented extraction/seeding workflow, `just verify-corpus`, schema validation and exact-target strict validation; inspect the emitted TSV and generated fields.

Phenotype enrichment requires an exact isolate-specific assay row and conditions. Strain/genome links require source-backed culture identity and explicit identifier chains. Full-corpus reproduction and QC remain unrun.

## Additional Notes

Review/curation guidance, checklist, relevant schema, harmonization and history rules were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the review skill was reread after context continuation. The existing review branch is retained, the other session is closed, and no extra worktree was created.

The original 2011 publisher figure was inspected at original resolution. The 2015 publisher page offers a subscription-content preview; the full paper and supplementary assay values were not inspected for this target. No payment, access-control bypass or external message was attempted.

The complete YAML was byte-compared with its initial read and remains unchanged. This report is the only new repository artifact for this target. No source inventory, generated product, history, prior report, Git/GitHub object or Eukaryota record was changed.
