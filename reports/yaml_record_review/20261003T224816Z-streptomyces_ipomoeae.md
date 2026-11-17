# YAML Record Review: Streptomyces ipomoeae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_ipomoeae.yaml`
- Started UTC: 2026-10-03T22:38:30Z
- Finished UTC: 2026-10-03T22:48:16Z
- Verdict: needs curation

## Target

Read all 844 lines of the generated `TaxonRecord`, `NCBITaxon:103232`,
Streptomyces ipomoeae, rank `SPECIES`, domain `BACTERIA`, grounding
`EXACT`, mapping status `SEEDED`. Both BacDive strains are present:
15330, designation 9820, with eight deposits and the type-strain flag;
15331, designation AE-419, with three deposits and no type flag.
They have 32 and nine related-record assertions respectively, but neither
has a genome assembly or typed genome record.

This read-only review changes no generated YAML, maintained source,
scope, history, status or prior report. Its finding concerns missing
strain-genome representation, not incorrect taxon identity.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_ipomoeae.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptomyces_ipomoeae.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured inventory comparison | Identity, complete lineage, synonyms, nomenclature, mappings, scope, path and all eight attestations agree. |
| Complete strain-link multiset comparison | Both empty genome lists and all 41 related-record assertions match the raw and StrainInfo link inventories, including nested evidence. |
| Native StrainInfo evidence comparison | All 24 carried evidence objects agree with the native records, own deposits, statuses, DOI versions and explicit sequence-deposit associations. |
| Native GOLD evidence comparison | All 17 carried source-strain assertions agree with nine native organism records. |
| Embedded history | Strict validation passed; the eight-source seed event and scope reason agree. |
| Standalone history | Identifier, label and slug searches, including ignored and hidden files, found no target entry under `history/`. |
| Graph and ontology-product checks | Not applicable: no causal graph or curator-added ontology-product assertion is present. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports, sequence alignment and FASTA checksum
replay. Focused comparisons are not corpus reproduction. No generator or
history writer was run. Validation success does not prove completeness.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18356` and live NCBI EFetch and
[taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103232)
agree on the identifier, species name, parent `NCBITaxon:1883`, genetic
code 11 and all nine root-first lineage entries. Preserve NCBI's
Kitasatosporales placement rather than substituting GTDB's Streptomycetales.
The child `NCBITaxon:698759`, Streptomyces ipomoeae 91-03, is a distinct
strain taxon and is not folded into direct-source counts.

The path at `data/taxa/PATHS.tsv:13185` and scope at
`curation/seed_scope.tsv:892` agree. Complete merged-ID and dropped-row
checks found no target exception. NCBI type-material rows 1595-1616
corroborate type designations; the culture inventory has all 11 carried
deposit associations. These are identity evidence, not genome assertions.

[LPSN 781770](https://lpsn.dsmz.de/species/streptomyces-ipomoeae)
supports the authority, ICNP-valid and legitimate correct name, and type
culture. Its full name includes the orthographic correction notation.
The five carried type designations are supported; the live page's
additional designations do not authorize alias expansion in genome joins.
[LPSN 43327](https://lpsn.dsmz.de/species/streptomyces-ipomoea)
identifies the inaccurate spelling. The six source-scoped synonyms match
their inventories: preserve the different NCBI exact-synonym and LPSN
related-name treatments rather than silently reconciling them.

`data/raw/lpsn_names.tsv:20428` supports the complete nomenclature object.
The medical-use wording is source nomenclatural metadata, not a clinical
recommendation. Exact taxonomic grounding does not make strains or
assemblies interchangeable.

## Evidence

- **BacDive:** raw strain rows 15155-15156, native
  `data/bacdive/records.jsonl.gz` rows 15154-15155, and inspected
  [15330](https://bacdive.dsmz.de/strain/15330) and
  [15331](https://bacdive.dsmz.de/strain/15331) pages support the two
  designations, taxon assignments and deposits. Native type values are
  explicitly yes and no respectively. Neither native record has a genome
  section. A bare type-strain field label on a rendered page must not
  override the actual value. The count two is a count of BacDive records.
- **Collection matching:** all carried deposits except `CGMCC AS 4.1381`
  and `ISP 5383` pass the pinned CAFI authority/full-accession matcher.
  Preserve those two source strings without treating them as eligible
  join keys or rewriting them to other aliases.
- **StrainInfo:** native rows 291955 and 23991, plus the live rich-record
  APIs for [389334](https://api.straininfo.dsmz.de/v2/data/strain/max/389334)
  and [35418](https://api.straininfo.dsmz.de/v2/data/strain/max/35418),
  support `10.60712/SI-ID389334.3` and `10.60712/SI-ID35418.2` and their
  archived version identities. Both records are published online.
  For 15330, the carried own deposits are ATCC25462/104144,
  IFO13050/104148, DSM40383/165409, CBS695.69/229323 and
  NBRC13050/486516. For 15331 they are DSM40818/166285 and
  ATCC11747/95879. All seven are available, with matching taxon and
  BacDive context. Source grouping alone does not transfer sequence links.
- **Nucleotide evidence:** live NCBI EFetch verifies all ten carried
  accessions and taxon 103232: AB184857.1 is NBRC13050 partial 16S;
  AY297025.1 is DSM40383 intergenic-spacer sequence; AY999840.1 is
  DSM40383 partial 16S; EF101632.1 is DSM40383 partial rpoB CDS;
  LC571066.1 through LC571071.1 are six NBRC13050 spacer/23S variants.
  The source's unversioned accessions are correctly retained as supplied.
  Each StrainInfo sequence explicitly names the same eligible own
  deposit. These gene/rRNA references are related records, not genomes.
  SI-ID35418 supplies no sequence list.
- **GOLD:** six organism IDs for 15330 are Go0032810, Go0603127,
  Go0603128, Go0603130, Go0603132 and Go0603133; each contributes
  separate culture-field and strain-field evidence. The three for 15331
  are Go0259605, Go0259606 and Go0259609. The last has only strain-field
  evidence for RIA77 and an empty culture field. All nine identities and
  the 17 field values were checked directly in
  `data/gold/organisms.jsonl.gz`. They remain organism references.
- **GTDB:** raw mapping row 1344 and a complete native cluster scan
  support closeMatch and count ten: nine members have NCBI taxon 103232,
  while GCF_000317595.1 has child taxon 698759. The native representative
  is RS_GCF_051122705.1, NRRL_B-12321, at
  `data/catalog/gtdb_genomes-0008.jsonl.gz:21454`. Species correspondence
  is supported, but the ten genomes are not ten genomes of either listed
  BacDive strain. The live GTDB tree was unavailable; the native catalog
  supplies the count and representative check.
- **Other attestations:** direct MediaDive count three agrees with raw
  row 100 and media 252, 65 and 84; GOLD count 30 agrees with row 421;
  Madin count three with row 606; BactoTraits count one with row 74.
  Units remain distinct. None establishes a taxon-wide phenotype or
  gathers records classified under the child strain taxon.
- **Carried publication:** Crossref metadata confirms
  [DOI 10.1099/00207713-30-1-225](https://api.crossref.org/works/10.1099/00207713-30-1-225)
  as the 1980 Approved Lists of Bacterial Names, volume 30(1), pages
  225-420. LPSN supports its nomenclatural use. The full historical list
  was not inspected; DOI metadata alone is not independent verification
  of its complete contents.
- **Structured adapter:** `kg-microbe-sources imodulondb datasets`
  returned 28 dataset keys but none for S. ipomoeae. iModulonDB is not
  applicable to the carried rpoB reference; no expression-module claim
  from another Streptomyces species was transferred.

## Completeness

The inspected Results section and Table 1 of
[Soares et al., DOI 10.1128/aem.00308-23](https://ttaxus.com/files/soares2023-streptomyces.pdf)
explicitly connect B12321 with ATCC25462 and identify its genome as
GCA_006547165.1. The paper's identity and accession table, rather than
similar names or species membership, establish this bounded connection.
Crossref independently confirms the article identity. Its November 2023
online date and December issue date are different bibliographic events.

Live [NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_006547165.1,GCF_006547165.1/dataset_report)
confirms the current paired accessions, B12321, taxon 103232, scaffold
assembly ASM654716v1, BioSample SAMN11109288 and BioProject PRJNA526936.
The deposited assembly has 10,892,772 bases. Native evidence includes:

| Source | Inspected chain |
| --- | --- |
| `data/catalog/ncbi_genbank-0005.jsonl.gz:24636` | GCA_006547165.1; strain=B12321; explicit GCF pair; SAMN11109288; PRJNA526936; latest. |
| `data/catalog/gtdb_genomes-0009.jsonl.gz:11220` | RS_GCF_006547165.1; explicit GenBank pair; B12321; same BioSample; source project PRJNA224116. |

The native sources do not label this assembly as type material. The
paper supplies the culture equivalence; do not invent a native annotation
or silently replace GTDB's project assertion with the submission project.

A separate inspected assembly, GCA/GCF_033793105.1, uses designation
NRRL_B-12321, SAMN33288068 and PRJNA934919. It is a distinct submission,
not an alias of GCA_006547165.1. Its appearance in the species cluster or
in the same StrainInfo group does not authorize adding it to either
BacDive strain. The later native representative GCF_051122705.1 is also
not silently substituted for the paper's assembly.

Complete gitignore-independent scans of relevant culture/strain fields
found no whole eligible carried-deposit match in 4,111,794 current and
historical NCBI assembly rows, 1,419,549 BV-BRC rows or 901,341 GTDB rows.
The complete GOLD culture-field scan found the eight exact matches above;
the ninth organism's RIA77 match is explicitly in its strain field.
These results explain the guarded output; they do not negate the paper.

Full link-table comparisons found 12 raw GOLD plus 20 SI assertions for
15330 and five raw GOLD plus four SI assertions for 15331, with no
assembly or genome-record assertions. Raw related rows are 190400-190411
and 190434-190438; SI related rows are 115898-115917 and 115943-115946.
Ignored-inclusive identifier/name/slug/BacDive searches found the seven
SI strain-link rows but no target SI assembly/exclusion or ATB
strain-link/exclusion row. There is no carried BIOSAMPLE assertion to
start an ATB join; the complete ATB catalog and sample FASTA eligibility
were not audited. No claim of absence from ATB is made.

Optional definitions, discussions and causal graphs are correctly empty.
Other culture aliases, source-group nucleotide accessions and phenotypes
are not mandatory additions. In particular, SI-ID389334 sequences assigned
only to NRRL B-12321 or CGMCC4.1381 are not own-deposit evidence for the
current carried deposit set.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - A literature-linked type-culture genome is missing from the strain
representation.** YAML lines 93-106 identify BacDive15330 and ATCC25462,
but no genome relationship follows. The inspected paper explicitly links
that culture to B12321 and GCA_006547165.1; current NCBI metadata and the
native catalog corroborate the assembly and sample. This is consequential
for the repository's strain-to-genome discovery use case.

The current matcher is not incorrectly rejecting a valid own-deposit
token: the genome metadata carry B12321, and the guarded link inventories
are empty too. The maintained owner is explicit source strain-genome
evidence consumed through `src/taxonmech/extract.py:799` and its
source-specific importers into `data/raw/strain_assemblies.tsv`,
`strain_genome_records.tsv` and `strain_related_records.tsv`.
`src/taxonmech/seed.py:518` emits those inventoried assertions.
Prefer provenance-backed enrichment of BacDive15330 or the same eligible
own deposit's sequence evidence. A local literature-curation route needs
a separately authorized maintained input and evidence contract. Do not
patch generated YAML or weaken `normalize_culture_identifier` to match
bare strain names, aliases, substrings or every genome of the species.

## Recommended Edits

1. Resolve M1 through maintained evidence acquisition, retaining the
   paper's explicit ATCC25462/B12321 connection and its exact assembly
   accession together with the NCBI pair, sample and project provenance.
2. After authorized source curation, refresh the relevant pinned source,
   regenerate guarded link inventories and seed the target. Add other
   database identifiers only when their own explicit source chain passes
   the same deposit and identity checks. Do not transfer whole SI groups
   or produce sample/genome Cartesian products.
3. Preserve supported identity, lineage, synonym scopes, nomenclature,
   strain classification, typed related records and source counts.
   Keep lifecycle status `SEEDED`; this review does not promote status or
   authorize a curation event.

## Follow-up Checks

- Require inspected deposit-to-assembly evidence in the maintained
  source. Test that AE-419, 91-03, 78-51, 88-35, similar collection
  numbers and unowned SI deposits remain separate.
- After authorization, use `just extract-inventory-dry`, `just seed` and
  `just seed-canary NCBITaxon:103232`. Inspect generated provenance, run
  both focused validators, then `just verify-corpus` and `just qc` for
  a publishable curation change.
- Assess ATB only after an eligible whole BioSample assertion exists;
  verify FASTA availability and preserve same-source-chain crosslinks.
  Additional GOLD project/analysis chains and newer NRRL submissions need
  their own evidence before they can add further genome relationships.
- Recheck unavailable browser pages and the complete Approved Lists only
  if needed for later nomenclatural work. They do not block the supported
  identity or the separately evidenced completeness finding.

## Additional Notes

NCBI's taxonomy browser, live GTDB tree and rendered SI pages were
unavailable through the web reader. NCBI structured taxonomy/assembly
APIs and both StrainInfo rich-record APIs succeeded. Europe PMC XML
returned HTTP 500 and PMC presented a challenge; the relevant primary
paper text and table were inspected in the author's hosted article PDF.
No paper phenotype, gene function or pathway assertion was generalized
to the species or imported into the YAML.

All absence findings above use complete explicit scans or
`rg --no-ignore --hidden -z`, including ignored files. Broader numeric and
epithet matches were discovery leads only: unrelated Phytoplasma and
Saccharopolyspora entries do not count as this species. No complete
GOLD project/analysis reconciliation or ATB source census is claimed.
Public free sources only were used. Older reports, generated records
and completed Eukaryota coverage were left untouched.
