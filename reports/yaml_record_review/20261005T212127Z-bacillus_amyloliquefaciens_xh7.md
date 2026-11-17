# YAML Record Review: Bacillus amyloliquefaciens XH7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_amyloliquefaciens_xh7.yaml`
- Started UTC: 2026-10-05T21:16:30Z
- Finished UTC: 2026-10-05T21:21:27Z
- Verdict: needs curation

## Target

This review covers the complete 90-line generated `TaxonRecord` for `NCBITaxon:1034836`, Bacillus amyloliquefaciens XH7, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:1390`. Its grounding is `EXACT` and lifecycle is `SEEDED`. It has one GTDB mapping, three synonyms, one GTDB xref, three source attestations, genetic code 11, zero listed BacDive strains, and one seed event.

The identity is pinned by `data/taxa/PATHS.tsv:14165`; scope is `curation/seed_scope.tsv:36164`. This report does not review similarly named Acinetobacter, Shewanella or Xanthomonas records. The YAML, scope, source inventories, history and generated products were not edited. Eukaryota was left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacillus_amyloliquefaciens_xh7.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacillus_amyloliquefaciens_xh7.yaml --out /private/tmp/bxh7-strict-20261005.tsv`, exit 0, one file, zero errors. The output TSV was read and contains only its header.
- PASS: header-aware inventory comparison checked the identity, genetic code, all 12 lineage entries, PATHS identity, scope reason, NCBI attestation and seed-event text. All seven taxon-source inventories were examined for exact target associations.
- PASS: exact identifier checks of `ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows. A backbone scan found no children of this taxon.
- PASS: a structured scan of all compressed GTDB genome catalog shards counted 94 distinct accessions in the exact species cluster, including one with NCBI taxon 1034836. The target and representative objects were inspected in full.
- Term/reference checks: the live NCBI Taxonomy EFetch and Datasets responses, both paired assembly reports, all four exact-taxonomy Nuccore results, the parent LPSN page, and the genome paper's PubMed metadata and abstract were inspected. These are bounded source checks, not a substitute for repository-wide validation.
- Not applicable: curator-added causal-graph term checks and iModulonDB searches. The target asserts no gene, locus, regulator, expression module or causal edge.
- Not run: `just verify-corpus`, `just qc`, the full test suite, full-corpus strict validation, `just provenance-check`, `just validate-history`, rendered-site drift, README statistics, publication-size and vendored-sync gates. This read-only single-record review does not claim full-corpus reproducibility, verified snapshot hashes or publication readiness.
- No separate target history report was found by the ignored-inclusive identifier/name search in `history/`. The embedded seed event was checked; no event or lifecycle promotion was written.

## Identity and Grounding

The [NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034836&retmode=xml) resolves 1034836 to this exact strain, with parent 1390, rank strain, bacterial division, genetic code 11, and the two equivalent names carried by the YAML. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034836) independently confirms its ID, name, rank and complete ancestor-ID chain.

The pinned chain is root 1, cellular organisms 131567, Bacteria 2, Bacillati 1783272, Bacillota 1239, Bacilli 91061, Caryophanales 1385, Bacillaceae 186817, Bacillus 1386, Bacillus subtilis group 653685, Bacillus amyloliquefaciens group 1938374, and Bacillus amyloliquefaciens 1390. The labels and ranks agree with the backbone and live authority. Root is present in Datasets and the pinned chain although Taxonomy EFetch omits it from its displayed lineage.

The two NCBI synonyms are supported equivalent names, not misfiled related synonyms. Their native rows are `data/catalog/ncbi_names-0005.jsonl.gz:31096` and `:31097`; the scientific-name row is `:31098`.

The [LPSN parent-species page](https://lpsn.dsmz.de/species/bacillus-amyloliquefaciens) identifies name 773632 as the validly published, correct species name and lists DSM 7 / ATCC 23350 among its type-strain deposits. That is parent-species context, not an XH7 deposit assertion. The full inventory row, `data/raw/lpsn_names.tsv:15533`, maps to NCBI 1390, not 1034836. No parent nomenclature or type strain should be copied onto XH7.

The sole identity defect is the GTDB species-level equivalence represented on this strain record, detailed in F1. It does not invalidate the independently supported NCBI grounding.

## Evidence

| Claim or source | Inspected support and limits |
|---|---|
| NCBI identity and NAME count 1 | `data/raw/ncbitaxon_taxa.tsv:221695` matches all identity fields, equivalent names and snapshot date 2026-09-13; live NCBI confirms them. NAME is an attestation unit, not a claim that there is only one alternate name. |
| GTDB mapping and GENOME count 94 | `data/raw/gtdb_mappings.tsv:1401` supplies the closeMatch and count; `data/raw/gtdb_species.tsv:16163` supplies the same species count. Native exact-cluster counting confirms 94, but not an equivalence between that species and XH7. |
| MADIN TRAIT_ASSERTION count 4 | `data/raw/madin_taxa.tsv:655` supplies exactly four. The original configured Madin edge file was unavailable, so individual traits were not verified or inferred. |
| Seed event | `curation/seed_scope.tsv:36164` supplies the stated three-source scope reason and 2026-09-12 inclusion date. The event's 2026-09-13T17:54:04Z timestamp matches the newest of the raw, ATB and StrainInfo manifests, as selected by `src/taxonmech/seed.py:139`. |

The exact GTDB cluster has 82 genomes labeled with NCBI species 1390, one with target strain 1034836, and 11 with other NCBI IDs. The full target object at `data/catalog/gtdb_genomes-0011.jsonl.gz:46764` is `RS_GCF_000221645.1`, nonrepresentative, with strain identifier XH7, no type-material designation, GenBank `GCA_000221645.1`, and BioSample `SAMN02603869`. The full representative object at `gtdb_genomes-0013.jsonl.gz:37801` is `RS_GCF_000196735.1`, DSM 7, NCBI 692420, with a type-material designation. Membership is supported; identity with the whole cluster is not. The 94 members were parsed for counting and classification, not all individually reviewed.

Native genome and related-record evidence was also checked:

- `data/catalog/ncbi_genbank-0000.jsonl.gz:3825` and `ncbi_refseq-0000.jsonl.gz:3294` describe current `GCA_000221645.1` / `GCF_000221645.1`, an explicitly identical pair, for taxon 1034836 and strain XH7. Both describe one complete chromosome of 3,939,203 bases. Full live [GenBank](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000221645.1/dataset_report) and [RefSeq](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000221645.1/dataset_report) reports confirm the pair and identity.
- The live embedded BioSample `SAMN02603869` contains strain XH7 but no culture-collection attribute. Native GenBank carries `PRJNA67079`, whereas native RefSeq and GTDB carry `PRJNA224116`; live Datasets reports the strain sequencing project `PRJNA67079`. These source-specific project assertions must remain distinct.
- `data/bvbrc/bvbrc-0000.jsonl.gz:3287` is genome `1034836.4`, carrying the same GenBank assembly, BioSample, project `PRJNA67079`, `CP002927` and `NC_017191.1`. Its bare XH7 designation is not a registered culture-deposit identifier.
- The complete GOLD chain is organism `Go0012486` at `data/gold/organisms.jsonl.gz:10995`, project `Gp0012486` at `projects.jsonl.gz:10859`, and isolate analysis `Ga0009445` at `analyses.jsonl.gz:4226`. The project explicitly names the organism and the analysis names that project, linking `GCA_000221645.1`, `CP002927` and IMG `2511231180`. The organism's culture-collection field is empty. The analysis's own organism field is empty, but its project chain resolves; none of the Go/Gp/Ga IDs is itself a genome ID.
- Exact NCBI searches returned one Assembly UID and four Nuccore UIDs. Full metadata, references, comments and source features were inspected for all four, excluding bases and non-source feature details. [CP002927.1](https://www.ncbi.nlm.nih.gov/nuccore/CP002927.1) and [NC_017191.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_017191.1) are the chromosome records; RefSeq explicitly states sequence identity with CP002927.1. `HG781812.1` and `HG519951.1` are 363-base tmRNA transcript/gene records derived from CP002927.1, not additional genome assemblies or culture deposits.
- Yang et al. 2011, Journal of Bacteriology 193:5593-5594, [PMID 21914895](https://pubmed.ncbi.nlm.nih.gov/21914895/), is the XH7 genome report. The inspected PubMed metadata and chromosome references agree on DOI `10.1128/JB.05880-11` and PMC3187415. Only bibliographic identity and the abstract were verified; no mechanism or phenotype claim is added to the taxon record.

Older native GTDB/BV-BRC hierarchy text uses Bacillales while the current NCBI backbone uses Caryophanales. This review preserves source hierarchies and does not replace the record's correctly carried NCBI lineage.

## Completeness

The existing `strain_count: 0` is a BacDive-record count, not a claim that XH7 has no genome. Exact target inventory checks found no BacDive, LPSN, GOLD KGX, MediaDive or BactoTraits taxon rows. The source-supported genome leads above merit future enrichment consideration, but this review found no eligible deposit-based strain entry that the current seeder demonstrably dropped. GOLD's native organism record is separate from its taxon-level KGX attestation inventory.

Ignored files were included throughout the bounded absence searches:

- `rg --no-ignore --hidden -n -z -i` searched `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, with `SOURCE.json` manifest files excluded. The completed whole-token XH7 / taxon-ID search produced 33 candidate rows, all inspected as full JSON objects or header-aware TSV rows.
- A completed follow-up search for assembly 000221645, CP002927, NC_017191, SAMN02603869 and the specific GOLD/IMG IDs produced eight rows. Seven repeated inspected target evidence; the eighth was an unrelated Salmonella assembly named PDT000221645.2. No target-specific BacDive, StrainInfo or ATB association was found within these searches.
- The matching-name candidates included Acinetobacter sp. XH7 (588227), Shewanella sp. XH7 (1540893) and Xanthomonas arboricola pv. corylina XH7 (487821), including current and historical Xanthomonas assemblies. These were rejected as distinct identities, not added as synonyms or genome links.
- Numeric false matches were also rejected: ATB row `data/catalog/allthebacteria.tsv.xz:65843` has sample SAMEA1034836 for Streptococcus dysgalactiae subsp. equisimilis; row `:569306` has run ERR1034836 for Mycobacterium tuberculosis. The BV-BRC ERR1034836 match is likewise not this taxon.
- The parent YAML `data/taxa/bacteria/bacillus_amyloliquefaciens.yaml` was searched for the target ID, bounded designation and verified genome/sample/GOLD identifiers; no matches were found. This is not a claim about unsearched repositories or later source releases.
- The configured kg-microbe checkout was searched with `rg --files --no-ignore --hidden -g '*madin*'`, and the configured `data/transformed/madin_etal/edges.tsv` path was tested directly. Both checks found no file. The four original trait assertions therefore remain unverified beyond the committed count.

The initial broad XH7 substring search also matched longer designations; those leads were not treated as target evidence. The final bounded search and accession follow-up above define the reviewed candidate set.

No definition, literature evidence list, causal graph, discussion, dataset or curator-authored phenotype is required merely because those slots are optional. No type-strain deposit should be borrowed from DSM 7. The runtime culture matcher returns an empty key for XH7, consistent with its registered-authority/full-accession rule; weakening that rule would create false joins.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**F1 - Major: a GTDB species membership mapping is promoted to exact strain identity.**

YAML lines 45-55, 62-63 and 73-78 attach the entire GTDB species by closeMatch, make the bare species name an `EXACT_SYNONYM`, and expose an equivalent-identifier xref on XH7. The schema reserves xrefs for true equivalences. The verified species cluster contains 94 genomes with multiple NCBI IDs and a different representative/type strain; only one member carries 1034836. Thus the count is valid at species-cluster scope, while species-to-XH7 equivalence is not.

The maintained upstream owner is kg-microbe's GTDB mapping transform feeding `data/transformed/gtdb/edges.tsv`; `src/taxonmech/extract.py:501` imports its relationship. The local promotion is owned by `src/taxonmech/seed.py:451`, where a closeMatch triggers identity without a rank guard, and lines 466-469 emit the xref and exact synonym. This is one causal defect across several generated fields, not separate findings. No upstream transform source file was located by the bounded ignored-inclusive GTDB filename search in the configured checkout, so its implementation was not claimed inspected.

The NCBI record still denotes the correct strain, so this is major rather than an identity blocker. The fix belongs in maintained transformation/seeding logic with tests, not in this generated YAML.

## Recommended Edits

1. Correct the upstream species-versus-strain mapping semantics and make local GTDB identity promotion rank-aware in `src/taxonmech/seed.py`. Preserve the supported genome's species membership and source provenance without representing the whole species as an equivalent XH7 identifier or exact synonym. Review the corresponding attestation relationship as part of the same change.
2. Add a regression in `tests/test_seed.py` using a strain-rank NCBI target and species-level GTDB input, preserving supported species-level mappings on the parent. Ensure membership does not become an exact synonym/xref. Preserve the valid cluster count of 94; do not change it to one to disguise the scope defect.
3. Any future deposit-independent genome enrichment needs an explicit maintained model/transform design. Retain the verified assemblies, BioSample and GOLD chain as leads; do not mint a BacDive strain, join other XH7 names, infer a deposit, conflate projects with genomes, or transfer DSM 7's type designation.

## Follow-up Checks

- After an authorized upstream/seed fix, run focused seeder tests, the documented seed dry run and `just seed-canary NCBITaxon:1034836`; inspect the emitted record, not only the exit code.
- Re-run schema and strict validation on the canary. Manually verify that the bare species exact synonym and equivalence xref are gone or correctly scoped, while the NCBI identity, lineage, equivalent names and source-supported species-cluster count remain intact.
- Before publishing an authorized regenerated corpus, run `just verify-corpus` and `just qc`, including their history, provenance and publication gates.
- When the original Madin input is available, trace its four exact-taxonomy assertions without inferring traits from the count.
- If genome enrichment is undertaken, require source-explicit strain evidence and preserve accession versions, source-specific project assertions, the GOLD chain, and marker sequences outside genome counts. Recheck exact BioSample-based ATB eligibility rather than matching the numeric taxon string.

## Additional Notes

GTDB species/genome web pages and the GOLD analysis web page were inaccessible through the browser tool; the findings use the fully inspected native catalog objects, not a claimed live web census. The PMC article page returned a browser-check challenge and the DOI resolver was inaccessible; neither was bypassed. The inspected PubMed abstract and NCBI metadata support only the bounded identity statements above.

This was an independent read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on the existing dedicated review branch. No curation event, human sign-off, GitHub mutation, paid research, source refresh or corpus regeneration was performed. Only this new timestamped report was added.
