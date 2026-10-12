# YAML Record Review: Vibrio vulnificus E64MW

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_vulnificus_e64mw.yaml`
- Started UTC: 2026-10-06T12:13:23Z
- Finished UTC: 2026-10-06T12:17:05Z
- Verdict: needs curation

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035116`, Vibrio vulnificus E64MW. It retains STRAIN rank, BACTERIA domain, parent Vibrio vulnificus (672), ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, a GTDB species mapping/xref, three synonyms, NCBITAXON/GTDB/MADIN attestations and one seed event. It contains no phenotype, habitat, individual genome link or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/vibrio_vulnificus_e64mw.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/vibrio_vulnificus_e64mw.yaml --out /private/tmp/e64mw-validation.tsv`: passed, one file and zero errors; output TSV read and header-only.
- Structured comparisons of the complete backbone row, ancestors, seven other imported taxon tables, PATHS/scope and seed provenance passed. Printed synonyms and all attestations were individually inspected. Reproducing source rows does not establish that their mapping scope is correct.
- Exact-ID reads of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Read live NCBI taxonomy, Assembly search and both Assembly summaries, two WGS master records, PubMed metadata and relevant primary-paper text. The exact Nuccore query returned 540 items; these were not treated as 540 genomes or individually annotated.
- Live GTDB genome pages failed through the browser reader; the pinned native GTDB genome row and imported species/mapping tables were inspected instead.
- `just validate-products` is inapplicable: no curator-added graph nodes. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history content and filename searches found no separate target artifact. The inline event was checked; no validator was run against a nonexistent history file.
- Full-corpus reproduction, validation, tests, history, provenance/site checks and `just qc` were not run. Focused checks do not certify the whole corpus.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221893` supports the identifier, label, rank, parent, genetic code and two strain-qualified NCBI synonyms. Full native scientific/equivalent-name rows are at `data/catalog/ncbi_names-0005.jsonl.gz:31328`, line 31329 and line 31330. `data/taxa/PATHS.tsv:14380` resolves the slug; `curation/seed_scope.tsv:36165` supports its three-source rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035116&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035116) agree on STRAIN, parent 672 and all ten ancestor IDs: 1, 131567, 2, 3379134, 1224, 1236, 135623, 641, 662 and 672. The browser/search representation displayed no rank, unlike both live structured authorities and the pinned backbone; that display discrepancy does not justify changing this YAML.

The NCBI identity is sound and its lineage should remain carried unchanged. The GTDB species association does not make the species an exact alternate name for this individual strain.

## Evidence

NCBITAXON counts one NAME in the 2026-09-13 snapshot. MADIN counts one imported TRAIT_ASSERTION at `data/raw/madin_taxa.tsv:659`; the row does not identify a specific phenotype, and none is asserted in the YAML. The inline 2026-09-13T17:54:04Z seed event agrees with scope and provenance.

The GTDB mapping at `data/raw/gtdb_mappings.tsv:1411` carries closeMatch and 186 genomes. The entire species row at `data/raw/gtdb_species.tsv:195992` also contains 186. All eight mappings for this GTDB species were read: seven target strain concepts and one targets NCBITaxon:672. Thus 186 is an imported species-cluster total, not a measured count of E64MW assemblies. `src/taxonmech/extract.py:501` counts assembly-to-species edges; line 751 attaches that species total to mapping rows.

The full native row at `data/catalog/gtdb_genomes-0003.jsonl.gz:5544` identifies GB_GCA_000269745.1 as E64MW, with NCBI strain taxid 1035116, species taxid 672 and GTDB classification s__Vibrio vulnificus. This supports membership, not strain/species equivalence.

[NCBI Assembly summaries](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&id=21709001,654418&retmode=json) identify original GCA_000269745.1 / GCF_000269745.1 and later GCA_963860615.1 as contig-level records classified to this strain. The RefSeq record is suppressed, with many frameshifted proteins given as the exclusion reason. The later record has a different BioSample/project and an isolate label referencing the older GCF; this is not proof of two independent isolates or permission to declare sequence equivalence.

[AFSX00000000.1](https://www.ncbi.nlm.nih.gov/nuccore/AFSX00000000.1) links the original WGS project to PRJNA67135 and SAMN01893923. [CAWLIA000000000.1](https://www.ncbi.nlm.nih.gov/nuccore/CAWLIA000000000.1) links the later project to PRJEB71012 and SAMEA115016949. Each master describes 269 component contigs; its length field is not a 269-base marker.

The original WGS record explicitly cites Morrison et al. (2012), PMID:22662170, DOI:10.1371/journal.pone.0037553. Read [the publisher's article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037553), including accession attribution, strain comparisons and methods. It identifies E64MW as an E-genotype wound isolate and connects it to AFSX and project 67135. The paper's environmental-genotype terminology must not be converted into environmental isolation provenance. Comparative gene content is not direct proof of a proposed mechanism or phenotype; no such claims were added.

Native BV-BRC 1035116.3 also links E64MW to GCA_000269745.1. GOLD's Go0011874 -> Gp0011874 -> Ga0020019 chain links that assembly and IMG 2548876515, but its culture-collection field is empty. These are useful taxon-level associations, not evidence of an eligible culture-deposit join.

## Completeness

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered ID, full label, slug and E64MW variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.

Read all forty initial candidate rows in full: seven TSV, fourteen GOLD and nineteen other native JSONL. Lossless common-field factoring was reconstruction-checked. Expanded searches covered the assembly/WGS, BioSample, original BioProject, GOLD/IMG and publication identifiers listed above. They returned twenty-five addresses, eight already read and seventeen new. Read the new ATB row in full and all sixteen new native rows' organism/taxon identities, accessions and matching fields; those sixteen were not full annotation reviews. Both address sets reconcile exactly.

The new ATB row at `data/catalog/allthebacteria.tsv.xz:1012924` is SAMN01893923 with NOT_PROCESSED, no assembly accession and no available FASTA. It does not support an ATB genome link. No eligible E64MW culture deposit was established in the checked sources. Zero BacDive strains is consistent with that result, not a claim that no genome or isolate exists.

The backbone has no direct children. Five imported taxon tables other than GTDB and MADIN have no exact target row. All five SOURCE.json files were separately discovered and fully traversed for the initial identity pattern with no match. Separate history content and filename searches found no target artifact.

Optional phenotype/graph enrichment is not required. iModulonDB is inapplicable to this YAML, which contains no functional gene, regulator or expression-module assertion.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**Major: species membership is promoted to strain identity.** At YAML line 46, the broader species name Vibrio vulnificus is an EXACT_SYNONYM of E64MW, accompanied by the identity-oriented GTDB xref at line 57. The source closeMatch at line 43 and repeated species total at line 71 require explicit scope handling, not automatic identity promotion. NCBI distinguishes the strain from species 672, and the native GTDB row distinguishes strain taxid, species taxid and species classification. The eight imported mapping destinations further disprove a one-to-one concept relationship.

Maintained owners: upstream kg-microbe GTDB mapping semantics, `src/taxonmech/extract.py:501` / line 751 for their inventory representation, and `src/taxonmech/seed.py:451` / line 468 for unguarded closeMatch-to-exact-synonym promotion. `src/taxonmech/seed.py:584` carries the species total into the attestation. This is one connected scope defect, not separate findings for every generated manifestation.

## Recommended Edits

1. Add rank/scope-aware handling in maintained mapping extraction and seeding. Preserve source predicates as source assertions, but do not turn a species-to-strain association into an exact synonym or identity xref. Retain the two supported strain-qualified NCBI synonyms.
2. Keep the 186 total explicitly species-scoped wherever retained; do not describe it as 186 E64MW genomes. Do not arbitrarily flip mapping direction or hand-replace the predicate without checking upstream semantics.
3. Add a focused regression test for this strain/species case, then regenerate through the validated writer. Do not edit the generated YAML or rewrite the NCBI lineage manually.

Taxon-level genome publication is a separate possible extension. It must not fabricate a BacDive/culture identifier to bypass the current deposit-based strain-link model, resurrect a suppressed RefSeq as current, or promote an unprocessed ATB sample into a genome.

## Follow-up Checks

Verify that the accepted generator change retains identity, rank, lineage and NCBI aliases while preventing the species label from becoming exact at strain rank. Confirm GTDB evidence remains queryable with its source scope and species count.

Run the focused regression test and both record validators; inspect the regenerated YAML. Before release, run corpus reproduction and full QC, including broader regression coverage for other strain-rank mappings. A live GTDB UI recheck remains useful but is not needed to establish the observed cross-rank scope defect.

## Additional Notes

Initial numeric collisions belong to Staphylococcus haemolyticus 6682 (SAMEA1035116; GCA/GCF_001237425.1; ATB ERZ3070581), Mycobacterium tuberculosis ERR1035116 (SAMEA3558649; ATB ERZ3502047), Bifidobacterium bifidum with SAMN41035116, Salmonella strain FZSY010301035116 and GOLD community projects with SAMN10351160-69.

Expanded WGS substring collisions include CAAFSX, ACAFSX, AAAFSX, DBAFSX, DAAFSX, JCAFSX, JAAFSX and ABAFSX prefixes for other organisms. Shared PMID 22662170 also retrieves JY1305 and JY1701 assemblies; these are comparator strains, not E64MW links.

No sequence equivalence analysis, individual inspection of all 540 Nuccore items, full paper-supplement review or current GTDB census was performed. Native catalogs, imported mapping totals and live assembly statuses were kept distinct. An exploratory read used the wrong catalog manifest suffix; ignored-inclusive filename discovery resolved it to MANIFEST.json, without changing any source file.

Only this new report was written for this individual review. No record, source, code, page, history or older report was changed. Eukaryotic reviews were not reopened.
