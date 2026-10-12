# YAML Record Review: Exiguobacterium sp. B1N2b

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/exiguobacterium_sp_b1n2b.yaml`
- Started UTC: 2026-10-06T23:24:33Z
- Finished UTC: 2026-10-06T23:27:22Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035346` denotes Exiguobacterium sp. B1N2b, rank SPECIES, domain BACTERIA, parent NCBITaxon:2644629. It asserts eleven root-first ancestors, genetic code 11, EXACT grounding, SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation and a seed event.

No synonyms, nomenclature, taxonomy mappings, strain listing, genomes, phenotype assertions, citations or causal graph are present. This is a generated record, not a maintained curator overlay.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/exiguobacterium_sp_b1n2b.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/exiguobacterium_sp_b1n2b.yaml --out /private/tmp/eb1-strict.tsv`: exit 0, one file, zero errors. The actual emitted TSV was read and is header-only.
- Exact backbone, every ancestor, direct children, seven other raw inventories, PATHS, scope, attestation and event comparisons passed. Type-material, merged-ID and dropped-ID checks found no exact target entry.
- All fourteen initial ignored-inclusive candidates and the one full-identifier follow-up candidate were read losslessly. Five SOURCE.json files were fully parsed and history filenames checked.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0, all 28 rows read before open-ended research. No covered organism/dataset matches B1N2b; iModulonDB was not applicable, not negative evidence.
- Live NCBI taxonomy XML/Datasets, exact Assembly/nuccore searches, full sequence metadata excluding bases/translations, independent Datasets genome lookup and PubMed metadata/abstract succeeded.
- The sequence-cited publisher article's methods, results, full Table 1 with footnotes, figure captions and discussion were inspected. The PMC browser page presented a challenge; publisher full text was available.
- Not checked: full-corpus reproduction, QC/history/provenance gates, tests, rendering, source hashes, original-taxdump regeneration or raw experimental data. No target-only reproduction gate is claimed.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:222033`, name object at `data/catalog/ncbi_names-0005.jsonl.gz:31508`, [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035346&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035346) agree on identifier, label, rank, parent, domain and code. Preserve the lowercase terminal b in the source label.

Every ancestor agrees in ID, label and normalized rank: root (1); cellular organisms (131567); Bacteria (2); Bacillati (1783272); Bacillota (1239); Bacilli (91061); Caryophanales (1385); Caryophanales incertae sedis (539002); Caryophanales Family XII. Incertae Sedis (539742); Exiguobacterium (33986); unclassified Exiguobacterium (2644629). Datasets independently supplies root ID 1. The two incertae-sedis entries are NO_RANK, including the one whose label contains Family.

Pinned synonym fields and live alternate-name content are empty; no pinned direct child was found. NCBI species rank is not formal nomenclatural standing or type status. B1N2b remains distinct from M2N2b, M2N2c and reference isolate M527; similar spellings, shared genus or study membership do not equate them.

## Evidence

The one NCBITAXON NAME attestation matches snapshot 2026-09-13. `data/taxa/PATHS.tsv:14524` fixes the stem and `curation/seed_scope.tsv:322305` agrees with the event reason. Parsed raw, ATB and StrainInfo timestamps are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z; their maximum matches the event under `src/taxonmech/seed.py`. SEEDED is not human review sign-off.

The sole exact nuccore hit is [JF795957.1](https://www.ncbi.nlm.nih.gov/nuccore/JF795957.1), UID 333826811, a 786-bp partial 16S rRNA sequence. Its source explicitly names B1N2b and taxon 1035346, root nodules and host fenugreek. Direct submission is dated 10-Apr-2011 by Rajendran and Patel at ARIBAS, Sardar Patel University, India; the submitter's address alone is not an isolation locality. No culture deposit, BioSample or assembly is asserted by this marker. Genetic code 11 is taxonomy metadata, not independently verified by a marker CDS.

The sequence and [PubMed 22518149](https://pubmed.ncbi.nlm.nih.gov/22518149/) identify Rajendran, Patel and Joshi's 2012 article, DOI [10.1155/2012/693982](https://onlinelibrary.wiley.com/doi/10.1155/2012/693982), PMC3299478. Its results explicitly pair B1N2b with JF795957, distinguish the other isolates, and report 97% partial-16S identity to M527, not strain equivalence. Table 1 gives B1N2b its own row. Plant experiments used coinoculation with S. meliloti, triplicates and a 55-day harvest. These bounded observations do not prove standalone nitrogen fixation, a whole-genome relationship or formal species assignment. The historical family terminology does not supersede the current NCBI lineage.

Exact Assembly search returned zero with a phrase-not-found warning; the independent [Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035346/dataset_report) returned an empty object. These are dated, bounded results, not a universal genome-absence claim.

## Completeness

Initial ID, separator-tolerant B1N2b and stem searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included.

Fourteen initial rows comprise three exact identity/scope rows and eleven numerical false matches:

- Mycobacterium tuberculosis ERR1035346, taxon 1773: BV-BRC 1773.18364 at `data/bvbrc/bvbrc-0006.jsonl.gz:6162` and ATB SAMEA3558879/ERR1035346/ERZ9334528 at `data/catalog/allthebacteria.tsv.xz:569816`.
- Microcystis aeruginosa FACHB-524, taxon 2486203, species taxon 1126: five rows across BV-BRC 2486203.3, GenBank GCA_003730145.1, RefSeq GCF_003730145.1, GTDB RS_GCF_003730145.1 and GOLD project Gp0393281. They name SAMN10353469, not taxon 1035346. GOLD associates Go0508571/PRJNA503142; GenBank and BV-BRC also use PRJNA503142, while RefSeq/GTDB use PRJNA224116. GTDB's separate classification is Microcystis ichthyoblabe_A. Neither the sample substring nor the genuine but unrelated FACHB deposit establishes a B1N2b link.
- Campylobacter jejuni CFSAN096324, taxon 197: GCA_010353465.2 is latest; historical GCA_010353465.1 is replaced, not live since 2020-03-16. Both use SAMN13656983/PRJNA258022.
- Candidatus Magasanikiibacteriota bacterium SI075_bin157, taxon 2026717: GCA_018658985.1, SAMN14915687, PRJNA630981. The matched number is its genome length, 1035346.
- Bacillus sp. SIMBA_033, taxon 3085776: GTDB RS_GCF_046535195.1, GCA_046535195.1, SAMN37992173, PRJNA224116. The matched number is contig N50, not taxon identity; GTDB classifies it as Bacillus velezensis.

Follow-up searches for JF795957, PMID digits 22518149 and the full DOI yielded one additional full row: `data/catalog/ncbi_genbank-0044.jsonl.gz:21313`, Salmonella enterica serovar Muenster strain FSIS22518149, taxon 82689, GCA_048160595.1, SAMN47108730, PRJNA242847. Its strain suffix is not a citation; its pubmed_id is empty. No target accession or full-DOI evidence was found in the bounded roots or separately parsed source metadata/history names.

The exact BacDive inventory and empty descendant set support zero inventoried strains. This count does not deny the existence of the biological isolate. No missing required nomenclature, strain, mapping or genome assertion was established. Optional literature and marker context need not be forced into unsupported genome links. Traits, habitats, media and ecological interactions belong in their appropriate sibling repositories.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated assertions. The public literature adds strain-specific context without exposing a missing required TaxonMech field.

## Recommended Edits

None required. Do not hand-edit the generated record or promote SEEDED to REVIEWED. Do not assign a species, culture deposit, genome or nitrogen-fixation phenotype from name similarity, marker similarity or coinoculation alone.

Any future supported identity/deposit enrichment belongs in maintained source ingestion, including `scripts/extract_source_inventory.py`, followed by the documented seeder workflow. Optional literature needs a representation that survives regeneration. Route experimentally scoped phenotype, habitat, media and interaction evidence to sibling repositories.

## Follow-up Checks

After authorized source changes, repeat the exact-target schema/strict checks and inspect the TSV. Generator/source changes additionally require the documented canary and full `just verify-corpus`/QC gates.

Require an exact culture-deposit or supported sample/source chain for future genome associations. Preserve database-specific identifiers, versions and historical statuses. Keep the B1N2b spelling and its exact sequence pairing distinct from the other strains in the paper.

## Additional Notes

An exploratory search on the bare article number 693982 was overbroad and was replaced by the full-DOI/accession/publication-ID query above; its incidental hits were not used as identity evidence. No absent-source conclusion relies on an ignored-aware search.

Guidance and generation/history boundaries were inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The YAML remains byte-identical to its initial full read. Only this new report is written; no source input, generated product, prior report, history record, event or lifecycle status is changed. Eukaryota remains untouched.
