# YAML Record Review: NC10 bacterium enrichment culture clone inoc SFBR 9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_9.yaml`
- Started UTC: 2026-10-06T20:14:52Z
- Finished UTC: 2026-10-06T20:17:05Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read: `NCBITaxon:1035289`, NC10 bacterium enrichment culture clone inoc SFBR 9. It carries species rank, BACTERIA domain, parent environmental samples (`NCBITaxon:671142`), seven root-first ancestors, genetic code 11, EXACT grounding, SEEDED lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. No synonyms, nomenclature, mappings, genomes, phenotypes or causal graph are asserted.

The inoc qualifier and clone number are identity-bearing. This review neither merges nor judges neighboring SFBR records. Generated YAML is read-only; future corrections belong to maintained source inputs, extraction, scope or seeding.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_9.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_9.yaml --out /private/tmp/ni9-strict.tsv`: exit 0, one record, zero errors. The actual TSV was read and contains only its header.
- Bounded comparisons checked the complete lineage, inventories, path lock, scope, attestation and seed event. These are not a target-level reproduction validator.
- The shared backbone and native-name shard were SHA-256 checked earlier this turn and match the previously inspected manifest entries. The original taxdump archive is unavailable locally; no archive-hash or original names.dmp comparison is claimed.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, full provenance and history gates. Reproduction has no target selector; `--max-diffs` limits diagnostics only. `just validate-products` is not applicable because no curator-added graph nodes exist.
- Before external follow-up, the local `culturebotai-claw` iModulonDB dataset adapter exited 0. All 28 rows were read; none covers NC10/Methylomirabilota. Component queries were not applicable, and absent coverage is not biological evidence.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221990`, path lock `data/taxa/PATHS.tsv:14481`, scope `curation/seed_scope.tsv:322264` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31466` agree on the exact target. Exact type-material, merged-ID and dropped-record scans found no target entry. The pinned backbone has no descendants.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035289&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035289) confirm active identity, label, rank, parent and genetic code. Every ancestor agrees: root, cellular organisms, Bacteria, Bacteria incertae sedis, Bacteria candidate phyla, Methylomirabilota (SeqCode) and environmental samples. Datasets confirms the root ID omitted from the XML lineage display.

The Environmental samples XML division is consistent with the ancestry-derived BACTERIA domain. Species rank does not prove formal nomenclature, a pure isolate, a deposit or type material. The phylum's SeqCode label is carried taxonomy, not a nomenclature assertion for this clone. The inspected XML supplies no alternate name, consistent with the pinned name catalog and empty synonyms.

## Evidence

The NCBITAXON attestation correctly counts one pinned name and states the 2026-09-13 snapshot. Exact inventory comparisons found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Zero BacDive strains agrees with the inventories and absent descendants; it does not deny the existence of an enrichment culture.

An exact nonexpanded nucleotide query returned one accession, [JF803479.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803479.1), UID 337730219. Full GenBank metadata were read, excluding bases. It is a 417-base partial 16S rRNA marker with ENV division/keyword and an environmental_sample qualifier. Definition, organism, clone qualifier and taxon xref identify inoc SFBR 9 and 1035289. Metadata specify Ooijpolder Ditch, Netherlands, collection date 26-May-2009 and submission on 13-Apr-2011. It is not an assembly, culture deposit or pure-isolate proof. The shared collection context of other inoc SFBR clones does not establish their equivalence.

The accession explicitly cites [PMID:22657102](https://pubmed.ncbi.nlm.nih.gov/22657102/) and DOI `10.1016/j.jhazmat.2012.05.032`. Primary PubMed EFetch was inspected during this turn and verified their correspondence, bibliography and full abstract. The paper discusses denitrifying methanotroph enrichment resembling Candidatus Methylomirabilis oxyfera and reactor-level behavior. That provides study context, not named-species equivalence or clone-specific physiological rates. Full article methods/results were not inspected, and no reactor phenotype is added.

An exact nonexpanded Assembly ESearch returned zero hits with a phrases-not-found warning. An independent [NCBI Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035289/dataset_report) succeeded with an empty object. These bound the current queries, not all possible genome evidence.

Scope and seed-event wording agree. The timestamp 2026-09-13T17:54:04Z is the newest raw/ATB/StrainInfo manifest extraction time used by `_seed_timestamp` in `src/taxonmech/seed.py:139`. Lifecycle remains SEEDED.

## Completeness

Ignored-inclusive compressed-content searches used `rg --no-ignore --hidden -n -z -i` for identifier, full clone designation/label and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 19 candidate rows were read in full native JSON or TSV form, including nested content. Three are this target's backbone, scientific name and scope.

The remaining 16 are unrelated numeric collisions:

- Twelve concern Escherichia coli BioSamples SAMN10352897, SAMN10352898 and SAMN10352899: three BV-BRC records, three current GenBank assemblies, three replaced historical versions and three ATB records. The assembly roots are GCA_003773995, GCA_003768445 and GCA_003768505; current .2 and historical .1 versions remain distinct source records.
- Two concern Pseudomonas aeruginosa BioSample SAMN10352895: GenBank GCA_024072675.1 and ATB ERZ25499656.
- Two concern Mycobacterium tuberculosis run ERR1035289: BV-BRC genome 1773.18304 and ATB sample SAMEA3558822/analysis ERZ9334427.

The E. coli ATB record for SAMN10352898 retains SYLPH_RESULTS_FAIL and an unknown current Sylph species; this source detail does not make it evidence for the NC10 clone. Native taxon, organism, sample and run fields establish the exclusions. Embedded digits, assembly replacements and source quality statuses must not be converted into clone relationships.

An additional ignored-inclusive search for JF803479 found no rows in the same ten roots. All five SOURCE.json files and history filenames were separately inspected for identity and accession queries, with no additional target evidence or external history. Ignored-inclusive report-filename discovery found no earlier report for this stem.

Earlier this turn, the configured archive was absent at `data/source_snapshots/ncbi-new-taxdump-2026-09-13.tar.gz`, and an ignored-independent filename search under `data` and `/private/tmp` found no taxdump artifact. This is a bounded local availability limit, not a target defect or a claim about the whole machine.

No supported missing nomenclature entry, attestation or strain-genome relationship was found within these bounds. Marker/literature enrichment and causal graphs are optional for a seeded NCBI-only record; empty optional slots are appropriate.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, names, attestation, strain count and audit event agree with inspected sources. This does not prove full-corpus reproducibility or experimental characterization of the clone.

## Recommended Edits

None required. Preserve this exact clone identity and distinguish its partial marker from assemblies, deposits and enrichment cultures. Do not import neighboring clone aliases or reactor-level phenotypes.

Future evidence enrichment belongs to maintained source acquisition/projection or an explicitly modeled curator overlay, followed by `src/taxonmech/seed.py`. Do not hand-edit generated YAML or promote lifecycle through this report.

## Follow-up Checks

No immediate corrective check is required. After authorized maintained-input changes, rerun the two target validators, then full `just verify-corpus` and `just qc`. Recover and verify the original archive before claiming complete provenance verification. Any physiological addition requires inspected primary methods/results at the correct clone or culture scope.

## Additional Notes

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The target was reread byte-for-byte unchanged. Only this new report was written for this target; records, history, lifecycle, generated site and Git/GitHub state were not changed. Eukaryota remained untouched.

