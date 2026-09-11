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
| Strains | `StrainEntry` | BacDive strain id, designation, `culture_collection_ids`, `is_type_strain`, `medium_count`, `genome_assemblies`; capped at 200 per record, `strain_count` gives the total |
| Strain-to-genome links | `GenomeAssemblyLink` | `assembly_id` (GCA/GCF, supplied version preserved), required `source` and `source_id`; optional `source_reference_id`, `assembly_name`, `assembly_level`, `taxon_id` as asserted by the source |
| Harmonization | `SourceAttestation` | One per source: `source_id`, `mapping_predicate`, `assertion_count`, `assertion_unit` (`AssertionUnitEnum`: NAME, STRAIN, GENOME, ORGANISM, MEDIUM, TRAIT_ASSERTION) |
| Evidence | `EvidenceItem` | Optional record-level citations |
| Mechanism | `CausalGraph` / `CausalNode` / `CausalEdge` | Same shape as HabitatMech and TraitMech; every edge requires evidence |
| Discourse | `Discussion`, `Dataset` | From the vendored `mech_shared` module |
| Lifecycle | `CurationEvent` | `grounding_status`, `mapping_status`, `replaces`, `contributors`, append-only `curation_history` |

`TaxonRankEnum` lists NCBI's `has_rank` values as of the 2026 release
(`superkingdom` is gone; `domain`, `realm`, `cellular_root` and
`acellular_root` replaced it) plus `NO_RANK`.

`GenomeAssemblyLink` is a source assertion attached to a strain. It is not an
identity mapping, and its `taxon_id` does not override the strain's
classification. The full crosswalk is `data/raw/strain_assemblies.tsv`,
including strains beyond record listing caps. See [STRAIN_GENOMES.md](STRAIN_GENOMES.md).

`mech_shared.yaml` and `history.yaml` are vendored byte-identically from
culturebotai-claw at the commit in `scripts/.vendored_canon_ref`, and compared
against it by `just vendored-check`. Do not edit them here.

Regenerate Pydantic classes with `just gen-schema` (output is git-ignored).
