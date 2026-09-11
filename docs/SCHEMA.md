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
| Strains | `StrainEntry` | BacDive strain id, designation, `culture_collection_ids`, `is_type_strain`, `medium_count`, `genome_assemblies`, `genome_records`; capped at 200 per record, `strain_count` gives the total |
| NCBI assembly links (primary) | `GenomeAssemblyLink` | `assembly_id` (GCA/GCF, supplied version preserved), required `source` and `source_id`; optional `source_reference_id`, `assembly_name`, `assembly_level`, `taxon_id` as asserted by the source |
| Other genome-record links | `GenomeRecordLink` | `genome_id` (`patric:<digits>.<digits>` or `img.taxon:<digits>`), required `source_database` (`patric` or `img`), `source` and `source_id` (currently `BACDIVE` and `bacdive:<digits>`); optional `source_reference_id`, `genome_name`, `assembly_level`, `taxon_id` as asserted by the source |
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
it is distinct from an `NCBITaxon:` identifier. `assembly_level` preserves the
source's description, including `plasmid` or `wgs`, rather than claiming a
complete assembly. The suffix of a PATRIC ID is kept as part of its opaque
identifier, not interpreted as an NCBI assembly version.

NCBI assemblies remain the primary links. The uncapped crosswalks are
`data/raw/strain_assemblies.tsv` and `data/raw/strain_genome_records.tsv`,
including strains beyond record listing caps. A shared strain or source
record does not establish equivalence between genome identifiers. See
[STRAIN_GENOMES.md](STRAIN_GENOMES.md).

`mech_shared.yaml` and `history.yaml` are vendored byte-identically from
culturebotai-claw at the commit in `scripts/.vendored_canon_ref`, and compared
against it by `just vendored-check`. Do not edit them here.

Regenerate Pydantic classes with `just gen-schema` (output is git-ignored).
