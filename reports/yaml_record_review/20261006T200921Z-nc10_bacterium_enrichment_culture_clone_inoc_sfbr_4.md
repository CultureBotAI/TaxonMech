# YAML Record Review: NC10 bacterium enrichment culture clone inoc SFBR 4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_4.yaml`
- Started UTC: 2026-10-06T20:06:40Z
- Finished UTC: 2026-10-06T20:09:21Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read: `NCBITaxon:1035287`, NC10 bacterium enrichment culture clone inoc SFBR 4. It carries species rank, BACTERIA domain, parent environmental samples (`NCBITaxon:671142`), seven root-first ancestors, genetic code 11, EXACT grounding, SEEDED lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. No synonyms, nomenclature, mappings, genomes, phenotypes or causal graph are asserted.

The inoc qualifier and clone number distinguish this target from neighboring SFBR records. Generated YAML is read-only; future changes belong to maintained source inputs, extraction, scope or seeding.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_4.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_4.yaml --out /private/tmp/ni4-strict.tsv`: exit 0, one record, zero errors. The actual TSV was read and contains only its header.
- Manual comparisons checked the full lineage, inventories, path lock, scope, attestation and seed event. These are bounded checks, not target-level corpus reproduction.
- The shared backbone and native-name shard were SHA-256 checked earlier this turn and match the previously inspected manifest entries. The original taxdump archive is unavailable locally; no archive-hash or original names.dmp comparison is claimed.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, full provenance and history gates. Reproduction has no target selector; `--max-diffs` limits diagnostics only. `just validate-products` is not applicable because there are no curator-added graph nodes.
- The local `culturebotai-claw` iModulonDB dataset adapter exited 0 before external follow-up. All 28 rows were read, with no NC10/Methylomirabilota coverage. No component query applies; absent coverage is not biological evidence.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221988`, path lock `data/taxa/PATHS.tsv:14479`, scope `curation/seed_scope.tsv:322262` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31464` agree on the exact target. Exact type-material, merged-ID and dropped-record scans found no target entry, and the pinned backbone has no descendants.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035287&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035287) confirm active identity, label, rank, parent and genetic code. Every ancestor agrees: root, cellular organisms, Bacteria, Bacteria incertae sedis, Bacteria candidate phyla, Methylomirabilota (SeqCode) and environmental samples. Datasets supplies the root ID omitted from the XML lineage display.

The XML's Environmental samples division does not conflict with the ancestry-derived BACTERIA domain. Species rank does not prove a formally named species, pure isolate, culture deposit or type strain. The phylum's SeqCode label is carried taxonomy, not a clone nomenclature assertion. No alternate name appears in the inspected XML, consistent with the pinned catalog and empty synonyms.

## Evidence

The NCBITAXON attestation correctly counts one pinned name and states the 2026-09-13 snapshot. Exact inventory comparisons found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Zero BacDive strains agrees with the inventories and absent descendants; it is not a claim that no enrichment culture existed.

An exact nonexpanded nucleotide query returned one accession, [JF803477.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803477.1), UID 337730217. Full GenBank metadata were read, excluding bases. The marker is 415 bases of partial 16S rRNA, with ENV division/keyword and an environmental_sample qualifier. Definition, organism, clone qualifier and taxon xref identify inoc SFBR 4 and 1035287. The source is Ooijpolder Ditch, Netherlands, collected 26-May-2009 and submitted 13-Apr-2011. The 415-base length is this accession's value, not the length of adjacent clone markers. It is not a genome, deposit or proof of a pure isolate.

The accession explicitly cites [PMID:22657102](https://pubmed.ncbi.nlm.nih.gov/22657102/) and DOI `10.1016/j.jhazmat.2012.05.032`. Their correspondence, bibliography and full abstract were inspected through primary PubMed EFetch during this turn. The paper discusses denitrifying methanotroph enrichment resembling Candidatus Methylomirabilis oxyfera and reactor-level behavior. This is study context, not species equivalence or clone-specific physiological evidence. Full article methods/results were not inspected; no reactor phenotype is added.

An exact nonexpanded Assembly ESearch returned zero hits with a phrases-not-found warning. An independent [NCBI Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035287/dataset_report) succeeded with an empty object. These are bounded query results, not universal genome absence.

Scope and seed-event text agree. The seed timestamp 2026-09-13T17:54:04Z matches the newest raw/ATB/StrainInfo manifest extraction time used by `_seed_timestamp` in `src/taxonmech/seed.py:139`. Lifecycle remains SEEDED.

## Completeness

Ignored-inclusive compressed-content searches used `rg --no-ignore --hidden -n -z -i` for identifier, full clone designation/label and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All seven candidates were read in full native JSON or TSV form, including nested content.

Three are this target's backbone, scientific name and scope. The four excluded rows are:

- BV-BRC genome 1773.18307 and ATB sample SAMEA3558820/analysis ERZ9334421, both Mycobacterium tuberculosis with run ERR1035287.
- ATB Salmonella enterica sample SAMN18636290, run SRR14154023, analysis ERZ25908607, whose SeqKit checksum contains the searched digits.
- ATB Mycobacterium tuberculosis sample SAMN35621627, run SRR24827282, analysis ERZ26499004, whose SeqKit checksum also contains those digits.

Native organism and sample fields establish the mismatches. A run number or checksum substring is not taxon identity; ATB PASS status does not turn either unrelated sample into a clone strain-genome link.

An additional ignored-inclusive JF803477 search found no rows in those ten roots. All five SOURCE.json files and history filenames were separately inspected for identity and accession queries, with no additional target evidence or external history. Ignored-inclusive report-filename discovery found no earlier report for this stem.

Earlier this turn, the configured archive was absent at `data/source_snapshots/ncbi-new-taxdump-2026-09-13.tar.gz`, and an ignored-independent filename search under `data` and `/private/tmp` found no taxdump artifact. This local availability limit is not a record defect or a claim about the whole machine.

No supported missing attestation, nomenclature entry or strain-genome relationship was found within these bounds. Optional marker/literature enrichment and causal graphs are not required for a seeded NCBI-only record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, names, attestation, strain count and audit event agree with the inspected sources. This does not prove full-corpus reproducibility or experimental characterization of the clone.

## Recommended Edits

None required. Preserve this clone's exact identity and distinguish its partial marker from assemblies, deposits and enrichment cultures. Do not import aliases, collection metadata or phenotypes from neighboring SFBR records.

Future evidence enrichment belongs to maintained source acquisition/projection or an explicitly modeled curator overlay, followed by `src/taxonmech/seed.py`. Do not hand-edit generated YAML or promote lifecycle through this review.

## Follow-up Checks

No immediate corrective check is required. Following any authorized input change, rerun the two target validators, then full `just verify-corpus` and `just qc`. Recover and verify the original archive before claiming full provenance verification. Any added physiology requires inspected primary methods/results at the appropriate clone or culture scope.

## Additional Notes

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The target was reread byte-for-byte unchanged. Only this new report was written for this target; records, history, lifecycle, generated site and Git/GitHub state were not changed. Eukaryota remained untouched.

