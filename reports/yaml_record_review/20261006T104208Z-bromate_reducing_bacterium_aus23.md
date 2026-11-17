# YAML Record Review: bromate-reducing bacterium AUS23

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_aus23.yaml`
- Started UTC: 2026-10-06T10:39:57Z
- Finished UTC: 2026-10-06T10:42:08Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1035071`, bromate-reducing bacterium AUS23. This SPECIES-rank entry in BACTERIA has parent unclassified Bacteria (49928), four root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero imported BacDive strains, one NCBITAXON NAME assertion and one seed event. Its exact ID and pinned path resolve the target despite other uses of AUS23. The functional wording is the source taxon's name, not a general definition of bromate-reducing organisms.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_aus23.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_aus23.yaml --out /private/tmp/aus23-validation.tsv`: passed for one file with zero errors. The diagnostic TSV was read and contains only its header.
- Structured source checks verified the complete backbone row, every ancestor, synonyms, seven other imported taxon tables, PATHS row, scope reason, NCBITAXON attestation and inline seed-event context.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Live taxonomy XML/Datasets checks, exact non-expanded Assembly/Nuccore searches and complete returned nucleotide metadata were inspected.
- `just validate-products` was not applicable: no curator-added graph nodes are present. Taxonomy identifiers were checked at NCBI; no undocumented focused term/reference validator was invented.
- Ignored-inclusive history content and filename searches found no target-specific separate history record. The inline event was checked with the YAML; no history validator was run on a nonexistent target history file.
- Full-corpus reproduction, validation, history, tests, provenance, site checks and `just qc` were not run for this individual read-only review. The focused checks do not certify a release.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221873` and the native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31309` agree with all retained identity fields. `data/taxa/PATHS.tsv:14356` pins the slug; `curation/seed_scope.tsv:322164` supplies the same label and one-source NCBI rationale.

The inspected [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035071&retmode=xml) confirms name, species rank, parent 49928 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035071) agrees on the root-first ancestor IDs 1, 131567, 2 and 49928. Their labels/ranks match the pinned backbone. No genus or family is inferred from the short classification; EXACT does not imply a validly published binomial.

The separately resolved [bacterium AUS23, NCBITaxon:1032698](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032698&retmode=xml), retains its own authority identity. Its pinned scientific name is at `ncbi_names-0005.jsonl.gz:30196`. No inspected synonym, merge or crosswalk equates it with 1035071. This is not proof of biologically distinct isolates, but it prevents evidence transfer based solely on the shared designation.

## Evidence

The 2026-09-13 NCBITAXON attestation correctly records one NAME, not one genome or experimental observation. The 2026-09-13T17:54:04Z seed event and scope text agree. There are no retained literature snippets, asserted mechanisms, causal edges or genome-equivalence claims to support separately.

The exact Nuccore query returns [JF951735.1](https://www.ncbi.nlm.nih.gov/nuccore/JF951735.1), a 1,403-base partial 16S rRNA sequence. The complete inspected metadata, references and feature qualifiers identify strain AUS23 and source taxon 1035071. The isolation qualifier describes a biologically active carbon filter receiving dechlorinated tap water. This is direct identity context, not a culture-collection deposit or genome assembly; no new phylogenetic placement was computed.

Its reference links [PMID:21943884](https://pubmed.ncbi.nlm.nih.gov/21943884/) with [DOI:10.1016/j.watres.2011.09.001](https://doi.org/10.1016/j.watres.2011.09.001), Davidson et al., Water Research 45:6051-6062 (2011). Re-read the PubMed bibliography and abstract retrieved earlier in this review session, and inspected the [USDA ARS author summary and technical abstract](https://www.ars.usda.gov/research/publications/publication/?seqNo115=274528). They describe a study of 15 isolates; their five-isolate nitrate/perchlorate result does not identify AUS23's subgroup or establish its enzyme mechanism.

Opening the publisher page returned HTTP 403. Search-index excerpts are leads only. The full article, isolate-level Table 2 and supplements were not read; AUS23-specific kinetics, nearest-neighbor assignment, nitrate effects and mechanisms are not asserted. That access limit does not affect the authority-backed identity fields currently present.

## Completeness

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the ID, full label, slug and bounded AUS23/AUS 23/AUS-23 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 36 returned rows were read in full using structured TSV/JSON parsing, with lossless common-field factoring; the read addresses match the discovery set.

An additional ignored-inclusive search for JF951735, PMID 21943884 and the exact DOI found no rows in those roots. SOURCE.json was excluded only from row discovery: all five such metadata files were independently discovered with ignored files included and traversed in full, with no matching keys or values. History filenames were checked independently of ignore rules. These are bounded local-snapshot checks, not global absence claims.

The pinned backbone has no direct children or synonyms for this ID. The seven other imported taxon tables have no direct target rows. The zero strain count is therefore consistent with imported BacDive coverage, not a denial of laboratory strain AUS23. No supported target deposit or genome association emerged from the inspected catalogs. Exact Assembly search returned zero items with a phrases-not-found warning; this does not prove a genome is absent from every resource.

Optional nomenclature, mappings, strains, evidence and graph slots can remain empty. The marker/article are useful supplementary context, not missing required genome links. iModulonDB is inapplicable to this taxonomy-only YAML: it has no asserted gene, regulator or expression-module relationship.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the retained record. Equivalence with 1032698 remains unestablished and is not asserted.

## Recommended Edits

None required. Preserve separate NCBI identities, carried lineage and SEEDED status.

Any future authority reconciliation or source enrichment belongs in maintained source handling, including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, with scope owned by `curation/seed_scope.tsv`. Do not hand-edit the generated record. A future marker link needs an explicit supported identity model and must not count as a genome; phenotypes, media and isolation context belong to the relevant sibling repositories.

## Follow-up Checks

After any later source correction, re-check both NCBI identities and the affected native rows, run the focused schema/strict validators, then corpus reproduction and full QC before release. Strain-genome enrichment needs explicit eligible deposit and accession provenance, not a bare AUS23 match.

Inspect the original isolate-level tables and conditions before making functional claims; do not assign the abstract's subgroup results or reductase hypotheses to this isolate without that evidence.

## Additional Notes

Source exclusions were resolved by complete row context:

- Pseudomonas aeruginosa 2D9A/AUS23 has taxon 287, BioSample SAMN05226616, paired GCA/GCF_002276485.1 and GOLD Go0482286 -> Gp0365970 -> Ga0343221. Those are not an explicit link to 1035071.
- StrainInfo strain 393656, version DOI 10.60712/SI-ID393656.2, uses AUS23 as a designation but classifies its own LMG 27628 deposit (SI-DP 895357) as Pseudomonas aeruginosa. It supplies no target crosswalk.
- Staphylococcus aureus AUS23 is taxon 1280 with GCA_903800465.1 and SAMEA4008646, not a supported target association.
- SAMEA1035071 belongs to Staphylococcus haemolyticus T_480, including paired GCA/GCF_001227385.1, BV-BRC 1283.102 and ATB ERZ3070514.
- SAMN41035071 identifies Phocaeicola vulgatus RTP21002st2_C4_RTP21002_201210, paired GCA/GCF_040928405.1 and BV-BRC 821.6662.
- ERR1035071 denotes a Mycobacterium tuberculosis run, represented by ATB ERZ3501847 and BV-BRC 1773.20507.
- GOLD SAMN10350710 through SAMN10350719 describe environmental or host-associated community studies, not target taxon identifiers.

The prior `reports/yaml_record_review/20261004T021945Z-bacterium_aus23.md` concerns 1032698, not this target; it served only as a disambiguation lead. Primary authority and sequence checks were performed for the present review.

Only this new report is written. Generated YAML, source inputs, existing reports, history entries, mapping statuses and eukaryotic reviews remain unchanged.
