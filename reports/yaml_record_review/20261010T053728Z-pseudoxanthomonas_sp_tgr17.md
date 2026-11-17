# YAML Record Review: Pseudoxanthomonas sp. TGR17

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoxanthomonas_sp_tgr17.yaml`
- Started UTC: 2026-10-10T05:35:19Z
- Finished UTC: 2026-10-10T05:37:28Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037517` denotes Pseudoxanthomonas sp. TGR17, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2645906`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudoxanthomonas_sp_tgr17.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/pseudoxanthomonas_sp_tgr17.yaml --out /private/tmp/taxonmech-tgr17-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, code, complete lineage, empty source synonyms, seven inventories, unique index/scope resolution, attestation and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Complete native name and extra assembly-candidate rows were read. Live NCBI EFetch/Datasets taxonomy, exact nucleotide search and full marker annotations were inspected. The taxonomy-browser web reader failed; direct retrieval succeeded and all 74 parsed HTML text lines were read.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused checks do not establish corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222789` agrees with the directly inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037517&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037517&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037517). Species rank, parent 2645906 and genetic code 11 agree; Datasets includes root 1.

The full root-first lineage agrees: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Lysobacterales, Lysobacteraceae, Pseudoxanthomonas and unclassified Pseudoxanthomonas. Order 135614, family 32033 and genus 83618 are correctly carried from NCBI; the immediate parent is `NO_RANK`. No alternative hierarchy was substituted.

`data/catalog/ncbi_names-0005.jsonl.gz:32427` supplies the exact scientific name and empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. The species-ranked placeholder and marker strain qualifier are compatible metadata layers. Exact grounding does not establish formal nomenclature or type status.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned inventory. No additional own source-count row was found.

The exact nucleotide query returns one entry, UID 334361455: [JF799823.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799823.1), a 730-base partial 16S rRNA gene with both ends partial. Its source explicitly names Pseudoxanthomonas sp. TGR17, strain TGR17, `taxon:1037517` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This supports marker-to-taxon linkage, not an assembly or culture-deposit association.

The marker's only reference is a direct submission dated 10-Apr-2011 by Li, Liu, Shao and Sun at Hebei University. It supplies no DOI, PMID, collection country, collection date or coordinates. Institutional address and submission date are not sampling metadata. Shared submitters, habitat wording or a designation prefix cannot transfer another isolate's traits.

The extra native hit, `data/catalog/ncbi_genbank-0009.jsonl.gz:7569`, was fully inspected. It describes `GCA_010375175.1`, assembly name `ASM1037517v1`, strain 17T0737, BioSample `SAMN12576383` and BioProject `PRJNA560345`. Its organism is Francisella tularensis subsp. holarctica, taxon 119857, species taxon 263. The matching numeral belongs to an assembly name, not this organism identifier. It supplies no missing TGR17 genome link.

Exact-name, spaced-designation, wetland and JF799823 web queries established no directly joined experimental publication. Broad taxonomy trees and neighboring species/genome results were treated only as discovery leads; genus membership does not transfer phenotype or genome evidence. Datasets omits an assembly-count field rather than explicitly returning zero. The bounded checks do not exclude other genomes or publications.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Bounded taxon ID, slug and designation were searched, then JF799823 and spaced/hyphenated TGR 17 variants were added. Both searches returned four lines: own backbone, native name and scope, plus the unrelated assembly-name collision inspected above.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements apply only to the inspected repository surfaces.

Zero strain count describes represented culture inventory, not isolate existence or culturability. Optional fields are appropriately empty without exact supporting joins. A partial marker and an unrelated assembly-name match do not establish a missing required genome field. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, complete Lysobacterales lineage, attestation and seed audit are supported. No consequential missing association was established.

## Recommended Edits

No generated-record correction is justified. Preserve Pseudoxanthomonas sp. TGR17, species rank, full lineage, `SEEDED` status and existing history. Do not join taxa through assembly-name numerals, promote the partial marker to a genome or infer locality from an institutional address.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not direct generated-YAML edits. Optional marker enrichment requires a supported taxon-level representation rather than an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm exact organism linkage and retain JF799823.1's version. Require typed identifiers and explicit organism/strain evidence before adding an assembly, and directly joined experimental evidence before assigning a phenotype. After maintained-source changes, run the documented seed canary, schema/strict/history validation, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `562b3be9706e5952457993ddcb66921b2114722209041c07c70acef3aa36d674`.
- JF799823.1 lowercase sequence SHA-256: `234aa0afd06b2319b17fa912dc2aa876ccc124de79a91e328c1d9b5b93e50629`.
- `data/taxa/PATHS.tsv:15342` and `curation/seed_scope.tsv:323006` uniquely resolve the target. Scope addition is 2026-09-13; the seed preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this report was added for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
