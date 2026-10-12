# YAML Record Review: Pseudomonas sp. IpA-93

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_ipa_93.yaml`
- Started UTC: 2026-10-04T16:26:36Z
- Finished UTC: 2026-10-04T16:28:33Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:103363, species, Bacteria,
EXACT/SEEDED, code 11, ten ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. IpA-93 is not IpA-92,
DhA-93 or another resin-acid isolate.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_ipa_93.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_ipa_93.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 18447 and scientific-name row 38465 in
`data/catalog/ncbi_names-0000.jsonl.gz` agree with the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103363&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103363)
confirm the exact name and species rank; EFetch confirms parent 196821
and code 11.

Root-first lineage matches the source: root (1), cellular organisms
(131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224),
Gammaproteobacteria (1236), Pseudomonadales (72274), Pseudomonadaceae
(135621), Pseudomonas (286) and unclassified Pseudomonas (196821), with
matching ranks. Species rank does not establish a validly published
species name.

## Evidence

Exact Nuccore search returned [AF177919.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177919.1),
UID 5834343, one 1532-base partial 16S rRNA sequence. Its inspected
qualifiers name strain IpA-93, taxon 103363 and genomic DNA, but supply
no location or habitat qualifier. This locus is not an assembly or a
culture-deposit accession. The direct submission by Yu, Stewart and Mohn
is dated 1999-08-17. Exact Assembly search returned zero with
phrase-not-found/no-items warnings.

PubMed EFetch verified [PMID 11097882](https://pubmed.ncbi.nlm.nih.gov/11097882/),
Yu, Stewart and Mohn, AEM 66(12):5148-5154 (2000), DOI
[10.1128/AEM.66.12.5148-5154.2000](https://doi.org/10.1128/AEM.66.12.5148-5154.2000),
PMC92436, and the AF177919 databank entry. The
[PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC92436/) was accessible:
abstract, methods, results, tables 1-3 and discussion were inspected.
It explicitly assigns IpA-93 to the Alert-2 enrichment and AF177919;
IpA-92 is a different isolate. Table 3 reports different strain-specific
substrate results. The proposed P. mandelii affiliation is tentative,
based on 99.2% 16S similarity, not a replacement for the carried NCBI
lineage. The negative ditA1 PCR result is bounded to that assay, not proof
of genome-wide gene absence. Figure captions were read, but figure pixels
and raw data were not independently analyzed.

The taxonomy-only YAML asserts no phenotype, gene function or experiment.
These paper observations are contextual evidence, not new YAML claims.
The single NAME attestation and snapshot 2026-09-13 agree with the
inventory; a name count is not an experimental count.

## Completeness

Full exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional fields are
appropriate. Zero inventoried strains does not mean never isolated or
cultivated.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
identifier, IpA-93 variants and label/slug forms across `data/raw`,
`data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`.
All 52 matching rows were classified from matching fields and structured
identity context: three target scope/backbone/name rows and 49 unrelated
numeric/accession matches. Twenty full native objects were additionally
read: three BacDive, three StrainInfo, two GOLD, two BV-BRC and ten
assembly/GTDB objects. This does not claim a full manual read of every
raw TSV row.

A separate recursive SOURCE.json scan found two matching fields in one
BacDive manifest entry. The full response 275 entry requests BacDive
103363 at requested_ids index 95 and caches records-0274.json.gz,
retrieved 2026-09-13T17:06:36.008774+00:00. It concerns the BacDive
identifier, not NCBITaxon:103363. No ATB target match appeared in the
ignored-inclusive search. Absence is bounded to these local sources and
exact public queries.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks. Unrelated native-source
naming and sequence-grouping differences below are not findings against
IpA-93.

## Recommended Edits

None. Future fixes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:144107`. Do not hand-edit generated YAML,
rename the target from tentative literature placement or import another
strain's deposit/genome relationships.

## Follow-up Checks

After an authorized fix, verify exact source identity and inventory deltas,
run `just seed-canary NCBITaxon:103363 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. Any future phenotype curation
must preserve the exact strain, condition and table-level evidence.
No canary, regeneration, promotion or history event ran.

## Additional Notes

Culture/deposit collisions:

- BacDive 103363 (`data/bacdive/records.jsonl.gz:27496`) is Agromyces sp. ST029897, taxon 51513, with an empty Sequence information object. DOI 10.13145/bacdive103363.20260601.11 matches the BacDive manifest identity, not the target taxon.
- CIP 103363 is Streptococcus vestibularis. BacDive 14794 (native row 14622) names MM1 and has separate species-level taxon 1343 and strain-level taxon 889206. Those ranks are not an IpA-93 match. It lists the unversioned assembly GCA_000188295, BV-BRC 889206.3 and IMG 649990016 for ATCC 49124. Its grouped rRNA entries include other Streptococcus taxon IDs despite ATCC 49124 wording; grouping does not settle those sequence identities. This unrelated source inconsistency is not reconciled here.
- StrainInfo SI-ID7693 (native row 7693), DOI 10.60712/SI-ID7693.3, identifies its own CIP 103363 deposit as SI-DP155860. Six unversioned gene sequences explicitly name that deposit: AM901438 (sip, 1248 bases), AY687375 (rpoB, 556), EU003687 (groEL, 757), EU003764 (gyrB, 458), EU917304 (recN, 1249) and Z95922 (sodA, 435). These are not genomes. Its grouped genome GCA_000188295 instead names ATCC 49124, SI-DP113799, and cannot be attributed to CIP merely by group membership or deposit origin. NCBI names/type-material rows and LPSN 781394 concern the same unrelated Streptococcus taxon.
- GOLD organism Go0271360 (`data/gold/organisms.jsonl.gz:209402`) names CIP 103363 and taxon 1343. It is an organism record, not a genome; no sequencing/analysis-project chain is invented.
- DSM 103363 is Carnobacterium antarcticum CP-1, taxon 2126436, BacDive 158403 (native row 80639), LPSN 797694. BacDive supplies MG734178, a 1432-base partial 16S, and unversioned GCA_042658365/GCA_042681165 described for CGMCC 1.15643. StrainInfo SI-ID396976 (native row 294865), DOI 10.60712/SI-ID396976.3, has own DSM deposit SI-DP903571 and no sequence array; its grouped CGMCC designation does not establish an SI-DP-to-genome link. GOLD Go0620533 (organism row 451168) likewise concerns DSM 103363, not IpA-93.
- KY103363 is a 682-base rRNA/ITS accession in SI-ID80185 (native row 67089), DOI 10.60712/SI-ID80185.2, explicitly naming CBS 7606, SI-DP204456. Native strain name is Lipomyces anomalus, taxon 1337061, while deposits use Babjevia/Dipodascopsis names. MUCL 39786 (SI-DP204455) and VKM Y-2716 (SI-DP204457) remain separate deposits. This is an unrelated eukaryotic source collision, not a reopened eukaryotic record review.

Assembly/sequence collisions:

- MGBC103363 is Paramuribaculum intestinale, taxon 2094151. BV-BRC 2094151.187 (`data/bvbrc/bvbrc-0012.jsonl.gz:44261`) explicitly supplies GCA_948708295.1, SAMEA112377312/PRJEB59335 and unversioned CAPTQV000000000. GenBank row 21841 in ncbi_genbank-0060 and GTDB row 40003 in gtdb_genomes-0003 identify the same GCA explicitly; GTDB identifier is GB_GCA_948708295.1, not RS. Both native catalog objects supply WGS CAPTQV000000000.1, 47 contigs, 36 scaffolds, total length 1453431 and ungapped length 1452331. GenBank is latest and has no RefSeq pair. MAG completeness/length flags do not establish target identity or alone justify this exclusion.
- MarMAG_103363 is an uncultured bacterium, taxon 77133. BV-BRC 77133.13879 (`data/bvbrc/bvbrc-0027.jsonl.gz:1549`) supplies SAMEA120729058/PRJEB104710 and unversioned CDUTUK000000000 but no assembly field. GenBank GCA_977591425.1 (`data/catalog/ncbi_genbank-0065.jsonl.gz:7765`) supplies that isolate/sample/project and CDUTUK000000000.1; it is latest, metagenome-derived, scaffold-level, 62 contigs/34 scaffolds, with no RefSeq pair. Shared BioSample/project/WGS is not asserted assembly equivalence.
- GCA_004463825.1 (`data/catalog/ncbi_genbank-0003.jsonl.gz:24300`) is Listeria monocytogenes 18B05744-10-R103363, taxon 1639, SAMN10519771/PRJNA215355, AAANDE000000000.1. GCA_023696225.1 (ncbi_genbank-0021 row 46106) is Shigella flexneri PNUSAE103363, taxon 623, SAMN28922583/PRJNA218110, ABGMSR000000000.1. Both are latest contig-level objects without RefSeq partners; their isolate suffixes, not target taxon identity, triggered the search.

Five additional GTDB hits are assembly statistics, not taxon identifiers.
Each full object supplies its GCA accession explicitly:

| Native GTDB object | Source identity | Sample/project; WGS | Matching statistic |
| --- | --- | --- | --- |
| GB_GCA_049325475.1; gtdb_genomes-0016:41965 | Patescibacteria group bacterium Betzabe_MAG025, taxon 2052139; GTDB MWCR01 sp049325475 | SAMN47594856/PRJNA1149943; JBMOLN000000000.1 | scaffold N75 103363 |
| RS_GCF_046295595.1; gtdb_genomes-0005:25927 | Brevundimonas sp. 21I_055.bin.2, taxon 1871086; GTDB Brevundimonas sp046295595 | SAMN45832956/PRJNA224116; JBKBMX000000000.1 | contig N50 103363 |
| RS_GCF_001324725.1; gtdb_genomes-0014:7802 | Mycobacterium tuberculosis 2180W, taxon 1773 | SAMEA1707117/PRJNA224116; CHCL00000000.1 | contig N50 103363 |
| GB_GCA_001573165.1; gtdb_genomes-0009:20520 | Bacillus thuringiensis KB1, taxon 1428; GTDB Bacillus_A tropicus | SAMN04492775/PRJNA312024; LSNJ00000000.1 | scaffold N90 103363 |
| RS_GCF_001238785.1; gtdb_genomes-0009:21116 | Campylobacter jejuni OXC6542, taxon 197; GTDB Campylobacter_D jejuni | SAMEA1010582/PRJNA224116; CUSO00000000.1 | scaffold N75 103363 |

The table's catalog paths are under `data/catalog/` with suffix
`.jsonl.gz`. Source-specific GTDB/NCBI names and placements are
preserved; neither their differences nor assembly quality link these
objects to IpA-93.

DOIs and citations on unrelated native records, including LPSN's
Carnobacterium PMID 29616891, were inspected as metadata only, not
independently fetched or used as target evidence. All supplied accession
versions and unversioned accessions are preserved. Sample/project/GOLD
organism identifiers remain separate from genomes.

Unique PATHS entry: `data/taxa/PATHS.tsv:13716`. Seed event remains
2026-09-13T17:54:04Z. NCBI taxonomy browser access failed; EFetch and
Datasets succeeded. PubMed browser content was empty, but PubMed EFetch
and PMC succeeded. iModulonDB is not applicable to the taxonomy-only
YAML; sequence/literature context is not automatically expression-module
evidence. Only this report and the validation TSV were written; YAML,
maintained inputs, scope, status, history and GitHub were not changed.

