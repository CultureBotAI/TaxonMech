# YAML Record Review: Capnocytophaga sp. oral taxon 326 str. F0382

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/capnocytophaga_sp_oral_taxon_326_str_f0382.yaml`
- Started UTC: 2026-10-06T14:22:51Z
- Finished UTC: 2026-10-06T14:25:07Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1035193`, label `Capnocytophaga sp. oral taxon 326 str. F0382`, rank STRAIN, domain BACTERIA. The entire YAML was read before findings and checked byte-for-byte unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED with one GTDB mapping, two synonyms, one equivalent xref, genetic code 11, zero listed strains, four source attestations and one inline seed event. It has no definition, nomenclature entry, nested genome link, publication citation or causal graph. Only this new report is written.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/capnocytophaga_sp_oral_taxon_326_str_f0382.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/capnocytophaga_sp_oral_taxon_326_str_f0382.yaml --out /private/tmp/cf0382-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: pinned identity, NCBI alias, all thirteen root-first lineage entries, genetic code, source counts, scope and seed provenance agree. These comparisons are not a focused corpus-reproduction validator.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- There are no curator-added ontology graph nodes to validate. The documented product checker excludes taxonomy fields and delegates those to corpus reproduction.
- No separate target history artifact was found by the ignored-independent history filename search. Inline history passed schema validation and agrees with scope provenance. No external history validator was run against an invented artifact.
- There are no DOI, PMID, quoted-evidence or definition references in this YAML. No additional record-specific citation validator is documented in the inspected commands.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221916` and inspected live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035193&retmode=xml) agree on the label, strain rank, parent `NCBITaxon:712212`, one equivalent name and genetic code 11. The [taxonomy dataset response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035193) supplies rank STRAIN and the same thirteen root-inclusive ancestor IDs.

All thirteen pinned ancestors match, including both intervening clades, Flavobacteriia, unclassified Capnocytophaga and the species-level oral taxon 326 parent. Live XML provides matching non-root labels/ranks. No children, type-material entry, merged-ID entry or dropped entry were found for the exact taxid in their pinned structured tables.

A separately inspected [cached NCBI browser page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1035193&lvl=0), crawled ten months earlier, displayed no rank. This differs from both current API responses and the pinned backbone. The review retains that temporal/source discrepancy and does not replace their supported STRAIN rank with the older rendered value.

The [LPSN C. periodontitidis page](https://lpsn.dsmz.de/species/capnocytophaga-periodontitidis), record 20391, concerns a validly published species with type strain p1a2 / JCM 34126 / CGMCC 1.17337, not F0382. The exact raw row at `data/raw/lpsn_names.tsv:3996` maps that species name to `NCBITaxon:2795027`, not this strain or its parent 712212. Its nomenclature and type designations do not automatically belong on this record.

The inspected [HOMD development genome page](https://devel.homd.org/genome/genome_description?gid=GCA_000318295.1) identifies F0382 as HMT-0326. It uses C. periodontitidis and displays GTDB V226 with that classification, while preserving C. endodontalis in its deposited-organism field. These classifications are source-specific context; TaxonMech must carry the NCBI lineage rather than reconcile them locally.

## Evidence

- NCBI: full native rows at `data/catalog/ncbi_names-0005.jsonl.gz:31373` and `31374` support the alias and scientific name. The attestation is one NAME.
- GTDB: `data/catalog/gtdb_genomes-0014.jsonl.gz:43186` identifies RS_GCF_000318295.1, F0382, taxid 1035193, SAMN02436687 and GenBank GCA_000318295.1 in the C. periodontitidis cluster. It explicitly marks this genome as not the representative. Its class is Bacteroidia, distinct from NCBI's Flavobacteriia; that is not a local lineage defect.
- GTDB count: `data/raw/gtdb_species.tsv:40628` and `data/raw/gtdb_mappings.tsv:1420` carry 16 cluster genomes. Exact cluster rows at mapping lines 39687, 209143, 218063 and 269479 also map to taxa 159273, 2708117, 2795027 and 327574. Their repeated count is cluster context, not sixteen F0382 genomes. The extraction owner at `src/taxonmech/extract.py:501` counts genome-to-species edges.
- GOLD: `data/raw/gold_organisms.tsv:479` supports one ORGANISM assertion. Native `data/gold/organisms.jsonl.gz:4960` identifies Go0005575, exact taxid 1035193, strain F0382 and culture-collection field BEI HM-754.
- MADIN: `data/raw/madin_taxa.tsv:669` supports five TRAIT_ASSERTIONs. The count alone does not establish a particular phenotype, disease association or mechanism.
- Scope: `data/taxa/PATHS.tsv:14407` and `curation/seed_scope.tsv:26086` identify this record. Its four-source reason agrees with the seed event of 2026-09-13T17:54:04Z; scope was added on 2026-09-12.

The following native and live genome metadata were inspected for completeness:

- GenBank `data/catalog/ncbi_genbank-0000.jsonl.gz:8027` and RefSeq `data/catalog/ncbi_refseq-0000.jsonl.gz:6893` identify current GCA_000318295.1 and GCF_000318295.1, respectively: 242 contigs, 127 scaffolds and 3,218,123 bp. The sources retain different annotation providers/counts; these are not extra biological genomes.
- The [live NCBI assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000318295.1/dataset_report) confirms both accessions are current and links F0382, PRJNA67197, SAMN02436687 and WGS AMEU01. Its ANI result is OK / genus_match, with a 96.86% best match to a C. endodontalis type assembly. This is a computational source result, not a locally resolved species identity.
- Complete [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN02436687&retmode=xml) gives F0382, taxid 1035193, human host and oral-cavity isolation source. It supplies no culture-collection attribute. No clinical phenotype is inferred from these sample-level fields.
- Native BV-BRC `data/bvbrc/bvbrc-0000.jsonl.gz:3315` gives PATRIC 1035193.3 with the same GenBank assembly, project and sample. Its collection field is blank and its strain field is bare F0382.
- GOLD's complete inspected chain is `Go0005575 -> Gp0005575 -> Ga0013857`, at organism line 4960, `data/gold/projects.jsonl.gz:4960` and `data/gold/analyses.jsonl.gz:7450`. It preserves GCA_000318295.1, IMG 2529292816, PRJNA67197 and SAMN02436687. The deposit lead is explicit in GOLD, but that does not make it an eligible existing TaxonMech strain-join key.
- The [BioProject page](https://www.ncbi.nlm.nih.gov/bioproject/67197) independently connects the monoisolate project to the assembly, BioSample, WGS master, GOLD Gp0005575 and IMG 2529292816. Sample/project/GOLD identifiers remain distinct from genome identifiers and counts.

## Completeness

The direct BacDive, LPSN, MediaDive and BactoTraits taxon tables have no exact target row. Ignored-independent searches for taxid, label-bearing designation, slug, source accessions and HM-754 found no matching BacDive or StrainInfo record. The initial BacDive Mx f382, Escherichia F382, Staphylococcus Crie-F382 and fungal F-382 records are distinct organisms, not deposit synonyms. They were inspected only to reject search collisions; their record reviews were not reopened.

No BacDive entry at this taxid and no descendants explains `strain_count: 0` under `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`. It does not mean no culture or genome exists. GOLD's BEI HM-754 is retained as a real source assertion, but the pinned CAFI registry has no BEI authority entry. Direct calls to the existing `normalize_culture_identifier` return empty for BEI HM-754, HM-754 and F0382. NCBI assembly-summary, GTDB and BV-BRC metadata supply only bare F0382. No compatible whole-deposit key was established, so absent nested links are not a separate defect under the current join contract.

Two attempted public BEI product URLs were unavailable through the browser tool; search did not yield an inspected BEI authority page. The live authority identity and supported registry representation remain follow-up work. This is not a claim that the BEI resource does not exist. Do not weaken the whole-authority/accession guard or transfer an unrelated F382 deposit to fill this gap.

The ignored-independent accession expansion found no exact SAMN02436687 ATB row. No assembly or FASTA was inferred from matching taxon names. The structured `imodulondb datasets` adapter completed successfully before open-ended follow-up; none of its 28 datasets covers Capnocytophaga. It is not applicable, not negative biological evidence. Optional definition, phenotype and causal-graph slots can remain empty.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species concept is promoted to exact strain identity.** `GTDB:s__Capnocytophaga_periodontitidis` is emitted as an equivalent xref and EXACT_SYNONYM `Capnocytophaga periodontitidis` on strain taxid 1035193. Native GTDB metadata support cluster membership of its genome, not equality between F0382 and a sixteen-genome species. LPSN independently assigns that species name to a different species-level taxid. This violates the true-equivalence boundary in `src/taxonmech/schema/taxonmech.yaml:180`. The maintained local owner is rank-insensitive promotion in `src/taxonmech/seed.py:449`, with regression coverage in `tests/test_seed.py`. The upstream kg-microbe closeMatch producer also needs rank- and direction-aware review. Mapping, synonym and xref manifestations are one finding.

Blockers: None found. Minor findings: None found. The NCBI identity is supported. Classification differences and the unverified BEI authority lead remain explicit qualifications, not grounds to replace the carried lineage or invent links.

## Recommended Edits

1. Make GTDB identity promotion in `src/taxonmech/seed.py` rank-aware. Retain supported source classification/counts without creating an equivalent species xref or exact species synonym on a strain record.
2. Ask the upstream kg-microbe mapping owner to assess rank and relationship direction rather than mechanically substitute a guessed broad/narrow predicate. Preserve NCBI oral-taxon identity and source-specific periodontitidis/endodontalis classifications.
3. Add a strain-versus-species case in `tests/test_seed.py`, preserving genuine species-level equivalences. Regenerate via maintained extraction/seeding inputs after an authorized fix; do not patch this YAML or raw inventories manually.
4. For later genome enrichment, verify BEI HM-754 at its authority and establish an explicit supported culture registry/inventory representation. Any registry update belongs in the maintained source/import process for `src/taxonmech/data/cafi_acronyms.json`, not a one-off permissive regex in `src/taxonmech/genome_sources.py`.
5. Preserve the full GOLD organism/project/analysis chain, exact accession versions, and the distinction between assembly, IMG/BV-BRC records, project and sample. Do not treat taxonomic agreement or a shared strain label as genome equivalence.

## Follow-up Checks

- After the rank-aware change, run `uv run pytest tests/test_seed.py` and this target's documented schema and strict commands.
- Confirm removal of the unsupported species synonym/equivalent xref while preserving the NCBI ID, thirteen ancestors, NCBI alias, genetic code, four attestations and source-scoped classification/count.
- Run actual full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc` after regeneration. Manual comparisons do not replace these gates.
- Retry the live GTDB species page and record its release before a taxonomy update. The page was unavailable; pinned native metadata and explicitly versioned HOMD context support this bounded review.
- Resolve the BEI authority lead before adding a culture/genome join. Require a supported whole-deposit identifier and preserve its source evidence; do not reuse unrelated F382 records.
- Recheck current assembly versions and source classifications before enrichment. Keep any future phenotype or mechanism evidence strain-specific rather than deriving it from a species name, annotation or count.

## Additional Notes

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, F0382/F382 separator variants and slug produced 27 candidate rows. Expansion with observed assembly, BioSample, WGS, GOLD, BioProject, IMG and HM-754 identifiers produced seven rows, all already included. All 27 distinct candidates were read in full using lossless structured decoding, including compressed source files. Separate exact scans read GTDB species/mappings and LPSN name rows. Five SOURCE.json files were searched structurally and history filenames checked separately. Absence findings are bounded to those sources, including ignored files.

The structured adapter command was `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. The main HOMD page failed, but the development page succeeded and is explicitly identified as such. NCBI APIs and LPSN succeeded; the GTDB and BEI page limitations are recorded above.

No source/YAML/generated-page edits, history events, review-status promotions, paid research, outbound contact or Git/GitHub mutations were performed. Eukaryota reviews were not reopened.
