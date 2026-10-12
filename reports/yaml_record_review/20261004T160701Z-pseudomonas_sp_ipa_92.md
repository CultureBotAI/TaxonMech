# YAML Record Review: Pseudomonas sp. IpA-92

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_ipa_92.yaml`
- Started UTC: 2026-10-04T16:00:49Z
- Finished UTC: 2026-10-04T16:07:01Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:103362, species, Bacteria,
EXACT/SEEDED, genetic code 11, ten ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. IpA-92 is distinct
from DhA-91, IpA-93 and other Pseudomonas isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_ipa_92.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_ipa_92.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded source comparisons do not replace these gates.

## Identity and Grounding

Backbone row 18446 and scientific-name row 38464 in
`data/catalog/ncbi_names-0000.jsonl.gz` agree with the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103362&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103362)
confirm the exact name and species rank; EFetch confirms parent 196821
and genetic code 11.

The root-first chain matches the source: root (1), cellular organisms
(131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224),
Gammaproteobacteria (1236), Pseudomonadales (72274), Pseudomonadaceae
(135621), Pseudomonas (286), unclassified Pseudomonas (196821), with
matching ranks. Species rank does not establish a validly published
species name; this remains a strain-designated taxonomy record.

## Evidence

Exact Nuccore search returned two records; qualifiers and references
were read for both:

- [DQ679938.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ679938.1), UID 110555022, 778 bases: partial CDS of a putative Rieske non-heme iron oxygenase alpha subunit, annotated `ipbAa`. Qualifiers name strain IpA-92, taxon 103362, genomic DNA, hydrocarbon-contaminated Arctic tundra soil, Canada, and primers bphAf371B/bphAr1153-2. Direct submission: 2006-06-08.
- [AF177918.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177918.1), UID 5834342, 1529 bases: partial 16S rRNA sequence. Qualifiers name strain IpA-92, taxon 103362 and genomic DNA; this sequence's qualifiers do not supply geography. Direct submission: 1999-08-17.

These are loci, not assemblies, deposited cultures or independent proof of
a species boundary. Exact Assembly search returned zero with
phrase-not-found/no-items warnings.

PubMed EFetch metadata and abstracts were read afresh for both cited
papers. [PMID 11097882](https://pubmed.ncbi.nlm.nih.gov/11097882/), Yu,
Stewart and Mohn, AEM 66(12):5148-5154 (2000), resolves to DOI
[10.1128/AEM.66.12.5148-5154.2000](https://doi.org/10.1128/AEM.66.12.5148-5154.2000)
and PMC92436; its databank includes AF177918. Its abstract explicitly
identifies IpA-92 among the Pseudomonas isolates from contaminated Arctic
soil and distinguishes its reported substrate range from DhA-91/DhA-95.
That distinction prevents transferring the latter strains' abietane
claims to IpA-92.

[PMID 17472635](https://pubmed.ncbi.nlm.nih.gov/17472635/), Witzig, Aly,
Stroempl, Wray, Junca and Pieper, Environmental Microbiology
9(5):1202-1218 (2007), resolves to DOI
[10.1111/j.1462-2920.2007.01242.x](https://doi.org/10.1111/j.1462-2920.2007.01242.x);
its databank includes DQ679938. The abstract discusses DitA1 homologues,
expression experiments and evolutionary analyses without specifically
naming IpA-92. Its title and general results do not justify relabeling
IpA-92's putative ipbAa sequence as experimentally validated DitA1.

Full methods, tables and results were not obtained: browser PubMed
content was unavailable, PMC presented a challenge and DOI full text
was inaccessible. The YAML contains no phenotype or gene-function claim;
none is added or inferred. The single NAME attestation and snapshot
2026-09-13 agree with the inventory; the count is not an experiment count.

## Completeness

Full exact-ID scans found no target rows in the BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional fields are
appropriate. Zero inventoried strains does not mean never isolated or
cultivated.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
identifier, IpA-92 designation variants, and label/slug forms across
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
The 180 matching rows comprised three target scope/backbone/name rows and
177 numeric/accession collisions. All were classified using matching
fields and structured identity context; 68 full native objects were
additionally read: seven BacDive/StrainInfo, twelve GOLD, thirty BV-BRC
and nineteen assembly/GTDB objects. This does not claim a full manual
read of every raw TSV row.

A separate recursive structured SOURCE.json scan found two matching
fields in one BacDive entry: response 275 requested BacDive 103362 and
cached records-0274.json.gz. The full manifest entry concerns the BacDive
identifier, not NCBITaxon:103362. Absence conclusions are bounded to the
searched local sources and exact public queries.

The principal collisions and their identity boundaries are documented
below. None supplies an IpA-92 strain/deposit/genome chain. Their rejection
is based on identity, not assembly quality.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:144106`. Do not hand-edit generated YAML or
transfer unrelated collection accessions, grouped sequences or phenotypes
into this taxon.

## Follow-up Checks

After an authorized fix, verify exact source identity and inventory deltas,
run `just seed-canary NCBITaxon:103362 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. A future phenotype or
gene-function curation would require strain-specific full-text evidence.
No canary, regeneration, status promotion or history event ran.

## Additional Notes

Native collision details, preserving identifier systems and supplied
versions:

- BacDive 103362 is Agromyces sp. ST029890, taxon 51513, with no Sequence information. Its DOI is 10.13145/bacdive103362.20260601.11. The matching SOURCE.json request is consistent with this BacDive identity.
- CIP 103362 is Borrelia/Borreliella garinii, taxon 29519, isolate 20047. BacDive 14307 currently uses Borrelia garinii subsp. garinii and lists DSM 10534, ATCC 51383 and CIP 103362. StrainInfo SI-ID42962, DOI 10.60712/SI-ID42962.3, explicitly links its own CIP deposit SI-DP115581 to unversioned GCA_001922545. Other deposits, including DSM SI-DP162064 and ATCC SI-DP115580, remain separate. Native species/subspecies naming differences are preserved, not resolved here.
- Three distinct CIP 103362 assembly pairs were read: GCA_001922545.1/GCF_001922545.1 (SAMN05941958, 12 replicons, 1156110 bases), GCA_040732965.1/GCF_040732965.1 (SAMN42329591, one replicon, 905581 bases), and GCA_040790705.1/GCF_040790705.1 (SAMN42233987, ten replicons, 1198954 bases). Each pair is reciprocally identical within that pair; the three assemblies are not interchangeable. GenBank projects are respectively PRJNA350560, PRJNA1132127 and PRJNA1130942; RefSeq uses PRJNA224116. All are latest complete assemblies with no WGS accession. The third uses CIP103362 without a separator.
- GTDB RS_GCF_001922545.1, RS_GCF_040732965.1 and RS_GCF_040790705.1 explicitly identify their corresponding GCA accessions. GTDB's Borreliales and NCBI's Spirochaetales placements remain source-specific.
- Twenty-five BV-BRC taxon-29519 objects were read. IDs 29519.15 through 29519.25 have Plasmid status and explicit GCA_001922545.1, SAMN05941958/PRJNA350560 and unversioned CP018745 through CP018755 sequences. IDs 29519.163 through 29519.172 are Plasmid records with SAMN05941958/PRJNA224116 and unversioned NZ_CP sequences but no assembly field; 29519.173 explicitly supplies GCA_001922545.1 and unversioned NZ_CP018755. Complete record 29519.9 explicitly supplies GCF_001922545.1, SAMN05941958/PRJNA350560, unversioned CP018744 through CP018755 and NZ_CP counterparts supplied with .1. Complete records 29519.499 and 29519.500 have no assembly field: their respective sample/project/sequence evidence is SAMN42329591/PRJNA1132127/CP160381 and SAMN42233987/PRJNA1130942/CP161030 through CP161039. Plasmid status is not whole-genome status; sample/sequence agreement alone does not establish an absent assembly link.
- GOLD chain Go0364026 -> Gp0203106 -> Ga0175939 explicitly supplies GCA_001922545.1, SAMN05941958/PRJNA350560, CP018744 through CP018755 and IMG 2728369389. Go0624453 -> Gp0854512 -> Ga0681605 supplies GCA_040732965.1, SAMN42329591/PRJNA1132127 and CP160381, without IMG. Go0033065 is a separate matching CIP organism object, not an invented project chain. GOLD Go/Gp/Ga identifiers are not genome identifiers.
- DSM 103362 is Bifidobacterium jacchi, taxon 2490545, BacDive 159320, MRM 9.3/JCM 31788. SI-ID404258, DOI 10.60712/SI-ID404258.3, has own DSM deposit SI-DP911387 but no sequence array. BacDive's unversioned GCA_009078285, BV-BRC 2490545.3 and IMG 2891598198 concern MRM 9.3; they cannot be attributed to the SI DSM deposit from grouping alone. KP718960 is partial 16S, 1466 bases, carrying taxon 1630179. GOLD Go0620532 is an organism object.
- SI-DP103362 is IFO 12839, Streptomyces antimycoticus, taxon 68175, in SI-ID38280, DOI 10.60712/SI-ID38280.3, with BacDive 14991. Its explicit sequence is unversioned AB122752, 565-base 16S. Grouped GCA_005405925 instead names NBRC 12839, SI-DP334253; origin references to the IFO deposit do not transfer that genome.
- KY103362 is a 749-base rRNA/ITS accession explicitly linked to CBS 6740, SI-DP181840, in SI-ID64726, DOI 10.60712/SI-ID64726.3. The record is Lipomyces anomalus, taxon 1337061, with Babjevia/Dipodascopsis deposit naming. Grouped GCA_030580435 belongs to NRRL Y-7931, SI-DP204453, not CBS 6740. This is an unrelated eukaryotic source collision, not a reopened eukaryotic record review.
- SRCM103362 is Lactiplantibacillus plantarum, taxon 1590. GCA_004101605.1/GCF_004101605.1 are reciprocally identical complete five-replicon assemblies of 3118171 bases, SAMN10743347, no WGS, GenBank PRJNA515153/RefSeq PRJNA224116. BV-BRC 1590.1389 explicitly supplies GCA_004101605.1 and unversioned CP035156 through CP035160, under the older Lactobacillus name. GTDB GB_GCA_004101605.1 is a GB identifier, not RS. GOLD Go0518847 -> Gp0442973 -> Ga0399691 supplies the GenBank assembly/sample/project, the CP sequences and IMG 2912325993.
- MGBC103362 is an uncultured Anaeroplasmataceae bacterium, taxon 658266. BV-BRC 658266.271 explicitly supplies GCA_948693585.1, SAMEA112377311/PRJEB59335 and unversioned CAPRMG000000000. The GenBank object supplies WGS CAPRMG000000000.1, a metagenome-derived scaffold assembly with 434 contigs and 427 scaffolds. It has no RefSeq pair and the search found no corresponding GTDB hit.
- MarMAG_103362 is an uncultured bacterium, taxon 77133. BV-BRC 77133.15074 has SAMEA120728967/PRJEB104710 and unversioned CDUZXC000000000 but no assembly field. GenBank GCA_977632675.1 shares this isolate/sample/project and WGS CDUZXC000000000.1; it is metagenome-derived, with 63 contigs and 30 scaffolds. Shared sample/project/WGS is not asserted assembly equivalence.
- CP103362 is a sequence accession for Bacteroides thetaiotaomicron BFG-505, taxon 818. Distinct BV-BRC records 818.2120 and 818.2189 explicitly supply GCA_024799725.1, SAMN30323408/PRJNA646575 and unversioned CP103361/CP103362. GOLD Ga0608769, project Gp0747335, supplies the same GCA and CP accessions, with no IMG.
- Other native GenBank isolate collisions are GCA_004472765.1, Listeria monocytogenes 18B05744-9-R103362, taxon 1639; GCA_023697805.1, Shigella flexneri PNUSAE103362, taxon 623; GCA_008803615.1, Salmonella enterica PNUSAS103362, taxon 28901; and GCA_026140445.1, Shigella boydii isolate 103362, taxon 621. The last supplies SAMEA8899876/PRJNA514245 and DAJVTT000000000.1. Its PMID 30286803 was not fetched or used as target evidence.
- ATB catalog row 377897 concerns SAMEA117626548, ERR14242004 and ERZ26976109, scientific/current Sylph name Staphylococcus aureus, earlier Sylph and prior-HQ NA. FASTA is available and assembly/Sylph/HQ filters PASS. Only the SeqKit signature seqkit.v0.1_DLS_k0_a9df5fd648bbc2cd7ae103362a634dc9 contains the numeric substring. This is not a target sample/strain/genome association. SeqKit is not MD5 and AWS URLs are mutable.

DOIs and citations on unrelated native objects were inspected as source
metadata, not independently fetched or used as IpA-92 evidence.
Supplied accession versions and unversioned accessions remain distinct;
shared taxonomy, culture names or BioSamples do not establish genome
equivalence.

Unique PATHS entry: `data/taxa/PATHS.tsv:13705`. Seed event remains
2026-09-13T17:54:04Z. NCBI browser access failed; EFetch and Datasets
succeeded. iModulonDB is not applicable to the taxonomy-only assertions
in the YAML; nearby sequence/literature context is not automatically
transcriptomic evidence. Only this report and the validation TSV were
written; YAML, maintained inputs, scope, status, history and GitHub
were not changed.

