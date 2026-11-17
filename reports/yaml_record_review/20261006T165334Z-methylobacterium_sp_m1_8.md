# YAML Record Review: Methylobacterium sp. M1-8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_m1_8.yaml`
- Started UTC: 2026-10-06T16:51:14Z
- Finished UTC: 2026-10-06T16:53:34Z
- Verdict: pass

## Target

The fully read generated `TaxonRecord` is `NCBITaxon:1035228`, Methylobacterium sp. M1-8: SPECIES in BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT and mapping status SEEDED. It carries ten root-first ancestors, `strain_count: 0`, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, discussions, phenotype claims or causal graphs are present.

`data/taxa/PATHS.tsv:14440` uniquely resolves the identifier and file stem; `curation/seed_scope.tsv:322224` supplies scope. These are generated assertions owned by maintained source extraction and seeding inputs. HEAD was rechecked as `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

Guidance, checklist, schema and command recipes were inspected at the unchanged repository revision. Project invocations used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_m1_8.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_m1_8.yaml --out /private/tmp/mm18-strict.tsv`: exit 0, one file scanned, zero errors. The actual TSV was read; only its header is present.
- Bounded structured comparisons confirmed the entire pinned lineage, identity fields, path/scope rows, attestation and seed-event text. These manual checks do not constitute the corpus reproduction gate.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates, and global `just validate-history`. Corpus-wide validity, references and reproducibility are not certified by this individual review.
- `just validate-products` was not run: its configured OAK surface is curator-added graph grounding, absent here; `conf/id_label_targets.yaml` skips NCBITaxon. Pinned and live NCBI were used for taxonomic identifier/label checks.
- Ignored-inclusive content and filename searches found no target external history artifact to validate. No history entry was written or SEEDED status promoted.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 dataset rows were inspected; no Methylobacterium/Methylorubrum dataset applies. This is not evidence against any phenotype.

## Identity and Grounding

The exact backbone row, `data/raw/ncbitaxon_taxa.tsv:221949`, supports identifier, label, rank, parent, code 11, empty synonym fields and the 2026-09-13 snapshot. The complete scientific-name source row is `data/catalog/ncbi_names-0005.jsonl.gz:31417`. Exact target scans of the type-material, merged-ID and dropped-record tables found no rows.

The complete current [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035228&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035228) agree. The stored chain contains root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), and unclassified Methylobacterium (2615210). Every label and rank agrees with the pinned lineage. XML LineageEx omits root; Datasets includes it.

EXACT denotes this NCBI species concept, not a validly published name, collection accession or genome equivalence. The [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was fully inspected this session and specifically searched for M1-8. It supplies no isolate/deposit identity bridge; genus-level nomenclature must not be copied here. The legacy NCBI browser was inaccessible through the web tool, while both authority APIs succeeded.

## Evidence

The NCBITAXON attestation agrees exactly with the inventory's source identifier, label, count 1, unit NAME and snapshot note. One name assertion is not one biological strain or genome. The seed event at 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES, matches the scoped one-source reason.

Exact source scans found no rows in `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, or `bactotraits_taxa.tsv`. No backbone taxon has this target as its direct parent. The zero BacDive strain count therefore agrees with the seeder's own/subtree gathering rule; it is not a claim that M1-8 was never cultivated.

The current NCBI exact query `txid1035228[Organism:noexp]` returned zero assembly records with phrases-not-found/no-items diagnostics, and one nucleotide UID, 347300725. Full [FR869824.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869824.1), excluding bases, was read. It is a 1333-nt partial 16S rRNA gene with strain M1-8 and explicit `taxon:1035228`; the host is Cerastium holosteoides and isolation source is host leaf surface. It was submitted 18 May 2011, created 18 September, and updated 6 December 2011. No culture collection, BioSample, BioProject or assembly identifier appears. The marker's genomic-DNA molecule qualifier does not turn it into a genome assembly.

Its source reference explicitly supplies [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The live PubMed bibliography and complete abstract fetched earlier in this same session were re-read for M1-8. They support study context about phyllosphere communities across hosts, localities and land-use conditions; the abstract does not identify M1-8-specific growth, traits or collection locality. The isolate's host association is from its own sequence metadata. Full text and supplements were not inspected.

## Completeness

Searches used `rg --no-ignore --hidden -n -z -i`, including ignored and compressed files, over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact scientific label and slug yielded 13 rows, all fully inspected: three genuine taxonomy/name/scope rows and ten numeric collisions detailed below. The five discovered `SOURCE.json` files were separately parsed for target values; no match occurred. Ignored-independent history path enumeration likewise found no target artifact.

The expanded query `(Methylobacterium|Methylorubrum).*\bM[- _]?1[- _]?8\b|\bM[- _]?1[- _]?8\b.*(Methylobacterium|Methylorubrum)` returned only those three genuine rows in the same roots. Variants were search leads, not asserted synonyms. A follow-up search for FR869824 found no local row in these roots. These statements are bounded to the named local surfaces and live exact NCBI queries, not universal claims about all databases.

`normalize_culture_identifier` returned empty for M1-8, M1 8 and M18. No eligible whole culture deposit, owning BacDive strain or explicit own-deposit sequence bridge was established. No required missing strain/genome association is demonstrated. The external marker could serve as optional identity evidence, but does not justify fabricating a strain entry, genome count or StrainInfo link. Empty optional evidence, definition and graph fields are not defects by themselves.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertions and bounded completeness checks. Unrun corpus gates and uninspected full text remain limitations, not established record defects.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

If later primary evidence resolves an eligible deposit or strain/genome chain, update maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests, and regenerate through the documented workflow. Scope edits belong in `curation/seed_scope.tsv`; corrections to upstream source mappings belong in kg-microbe. Do not hand-edit `data/taxa/` or generated pages.

## Follow-up Checks

Any proposed future link requires the target's own whole culture accession, matched against the CAFI authority and full template. Preserve taxon, strain, deposit, sample, project, marker and genome identities separately. StrainInfo sequence evidence must name that same eligible SI-DP, GOLD must provide a consistent own-organism/project/analysis chain, and ATB must match existing exact BioSample evidence with an eligible available FASTA. A shared sample or search substring is not genome equivalence.

After an authorized maintained-input change, rerun target schema/strict checks and relevant regression tests, then `just verify-corpus` and `just qc`. Read full-text or supplementary evidence before adding isolate-specific literature claims.

## Additional Notes

- Four numeric matches are Lactobacillus acidophilus taxid 1579, strain RTP21277st1_G1_RTP21277_210401, GCA/GCF_040925255.1, BV-BRC 1579.928 and BioSample SAMN41035228: `data/bvbrc/bvbrc-0004.jsonl.gz:1769`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20867`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20013`, and `data/catalog/gtdb_genomes-0014.jsonl.gz:40809`.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6255` is Mycobacterium tuberculosis taxid 1773, genome 1773.18449, strain/run ERR1035228.
- `data/catalog/ncbi_genbank-0018.jsonl.gz:21520` is Salmonella enterica taxid 28901, strain 1035228001, GCA_020044985.1, BioSample SAMN21475434.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6449` is Campylobacter jejuni taxid 197, strain 305171, GCA_010352285.1, BioSample SAMN13326923.
- `data/catalog/ncbi_genbank-0033.jsonl.gz:35469` is Streptococcus pneumoniae taxid 1313, isolate 470, GCA_036051495.1, BioSample SAMN11116956; its assembly name PDT001035228.1 caused the match. Its publication is not target evidence.
- `data/catalog/gtdb_genomes-0011.jsonl.gz:42121` is Staphylococcus aureus taxid 1280, GCA/GCF_051258135.1, source strain identifiers 23;SA001, BioSample SAMN43266909. Scaffold N50 and N75 are 1035228, not its taxid.
- `data/catalog/allthebacteria.tsv.xz:569698` is Mycobacterium tuberculosis, run ERR1035228, sample SAMEA3558761, analysis ERZ3502574. FASTA availability and PASS filters do not establish M1-8 identity.
- All native fields in those rows were losslessly inspected and rejected as target links; none supplies a missing strain, deposit, sample or genome association here.
- The target was re-read and unchanged before this report. Only this new review report was written; no YAML, history, mapping status, generated product, Git or GitHub state was mutated.

