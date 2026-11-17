# YAML Record Review: Streptococcus mitis SK569

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptococcus_mitis_sk569.yaml`
- Started UTC: 2026-10-06T13:47:49Z
- Finished UTC: 2026-10-06T13:51:58Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1035187`, label `Streptococcus mitis SK569`, rank STRAIN, domain BACTERIA. The entire YAML was read before findings and checked byte-for-byte unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED, with one GTDB mapping, three synonyms, one equivalent xref, genetic code 11, zero listed BacDive strains, three source attestations and one inline seed event. It contains no definition, nomenclature entry, citation, quoted evidence, gene claim or causal graph. Only this new report is written.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptococcus_mitis_sk569.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptococcus_mitis_sk569.yaml --out /private/tmp/smsk569-strict.tsv`: one file, zero ERROR rows. The actual TSV was read; only its header is present.
- PASS, bounded manual comparison: exact identity, two NCBI aliases, all 11 root-first lineage entries, genetic code, source counts, scope and seed provenance match their pinned rows. This is not a focused corpus-reproduction validator.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- Ontology-node checking is not applicable to this target because it has no curator-added grounded graph nodes. The documented product checker excludes taxonomy fields and delegates those to corpus reproduction.
- No separate target history artifact was found by the ignored-independent history filename search. Inline history passed the schema check and was compared to scope provenance. No external history validator was run against an invented artifact.
- No DOI, PMID, definition citation or causal-edge reference occurs in this YAML. No additional record-specific citation validator is documented in the inspected local commands.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221911` and the inspected live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035187&retmode=xml) agree on label, strain rank, parent `NCBITaxon:28037`, both equivalent names and genetic code 11. The [NCBI taxonomy dataset response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035187) independently supplies rank STRAIN and the same root-inclusive ancestor IDs.

The complete pinned lineage matches the YAML, including Bacillati, Bacillota and `NCBITaxon:3409772`, Streptococcus mitis group. Live XML supplies the matching non-root ancestor labels/ranks. The backbone contains no children of the target; the merged-ID, type-material and dropped tables have no exact target entry. Cached browser search text showing an older rank was not used over the inspected authority responses.

GTDB names the genome's cluster `s__Streptococcus mitis_N`. The strain is the representative genome of that cluster in the pinned native metadata. Representative status does not make one strain identical to the species cluster. NCBI lineage is retained independently.

## Evidence

- NCBI: the backbone row and native names at `data/catalog/ncbi_names-0005.jsonl.gz:31356`, `31357` and `31358` support the label and both NCBI exact synonyms. The NCBI attestation is one NAME.
- GTDB: `data/catalog/gtdb_genomes-0001.jsonl.gz:21413` names taxid 1035187, strain SK569, representative accession `GB_GCA_000222785.2`, sample `SAMN00621701`, project `PRJNA67187` and species S. mitis_N. It is direct genome-classification evidence, not species/strain equivalence.
- GTDB counts: `data/raw/gtdb_species.tsv:168954` records four genomes in that cluster; `data/raw/gtdb_mappings.tsv:1415` repeats that value for this taxon. Three other mappings carry the same four-genome total for NCBI targets 1095735, 257758 and 28037. The count matches the inventory but is not four genomes of SK569. The extraction code at `src/taxonmech/extract.py:501` counts genome-to-species edges.
- MADIN: `data/raw/madin_taxa.tsv:664` supports one TRAIT_ASSERTION count. The YAML asserts no particular trait value or experimental mechanism, and none is inferred from the count.
- Scope: `data/taxa/PATHS.tsv:14402` and `curation/seed_scope.tsv:36168` identify this exact record. The scope reason and three sources agree with the seed event of 2026-09-13T17:54:04Z; scope was added on 2026-09-12.

The following evidence was inspected to establish completeness and avoid confusing a zero listed-strain count with absence of a deposited strain:

- [CCUG 62643](https://www.ccug.se/strain?id=62643) explicitly gives aliases SK569 and H2112 and identifies a human-blood isolate from Lausanne, deposited by M. Kilian. This is a whole deposit identity link, not a shared species-name inference.
- [BacDive 156544](https://bacdive.dsmz.de/strain/156544) and the full native row at `data/bacdive/records.jsonl.gz:78783` identify CCUG 62643 but classify it at species taxid 28037. The native row says type strain no and has empty sequence information. `data/raw/bacdive_strains.tsv:78784` and `data/raw/culture_collection_strains.tsv:34355` preserve that classification and deposit.
- The full native StrainInfo row at `data/straininfo/records.jsonl.gz:308674` and inspected live [StrainInfo API record](https://api.straininfo.dsmz.de/v2/data/strain/max/410787) agree on SI-ID 410787, available deposit SI-DP 918659, CCUG 62643, aliases SK569/H2112, non-type status and species taxid 28037. The source record version is DOI 10.60712/SI-ID410787.2. The live maximum record contains no sequence assertion.
- GOLD's full native chain is `Go0009705 -> Gp0009705 -> Ga0015431`, inspected at `data/gold/organisms.jsonl.gz:8559`, `data/gold/projects.jsonl.gz:8418` and `data/gold/analyses.jsonl.gz:8989`. The organism explicitly supplies CCUG 62643. The project supplies PRJNA67187 and SAMN00621701; the analysis supplies IMG 2534681982 and unversioned GCA_000222785. Do not append a version to GOLD's unversioned assertion.
- The corresponding maintained inventories contain one GOLD assembly assertion at `data/raw/strain_assemblies.tsv:63528`, one IMG assertion at `data/raw/strain_genome_records.tsv:48984`, and five related records at `data/raw/strain_related_records.tsv:201765` through `201769`. All retain the explicit CCUG match and organism/project chain. StrainInfo contributes its strain and deposit context at `data/straininfo/strain_links.tsv:54710` and `data/straininfo/related_records.tsv.gz:129372`, `129373`.
- The existing culture-ID normalizer confirms CCUG 62643 matches `kgmicrobe.strain:CCUG-62643`, while SK569 and H2112 are not eligible culture-deposit join keys. There is no reason to relax whole-accession checks.
- The exact BacDive 156544 block on `data/taxa/bacteria/streptococcus_mitis.yaml` was inspected as context only. It already retains that deposit, the GOLD assembly and IMG assertion, five GOLD related records, and two StrainInfo related records. No verdict on the full parent record is made here.

The inspected [NCBI assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000222785.2/dataset_report) identifies current GenBank GCA_000222785.2, 54 contigs and 1,975,266 bp, but marks paired RefSeq GCF_000222785.1 suppressed. It flags unverified source organism and an inconclusive taxonomy check. This is a qualification on the assembly's classification, not evidence that the NCBI taxon identifier is broken. The full [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN00621701&retmode=xml) explicitly links SK569 to source material CCUG 62643.

The native current GenBank row at `data/catalog/ncbi_genbank-0000.jsonl.gz:3871` agrees. Historical rows `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:1186` and `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:1103` preserve the suppressed GenBank .1 and RefSeq .1 statuses. The [BioProject page](https://www.ncbi.nlm.nih.gov/bioproject/67187) links the same monoisolate, current assembly, sample, WGS master AFUF00000000, GOLD project and IMG record. `data/bvbrc/bvbrc-0000.jsonl.gz:3310` independently associates BV-BRC 1035187.4 with that current GenBank assembly.

## Completeness

The zero listed-strain count faithfully implements the documented subtree rule in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: gather BacDive strains filed at the target or below it, not all strains filed at its parent. BacDive 156544 is filed at species 28037 and is already represented there. The GOLD link's taxon_id is the source genome's classification; it does not reclassify the BacDive strain. The missing nested links on this particular strain-taxon page are therefore a documented placement limitation, not lost inventory evidence or an incorrect count under the current contract. An explicit cross-classification presentation/model improvement would need separate design and evidence.

No exact target row occurs in the direct BacDive, LPSN, transformed GOLD, MediaDive or BactoTraits taxon inventories. Native GOLD evidence and the parent-classified BacDive deposit do exist, as detailed above. Source units are kept separate; NAME, GENOME and TRAIT_ASSERTION counts are not summed.

The exact ATB sample is NOT_PROCESSED with no available FASTA or assembly accession. This agrees across `data/catalog/allthebacteria.tsv.xz:1004098`, `data/atb/assemblies.tsv:2162` and exclusion `data/atb/exclusions.tsv:1427` (assembly_unavailable). It does not justify an ATB genome link. Initial ATB hits at lines 569657 and 1310770 were unrelated sample/run or checksum substring collisions.

A bounded literature follow-up inspected Table 1 and its deposit footnote plus the relevant results in [Harth-Chu et al. 2019](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.02567/full), DOI 10.3389/fmicb.2019.02567. It independently connects SK569/H2112 to CCUG 62643 and includes SK569 among high-PcsB strains in condition-specific biofilm/complement experiments. These are potential strain-specific enrichment evidence, not permission to infer species-wide phenotypes or a causal mechanism from group correlations. Optional phenotype and graph slots need not be populated by this review.

Before assessing that experimental lead, the structured command `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` completed successfully. None of its 28 datasets covers S. mitis or SK569. S. pneumoniae and S. pyogenes modules were not transferred. iModulonDB is not applicable here, not negative biological evidence.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species cluster is promoted to exact strain identity.** The source mapping to `GTDB:s__Streptococcus_mitis_N` becomes both an equivalent xref and EXACT_SYNONYM `Streptococcus mitis N`. The native GTDB metadata establish SK569 as a representative genome of that cluster; they do not make one strain equivalent to the cluster or its four genomes. The xref violates the true-equivalence boundary in `src/taxonmech/schema/taxonmech.yaml:180`. The local maintained owner is the rank-insensitive GTDB identity promotion in `src/taxonmech/seed.py:449`; regression tests belong in `tests/test_seed.py`. The upstream kg-microbe GTDB mapping that supplies the raw closeMatch also needs a direction- and rank-aware review. Mapping, synonym and xref manifestations are counted as one scope-inflation finding.

Blockers: None found. Minor findings: None found. The exact NCBI strain identity is supported. The assembly warning and parent placement are preserved as qualifications, not silently resolved or counted as unrelated YAML defects.

## Recommended Edits

1. Make GTDB identity promotion in `src/taxonmech/seed.py` rank-aware. Do not turn a species-cluster mapping into an exact synonym or equivalent xref on a strain taxon. Retain the supported genome classification with source/release context and the upstream cluster count.
2. Have the upstream kg-microbe mapping owner assess the directed relationship and pooling semantics. Do not mechanically swap broad/narrow predicates. Preserve the exact GTDB cluster suffix `mitis_N` in source-facing explanations; `mitis N` is a generated display transformation, not an independently established strain alias.
3. Add a strain-versus-species regression case in `tests/test_seed.py` while preserving supported species-level mappings. After an authorized fix, regenerate through the maintained extraction/seeding pipeline rather than hand-editing this YAML or raw inventories.
4. Keep CCUG 62643 and its existing source assertions on the parent record under the current classification contract. If a later task adds navigation from strain taxa to parent-filed deposits, implement it in the maintained model/seeder/rendering logic with explicit evidence; do not copy every parent strain downward.
5. For later direct NCBI enrichment, pin the BioSample source-material assertion before extending `src/taxonmech/ncbi_assemblies.py` and its configured inputs. The current importer uses assembly-summary strain tags, here only SK569. Preserve GenBank's organism warning, the suppressed RefSeq status, and GOLD's supplied unversioned accession.

## Follow-up Checks

- After the rank-aware change, run `uv run pytest tests/test_seed.py`, then this target's documented schema and strict commands.
- Confirm removal of the unsupported GTDB exact synonym/equivalent xref while retaining the NCBI ID, lineage, two NCBI aliases, source attestations and the source-scoped cluster membership/count.
- Run the real full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc` gates after regeneration. No manual source comparison in this report replaces those checks.
- Resolve the live GTDB taxon page and record its release before any taxonomic update; the browser could not retrieve it during this review. Pinned native metadata support the finding without assuming the latest classification.
- If adding direct assembly links, distinguish current GCA_000222785.2 from suppressed GCA_000222785.1 and GCF_000222785.1, carry the source-organism warning, and test explicit CCUG evidence without enabling bare-name joins.
- Recheck ATB availability before any later ATB addition. Keep sample/project/GOLD and StrainInfo context separate from genome identifiers and counts.

## Additional Notes

The ignored-independent searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial taxid, designation/separator and slug searches produced 33 candidate rows. Expansion with the observed deposit, assembly, sample, WGS, GOLD, project, IMG and BacDive identifiers produced 25 rows, nine new. All 42 distinct rows were read in full with lossless structured decoding, and incidental numeric matches were rejected. Five SOURCE.json files were searched structurally; history filenames were checked separately. Absence statements are confined to these named roots and inspected authority responses.

The StrainInfo version DOI and BacDive DOI 10.13145/bacdive156544.20260601.11 both resolved by HTTP HEAD to authority pages with status 200. The BacDive PDF itself was not downloaded or visually inspected. The primary StrainInfo API record was read in full. PMC returned a browser challenge, so the publisher's accessible article text was used; no access-control bypass was attempted. The GTDB live page remained unavailable.

No source/YAML/generated-page edits, history events, review-status promotions, paid research, outbound contacts or Git/GitHub mutations were performed. Eukaryota reviews were not reopened.
