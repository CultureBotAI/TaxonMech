# YAML Record Review: Prevotella sp. MSX73

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/prevotella_sp_msx73.yaml`
- Started UTC: 2026-10-04T00:56:55Z
- Finished UTC: 2026-10-04T00:59:03Z
- Verdict: pass

## Target

Read all 84 lines of generated `TaxonRecord` NCBITaxon:1032506,
Prevotella sp. MSX73. It carries `SPECIES`, `BACTERIA`, `EXACT`,
`SEEDED`, parent NCBITaxon:2638335, code11, twelve ancestors, one
GTDB mapping/synonym/xref, three attestations and `strain_count: 0`.
No listed strains, genome assertions, nomenclature, general evidence or
causal graph are carried. No YAML, source, history or status was edited.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/prevotella_sp_msx73.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/prevotella_sp_msx73.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, full lineage, names, mapping, path, scope, attestations and embedded seed event agree. |
| History/reference checks | Embedded event checked; ignored-inclusive searches found no target standalone history entry. No curator-added graph/product grounding requires validation. |
| GTDB census and join context | All 901,341 native GTDB rows scanned; all 24 exact cluster members inspected in a compact field projection. Repository culture-identifier matcher checked against both source strain spellings. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendering, exports, sequence alignment, FASTA download or
independent culture authentication. Focused checks do not prove corpus
reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220865`, live
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032506&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032506)
agree on exact identity, species rank, parent2638335 and code11. The
complete root-first chain agrees through Pseudomonadati, FCB group,
Bacteroidota/Chlorobiota group, Bacteroidota, Bacteroidia, Bacteroidales,
Prevotellaceae, Prevotella and unclassified Prevotella. Both clade ranks
are preserved. Complete backbone scanning found no children.

Native names0005:30154 supplies the scientific name and no NCBI synonym.
`data/taxa/PATHS.tsv:13238`, scope row36143 and legacy row776 agree.
The September13 seed event reproduces the September12 scope reason.

This NCBI concept is a species-level placeholder, not a strain child of
the named buccae species. GTDB assigns its assembly to P. buccae, while
NCBI retains MSX73's placeholder and uses Segatella buccae for the best
type-genome match. GTDB also uses Bacteroidaceae where the NCBI lineage
uses Prevotellaceae. Those source classifications remain distinct; no
reconciled lineage or substitution of NCBITaxon:28126 is justified.

## Evidence

- `data/raw/gtdb_mappings.tsv:1349` supplies
  `GTDB:s__Prevotella_buccae`, `skos:closeMatch` and count24;
  species row143453 agrees. All 24 genome accessions are distinct.
  NCBI taxon membership counts are28126:19,159272:2 and one each
  for575611,1032506 and873513. The count is the whole source species
  cluster, as specified by `TaxonomyMapping.genome_count`, not 24
  MSX73 assemblies. Other mapped NCBI IDs are not asserted to be
  equivalent culture deposits or interchangeable taxonomy identifiers.
- GTDB0013:5623 explicitly classifies GB_GCA_000287635.1, strainMSX73,
  taxon/species1032506 and sample SAMN00828778 in that cluster.
  It is nonrepresentative. Representative RS_GCF_000184945.1 at
  GTDB0013:23977 is ATCC33574, taxon873513, species28126,
  sample SAMN00216833, from type material. No representative-specific
  deposit, sample or biological attribute was transferred to MSX73.
- Live [GenBank assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000287635.1/dataset_report)
  confirms current GCA_000287635.1, MSX73, SAMN00828778,
  PRJNA78571 and a47-contig,3,164,912bp assembly. It also explicitly
  flags `unverified source organism`. The taxonomy check is `Failed`/
  `mismatch`, with a98.83% ANI best match to type assembly
  GCA_000184945.1, Segatella buccae, at90.31% assembly and88.69%
  type-assembly coverage. This agrees with the buccae species placement
  but does not authenticate the submitted culture or erase the warning.
- Live [RefSeq metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000287635.1/dataset_report)
  confirms GCF_000287635.1 is suppressed for that source-organism
  reason, while its GenBank partner remains current. Pinned
  GenBank0000:6664 and RefSeq-historical0000:1952 preserve the same
  warning, pair and sample; the historical not-live date is2023-11-30.
  The GenBank/RefSeq project fields PRJNA78571/PRJNA224116 are kept
  as distinct source metadata. The YAML does not misrepresent the
  suppressed RefSeq as a current strain-genome link.
- [LPSN779785](https://lpsn.dsmz.de/species/prevotella-buccae)
  retains P. buccae as the correct name; its type includes ATCC33574,
  not MSX73. [LPSN36184](https://lpsn.dsmz.de/species/segatella-buccae)
  treats Segatella buccae as a homotypic synonym. Local rows19123/6148
  agree on those statuses; the latter maps to28126, while the former
  has no direct NCBI mapping. Neither maps to1032506. The GTDB-sourced
  species name is supported taxonomic context, not NCBI synonym approval,
  a type-strain assertion or a reason to copy LPSN nomenclature here.
- BV-BRC0000:3170 identifies1032506.3, the GenBank assembly and same
  sample/project, but supplies bareMSX73 and no culture-collection field.
  GOLD organism9959, Go0011336, explicitly names `BEI HM-771`;
  project9820, Gp0011336, links that organism to the sample/project;
  analysis8181, Ga0014592, links that project to GCA_000287635.1 and
  IMG2531839272. The analysis's organism field is empty, so the project
  provides the inspected connection. Go/Gp/Ga are related records,
  not genome identifiers.
- The live BioSample independently carries `source_material_id: BEI HM-771`.
  Thus the collection attribution is not merely inferred from MSX73's name.
  However, `normalize_culture_identifier` in
  `src/taxonmech/genome_sources.py` returns empty for both `BEI HM-771`
  and `MSX73` under the pinned CAFI authority/template rules. Ignored-
  inclusive source searches found no matching BacDive or StrainInfo
  deposit on the searched surfaces. Source attribution therefore remains
  catalog context, not an eligible TaxonMech culture-deposit join.
- The full-catalog whole-sample search found ATB row1007570 for
  SAMN00828778, SRR445467 and ERZ9436017. Although FASTA is available
  and the Sylph filter is PASS, both assembly and HQ filters are
  `META_FAIL`; source comments distinguish the earlier661k checks from
  ATB's failed checks. `src/taxonmech/atb_catalog.py:31` and
  `crosslink_exclusion_reason` explicitly disallow this identity-warning
  flag. The row remains searchable but cannot supply an ATB strain/genome
  link. Available FASTA, same sample and species assignment do not
  override that exclusion. No sequence equivalence is inferred.
- NCBI NAME1, GTDB GENOME24 and Madin TRAIT_ASSERTION1 reproduce
  their separate source units; Madin is raw row611. Full exact-target raw
  scans found no BacDive, LPSN, GOLD aggregate, MediaDive or BactoTraits
  assertion for1032506. Native GOLD evidence above remains present;
  absence of an aggregate is not absence of the source.

## Completeness

No required representation is proven missing. Zero listed strains agrees
with the BacDive inventory and lack of descendants, not biological absence
of the isolate or sequence. Native genome evidence is retained without
fabricating a BacDive entry, accepting an unsupported collection key,
promoting suppressed RefSeq data or bypassing ATB's metadata warning.

Ignored-inclusive ID, label, slug and whole MSX73 searches covered raw
tables, native catalog shards, BacDive, BV-BRC, GOLD, SeqCode, StrainInfo,
ATB inventories, curation and history. Additional searches used the exact
BEI designation, assembly accessions and whole BioSample. SOURCE.json
files were JSON-traversed with no target/alias match. Structured scans
found no own type-material, merged-ID or dropped row, and no target
standalone history entry was found. These are bounded searched surfaces,
not global biological absence.

Optional definition, general evidence, nomenclature and graph slots need
not be invented. No gene, regulator or transcriptomic claim is carried;
iModulonDB was not applicable. Culture authentication and the underlying
NCBI/ATB warnings remain unresolved upstream, not silently adjudicated.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the carried taxon-record claims. This pass is not a finding
that the genome's submitted organism has been independently authenticated.
The verified warning statuses above must remain visible in source context
and constrain any later genome enrichment.

## Recommended Edits

None to this generated YAML. Leave `SEEDED` unchanged. Source-organism
authentication and any assembly-status correction belong to the NCBI
submitter/authority; ATB metadata flags belong to its source release.
Do not change either locally to create an eligible link. A future expansion
of culture-authority coverage belongs to the maintained CAFI registry
provenance and matching policy, with evidence and tests, not a one-off
BEI-prefix exception or an invented strain association.

## Follow-up Checks

- At an authorized refresh, recheck both assembly statuses, NCBI's warning
  and the exact ATB sample flags; do not treat GenBank-current as
  RefSeq-current or taxonomic similarity as culture authentication.
- Recheck NCBI1032506, GTDB's species placement and LPSN's naming
  independently, preserving genus/family disagreements and count scope.
- Any new deposit join must satisfy the full authority/accession rule
  and exact source chain; any ATB link must additionally pass all
  metadata-identity checks. Keep Go/Gp/Ga outside genome counts.
- After maintained changes and regeneration, run both focused validators
  and the full documented corpus gates.

## Additional Notes

The NCBI browser, GTDB page and attempted BEI product page did not supply
usable text. EFetch/Datasets and native catalogs supplied the evidence;
BEI catalog availability was not independently verified or inferred absent.
An initial file lookup named nonexistent matcher modules; it was corrected
to the inspected `src/taxonmech/genome_sources.py` implementation.
A combined output truncated part of the LPSN text; relevant name/status/
type passages were fetched again before judgment. No phenotype or
pathogenicity claim was imported from source labels. All checks were
read-only except this report and validator diagnostic. Eukaryota reviews
were untouched.
