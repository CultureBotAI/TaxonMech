# YAML Record Review: Methylobacterium sp. M1-6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_m1_6.yaml`
- Started UTC: 2026-10-06T16:47:59Z
- Finished UTC: 2026-10-06T16:50:14Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. It denotes `NCBITaxon:1035227`, Methylobacterium sp. M1-6, with rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT and mapping status SEEDED. Its ten ancestors, zero inventoried strains, one NCBITAXON attestation and seed event are its material assertions. No synonyms, xrefs, nomenclature, taxonomy mappings, strain entries, assemblies, genome records, definition, cited evidence, discussion, phenotype or causal graph is present.

The unique target resolves through `data/taxa/PATHS.tsv:14439` and `curation/seed_scope.tsv:322223`. Seeded fields are generated from maintained source inputs, not manually curated YAML. Review occurred at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

The local review skill, curation boundaries, checklist, documentation, schema and authoritative recipes were inspected at the unchanged revision. Project commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_m1_6.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_m1_6.yaml --out /private/tmp/mm16-strict.tsv`: exit 0, one file scanned, zero errors. The actual TSV was read and has only its header.
- Structured manual comparisons of backbone, complete lineage, scope/path rows, attestation and seed text passed. These bounded comparisons do not substitute for `just verify-corpus`.
- Not run: full-corpus reproduction, strict validation, `just qc`, tests, provenance/site gates, and global `just validate-history`. No claim of corpus-wide validity or reproducibility is made.
- `just validate-products` was not run: `conf/id_label_targets.yaml` targets curator-added graph groundings and skips NCBITaxon. This record has no graph; taxon identity was checked at NCBI and in pinned inputs.
- No target history artifact was found in the ignored-inclusive content and filename searches; there was no focused external history record to validate. Review did not append history or promote SEEDED.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 dataset rows were inspected; Methylobacterium/Methylorubrum is not covered. iModulonDB is not applicable, not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221948` agrees with the identifier, label, species rank, parent, genetic code, empty synonym fields and 2026-09-13 snapshot. The complete native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31416`. Exact scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.

The complete current [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035227&retmode=xml) and [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035227) agree with the record. Every stored ancestor label and rank agrees with the pinned root-first chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), unclassified Methylobacterium (2615210). XML LineageEx omits root; Datasets includes it.

EXACT is grounding to this isolate-labelled NCBI species concept, not a claim of valid nomenclature or a culture deposit. The [LPSN genus record](https://lpsn.dsmz.de/genus/methylobacterium), fully inspected this session and searched specifically for M1-6, provides no target identity bridge. Its genus nomenclature cannot populate this target's nomenclature. The legacy NCBI browser failed through the web tool; both NCBI authority APIs succeeded.

## Evidence

The sole attestation matches source NCBITAXON, identifier and label, assertion count 1, unit NAME and the pinned snapshot date. Count 1 means one name assertion, not one genome or strain. The `seed_from_sources` event at 2026-09-13T17:54:04Z, action SEEDED_FROM_SOURCES, exactly matches the one-source scope reason.

No exact target row occurs in the inspected transformed tables `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, or `bactotraits_taxa.tsv`. The target has no direct backbone children. Zero BacDive strain records therefore agrees with the subtree gathering rule in `src/taxonmech/seed.py`; it does not mean the isolate was never cultivated.

The exact live query `txid1035227[Organism:noexp]` returned zero assembly hits with phrases-not-found/no-items diagnostics, and one nucleotide UID, 347300724. Full [FR869823.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869823.1), excluding bases, was read: a 1327-nt partial 16S rRNA gene, strain M1-6, explicit `taxon:1035227`, host Cerastium holosteoides and isolation source host leaf surface. It was submitted 18 May 2011, created 18 September, and updated 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. This is a marker, not a genome; genomic DNA describes its source molecule.

The sequence explicitly cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The complete bibliography and abstract, freshly fetched earlier in this same session, were re-read for M1-6. This is a community-level study of phyllosphere bacteria across hosts, locations and land-use conditions. It does not name M1-6 in the abstract or establish an isolate-specific growth, trait or collection locality. Its host is supported by the sequence metadata. Full text and supplements were not inspected.

## Completeness

Ignored and compressed files were included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The taxid, bounded exact label and slug search returned ten rows. All were read: three genuine taxonomy/name/scope rows and seven unrelated numeric matches listed below. Five discovered `SOURCE.json` metadata files were separately parsed in full for target values; none matched. Ignored-independent history filename enumeration found no target history path.

A same-root search for `(Methylobacterium|Methylorubrum).*\bM[- _]?1[- _]?6\b|\bM[- _]?1[- _]?6\b.*(Methylobacterium|Methylorubrum)` returned only those three genuine rows. These variants were leads, not new aliases. An accession search for FR869823 returned zero local rows in the same roots. Absence claims are limited to these searched surfaces and exact live NCBI queries.

The current `normalize_culture_identifier` returns empty for M1-6, M1 6 and M16. No eligible deposit or supported strain identity bridge was established, so no required missing strain-to-genome link was demonstrated. The external marker may be useful optional evidence, but does not supply an owning BacDive strain or own-deposit StrainInfo link. Optional definition, evidence and graph slots need not be filled without appropriate claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. This pass covers inspected assertions and bounded source searches, not unrun corpus gates or all possible external evidence.

## Recommended Edits

None required. Preserve the generated record and SEEDED status.

Future evidence-backed additions must be made through maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Taxon scope belongs in `curation/seed_scope.tsv`; erroneous upstream mappings belong in kg-microbe. Do not patch this YAML or its generated page to insert a guessed strain or genome.

## Follow-up Checks

Before adding links, resolve the target's own whole culture accession under the CAFI authority and full-accession rule. Keep sample, project, strain, deposit, marker and genome identities separate. StrainInfo sequences must identify that same eligible SI-DP; GOLD links require an unambiguous own-organism/project/analysis chain; ATB requires an exact already-supported BioSample and eligible available FASTA. None of the numeric matches below meets the target identity requirement.

After any authorized maintained-input change, rerun target schema/strict checks, relevant join tests, `just verify-corpus` and `just qc`. Inspect full text or supplements before making any new isolate-specific literature assertion.

## Additional Notes

- Four excluded rows belong to Lactobacillus acidophilus, taxid 1579, strain RTP21277st1_B3_RTP21277_210401, GCA/GCF_040925285.1, BV-BRC 1579.929 and BioSample SAMN41035227: `data/bvbrc/bvbrc-0004.jsonl.gz:1770`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20868`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20014`, `data/catalog/gtdb_genomes-0013.jsonl.gz:14157`.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6251` is Mycobacterium tuberculosis taxid 1773, genome 1773.18445, strain/run ERR1035227.
- `data/catalog/ncbi_genbank-0063.jsonl.gz:41862` is Candidatus Nanopelagicus hibericus taxid 1884915, GCA_964709635.1, BioSample SAMEA117469832. Its genome length 1035227, not its taxid, triggered the search.
- `data/catalog/allthebacteria.tsv.xz:569697` is Mycobacterium tuberculosis, run ERR1035227, sample SAMEA3558760, analysis ERZ3502569, with available FASTA and PASS filters. Availability does not overcome the different organism/run identity.
- All native candidate fields were losslessly inspected. No unrelated source identifier, sample or genome was transferred.
- The complete target was re-read before writing and remained byte-identical. Only this new report was written; no record, history, status, generated product, Git or GitHub mutation was performed.

