# YAML Record Review: Sphingomonas sp. DhA-95

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sphingomonas_sp_dha_95.yaml`
- Started UTC: 2026-10-04T15:12:35Z
- Finished UTC: 2026-10-04T15:15:54Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:103360, species, Bacteria,
EXACT/SEEDED, genetic code 11, ten ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The complete designation
DhA-95, not a collection number or a neighboring DhA strain, is the target.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/sphingomonas_sp_dha_95.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/sphingomonas_sp_dha_95.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 18444 and scientific-name row 38462 in
`data/catalog/ncbi_names-0000.jsonl.gz` agree with the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103360&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103360)
confirm name and species rank; EFetch confirms parent 196159 and code 11.
Root-first lineage matches: root (1), cellular organisms (131567), Bacteria
(2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria
(28211), Sphingomonadales (204457), Sphingomonadaceae (41297), Sphingomonas
(13687), unclassified Sphingomonas (196159). The respective ranks are
NO_RANK, CELLULAR_ROOT, DOMAIN, KINGDOM, PHYLUM, CLASS, ORDER, FAMILY,
GENUS and NO_RANK. Species rank for this strain-designated taxon does not
establish a validly published species name or a more precise placement.

## Evidence

Exact Nuccore search returned one [AF177917.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177917.1)
record, UID 5834341, a 1,482-base partial 16S rRNA sequence. Inspected source
qualifiers identify Sphingomonas sp. DhA-95, strain DhA-95, genomic DNA and
taxon 103360. The sequence is not a genome or culture-deposit accession.
Exact Assembly search returned zero with phrase-not-found/no-items warnings.

The sequence cites Yu, Stewart and Mohn's 2000 study in Applied and
Environmental Microbiology 66(12):5148-5154 and their direct submission
dated 1999-08-17. Primary [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=11097882&retmode=xml&tool=taxonmech_record_review)
confirms PMID 11097882, DOI 10.1128/AEM.66.12.5148-5154.2000, PMC92436,
authors, year, journal and the AF177917 accession association. The inspected
abstract explicitly identifies DhA-95 as Sphingomonas and reports its
isolation and cultivation in the Arctic-soil study. This supports a
cultivated strain, not a collection deposit or an assembly link. Its
experimental results are not generalized to the genus or added as new
claims to this taxonomy-only record.

PubMed and PMC browser pages returned access challenges; the publisher
returned HTTP 403 and Europe PMC full-text XML returned HTTP 500. NCBI
PubMed/PMC APIs supplied the inspected metadata and abstract. Full paper
methods, tables and results were not read. The record itself makes no
phenotype claim requiring inference from the paper title.

The one NAME attestation and snapshot 2026-09-13 agree with the inventory;
one name is not one experiment. Zero inventoried strains does not assert
that DhA-95 was never cultured.

## Completeness

Complete exact-ID scans found no target entries in BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin or BactoTraits inventories. Optional nomenclature,
mapping, strain and genome fields need not be filled with near matches.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID, full label/slug and DhA-95 designation with separator variants across
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All 43 matching lines were inspected; all 20 matching native JSON objects
were read in full. Three lines are the target's scope/backbone/name.
Remaining matches are unrelated numeric identifiers or assembly statistics.
Recursive structured SOURCE.json search found two matching fields in one
BacDive response entry; that full entry was inspected and requests BacDive
103360, not NCBITaxon:103360. Absence is bounded to these searches.

- BacDive 103360 (`data/bacdive/records.jsonl.gz:27493`; inventory row 27494) is Agromyces sp. ST029782, taxon 51513, without sequence entries. The matching DOI and SOURCE.json request number belong to this BacDive namespace.
- CIP 103360 belongs to Leminorella richardii: BacDive 4982 (`records.jsonl.gz:4872`), strain BE2-2083, strain taxon 1354266/species 158841; LPSN 777470, NCBI type-material rows, culture-collection inventory and GOLD Go0296487 (`data/gold/organisms.jsonl.gz:234477`) agree on the unrelated organism. StrainInfo SI-ID 13713 (`data/straininfo/records.jsonl.gz:13713`), DOI version 10.60712/SI-ID13713.3, explicitly associates CIP 103360 with SI-DP 52734 and gene sequence AM422901. Its genome GCA_900478135 belongs to NCTC 12151 / SI-DP 52739, not to the CIP deposit by mere record grouping. BacDive also carries unversioned GCA_900478135, BV-BRC 158841.3 and IMG 2887760073 for that other strain association. No versions or cross-deposit links are inferred.
- DSM 103360 belongs to Pedococcus soli THG-a14, taxon 1456769: BacDive 132227 (`records.jsonl.gz:54537`), StrainInfo SI-ID 400907 / SI-DP 907800 (`records.jsonl.gz:298796`), DOI version 10.60712/SI-ID400907.3. LPSN inventories carry Pedococcus soli and its Phycicoccus soli synonym. GOLD Go0620527 (`data/gold/organisms.jsonl.gz:451162`) retains Phycicoccus soli. BacDive's KF999706 is a partial 16S sequence; the SI record supplies no sequences. These names and source chains are preserved without transferring evidence to DhA-95. GOLD organism IDs are not genome identifiers.
- StrainInfo SI-ID 111687 (`data/straininfo/records.jsonl.gz:77316`), DOI version 10.60712/SI-ID111687.2, is Dioszegia zsoltii, taxon 183969. The numeric match is unversioned KY103360, an rRNA/ITS locus explicitly attached to CBS 9127 / SI-DP 457818, not a target genome. This unrelated eukaryotic source hit was inspected only to exclude a false match, not to re-review Eukaryota.
- BV-BRC 194843.4359 (`data/bvbrc/bvbrc-0009.jsonl.gz:2285`), GenBank GCA_948736365.1 (`data/catalog/ncbi_genbank-0060.jsonl.gz:24648`) and GTDB GB_GCA_948736365.1 (`data/catalog/gtdb_genomes-0014.jsonl.gz:31783`) concern MGBC103360, uncultured Bacteroidales bacterium, taxon 194843, SAMEA112377309, PRJEB59335. Explicit assembly links are present. BV-BRC retains CAPXUX000000000 without a version; GenBank/GTDB carry CAPXUX000000000.1. GTDB assigns Cryptobacteroides sp009774765 while carrying the different NCBI classification; neither classification concerns DhA-95.
- BV-BRC 77133.13878 (`data/bvbrc/bvbrc-0027.jsonl.gz:1548`) and GenBank GCA_977591415.1 (`data/catalog/ncbi_genbank-0065.jsonl.gz:7764`) concern MarMAG_103360, uncultured bacterium taxon 77133, SAMEA120729052, PRJEB104710. BV-BRC supplies no assembly accession; it retains unversioned CDUTUP000000000, while GenBank carries CDUTUP000000000.1. Shared sample/project and similar WGS accessions are not asserted to prove assembly equivalence.
- GenBank GCA_023697045.1 (`ncbi_genbank-0021.jsonl.gz:46147`) is Shigella flexneri PNUSAE103360, taxon 623; GCA_008794735.1 (`ncbi_genbank-0007.jsonl.gz:34788`) is Salmonella enterica PNUSAS103360, taxon 28901. Only strain-name suffixes match.
- Four GTDB objects match only assembly statistics: RS_GCF_006369905.1 (`gtdb_genomes-0007.jsonl.gz:40367`), Xylella fastidiosa taxon 2371, contig/scaffold N50; GB_GCA_964409615.1 (`gtdb_genomes-0005.jsonl.gz:6181`), uncultured Candidatus Saccharibacteria bacterium taxon 179883, scaffold N75; RS_GCF_948908075.1 (`gtdb_genomes-0014.jsonl.gz:30617`), Parabacteroides goldsteinii taxon 328812, contig/scaffold N50; RS_GCF_019841565.1 (`gtdb_genomes-0015.jsonl.gz:41961`), Escherichia coli taxon 562, scaffold N50. Their explicit GenBank links and supplied versions remain separate from this target.

The corresponding raw/StrainInfo links are projections of these unrelated
identities, not new target attestations. Non-target DOIs, papers and sequence
accessions were inspected as local source fields, not independently fetched
or used as target evidence. No explicit DhA-95 deposit/genome chain was found.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:144104`. Do not hand-edit generated YAML or convert
numeric suffix matches into taxon/strain/genome equivalence.

## Follow-up Checks

If future curation adds a collection or genome link, verify its explicit
DhA-95 identity and deposit-specific source chain, preserving versions.
Then run `just seed-canary NCBITaxon:103360 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. Inspect full paper methods and
results before any future phenotype curation. No canary or regeneration ran.

## Additional Notes

Unique PATHS entry: `data/taxa/PATHS.tsv:13683`. Seed event remains
2026-09-13T17:54:04Z. NCBI taxonomy browser access failed; taxonomy EFetch
and Datasets succeeded. iModulonDB is not applicable to this taxonomy-only
record. Only this report and the validation TSV were written; YAML, inputs,
scope, status, history and GitHub were not changed.
