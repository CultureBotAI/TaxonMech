# YAML Record Review: Mycoplasmopsis anatis 1340

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mycoplasmopsis_anatis_1340.yaml`
- Started UTC: 2026-10-05T20:56:39Z
- Finished UTC: 2026-10-05T21:03:30Z
- Verdict: needs curation

## Target

The complete 87-line generated `TaxonRecord` was read before judgment. It denotes `NCBITaxon:1034808`, Mycoplasmopsis anatis 1340, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:171279`, grounding `EXACT`, and lifecycle `SEEDED`. It carries nine ancestors, genetic code 4, one GTDB mapping, five exact synonyms, a GTDB xref, zero classified BacDive strains, and three source attestations.

The target resolves uniquely at `data/taxa/PATHS.tsv:14162`, `curation/seed_scope.tsv:36162`, and `curation/legacy_page_paths.tsv:844`. The parent species and its BacDive entries were consulted as placement context, not treated as additional completed record reviews.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/mycoplasmopsis_anatis_1340.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/mycoplasmopsis_anatis_1340.yaml --out /private/tmp/ma1340-strict-20261005.tsv`: exit 0, one file, zero errors; the TSV was read and contains only its header.
- Read-only structured source comparisons checked the target backbone, complete ancestor chain, children, seven source inventories, pinned path, scope reason, NCBI snapshot attestation, and seed-event wording. They agree with the generated record. This is not a substitute for full corpus reproduction or biological review.
- Public NCBI Taxonomy EFetch/Datasets and Assembly Datasets/ESummary were read. Nuccore summary metadata was screened for all 103 exact-taxid results; sequence bases and individual gene annotations were not audited.
- `normalize_culture_identifier` was exercised read-only: ATCC 25524 and ATCC:25524 produce `ATCC-25524`; NCTC 10156 produces `NCTC-10156`; bare 1340 and separator-free NCTC10156 produce no join key.
- `just validate-products` is not applicable because the record has no curator-added causal graph. Source references were inspected directly; no undocumented single-record reference validator was substituted.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, generated-site drift, documentation statistics, publication-size budget, and vendored synchronization.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221692` and live [NCBI taxonomy 1034808](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034808) agree on identity, strain rank, species parent, bacterial placement, and genetic code 4. The complete root-first chain is:

`1 > 131567 > 2 > 1783272 > 544448 > 2790996 > 2895623 > 2767358 > 171279`.

All ancestor labels and ranks match the pinned backbone; live Datasets returns the same IDs. The absence of a Mollicutes class entry reflects NCBI's supplied chain, not a reason to insert another source's hierarchy. No children, retired status, exact-target merged-ID entry, or exact-target type-material row was found in the inspected inventories.

The four NCBI-derived synonyms retain the strain/deposit qualifier and agree with the live source and `data/catalog/ncbi_names-0005.jsonl.gz:31088` through line 31091: two synonym-class names and two equivalent-name-class names. The fifth, GTDB-derived bare species name does not denote the same taxonomic scope; see F1.

[ATCC 25524](https://www.atcc.org/products/25524) explicitly identifies its designation as 1340 / Weybridge and marks it as a type strain. [LPSN 798557](https://lpsn.dsmz.de/species/mycoplasmopsis-anatis) supplies the correct species name and the type deposits ATCC 25524, IFO 14861, NBRC 14861, and NCTC 10156. NCBI's parent-species type-material rows at `data/raw/ncbi_type_material.tsv:54256` through line 54265 additionally include strain 1340. Type material belongs to a species but is not equivalent to that species as a taxonomic concept.

The LPSN inventory maps the correct name to species 171279, not this strain; the old combination is retained separately at `data/raw/lpsn_names.tsv:22374`, with the correct-name row at line 33657. The lack of an LPSN nomenclature block on this strain is appropriate.

## Evidence

The GTDB species inventory at `data/raw/gtdb_species.tsv:123730` counts 18 genomes. Both `data/raw/gtdb_mappings.tsv:1399` and line 50113 map that same species, respectively to this strain and its species parent, using closeMatch. All 18 corresponding native GTDB genome objects were read in full. They include:

| Native GTDB genome | Strain metadata | Native row in `data/catalog/` |
|---|---|---|
| `RS_GCF_000221305.1` | 1340; exact NCBI strain taxon 1034808 | `gtdb_genomes-0017.jsonl.gz:6764` |
| `RS_GCF_900660655.1` | NCTC10156; species taxon 171279; GTDB representative | `gtdb_genomes-0009.jsonl.gz:21466` |
| `RS_GCF_003285065.1` | NCTC 10156; species taxon 171279 | `gtdb_genomes-0002.jsonl.gz:29329` |
| `RS_GCF_019279375.1` | DP07; species taxon 171279 | `gtdb_genomes-0017.jsonl.gz:25357` |
| `RS_GCF_052039995.1` | LC01; species taxon 171279 | `gtdb_genomes-0005.jsonl.gz:27370` |

The other thirteen objects name F6-2, LH07, LH08, DP15, DP06, MA220, DP05, LH04, DP10, DP09, DP12, LH05, and F6-5. These are species-cluster members, not eighteen independently supported genomes of strain 1340. The numeric count is correct at cluster scope; the identity mapping is the problem.

[BacDive 169044](https://bacdive.dsmz.de/strain/169044), its full native object at `data/bacdive/records.jsonl.gz:91276`, and `data/raw/bacdive_strains.tsv:91277` retain the four type deposits but classify the culture at species 171279. Native BacDive records 159511 and 159512 instead describe K6193A and K6193C. They cannot be transferred to 1340 merely because they share the parent species.

The strain-to-genome relationship is already represented on the parent record at `data/taxa/bacteria/mycoplasmopsis_anatis.yaml:83`. Its BacDive 169044 entry contains an unversioned `ncbi.assembly:GCA_000221305` assertion from GOLD and `img.taxon:2512047064`, with an explicit ATCC 25524 match. The full native chain is:

`Go0011533 > Gp0011533 > Ga0009333`.

Its organism, project, and analysis objects were read at `data/gold/organisms.jsonl.gz:10131`, `projects.jsonl.gz:9985`, and `analyses.jsonl.gz:4116`. The assembly and IMG links are retained in `data/raw/strain_assemblies.tsv:90171` and `data/raw/strain_genome_records.tsv:72263`. BioSample SAMN02469901, BioProject PRJNA67125, and the GOLD IDs remain typed related records on the parent entry, not genome counts.

Live [NCBI GCA_000221305.2](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000221305.2/) explicitly pairs the current GenBank assembly with GCF_000221305.1: strain 1340, taxon 1034808, 44 contigs, 928,687 bases, type material. The returned BioSample includes culture_collection ATCC:25524. These agree with full native current rows `data/catalog/ncbi_genbank-0000.jsonl.gz:3808` and `ncbi_refseq-0000.jsonl.gz:3278`. The older GCA_000221305.1 row at `ncbi_genbank_historical-0000.jsonl.gz:1137` is suppressed. The two exact-taxid Assembly search hits represent this current paired record and the historical version, not two independent strains.

BV-BRC's native `1034808.3` row at `data/bvbrc/bvbrc-0000.jsonl.gz:3285` names GCA_000221305.2, the same sample/project, and the bare designation 1340. It is a retained candidate, not an eligible culture-deposit join under the current matching rule. NCTC assemblies GCA_003285065.1 and GCA_900660655.1 have distinct samples and source chains and must not be collapsed into the 2011 assembly.

NCBI PubMed metadata and abstracts verify the 1340 genome announcement, [PMID 21952548 / DOI 10.1128/JB.05891-11](https://pubmed.ncbi.nlm.nih.gov/21952548/), and the later NCTC type-strain announcement, [PMID 30533671 / DOI 10.1128/MRA.00939-18](https://pubmed.ncbi.nlm.nih.gov/30533671/). Full articles were unavailable through the attempted publisher and PMC pages; no claim here depends on unread full-text methods or results.

Madin's one TRAIT_ASSERTION matches `data/raw/madin_taxa.tsv:653`. The original configured Madin edge input was unavailable, so that individual trait was not independently recounted or interpreted as a phenotype. NCBI's one NAME assertion and snapshot note match the backbone.

## Completeness

Ignored-inclusive, hidden-inclusive compressed searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding per-file `SOURCE.json` manifests. Queries covered the exact taxid, both genus spellings, the four deposits, BacDive/SI identifiers, relevant assembly accessions, and the original GOLD chain. They yielded 282 distinct candidate lines; source chains used above were read as full native objects or header-aware TSV rows. This was not a separate review of every other species-level genome candidate.

The zero BacDive strain count is correct for the present classification inputs and the own-taxon-plus-descendants rule in `src/taxonmech/seed.py:483`. The parent record's existing sourced genome relationship prevents a claim that the repository has no genome link for 1340. No second major finding is asserted merely because the child record does not inherit an ancestor's strains.

StrainInfo's full native SI-ID 38579 record at `data/straininfo/records.jsonl.gz:26954` retains 1340/Weybridge, the four deposits, and version DOI 10.60712/SI-ID38579.3. Its two genome assertions explicitly belong to NCTC deposit 341589 and appear at `data/straininfo/assemblies.tsv:6341` and line 6342. ATCC deposit 104288 instead supplies marker/gene sequences; grouping the deposits does not transfer genome assertions between them.

The inspected ATB native row at `data/catalog/allthebacteria.tsv.xz:1431377` and committed row `data/atb/assemblies.tsv:6123` concern SAMN09469955, the NCTC assembly context. Its available FASTA and PASS assembly filter permit the link despite non-HQ warnings. The source-specific sample chains and five shares_biosample crosslinks were read, and the local ATB record is already present on the parent strain entry. It does not assert sequence identity with the 1340 assembly. Numeric collisions involving SAMEA1034808, ERR1034808, and a Salmonella assembly-name suffix were rejected from full native rows.

All 103 exact-taxid Nuccore summaries were screened: 88 contig records, two WGS masters, twelve marker/gene records, and one short patent sequence. They are not 103 genomes. No sequence-level functional or phenotype claim is inferred from them.

Optional definitions, record-level citations, phenotype lists, discussions, and causal graphs are not blanket requirements for this seeded taxon. iModulonDB is not applicable to its claims. Further enrichment through the BioSample's explicit deposit or a more specific BacDive classification is a maintained-source/design follow-up, not permission to join bare aliases or hand-patch this generated YAML.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major F1: the GTDB species mapping is promoted to exact identity with strain 1340.** Target lines 36-41 retain a species closeMatch, lines 55-60 emit the bare species as EXACT_SYNONYM and equivalent xref, and lines 70-75 repeat the same relationship in the attestation. The inspected 18-member cluster includes other named strains such as DP07 and LC01. Type-strain membership does not make the strain equivalent to the species. The upstream owner is kg-microbe's GTDB transform, imported by `src/taxonmech/extract.py:501`; the local amplification is the rank-unaware closeMatch identity branch in `src/taxonmech/seed.py:454`. The NCBI record's core identity remains correct, so this is major rather than a blocker.

## Recommended Edits

1. Correct the maintained upstream species-to-strain mapping or represent the relationship explicitly as membership, without an identity predicate. Keep cluster-wide metadata scoped to the species concept.
2. Add a rank-aware guard to `src/taxonmech/seed.py` so this closeMatch cannot produce a bare-species exact synonym or equivalent xref on a strain. Preserve all four valid NCBI strain synonyms and genetic code 4. Do not change the valid cluster count from eighteen to one as a substitute for repairing scope.
3. Preserve the parent strain entry, its GOLD assembly/IMG relationship, separate NCTC assemblies, original supplied accession versions, SI deposit-specific evidence, and ATB sample chains. Any optional enrichment should first capture explicit primary-source deposit evidence in the maintained importer; do not loosen generic name matching.
4. After an authorized upstream/code correction, re-extract and re-seed through the validated writer. Do not hand-edit taxon YAML, inventories, or pages.

## Follow-up Checks

Extend `tests/test_seed.py` with a STRAIN target receiving this GTDB species closeMatch. Verify that species membership cannot create exact identity, while the parent species retains its valid mapping and eighteen-member count. Include a fixture with more than one named strain in the cluster so type-strain status cannot mask the rank mismatch.

After an authorized fix, run the relevant unit tests, documented extraction/seed dry runs, `just seed-canary NCBITaxon:1034808`, focused schema/strict validation, corpus reproduction, and full QC. Reinspect the generated file and parent strain evidence. Current tests and schema success alone do not demonstrate that F1 is fixed.

If deposit enrichment is separately pursued, retain the explicit SAMN02469901-to-ATCC:25524 evidence and distinguish current GCA_000221305.2 / GCF_000221305.1 from suppressed GCA_000221305.1 and the two NCTC assemblies. Require source-specific regression tests before using new joins.

## Additional Notes

- HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on the existing review branch. The preceding turn completed the FL-15 report; this turn advances a different uncovered target.
- The seed timestamp 2026-09-13T17:54:04Z equals the newest raw/ATB/StrainInfo manifest timestamp. It records seeding, not human review.
- The GTDB species page was inaccessible through the web tool. Cluster statements rely on inspected pinned native metadata, not a claimed current online census.
- The configured `kg-microbe/data/transformed/madin_etal/edges.tsv` path did not exist; an ignored-inclusive filename search of that configured checkout found no Madin-named file. This is not a claim about every alternate checkout.
- An ignored-inclusive target search of review reports and history found no prior target match before creation. This report does not overwrite an earlier review or append a curation event.
- Only this new report was written. No YAML, scope, source inventory, history, lifecycle status, generated product, or Eukaryota record was changed. No provider credits, external contacts, GitHub mutations, commits, or new worktrees were used.
