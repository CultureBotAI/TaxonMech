# YAML Record Review: Pseudomonas sp. DhA-91

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_dha_91.yaml`
- Started UTC: 2026-10-04T15:38:28Z
- Finished UTC: 2026-10-04T15:41:07Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:103361, species, Bacteria,
EXACT/SEEDED, code 11, ten ancestors, zero inventoried strains, one NCBITAXON
NAME attestation and one seed event. DhA-91 is the target designation, not
DhA-95, a generic Pseudomonas isolate or a culture accession ending 103361.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_dha_91.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_dha_91.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 18445 and scientific-name row 38463 in
`data/catalog/ncbi_names-0000.jsonl.gz` agree with the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103361&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103361)
confirm the name and rank; EFetch confirms parent 196821 and code 11.
Root-first lineage is root (1), cellular organisms (131567), Bacteria (2),
Pseudomonadati (3379134), Pseudomonadota (1224), Gammaproteobacteria (1236),
Pseudomonadales (72274), Pseudomonadaceae (135621), Pseudomonas (286) and
unclassified Pseudomonas (196821), with matching ranks. Species rank does
not establish a validly published species name or finer placement.

## Evidence

Exact Nuccore search returned three records; all source qualifiers and
references were inspected. Each explicitly identifies strain DhA-91,
genomic DNA and taxon 103361:

- [AF177916.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177916.1), UID 5834340: 1,530-base partial 16S rRNA sequence; direct submission 1999-08-17.
- [DQ844798.2](https://www.ncbi.nlm.nih.gov/nuccore/DQ844798.2), UID 116069837: 902-base partial gyrB coding sequence; submission 2006-07-12, sequence update 2006-10-12. Version .2 is preserved.
- [DQ789346.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ789346.1), UID 110631426: 639-base partial coding sequence annotated as a putative diterpenoid dioxygenase alpha subunit; source qualifiers additionally identify Arctic soil, Canada, and primer names; submission 2006-06-20.

These loci are not genomes, culture deposits or independent taxonomic
reclassification. Exact Assembly search returned zero with
phrase-not-found/no-items warnings.

PubMed EFetch metadata and abstracts were inspected for both cited papers:

- Yu, Stewart and Mohn (2000), AEM 66(12):5148-5154, [PMID 11097882](https://pubmed.ncbi.nlm.nih.gov/11097882/), [DOI 10.1128/AEM.66.12.5148-5154.2000](https://doi.org/10.1128/AEM.66.12.5148-5154.2000), PMC92436. The abstract explicitly identifies DhA-91 among cultivated Pseudomonas isolates from hydrocarbon-contaminated Arctic soil. Its GenBank list includes AF177916. This supports isolation context, not a collection deposit or genome link.
- Witzig, Aly, Strompl, Wray, Junca and Pieper (2007), Environmental Microbiology 9(5):1202-1218, [PMID 17472635](https://pubmed.ncbi.nlm.nih.gov/17472635/), [DOI 10.1111/j.1462-2920.2007.01242.x](https://doi.org/10.1111/j.1462-2920.2007.01242.x). Metadata agree with both coding-sequence references and its GenBank list includes DQ789346 and DQ844798. The abstract discusses diterpenoid dioxygenase homologues and gyrB across several strains; its general claims are not assigned specifically to DhA-91 without the experiment-level text.

Full methods, tables and results were not read. PubMed/PMC browser access
was empty or challenged and the DOI page was unavailable; public PubMed
EFetch succeeded. No phenotype or causal claim was added to this
taxonomy-only record. The NAME attestation and snapshot 2026-09-13 agree
with the inventory; one name is not one experiment.

## Completeness

Full exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional fields are
appropriate. `strain_count: 0` counts inventoried strain associations;
it does not assert that DhA-91 was never cultivated.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID, DhA-91 separator variants, label and slug forms across `data/raw`,
`data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`. All 96 matching
rows were inspected, including all 33 native JSON objects read in full.
Three rows concern target scope/backbone/name; the other 93 are unrelated.
Structured recursive SOURCE.json search found two matching fields in
one BacDive response entry; the entire entry was read. It requests
BacDive 103361, not NCBITaxon:103361. Absence is bounded to these searches
and the exact public queries.

Principal numeric collisions:

- BacDive 103361 (`records.jsonl.gz:27494`, raw row 27495) is Agromyces sp. ST029783, taxon 51513, without sequence entries. SOURCE response 275 points to `records-0274.json.gz` for this BacDive request.
- CIP 103361 is Serratia grimesii: BacDive 5163 (native row 5053), species 82995 and strain taxon 1218094, LPSN 780874. StrainInfo 92427 (row 69992), DOI 10.60712/SI-ID92427.3, explicitly associates its own CIP deposit 143676 with the 972-base gyrB accession AJ300538. The grouped genomes GCA_900456935 and GCA_001590905 instead name NCTC 11543 deposit 154944 and NBRC 13537 deposit 335054; grouping does not transfer them to CIP or DhA-91.
- DSM 103361 is Pontivivens insulae GYSW-23, taxon 1639689: BacDive 132247 (native row 54557), StrainInfo 405257 (row 303146), DOI 10.60712/SI-ID405257.3. Its own DSM deposit 912462 explicitly links unversioned GCA_003385715. BacDive also lists a separate CECT 8812 assembly GCA_900302495; neither is target evidence.
- Pontivivens native GenBank/RefSeq GCA_003385715.1 and GCF_003385715.1 have reciprocal identical pairing, DSM 103361, SAMN09074945 and QRDO00000000.1. BV-BRC 1639689.6 explicitly links GCA_003385715.1 and unversioned QRDO00000000. GTDB RS_GCF_003385715.1 explicitly links that GenBank assembly. GOLD Go0402710 -> Gp0290609 -> Ga0244584 connects the organism, project, assembly and IMG 2770939548. GenBank/GOLD/BV-BRC use PRJNA463380; RefSeq/GTDB use PRJNA224116. GTDB Rhodobacteraceae and carried NCBI Paracoccaceae are preserved, not reconciled.
- ATB strain/genome-link matches also concern Pontivivens SAMN09074945. A supplementary full-catalog exact-sample scan found native row 1397317: SRR7174990, ERZ26862051, available FASTA, assembly/Sylph/HQ PASS, prior-HQ T, scientific name and both Sylph fields Pontivivens insulae. These are shared-BioSample links, not assembly equivalence; they supply no DhA-91 chain. SeqKit signatures are not MD5 values and AWS URLs are mutable.
- SRCM103361 is Lactiplantibacillus plantarum, taxon 1590: GenBank/RefSeq GCA_004101545.1/GCF_004101545.1 are reciprocally identical; BV-BRC 1590.1388, GTDB RS_GCF_004101545.1 and GOLD Go0518851 -> Gp0442978 -> Ga0399139 carry explicit links. Native records name SAMN10743316, PRJNA515145 (RefSeq/GTDB PRJNA224116), IMG 2908820819 and CP035148/CP035149/CP035150. BV-BRC retains the older Lactobacillus name. None denotes DhA-91.
- MGBC103361 is an uncultured Muribaculaceae bacterium, taxon 2301481: BV-BRC 2301481.5917, GCA_948671085.1 and GTDB GB_GCA_948671085.1 explicitly correspond, with SAMEA112377310, PRJEB59335 and CAPODU000000000.1 (BV-BRC unversioned). GTDB CAG-873 sp948665475 does not replace the carried NCBI label.
- CP103361 is an unversioned sequence accession for Bacteroides thetaiotaomicron BFG-505, not the target taxon: GOLD Ga0608769 (project Gp0747335) and BV-BRC 818.2120/818.2189 explicitly identify GCA_024799725.1. BV-BRC names taxon 818, SAMN30323408, PRJNA646575 and CP103361/CP103362. The two BV-BRC IDs remain distinct.
- KY103361 is a 686-base rRNA/ITS accession for Lipomyces anomalus, taxon 1337061, in StrainInfo 80186 (row 67090), DOI 10.60712/SI-ID80186.2. It explicitly names CBS 7607 deposit 204459; deposits carry Babjevia anomala. This unrelated source hit does not reopen the Eukaryota corpus review.
- GCA_023696505.1, GCA_004410605.1 and GCA_008795595.1 respectively concern Shigella flexneri PNUSAE103361 (623), Listeria monocytogenes 18B05744-8-R103361 (1639) and Salmonella enterica PNUSAS103361 (28901).
- Three GTDB objects match only assembly statistics: RS_GCF_040325615.1 (Klebsiella pneumoniae, 573, scaffold N90), GB_GCA_003526595.1 (Nitrospina sp., 2024844, total gap length) and RS_GCF_044751945.1 (Pectobacterium sp. CHL-2024, 3377079, scaffold N90). None identifies taxon 103361.

Non-target citations and DOIs were inspected as native metadata, not
independently fetched as target evidence. Supplied accession versions and
unversioned IDs are preserved; source grouping, numeric suffixes, shared
samples and taxonomy alone do not establish strain/genome equivalence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future fixes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:144105`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized fix, verify exact source identity and inventory deltas,
run `just seed-canary NCBITaxon:103361 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. No canary or regeneration ran.
Any future phenotype curation requires the relevant full experiment-level
paper text and an appropriate maintained representation.

## Additional Notes

Unique PATHS entry: `data/taxa/PATHS.tsv:13694`. Seed event remains
2026-09-13T17:54:04Z. NCBI browser access failed; EFetch and Datasets
succeeded. iModulonDB is not applicable to the record's taxonomy-only
assertions; sequence-paper context was not turned into a transcriptomic claim.
Only this report and the validation TSV were written; YAML, maintained
inputs, scope, status, history and GitHub were not changed.
