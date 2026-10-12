# YAML Record Review: Campylobacter californiensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_californiensis.yaml`
- Started UTC: 2026-10-03T21:42:35Z
- Finished UTC: 2026-10-03T21:45:32Z
- Verdict: needs curation

## Target

Read all 152 lines of the generated `TaxonRecord`, `NCBITaxon:1032243`,
Campylobacter californiensis, rank `SPECIES`, domain `BACTERIA`, grounding
`EXACT`, mapping status `SEEDED`. The species record lists one BacDive
strain, RM 6914, with CCUG 75329 and LMG 32304 and a true type-strain flag.
Its assembly, genome-record and related-record lists are absent.

This is a read-only review. No generated YAML, maintained source, scope,
history, status or older report was changed. The finding concerns missing
representation of independently documented strain-genome evidence, not a
wrong species identity or permission to broaden automatic joins.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/campylobacter_californiensis.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/campylobacter_californiensis.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured source comparisons | Backbone, complete lineage, scope, path and source attestations agree with the committed inventories. |
| Full-field strain-link comparisons | Zero assemblies, zero non-ATB genome records and zero related records match the complete raw and StrainInfo link-table scans for this strain. |
| Embedded history | Strict validation passed; the six-source seed event and preserved scope reason agree. |
| Standalone history | Not applicable: identifier, label and slug searches under `history/`, including ignored and hidden files, found no target entry. |
| Graph and ontology-product gates | Not applicable: the complete YAML contains no causal graph or curator-added ontology-product assertions. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports, sequence alignment and FASTA checksum
replay. Focused inventory comparisons are not corpus reproduction. No
generator or history writer was run. Passing validators do not establish
biological completeness.

## Identity and Grounding

The identifier, name, parent `NCBITaxon:194`, genetic code 11 and all nine
root-first lineage entries match `data/raw/ncbitaxon_taxa.tsv:220801` and
live NCBI EFetch/[taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032243).
Native names in `data/catalog/ncbi_names-0005.jsonl.gz` rows 30073-30083
preserve the scientific name, one authority and nine `includes` names.
The latter ten are correctly represented as related synonyms, not exact
strain equivalences. A complete backbone scan found no children.

The path at `data/taxa/PATHS.tsv:13163` and scope at
`curation/seed_scope.tsv:10794` agree. Eight source redirects into this
species are retained in `data/raw/ncbi_merged_ids.tsv`, rows 25108-25110
and 50016-50020. They do not imply that all included isolates are RM6914.

[LPSN name 54098](https://lpsn.dsmz.de/species/campylobacter-californiensis)
corroborates Miller et al. 2024, species rank, valid publication and
correct-name status. Its linked collection deposits match the two carried
type designations; RM 6914 is also named on the page.
`data/raw/lpsn_names.tsv:8684` supports the complete carried nomenclatural
object, including status booleans, the two DOIs, PMID and marker accession.
Both culture identifiers pass the pinned CAFI authority/template matcher.

## Evidence

- **BacDive:** `data/raw/bacdive_strains.tsv:98402`, native
  `data/bacdive/records.jsonl.gz:98401` and the inspected
  [BacDive 176171 page](https://bacdive.dsmz.de/strain/176171) agree on
  taxon 1032243, designation RM 6914 and both deposits. Their intersection
  with LPSN's type-designation set supports `is_type_strain: true`.
  The native source has a 16S sequence but no genome section. Its
  Pseudomonadota source hierarchy does not replace NCBI's carried lineage.
- **Type material:** NCBI type-material inventory rows 1583-1594 retain
  the deposit variants and RM6914; culture-inventory rows 35615 and 128266
  place CCUG-75329 and LMG-32304 under this taxon. These corroborate
  identity but are not themselves assembly assertions.
- **Original publication:** NCBI PubMed EFetch confirms that PMID:39374062
  identifies DOI:10.1099/ijsem.0.006524 and PMC11457942. The publisher
  abstract and relevant sections of the
  [open full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11457942/fullTextXML)
  were inspected. The species description explicitly equates RM6914 with
  LMG 32304 and CCUG 75329 and identifies CP012545 as its genome sequence.
  The genome section reports a complete type-strain chromosome, separately
  from eight other draft genomes. This is explicit evidence for this
  strain, not a shared-name inference.
- **Notification citation:** DOI:10.1099/ijsem.0.006588 resolves to the
  [Oren and Goker notification list](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.006588).
  The [publisher-deposited DOI metadata](https://api.crossref.org/works/10.1099/ijsem.0.006588)
  confirms its title, authors, volume 75, issue 1 and January 31, 2025
  publication. This later notification does not change the species
  authority year from 2024. The complete notification table was not
  inspected and is not independently relied on for the strain identity.
- **Marker:** Live NCBI Nuccore confirms MW131429.1 as a 1,499-base partial
  16S rRNA sequence from RM6914, taxon 1032243, with type-material
  annotation. The unversioned `INSDC:MW131429` correctly preserves the
  LPSN-supplied accession and is not counted as a genome.
- **Collection:** The inspected
  [CCUG 75329 page](https://www.ccug.se/strain?id=75329) independently lists
  RM6914 and LMG 32304 as other designations. Additional marker references
  MW139784 and MW139842 are source-page follow-up leads only; they were
  not independently revalidated in this review.
- **GTDB:** `data/raw/gtdb_mappings.tsv:1343` and
  `data/raw/gtdb_species.tsv:40279` support the closeMatch and count ten.
  A complete native cluster scan found ten members: nine with NCBI taxon
  1032243 and one, GCF_014892335.1, with taxon 2735741, Campylobacter sp.
  7477a. The representative is RM6914's GCF_004803835.1, in native shard
  0003 row 11750. The named species and its type representative support
  the species-level correspondence here. Ten means the whole GTDB
  cluster, not ten NCBI-1032243 assemblies or ten type-strain genomes.
  Preserve the different source taxonomies; do not infer that 7477a is
  RM6914 or revise NCBI's lineage. The live GTDB tree page was unavailable;
  the complete native catalog supplied the count check.
- **Other counts:** GOLD count nine matches
  `data/raw/gold_organisms.tsv:420`; nine native organism rows carry this
  taxon, with different RM strain designations. Madin count four matches
  `data/raw/madin_taxa.tsv:605`. These are source organism and trait-assertion
  counts, not genome links or phenotype claims for the type strain.
  Complete corresponding raw-table scans found no MediaDive or BactoTraits
  attestation. The single uncapped BacDive entry is complete for the
  committed inventory and childless species.
- **Structured adapter:** `kg-microbe-sources imodulondb datasets` returned
  28 keys, none for Campylobacter. iModulonDB is not applicable; no other
  organism's expression-module evidence was transferred, and absence from
  that resource is not negative biological evidence.

## Completeness

The published RM6914 genome is present in independent primary-source
metadata but lacks an eligible automatic match to a carried culture deposit:

| Native source | Inspected identity chain |
| --- | --- |
| `data/catalog/ncbi_genbank-0003.jsonl.gz:39949` | GCA_004803835.1; RM6914; complete type-material assembly; SAMN03737965; PRJNA66813. |
| `data/catalog/ncbi_refseq-0002.jsonl.gz:18499` | Paired GCF_004803835.1; RM6914; same BioSample; native project PRJNA224116. |
| `data/catalog/gtdb_genomes-0003.jsonl.gz:11750` | RS_GCF_004803835.1; explicit GenBank pair; strain RM6914; same BioSample; native project PRJNA224116. |
| `data/bvbrc/bvbrc-0000.jsonl.gz:3155` | patric:1032243.3 explicitly connects GCA_004803835.1, CP012545, SAMN03737965 and PRJNA66813; strain RM6914, no culture-collection field. |
| GOLD organism/project/analysis | Go0011836 at organism row 10414 has RM6914 but an empty culture field. Gp0011836 at project row 10272 explicitly connects that organism, sample and project. Ga0693765 at analysis row 458670 follows Gp0011836 and connects CP012545 to GCA_004803835.1; IMG taxon ID is empty. |

Live [NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_004803835.1,GCF_004803835.1/dataset_report)
confirms both current paired accessions, assembly ASM480383v1, complete
genome level, RM6914, taxon 1032243 and the sample/project above. Nuccore
confirms CP012545.1 as a 1,782,759-base complete genome with RM6914,
type-material annotation, SAMN03737965 and PRJNA66813. Component sequence,
assembly, sample and project identities must remain distinct. The native
RefSeq/GTDB project differs from the original submission project; retain
each source's assertion rather than normalizing them silently.

Complete gitignore-independent scans found no whole CAFI-valid match for
CCUG-75329 or LMG-32304 in the relevant culture/strain fields of 4,111,794
current/historical NCBI assembly rows, 1,419,549 BV-BRC rows, 901,341 GTDB
rows and 531,961 GOLD organism rows. A full scan of 314,470 native
StrainInfo records found neither own deposit nor taxon 1032243. Exact
SI-ID284452 search also found no native record, and its live rich-record
API returned HTTP 404. That BacDive cross-reference is not carried in the
YAML and would not itself authorize a join.

Full raw/StrainInfo link-table scans agree with the empty YAML link sets.
Ignored-inclusive searches by target identifier, label, slug, BacDive ID
and deposits found no target SI/ATB strain-link or exclusion row. This
does not claim that the sample is absent from the complete ATB catalog:
there is currently no eligible BIOSAMPLE assertion on the listed strain
to start that join, and native ATB sample eligibility was not assessed.

Optional definitions, general evidence, discussions and causal graphs
are correctly absent. Other isolates and the paper's phenotype tests are
not mandatory strain entries or taxon-wide phenotype assertions. The
additional GTDB isolate and eight other GOLD RM strains must remain
separate from the type strain.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - An explicitly documented type-strain genome is missing from the
record's strain representation.** YAML lines 103-111 identify RM 6914 and
both type deposits but carry no genome relationship. The inspected paper
explicitly links those deposits to RM6914 and CP012545, while NCBI and
the native source chains identify the paired GCA/GCF_004803835.1 assembly.
That is a consequential completeness gap for strain-to-genome discovery.

It is not an erroneous rejection by the existing whole-deposit matcher:
the genome sources supply the bare RM6914 designation, and the guarded
inventories are empty too. The maintained owner is explicit source
strain-genome evidence consumed through `src/taxonmech/extract.py:799`
and its source-specific importers into `data/raw/strain_assemblies.tsv`,
`strain_genome_records.tsv` and `strain_related_records.tsv`.
`src/taxonmech/seed.py:519` only emits those inventoried assertions.
Prefer upstream BacDive 176171 or own-deposit source enrichment with
explicit provenance; a local literature-curation alternative requires a
separately authorized maintained input and evidence contract. Do not
hand-edit YAML or weaken `normalize_culture_identifier` to join bare RM
names, all species members or culture-number substrings.

## Recommended Edits

1. Resolve M1 through maintained evidence acquisition, preserving the
   paper's RM6914/LMG32304/CCUG75329 identity and CP012545 reference,
   together with NCBI's assembly relationship. An explicit assembly entry
   on BacDive or the same eligible own culture deposit can supply the
   missing relationship without weakening automatic matching.
2. After authorized source curation, refresh the appropriate pinned source
   and extraction inputs, then regenerate the link inventories and target
   YAML. Carry each additional database identifier only with its own
   explicit chain. Keep source versions and project differences intact;
   the evidence table is not permission for Cartesian-product joins.
3. Preserve the correct species identity, lineage, synonym scopes,
   nomenclature, type flag, source counts and `SEEDED` lifecycle status.
   No status promotion or curation event follows from this read-only review.

## Follow-up Checks

- Require inspected, explicit deposit-to-assembly provenance in the
  maintained input. Test that RM6913, RM6883, 7477a, unrelated collection
  accessions and other deposits remain unjoined.
- After authorization, use extraction dry run, `just seed` and
  `just seed-canary NCBITaxon:1032243`; inspect the actual generated
  provenance. Run both focused validators above, then `just verify-corpus`
  and `just qc` for a publishable curation change.
- If an eligible BIOSAMPLE assertion is added, assess ATB eligibility by
  the whole accession and retain same-source-chain evidence for crosslinks.
  No current ATB availability or equivalence claim is made here.
- Recheck the unavailable SI-ID284452 source reference and full
  notification table as bounded source follow-ups, without inventing
  missing source records or treating a BacDive cross-reference as a join.

## Additional Notes

The type identity, genomic characterization, species description and
accession disclosure were inspected in openly available full-text XML;
supplementary files were not downloaded or needed for M1. The species
paper and notification DOI are distinct references. The PMID-to-DOI match
was taken from the article's own identifiers, not its reference list.

All absence checks used explicit complete scans or
`rg --no-ignore --hidden -z`, including ignored files. Broad epithet and
numeric search hits were only leads; unrelated genera and culture numbers
were excluded using full identities. Searches under `curation/` found
only the existing scope and legacy page-path rows for this target.
Source access was public and free. Prior reports, generated records and
completed Eukaryota coverage were left untouched.
