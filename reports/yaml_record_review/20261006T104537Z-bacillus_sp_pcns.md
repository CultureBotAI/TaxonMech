# YAML Record Review: Bacillus sp. PCNS

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_pcns.yaml`
- Started UTC: 2026-10-06T10:43:27Z
- Finished UTC: 2026-10-06T10:45:37Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1035084`, Bacillus sp. PCNS. This SPECIES-rank entry in BACTERIA has parent `NCBITaxon:185979`, ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. The target is the exact NCBI placeholder, not a formally named Bacillus species or a generic meaning of PCNS. No phenotype, gene-function, causal-graph or genome-equivalence assertion is present.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bacillus_sp_pcns.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/bacillus_sp_pcns.yaml --out /private/tmp/pcns-validation.tsv`: passed for one file with zero errors. Read the diagnostic TSV; it contains only its header.
- Structured comparisons checked the entire backbone row, complete ancestor chain, synonyms, seven other imported taxon tables, PATHS entry, scope row, NCBITAXON attestation and inline seed-event context. These focused comparisons passed.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Live NCBI Taxonomy XML/Datasets checks, exact non-expanded Assembly/Nuccore searches and complete returned nucleotide metadata were inspected.
- `just validate-products` was not run because no curator-added graph nodes are present. Carried taxonomy identifiers were checked at their authority; no undocumented focused term/reference validator was invented.
- Ignored-inclusive history content and filename searches found no separate target history record. The inline event was validated with the YAML; no separate history validator was run against a nonexistent target file.
- Full-corpus reproduction, closed-schema validation, history, tests, provenance/site checks and `just qc` were not run for this individual read-only review. This is not corpus or release certification.

## Identity and Grounding

The backbone row at `data/raw/ncbitaxon_taxa.tsv:221874` and the native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31310` agree with the retained identity. `data/taxa/PATHS.tsv:14358` pins the identifier to this slug; `curation/seed_scope.tsv:322165` carries the same label and one-source NCBI rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035084&retmode=xml) confirms species rank, name, parent 185979 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035084) supplies the same ten root-first ancestor IDs: 1, 131567, 2, 1783272, 1239, 91061, 1385, 186817, 1386 and 185979. XML and the pinned backbone agree on their labels and ranks, including Caryophanales and the verbatim parent label unclassified Bacillus (in: firmicutes).

The SPECIES rank and EXACT grounding express NCBI's identity assignment. Neither claims a validly published species name, species-level resolution by a short marker, or equivalence to an arbitrary named Bacillus. The lineage is source-carried, not reconciled or inferred.

## Evidence

The NCBITAXON assertion correctly counts one NAME from the 2026-09-13 taxonomy snapshot. It is not a genome, phenotype or biological-isolate count. The seed event at 2026-09-13T17:54:04Z agrees with the source and scope context. No retained citation, snippet or causal edge requires additional support.

The exact Nuccore query returned [JF789565.1](https://www.ncbi.nlm.nih.gov/nuccore/JF789565.1), a 536-base partial 16S rRNA gene sequence. Its complete inspected metadata, references and feature qualifiers explicitly name strain PCNS and source taxon 1035084. The submitter records agricultural soil from Salem District, Tamil Nadu, India as collection context. That is source metadata, not an independent habitat study or a whole-genome association.

The same sequence record lists an unpublished reference titled Carotenoid producing bacterium, by P. Indra Arulselvi, S. Umamaheswari, P. Michael and S. Sangeetha, plus a direct submission dated 2011-04-06. No DOI or PMID is supplied in the inspected sequence references. A submission title is not experimental proof of pigment identity, biosynthesis, yield or activity, and none of those claims is present in the YAML. The source's unpublished label also does not prove that no later publication exists.

## Completeness

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and bounded PCNS tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 37 matching rows were read completely as structured TSV/JSON, including lossless common-field factoring. The full-row address set reconciles to every discovered address.

An additional ignored-inclusive JF789565 search found no rows in those source/curation/history roots. SOURCE.json files were excluded only from row discovery: all five were independently found without honoring ignore rules and traversed in full, with no matching keys or values. Separate history filenames were also checked independently of ignore rules.

No synonyms or direct children occur for this ID in the pinned backbone; the seven other imported taxon tables contain no direct target rows. No supported culture deposit, target genome link or extra source mapping was identified within the inspected catalogs. Zero imported BacDive strains is consistent with that coverage and does not deny the laboratory strain's existence. PCNS alone is not a registered culture accession.

Exact Assembly search returned zero items, with a phrases-not-found warning; this is an exact-query result, not proof of genome absence everywhere. The partial rRNA marker is not a missing assembly. Optional nomenclature, mappings, strains, evidence and graph slots can remain empty. iModulonDB is not applicable to the identity-only YAML: the record names no functional gene, regulator or transcriptomic assertion.

Exact-name, accession and submitter-name web searches did not yield a verified target-linked publication. Broad pigment literature and similarly named entities were leads only. This is a bounded literature check, not an exhaustive assertion that a publication does not exist.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the retained record. Pigment characterization remains an unverified enrichment lead, not an unsupported current YAML claim or a required missing field.

## Recommended Edits

None required. Preserve the carried NCBI classification, generated ownership and SEEDED status.

Any future identity or source enrichment belongs in maintained inputs and source handling, including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`; scope is owned by `curation/seed_scope.tsv`. Do not hand-edit the generated YAML. Marker metadata must remain distinct from genomes. Pigment, habitat and culture-condition evidence belongs to the appropriate sibling repositories unless a supported TaxonMech representation is explicitly introduced.

## Follow-up Checks

For later source changes, re-check the exact authority identity and all affected native assertions, rerun focused schema/strict validation, then corpus reproduction and full QC before release. Genome enrichment requires explicit eligible culture-deposit and accession provenance.

Before assigning carotenoid production or a named species to PCNS, obtain an isolate-linked primary publication or equivalent experimental evidence. Do not infer a pigment structure or biosynthetic mechanism from the unpublished title or from unrelated Bacillus studies.

## Additional Notes

All non-target source matches were resolved by full row context:

- SAMEA1035084 belongs to Staphylococcus haemolyticus 51-72, including paired GCA/GCF_001233165.1, BV-BRC 1283.143, GOLD Gp0140499 and ATB ERZ3070538.
- ERR1035084 belongs to Mycobacterium tuberculosis, with BV-BRC 1773.20516 and ATB ERZ3501921.
- SAMN41035084 belongs to Bacteroides xylanisolvens RTP21277st1_C6_RTP21277_210401, with paired GCA/GCF_040928155.1 and BV-BRC 371601.1587.
- GCA_010350845.1 is Campylobacter jejuni 839957, taxon 197, not an NCBI taxon-ID match.
- GOLD SAMN10350840 through SAMN10350849 describe root or soil-community projects, not this isolate.
- ATB SRR10350840 through SRR10350849 and SRR21035084 belong to Escherichia coli, Shigella flexneri, Listeria monocytogenes or Escherichia albertii source records. Their source/Sylph naming differences were preserved; none provides a PCNS link.

A related-title publication lead, DOI 10.4172/2157-7110.1000292, shared submitter surnames but was not verified as PCNS evidence. The DOI page failed to open and the publisher issue page timed out. Its full text was not inspected; no conclusions or isolate equivalence were taken from search excerpts. Generic PCNS acronym results likewise supplied no identity link.

Only this new report is written for PCNS. No generated record, source input, existing report, curation history, mapping status or eukaryotic review is changed.
