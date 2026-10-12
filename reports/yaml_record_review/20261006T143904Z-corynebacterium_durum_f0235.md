# YAML Record Review: Corynebacterium durum F0235

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/corynebacterium_durum_f0235.yaml`
- Started UTC: 2026-10-06T14:36:01Z
- Finished UTC: 2026-10-06T14:39:04Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1035195`, label `Corynebacterium durum F0235`, rank STRAIN, domain BACTERIA. The entire YAML was read before findings and checked byte-for-byte unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED with ten root-first ancestors, one GTDB mapping, three synonyms, one equivalent xref, genetic code 11, zero listed strains, three source attestations and one inline seed event. There are no nested genome links, nomenclature entries, definition, publication citations or causal graph. Only this new review report is written.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/corynebacterium_durum_f0235.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/corynebacterium_durum_f0235.yaml --out /private/tmp/cdf0235-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: pinned identity, aliases, all ten lineage entries, genetic code, source counts, scope and seed provenance agree. These comparisons are not a focused corpus-reproduction validator.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- No curator-added ontology graph nodes require term validation. The documented product checker excludes taxonomy fields and delegates them to corpus reproduction.
- No separate target history artifact was found by the ignored-independent history filename search. Inline history passed schema validation and agrees with scope provenance. No external history validator was run against an invented artifact.
- The YAML contains no DOI, PMID, definition reference or quoted evidence. No additional record-specific citation validator is documented in the inspected commands.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221918`, inspected [live NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035195&retmode=xml), and [NCBI taxonomy dataset response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035195) agree on the strain identity, parent `NCBITaxon:61592`, two equivalent names and genetic code 11. All ten root-inclusive ancestor identifiers agree. Pinned labels/ranks match the YAML, and live XML confirms the non-root lineage. No children, exact type-material entry, merged-ID entry or dropped entry were found in their pinned structured tables.

The inspected [legacy NCBI browser page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1035195), returned from a three-month-old crawl, displays no rank. Both current API responses and the pinned backbone instead supply STRAIN. This temporal/source discrepancy is preserved rather than silently changing the record to the cached browser value.

The [LPSN species page](https://lpsn.dsmz.de/species/corynebacterium-durum), record 775179, concerns the validly published species and its type strain IBS G-15036, including CCUG 37331, CIP 105490, DSM 44351, DSM 45333 and JCM 11948. The exact raw row at `data/raw/lpsn_names.tsv:16456` maps to species taxid 61592, not F0235. Species nomenclature and type identity should not be inherited by this strain.

NCBI's legacy LinkOut includes a species type-strain BacDive link. The inspected [BacDive 3181 page](https://bacdive.dsmz.de/strain/3181) explicitly identifies that type deposit group, carries taxid 61592 and links SI-ID 12971. It does not establish F0235 as a member of that group. A LinkOut shown on this taxon page is not sufficient strain identity evidence.

GTDB's native family is Mycobacteriaceae, whereas the carried NCBI lineage uses Corynebacteriaceae. These remain source-specific classifications, not grounds for locally replacing the NCBI lineage. Unsupported species-to-strain equivalence is the major finding below.

## Evidence

- NCBI: complete native rows at `data/catalog/ncbi_names-0005.jsonl.gz:31379` through 31381 support the scientific name and both equivalent aliases. The source attestation counts one NAME, not three aliases.
- GTDB: `data/catalog/gtdb_genomes-0006.jsonl.gz:31191` identifies RS_GCF_000318135.1, F0235, taxid 1035195 and SAMN02436928 in the C. durum cluster. It marks this genome as not the representative and retains its bare strain designation rather than a culture identifier.
- GTDB count: `data/raw/gtdb_species.tsv:46238` and `data/raw/gtdb_mappings.tsv:1422` carry 27 cluster genomes. The same cluster maps to taxid 556548 at mapping line 296468 and parent species 61592 at line 299760. This is not a count of F0235 genomes. The extraction owner at `src/taxonmech/extract.py:501` counts genome-to-species edges.
- MADIN: `data/raw/madin_taxa.tsv:671` supports one TRAIT_ASSERTION. That count alone does not establish a specific phenotype, isolation outcome or mechanism.
- Scope: `data/taxa/PATHS.tsv:14409` and `curation/seed_scope.tsv:36172` identify this target. Its three-source reason and 2026-09-12 scope date agree with the seed event of 2026-09-13T17:54:04Z.

The following complete native and live genome metadata were inspected for completeness, without treating all their identifiers as interchangeable genomes:

- GenBank `data/catalog/ncbi_genbank-0000.jsonl.gz:8019` and RefSeq `data/catalog/ncbi_refseq-0000.jsonl.gz:6885` identify GCA_000318135.1 and GCF_000318135.1, with 44 contigs, 20 scaffolds and 2,809,576 bp. Their source annotation dates and gene counts differ; these differences do not create extra genomes.
- The [live NCBI assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000318135.1/dataset_report) confirms both accessions are current, taxid 1035195, strain F0235, PRJNA67201, SAMN02436928 and WGS AMEM01. Its ANI status is OK / species_match, with 97.32% identity against a C. durum type assembly. This computational comparison does not make F0235 the type strain or equivalent to the species.
- Complete [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN02436928&retmode=xml) identifies F0235, the exact taxid, human host and oral-cavity isolation source. It contains no culture-collection attribute. No clinical phenotype is inferred from sample origin.
- `data/bvbrc/bvbrc-0000.jsonl.gz:3317` supplies PATRIC 1035195.3 with the same GenBank assembly, sample and project. Its collection field is blank and its strain field contains only F0235.
- GOLD's complete native chain is `Go0010541 -> Gp0010541 -> Ga0016259`, inspected at `data/gold/organisms.jsonl.gz:9261`, `data/gold/projects.jsonl.gz:9126` and `data/gold/analyses.jsonl.gz:9788`. It supplies exact taxid 1035195, GCA_000318135.1, IMG 2537561950, PRJNA67201 and SAMN02436928. The organism's culture-collection field explicitly says BEI HM-755. The analysis has an empty organism field, not an organism conflicting with its project chain.
- The [BioProject page](https://www.ncbi.nlm.nih.gov/bioproject/67201) independently links the monoisolate project to the assembly, sample, WGS master, GOLD Gp0010541 and IMG 2537561950. Project, sample, GOLD organism and analysis IDs remain related records, not genome counts.

## Completeness

The transformed BacDive, LPSN, GOLD, MediaDive and BactoTraits taxon tables have no exact target row. Native GOLD metadata are nevertheless present, as described above; an absent transformed attestation is not a claim that the source lacks this strain.

Ignored-independent searches found no eligible F0235 BacDive or StrainInfo record. The retrieved YIM F235 / DSM 29932 record belongs to Deinococcus; other f235/F-235 matches denote unrelated enrichment clones, bacteria or fungal deposits. Complete candidate rows were inspected only to reject these identity collisions, not to reopen their reviews. No BacDive entry at this taxid and no descendants explains `strain_count: 0` under `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`. It does not mean that F0235 has no physical culture or sequenced genome.

GOLD's BEI HM-755 is a real source assertion, but an ignored-independent search found no BEI authority in `src/taxonmech/data/cafi_acronyms.json`. Calls to the existing `normalize_culture_identifier` return empty for BEI HM-755, HM-755 and F0235. The NCBI assembly-summary, GTDB and BV-BRC fields supply only bare F0235. No supported existing whole-deposit join key was established, so absent nested genome links are not a separate required-representation defect under the current contract.

Two attempted public BEI product URLs were unavailable through the browser tool, and search produced no inspected BEI authority page. The authority-level identity and registry representation remain unresolved follow-up work; this is not a claim that BEI HM-755 does not exist. Do not weaken the culture-identifier guard or reuse the species type-strain group to fill this gap.

The accession expansion found no exact SAMN02436928 ATB row, including ignored/compressed sources. The initial ATB search hit is for SAMN02228251 and a different F235-bearing strain, not this target; it cannot be transferred. The structured `imodulondb datasets` adapter returned 28 datasets before open-ended follow-up. It covers C. glutamicum, not C. durum F0235. No glutamicum module evidence was borrowed. Absence from iModulonDB is not negative biological evidence. Optional definition, phenotype and causal-graph slots can remain empty.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species concept is promoted to exact strain identity.** `GTDB:s__Corynebacterium_durum` is emitted as an equivalent xref and species-name EXACT_SYNONYM on strain taxid 1035195. Native GTDB metadata support membership of F0235's genome in the 27-genome species cluster, not identity of that cluster with this strain. LPSN assigns the species concept to parent taxid 61592. This violates the true-equivalence contract in `src/taxonmech/schema/taxonmech.yaml:180`. The maintained local owner is rank-insensitive promotion in `src/taxonmech/seed.py:449`, with regression coverage in `tests/test_seed.py`. The upstream kg-microbe closeMatch producer also needs rank- and direction-aware review. Mapping, synonym and xref manifestations are one finding.

Blockers: None found. Minor findings: None found. NCBI identity is supported. The cached browser discrepancy, family classification difference and unresolved BEI authority lead remain explicit qualifications, not grounds for inventing lineage or genome links.

## Recommended Edits

1. Make GTDB identity promotion in `src/taxonmech/seed.py` rank-aware. Preserve supported classification and cluster counts without creating an equivalent species xref or exact species synonym on a strain record.
2. Review rank and relationship direction in the upstream kg-microbe mapping producer rather than mechanically substituting a guessed broad/narrow predicate. Preserve the carried NCBI lineage.
3. Add a strain-versus-species regression in `tests/test_seed.py`, retaining genuine species-level equivalences. Regenerate through maintained extraction/seeding inputs after an authorized fix; do not patch this generated YAML or raw tables manually.
4. For later genome enrichment, verify BEI HM-755 at its authority and establish a supported culture registry/inventory representation. Any registry correction belongs in the maintained source/import process for `src/taxonmech/data/cafi_acronyms.json`, not a permissive one-off regex in `src/taxonmech/genome_sources.py`.
5. Preserve the explicit GOLD organism/project/analysis chain and accession versions. Do not conflate assembly, IMG/PATRIC records, sample, project or species type-strain identifiers.

## Follow-up Checks

- After an authorized rank-aware change, run `uv run pytest tests/test_seed.py` and this target's documented schema and strict commands.
- Confirm removal of the unsupported species synonym/equivalent xref while preserving the NCBI ID, ten ancestors, two NCBI aliases, genetic code, three attestations and source-scoped GTDB classification/count.
- Run actual full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc` after regeneration. Manual comparisons do not replace those gates.
- Retry the GTDB species page and record its release before a classification update; it was unavailable here. Pinned native metadata support the bounded classification review.
- Resolve BEI HM-755 authority evidence before introducing a culture/genome join. Require a supported whole-deposit identifier, not the label F0235 or a species-wide LinkOut.
- Recheck current assembly versions before enrichment. Any future phenotype or mechanism assertion needs separately inspected strain-specific evidence, not an annotation, aggregate count or species description.

## Additional Notes

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid 1035195, F0235/F235 separator variants and the target slug produced 36 candidate rows. Expansion with observed assembly, BioSample, BioProject, WGS, GOLD, IMG, PATRIC and HM-755 identifiers produced seven rows, all already included. All 36 distinct candidates were read in full using lossless structured decoding, including compressed source files. Separate exact scans read GTDB species/mapping and LPSN rows, lineage/status tables and scope. Five SOURCE.json files were searched structurally and history filenames checked separately. Absence findings are bounded to those sources, including ignored files.

The adapter command was `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. NCBI APIs, LPSN and the species type-strain BacDive page succeeded. GTDB, two BEI product routes and the attempted HOMD development genome page were unavailable. Search snippets were not used as evidence of strain equivalence or experimental phenotype.

No source/YAML/generated-page edits, history events, review-status promotions, paid research, outbound contact or Git/GitHub mutations were performed. Eukaryota reviews were not reopened.
