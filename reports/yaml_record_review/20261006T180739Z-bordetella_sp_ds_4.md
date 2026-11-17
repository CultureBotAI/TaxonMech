# YAML Record Review: Bordetella sp. Ds-4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bordetella_sp_ds_4.yaml`
- Started UTC: 2026-10-06T18:03:35Z
- Finished UTC: 2026-10-06T18:07:39Z
- Verdict: pass

## Target

The fully read generated TaxonRecord denotes NCBITaxon:1035250, Bordetella sp. Ds-4, rank SPECIES, domain BACTERIA, parent NCBITaxon:2630031, genetic code 11, grounding EXACT and status SEEDED. It contains ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, phenotype claim, discussion or graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14456`; scope is `curation/seed_scope.tsv:322240`. HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Eukaryota was not reopened.

## Validation

The review skill, checklist, justfile and curation skill were reread. CLAUDE.md, CURATION, HARMONIZATION, SCHEMA, history guidance, source boundaries and relevant schema/seeder had been inspected at this unchanged revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bordetella_sp_ds_4.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/bordetella_sp_ds_4.yaml --out /private/tmp/bds-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Bounded manual comparisons confirmed identity, every ancestor, path/scope, attestation and event. These are not a focused corpus-reproduction validator.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates or global `just validate-history`. The reproduction CLI was rechecked: no target selector, only a maximum-difference option. No corpus-wide reproducibility/reference-integrity claim is made.
- `just validate-products` was not run: graph grounding is absent. Its configuration was reread and excludes NCBITaxon from OAK lookup; identifiers were checked against pinned/live taxonomy instead.
- Ignored-inclusive content/path searches found no target external history artifact within the searched history tree. No history or status mutation was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` first failed under restricted-network DNS, then succeeded with read-only network access. All 28 rows were inspected; none covers Bordetella. Not applicable, not negative biological evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221965` supports identifier, exact case-sensitive label, rank, parent, code 11, empty synonyms and the 2026-09-13 snapshot. The scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31433`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035250&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035250) agree. Every stored ancestor label/rank matches the pinned root-first chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Betaproteobacteria (28216), Burkholderiales (80840), Alcaligenaceae (506), Bordetella (517), unclassified Bordetella (2630031). XML omits root in LineageEx; Datasets includes it.

SPECIES is NCBI's rank for this strain-labelled taxon, not proof of a formally named species. EXACT identifies the NCBI source concept, not nomenclatural validity. The fully inspected [LPSN Bordetella genus page](https://lpsn.dsmz.de/genus/bordetella), record 516980, concerns a validly published/correct genus and its type species Bordetella pertussis. It does not identify Ds-4. Genus nomenclature, type material and risk classifications are not automatically target assertions. No exact target LPSN mapping occurs in the pinned inventory.

## Evidence

The NCBITAXON attestation matches identifier, label, count 1, unit NAME and snapshot. The seed event at 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree. Count 1 measures a source-name assertion, not a genome or biological strain.

No exact target row occurs in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone child has this taxon as parent. Zero inventoried strains agrees with the own/subtree BacDive gathering rule in `src/taxonmech/seed.py:488`, not a general claim that the organism has never been cultured.

The exact live query `txid1035250[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 333830300. Full [HQ857791.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/HQ857791.1), excluding bases, was inspected: 727 nt, partial 16S rRNA, strain Ds-4, explicit taxon:1035250 and cultivated-soil isolation source. Submitted 30 December 2010 by R. Sasikala and S. Barathi; created 29 May 2011, updated 28 June 2011. The source feature has no geographic qualifier, culture deposit, BioSample, BioProject or assembly identifier. The Indian institutional submission address is not itself a specimen-location qualifier. Its bibliography is direct submission only, without PMID or DOI. This marker is not a genome assembly.

The inspected publisher text of [Soumana, Linz and Harvill's 2017 study](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2017.00028/full), DOI 10.3389/fmicb.2017.00028, explicitly lists Ds-4/HQ857791.1/727 bp in Table 2, with cultivated soil and India, citing NCBI. This is a database-derived inventory entry, not evidence of a new Ds-4 isolation or experiment. The paper requires at least 1376 bp for its phylogenetic analysis; Ds-4's marker is shorter, so no clade assignment can be borrowed from that analysis. The experimental growth strains are RB50, L60 and DSMZ12804, not Ds-4. No growth, pathogenicity, biodegradation, metal-resistance or genome claim is transferred from those other strains. The PMC mirror presented a browser check; the primary publisher's HTML succeeded. Relevant methods, table, results and discussion were inspected; no separate supplement or original PDF was inspected.

## Completeness

Ignored and compressed content was included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, exact label and slug returned 12 rows: three genuine target rows and nine numeric collisions. All original candidate native JSON/TSV rows, including the compressed ATB row, were read losslessly.

An expanded same-root `\bDs[- _]?4\b|HQ857791` search returned 213 rows. All 69 inventory/name/scope rows and 144 other native rows were parsed for identity and every matching field. These broader candidate projections are triage, not full reviews of those organisms. The only target concepts were the same three rows; no matching field contained HQ857791. Five SOURCE.json documents and history filenames were separately checked for initial and expanded identifiers without a target/accession hit. These are bounded input-root results, not claims about all original ignored snapshots or remote databases.

The principal same-designation culture candidates were read in full. BacDive 14247 is Sphingomonas dokdonensis, NCBITaxon:344880, strain DS-4, with DQ178975 and deposits DSM 21029/CIP 108841/KCTC 12541. StrainInfo SI-ID297316 attaches GCA_002197685 to its own DSM 21029 deposit, SI-DP913101. These sources do not identify Bordetella Ds-4. Another DS4 alias belongs to Helicobacter felis, SI-ID7691, NCBITaxon:214. No deposit or genome can be transferred by normalizing these bare names.

Other expanded matches include distinct taxonomic concepts, DS4.bin suffixes, community project labels and unrelated strain designations. Unknown/generic bacterial names are not a positive identity bridge either. The culture normalizer rejects Ds-4, DS-4 and Ds4 as deposit keys.

No supported owning-strain/own-deposit bridge or required missing genome relationship was established. Marker/literature context may inform optional later curation, but does not create a BacDive owner, culture deposit, assembly or same-deposit StrainInfo bridge. Optional definition, evidence and graph slots need not be filled.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the existing seeded assertions and bounded completeness checks. Homonyms and paper-level generalizations are explicit cautions, not defects present in the YAML. Pass does not certify unrun corpus gates or universal completeness.

## Recommended Edits

None required. Retain the exact NCBI identifier, Ds-4 label, parent chain and SEEDED status. Do not import Sphingomonas/Helicobacter deposits or type flags, count the marker as a genome, or assign phenotype/clade evidence from other Bordetella strains.

Future supported additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests. Scope changes belong in `curation/seed_scope.tsv`; authoritative taxonomy corrections belong upstream in kg-microbe or NCBI. Do not hand-edit generated YAML or pages.

## Follow-up Checks

Before adding a strain/genome link, require an eligible complete collection accession and a source-specific identity chain. Keep strain, taxon, marker, deposit, sample, project and genome identities separate. StrainInfo must name the same matched SI-DP; GOLD must resolve the same organism/project/analysis chain; ATB requires existing BioSample evidence. Shared sample does not imply genome equivalence.

After an authorized maintained-input change, rerun target schema/strict validation and relevant join tests, followed by `just verify-corpus` and `just qc`. Require Ds-4-specific evidence before curator-authored phenotype or phylogenetic claims.

## Additional Notes

- Four excluded Ligilactobacillus salivarius rows identify taxid 1624, strain 1001295st1_D10_RTP21277_210401, GCA/GCF_040924825.1, BV-BRC 1624.985 and SAMN41035250: `data/bvbrc/bvbrc-0004.jsonl.gz:27286`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20845`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19991`, `data/catalog/gtdb_genomes-0006.jsonl.gz:6633`.
- `data/bvbrc/bvbrc-0018.jsonl.gz:45635` and `data/catalog/ncbi_genbank-0031.jsonl.gz:25441` concern Cyanobacterium aponinum AL20115, taxid 3090662, GCA_033798705.1, BV-BRC 3090662.3, SAMN38084912 and PRJNA1035250. A project-number substring is not the target taxid.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6404` concerns Mycobacterium tuberculosis, taxid 1773, BV-BRC 1773.18585 and run ERR1035250. `data/catalog/allthebacteria.tsv.xz:569720` concerns the same run, SAMEA3558783 and ERZ3502659. Available FASTA/PASS filters do not supply a target association.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6459` is Campylobacter jejuni, taxid 197, PNUSAC014948, GCA_010352505.1 and SAMN13825585.
- The full-read Sphingomonas homonym rows are `data/raw/bacdive_strains.tsv:14081`, `data/bacdive/records.jsonl.gz:14080`, `data/straininfo/records.jsonl.gz:228458` and `data/raw/ncbi_type_material.tsv:189386` plus the following line. The Helicobacter homonym is `data/straininfo/records.jsonl.gz:7691`. StrainInfo supplies an unversioned assembly accession for Sphingomonas; no version was invented.
- Expanded GOLD/name search hits that happen to concern eukaryotes were excluded as identity mismatches; no eukaryotic TaxonRecord was reopened or given a new report.
- The target was reread byte-identical. Only this report was written; no YAML, source inventory, history, status, generated product, Git or GitHub mutation was made.
