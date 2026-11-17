# YAML Record Review: Streptococcus infantis SK970

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptococcus_infantis_sk970.yaml`
- Started UTC: 2026-10-06T14:03:44Z
- Finished UTC: 2026-10-06T14:07:11Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1035189`, label `Streptococcus infantis SK970`, rank STRAIN, domain BACTERIA. The entire YAML was read before findings and checked byte-for-byte unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED with one GTDB mapping, three synonyms, one equivalent xref, genetic code 11, zero listed BacDive strains, three source attestations and one inline seed event. It contains no definition, nomenclature entry, nested genome links, publication citation, gene claim or causal graph. Only this new report is written.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptococcus_infantis_sk970.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptococcus_infantis_sk970.yaml --out /private/tmp/sisk970-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: identity, both NCBI synonyms, all ten root-first ancestor entries, genetic code, source counts, scope and seed provenance match pinned rows. This is not a focused corpus-reproduction validator.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- Ontology-node checking is not applicable: the record has no curator-added grounded graph nodes. The documented product checker excludes taxonomy fields and delegates them to corpus reproduction.
- No separate target history artifact was found by the ignored-independent history filename search. Inline history passed schema validation and was compared to scope provenance. No external history validator was run against an invented artifact.
- There are no DOI, PMID, quoted evidence or definition references in this YAML. No additional record-specific citation validator is documented in the inspected local commands.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221913` and inspected live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035189&retmode=xml) agree on label, strain rank, parent `NCBITaxon:68892`, genetic code 11 and both equivalent names. The [taxonomy dataset response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035189) supplies the matching root-inclusive ancestor IDs and rank STRAIN.

All ten pinned lineage entries match the YAML, including Bacillati, Bacillota, Bacilli, Lactobacillales, Streptococcaceae, Streptococcus and S. infantis. Live XML supplies the matching non-root labels/ranks. The pinned backbone has no children of the target; type-material, merged-ID and dropped tables contain no exact target entry.

The [LPSN species page](https://lpsn.dsmz.de/species/streptococcus-infantis) lists S. infantis as the validly published correct name and its type as ATCC 700779 / CCUG 39817 and other listed deposits, not SK970. Raw LPSN row `data/raw/lpsn_names.tsv:20106`, lpsn:781349, maps to parent 68892 and the unsuffixed GTDB species. It is not a nomenclature assertion for strain taxid 1035189. No parent type material is transferred to this strain.

GTDB places the SK970 assembly in the separate cluster `s__Streptococcus infantis_G`. NCBI lineage is retained independently; a cluster with one currently inventoried genome still is not identical in scope to a strain.

## Evidence

- NCBI: the backbone and complete native names at `data/catalog/ncbi_names-0005.jsonl.gz:31364`, `31365` and `31366` support the scientific label and both retained NCBI synonyms. The NCBI attestation is one NAME.
- GTDB: the full native row at `data/catalog/gtdb_genomes-0015.jsonl.gz:2186` names GB_GCA_000223255.2 as the cluster representative, with taxid 1035189, strain SK970, BioSample SAMN00621709 and project PRJNA67191. It supports genome classification, not species/strain equivalence.
- GTDB count: `data/raw/gtdb_species.tsv:168816` and `data/raw/gtdb_mappings.tsv:1417` agree on one genome and the supplied closeMatch. The complete mapping scan finds only this target for the exact suffixed cluster. The count is a pinned source cluster count; `src/taxonmech/extract.py:501` counts genome-to-species edges.
- MADIN: `data/raw/madin_taxa.tsv:666` supports one TRAIT_ASSERTION count. The YAML does not assert a particular phenotype, growth condition or experimental mechanism, and none is inferred from that count.
- Scope: `data/taxa/PATHS.tsv:14404` and `curation/seed_scope.tsv:36169` identify this target. Its three-source scope reason agrees with the inline seed event of 2026-09-13T17:54:04Z; scope was added on 2026-09-12.

The following complete native evidence was inspected for genome completeness, not automatically promoted to new record assertions:

- `data/catalog/ncbi_genbank-0000.jsonl.gz:3884` identifies current GCA_000223255.2, nine contigs and 1,945,605 bp. Historical `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:1193` contains suppressed GCA_000223255.1, while `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:1107` contains suppressed GCF_000223255.1, withdrawn on 2020-12-30.
- The inspected [live assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000223255.2/dataset_report) confirms current GenBank .2 and the suppressed RefSeq counterpart, with annotation-completeness and frameshift warnings. Its taxonomy check is inconclusive: reported ANI is 91.99% against a suspected-type S. infantis assembly. This qualifies the assembly's species placement; it does not break the NCBI strain identifier or authorize a local lineage rewrite.
- The complete [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN00621709&retmode=xml) gives SK970, taxid 1035189, HMPREF9954, HMP body site Blood and source material CCUG 27560. That deposit assertion is explicit but conflicts with another inspected source association below.
- Native BV-BRC `data/bvbrc/bvbrc-0000.jsonl.gz:3312` gives PATRIC 1035189.4, GCA_000223255.2, PRJNA67191 and SAMN00621709, with only the bare strain identifier SK970.
- GOLD's full native chain is `Go0009742 -> Gp0009742 -> Ga0015433`, read at `data/gold/organisms.jsonl.gz:8589`, `data/gold/projects.jsonl.gz:8451` and `data/gold/analyses.jsonl.gz:8991`. It supplies project PRJNA67191, sample SAMN00621709, IMG 2534681984 and unversioned GCA_000223255. The organism's culture-collection field is empty and its strain field is SK970, so this chain supplies no eligible whole-deposit match. Do not append a version to GOLD's accession.
- The inspected [BioProject page](https://www.ncbi.nlm.nih.gov/bioproject/67191) independently connects the monoisolate project to the current assembly, sample, WGS master AFUT00000000, GOLD project and IMG identifier. These are distinct source entities, not additional genomes.
- The accessible [HOMD development genome page](https://devel.homd.org/genome/genome_description?gid=GCA_000223255.2) links the same assembly to HMT-0638 and labels its GTDB context V226 / S. infantis_G. This corroborates source classification but is not a substitute for a current GTDB release audit.

## Completeness

The pinned direct BacDive, LPSN, transformed GOLD, MediaDive and BactoTraits taxon inventories have no exact target row; the native GOLD chain does exist as detailed above. With no BacDive strains filed at this target and no descendants, `strain_count: 0` correctly follows the documented target-plus-descendants rule in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`. It is not a statement that no culture or genome exists.

An ignored-independent expansion for the BioSample's whole deposit CCUG 27560 found one native catalog row: `data/bvbrc/bvbrc-0000.jsonl.gz:1736` assigns that deposit to Streptococcus oralis SK255, taxid 1005704, PATRIC 1005704.3, GCA_000215365.2 and a different BioSample, SAMN00621703. This is conflicting source identity metadata, not proof that SK255 and SK970 are equivalent or that one source is correct. No corresponding eligible BacDive or StrainInfo deposit was found by the named searches. The direct CCUG catalogue URL could not be retrieved, so the conflict remains unresolved. No verdict on the other taxon's full record is made here.

The existing CAFI normalizer accepts CCUG 27560 as CCUG-27560 but rejects bare SK970. Format validity alone does not resolve the conflicting source association. Current direct NCBI ingestion reads assembly-summary strain tags (`src/taxonmech/ncbi_assemblies.py:90`), not BioSample source-material fields. GTDB/BV-BRC/GOLD SK970 rows likewise lack an eligible explicit deposit key. The absence of nested genome links is therefore not evidence loss under the current contract; a later enrichment requires verified deposit identity and maintained source support.

The exact ATB sample at `data/catalog/allthebacteria.tsv.xz:1004106` is NOT_PROCESSED with no available FASTA or assembly accession. Two additional full ATB rows, at lines 85494 and 258589, carry the same sylph species label S. infantis_G but different BioSamples, SAMEA104151619 and SAMEA114309594. Shared classification cannot attach those assemblies to SK970. Initial ATB hits at lines 569659 and 1961912 were unrelated run/checksum substring matches.

Before open-ended follow-up, the structured command `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` was attempted. Sandbox DNS failed; the read-only network-approved retry succeeded. None of its 28 datasets covers S. infantis. Other Streptococcus datasets were not transferred. iModulonDB is not applicable, not negative biological evidence. No optional phenotype or causal graph needs to be invented.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species cluster is promoted to exact strain identity.** The mapping to `GTDB:s__Streptococcus_infantis_G` produces both an equivalent xref and EXACT_SYNONYM `Streptococcus infantis G`. The inspected metadata support SK970 as the representative genome of this currently single-genome cluster, not identity between the strain and the species concept. Singleton membership does not remove the scope difference. This violates the true-equivalence boundary in `src/taxonmech/schema/taxonmech.yaml:180`. The maintained local owner is rank-insensitive identity promotion at `src/taxonmech/seed.py:449`, with regression coverage in `tests/test_seed.py`. The upstream kg-microbe closeMatch producer also needs rank- and direction-aware review. Mapping, synonym and xref manifestations are counted as one finding.

Blockers: None found. Minor findings: None found. The CCUG metadata conflict and assembly-quality/classification qualifications are unresolved context, not false claims currently asserted by this YAML.

## Recommended Edits

1. Make GTDB identity promotion in `src/taxonmech/seed.py` rank-aware. Preserve source-scoped cluster classification and its count, but do not emit a species-cluster identifier as an equivalent strain xref or exact strain synonym.
2. Have the upstream kg-microbe mapping owner assess rank and relationship direction; do not mechanically replace closeMatch with a guessed broad/narrow predicate. Preserve the source suffix `infantis_G`; the generated display form `infantis G` is not an independently documented strain alias.
3. Add a singleton-cluster/strain regression case in `tests/test_seed.py`, while retaining supported species-level behavior. Regenerate through maintained extraction/seeding inputs after an authorized fix, not by hand-editing this YAML or raw inventories.
4. Treat CCUG 27560 as an unresolved deposit lead until its authority and the SK255/SK970 source assertions are reconciled. Any later BioSample enrichment belongs in maintained source ingestion and its configured inputs, with explicit conflict handling and whole-deposit evidence. Do not create or join a BacDive strain from a bare alias.
5. Preserve current versus suppressed accession status and the assembly's quality/taxonomy warnings during future enrichment. Do not collapse assemblies, projects, samples, GOLD entities or ATB species matches into genome equivalence.

## Follow-up Checks

- After the rank-aware change, run `uv run pytest tests/test_seed.py` and this target's documented schema and strict commands.
- Confirm removal of the unsupported GTDB exact synonym/equivalent xref while retaining the NCBI ID, all ten ancestors, both NCBI synonyms, three source attestations and source-scoped cluster membership/count.
- Run actual full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc` after regeneration. Manual comparisons in this report do not replace those gates.
- Retrieve a populated live GTDB taxon/genome record and its release before a taxonomic update. The tree page failed and the genome page returned an unpopulated loading shell.
- Resolve the CCUG catalogue and compare pinned source material for both SK970 and SK255 before any deposit link is added. Require a matched BacDive/eligible deposit identity under the maintained model, not just a syntactically valid accession.
- Recheck GenBank/RefSeq states and preserve the annotation and inconclusive-ANI qualifications. Recheck ATB availability using the exact target BioSample; do not transfer the other two assemblies sharing its sylph classification.

## Additional Notes

Ignored-independent candidate searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial taxid, designation/separator and slug searches produced 23 candidate rows. Expansion with observed assembly, sample, WGS, GOLD, project, IMG and GTDB species identifiers produced 11 rows, three new; the deposit search added one. All 27 distinct candidate rows were read fully using lossless structured decoding. Separate exact structured scans read the GTDB species/mapping rows and parent LPSN row. Five SOURCE.json files were searched structurally; history filenames were checked separately. Absence statements are bounded to those roots, spellings and inspected authority responses, including ignored and compressed files.

The main HOMD page and direct CCUG page were unavailable; the accessible HOMD development page is explicitly identified above. BioProject succeeded using the numeric URL after the accession URL timed out. Search snippets for literature/proteins were treated only as leads, not experimental evidence; this YAML has no such cited claim. No access-control bypass, paid research or outbound contact was performed.

No source/YAML/generated-page edits, history events, review-status promotions or Git/GitHub mutations were performed. Eukaryota reviews were not reopened.
