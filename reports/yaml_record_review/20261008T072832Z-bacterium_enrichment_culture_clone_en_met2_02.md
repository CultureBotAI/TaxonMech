# YAML Record Review: bacterium enrichment culture clone En_MET2_02

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_02.yaml`
- Started UTC: 2026-10-08T07:21:01Z
- Finished UTC: 2026-10-08T07:28:32Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036338`, bacterium enrichment culture clone En_MET2_02, at SPECIES rank in BACTERIA. It has parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding, SEEDED mapping status, zero linked BacDive strains, one NCBITAXON NAME assertion and one seed event dated 2026-09-13.

The identifier, label and filename resolved one target. This is an environmental enrichment-culture clone, not a demonstrated pure isolate, named species, culture deposit or whole enrichment community. Authority rank SPECIES does not establish those broader identities. No other record, including Eukaryota records, was reviewed under this report.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_02.yaml`: passed with no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_02.yaml --out /private/tmp/em202-strict.tsv`: passed; one file scanned, zero ERROR files and zero ERROR rows. The inspected TSV contains only its header.
- Structured read-only comparisons checked the complete backbone row, every ancestor ID/label/rank/order, attestation, scope membership, path index and seed-event wording. All matched. These bounded comparisons do not replace corpus reproduction.
- Exact authority checks inspected NCBI Taxonomy EFetch, Datasets, the full nucleotide accession and its linked protein record.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. No focused substitute for a documented corpus-only gate is claimed.
- Graph-product validation is not applicable: no graph is present. iModulonDB was not run: the YAML contains no gene or transcriptomic assertion, and the additional evidence concerns an unidentified environmental clone rather than an identified organism/dataset suitable for an expression-module cross-check. No negative inference about database coverage is made.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:222340` matches the taxon ID, label, rank, parent, genetic code and 2026-09-13 snapshot. Its synonym fields are empty, consistent with the record. The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31884` corroborates identity. `data/taxa/PATHS.tsv:14847` maps the ID to the exact stem; `curation/seed_scope.tsv:322587` supports membership and seed-event wording.

All four ancestors match the pinned backbone: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), and environmental samples (48479, NO_RANK). Numbers denote NCBI taxon IDs. This short chain is authority-supported; absent phylum, class and genus assignments are not missing YAML entries.

The inspected [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036338&retmode=xml) agrees with name, species rank, parent 48479, code 11 and ancestor labels/ranks. Its Environmental samples division does not contradict the Bacteria lineage: division and taxonomic domain are different fields. There is no `OtherNames` element. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036338) gives the same root-inclusive order; EFetch omits root from `LineageEx`. EXACT identifies this clone taxon, not a named species inferred from a functional marker.

## Evidence

The sole NCBITAXON attestation supports one NAME assertion, not a culture, organism or experiment count. The seed event represents pinned provenance without implying human review.

The exact Nuccore query `txid1036338[Organism:noexp]` returned UID 336092276. The complete inspected [HQ630104.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630104.1) is a 347-base partial `nosZ` coding sequence, not a 16S marker. Its qualifiers give the exact organism, clone En_MET2_02 and `taxon:1036338`, an environmental-sample flag, a microbial-fuel-cell cathode as isolation source, and an H2-supplemented mineral-medium note. The gene/CDS features are partial at both ends, use codon start 3 and translation table 11, and link protein AEI00762.1.

The complete inspected [AEI00762.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00762.1) is a 115-amino-acid partial nitrous-oxide reductase, explicitly a conceptual translation. Its `coded_by` link points to HQ630104.1, and clone/source/taxon qualifiers agree. Both sequences were returned and read with all feature annotations; no independent alignment, reannotation or biochemical assay was performed. This is evidence of an annotated partial gene sequence associated with the clone, not measured enzyme activity, a complete denitrification pathway, pure-culture physiology or electrotrophy.

The accession's reference title is "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells", marked unpublished, with Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras listed as submitted. The direct submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016. The Girona institutional address is not a geographic isolation qualifier. No strain, culture-deposit or geographic-location qualifier appears in the inspected source feature.

Ariadna Vilar Sanz's 2015 dissertation, [Where nitrite respiration meets electrotrophy: Diversity studies and functional characterization of autotrophic bacterial isolates from bioelectrochemical systems](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), provides a study-level bridge: printed page 54 lists HQ630075-HQ630210 for enrichment-derived `nosZ` sequences, a range containing HQ630104. Page 92 cautions that a single DGGE band does not ensure culture purity. Both pages were reread for this target. The complete extracted text of the 164-page PDF had no exact HQ630104 or En_MET2_02 match; this does not establish absence from raster figures or uninspected supplements. Relevant pages 88-100 and Table 24 had already been inspected in this continuing session. The table reports band-position similarities to reference sequences, not an established En_MET2_02-to-species assignment. Accession-range membership supports study context, not transfer of a reference species name or community activity to the clone.

The related [2013 PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), DOI `10.1371/journal.pone.0063460`, was inspected earlier in this continuing session. Its accession section lists a different JX series, including JX237213-JX237355 for `nosZ`. Current exact searches within its retrieved main article found neither HQ630104 nor En_MET2_02. It was not treated as an exact-clone citation; supplements were not exhaustively audited. Shared authors and research setting are not an identity bridge.

## Completeness

No consequential required-field omission was found. Complete exact-target scans of the seven pinned inventories for BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin traits and BactoTraits found no target row requiring another mapping or attestation. The full pinned backbone has no child row for this taxon. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These findings are bounded to the inspected snapshots.

Compressed-aware `rg --no-ignore --hidden -z` searches included ignored/hidden files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches covered the exact taxon number, slug and clone-label variants, then expanded to HQ630104, AEI00762, the unpublished title and the PLOS DOI. Four rows matched: the backbone, name and scope rows above, plus an incidental GTDB row. All four were read as complete parsed TSV/JSON records. Five `SOURCE.json` metadata files were separately parsed without an identity match; history filename/content searches found no target entry within these roots.

The incidental row at `data/catalog/gtdb_genomes-0014.jsonl.gz:19919` matched because its `ncbi_contig_n50` is 1036338. It describes RS_GCF_002891565.1 / GCA_002891565.1, NCBI taxon 380021, Pseudomonas protegens strain 11, with GTDB taxonomy Aquipseudomonas danubii. The numeric assembly metric is not a taxon link. This unrelated row supplies no target genome, trait or NCBI-versus-GTDB conflict; its assembly was not independently audited.

An ignored-independent filename inventory across `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report for the stem before this report was created. No absence outside the bounded roots is claimed.

The exact-taxonomy Assembly query returned zero results with a phrase-not-found warning, not proof that no genome exists. Zero linked BacDive strains is consistent with the inspected inputs and does not deny sequence evidence. Optional literature, discussion, culture links, gene/trait assertions and graphs can remain empty. The taxonomy-only YAML does not assert a phenotype, culture purity or named-species identity that requires additional support.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. No wrong identity, broken stored reference, unsupported record assertion or missing required representation was established. Species identity, culture purity and measured clone-specific activity remain unresolved and appropriately unasserted.

## Recommended Edits

None. Preserve the environmental-clone label, four-entry authority lineage and SEEDED status. Do not infer a named species from `nosZ` similarity, attach the incidental GTDB assembly, treat a conceptual translation as an enzyme assay, or transfer community performance to the clone.

A future confirmed taxonomy correction belongs first at NCBI and then in the maintained import workflow (`conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py`) and documented refresh/seed commands. Seed transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect is established here. Do not hand-edit generated YAML to bypass maintained inputs.

## Follow-up Checks

No follow-up is required for this verdict. Any separately authorized enrichment should preserve the narrow provenance of the partial `nosZ` annotation and source qualifiers. Organism-level or activity claims require explicit clone-to-organism linkage and direct evidence at that scope, not accession-range membership or a nearest-reference similarity table alone.

After an authorized curation change, rerun both focused validators and the applicable documented corpus, provenance, history and generated-product gates. Those global gates remain unrun in this review.

## Additional Notes

The PDF was reused from `/private/tmp/em201-thesis.pdf`, downloaded over verified TLS during the preceding individual review. That review rendered and visually inspected printed pages 54, 92, 95 and 96, including both pages of Table 24. This review rechecked the exact-target text search and pages 54/92 with PyMuPDF in the same temporary no-project environment; it did not redownload or newly render the PDF. Repository dependencies were unchanged. This is not a full-thesis or exhaustive figure/supplement audit, and no uninspected plot measurements support this verdict.

Exact-label web searches yielded leads but no additional inspected exact-clone study. An accession/protein search returned no results; the identical unpublished-title search from the preceding review was reused as context, not represented as a new search. These bounded search outcomes are not proof that no publication exists.

This sequential individual review used the local review skill and field checklist. No YAML, maintained source, curation event, review status, history entry or generated product was changed. No paid research, outreach, GitHub mutation, source refresh or regeneration was performed. Existing worktrees and Eukaryota were left untouched.

The record SHA-256 remained `c8dfdb5e29f81e68c4acbe21060c14cdb46d0b5859077291284880848eed4fc1` through the pre-report check. This is the sole new repository review artifact for this target.
