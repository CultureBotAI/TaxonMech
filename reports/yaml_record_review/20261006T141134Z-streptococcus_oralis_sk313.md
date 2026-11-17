# YAML Record Review: Streptococcus oralis SK313

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptococcus_oralis_sk313.yaml`
- Started UTC: 2026-10-06T14:08:39Z
- Finished UTC: 2026-10-06T14:11:34Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1035190`, label `Streptococcus oralis SK313`, rank STRAIN, domain BACTERIA. The entire YAML was read before findings and checked byte-for-byte unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED with one GTDB mapping, three synonyms, one equivalent xref, genetic code 11, zero listed BacDive strains, three source attestations and one inline seed event. There is no definition, nomenclature entry, nested genome link, publication citation, gene claim or causal graph. Only this new report is written.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptococcus_oralis_sk313.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptococcus_oralis_sk313.yaml --out /private/tmp/sosk313-strict.tsv`: one file, zero ERROR rows. The actual TSV was read; it contains only its header.
- PASS, bounded manual comparison: exact identity, both NCBI synonyms, all ten root-first lineage entries, genetic code, source counts, scope and seed provenance match pinned inputs. This is not a focused corpus-reproduction validator.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- Ontology-node checking is not applicable because there are no curator-added grounded graph nodes. The documented product checker excludes taxonomy fields and delegates those to corpus reproduction.
- No separate target history artifact was found by the ignored-independent history filename search. Inline history passed schema validation and agrees with scope provenance. No external history validator was run against an invented artifact.
- There are no DOI, PMID, quoted-evidence or definition references in this YAML. No additional record-specific citation validator is documented in the inspected commands.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221914` and the inspected live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035190&retmode=xml) agree on label, strain rank, parent `NCBITaxon:1303`, both equivalent names and genetic code 11. The [taxonomy dataset response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035190) supplies the same root-inclusive ancestor IDs and rank STRAIN.

All ten pinned ancestors match the YAML, including Bacillati, Bacillota, Bacilli, Lactobacillales, Streptococcaceae, Streptococcus and S. oralis. Live XML supplies matching non-root labels/ranks. There are no children in the pinned backbone, and no exact target entries in the type-material, merged-ID or dropped tables.

The [LPSN species page](https://lpsn.dsmz.de/species/streptococcus-oralis) lists S. oralis as a validly published correct name and its type strain as SK23 / ATCC 35037 and other deposits, not SK313. The raw name at `data/raw/lpsn_names.tsv:20119`, lpsn:781364, maps to parent 1303 and the unsuffixed GTDB species. Parent nomenclature and type designations do not automatically belong to this strain record.

GTDB classifies the SK313 assembly within `s__Streptococcus oralis_BW`. The inspected [HOMD development genome page](https://devel.homd.org/genome/genome_description?gid=GCA_000223235.2) places it in HMT-0071 and labels its deposited organism as S. oralis subsp. tigurinus SK313, while displaying GTDB V226 / oralis_BW. These source classifications should remain distinguishable; none authorizes replacing the verbatim NCBI lineage locally.

## Evidence

- NCBI: the backbone and full native name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31367`, `31368` and `31369` support the label and both retained NCBI synonyms. Its attestation is one NAME.
- GTDB: `data/catalog/gtdb_genomes-0016.jsonl.gz:17794` identifies GB_GCA_000223235.2, strain SK313, taxid 1035190, project PRJNA67193 and sample SAMN00621710 in the oralis_BW cluster. The row explicitly says this genome is not the representative. This supports classification, not exact species/strain identity.
- GTDB count: `data/raw/gtdb_species.tsv:168989` records 14 cluster genomes, matching `data/raw/gtdb_mappings.tsv:1418`. The exact cluster scan also finds mappings at lines 2892, 17387, 170882, 312048 and 320979 to taxa 1077464, 1303, 2172545, 83427 and 936580, each carrying the same total. Fourteen is not a count of SK313 genomes. The extraction owner at `src/taxonmech/extract.py:501` counts genome-to-species edges.
- MADIN: `data/raw/madin_taxa.tsv:667` supports one TRAIT_ASSERTION count. The record does not assert a particular phenotype or mechanism, and none is inferred from that count.
- Scope: `data/taxa/PATHS.tsv:14405` and `curation/seed_scope.tsv:36170` identify the exact target. Its three-source reason agrees with the seed event of 2026-09-13T17:54:04Z; scope was added on 2026-09-12.

The following native and live metadata were inspected for completeness:

- `data/catalog/ncbi_genbank-0000.jsonl.gz:3883` identifies current GCA_000223235.2, five contigs and 1,888,813 bp. Historical `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:1192` records suppressed GCA_000223235.1; `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:1106` records suppressed GCF_000223235.1, withdrawn on 2020-06-30.
- The [live NCBI assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000223235.2/dataset_report) confirms current GenBank .2 and the suppressed RefSeq counterpart, with annotation-completeness and frameshift warnings. Its taxonomy check is OK / derived_species_match; the reported 94.41% ANI comparison is to a suspected-type S. oralis subsp. tigurinus assembly. This is source-qualified assembly metadata, not an independent determination of subspecies identity.
- The complete [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN00621710&retmode=xml) identifies SK313, taxid 1035190 and HMPREF9950. It supplies HMP body site Throat and supersite airways, but source material, collection date and geographic location are not determined. No culture-deposit identifier is supplied.
- Native BV-BRC `data/bvbrc/bvbrc-0000.jsonl.gz:3313` gives PATRIC 1035190.4, current GenBank GCA_000223235.2, project PRJNA67193 and sample SAMN00621710, with only bare designation SK313.
- GOLD's complete inspected chain is `Go0009743 -> Gp0009743 -> Ga0014024`, at `data/gold/organisms.jsonl.gz:8590`, `data/gold/projects.jsonl.gz:8452` and `data/gold/analyses.jsonl.gz:7616`. It supports that project/sample context, IMG 2529292983 and unversioned GCA_000223235. The organism culture-collection field is empty and its strain field is SK313. The chain therefore does not supply a whole-deposit match; do not append a version to GOLD's accession.
- The inspected [BioProject page](https://www.ncbi.nlm.nih.gov/bioproject/67193) independently links the monoisolate project to GCA_000223235.2, SAMN00621710, WGS master AFUU00000000, GOLD Gp0009743 and IMG 2529292983. These identifiers denote different entities and are not added together as genomes.

A bounded primary-literature follow-up inspected the article metadata and SK313-containing results/discussion paragraphs, with their adjacent context, in [Conrads et al. 2017](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5405715/fullTextXML), PMID 28473881, DOI 10.1080/20002297.2017.1307079. The paper explicitly includes SK313 among genome-sequenced gtfR-negative strains discussed as tigurinus-like, and associates it with AFUU00000000.1. This supports a taxonomic discussion lead, not a claim that SK313 caused the study's endocarditis cases or carries another strain's experimentally investigated virulence. The source's qualified classification is retained; no mechanism or clinical phenotype is transferred.

## Completeness

The direct BacDive, LPSN, transformed GOLD, MediaDive and BactoTraits taxon inventories have no exact target row. Native GOLD does contain the chain described above. No BacDive or StrainInfo match was found by the ignored-independent target/designation searches and accession expansions. These are bounded findings about inspected sources, not a claim that no culture exists.

With no BacDive entry at the target and no descendants, `strain_count: 0` implements the target-plus-descendants rule in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`. Bare SK313 is rejected by the existing CAFI whole-culture normalizer. The NCBI importer uses assembly-summary strain tags (`src/taxonmech/ncbi_assemblies.py:90`), and the inspected GTDB, BV-BRC and GOLD rows also provide only the bare designation. Neither shared taxon identity nor a matching strain name supplies the missing eligible deposit. An absent nested genome link is therefore not evidence loss under the current contract.

The exact ATB sample at `data/catalog/allthebacteria.tsv.xz:1004107` is NOT_PROCESSED with no available FASTA or assembly accession. The initial ATB hit at line 569660 is an unrelated M. tuberculosis row whose run identifier contains the target's digits. It cannot supply an SK313 assembly.

Before open-ended follow-up, `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` completed successfully. None of its 28 datasets covers S. oralis. Other Streptococcus datasets were not transferred. iModulonDB is not applicable, not negative biological evidence. Optional phenotype and causal-graph slots can remain empty.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species cluster is promoted to exact strain identity.** `GTDB:s__Streptococcus_oralis_BW` becomes an equivalent xref and EXACT_SYNONYM `Streptococcus oralis BW` for strain taxid 1035190. The native metadata establish cluster membership of the SK313 assembly, not identity between one strain and a 14-genome species cluster. This breaches the true-equivalence boundary in `src/taxonmech/schema/taxonmech.yaml:180`. The maintained local owner is rank-insensitive GTDB identity promotion at `src/taxonmech/seed.py:449`, with regression coverage in `tests/test_seed.py`. The upstream kg-microbe closeMatch producer also needs rank- and direction-aware review. Mapping/synonym/xref manifestations are counted as one finding.

Blockers: None found. Minor findings: None found. The NCBI identity is supported. Source-specific tigurinus classification and assembly warnings remain qualifications, not permission to rewrite the carried lineage or invent genome equivalence.

## Recommended Edits

1. Make GTDB identity promotion in `src/taxonmech/seed.py` rank-aware: retain supported cluster classification and source counts, but do not create an equivalent species-cluster xref or exact synonym on a strain taxon.
2. Have the upstream kg-microbe mapping owner assess rank and relationship direction rather than replacing closeMatch with a guessed broad/narrow predicate. Preserve the source suffix `oralis_BW`; its generated display form is not an independently established strain alias.
3. Add a strain-versus-species regression case in `tests/test_seed.py`, preserving supported species-level mappings. Regenerate through maintained extraction/seeding inputs after an authorized fix; do not hand-edit this YAML or raw inventories.
4. If later enriching genome links, first obtain explicit eligible deposit evidence. Keep GenBank's current version, historical/suppressed states and quality warnings, GOLD's unversioned assertion and its full chain. Do not change the whole-accession matcher to accept SK313 as a culture authority.
5. If a later task adds a discussion of the tigurinus placement, use a maintained curator mechanism and source-qualified evidence. Leave NCBI lineage verbatim and keep marker/genome analyses distinct from experimentally measured strain phenotypes.

## Follow-up Checks

- After the rank-aware change, run `uv run pytest tests/test_seed.py`, then this target's documented schema and strict commands.
- Confirm removal of the unsupported GTDB exact synonym/equivalent xref while preserving the NCBI ID, all ten ancestors, two NCBI aliases, three source attestations and source-scoped cluster membership/count.
- Run the actual full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc` gates after regeneration. The manual source comparisons here do not replace those checks.
- Retrieve the live GTDB taxon page and record its release before any taxonomic update. It was unavailable during this review; the pinned native metadata and explicitly versioned HOMD context support this bounded finding.
- Recheck current versus suppressed assembly status before enrichment. Preserve the annotation and frameshift warnings; do not reinterpret a source ANI result as a locally reconciled taxonomy.
- Require explicit whole-deposit evidence for any later strain/genome join and exact BioSample evidence for any ATB addition. Do not transfer parent strains, type designations or another culture's experimental results.

## Additional Notes

Ignored-independent candidate searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial taxid, designation/separator and slug searches produced 26 rows. Expansion with observed assembly, sample, WGS, GOLD, project and IMG identifiers produced nine rows, one new. All 27 distinct candidate rows were read in full using lossless structured decoding; numeric and longer-designation collisions were rejected. Separate exact structured scans read the GTDB cluster/mapping rows and parent LPSN row. Five SOURCE.json files were searched structurally, and history filenames checked separately. Absence statements are bounded to those roots and inspected authority responses, including ignored and compressed files.

The main HOMD page failed; its accessible development page is explicitly identified above. The publisher article page failed and PMC returned a browser challenge; the public Europe PMC full-text XML endpoint succeeded. Only article identifiers and the relevant textual context were inspected, not supplementary experiments or figure images. No access-control bypass, paid research or outbound contact was performed.

No source/YAML/generated-page edits, history events, review-status promotions or Git/GitHub mutations were performed. Eukaryota reviews were not reopened.
