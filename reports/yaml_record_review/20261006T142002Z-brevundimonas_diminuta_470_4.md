# YAML Record Review: Brevundimonas diminuta 470-4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/brevundimonas_diminuta_470_4.yaml`
- Started UTC: 2026-10-06T14:13:56Z
- Finished UTC: 2026-10-06T14:20:02Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1035191`, label `Brevundimonas diminuta 470-4`, rank STRAIN, domain BACTERIA. The entire YAML was read before findings and checked byte-for-byte unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED with one GTDB mapping, three synonyms, one equivalent xref, genetic code 11, zero listed strains, three source attestations and one inline seed event. It contains no definition, nomenclature entry, nested genome link, publication citation or causal graph. Only this new report is written.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/brevundimonas_diminuta_470_4.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/brevundimonas_diminuta_470_4.yaml --out /private/tmp/bd4704-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: pinned identity, both NCBI aliases, all ten root-first lineage entries, genetic code, source counts, scope and seed provenance agree. These comparisons are not a focused corpus-reproduction validator.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- There are no curator-added ontology graph nodes to validate. The documented product checker excludes taxonomy fields and delegates those to corpus reproduction.
- No separate target history artifact was found by the ignored-independent history filename search. Inline history passed schema validation and agrees with scope provenance. No external history validator was run against an invented artifact.
- There are no DOI, PMID, quoted-evidence or definition references in this YAML. No additional record-specific citation validator is documented in the inspected commands.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221915` and inspected live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035191&retmode=xml) agree on label, strain rank, parent `NCBITaxon:293`, both equivalent names and genetic code 11. The [taxonomy dataset response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035191) supplies the same root-inclusive ancestor IDs and rank STRAIN.

All ten pinned ancestors match the YAML, including Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Caulobacterales, Caulobacteraceae, Brevundimonas and B. diminuta. Live XML supplies matching non-root labels/ranks. There are no children in the pinned backbone and no exact target entries in the type-material, merged-ID or dropped tables.

The [LPSN species page](https://lpsn.dsmz.de/species/brevundimonas-diminuta), record 774245, concerns the parent species, a validly published correct name. Its type deposits include ATCC 11568 and DSM 7234, not ATCC 13184. The raw name at `data/raw/lpsn_names.tsv:15913` maps to parent 293 and the unsuffixed GTDB species. Parent nomenclature and type designations must not be copied onto this non-type strain.

[ATCC 13184](https://www.atcc.org/products/13184) explicitly identifies designation 470-4, equivalent deposits CCUG 2031 and LMG 9561, non-type status and buccal-cavity origin. [BacDive 141457](https://bacdive.dsmz.de/strain/141457) connects these deposits with JCM 13047 and BCRC 14891 but files its taxonomic classification under species 293. This is compatible strain-identity evidence with differently scoped taxonomic placement, not a reason to replace the carried NCBI lineage.

## Evidence

- NCBI: full native name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31370`, `31371` and `31372` support the label and both NCBI synonyms. Its attestation is one NAME.
- GTDB: `data/catalog/gtdb_genomes-0015.jsonl.gz:23267` identifies GB_GCA_000318405.1 as the representative of `s__Brevundimonas diminuta_B`, with strain 470-4, taxid 1035191, PRJNA67195 and SAMN02436690. A representative genome anchors a cluster; it is not identical to the species concept.
- GTDB count: `data/raw/gtdb_species.tsv:20234` and `data/raw/gtdb_mappings.tsv:1419` carry 35 cluster genomes. Exact mapping rows at lines 70615, 113611, 235405 and 297995 also associate this cluster with taxa 1871086, 1977087, 293 and 588932, respectively, as broadMatch. The count is repeated cluster context, not 35 genomes of strain 470-4. Its extraction owner is `src/taxonmech/extract.py:501`.
- MADIN: `data/raw/madin_taxa.tsv:668` supports three TRAIT_ASSERTIONs. This aggregate count does not establish any particular phenotype or mechanism.
- Scope: `data/taxa/PATHS.tsv:14406` and `curation/seed_scope.tsv:36171` resolve the exact record. Its three-source scope reason agrees with the seed event of 2026-09-13T17:54:04Z; scope was added on 2026-09-12.

The following genome and deposit evidence was inspected for completeness:

- Native GenBank `data/catalog/ncbi_genbank-0000.jsonl.gz:8031` identifies current GCA_000318405.1, 168 contigs, 80 scaffolds and 3,337,682 bp. Historical RefSeq `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:2427` records suppressed GCF_000318405.1 and its 2021-02-24 withdrawal. Both rows flag contamination.
- The [live NCBI assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000318405.1/dataset_report) confirms current GenBank and suppressed RefSeq status, the contamination warning, and an explicit statement that ATCC 13184 supplied the strain. Its ANI taxonomy check is Inconclusive / below_threshold_mismatch, reporting 90.43% against the B. diminuta type assembly and 94.01% against a B. naejangsanensis type assembly. These source-qualified comparisons do not authorize a local taxonomic reassignment.
- The complete [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN02436690&retmode=xml) independently gives strain 470-4, culture collection ATCC:13184, human host and oral-cavity isolation source. Those are sample-level metadata, not evidence of a clinical phenotype.
- Native BV-BRC `data/bvbrc/bvbrc-0000.jsonl.gz:3314` gives PATRIC 1035191.3, the same assembly/project/sample and bare designation 470-4. Its culture-collection field is blank; the explicit deposit support instead comes from GOLD, NCBI and ATCC.
- GOLD's inspected chain is `Go0004434 -> Gp0004434 -> Ga0015024`, at `data/gold/organisms.jsonl.gz:3929`, `data/gold/projects.jsonl.gz:3955` and `data/gold/analyses.jsonl.gz:8605`. It connects explicit ATCC 13184 to GCA_000318405.1, IMG 2531839707, PRJNA67195 and SAMN02436690. The corresponding joined rows are already in `data/raw/strain_assemblies.tsv:49377`, `data/raw/strain_genome_records.tsv:38614` and `data/raw/strain_related_records.tsv:141805` through line 141817. These are different record identifiers and provenance assertions, not independent biological genomes.
- Native BacDive at `data/bacdive/records.jsonl.gz:63740` and transformed `data/raw/bacdive_strains.tsv:63741` resolve `kgmicrobe.strain:bacdive_141457`, with five normalized deposits and species-level classification 293. The native record explicitly says it is not a type strain.
- Native StrainInfo at `data/straininfo/records.jsonl.gz:4032` resolves SI-ID 4032, source DOI 10.60712/SI-ID4032.2, and six deposits including CCRC 14891. Its sequence assertion LC507944 explicitly belongs to JCM 13047 / SI-DP 699766. The local links at `data/straininfo/strain_links.tsv:28674` through line 28678 retain the five deposits recognized in the BacDive crosswalk; `data/straininfo/related_records.tsv.gz:68895` through line 68905 preserve the sequence and deposit provenance.
- Complete [NCBI nucleotide metadata for LC507944](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=LC507944&rettype=gb&retmode=xml) confirms LC507944.1, JCM:13047, taxid 293 and a 1,385-base partial 16S rRNA sequence. This is not an assembly or proof of whole-genome equivalence.

## Completeness

The direct BacDive, LPSN, transformed GOLD, MediaDive and BactoTraits taxon inventories have no exact target row. This must not be confused with absent native evidence: the GOLD chain and BacDive deposit above are present, and the fully inspected BacDive-141457 block in `data/taxa/bacteria/brevundimonas_diminuta.yaml` already carries its GOLD assembly, IMG record, project/sample links and StrainInfo sequence/deposits. That parent block was contextual evidence only, not a second record-level review.

With no BacDive entry at target 1035191 and no descendants, `strain_count: 0` follows the target-plus-descendants rule in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`. It does not mean this strain lacks deposits or a genome. The seeder gathers by BacDive's taxonomic placement, then joins genome records by strain identity. It does not inherit every parent strain into each child. A future explicit, source-preserving identity bridge could improve discoverability, but the present omission is consistent with the documented rule and is not counted as a separate defect.

The ignored-independent searches found no exact SAMN02436690 ATB row. The two initial ATB matches were unrelated Mycobacterium tuberculosis and Salmonella rows whose run identifier or sequence checksum contains the target's digits. Neither is an eligible link. No genome-wide identity was inferred from shared deposits, taxon labels or sequence fragments.

Before open-ended follow-up, `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` completed successfully. None of its 28 datasets covers Brevundimonas. iModulonDB is not applicable, not negative biological evidence. Empty optional definition, phenotype and causal-graph slots do not require invented content.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species cluster is promoted to exact strain identity.** `GTDB:s__Brevundimonas_diminuta_B` becomes an equivalent xref and EXACT_SYNONYM `Brevundimonas diminuta B` for strain taxid 1035191. The native source establishes representative-genome membership of a 35-genome cluster, not equality between a strain and a species concept. This violates the true-equivalence boundary in `src/taxonmech/schema/taxonmech.yaml:180`. The maintained local owner is rank-insensitive GTDB identity promotion in `src/taxonmech/seed.py:449`, with regression coverage in `tests/test_seed.py`. The upstream kg-microbe closeMatch producer also needs rank- and direction-aware review. The xref, synonym and mapping manifestations count as one finding.

Blockers: None found. Minor findings: None found. NCBI identity remains supported. Genome-quality warnings and the inconclusive ANI classification are explicit qualifications on prospective enrichment, not additional unsupported assertions already present in this YAML.

## Recommended Edits

1. Make GTDB identity promotion in `src/taxonmech/seed.py` rank-aware. Preserve supported source-classification context and the cluster count, but do not generate a species-cluster equivalent xref or exact synonym on a strain record.
2. Have the upstream kg-microbe mapping owner assess rank and relationship direction rather than mechanically substituting a guessed broad/narrow predicate. Preserve the source suffix diminuta_B and the distinction between cluster representative and strain identity.
3. Add a strain-versus-species regression case in `tests/test_seed.py`, including this representative-genome case and supported species-level equivalences. Regenerate only through maintained extraction/seeding inputs after an authorized fix; do not hand-edit YAML or raw inventories.
4. If later adding explicit child-record deposit discovery, design that behavior in the maintained seeder and document it in `docs/HARMONIZATION.md`. Use the exact ATCC/BacDive/GOLD/BioSample evidence, preserve BacDive's classification under 293, and do not indiscriminately inherit parent strains. The existing parent links should remain available.
5. Any later genome enrichment must retain current versus suppressed status and the contamination warning, keep the GOLD chain and source identifiers distinct, and retain LC507944 as a deposit-specific partial rRNA sequence. Do not silently reconcile NCBI, GTDB and ANI classifications.

## Follow-up Checks

- After a rank-aware change, run `uv run pytest tests/test_seed.py`, then this target's documented schema and strict commands.
- Confirm removal of the unsupported GTDB exact synonym/equivalent xref while retaining the NCBI ID, ten ancestors, two NCBI aliases, genetic code, three source attestations and source-scoped cluster membership/count.
- Run the actual full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc` gates after regeneration. Manual source comparisons do not replace them.
- Retry the live GTDB species/genome page and record its release before a taxonomy update. Those endpoints were unavailable during this review; the pinned native representative row and species inventory support the bounded finding.
- Before adding any deposit bridge, test that only the explicitly matched strain is exposed on this child, that original classification/provenance remain intact, and that other parent strains are not inherited.
- Recheck assembly status and contamination warnings before enrichment. Keep the RefSeq suppression, inconclusive ANI result and deposit-specific sequence scope visible; none licenses a phenotype claim or taxonomic rewrite.

## Additional Notes

Ignored-independent candidate searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial taxid, designation/separator and slug search produced 34 rows. An accession/deposit expansion was tightened with identifier boundaries after a broad SI-ID prefix matched unrelated numbers; the bounded expansion produced 52 rows, 37 new. All 71 distinct bounded candidate rows were read in full using lossless structured decoding, including compressed inputs. Numeric, accession-substring and longer-designation collisions were rejected. No claim of full inspection is made for the discarded broad-prefix result set.

Separate structured scans read the exact GTDB species/mapping rows and parent LPSN row. Five SOURCE.json files were searched structurally, and history filenames checked separately. Absence statements are bounded to these roots and authority responses, including ignored and compressed files.

The live GTDB species tree, genome and search URLs returned tool-access errors. NCBI, ATCC, BacDive and LPSN responses succeeded. No paid research, access-control bypass, outbound contact, source/YAML/generated-page edits, history events, review-status promotions or Git/GitHub mutations were performed. Eukaryota reviews were not reopened.
