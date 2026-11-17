# YAML Record Review: NC10 bacterium enrichment culture clone inoc SFBR 2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_2.yaml`
- Started UTC: 2026-10-06T19:57:53Z
- Finished UTC: 2026-10-06T20:00:26Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035285`, NC10 bacterium enrichment culture clone inoc SFBR 2. It has species rank, BACTERIA domain, parent environmental samples (`NCBITaxon:671142`), seven root-first ancestors, genetic code 11, EXACT grounding, SEEDED lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. It asserts no synonyms, nomenclature, mappings, genome links, phenotypes or causal graph.

The word inoc is part of this source identity. This is not the distinct SFBR 2 taxon 1035284, nor another SFBR clone. Generated YAML is read-only; future changes belong to maintained inputs, extraction, scope or seeding. This review gives no verdict to neighboring records.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_2.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_inoc_sfbr_2.yaml --out /private/tmp/ni2-strict.tsv`: exit 0, one record, zero errors. The actual TSV was read and contains only its header.
- Manual bounded comparisons checked all lineage fields, inventories, path lock, scope, attestation and seed event. They are not a target-level reproduction validator.
- The shared backbone and native-name shard were SHA-256 checked earlier in this turn and match the previously inspected manifest entries. The original pinned taxdump is unavailable locally; no original names.dmp comparison or archive-hash verification is claimed.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, full provenance and history gates. Corpus reproduction has no target selector, and `--max-diffs` only limits diagnostics. `just validate-products` is not applicable because no curator-added graph nodes exist.
- The local `culturebotai-claw` iModulonDB dataset adapter exited 0 before external follow-up. All 28 dataset rows were read, with no NC10/Methylomirabilota coverage. Component queries were not applicable, and lack of coverage is not biological evidence.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221986`, path lock `data/taxa/PATHS.tsv:14477`, scope `curation/seed_scope.tsv:322260` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31462` agree on the exact identifier and label. Exact type-material, merged-ID and dropped-record scans found no target entry, and the pinned backbone has no descendants.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035285&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035285) confirm the active identity, species rank, parent and genetic code. Every stored ancestor agrees: root, cellular organisms, Bacteria, Bacteria incertae sedis, Bacteria candidate phyla, Methylomirabilota (SeqCode) and environmental samples. Datasets confirms the root ID that the XML lineage display omits.

The Environmental samples XML division is not a domain disagreement: BACTERIA follows ancestry. Species rank does not prove formal nomenclature, a pure isolate, a deposit or type material. The phylum's SeqCode label is carried taxonomy, not a nomenclature assertion for this clone.

The inspected live XML supplies no alternate name for this taxon, consistent with the sole scientific-name catalog row and empty synonym fields. The misspelling aliases found on neighboring SFBR clones must not be transferred here.

## Evidence

The NCBITAXON attestation correctly counts one pinned name and states the 2026-09-13 snapshot. Exact inventory comparisons found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. With no listed BacDive strains or descendants, `strain_count: 0` is consistent; it is not a biological statement that no enrichment culture existed.

An exact nonexpanded nucleotide query returned one accession, [JF803475.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803475.1), UID 337730215. The full GenBank metadata were read, excluding bases. It is a 417-base partial 16S rRNA marker with ENV division/keyword and an environmental_sample qualifier. Organism, definition, clone qualifier and taxon xref agree on inoc SFBR 2 and taxon 1035285. The metadata record Ooijpolder Ditch, Netherlands, collection date 26-May-2009 and direct submission on 13-Apr-2011. This is distinct from the later SFBR 2 marker JF803482.1 inspected separately during this turn. Shared marker length or study does not establish clone or genome identity.

JF803475.1 explicitly cites [PMID:22657102](https://pubmed.ncbi.nlm.nih.gov/22657102/) and DOI `10.1016/j.jhazmat.2012.05.032`. The primary PubMed bibliography and full abstract were inspected through EFetch during this turn and agree with the accession's citation. The paper discusses enrichment of denitrifying methanotrophs resembling Candidatus Methylomirabilis oxyfera and reactor-level behavior. That is study context, not proof that this marker denotes that named species, a pure strain or a clone-specific physiological rate. Full text was not inspected; no reactor phenotype is added.

An exact nonexpanded NCBI Assembly ESearch returned zero hits with a phrases-not-found warning. An independent [NCBI Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035285/dataset_report) succeeded and returned an empty object. These results bound the current queries, not all possible external genome evidence.

Scope and seed-event wording agree. The seed timestamp 2026-09-13T17:54:04Z matches the newest raw/ATB/StrainInfo manifest extraction timestamp, as required by `_seed_timestamp` in `src/taxonmech/seed.py:139`. Lifecycle stays SEEDED; this report is not human review promotion.

## Completeness

Ignored-inclusive compressed-content searches used `rg --no-ignore --hidden -n -z -i` for identifier, full clone designation/label and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 18 candidate rows were read in full native JSON or TSV form, including nested content. Three are the target backbone, scientific name and scope.

The remaining 15 are unrelated numeric collisions:

- Four concern Streptococcus mutans BioSample SAMN41035285 and its assembly/BV-BRC/GTDB records.
- Two concern Mycobacterium tuberculosis run ERR1035285 in BV-BRC and ATB.
- Five concern Pseudomonas aeruginosa Pae_CF67.09a and assembly pair GCA/GCF_001035285.1, including GOLD analysis Ga0158544 and project Gp0189775.
- One GTDB row has contig N50 1035285 for Streptococcus sp. Marseille-Q4154, not this taxon.
- Two concern Vibrio parahaemolyticus VP20047 and GCA/GCF_051035285.1; the RefSeq historical row is suppressed, not target evidence.
- One concerns Escherichia coli assembly GCA_021035285.1.

Source-native organism and taxon fields establish these exclusions. GOLD analysis/project IDs, BioSamples, runs, numeric assembly metrics and embedded assembly digits are not interchangeable with NCBITaxon identifiers. None supplies a strain-genome join for inoc SFBR 2.

An additional ignored-inclusive accession search for JF803475 found no row in the same ten roots. All five SOURCE.json files and history filenames were inspected separately for the identity and accession queries, with no additional target evidence or external history. Ignored-inclusive report-filename discovery found no earlier review for this stem.

The configured original archive was checked earlier this turn and was absent at `data/source_snapshots/ncbi-new-taxdump-2026-09-13.tar.gz`; an ignored-independent filename search under `data` and `/private/tmp` also found no taxdump artifact. This is a bounded local availability limit, not a claim about the entire machine or a detected target defect.

No supported missing nomenclature entry, source attestation or strain-genome relationship was found within these bounds. Optional marker/literature enrichment and causal graphs are not mandatory for this seeded NCBI-only record. Empty optional slots are appropriate.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Current identity, lineage, name coverage, attestation, strain count and audit event agree with the inspected pinned and live sources. Passing these checks does not prove full-corpus reproducibility or biological characterization of the clone.

## Recommended Edits

None required by the inspected evidence. Preserve the inoc qualifier and exact taxon identity. Do not copy the plus/minus aliases, markers or collection dates of neighboring SFBR clones into this record, and do not treat this partial 16S accession as a genome.

Any future evidence enrichment belongs to maintained source acquisition/projection or an explicitly modeled curator overlay, followed by `src/taxonmech/seed.py`. Optional physiological claims would need inspected primary methods/results at the correct clone or enrichment-culture scope. No generated YAML edit is recommended.

## Follow-up Checks

After an authorized maintained-input change, rerun both target validators and full `just verify-corpus` and `just qc`. Recover and verify the original pinned archive before claiming a complete source-provenance audit. Preserve distinctions among clone identity, marker accession, enrichment culture, deposit, sample, project and genome when evaluating future evidence.

No immediate corrective follow-up is required. Full article methods/results remain necessary only before introducing claims beyond the abstract's study context.

## Additional Notes

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The entire target was reread byte-for-byte unchanged. Only this new report was written for this target; no record, history, lifecycle, generated site or Git/GitHub state was changed. Eukaryota remained untouched.

