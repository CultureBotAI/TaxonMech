# YAML Record Review: Rhodococcus qingshengii JCM 15477

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhodococcus_qingshengii_jcm_15477.yaml`
- Started UTC: 2026-10-03T13:49:55Z
- Finished UTC: 2026-10-03T13:56:08Z
- Verdict: needs curation

## Target

- Class `TaxonRecord`; identifier `NCBITaxon:1303681`; rank `STRAIN`;
  domain `BACTERIA`; parent species `NCBITaxon:334542`.
- Read all 940 YAML lines in two complete, untruncated sections before
  making findings. Grounding is `EXACT`; mapping status is `SEEDED`.
- One directly classified BacDive strain, `bacdive:11046`, designation
  djl-6, has five culture deposits, 17 assembly assertions, 15 other genome
  assertions, and 44 related-record assertions. All 76 were reviewed.
- This is generated YAML. Maintained inventories and
  `src/taxonmech/seed.py` own future changes. Only this new report was
  manually written; no record, history, mapping status, or source was edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/rhodococcus_qingshengii_jcm_15477.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/rhodococcus_qingshengii_jcm_15477.yaml`:
  PASS; one file scanned, zero errors. This writes the normal
  `reports/instance_validation_failures.tsv` diagnostic.
- Structured identity, rank, parent, genetic code, eleven ancestor labels
  and ranks, root-first parent chain, three NCBI synonyms, complete target
  subtree, BacDive strain count, and five deposit checks: PASS.
- Exact comparisons of every populated field in all 76 assertions against
  raw inventories and the StrainInfo overlay: PASS. Nested StrainInfo
  evidence was parsed as JSON before comparison.
- All five culture identifiers and explicit source-field matches passed
  the repository's culture-key and CAFI-aware normalization checks.
- Native StrainInfo deposit eligibility, nonerroneous relation, source
  status, versioned DOI, and both exact sequence-deposit checks: PASS.
- A complete scan of all nineteen native GTDB genome shards found 186
  members of the exact mapped species cluster, with 59 distinct NCBI
  taxon identifiers. This semantic check supports finding M1 below.
- `just verify-corpus`: Not checked; it is full-corpus-only, not a
  documented focused validator. No corpus-wide reproduction claim is made.
- No matching external history entry was found by the ignored-inclusive
  search of `history/`; standalone history validation therefore had no
  target. The embedded seed event passed strict validation.
- No causal graph is asserted, so graph gates are not applicable.
  Generated pages, exports, and global product validation were not audited.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308107` identifies the strain and its three
NCBI synonyms; row 68477 identifies its parent species. Native name objects
at `data/catalog/ncbi_names-0007.jsonl.gz:30643` through 30646 distinguish
the scientific name from those synonyms. The complete target subtree is
the singleton taxon 1303681, and all eleven ancestor records agree.

The inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1303681)
supports identity, lineage, and code 11, but displays `no rank`. Approved
read-only requests to [Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303681&retmode=xml)
and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303681)
returned `strain`/`STRAIN`, the same name, parent 334542, and all eleven
lineage IDs. The browser/API discrepancy does not warrant changing the
pinned strain rank.

[JCM 15477](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=15477)
and [BacDive 11046](https://bacdive.dsmz.de/strain/11046) support djl-6 and
CCM 8451, CGMCC 1.6580, DSM 45222, JCM 15477, and KCTC 19205. Their current
pages use Rhodococcus erythropolis, while the NCBI strain retains
Rhodococcus qingshengii. [LPSN's species entry](https://lpsn.dsmz.de/species/rhodococcus-qingshengii)
identifies qingshengii as a synonym of erythropolis and documents the
historical type designations. This is a source-authority difference, not
evidence to rename the NCBI concept or transfer species identity onto it.
The pinned LPSN row `data/raw/lpsn_names.tsv:24288` is species-level
name 786965, linked to parent 334542 and synonym-of 780449. No strain-level
LPSN name or mandatory same-taxon type flag is implied.

The three NCBI strain synonyms remain supported by native name classes
and deposit identity. In contrast, the exact GTDB species synonym and
equivalence xref do not identify this individual strain; see M1.

## Evidence

Maintained inputs were inspected at these locations:

| Input | Row or lines | Supported scope |
| --- | --- | --- |
| `data/raw/bacdive_strains.tsv` | 10900 | Direct strain, five deposits, zero imported medium count |
| `data/raw/mediadive_taxa.tsv` | 2811 | Three direct media: 535, 65, J57 |
| `data/raw/bactotraits_taxa.tsv` | 2277 | Seven direct trait assertions |
| `curation/seed_scope.tsv` | 15421 | Five-source admission reason |
| `data/raw/gtdb_species.tsv` | 154090 | Species cluster size 186 |
| `data/raw/gtdb_mappings.tsv` | 17458 | Strain-targeted closeMatch and cluster count |
| `data/raw/strain_assemblies.tsv` | 3501-3517 | Seventeen assembly assertion paths |
| `data/raw/strain_genome_records.tsv` | 2739-2753 | Fifteen other genome assertion paths |
| `data/raw/strain_related_records.tsv` | 10754-10793 | Forty source-qualified relationships |
| `data/straininfo/related_records.tsv.gz` | 7934-7937 | Four deposit-specific relationships |

The complete native BacDive object at `data/bacdive/records.jsonl.gz:10899`
supports three assembly families and their native IMG and BV-BRC links.
Reference 66792 supports GCA_001313445, IMG 2734481946, and 1303681.3,
and separately GCA_023221595, IMG 8113001176, and 1303681.9. Reference
67770 supports GCA_001646745, IMG 2744054616, and 334542.13. Unversioned
BacDive accessions remain unversioned; source taxon differences are retained.

Complete native genome objects establish the following bounded paths:

- `data/catalog/ncbi_genbank-0000.jsonl.gz:49278`,
  `data/bvbrc/bvbrc-0001.jsonl.gz:23806`, and
  `data/catalog/gtdb_genomes-0011.jsonl.gz:36299` support the explicit
  JCM 15477 deposit, GCA_001313445.1, GTDB GB_GCA_001313445.1,
  PRJDB938, SAMD00016939, and WGS BBFW00000000.1.
- `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:10465` identifies
  GCF_001313445.1 as suppressed, with an assembly-not-live date of
  2020-12-22. YAML assertions for that RefSeq identifier are attributed to
  the dated BV-BRC record, not to current NCBI Assembly. This is supported
  historical association, not a claim of a currently live RefSeq assembly.
- `data/catalog/ncbi_genbank-0001.jsonl.gz:13851`,
  `data/catalog/ncbi_refseq-0001.jsonl.gz:3447`,
  `data/bvbrc/bvbrc-0019.jsonl.gz:18139`, and
  `data/catalog/gtdb_genomes-0010.jsonl.gz:44694` support the JCM 15477
  culture under species taxon 334542, GCA_001646745.1 /
  GCF_001646745.1, SAMN04357315, and WGS LRRJ00000000.1. GenBank and
  BV-BRC use PRJNA306614; RefSeq and GTDB use PRJNA224116. Native NCBI
  rows explicitly pair these assemblies; culture identity is not inferred
  merely from their shared species classification.
- `data/catalog/ncbi_genbank-0021.jsonl.gz:24188`,
  `data/catalog/ncbi_refseq-0004.jsonl.gz:13555`,
  `data/bvbrc/bvbrc-0001.jsonl.gz:23807`, and
  `data/catalog/gtdb_genomes-0011.jsonl.gz:36084` identify the complete
  GCA_023221595.1 / GCF_023221595.1 assembly, SAMN27755118, and strain
  djl-6. Their bare designation is not an explicit registered culture key;
  it does not create additional direct provider joins under the current
  contract. BacDive's own genome relationships are separately supported.

Native GOLD objects preserve organism-project-analysis chains:

- `data/gold/organisms.jsonl.gz:54641` is JCM organism Go0093131.
  Projects Gp0093131 and Gp0150353 at `data/gold/projects.jsonl.gz:55018`
  and 95401 both point to that organism. Analyses Ga0128430 and Ga0132900
  at `data/gold/analyses.jsonl.gz:74792` and 78913 point respectively to
  those projects and support the two JCM assembly/IMG paths above.
- Organism rows 22208, 440898, and 440900 support KCTC Go0026210,
  DSM Go0610126, and CGMCC Go0610128. Their explicit deposit fields
  support organism references, not transfer of the JCM genome paths.
- Analysis Ga0608004 at line 401159 points to Gp0745148 at project
  line 557026 and Go0610127 at organism line 440899. The organism has
  djl-6 but no culture collection identifier. This investigated third
  assembly path is appropriately not joined by a bare designation.

The native StrainInfo object at `data/straininfo/records.jsonl.gz:302218`
is SI-ID 404329 with BacDive ID 11046 and published-online status.
Its sole own eligible deposit is available, nondeprecated DSM 45222,
deposit 911467, with a nonerroneous relation. Both gene sequences explicitly
name that deposit; relation-only alternative designations do not authorize
extra deposit or assembly joins. The [DataCite record](https://api.datacite.org/dois/10.60712/si-id404329.2)
confirms findable DOI 10.60712/SI-ID404329.2, version 2, and its StrainInfo
destination. [NCBI nucleotide EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=KF374699,KF500432&rettype=gb&retmode=xml)
confirms KF374699.1 as partial gyrB, 1,206 bp, and KF500432.1 as partial
catA, 534 bp, both DSM 45222 and taxon 1303681. These are gene sequences,
not assemblies or direct phenotype evidence.

The inspected [BioSample SAMD00016939](https://www.ncbi.nlm.nih.gov/biosample/SAMD00016939)
explicitly names JCM 15477 in the strain and culture-collection fields and
links PRJDB938. A live open of SAMN04357315 and a BioProject search endpoint
failed in the web tool; their YAML relationships remain supported by the
inspected native source rows, not by an assumed successful live lookup.

The five source attestations and embedded seed event reproduce the pinned
inventories. The GTDB total is a species-cluster total, not 186 genomes
of this strain. Media and trait counts are source-attestation counts, not
new growth experiments or phenotype mechanisms asserted by this record.

## Completeness

- All 76 populated links have qualified source support. Repeated accessions
  with different providers or matching source fields preserve independent
  assertion paths and are not accidental duplicate entities.
- Ignored-inclusive exact-deposit searches of the native StrainInfo archive
  found only the eligible DSM object above. Full relevant overlay scans
  found no additional strain assembly assertion for this target.
- Ignored-inclusive searches of `history/`, `data/atb/`, and the compressed
  ATB catalog for the taxon ID, label, slug, BacDive ID, three assembly
  families, and their three BioSamples returned no matches. This is a
  bounded local-source result, not evidence that no sequencing reads exist.
- The structured iModulonDB runner was available but its dataset request
  failed DNS resolution. A subsequent approved read-only request to the
  official [dataset API](https://imodulondb.org/api/datasets) returned the
  complete organism list with no Rhodococcus coverage. Component/gene
  searches were therefore not applicable; this is not negative biological
  evidence for gyrB, catA, or a phenotype.
- Optional causal graphs, experimental phenotypes, and species-level
  nomenclature are not required additions. A native BacDive type-strain
  assertion does not override the documented same-taxon LPSN derivation.
- The consequential gap is semantic scoping of the GTDB identity promotion,
  not missing optional slots or missing direct joins through bare djl-6.

## Findings

**M1 - Major: a GTDB species cluster is promoted to strain equivalence.**

At YAML lines 49-52 the species label Rhodococcus F qingshengii is an
`EXACT_SYNONYM` of the strain, and line 63 puts the species identifier in
equivalence xrefs. The mapping at lines 42-47 and attestation at 913-918
carry the raw `skos:closeMatch` and whole-cluster count that feed this
promotion. Membership in this species does not establish strain identity.

The complete native cluster census found 186 genomes spanning 59 NCBI
taxon identifiers. Counterexamples in
`data/catalog/gtdb_genomes-0000.jsonl.gz` include line 5606,
RS_GCF_021352185.1, strain Ni2, NCBITaxon 2681985, and line 7817,
RS_GCF_001653035.1, strain YH3-3, NCBITaxon 1803579. Exactly two rows
have NCBI taxon 1303681: GB_GCA_001313445.1 and RS_GCF_023221595.1.
That count is not the number of all genomes of this culture: the additional
JCM-matched RS_GCF_001646745.1 row uses parent species taxon 334542.

**Maintained owner:** `src/taxonmech/seed.py`, in the GTDB mapping block
starting around line 450, treats any `skos:closeMatch` as identity without
a compatible-rank guard, then adds both xref and exact synonym. The source
predicate comes through the kg-microbe GTDB transform declared in
`conf/sources.yaml`, via `data/transformed/gtdb/{nodes,edges}.tsv` and
generated `data/raw/gtdb_mappings.tsv`. Upstream predicate semantics also
need review; the generated table and generated YAML are not manual fixes.

Finding counts: zero blockers, one major, zero minor. The NCBI identity,
NCBI strain synonyms, qualified genome links, and source-specific taxonomic
differences do not create additional findings.

## Recommended Edits

1. In `src/taxonmech/seed.py`, require compatible biological scope before
   promoting a GTDB mapping to an exact synonym or equivalence xref.
   This strain must not acquire the species cluster as an identity.
   Add regression coverage in `tests/test_seed.py` for the strain case
   and for valid species-level behavior.
2. Review the upstream kg-microbe GTDB predicate derivation, then refresh
   derived inventories through the documented extraction workflow if
   warranted. Preserve classification or membership provenance without
   inventing a replacement broad/narrow predicate. Do not silently move
   the cluster onto the parent: that species also has another GTDB cluster.
3. Keep the 186 count explicitly scoped to the GTDB species cluster, not
   the strain. Preserve the NCBI identity, three NCBI synonyms, all five
   deposits, and all 76 supported source-qualified relationships.
4. After an authorized maintained-input/code fix, regenerate through the
   documented seed workflow. Do not hand-patch generated YAML or promote
   its review status based on this report alone.

## Follow-up Checks

- Run the focused seed regression tests, including a valid species mapping
  and this below-species target. Schema validity alone cannot detect M1.
- Inspect the regenerated target to confirm the species exact synonym and
  equivalence xref are absent while bounded GTDB provenance remains.
- Repeat the complete cluster census and 76-link comparison; verify that
  accession versions, source IDs, deposit matches, and DOI version survive.
- Rerun both focused validation commands above. After an authorized broad
  regeneration, run full-corpus `just verify-corpus` and the documented
  product gates; those checks were not run during this read-only review.
- Preserve source naming and browser/API rank conflicts explicitly when
  refreshing sources. Recheck live GTDB and unavailable NCBI pages if a
  later change depends on their then-current content.

## Additional Notes

The live GTDB species page was unavailable through the web tool. The
cluster finding rests on the inspected pinned mapping and a complete native
genome census, not a presumed current GTDB release. GTDB's native family
classification differs from NCBI's; the NCBI lineage is not rewritten from it.

The suppressed RefSeq accession is retained as a BV-BRC-attributed historic
association, without an assembly-quality endorsement. Provider-specific
classification at strain or parent species rank is likewise not a reason
to discard an explicit culture match.

Report-file coverage counts do not certify that every existing report has
received the same evidence review. Eukaryota was excluded from new target
selection in accordance with the active goal. No paid provider, source
refresh, GitHub mutation, curation history update, or generated-product
rebuild was performed.
