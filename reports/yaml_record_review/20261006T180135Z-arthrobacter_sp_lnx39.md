# YAML Record Review: Arthrobacter sp. LNX39

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_lnx39.yaml`
- Started UTC: 2026-10-06T17:55:21Z
- Finished UTC: 2026-10-06T18:01:35Z
- Verdict: pass

## Target

The fully read generated TaxonRecord denotes NCBITaxon:1035245, Arthrobacter sp. LNX39, rank SPECIES, domain BACTERIA, parent NCBITaxon:235627, genetic code 11, grounding EXACT and status SEEDED. It contains ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, phenotype assertion, discussion or graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14455`; scope is `curation/seed_scope.tsv:322239`. HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Eukaryota was not reopened.

## Validation

The review skill, checklist and CLAUDE.md were reread. Curation guidance, justfile, CURATION, HARMONIZATION, SCHEMA, history guidance, source boundaries and relevant schema/seeder had been inspected at this unchanged revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/arthrobacter_sp_lnx39.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/arthrobacter_sp_lnx39.yaml --out /private/tmp/alnx-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Bounded manual comparisons confirmed identity, every ancestor, path/scope, attestation and event. These are not a focused corpus-reproduction validator.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates or global `just validate-history`. Corpus reproduction has no target selector; no corpus-wide reproducibility/reference-integrity claim is made.
- `just validate-products` was not run: curator-added graph grounding is absent, and its configured gate skips NCBITaxon. Taxonomic identifiers were checked against pinned and live authority data.
- Ignored-inclusive content/path searches found no target external history artifact within the searched history tree. No history or status mutation was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were inspected; none covers Arthrobacter. Not applicable, not negative biological evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221964` supports the identifier, exact label, rank, parent, code 11, empty synonyms and 2026-09-13 snapshot. The scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31432`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035245&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035245) agree. Every stored ancestor label/rank matches the pinned root-first chain: root (1), cellular organisms (131567), Bacteria (2), Bacillati (1783272), Actinomycetota (201174), Actinomycetes (1760), Micrococcales (85006), Micrococcaceae (1268), Arthrobacter (1663), unclassified Arthrobacter (235627). XML omits root in LineageEx; Datasets includes it.

SPECIES is NCBI's rank for this strain-labelled taxon, not proof of a formally named species. EXACT identifies this source concept, not nomenclatural validity. The relevant nomenclature/classification text on the [LPSN genus page](https://lpsn.dsmz.de/genus/arthrobacter) was inspected, and its full-page text search found no LNX39. Genus-level conserved/valid/correct status and the type species Arthrobacter globiformis are not the target's nomenclature or type strain. No exact LPSN mapping occurs in the pinned inventory.

## Evidence

The NCBITAXON attestation matches identifier, label, count 1, unit NAME and snapshot. The seed event at 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree. This is a source-name assertion count, not a genome or biological strain count.

No exact target row occurs in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone child has this taxon as parent. Zero inventoried strains agrees with the own/subtree BacDive gathering rule in `src/taxonmech/seed.py:488`; it does not assert that this organism has never been cultured.

The exact live query `txid1035245[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 334145784. Full [JF799944.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF799944.1), excluding bases, was inspected: 1422 nt, partial 16S rRNA, strain LNX39, explicit taxon:1035245 and geographic qualifier Spain: Granada. Submitted 11 April 2011 by L. Santa Cruz Calvo; created/updated 10 May 2012. It supplies no culture deposit, BioSample, BioProject or assembly identifier. Its bibliography is direct submission only, with no PMID or DOI. Genomic DNA and a ribosomal marker are not a genome assembly.

A primary [WIT Press paper](https://www.witpress.com/Secure/elibrary/papers/ETOX10/ETOX10012FU1.pdf), DOI 10.2495/ETOX100121, was downloaded after the web reader failed. All ten pages were text-inspected, and page 125/Figure 1 was rendered and visually inspected. The 2010 study plots LNX39 separately from LPX39 and other isolates in desiccation testing. Methods describe 24-hour drying whereas results describe 48-hour desiccation; this discrepancy remains unresolved. Subsequent plant tests use genus-only labels, without an explicit LNX39-to-Arthrobacter assignment in the inspected paper. It gives no JF799944 accession bridge. Matching designation, location and author context make this a relevant literature lead, not proof that every study-level result belongs to this taxon. No plant-growth, PAH-removal, habitat or quantitative survival claim is transferred into the YAML.

## Completeness

Ignored and compressed content was included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, exact label and slug returned 18 rows: three genuine target rows and fifteen unrelated numeric matches. All candidate native JSON/TSV rows, including nested fields and the compressed ATB row, were read losslessly. Five SOURCE.json documents were separately parsed without a target value; history filenames were enumerated independently of ignore rules.

The same-root expanded strain-designation search for LNX39/LNX-39/LNX 39 returned only the three genuine rows. A separate same-root JF799944 search found no local hit; SOURCE.json documents were excluded from that accession search. These are bounded input-root results, not claims about every ignored original snapshot or remote database. The culture normalizer rejects all three bare strain-name variants as deposit keys.

No supported owning-strain/own-deposit bridge or required missing genome relationship was established. The marker and paper may inform later optional identity context; neither establishes a BacDive owner, culture deposit, assembly or same-deposit StrainInfo bridge. Optional evidence, definition and graph slots need not be filled. Phenotype/habitat curation belongs in the corresponding sibling repositories with claim-level evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in existing seeded assertions and bounded completeness checks. The paper's incomplete identity bridge and timing inconsistency limit optional future claims, not assertions currently present in this YAML. Pass does not certify unrun corpus gates or universal completeness.

## Recommended Edits

None required. Retain the exact NCBI identifier, label, parent chain and SEEDED status. Do not reinterpret the taxonomic rank as formal nomenclature, count the marker as a genome, or inherit genus-level type information.

Future supported additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests. Scope changes belong in `curation/seed_scope.tsv`; authoritative taxonomy corrections belong upstream in kg-microbe or NCBI. Do not hand-edit generated YAML or pages.

## Follow-up Checks

Before any phenotype claim, resolve the paper-to-accession identity bridge and the assay timing; genus-only experimental labels are insufficient. Before strain/genome links, require an eligible complete collection accession and source-specific chain. Keep strain, taxon, marker, deposit, sample, project and genome identities separate. StrainInfo must name the same matched SI-DP, GOLD must resolve the same organism/project/analysis chain, and ATB needs existing BioSample evidence; shared sample does not imply genome equivalence.

After any authorized maintained-input change, rerun target schema/strict validation and relevant join tests, followed by `just verify-corpus` and `just qc`.

## Additional Notes

- Four excluded Lacticaseibacillus rhamnosus rows concern taxid 47715, strain 1001270st1_G4_2201SCRN_220225, GCA/GCF_040924925.1, BV-BRC 47715.1896 and SAMN41035245: `data/bvbrc/bvbrc-0020.jsonl.gz:45785`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20850`, `data/catalog/gtdb_genomes-0004.jsonl.gz:4203`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19996`.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6268` is Mycobacterium tuberculosis, taxid 1773, BV-BRC 1773.18460 and run ERR1035245. `data/catalog/allthebacteria.tsv.xz:569715` concerns that run, SAMEA3558778 and ERZ3502640. Available FASTA/PASS filters do not supply a target association.
- Five rows concern Pseudomonas aeruginosa, taxid 287, Pae_CF67.08t, GCA/GCF_001035245.1, BV-BRC 287.1614 and SAMN03566384: `data/gold/analyses.jsonl.gz:101322`, `data/bvbrc/bvbrc-0016.jsonl.gz:22049`, `data/catalog/ncbi_refseq-0000.jsonl.gz:30446`, `data/catalog/gtdb_genomes-0006.jsonl.gz:7748`, `data/catalog/ncbi_genbank-0000.jsonl.gz:36041`. GOLD identifies Ga0158543/Gp0189774, LEHE00000000 and the assembly; its own organism GOLD ID and IMG field are empty. Neither missing organism chain nor unrelated name supports LNX39.
- `data/catalog/ncbi_genbank-0037.jsonl.gz:25650` is Klebsiella pneumoniae, taxid 573, zj02027, GCA_041035245.1 and SAMN37542638.
- `data/catalog/ncbi_genbank-0047.jsonl.gz:6722` and `data/catalog/ncbi_refseq_historical-0001.jsonl.gz:38990` concern Vibrio parahaemolyticus, taxid 670, VP20048 and SAMN46338791. GCA_051035245.1 is latest; GCF_051035245.1 is historical/suppressed, dated 2025-06-27. Neither is a target assembly.
- `data/catalog/ncbi_genbank-0019.jsonl.gz:18994` is Escherichia coli, taxid 562, PP86, GCA_021035245.1 and SAMEA8581605.
- Neither pdftotext nor pdftoppm was on PATH. The isolated offline-cached PyMuPDF runner read the downloaded primary PDF and rendered the relevant figure; no project dependency was changed.
- The full target was reread byte-identical. Only this report was written; no YAML, source inventory, history, status, generated product, Git or GitHub mutation was made.
