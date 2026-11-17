# YAML Record Review: Psychrobacter sp. MF2-13c1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/psychrobacter_sp_mf2_13c1.yaml`
- Started UTC: 2026-10-06T17:46:58Z
- Finished UTC: 2026-10-06T17:49:04Z
- Verdict: pass

## Target

The fully read generated `TaxonRecord` denotes `NCBITaxon:1035243`, Psychrobacter sp. MF2-13c1, rank SPECIES, domain BACTERIA, parent `NCBITaxon:196806`, genetic code 11, grounding EXACT and status SEEDED. It contains ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, host/phenotype claim, discussion or graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14453`; scope is `curation/seed_scope.tsv:322237`. These are generated fields, not hand-curated assertions. HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

Review and curation skills, checklist, CLAUDE.md, justfile, CURATION, HARMONIZATION, SCHEMA, source-coverage and history guidance, relevant schema and seeder were inspected at this unchanged revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/psychrobacter_sp_mf2_13c1.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/psychrobacter_sp_mf2_13c1.yaml --out /private/tmp/pmf13-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Bounded manual source checks confirmed identity, all ancestors, scope/path, attestation and event. They are not a focused corpus-reproduction validator.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates or global `just validate-history`. The reproduction gate exposes no target selector. No corpus-wide reproducibility or reference-integrity claim is made.
- `just validate-products` was not run: its configured curator-added graph grounding is absent, and it skips NCBITaxon. Pinned and live authority data were used for taxonomic identifiers.
- Ignored-inclusive searches found no target external history artifact in the searched history tree. No review-history event or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were inspected; none covers Psychrobacter. Not applicable, not evidence of phenotype absence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221962` supports identifier, label, rank, parent, code 11, empty synonyms and the 2026-09-13 snapshot. The complete scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31430`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035243&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035243) agree. All ancestor labels/ranks match the pinned root-first chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Gammaproteobacteria (1236), Moraxellales (2887326), Moraxellaceae (468), Psychrobacter (497), unclassified Psychrobacter (196806). XML omits root in LineageEx; Datasets includes it.

EXACT denotes this NCBI concept, not a validly published binomial or culture deposit. The [LPSN genus page](https://lpsn.dsmz.de/genus/psychrobacter), fully inspected in the immediately preceding review and searched specifically for MF2-13c1 here, supplies no exact strain match. It uses order Pseudomonadales rather than NCBI's Moraxellales. This external hierarchy difference is preserved as context, not treated as a YAML defect: TaxonMech carries NCBI's lineage without reconciling it. Genus nomenclature, type species or other species' properties must not be transferred.

## Evidence

The sole NCBITAXON attestation matches identifier, label, assertion_count 1, assertion_unit NAME and snapshot. It counts a source name assertion, not a biological genome or strain. The 2026-09-13T17:54:04Z event, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree.

No exact target rows occur in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone child has this target as parent. Zero inventoried strains is consistent with BacDive own/subtree gathering in `src/taxonmech/seed.py:488`, not a claim that the isolate was never cultivated.

The exact live query `txid1035243[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 333827855. Full [JF800152.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF800152.1), excluding sequence bases, was read. It is a 1461-nt partial 16S rRNA gene, strain MF2-13c1, explicit `taxon:1035243`. Source qualifiers report Long Island Sound, host Fundulus heteroclitus, USA and `identified_by` C. Fricano. Submitted 25 March 2011; created and updated 29 May 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. Genomic DNA is a molecule-source description, not a complete genome.

The source bibliography names Boucaud and Fricano and an unpublished investigation of two Psychrobacter isolates from this host's scales. It contains no PMID or DOI. The title and direct submission do not establish valid publication, a named species, genome equivalence or a second isolate's deposit. The university submission address is not collection locality. Full text and supplements for that unpublished study were not inspected.

The [ATCC BAA-2286 product](https://www.atcc.org/products/baa-2286), inspected in the immediately preceding review, explicitly identifies MF2-10b2 and JF800153, not this target's MF2-13c1/JF800152. Its deposit, collection name, type flag and genome link are not transferred here. Adjacency in NCBI, common authors, host and manuscript title do not equate the two isolates.

## Completeness

Ignored and compressed content was included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug returned 12 rows, all read losslessly: three genuine taxonomy/name/scope rows and nine unrelated numeric matches. Five SOURCE.json documents were separately parsed in full with no target value; history filenames were enumerated independently of ignore rules.

The expanded same-root regex `\bMF[- _]?2[- _]?13[- _]?c[- _]?1\b` returned only the three genuine rows. A separate JF800152 search returned zero local hits in these roots. `normalize_culture_identifier` rejected MF2-13c1, MF2 13c1 and MF2_13c1 as join keys. Search variants were leads, not asserted aliases.

Bounded web follow-up used the exact strain, accession, ATCC-restricted strain query, spaced strain variant and authors/genus. It established no additional target-specific deposit or genome chain. Broad irrelevant search hits were not used as evidence. This is not an assertion that no deposit, genome or publication exists elsewhere; collection coverage is explicitly bounded in `docs/SOURCE_COVERAGE.md`.

No eligible own-deposit/owning-strain bridge or required missing genome relationship was established for MF2-13c1. The optional marker evidence is not a BacDive owner, whole collection accession or own-deposit StrainInfo sequence assertion. Empty optional definition/evidence/graph fields need not be populated without supported claims. Host, phenotype and media curation belong in the sibling domain repositories.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertions and bounded completeness checks. Pass does not certify unrun corpus gates, uninspected study text or universal source completeness.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status. Do not import the neighboring isolate's collection/genome evidence.

Future supported additions belong in maintained source capture/extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and a documented source boundary. Scope edits belong in `curation/seed_scope.tsv`; upstream taxonomic mappings belong in kg-microbe. Do not patch generated YAML or pages.

## Follow-up Checks

Require MF2-13c1's own eligible full culture accession and explicit source chain before adding strain/genome links. StrainInfo sequences must identify the matched SI-DP; GOLD must resolve an unambiguous organism/project/analysis chain; ATB requires existing BioSample evidence and an eligible available FASTA. A shared sample is not genome equivalence. Keep markers, strains, deposits, samples, projects and genomes distinct.

After an authorized maintained-input change, run target schema/strict validation and relevant join tests, then `just verify-corpus` and `just qc`. Inspect original study text before asserting isolate-specific phenotypes or nomenclature not supplied by an authority.

## Additional Notes

- Four excluded Lacticaseibacillus rhamnosus rows identify taxid 47715, strain 1001216st2_G9_RTP21198_201120, GCA/GCF_040924985.1, BV-BRC 47715.1900 and SAMN41035243: `data/bvbrc/bvbrc-0020.jsonl.gz:45789`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20854`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20000`, `data/catalog/gtdb_genomes-0000.jsonl.gz:26847`.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6263` is Mycobacterium tuberculosis, taxid 1773, BV-BRC 1773.18456, strain/run ERR1035243. `data/catalog/allthebacteria.tsv.xz:569713` is the same run, SAMEA3558776 and ERZ3502629, with matching Mycobacterium tuberculosis source classifications. Available FASTA and PASS filters do not supply a target link.
- `data/catalog/ncbi_genbank-0042.jsonl.gz:41464` is Legionella pneumophila serogroup 1, taxid 66976, species taxid 446, strain CNR-L_210352433, GCA_046490055.1 and SAMN38117040.
- `data/catalog/gtdb_genomes-0005.jsonl.gz:5406` and `data/catalog/ncbi_genbank-0058.jsonl.gz:8003` concern GCA_903831805.1, SAMEA6955414 and freshwater MAG AlinenLipids_bin-5474. NCBI calls it uncultured bacterium, taxid 77133; GTDB classifies it as CAIKZD01 sp903831805 in Patescibacteriota. Their numeric match is genome length 1035243, not this Psychrobacter taxid. The source classification difference is retained, not silently resolved.
- The target was re-read byte-identical. Only this new report was written for MF2-13c1; no YAML, inventory, history, status, generated product, Git or GitHub mutation was made.

