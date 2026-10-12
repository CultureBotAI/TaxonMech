# YAML Record Review: Echinicola shivajiensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/echinicola_shivajiensis.yaml`
- Started UTC: 2026-10-07T13:54:42Z
- Finished UTC: 2026-10-07T14:02:06Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035916`,
Echinicola shivajiensis. Identity is `EXACT`, lifecycle `SEEDED`,
rank `SPECIES`, domain `BACTERIA`, genetic code 11. It carries
11 ancestors, two related synonyms, one GTDB close mapping/xref,
one BacDive strain (AK12), one BacDive assembly assertion, one
BV-BRC genome assertion, two StrainInfo related records, three
source attestations, and one inline seed event.

It has no nomenclature object, explicit type-strain flag, record-level
literature evidence, definition, or causal graph. Seeded fields are
generated and read-only; recommendations below concern maintained
upstream inputs and transforms.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/echinicola_shivajiensis.yaml`: passed, no LinkML issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/echinicola_shivajiensis.yaml --out /private/tmp/ech-shivajiensis-strict.tsv`: passed, one file, zero errors; complete header-only diagnostics read.
- Bounded parsed-source comparisons passed for identity, lineage, source/scope wording, and path. Complete raw rows were compared with synonyms, counts, strain designation, deposits, and GTDB mapping.
- Additional all-field comparisons passed for the assembly, genome record, and both related records against raw/StrainInfo inventories. The repository's CAFI normalizers confirm the exact JCM 17847 own-deposit match. This is a diagnostic comparison, not a replacement corpus-reproduction validator.
- Live NCBI, BacDive, LPSN, JCM, BV-BRC, StrainInfo, DataCite, and SeqCode evidence was inspected. GTDB live pages were inaccessible; an attempted genome API route returned 404 and API-schema discovery returned 403. GTDB checks therefore rely on the pinned species, mapping, and native genome rows, not a verified current live release.
- Upstream LPSN and MediaDive KGX files could not be opened at the paths configured by `conf/sources.yaml`; `data/source_snapshots` was likewise unavailable. Thus the original MediaDive edge behind `medium_count: 1` was not independently replayed. The count matches the committed strain inventory.
- The DSMZ catalog page returned 502; the original paper's publisher page was inaccessible. JCM/BacDive deposits and the full PubMed abstract were available. No full-text claim is made.
- `just validate-products`: not applicable; no curated graph grounding/label pairs. Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target history artifact. Inline history passed schema/strict and source comparisons.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, or the test suite. No corpus-wide acceptance claim is made.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035916&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035916)
confirm the active identifier, label, species rank, code 11, and
parent Echinicola (`NCBITaxon:390846`). All 11 local ancestor IDs,
labels, and ranks agree with the pinned backbone and live chain,
with root supplied by Datasets. NCBI lineage remains authoritative
for this field; GTDB's Bacteroidia classification does not replace
NCBI's Cytophagia.

Complete local rows are at `data/raw/ncbitaxon_taxa.tsv:222215`,
`data/taxa/PATHS.tsv:14714`, and
`curation/seed_scope.tsv:30319`. The scope row dates from
2026-09-12; the taxonomic snapshot is 2026-09-13. The distinct
dates are not contradictory.

The two NCBI related synonyms retain the authority string and
the included name Echinicola sp. AK12; they are not claimed as
exact synonyms. Full native name rows at
`data/catalog/ncbi_names-0005.jsonl.gz:31721`,
`:31722`, and `:31723` agree. No target child, merged-ID,
or dropped row was found by parsed inventory checks.

Fresh [LPSN](https://lpsn.dsmz.de/species/echinicola-shivajiensis)
page text confirms record 795859, status "not validly published",
and "preferred name (not correct name)". Its proposed type is
AK12, JCM 17847, MTCC 11083. These distinctions are absent from
the YAML's nomenclature layer; see the minor finding. NCBI identity
does not assert ICNP valid publication.

## Evidence

The GTDB mapping and xref match
`data/raw/gtdb_mappings.tsv:1446` and
`data/raw/gtdb_species.tsv:57274`: one genome, closeMatch.
The complete native row
`data/catalog/gtdb_genomes-0015.jsonl.gz:51` identifies
`RS_GCF_018642165.1` as the representative of
`s__Echinicola shivajiensis`, NCBI taxid 1035916.
The one-genome species count does not mean every strain has an
independently supported GTDB genome link.

The complete BacDive identity row
`data/raw/bacdive_strains.tsv:62691` supports AK12,
DSM 24933, JCM 17847, MTCC 11083, and one imported medium.
There are no descendant taxa to add further BacDive strains.
[BacDive 140406](https://bacdive.dsmz.de/strain/140406)
confirms these deposit identities and taxon; the full pinned native
record at `data/bacdive/records.jsonl.gz:62690` was read.
The [JCM catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=17847)
explicitly traces JCM 17847 to Anil Kumar AK12 and MTCC 11083.

BacDive reference 66792 directly supplies unversioned
`GCA_018642165` and `1035916.4` with contig-level scope.
The YAML retains source fields, reference, description, and
taxon without adding an unsupported accession version.
All fields match `data/raw/strain_assemblies.tsv:45295`
and `data/raw/strain_genome_records.tsv:35514`.

The [NCBI genome report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_018642165.1/dataset_report)
resolves the current GenBank assembly to GCA_018642165.1, explicitly
paired with GCF_018642165.1, strain AK12, 34 contigs, BioSample
SAMN19429923, and BioProject PRJNA733650.
The [BV-BRC record](https://www.bv-brc.org/api/genome/1035916.4)
independently names the same taxon/strain, versioned GenBank assembly,
sample, and project. Their local complete records also agree.
The source-supplied unversioned BacDive assertion remains valid as
provenance; a newly added paired RefSeq or GTDB link would need its
own explicit source chain, not a prefix rewrite.

GTDB and primary assembly metadata supply only the bare designation
AK12, not a matched culture-deposit identifier. Under the documented
CAFI rules they cannot independently create cross-source deposit
joins. The existing BacDive assertion is direct, so it does not
depend on that matcher.

The complete
`data/straininfo/records.jsonl.gz:289787`,
`strain_links.tsv:27429`, and
`related_records.tsv.gz:66105`/`:66106`
support JCM 17847 as SI-DP873947 in SI-ID377731.
The [live StrainInfo API](https://api.straininfo.dsmz.de/v2/data/strain/max/377731)
agrees on the deposit, available status, published-online strain
record, BacDive cross-reference, and DOI.
[DataCite](https://api.datacite.org/dois/10.60712/SI-ID377731.2)
confirms version 2 as a StrainInfo dataset DOI, not a paper or genome.
No source sequence object is supplied for this deposit; exact local
StrainInfo assembly and ATB strain/genome-link scans returned none.

LMG 26481 is another deposit within that StrainInfo group, but it
does not occur in this BacDive deposit inventory. The JCM deposit
match does not authorize adding every other group member.

Attestation units remain separate: NCBITAXON one NAME, GTDB one
GENOME, BACDIVE one STRAIN. No LPSN, GOLD, MediaDive taxon-level,
Madin, or BactoTraits attestation row was found for this exact taxon.
A strain's medium count does not require a separate taxon-level
MediaDive attestation. The seed event's wording matches the source
set/scope and its timestamp is the newest raw/ATB/StrainInfo
manifest extraction time, as `_seed_timestamp` specifies.

## Completeness

The present identity and imported strain/genome/StrainInfo assertions
are supported. Missing optional phenotype, causal-graph, and
transcriptomic fields are not defects. iModulonDB is not applicable
to these identity and deposit-link claims.

Exact NCBI searches returned one Assembly UID (10182151) and 39
Nuccore UIDs. Four Nuccore records were inspected in full metadata,
features, and references, excluding sequence payloads:

- `JAHHZM000000000.1`: the AK12 WGS master, explicitly describing 34 component sequences. It supports project context, not 34 additional assemblies.
- `FR870465.1` and `NR_132601.1`: 1,409-nt AK12 type-strain 16S markers; RefSeq explicitly identifies the underlying FR870465 sequence.
- `MF796610.1`: a 1,298-nt 16S marker for distinct strain s118b from Peru. It does not identify AK12 or supply another BacDive strain.

The remaining Nuccore records and their feature annotations were not
individually reviewed; no whole-sequence or functional quality claim
is made. The original [species-description abstract](https://pubmed.ncbi.nlm.nih.gov/22105533/)
verifies DOI 10.1007/s10482-011-9679-6 and the AK12/JCM/MTCC
proposed-type equivalence. The later s118b sequence's
[publication metadata and abstract](https://pubmed.ncbi.nlm.nih.gov/29023396/)
verify DOI 10.3390/md15100308; experimental outcomes are not
transferred to AK12 or the species. Literature remains optional.

Initial and final expanded local searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`. Ignored, hidden, and compressed
content was included. Terms covered taxon ID, label/slug, old name,
culture deposits, source identifiers, markers, publication, sample,
project, and assembly accessions. Both final search sets contain
the same 32 rows; all were read in full. Five native `SOURCE.json`
files were separately parsed and history filenames checked.
No target LPSN inventory row or standalone history artifact was found.

Two rows are numeric collisions: GOLD analysis
`data/gold/analyses.jsonl.gz:437386` concerns Salmonella
and matches IMG 8103591682; assembly
`data/catalog/ncbi_genbank-0009.jsonl.gz:6784`
is Campylobacter upsaliensis AG20-0004, taxid 28080,
with accession GCA_010359165.1. Neither supports this taxon.

The native SeqCode row at `data/seqcode/names.jsonl.gz:34922`
resolves to [entry 36809](https://api.seqco.de/v1/names/36809.json),
an automated-discovery name with unknown nomenclatural type,
not an independently validated name or genome-backed mapping.

An intermediate search used short bare numeric name IDs and returned
12,324 mostly ambiguous candidate addresses. It was not used as
record-level evidence or an absence proof; the final expanded search
uses namespace/field-qualified IDs and descriptive identifiers.
The bounded local searches are not a claim of global source absence.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. **Minor: nomenclatural and proposed-type provenance is not represented.**
   LPSN 795859, JCM 17847, NCBI type-material rows
   `data/raw/ncbi_type_material.tsv:1844` through `:1849`,
   and the original description identify the proposed AK12 type.
   LPSN also explicitly distinguishes a not-validly-published,
   preferred name from a correct name. The YAML has no nomenclature
   entry and no `is_type_strain` flag. This is a non-blocking
   provenance gap, not a false negative type assertion or an identity
   error: the flag is absent, and the proposed type strain itself
   is present with supported deposits and genome links.

   The pinned BacDive projection says type strain "no"; its current
   public page displays a type-strain badge. StrainInfo marks the
   overall strain and LMG deposit as type but JCM deposit as non-type,
   whereas JCM itself says proposed type. Preserve these distinctions
   and conflicts, including nomenclatural validity, rather than
   silently choosing a boolean from a secondary source.

   Maintained owner: kg-microbe's LPSN name/mapping/type evidence
   feeding `data/raw/lpsn_names.tsv`, and
   `src/taxonmech/extract.py:420` if extraction loses that evidence.
   `src/taxonmech/seed.py:390` and `:514` show that nomenclature
   and the type flag depend on mapped LPSN designations. Upstream KGX
   files were unavailable at configured paths, so the exact earlier
   loss point is unresolved. Do not patch generated YAML.

## Recommended Edits

1. During later authorized curation, reconcile LPSN 795859 with this
   NCBI taxon in the upstream name/mapping inputs; retain the explicit
   not-validly-published/preferred-name status, original publication,
   marker, and proposed type designations. Preserve source disagreements.
2. Refresh the maintained LPSN inputs and extraction, then let the
   seeder derive the nomenclature and type flag from the authoritative
   designation match. Keep NCBI lineage and supported existing links
   unchanged; do not infer valid publication from type-strain evidence.
3. Keep lifecycle `SEEDED` in this read-only review. No review event,
   generated-file edit, or GitHub mutation is authorized.

## Follow-up Checks

- Reopen LPSN/JCM and reconcile the conflicting BacDive/StrainInfo type fields before changing source data.
- Inspect the missing upstream LPSN KGX node/edges to locate the loss. Add a regression test for this mapping and proposed-type case in the owning transform.
- Verify status parsing keeps "not validly published" and "not correct name" false; positive-word substring tests must not invert those phrases.
- After authorized changes, run extraction dry-run, inspect maintained-input changes, seed a canary, and run documented schema, strict, corpus-reproduction, provenance, and QC gates. Validate history/products if introduced.
- Retry GTDB live verification and retrieve the original MediaDive edge when their sources are available. These access limitations do not invalidate the inspected pinned rows.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- A first diagnostic comparison assumed the CAFI helper returned a tuple; code inspection showed a string return. The corrected comparison passed; this was a review-script error, not a record defect.
- NCBI and BV-BRC quality estimates differ; neither is asserted by this YAML. No assembly-quality threshold or biological functional conclusion is inferred.
- The entire YAML was reread byte-identical before report creation.
- Only this new report is created. No YAML, source, product, history event, GitHub object, branch, or worktree is changed.
- Eukaryota is already fully covered and was not re-reviewed.
