# YAML Record Review: NC10 bacterium enrichment culture clone inoc SFBR 6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_6.yaml`
- Started UTC: 2026-10-06T20:11:04Z
- Finished UTC: 2026-10-06T20:13:47Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035288`, NC10 bacterium enrichment culture clone inoc SFBR 6. It has species rank, BACTERIA domain, parent environmental samples (`NCBITaxon:671142`), seven root-first ancestors, genetic code 11, EXACT grounding, SEEDED lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. It asserts no synonyms, nomenclature, mappings, genomes, phenotypes or causal graph.

The inoc qualifier and clone number distinguish this target. Generated YAML is read-only; future changes belong to maintained source inputs, extraction, scope or seeding. No neighboring clone receives a verdict from this review.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_6.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_6.yaml --out /private/tmp/ni6-strict.tsv`: exit 0, one record, zero errors. The actual TSV was read and contains only its header.
- Bounded comparisons checked the complete lineage, source inventories, path lock, scope, attestation and seed event. These are not a target-level reproduction gate.
- SHA-256 checks returned 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6 for `data/raw/ncbitaxon_taxa.tsv` and 31c672adade0c3485ee5d6817567f7972b06ce3b6853cf191159b76cad3b023c for `data/catalog/ncbi_names-0005.jsonl.gz`, matching the previously inspected manifest entries. The original taxdump is unavailable locally; no archive-hash or original names.dmp check is claimed.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, full provenance and history gates. Reproduction has no target selector; `--max-diffs` only limits diagnostics. `just validate-products` is not applicable because there are no curator-added graph nodes.
- Before external follow-up, the local `culturebotai-claw` iModulonDB dataset adapter exited 0. All 28 rows were read, with no NC10/Methylomirabilota coverage. Component queries were not applicable; missing coverage is not biological evidence.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221989`, path lock `data/taxa/PATHS.tsv:14480`, scope `curation/seed_scope.tsv:322263` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31465` agree on the exact taxon. Exact type-material, merged-ID and dropped-record scans found no target entry. The pinned backbone has no descendants.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035288&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035288) confirm active identity, label, rank, parent and genetic code. Every ancestor agrees: root, cellular organisms, Bacteria, Bacteria incertae sedis, Bacteria candidate phyla, Methylomirabilota (SeqCode) and environmental samples. Datasets supplies the root ID omitted from the XML lineage display.

The XML division Environmental samples is compatible with the ancestry-derived BACTERIA domain. Species rank does not establish formal nomenclature, a pure isolate, a deposit or type material. The phylum's SeqCode label is carried taxonomy, not a nomenclature assertion for this clone. The inspected XML supplies no alternate name, consistent with the pinned name catalog and empty synonyms.

## Evidence

The NCBITAXON attestation correctly counts one pinned name and states the 2026-09-13 snapshot. Exact inventory comparisons found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Zero BacDive strains agrees with the inventories and absent descendants; it is not a claim that no enrichment culture existed.

An exact nonexpanded nucleotide search returned one sequence, [JF803478.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803478.1), UID 337730218. Full GenBank metadata were read, excluding bases. It is a 417-base partial 16S rRNA marker with ENV division/keyword and an environmental_sample qualifier. Its definition, organism, clone qualifier and taxon xref identify inoc SFBR 6 and 1035288. Source metadata record Ooijpolder Ditch, Netherlands, collection date 26-May-2009 and submission on 13-Apr-2011. This marker is not a genome assembly, culture deposit or pure-isolate proof.

The accession explicitly cites [PMID:22657102](https://pubmed.ncbi.nlm.nih.gov/22657102/) and DOI `10.1016/j.jhazmat.2012.05.032`. Primary PubMed EFetch verified their correspondence, bibliography and full abstract. The paper discusses enrichment of denitrifying methanotrophs resembling Candidatus Methylomirabilis oxyfera and reactor-level behavior. It supports study context, not species equivalence or clone-specific physiological rates. Full article methods/results were not inspected, and no reactor phenotype is added.

An exact nonexpanded Assembly ESearch returned zero hits with a phrases-not-found warning. An independent [NCBI Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035288/dataset_report) succeeded with an empty object. These are bounded query results, not universal genome absence.

The seed-event text agrees with the scope reason. Its timestamp 2026-09-13T17:54:04Z is the newest raw/ATB/StrainInfo manifest extraction time, consistent with `_seed_timestamp` in `src/taxonmech/seed.py:139`. Lifecycle remains SEEDED.

## Completeness

Ignored-inclusive compressed-content searches used `rg --no-ignore --hidden -n -z -i` for identifier, full clone designation/label and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All eight candidate rows were read in full native JSON or TSV form, including nested content.

Three concern the target: backbone, scientific name and scope. Five are unrelated numeric collisions:

- BV-BRC genome 1773.18306 and ATB sample SAMEA3558821/analysis ERZ9334422 concern Mycobacterium tuberculosis run ERR1035288.
- GenBank assembly GCA_033542235.1 and BV-BRC genome 3090670.3 concern Mesorhizobium sp. BAC0120, taxon 3090670, BioSample SAMN38085656 and BioProject PRJNA1035288.
- GenBank assembly GCA_010352885.1 concerns Campylobacter jejuni, taxon 197, strain 302589 and BioSample SAMN13326892.

The native identity fields establish exclusion. A BioProject, run or embedded assembly number is not interchangeable with a taxon ID, and none supplies a clone strain-genome join.

An additional ignored-inclusive search for JF803478 found no rows in the same ten roots. All five SOURCE.json files and history filenames were separately inspected for identity and accession queries, with no additional target evidence or external history. Ignored-inclusive report-filename discovery found no earlier review for this stem.

The archive was absent at `data/source_snapshots/ncbi-new-taxdump-2026-09-13.tar.gz`; an ignored-independent filename search under `data` and `/private/tmp` also found no taxdump artifact. This is a bounded local availability limit, not a target defect or a claim about the whole machine.

No supported missing nomenclature entry, attestation or strain-genome relationship was found within these bounds. Marker/literature enrichment and causal graphs are optional for this seeded NCBI-only record; empty optional slots are appropriate.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, names, attestation, strain count and audit event agree with inspected sources. This does not prove full-corpus reproduction or experimental characterization of the clone.

## Recommended Edits

None required. Preserve the exact clone identity and distinguish the partial marker from assemblies, deposits and enrichment cultures. Do not transfer aliases, collection metadata or phenotypes from neighboring SFBR taxa.

Future evidence enrichment belongs to maintained source acquisition/projection or an explicitly modeled curator overlay, followed by `src/taxonmech/seed.py`. Do not hand-edit generated YAML or promote lifecycle through this report.

## Follow-up Checks

No immediate corrective check is required. After authorized maintained-input changes, rerun both target validators, then full `just verify-corpus` and `just qc`. Recover and verify the original archive before claiming complete provenance verification. Added physiological claims require inspected primary methods/results at the appropriate clone or culture scope.

## Additional Notes

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The target was reread byte-for-byte unchanged. Only this new report was written for this target; records, history, lifecycle, generated site and Git/GitHub state were not changed. Eukaryota remained untouched.

