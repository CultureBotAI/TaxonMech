# YAML Record Review: NC10 bacterium enrichment culture clone inoc SFBR 3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_3.yaml`
- Started UTC: 2026-10-06T20:02:35Z
- Finished UTC: 2026-10-06T20:05:27Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read: `NCBITaxon:1035286`, NC10 bacterium enrichment culture clone inoc SFBR 3. It has species rank, BACTERIA domain, parent environmental samples (`NCBITaxon:671142`), seven root-first ancestors, genetic code 11, EXACT grounding, SEEDED lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. It asserts no synonyms, nomenclature, mappings, genomes, phenotypes or causal graph.

The inoc qualifier and clone number are part of the identity. This review does not merge or judge other SFBR clones. Generated YAML is read-only; future corrections belong to maintained source inputs, extraction, scope or seeding.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_3.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_3.yaml --out /private/tmp/ni3-strict.tsv`: exit 0, one record, zero errors. The actual TSV was read and contains only its header.
- Bounded source comparisons checked the entire lineage, inventories, path lock, scope, attestation and seed event. These are not a target-level reproduction validator.
- SHA-256 checks of `data/raw/ncbitaxon_taxa.tsv` and `data/catalog/ncbi_names-0005.jsonl.gz` returned 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6 and 31c672adade0c3485ee5d6817567f7972b06ce3b6853cf191159b76cad3b023c, matching the previously inspected manifest entries. The original configured taxdump archive remains unavailable; no archive-hash or original names.dmp verification is claimed.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, full provenance and history gates. Reproduction has no target selector; `--max-diffs` only limits diagnostics. `just validate-products` is not applicable because no curator-added graph nodes exist.
- Before external follow-up, the local `culturebotai-claw` iModulonDB dataset adapter exited 0. All 28 rows were read; none covers NC10/Methylomirabilota. Component queries were not applicable, and missing coverage is not biological evidence.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221987`, path lock `data/taxa/PATHS.tsv:14478`, scope `curation/seed_scope.tsv:322261` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:31463` agree on the exact identity. Exact type-material, merged-ID and dropped-record scans found no target entry; the pinned backbone has no descendants.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035286&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035286) confirm the active taxon, label, species rank, parent and genetic code. All ancestors agree: root, cellular organisms, Bacteria, Bacteria incertae sedis, Bacteria candidate phyla, Methylomirabilota (SeqCode) and environmental samples. Datasets supplies the root ID omitted from the XML lineage display.

Environmental samples is the XML division, not a disagreement with the ancestry-derived BACTERIA domain. Species rank does not establish formal nomenclature, a pure isolate, a culture deposit or type material. The phylum's SeqCode label is carried taxonomy, not a nomenclature assertion for this clone.

The inspected XML supplies no alternate name, consistent with the sole scientific-name catalog row and empty synonym fields. Aliases from other SFBR taxa are not evidence for this one.

## Evidence

The NCBITAXON attestation correctly counts one pinned name and states the 2026-09-13 snapshot. Exact inventory comparisons found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Zero BacDive strains agrees with those inventories and the lack of descendants; it does not deny the existence of an enrichment culture.

An exact nonexpanded nucleotide query returned one sequence, [JF803476.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803476.1), UID 337730216. The full GenBank metadata were read, excluding bases. It is a 417-base partial 16S rRNA marker with ENV division/keyword and an environmental_sample qualifier. Organism, definition, clone qualifier and taxon xref identify inoc SFBR 3 and 1035286. Metadata specify Ooijpolder Ditch, Netherlands, collection date 26-May-2009 and direct submission on 13-Apr-2011. This is a marker, not a genome assembly, registered deposit or proof of a pure isolate.

The sequence explicitly cites [PMID:22657102](https://pubmed.ncbi.nlm.nih.gov/22657102/) and DOI `10.1016/j.jhazmat.2012.05.032`. Primary PubMed EFetch verified their correspondence and supplied the complete bibliography/abstract. The paper discusses enrichment of denitrifying methanotrophs resembling Candidatus Methylomirabilis oxyfera and reactor-level behavior. That supports study context, not equivalence to the named species or clone-specific physiological rates. Full article methods/results were not inspected; no reactor phenotype is added.

An exact nonexpanded Assembly ESearch returned zero hits with a phrases-not-found warning. An independent [NCBI Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035286/dataset_report) succeeded with an empty object. These bound the queries, not genome availability in every resource.

The seed event agrees with the maintained scope reason. Its 2026-09-13T17:54:04Z timestamp matches the newest raw/ATB/StrainInfo manifest extraction time, consistent with `_seed_timestamp` in `src/taxonmech/seed.py:139`. Lifecycle remains SEEDED.

## Completeness

Ignored-inclusive compressed-content searches used `rg --no-ignore --hidden -n -z -i` for identifier, full clone designation/label and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five candidate rows were read in full native JSON or TSV form, including nested content.

Three concern this target: backbone, scientific name and scope. The other two are numeric collisions: Campylobacter jejuni assembly GCA_010352865.1, taxon 197, strain PNUSAC014940; and an ATB Mycobacterium tuberculosis record with run ERR1035286, sample SAMEA3558819 and analysis ERZ9334420. Native identity fields establish their exclusion. Neither supplies a clone strain-genome relationship.

An additional ignored-inclusive search for JF803476 found no rows in the same ten roots. All five SOURCE.json files and history filenames were separately checked for identity and accession queries, with no additional target evidence or external history. Ignored-inclusive report-filename discovery found no earlier report for this stem.

The archive was absent at `data/source_snapshots/ncbi-new-taxdump-2026-09-13.tar.gz`. An ignored-independent filename search under `data` and `/private/tmp` also found no taxdump artifact. This is a bounded local availability limit, not a target defect or a claim about the whole machine.

No supported missing attestation, nomenclature entry or strain-genome join was found within these bounds. Marker/literature enrichment and causal graphs are optional for this seeded record; empty optional slots are appropriate.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, name coverage, attestation, strain count and audit event agree with the inspected sources. Passing target checks does not prove full-corpus reproducibility or experimental characterization of this clone.

## Recommended Edits

None required by the inspected evidence. Preserve inoc SFBR 3 as a separate clone taxon, and do not promote its partial marker into a genome or copy aliases and phenotypes from adjacent records.

Future evidence enrichment belongs to maintained source acquisition/projection or an explicitly modeled curator overlay, followed by `src/taxonmech/seed.py`. Any physiological claim requires primary methods/results at the correct clone or culture scope. Do not hand-edit generated YAML.

## Follow-up Checks

No immediate corrective check is required. After any authorized maintained-input change, rerun both target validators, then full `just verify-corpus` and `just qc`. Recover and verify the original pinned archive before claiming full source-provenance verification. Preserve distinctions among clone, enrichment culture, marker, deposit, sample and assembly.

## Additional Notes

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The target was reread byte-for-byte unchanged. Only this new report was written for this target; records, history, lifecycle, generated site and Git/GitHub state were not changed. Eukaryota remained untouched.

