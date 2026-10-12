# YAML Record Review: Marinobacter adhaerens

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marinobacter_adhaerens.yaml`
- Started UTC: 2026-10-04T19:30:10Z
- Finished UTC: 2026-10-04T19:33:53Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1033846`,
Marinobacter adhaerens: SPECIES, BACTERIA, parent `NCBITaxon:2742`,
`grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11.
The record contains one LPSN name, five GTDB mappings, two NCBI related
synonyms, one BacDive type strain, two assembly assertions, three other
genome assertions, sixteen related-record assertions, eight source
attestations and one seed event.

This review concerns only the species record. HP15's separate taxon and
other organisms mentioned below were inspected as source context, not as
additional completed YAML reviews. Generated data and curation history
were not edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/marinobacter_adhaerens.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/marinobacter_adhaerens.yaml`.
  One file scanned, zero files with errors and zero error rows. This is the
  implementation of `just validate-strict`; it writes the standard
  `reports/instance_validation_failures.tsv` diagnostic.
- Passed read-only structured comparisons of the full parent chain,
  identity, source inventory rows, filename lock, scope and seed-event
  wording. Complete backbone scans found the one child taxon, HP15, and no
  children below it. A complete BacDive inventory scan over that subtree
  found exactly the one listed strain.
- Read all matching rows in the complete strain assembly, genome,
  related-record, StrainInfo and AllTheBacteria crosswalks. Their two
  assembly, three genome and sixteen related-record assertions agree with
  the YAML, including distinct provenance on repeated identifiers.
- Ran the existing CAFI-backed culture identifier normalizer: `DSM 23420`
  and `CIP 110141` resolve to the recorded deposit keys; `HP15` and
  `NCBI AY241552` do not. The encoded NCBI alias also yields no join key.
- Not run: `just verify-corpus`. It is a full-corpus byte-comparison gate;
  inspection of its implementation confirms that `--max-diffs` only limits
  diagnostic output. The bounded checks above are not a focused substitute.
- Not applicable: `just validate-products`, because there are no
  curator-added causal-graph nodes. NCBI terms were checked at their source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline seed event was inspected,
  and this read-only review creates no event or lifecycle promotion.
  Full-corpus QC, provenance, rendering and test-suite gates were not run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221317` and the live
[NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033846&retmode=xml)
agree on identifier, label, species rank, genus parent and code 11. All nine
root-first lineage entries agree with the pinned backbone; the
[Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033846)
also confirms their IDs and the HP15 child `225937`. The two source names
are authority strings, correctly retained as RELATED_SYNONYM rather than
promoted to exact synonym concepts.

The [LPSN name page](https://lpsn.dsmz.de/species/marinobacter-adhaerens)
identifies record 789625, Kaeppel et al. 2012, a validly published correct
name, and type strain HP15 with CIP 110141 and DSM 23420. The complete
inventory row `data/raw/lpsn_names.tsv:26667` additionally supplies the
legitimate flag, GTDB correspondence, exact status text and cited IDs.
NCBI's six type-material rows at `data/raw/ncbi_type_material.tsv:1681`
onward independently support these deposits and HP15. Complete exact-ID
merged and dropped table scans found no retirement row for the species.

BacDive's taxonomic hierarchy uses Alteromonadales/Alteromonadaceae, whereas
NCBI uses Pseudomonadales/Marinobacteraceae and the inspected GTDB metadata
uses Pseudomonadales/Oleiphilaceae. These are source-specific hierarchies;
none authorizes rewriting the NCBI lineage. BacDive classifies strain 493
directly under this species, while its genome assertions carry the HP15
strain taxon. Consequently the omitted `classified_as` field is correct.

## Evidence

The per-source assertions reproduce these inspected inventory rows:

| Source | Row and supported assertion |
| --- | --- |
| NCBITAXON | `ncbitaxon_taxa.tsv:221317`: one NAME, snapshot `2026-09-13`. |
| LPSN | `lpsn_names.tsv:26667`: one name `lpsn:789625`, source closeMatch. |
| GTDB | `gtdb_mappings.tsv:1376` through `:1380`: five source broadMatch mappings; only the LPSN-linked primary cluster's 17 genomes supply the attestation. |
| BACDIVE | `bacdive_strains.tsv:492`: one strain, directly classified under this species. |
| MEDIADIVE | `mediadive_taxa.tsv:109`: one taxon-level medium assertion, medium 514. |
| GOLD | `gold_organisms.tsv:457`: three directly classified ORGANISM assertions. |
| MADIN | `madin_taxa.tsv:637`: fourteen TRAIT_ASSERTIONs. |
| BACTOTRAITS | `bactotraits_taxa.tsv:82`: nineteen TRAIT_ASSERTIONs. |

All table names above are under `data/raw/`. Counts in different units were
not summed. The trait counts are source inventory counts, not newly
validated phenotypes. The direct-only notes on the latter four sources
correctly distinguish them from BacDive subtree gathering. The strain's
inventory medium count is zero, while MediaDive's species count is one;
these are different source scopes, not inconsistent measurements.

A complete scan of all 901,341 pinned GTDB native genome rows found:

| GTDB species | Cluster genomes | Direct NCBI `1033846` members | HP15 `225937` members |
| --- | ---: | ---: | ---: |
| Marinobacter adhaerens | 17 | 13 | 1 |
| Marinobacter salsuginis | 49 | 3 | 0 |
| Marinobacter flavimaris | 19 | 3 | 0 |
| Marinobacter sp001650915 | 9 | 2 | 0 |
| Marinobacter piscensis | 2 | 1 | 0 |

There were no duplicate accessions in these clusters. Counts match the
YAML, and each pooled mapping has direct native membership support. The
primary cluster also includes three members with other NCBI taxon IDs;
its count is not a count of HP15 isolates. Five representative objects
were read in full, including HP15 at
`data/catalog/gtdb_genomes-0003.jsonl.gz:36917`. It is the type-material
representative `RS_GCF_000166295.1` of the adhaerens cluster. Other members
were counted structurally, not all individually biologically audited.

The primary GTDB xref is supported by the explicit LPSN correspondence and
type-genome anchor under the repository's documented harmonization rule
(`src/taxonmech/seed.py:440` onward). It was not inferred merely from a
broadMatch predicate. The four pooled species are not xrefs or exact
synonyms. Their counts are not added to the primary attestation. The live
GTDB page was inaccessible, so this is verification of the pinned native
release, not a claim about a freshly retrieved GTDB website census.

The nomenclatural references resolve to the intended objects:

- [PMID 21335492](https://pubmed.ncbi.nlm.nih.gov/21335492/) and
  DOI `10.1099/ijs.0.030189-0` identify the species description. PubMed's
  abstract and metadata were inspected: HP15 is the type, the two deposits
  match, and the 2012 print publication agrees with the authority despite
  earlier online publication. The full paper was not inspected; no detailed
  phenotype claim is taken from an unseen body.
- [DOI 10.1099/ijs.0.042309-0](https://doi.org/10.1099/ijs.0.042309-0)
  resolves in Crossref to the 2012 IJSEM notification list, pages 757-758,
  also identified by LPSN. It is not a second species-description experiment.
- The [NCBI sequence response for AY241552](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AY241552&rettype=gb&retmode=xml)
  resolves to `AY241552.2`, a 1,531-base partial 16S rRNA sequence of HP15,
  taxon `225937`, explicitly marked type material. The source-supplied
  unversioned accession is legitimate; it is neither an assembly nor a
  culture-collection accession.

The complete native BacDive object at `data/bacdive/records.jsonl.gz:491`
and the [public strain page](https://bacdive.dsmz.de/strain/493) support
strain 493, HP15 and its two genuine culture deposits. Native reference
`66792` explicitly supplies the unversioned `GCA_000166295`,
`img.taxon:650377991` and `patric:225937.3` assertions with HP15 taxon
metadata. The marker-like alias is preserved from the source's culture
number field, but the existing normalizer excludes it from deposit joins.

The [live NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000166295.1/dataset_report)
and full native rows `data/catalog/ncbi_genbank-0000.jsonl.gz:1987` and
`data/catalog/ncbi_refseq-0000.jsonl.gz:1810` confirm current
`GCA_000166295.1` / `GCF_000166295.1`, ASM16629v1, HP15, taxon 225937,
Complete Genome, type material and BioSample `SAMN00713638`.
The exact HP15-taxonomy Assembly search returns one paired assembly entry.
The YAML preserves the unversioned BacDive accession and the independently
asserted GOLD `.1` accession rather than pretending they are two biological
genomes or silently rewriting either source.

GOLD's complete native chain was verified:

- `data/gold/organisms.jsonl.gz:6270` supplies `Go0007031`, HP15, taxon
  225937 and the whole DSM 23420 deposit.
- `data/gold/projects.jsonl.gz:6260`, `:35889` and `:65054` explicitly link
  `Gp0007031`, `Gp0050837` and `Gp0113765` to that organism. Their three
  BioProjects and two supplied BioSamples exactly match the YAML.
- `data/gold/analyses.jsonl.gz:21556` supplies the isolate-genome analysis
  `Ga0031593`, its `Gp0007031` project link, `GCA_000166295.1` and
  `img.taxon:650377991`. Its empty organism field does not conflict with the
  explicit project-to-organism chain.
- `data/gold/organisms.jsonl.gz:443521` supplies `Go0612776` with
  CIP 110141 in both its culture and strain fields. The YAML retains those
  two source-field assertions, not two organism identities. Full rows
  `:420150` and `:473714` supply the other two directly classified species
  organisms, HP15-B and DP2N14-4, without culture deposits; the HP15 child
  organism is correctly excluded from the species' direct count of three.

Live NCBI BioSample and BioProject EFetch responses confirm
`SAMN02745440` / `PRJNA234433` and `SAMN06314090` / `PRJNA372854`, their
HP15 identities and project relations. These are FEBA-related projects,
not extra genome assemblies. `PRJNA46089` independently confirms the
genome project and identifies a chromosome and two plasmids. Full BV-BRC
rows `data/bvbrc/bvbrc-0013.jsonl.gz:26075` through `:26077` retain two
plasmid records and the explicitly linked complete record `225937.3`.
The unlinked plasmid records have only the bare HP15 strain name, not a
new eligible culture-deposit assertion.

The full native StrainInfo record at
`data/straininfo/records.jsonl.gz:290093` and the
[live rich StrainInfo response](https://api.straininfo.dsmz.de/v2/data/strain/max/379044)
agree on SI-ID 379044, published-online status and version DOI
`10.60712/SI-ID379044.3`. Own deposits 868681 and 868682 are available
CIP 110141 and DSM 23420, respectively, and support the four typed YAML
associations. The shared BacDive ID agrees but is not the join key.
LMG 29242 is another source-group deposit, not an existing deposit in this
record's BacDive inventory; it must not be transferred by group membership.
Neither the native nor live response supplies a sequence assertion.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` over
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifest files. A first overly broad numeric
search produced truncated output and was not used to establish absence.
The replacement used the taxon ID, species name, slug, whole DSM/CIP
designations and marker accession, completed with 193 matching lines, and
its matching contexts were inspected. Relevant native source objects were
then read in full. Further accession/sample searches identified the ATB
exclusions below; unrelated numeric matches and other species members were
not treated as strain-identity evidence.

Complete crosswalk scans found two raw assembly rows, three raw genome
rows, twelve raw related-record rows, four StrainInfo related-record rows,
zero StrainInfo assembly rows and zero ATB strain/genome links for
`kgmicrobe.strain:bacdive_493`. All eligible listed assertions are retained.
These are bounded inventory checks, not a claim that every external genome
database entry for this species has a proven culture-deposit connection.

The missing ATB links have explicit explanations:
`data/atb/assemblies.tsv:3324` and `:5376` mark `SAMN02745440` and
`SAMN06314090` NOT_PROCESSED with no available assembly; corresponding
`data/atb/exclusions.tsv:1872` and `:2358` state `assembly_unavailable`.
Other ATB records with the species name, and the unrelated sample
`SAMEA1033846`, cannot replace those exact BioSamples. GTDB and primary
NCBI genome metadata supply bare HP15, so the absence of newly inferred
GTDB/RefSeq deposit links does not violate the explicit-culture-match rule.

An ignored-independent filename search of the report, history and curation
roots found no pre-existing target-stem artifact. History content was also
included in the searches above. `data/taxa/PATHS.tsv:13772` resolves the
single target and `curation/seed_scope.tsv:4043` supplies its eight-source
scope reason. The seed event remains consistent with that provenance and
the manifest-derived `2026-09-13T17:54:04Z` timestamp.

No consequential missing required field or eligible source link was
established. Optional definitions, additional literature evidence,
discussions and causal graphs are not required additions to this seeded
taxonomic identity record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed assertions. Source hierarchy differences,
repeated identifiers with distinct evidence, the unsupported collection
alias and omitted ineligible links are preserved according to the
repository's documented rules rather than silently reconciled or deduplicated.

## Recommended Edits

None required on the inspected evidence. Do not hand-edit the generated
YAML, sum pooled GTDB cluster counts into the primary attestation, transfer
LMG-group sequence links, append accession versions to source assertions,
or promote SEEDED status to REVIEWED from this report.

If future source evidence changes the verdict, the maintained owners are
`scripts/extract_source_inventory.py` for source extraction,
`src/taxonmech/genome_sources.py` and `src/taxonmech/gold_genomes.py` for
deposit-backed genome joins, `src/taxonmech/straininfo_links.py` for
own-deposit StrainInfo evidence and `src/taxonmech/seed.py` for harmonized
record generation. Taxonomy mapping corrections belong upstream in
kg-microbe. These are ownership notes, not authorized changes.

## Follow-up Checks

- On a future refresh, recheck primary GTDB membership and source-specific
  taxonomy rather than interpreting pooling as synonymy.
- Require complete deposit evidence before adding another strain/genome
  association. Preserve exact source versions, separate BioSample/project
  entities and both independent IMG assertions.
- Recheck ATB eligibility if either exact GOLD-linked BioSample gains an
  available assembly; no current exclusion should be overridden by name.
- After authorized changes, run focused schema/strict validation, relevant
  source-matching tests and the full `just verify-corpus` reproduction gate.
  Validate history only when a later curation action actually creates it.

## Additional Notes

Live GTDB, IMG, BV-BRC and GOLD page requests were inaccessible through the
web tool. Their pinned native records and explicit source chains were
inspected; no claim is made that all current web interfaces or database
contents were verified. LPSN and BacDive pages were accessible, as were
NCBI, Crossref and StrainInfo structured responses. The nomenclatural paper
was checked at abstract/metadata level, not full-text level.

NCBI's current assembly ANI metadata notes a within-genus best match to
M. flavimaris while retaining HP15's type-material identity and reporting
the taxonomy check as OK. It explicitly treats that situation as expected
for the type strain. This is not authority to rename the taxon or erase
the distinct LPSN/GTDB classifications.

iModulonDB is not applicable: the YAML contains no gene, locus, regulator,
pathway, stress response or expression-module assertion. The presence of
FEBA project metadata does not create such a claim. No mechanism or
phenotype is inferred from source membership alone.

Only this new review report was manually created. No record, inventory,
source code, prior report, page, history entry or status was changed, and
no paid research or GitHub mutation was performed. Eukaryota coverage was
left intact.
