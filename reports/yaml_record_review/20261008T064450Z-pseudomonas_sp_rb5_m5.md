# YAML Record Review: Pseudomonas sp. RB5-M5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_rb5_m5.yaml`
- Started UTC: 2026-10-08T06:40:31Z
- Finished UTC: 2026-10-08T06:44:50Z
- Verdict: pass

## Target

The complete 54-line YAML was read before judgment. This generated `TaxonRecord` represents `NCBITaxon:1036331`, Pseudomonas sp. RB5-M5, at SPECIES rank in BACTERIA. Its parent is `NCBITaxon:196821` (unclassified Pseudomonas), genetic code is 11, grounding is EXACT and mapping status is SEEDED. It contains zero linked BacDive strains, one NCBITAXON NAME assertion and one seed event dated 2026-09-13.

The identifier, label and filename resolve one target. SPECIES rank here is the authority's rank for an unnamed isolate taxon, not a claim of formal species nomenclature. Other records, including Eukaryota, are not reviewed under this report.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/pseudomonas_sp_rb5_m5.yaml`: passed with no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/pseudomonas_sp_rb5_m5.yaml --out /private/tmp/prb5-strict.tsv`: passed; one file scanned, zero ERROR files and zero ERROR rows. The output TSV was read and contains only its header.
- Structured read-only comparisons checked the complete target backbone row, every ancestor's ID/label/rank/order, source attestation, path index, scope membership and seed-event wording. All passed. These are bounded comparisons, not full-corpus regeneration or provenance validation.
- Exact authority checks inspected live NCBI Taxonomy EFetch and Datasets responses.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. No invented focused validator is substituted for a documented corpus-only gate.
- Graph-product validation and iModulonDB are not applicable: no causal graph, gene, regulator, functional claim or transcriptomic assertion is present. Their inapplicability is not negative evidence.

## Identity and Grounding

The complete pinned row at `data/raw/ncbitaxon_taxa.tsv:222335` agrees with the stored name, taxon ID, rank, parent, genetic code and 2026-09-13 snapshot. Its synonym fields are empty, consistent with the YAML. The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31879` independently matches within the local snapshot. `data/taxa/PATHS.tsv:14842` supplies the exact filename stem; `curation/seed_scope.tsv:322582` supports membership and the seed-event text.

The ten ancestor entries match the pinned backbone in IDs, labels, ranks and order: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Gammaproteobacteria (1236), Pseudomonadales (72274), Pseudomonadaceae (135621), Pseudomonas (286), and unclassified Pseudomonas (196821). Numbers denote NCBI taxon IDs; the final entry correctly carries NO_RANK.

The inspected [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036331&retmode=xml) agrees with the name, species rank, bacterial division, parent 196821, code 11 and ancestor labels/ranks. It contains no `OtherNames` element. The inspected [NCBI Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036331) gives the same root-inclusive ancestor order. EFetch omits root from `LineageEx`; this is not a record mismatch. EXACT appropriately identifies the authority taxon, without implying a named species, type culture or phenotype.

## Evidence

The NCBITAXON attestation supports exactly one NAME assertion. Its count is not a number of organisms, cultures or experiments.

The exact Nuccore search `txid1036331[Organism:noexp]` returned one UID, 334701520. The inspected top-level, source-feature and reference metadata for [JN019027.1](https://www.ncbi.nlm.nih.gov/nuccore/JN019027.1) describe a 1,502-base partial 16S rRNA sequence, organism Pseudomonas sp. RB5-M5, strain RB5-M5 and `taxon:1036331`. This supports the exact sequence/strain/taxon association. Bases and non-source features were not inspected; no alignment, independent species identification or genome-quality assessment was performed.

The accession includes an unpublished reference by Yu, W., titled "Biological decoloring performance of Aeromonas hydrophila strain RB5-M". Its taxonomic name and shorter strain designation differ from the source qualifiers. The title does not establish that RB5-M is RB5-M5, justify an Aeromonas rename, or transfer a dye-decolorization result. The bibliographic relationship remains unresolved. Because the YAML asserts only the supported taxonomy and provenance, this is an external evidence limit rather than a demonstrated record defect.

The direct submission is dated 25-MAY-2011, and sequence creation/update dates are 07-JUN-2011. Inspected source qualifiers contain organism, genomic-DNA molecular type, strain and taxon cross-reference, but no isolation-source, geographic-location or culture-deposit qualifier. The submitter's Shanghai institution is not evidence of an isolation location.

Exact-name and RB5-M5 searches did not establish an inspected exact-target primary publication. The exact JN019027 web query returned no results. The identical unpublished title had also been searched in the immediately preceding individual review during this session, without an exact-strain primary study being established. Broad dye literature and near-name strains were not used as primary evidence. These bounded searches do not prove that no publication exists.

## Completeness

No consequential required-field gap was found. Complete exact-target scans of the seven pinned inventories for BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin traits and BactoTraits found no row requiring an additional attestation or mapping. The full pinned backbone had no child row for this taxon. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These are snapshot-limited statements.

Compressed-aware searches with `rg --no-ignore --hidden -z` included ignored/hidden files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches covered the exact numeric taxon ID, slug and RB5-M5 variants, then expanded to JN019027 and the unpublished title. Only the three backbone, scientific-name and scope rows above matched; all three were read as complete parsed TSV/JSON records. Five `SOURCE.json` files were separately parsed and had no exact identity match; history filename/content searches found no target entry within those roots.

An ignored-independent filename inventory across `data/taxa`, `reports/yaml_record_review` and `history` found the one target YAML and no prior target report before this report was written. No global absence outside the searched roots is claimed.

The exact-taxonomy Assembly query returned zero results and a phrase-not-found warning. It does not establish that no genome exists. Zero linked BacDive strains does not mean no biological strain exists. Optional literature, traits, culture links, discussion and graphs may remain empty: no supported missing assertion was established, and family/genus-level or similarly named strain evidence must not be transferred.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. The unpublished study-title relationship remains unresolved, but the record makes no corresponding study or phenotype claim. No wrong identity, broken stored reference, unsupported assertion or missing required representation was demonstrated.

## Recommended Edits

None. Preserve the SEEDED status. Do not rename the target, add decolorization or isolation-location claims, or infer a culture deposit from the inspected metadata.

A future confirmed taxonomy error should be corrected at NCBI and propagated through the maintained import workflow (`conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py`) and documented refresh/seed commands. Seed transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect is established here. Do not patch generated YAML to bypass the maintained owner.

## Follow-up Checks

No follow-up is required for this verdict. Before future enrichment, inspect an exact-strain primary source linking RB5-M5/JN019027.1 to the proposed study or phenotype. Resolve the unpublished RB5-M reference relationship explicitly; shared prefixes or a study title are insufficient.

After a separately authorized curation change, rerun the two focused validators and the applicable documented corpus, provenance, history and generated-product checks. Those global checks remain unrun here.

## Additional Notes

This sequential individual review followed the local review skill and field checklist. No YAML, source, curation event, review status, history entry or generated product was changed. No paid research, outreach, GitHub mutation, source refresh or regeneration was performed. Existing worktrees and Eukaryota records were left untouched.

The record SHA-256 remained `21add8aface44ae200ac07e586ce84910f1c42c9525025507f432e6f8f967997` through the pre-report check. This is the sole new review artifact for this target.
