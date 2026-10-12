# YAML Record Review: Rhodanobacter sp. MRhNF3(4)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhodanobacter_sp_mrhnf3_4.yaml`
- Started UTC: 2026-10-10T22:43:36Z
- Finished UTC: 2026-10-10T22:45:59Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Rhodanobacter sp. MRhNF3(4), `NCBITaxon:1037656`. It records species rank, bacterial domain, parent `NCBITaxon:2621553`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories, `curation/seed_scope.tsv`, and extraction/seeding code own future changes; generated YAML is read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/rhodanobacter_sp_mrhnf3_4.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/rhodanobacter_sp_mrhnf3_4.yaml --out /private/tmp/taxonmech-rhodanomrhnf34-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, full lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. These do not establish full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. These full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222871` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1 (no rank); cellular organisms 131567 (cellular root); Bacteria 2 (domain); Pseudomonadati 3379134 (kingdom); Pseudomonadota 1224 (phylum); Gammaproteobacteria 1236 (class); Lysobacterales 135614 (order); Rhodanobacteraceae 1775411 (family); Rhodanobacter 75309 (genus); unclassified Rhodanobacter 2621553 (no rank).

Complete live [EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037656&retmode=xml), [Datasets taxonomy JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037656), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037656) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not a validly published species name or culture deposit. The mixed-case strain designation MRhNF3(4) is preserved.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32507` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15426` uniquely resolves ID/slug; `curation/seed_scope.tsv:323086` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037656[Organism:exp]` returned one UID, 345019073. Complete [GenBank annotation JF779822.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779822.1) explicitly joins organism, strain MRhNF3(4), and taxon 1037656. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `1b2d6340f05e5e3c36033ded2ef0d5415931deac4917ee8012b8c25fbc877ed3`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), inspected for the shared study during the preceding BSF3(3) review, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate study compares mineral-amended and control forest plots. Its cohort results do not establish MRhNF3(4)-specific weathering, iron-release, chitin-degradation, or plant-growth phenotypes. Full text and isolate-level assay tables were not inspected. The non-fertilized ectomycorrhizosphere context comes from this marker's own annotation, not from a neighboring record.

All 13 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7637`: Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 12T0052, GCA_010376565.1, PRJNA560345, SAMN12576312, JAAGHJ000000000.1. The match is assembly name ASM1037656v1, not this taxon ID.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:20445`: Salmonella Typhimurium, taxid 90371/species 28901, strain 1037656, GCA_015873585.1, PRJNA248792, SAMN16972257, AAXRPS000000000.1, assembly PDT000901565.1. The bare strain number does not establish identity with NCBITaxon:1037656.
- `data/catalog/ncbi_genbank-0017.jsonl.gz:19211`: Campylobacter jejuni, taxid/species 197, strain PNUSAC021143, GCA_018962745.1, PRJNA239251, SAMN19222485, ABAXNR000000000.1. The match is assembly name PDT001037656.1. All three GenBank rows are latest contig assemblies excluded from RefSeq as large multi-isolate-project records, with no paired assembly; complete annotation and download fields were inspected.
- Ten AllTheBacteria rows match run-accession substrings. All have scientific/current/prior Sylph E. coli, dataset r0.2, available FASTA, and passing assembly/Sylph filters. Nine have passing HQ filters and true prior HQ membership. Row 993004 instead has `CHECKM2_MAX_CONTAM` and false prior HQ membership; its FASTA remains available. Complete checksum and download fields were inspected. Neither quality status nor these unrelated identities was transferred to the target.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992912 | SAMEA9850172 | ERR10376560 | ERZ25465705 |
| 993000 | SAMEA9850557 | ERR10376561 | ERZ25466565 |
| 993001 | SAMEA9850559 | ERR10376563 | ERZ25466571 |
| 993002 | SAMEA9850561 | ERR10376565 | ERZ25466578 |
| 993003 | SAMEA9850562 | ERR10376567 | ERZ25576691 |
| 993004 | SAMEA9850564 | ERR10376569 | ERZ25576704 |
| 993067 | SAMEA9850649 | ERR10376562 | ERZ25466831 |
| 993069 | SAMEA9850651 | ERR10376564 | ERZ25466835 |
| 993070 | SAMEA9850652 | ERR10376566 | ERZ25466839 |
| 993071 | SAMEA9850653 | ERR10376568 | ERZ25466843 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Case-insensitive patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779822, the DOI, and S003807171100280X. Both returned the same 16 lines: own backbone, scope, scientific name, and 13 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism and taxon-ID/16S web queries returned no search results; this is a bounded search outcome, not proof of literature absence. Dedicated NCBI primary resources were inspected independently.

The unrepresented marker is contextual evidence, not a missing required genome/deposit representation. No unsupported phenotype or causal graph is asserted. iModulonDB is not applicable to this taxonomy-only record without a gene, regulator, expression-module, or stress-response dataset claim; its absence is not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded evidence. Full-corpus quality gates and isolate-specific experimental conclusions remain outside this verdict.

## Recommended Edits

None required. Preserve `SEEDED` status and the existing event. Any future marker/context enrichment belongs in supported maintained inputs and extraction/seeding logic, or an explicitly supported curated overlay, not a manual generated-YAML edit. Do not infer a culture deposit or genome from the marker or transfer cohort phenotypes.

## Follow-up Checks

After a future maintained-input change, rerun the schema and strict validators, history validation where applicable, and documented corpus-reproduction/QC gates. Any phenotype enrichment needs inspected isolate-specific primary results; any genome link needs an explicit identity chain. No such enrichment was attempted here.

## Additional Notes

All target live NCBI requests succeeded. Shared HAL metadata/abstract were inspected during the preceding review; full text was not. Previously tested publisher and HAL-linked ISTEX routes were respectively HTTP 403 and institutional-login HTML; they were not retried here. No paid access, authentication, or contact was attempted.

YAML SHA-256: `33e7b935f80feddb245eb9735273d495ee252fe2a0e9ec2ae5cfcb718dbb83ed`. No taxon record, source inventory, schema, history, generated page, GitHub item, branch, or worktree was changed; this report is the only repository write for this review.
