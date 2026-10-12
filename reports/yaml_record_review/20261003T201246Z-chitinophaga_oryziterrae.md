# YAML Record Review: Chitinophaga oryziterrae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chitinophaga_oryziterrae.yaml`
- Started UTC: 2026-10-03T20:10:00Z
- Finished UTC: 2026-10-03T20:12:46Z
- Verdict: pass with minor issues

## Target

Read all 813 lines of the generated `TaxonRecord` for `NCBITaxon:1031224`,
Chitinophaga oryziterrae: `SPECIES`, `BACTERIA`, grounding `EXACT`, mapping
status `SEEDED`. One BacDive strain carries 18 assembly assertions, ten
genome-record assertions and 38 related-record assertions. Those are
provenance-bearing assertions, not distinct-strain or genome counts.

The record is generated from maintained source inventories and transforms.
Only this review report was created; the YAML and its curation status were
not modified.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/chitinophaga_oryziterrae.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/chitinophaga_oryziterrae.yaml` | Passed; one file, zero ERROR rows. Standard diagnostic: `reports/instance_validation_failures.tsv`. |
| Backbone and source comparisons | Identity, complete lineage, source counts, index and seed-history checks passed. |
| Strain assertion comparison | All fields of all 18/10/38 assertions match the raw and StrainInfo inventories as multisets. No assertion was silently deduplicated. |
| Embedded history | Checked by strict validation; the seed event matches source inventory and seed-scope provenance. |
| Standalone history | Not applicable: ignored-inclusive identifier, label, alias and slug searches under `history/` found no target history. |
| Graph and ontology-product gates | Not applicable: the fully read record has no causal graph. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
rendered products, exports or full test suite. The upstream kg-microbe KGX
transforms were not reread; local pinned inventories and native catalogs
were checked instead. No focused substitute for corpus reproduction is
claimed. No generator or history writer was run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220614` agrees with the species name, parent
`NCBITaxon:79328`, genetic code 11 and complete eleven-entry root-first
lineage. A complete backbone scan finds no child taxa. Live
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1031224)
and taxonomy EFetch confirm the identity and lineage. The authority string
and the former included name Chitinophaga sp. YC7001 are correctly retained
as related synonyms, not exact synonyms. Native NCBI name rows at
`data/catalog/ncbi_names-0005.jsonl.gz:29752` and the following two rows
corroborate their name classes.

`PATHS.tsv:12912` and `curation/seed_scope.tsv:10787` agree on the identifier
and slug. The record remains explicitly seeded, not human-reviewed.

LPSN `790316`, name, authority, status, publication identifiers and marker
accession agree with `data/raw/lpsn_names.tsv:27293`. The inspected
[LPSN species page](https://lpsn.dsmz.de/species/chitinophaga-oryziterrae)
supports the correct-name status and YC7001/JCM 16595/KACC 14533 type strain.
Its medical-name recommendation is nomenclatural context, not a claim that
this species is pathogenic. The omitted KACC type designation is the sole
finding below.

The GTDB `closeMatch` and count of two agree with
`data/raw/gtdb_mappings.tsv:1299`, the LPSN-linked GTDB identifier and both
native genome records. GTDB uses class Bacteroidia, whereas the NCBI lineage
uses Chitinophagia; these source classifications are kept distinct.

## Evidence

- **Strain identity:** `data/raw/bacdive_strains.tsv:56079`, native
  `data/bacdive/records.jsonl.gz:56078`, and the inspected
  [BacDive record](https://bacdive.dsmz.de/strain/133769) support YC7001,
  JCM 16595, KACC 14533, NBRC 109756, species taxon 1031224 and type-strain
  status. All three whole culture identifiers pass the local CAFI-backed
  normalizer. The raw culture-collection inventory independently assigns
  each deposit to this taxon. The strain-level medium count of one matches
  the pinned raw row; it is not a taxon-level MediaDive attestation.
- **Assembly provenance:** Raw assembly rows 32017-32034 match every field
  of the YAML. BacDive reference 67770 supplies unversioned GCA_009758125,
  IMG 3003151199 and PATRIC 1031224.3; reference 124043 supplies unversioned
  GCA_039536685. These source-unversioned assertions are preserved alongside
  explicitly versioned GCA/GCF assertions, not silently upgraded.
- **BV-BRC and GOLD:** Native BV-BRC `bvbrc-0000.jsonl.gz:3056` and the next
  row explicitly provide JCM 16595 and JCM:16595, two genome IDs, and their
  corresponding assemblies, BioSamples and BioProjects. GOLD organism
  `organisms.jsonl.gz:36665` is Go0043747. Project rows 403232 and 620666
  link it separately to Gp0549467 and Gp0854995; analysis rows 316313 and
  454816 link those projects to Ga0488926 and Ga0682086. IMG 3003151199
  belongs to the first analysis only; no IMG identifier is invented for
  the second analysis.
- **NCBI and GTDB:** Native GenBank rows
  `ncbi_genbank-0008.jsonl.gz:30552` and `ncbi_genbank-0036.jsonl.gz:5053`,
  RefSeq rows `ncbi_refseq-0002.jsonl.gz:36499` and
  `ncbi_refseq-0006.jsonl.gz:3054`, and GTDB rows
  `gtdb_genomes-0008.jsonl.gz:46987` and `gtdb_genomes-0012.jsonl.gz:7281`
  agree on both JCM 16595 assembly pairs. GTDB has two genomes of this
  species, not two independent strains. Live NCBI reports for
  [GCA_009758125.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_009758125.1/dataset_report)
  and [GCA_039536685.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_039536685.1/dataset_report)
  confirm the current accessions, corresponding RefSeq pairs, type
  material and contig/scaffold levels. The first links to SAMN13509244 and
  PRJNA594242, the second to SAMD00645534 and PRJDB10510. RefSeq/GTDB retain
  their source project PRJNA224116. The separate sample/project chains
  are not collapsed by their shared culture designation.
- **Complete assertion comparison:** Raw genome-record rows 25252-25261
  and related-record rows 86509-86546 exactly match the YAML. Entries that
  appear duplicated preserve distinct source fields or source authorities.
  The StrainInfo overlay has no assembly or related-record assertion for
  this BacDive strain.
- **Publications and sequence:** Crossref metadata resolves
  [the species-description DOI](https://api.crossref.org/works/10.1099/ijs.0.036442-0)
  to the 2012 article, volume 62, pages 3030-3035, and
  [the notification-list DOI](https://api.crossref.org/works/10.1099/ijs.0.050427-0)
  to the 2013 notice, volume 63, pages 799-800. The fully inspected
  [PubMed abstract and metadata, PMID 22307507](https://pubmed.ncbi.nlm.nih.gov/22307507/)
  link the species article, DOI, type deposits and JF710262. NCBI nuccore
  metadata for [JF710262.1](https://www.ncbi.nlm.nih.gov/nuccore/JF710262.1)
  confirms a 1491-base partial 16S sequence from YC7001, taxon 1031224,
  annotated as type material. The YAML correctly retains the unversioned
  source accession. Article full texts and sequence alignment were not
  checked; the report makes no broader physiological claim.
- **Attestations:** Complete scans of the seven raw source inventories
  confirm NCBI NAME 1, LPSN NAME 1, GTDB GENOME 2, BacDive STRAIN 1, GOLD
  ORGANISM 1 and MADIN TRAIT_ASSERTION 23. These units are not summed or
  interpreted as experimentally verified traits. No taxon-level
  MediaDive or BactoTraits row matches this taxon in those inventories.

## Completeness

Ignored-inclusive compressed searches covered native NCBI/GTDB catalogs,
BacDive, BV-BRC, GOLD, SeqCode and StrainInfo using the full name, slug,
YC7001, taxon identifier and whole culture identifiers. The pinned
backbone has no descendants, and its one BacDive strain is fully listed.
The SeqCode name hit 4988 corroborates the name, not a separate type-genome
claim. Full structured scans of retired and dropped inventories found no
target entry. These are bounded local-source findings, not assertions of
exhaustive worldwide strain coverage.

No AllTheBacteria row matched the full name, alias, slug, either BioSample
or BacDive strain ID in the complete ignored
`data/catalog/allthebacteria.tsv.xz` and committed `data/atb/` files.
Accordingly, no ATB assembly is manufactured from a taxon or culture match.
No FASTA or download-archive checks apply to an absent association.

The local native StrainInfo catalog and overlays contain no matching
strain under those identity searches. BacDive links to SI-ID 393488, but
the live `/v2/data/strain/max/393488` request returned HTTP 404. A numeric
hit for SI-DP 393488 belongs to an unrelated Escherichia coli deposit,
SI-ID 140949; it must not be treated as the requested strain ID. The absent
StrainInfo association is therefore not an established curation omission.
Future resolution requires an actual available record with an eligible
own-deposit match.

The resolved `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb
datasets` adapter returned 28 dataset keys, none for Chitinophaga. No
organism-matched expression query applies. This is not negative evidence
for the marker sequence. The YAML contains no gene-regulatory or causal
mechanism claim requiring a graph.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**m1 - Minor: incomplete LPSN type-deposit list.** The nomenclature section
lists only `kgmicrobe.strain:JCM-16595`, while inspected LPSN and the original
publication's abstract also identify KACC 14533 as a type deposit. The
local `data/raw/ncbi_type_material.tsv:1507` and following row independently
support KACC 14533. Its valid normalized identifier is already retained
under the BacDive strain's culture-collection IDs. The species identity,
type flag and genome links remain supported, so this is a nonblocking
nomenclatural provenance gap.

Maintained owner: the LPSN source/transform path consumed by
`src/taxonmech/extract.py:420`. Its materialized
`data/raw/lpsn_names.tsv:27293` contains only JCM 16595. The extractor reads
type-deposit `biolink:close_match` edges; `src/taxonmech/seed.py:405`
faithfully carries that list into the generated YAML. The review establishes
the missing source inventory value, not whether its origin is an older
snapshot or an upstream extraction omission.

## Recommended Edits

1. In a later curation change, reconcile the maintained LPSN input for
   `lpsn:790316` so its type-deposit evidence includes
   `kgmicrobe.strain:KACC-14533` alongside JCM 16595. Inspect the upstream
   KGX edge and producer before deciding whether refresh or transform
   repair is needed; do not hand-patch this generated YAML.
2. Re-extract the affected inventory and regenerate through the documented
   seed workflow after approval. Preserve YC7001 as a designation, all
   three BacDive deposit IDs and the separate genome/sample provenance.
   Do not add NBRC 109756 to the LPSN type list merely because BacDive
   lists that deposit.

## Follow-up Checks

- Verify the upstream LPSN edge and resulting `type_strain_ids` against
  inspected LPSN and PMID 22307507. If parser behavior changes, add a
  focused regression for multiple type deposits in its owning transform.
- Run the documented seed dry run, then an authorized target canary for
  `NCBITaxon:1031224`. Check that the only intended nomenclature change is
  supported and that the 18/10/38 provenance assertions remain intact.
- Rerun both target validators; use full-corpus reproduction, provenance
  and rendered-product checks in the subsequent curation workflow.
- Recheck the GTDB page when available: this browser request failed, so
  GTDB verification used the inspected pinned native genome records.
  Recheck StrainInfo only if its linked record becomes available; never
  substitute a matching deposit-number suffix for a strain identifier.

## Additional Notes

The medium count is strain-scoped by `extract_mediadive`, while taxon-level
attestations require direct NCBI-taxon source rows. Their difference here
is not evidence of a lost species-level attestation. Native catalog
projections do not include every growth-condition field, so no current
medium identity was inferred from them.

All absence statements above include ignored files or complete structured
reads within the stated boundaries. No paid research, source refresh,
GitHub mutation, history event, status promotion or generated-product edit
was performed. Prior reports and Eukaryota records were left untouched.
