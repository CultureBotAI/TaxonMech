# YAML Record Review: Cryobacterium sp. NA-9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/cryobacterium_sp_na_9.yaml`
- Started UTC: 2026-10-06T23:39:45Z
- Finished UTC: 2026-10-06T23:43:04Z
- Verdict: pass

## Target

The entire generated TaxonRecord was read. NCBITaxon:1035349 denotes Cryobacterium sp. NA-9, rank SPECIES, domain BACTERIA, parent NCBITaxon:2649013. The record has ten root-first ancestors, code 11, EXACT grounding, SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event. Synonyms, nomenclature, mappings, strain/genome listings, phenotype claims, citations and causal graphs are not populated. The YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/cryobacterium_sp_na_9.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/cryobacterium_sp_na_9.yaml --out /private/tmp/cna9-strict.tsv`: exit 0, one file, zero errors. The emitted TSV was read and is header-only.
- Exact backbone, every ancestor, children, seven other raw inventories, PATHS, scope and attestation comparisons passed. Type-material, merged-ID and dropped-ID inventories have no exact target row.
- All 69 ignored-inclusive candidates were read losslessly: 46 JSON objects and 23 TSV rows. One initially truncated assembly read was repeated in full before judgment. SOURCE.json metadata and history filenames were checked separately.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows read before web research. No covered organism/dataset matches NA-9; not applicable, not negative evidence.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, full sequence metadata excluding bases/translations and Datasets genome lookup succeeded. Both literature leads were checked in PubMed metadata/abstracts and publisher previews.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration, primary-paper full texts or raw experimental data. Bounded checks do not reproduce the corpus.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222036`, name object at `data/catalog/ncbi_names-0005.jsonl.gz:31511`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035349&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035349) agree on identifier, label, rank, parent, domain and code.

All ancestor IDs, labels and normalized ranks agree: root (1); cellular organisms (131567); Bacteria (2); Bacillati (1783272); Actinomycetota (201174); Actinomycetes (1760); Micrococcales (85006); Microbacteriaceae (85023); Cryobacterium (69578); unclassified Cryobacterium (2649013). Datasets independently includes root ID 1. The unclassified parent is NO_RANK.

Pinned synonyms and live alternate names are empty, with no pinned direct children. NCBI species rank is not formal nomenclatural standing or type-strain status. NA-9 is not MB-5, an arbitrary NA9 from another genus, or a named Cryobacterium species inferred from marker similarity.

## Evidence

The NCBITAXON attestation is exactly one NAME in snapshot 2026-09-13. `data/taxa/PATHS.tsv:14527` and `curation/seed_scope.tsv:322308` agree with the stem and event reason. Parsed raw, ATB and StrainInfo manifest timestamps are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z; their maximum matches the event under the inspected `src/taxonmech/seed.py` rule. This review does not promote SEEDED.

Only [JF790966.1](https://www.ncbi.nlm.nih.gov/nuccore/JF790966.1), UID 335331576, was returned by exact nuccore search. This is an 806-bp partial 16S rRNA sequence, explicitly naming strain NA-9 and taxon 1035349. Source metadata place it in cryoconite-hole soil from Austre Broggerbreen glacier, Svalbard: Ny-Alesund. The 8-Apr-2011 direct submission names Singh, Singh and two Dhakephalkar authors at BITS Goa. Its research reference remains marked Unpublished. No deposit, BioSample, assembly or CDS is supplied; the Indian submitter address is not the isolation locality.

[PMID 24283367](https://pubmed.ncbi.nlm.nih.gov/24283367/) identifies Singh, Hanada, Singh and Tsuda's 2014 antifreeze study, [DOI 10.1111/1574-6968.12345](https://academic.oup.com/femsle/article-abstract/351/1/14/501000). Its inspected PubMed DataBankList explicitly includes JF790966. The abstract concerns multiple isolates and does not establish NA-9's result. A teaching-slide search hit suggests the alias Cry-9, but its copied table was not accepted as primary evidence. No positive or negative antifreeze phenotype is asserted here.

A recent rice-straw paper's reference trail led to the original diversity/enzyme study, [PMID 24346230](https://pubmed.ncbi.nlm.nih.gov/24346230/), [DOI 10.1007/s00792-013-0609-6](https://link.springer.com/article/10.1007/s00792-013-0609-6), by Singh, Singh and Dhakephalkar, published online in 2013 and in the 2014 volume. Its inspected abstract highlights other isolates, including MLB-32, not NA-9-specific enzyme results. The publisher provides a subscription preview. A secondary NA-9 cellulase attribution remains a lead requiring the original strain row and conditions; no such phenotype is imported.

Exact Assembly search returned zero with a phrase-not-found warning, while [Datasets genome](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035349/dataset_report) returned an empty object. These dated results do not prove worldwide genome absence.

## Completeness

The initial regex combined taxon ID, separator-tolerant NA9 and record stem. It used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. All candidate values were inspected, not sampled.

Three rows are the exact name/backbone/scope records. The five other name concepts, each with name/backbone/scope rows, are Agreia sp. CJ-G-NA9 (1052621), Salinibacter sp. NA9-35 (1397534), NA9-38 (1397535), NA9-83 (1397536), and Campylobacter sp. VBCF_03 NA9 (2983839).

Other nonmatching evidence is distinguished as follows:

- Vibrio parahaemolyticus NA9, taxon 670: BV-BRC 670.1373, GCA/GCF_002880435.1, GTDB RS_GCF_002880435.1, SAMN08329241 and PRJNA429067. Native metadata describe Malaysian aquaculture pond water, not this Arctic Cryobacterium.
- Campylobacter sp. VBCF_03 NA9: BV-BRC 2983839.3, GCA/GCF_027737105.1, SAMN31141461 and PRJNA886670. GTDB RS_GCF_027737105.1 is classified Campylobacter_B sp017934385 and describes Austrian rumen epithelial tissue. GOLD Go0677357, Gp0779171 and Ga0628683/IMG 8085915604 retain the sample/project/assembly chain; the analysis organism-ID field is empty. These objects do not identify NA-9.
- Xanthomonas citri pv. citri NA9: taxon 611301, species taxon 346, GCA_050074715.1, SAMN35800537 and PRJNA977242, at `data/catalog/ncbi_genbank-0046.jsonl.gz:10372`.
- Mycobacterium tuberculosis ERR1035349, taxon 1773: BV-BRC 1773.18362 and ATB SAMEA3558882/ERR1035349/ERZ9334536. The run suffix is not a taxon ID.
- GOLD Gp0276532/SAMN03451634/PRJNA279700 is a Dianchi lake community metatranscriptome with NA9 in its site designation; Gp0840874/SAMN35688650/PRJNA982183 is a Tibetan lake community. Neither is an isolate genome.

RefSeq/GTDB BioProject PRJNA224116 remains source-specific umbrella metadata, not a replacement for GenBank study accessions. GOLD organism/project/analysis identifiers, IMG genome identifiers, samples and assemblies remain distinct.

The remaining 35 numeric matches concern ten E. coli samples, taxon 562 and PRJNA218110: eight BV-BRC rows, ten current and six historical GenBank rows, ten ATB rows and GOLD Gp0386980/Go0502703 for SAMN10353494.

| BioSample | E. coli strain | Current GenBank | ATB analysis |
|---|---|---|---|
| SAMN10353490 | PNUSAE015624 | GCA_003774025.2 | ERZ9092865 |
| SAMN10353491 | PNUSAE019805 | GCA_003760205.2 | ERZ25499673 |
| SAMN10353492 | PNUSAE019342 | GCA_003756705.2 | ERZ9092868 |
| SAMN10353493 | PNUSAE019329 | GCA_003768925.2 | ERZ9092869 |
| SAMN10353494 | PNUSAE019328 | GCA_003757365.1 | ERZ9092873 |
| SAMN10353495 | PNUSAE019327 | GCA_003770005.2 | ERZ9092874 |
| SAMN10353496 | PNUSAE019326 | GCA_016555825.1 | ERZ9092877 |
| SAMN10353497 | PNUSAE019646 | GCA_003757225.1 | ERZ9092878 |
| SAMN10353498 | PNUSAE019645 | GCA_016555865.1 | ERZ9092882 |
| SAMN10353499 | PNUSAE019644 | GCA_003769865.2 | ERZ9092881 |

The six historical .1 assemblies were replaced on 2020-03-07; two other .1 accessions remain current, so versions cannot be normalized by assumption. BV-BRC preserves the older identifiers. ATB retains full run IDs, SeqKit sums and PASS/available-FASTA metadata; availability does not turn these into target matches.

Secondary ignored-inclusive searches for JF790966, Cry-9, both PMIDs and both full DOIs found no matches in the same roots. Five SOURCE.json files were fully parsed and history filenames checked separately. These bounded misses do not deny external literature.

Zero inventoried BacDive strains agrees with the exact inventory and empty child set, not a claim that NA-9 was never isolated. No missing required nomenclature, mapping, deposit or genome representation was established. Optional literature, marker and experimental fields need not be invented for this seeded record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated assertions. Primary strain-level experimental results remain unverified, but no such result is asserted by the record.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status; do not import NA9 homonyms or represent JF790966.1 as a genome.

Future supported strain/deposit enrichment belongs in maintained source ingestion, including `scripts/extract_source_inventory.py`, followed by the documented seeder workflow. Optional literature needs a maintained representation that survives regeneration. Trait, habitat, medium and interaction evidence belongs in the corresponding sibling repositories.

## Follow-up Checks

Obtain lawful primary full text before resolving Cry-9 or assigning an NA-9-specific enzyme/antifreeze phenotype. Preserve exact isolate identity and experimental conditions.

After authorized upstream changes, repeat both exact-target validators and inspect the emitted TSV. Source/generator changes additionally require the documented canary and full `just verify-corpus`/QC gates; no target-only reproduction gate is claimed.

## Additional Notes

Local guidance and generation boundaries were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The YAML remains byte-identical to its initial complete read. Only this timestamped report is written; source inputs, generated products, prior reports, history events and lifecycle status are unchanged. Eukaryota remains untouched.
