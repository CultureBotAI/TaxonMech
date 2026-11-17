# YAML Record Review: Pseudonocardia tetrahydrofuranoxydans

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudonocardia_tetrahydrofuranoxydans.yaml`
- Started UTC: 2026-10-03T13:30:38Z
- Finished UTC: 2026-10-03T13:37:41Z
- Verdict: pass

## Target

- Class: `TaxonRecord`; identifier `NCBITaxon:102884`; rank `SPECIES`;
  domain `BACTERIA`; parent `NCBITaxon:1847` (Pseudonocardia).
- Read all 720 YAML lines. Grounding is `EXACT`; mapping status is `SEEDED`.
- Generated record owned by maintained inventories and `src/taxonmech/seed.py`,
  not a hand-curated YAML. No record, source, history, or status was changed.
- The species includes one BacDive strain, K1 (`bacdive:13395`), classified
  under descendant `NCBITaxon:1303679` (JCM 14745), with four culture deposits.
- Reviewed all seven assembly assertions, six other genome assertions, and
  32 related-record assertions, including their source and deposit provenance.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudonocardia_tetrahydrofuranoxydans.yaml`:
  PASS; no schema issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudonocardia_tetrahydrofuranoxydans.yaml`:
  PASS; one file, zero errors. This command may update the standard ignored
  `reports/instance_validation_failures.tsv` diagnostic.
- Structured taxonomy checks: PASS for identity, rank, parent, genetic code,
  all nine ancestors, both native NCBI name classes, and the BacDive subtree.
- Structured multiset comparisons: PASS for all 45 link assertions against
  maintained inputs, including parsed StrainInfo evidence objects and all
  populated fields, rather than accession-only comparisons.
- Culture-identifier checks used the repository's normalization and
  `culture_curie_key` helpers with its pinned collection vocabulary: PASS for
  all four deposits and each asserted source-field match.
- StrainInfo native-object checks: PASS for eligible deposits, strain identity,
  availability, nondeprecated collections, nonerroneous relations, and exact
  sequence-to-deposit links.
- `just verify-corpus`: Not checked; this is a full-corpus regeneration check,
  not a documented focused validator. No corpus-wide reproducibility claim.
- Standalone history validation: not applicable to a separate history file;
  none was found in the bounded ignored-inclusive search described below.
  The embedded seed event passed strict validation.
- Graph-specific checks: not applicable; this record asserts no causal graph.
  Rendered pages, exports, and global product validation were not audited.

## Identity and Grounding

The raw NCBI taxonomy inventory identifies species 102884 and its only
descendant, JCM 14745 (1303679). The reconstructed subtree is exactly those
two identifiers. All nine lineage nodes and genetic code 11 agree with the
record. The live [NCBI species page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=102884&lvl=&mode=node)
and [strain page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1303679)
support this species/strain distinction.

The two related synonyms preserve the native NCBI `includes` and `authority`
names. Neither is incorrectly promoted to an exact synonym. Native name
objects were inspected in `data/catalog/ncbi_names-0000.jsonl.gz` at lines
38158-38160 and the child object in `ncbi_names-0007.jsonl.gz` at line 30641.

[LPSN](https://lpsn.dsmz.de/species/pseudonocardia-tetrahydrofuranoxydans)
supports name record 780187, the 2006 authority, valid publication and correct
name status, the three listed type deposits, and AJ249200. Its name crosswalk
remains `skos:closeMatch`; this does not contradict exact NCBI identity.
The serialized `legitimate=True` status prefix comes from the maintained
inventory, not a quotation attributed to the live page.

## Evidence

Maintained inventory support was inspected at these locations:

| Input | Relevant row or lines | Verified scope |
| --- | --- | --- |
| `data/raw/ncbitaxon_taxa.tsv` | 18155, 308105 | Species and child identity |
| `data/raw/lpsn_names.tsv` | 19399 | Nomenclature, types, citations, sequence |
| `data/raw/bacdive_strains.tsv` | 13232 | K1, four deposits, child taxon, type flag |
| `data/raw/gold_organisms.tsv` | 355 | Two species-direct organisms |
| `data/raw/madin_taxa.tsv` | 540 | Fifteen direct trait assertions |
| `curation/seed_scope.tsv` | 23616 | Species scope and original admission reason |
| `data/raw/strain_assemblies.tsv` | 33267-33272 | Six source assembly assertions |
| `data/straininfo/assemblies.tsv` | 2543 | One deposit-scoped assembly assertion |
| `data/raw/strain_genome_records.tsv` | 26129-26134 | Six IMG/BV-BRC assertions |
| `data/raw/strain_related_records.tsv` | 89343-89362 | Twenty source relationships |
| `data/straininfo/related_records.tsv.gz` | 38424-38435 | Twelve StrainInfo relationships |

The complete native BacDive object at `data/bacdive/records.jsonl.gz:13231`
and the live [BacDive record](https://bacdive.dsmz.de/strain/13395) agree on K1,
the four deposits, and species/strain identifiers. Native reference 66792
supports the unversioned assembly, IMG, and BV-BRC identifiers; reference
11614 supports deposit provenance. These are source associations, not four
independent biological strains.

The native current GenBank object at
`data/catalog/ncbi_genbank-0000.jsonl.gz:49276` identifies
`GCA_001313405.1`, ASM131340v1, JCM 14745, taxon 1303679,
`PRJDB936`, `SAMD00016936`, and WGS accession `BBFU00000000.1`.
It is a contig-level assembly with 1,947 contigs and a fragmented-assembly
RefSeq exclusion. The YAML does not claim completeness or high genome quality.
The original external snapshot download was not reread; its configured
reference was checked against `conf/ncbi_assemblies.yaml` and
`data/raw/MANIFEST.yaml`, and the native catalog projection was inspected.

The complete BV-BRC object at `data/bvbrc/bvbrc-0001.jsonl.gz:23804`
supports genome `1303679.3`, the versioned assembly, project, and sample.
Both `strain` and `culture_collection` matches are preserved. `JCM: 14745`
normalizes to the existing JCM deposit, without inventing an alias.

Native GOLD objects establish these exact paths:

- `Go0094255` at `data/gold/organisms.jsonl.gz:55145` identifies JCM 14745.
  `Gp0094255` at `projects.jsonl.gz:55650` links that organism to the project
  and sample. `Ga0128428` at `analyses.jsonl.gz:74790` links that project to
  the assembly and `img.taxon:2734481945`.
- `Go0028501` at `organisms.jsonl.gz:24231` identifies DSM 44239;
  `Go0608774` at `organisms.jsonl.gz:439742` identifies CIP 109050.
  Their assertions remain organism relationships. They do not inherit the
  JCM assembly through an unsupported GOLD chain.
- Both organism culture-collection and strain fields support their respective
  assertions. A blank analysis-level organism field is not a contradictory
  organism assignment; the explicit project-to-organism chain was checked.

The inspected [NCBI BioProject result](https://www.ncbi.nlm.nih.gov/bioproject/?term=txid1303679%5BOrganism:noexp%5D)
independently connected PRJDB936 (NCBI project 245957) with the JCM strain,
assembly, sample, GOLD project, and IMG identifier. Subsequent attempts to
open the canonical project and a separate BioSample page failed in the web
tool. No separate live BioSample attribute verification is claimed; the
complete native source records above support the asserted sample links.

The complete StrainInfo object at `data/straininfo/records.jsonl.gz:79230`
identifies SI-ID113658, BacDive 13395, and record version
`DOI:10.60712/SI-ID113658.3`. Its four eligible deposits are DSM 340748,
CIP 690288, CCUG 703098, and JCM 792172. The JCM assembly is linked only
through deposit 792172. The four partial-gene sequences are linked only
through DSM deposit 340748. Each `sequence_deposit_id` agrees with its
matched deposit; none is spread across all four deposits.

[DataCite metadata](https://api.datacite.org/dois/10.60712/si-id113658.3)
verified the findable StrainInfo version-3 DOI and its strain landing URL.
The live StrainInfo page exposed only its JavaScript shell; the complete
pinned record, not that shell, supported deposit-level checks.

Official [NCBI nucleotide EFetch XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AJ249200,EU722544,EU722578,EU722600,EU722633&rettype=gb&retmode=xml)
was fetched and parsed for all five cited sequence accessions:

| Accession returned | Source strain | Sequence identity | Length |
| --- | --- | --- | --- |
| AJ249200.1 | K1 | 16S ribosomal RNA | 1440 bp |
| EU722544.1 | DSM 44239 | fusA, partial CDS | 783 bp |
| EU722578.1 | DSM 44239 | gyrB, partial CDS | 1229 bp |
| EU722600.1 | DSM 44239 | lepA, partial CDS | 966 bp |
| EU722633.1 | DSM 44239 | rpoB, partial CDS | 798 bp |

All five source features identify taxon 102884. The versions returned by the
API verify resolution; they do not justify rewriting source assertions that
intentionally preserve unversioned identifiers. Sequence annotations support
the link labels, not experimental phenotype or regulatory claims.

The [original publication abstract](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.64199-0)
and official [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=16825626&retmode=xml)
verify PMID 16825626, DOI 10.1099/ijs.0.64199-0, the species description,
and K1 type equivalence with DSM 44239 and CIP 109050.
[Crossref metadata](https://api.crossref.org/works/10.1099%2Fijs.0.64719-0)
verifies the separate notification DOI, volume 56, issue 10, pages 2251-2252,
published October 2006. Its notification body and the original full paper
were not reviewed. Their distinct bibliographic roles were retained.

## Completeness

- The one-strain count matches all BacDive inventory rows in the complete
  target subtree. The descendant classification is retained explicitly.
- Source counts have the correct units: one NCBI name, one LPSN name,
  one BacDive strain, two species-direct GOLD organisms, and fifteen direct
  Madin trait assertions. The child-classified GOLD organism is not silently
  added to the species-direct count.
- Seven assembly assertions are multiple provenance paths to two accession
  strings, not seven distinct assemblies. Six other genome assertions refer
  to two distinct database identifiers, not six distinct genomes.
- Optional phenotype, graph, medium count, GTDB, and ATB slots were not
  populated speculatively. The raw BacDive medium count is zero; live culture
  information alone does not establish a missing maintained aggregate.
- Ignored and hidden files were included in bounded compressed-source searches
  of `data/catalog/`, `data/bvbrc/`, and `data/gold/`, using the species name,
  assembly/sample identifiers, and all four culture identifiers. No additional
  matching native RefSeq or GTDB object was found within that search scope.
- Ignored-inclusive searches of `history/`, `data/atb/`, and the compressed
  AllTheBacteria catalog found no matching standalone history or ATB overlap
  for the target identifiers/name/slug, BacDive ID, assembly, or sample.
- Ignored-inclusive target/child searches of raw MediaDive and BactoTraits
  inventories found no matching rows. These are bounded inventory results,
  not claims that no biological evidence exists elsewhere.
- iModulonDB was not applicable. The local claw runner was resolved and its
  `imodulondb datasets` command attempted; sandbox DNS prevented that call.
  An approved read-only request to the official
  [datasets API](https://imodulondb.org/api/datasets) succeeded and its complete
  20-organism listing contained no Pseudonocardia dataset. This is not negative
  evidence about the genes or phenotype.

## Findings

None found: 0 blocker, 0 major, 0 minor findings within the reviewed scope.
The live-page and full-corpus limitations above do not demonstrate a record
defect. This pass is not a genome-quality endorsement or a full-corpus audit.

## Recommended Edits

None required. Preserve independent source-field assertions, source accession
versions, descendant classification, and deposit-specific sequence provenance.
Any later source correction belongs in the maintained `data/raw/` inventories
or `data/straininfo/` input and its owning transform, with record generation
through `src/taxonmech/seed.py`; do not patch this generated YAML directly.

## Follow-up Checks

- For future source refreshes, rerun both focused validators and the exact
  structured link/deposit checks, especially JCM assembly versus DSM genes.
- Run `just verify-corpus` before claiming corpus-wide reproducibility.
- A future detailed assembly-quality review should consult current assembly
  metadata; fragmented assembly is contextual evidence, not an identity error.
- Separate live BioSample attributes, notification full text, and rendered
  products remain outside this completed record-level verification.

## Additional Notes

The seed event's four-source admission reason is historical scope text;
the present five attestations include the descendant BacDive aggregation.
This does not establish an incorrect source count or a missing history event.
No curation event, review-status promotion, source refresh, regeneration,
GitHub action, or taxon YAML edit was performed.
