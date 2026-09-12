# Schema guide

`src/taxonmech/schema/taxonmech.yaml` defines **TaxonRecord**, the single tree
root. One YAML per record.

| Section | Class | What it holds |
|---|---|---|
| Identity | — | `identifier` (NCBITaxon CURIE), `label`, `rank` (`TaxonRankEnum`), `taxon_domain` (filesystem bucket), `parent_taxon`, `genetic_code`, `xrefs` |
| Lineage | `LineageEntry` | Ancestors root-first, each with label and rank |
| Names | `TaxonSynonym` | Alternate names with scope (`SynonymTypeEnum`) and source (NCBITaxon, LPSN, GTDB) |
| Nomenclature | `NomenclatureEntry` | One per LPSN name: authority, verbatim status, `validly_published` / `legitimate` / `is_correct_name`, `type_strain_designations`, `publications`, `sequence_accessions` |
| Mappings | `TaxonomyMapping` | A GTDB species mapped here, with `mapping_predicate` (from the source taxon's side) and `genome_count` |
| Strains | `StrainEntry` | BacDive strain id, designation, `culture_collection_ids`, `is_type_strain`, `medium_count`, `genome_assemblies`, `genome_records`, `related_records`; capped at 200 per record, `strain_count` gives the total |
| NCBI assembly links (primary) | `GenomeAssemblyLink` | `assembly_id` (GCA/GCF, supplied version preserved), required `source` and `source_id`; optional `source_reference_id`, `assembly_name`, `assembly_level`, `taxon_id` as asserted by the source |
| Other genome-record links | `GenomeRecordLink` | `genome_id` (`patric:<digits>.<digits>`, `img.taxon:<digits>`, `gtdb.genome:RS_GCF_…` / `gtdb.genome:GB_GCA_…` or `atb.assembly:202505.SAM…`), required `source_database`, `source` and `source_id`; optional `source_reference_id`, `genome_name`, `assembly_level`, `taxon_id` as asserted by the source |
| Related records | `GenomeRelatedRecordLink` | `record_id`, `record_type` (`BIOSAMPLE`, `BIOPROJECT`, `GOLD_ORGANISM`, `GOLD_PROJECT`, `GOLD_ANALYSIS`, `STRAININFO_STRAIN`, `STRAININFO_DEPOSIT` or `NUCLEOTIDE_SEQUENCE`), source provenance, optional `record_name` and `taxon_id`; these are excluded from genome counts |
| Strain-link evidence | `StrainLinkEvidence` | Shared `source_field`, `matched_strain_id` (an existing culture-deposit CURIE), `source_strain_field` and verbatim `source_strain_identifiers`; GOLD chains also retain `source_organism_id` and `source_project_id` |
| Harmonization | `SourceAttestation` | One per source: `source_id`, `mapping_predicate`, `assertion_count`, `assertion_unit` (`AssertionUnitEnum`: NAME, STRAIN, GENOME, ORGANISM, MEDIUM, TRAIT_ASSERTION) |
| Evidence | `EvidenceItem` | Optional record-level citations |
| Mechanism | `CausalGraph` / `CausalNode` / `CausalEdge` | Same shape as HabitatMech and TraitMech; every edge requires evidence |
| Discourse | `Discussion`, `Dataset` | From the vendored `mech_shared` module |
| Lifecycle | `CurationEvent` | `grounding_status`, `mapping_status`, `replaces`, `contributors`, append-only `curation_history` |

`TaxonRankEnum` lists NCBI's `has_rank` values as of the 2026 release
(`superkingdom` is gone; `domain`, `realm`, `cellular_root` and
`acellular_root` replaced it) plus `NO_RANK`.

`GenomeAssemblyLink` and `GenomeRecordLink` are source assertions attached to
a strain. Their `taxon_id` is NCBI classification metadata and does not
override the strain's classification. An IMG genome ID uses `img.taxon:`;
it is distinct from an `NCBITaxon:` identifier. GTDB genome IDs use
`gtdb.genome:` and retain the `RS_GCF_` or `GB_GCA_` accession and version;
they are distinct from GTDB species identifiers in `taxonomy_mappings`.
`assembly_level` preserves the source's description, including `plasmid` or
`wgs`, rather than claiming a complete assembly. The suffix of a PATRIC ID
is kept as part of its opaque identifier, not interpreted as an NCBI assembly
version.

AllTheBacteria genome records use `source_database: allthebacteria` and
`source: ALLTHEBACTERIA`, with the same local snapshot-scoped assembly ID
in `genome_id` and `source_id`. Their nested `atb_evidence`
(`AtbAssemblyEvidence`) retains `release`, `sample_id`, optional `ena_analysis_id`, `run_accessions`,
`assembly_seqkit_sum`, `dataset`, `assembly_filter`, `hq_filter`,
`download_url`, `archive_url`, `archive_filename` and optional `sylph_species`.
`sample_links` uses `AtbSampleLink`, a BIOSAMPLE-only specialization of
`GenomeRelatedRecordLink` with GTDB or GOLD source evidence. It preserves the
complete prior assertions, including culture-match and organism/project chains.
A shared sample establishes an association rather than identical assemblies.
The uncapped ATB overlap and its supported genome crosslinks are in
`data/atb/`; see [ALLTHEBACTERIA.md](ALLTHEBACTERIA.md).

StrainInfo assertions use `source: STRAININFO` and required nested
`straininfo_evidence` (`StrainInfoEvidence`). Required fields are `strain_id`
(`straininfo.strain:`), `deposit_id` (`straininfo.deposit:`),
`deposit_designation`, `strain_status`, `deposit_status` and
`match_method: culture_identifier`. Optional fields are `strain_doi` (a
`DOI:10.60712/SI-IDN.version` record-version identifier), `source_bacdive_id`
and `bacdive_reference_conflict`. Sequence evidence additionally requires
`sequence_type` and `sequence_deposit_id`, which must identify the matched
deposit. Genomes use `GenomeAssemblyLink`; unversioned GCA/GCF accessions
remain unversioned. `NUCLEOTIDE_SEQUENCE` links use `INSDC:` accessions and
source types `gene`, `rrnaop` or `patent`. SI strain/deposit and nucleotide
references remain related records, not genome identifiers. See
[STRAININFO.md](STRAININFO.md) for source matching, status and DOI semantics.

`matched_strain_id` preserves the existing `kgmicrobe.strain:` identifier,
including suffix characters such as `/` or `+`. Its syntactic validity does
not establish collection authority: GTDB, GOLD and StrainInfo joins additionally require
an authority recognized by the pinned CAFI registry and an accession that
fully matches its `regex_id.full` template. A schema-valid identifier can
still be ineligible for a join. Existing values in `culture_collection_ids`
may include aliases or unsupported formats that are retained but not joined.

NCBI assemblies remain the primary links. The uncapped crosswalks are
`data/raw/strain_assemblies.tsv` and `data/raw/strain_genome_records.tsv`,
including strains beyond record listing caps. A shared strain or source
record does not establish equivalence between genome identifiers.

`related_records` uses `biosample:`, `bioproject:`, `gold:Go…`, `gold:Gp…` and
`gold:Ga…` identifiers, typed by `record_type`. These references retain
sample, sequencing-project, analysis-project and GOLD organism context
without promoting those entities to genomes. The
uncapped inventories are `data/raw/strain_related_records.tsv` and
`data/straininfo/related_records.tsv.gz`; StrainInfo NCBI assertions are in
`data/straininfo/assemblies.tsv`. See
[STRAIN_GENOMES.md](STRAIN_GENOMES.md).

`mech_shared.yaml` and `history.yaml` are vendored byte-identically from
culturebotai-claw at the commit in `scripts/.vendored_canon_ref`, and compared
against it by `just vendored-check`. Do not edit them here.

Regenerate Pydantic classes with `just gen-schema` (output is git-ignored).
