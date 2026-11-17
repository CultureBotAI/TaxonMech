# YAML Record Review: bacterium enrichment culture clone En_MET2_08

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_08.yaml`
- Started UTC: 2026-10-08T08:04:06Z
- Finished UTC: 2026-10-08T08:07:36Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036344`, bacterium enrichment culture clone En_MET2_08: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED mapping status. It has zero linked BacDive strains, one NCBITAXON NAME assertion and one seed event dated 2026-09-13.

Identifier, label and stem resolve one environmental enrichment-culture clone. Authority rank SPECIES does not establish a named species, pure isolate, culture deposit or whole-community identity. Only this target is reviewed here; Eukaryota was left untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_08.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_08.yaml --out /private/tmp/em208-strict.tsv`: passed; one file, zero ERROR files/rows. The inspected TSV contains only its header.
- Structured read-only comparisons matched the complete backbone row, every ancestor ID/label/rank/order, attestation, path index, scope membership and seed-event wording. These bounded comparisons do not replace corpus reproduction.
- Live checks inspected NCBI Taxonomy EFetch and Datasets, plus full nucleotide and linked protein records.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. No focused equivalent of a corpus-only gate is claimed.
- Graph validation is not applicable: no graph is present. iModulonDB was not run because the YAML contains no gene or transcriptomic assertion, and supplementary evidence concerns an unidentified clone without an identified organism/dataset for expression-module comparison. This is not negative database-coverage evidence.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:222346` agrees with ID, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31890` confirms identity. `data/taxa/PATHS.tsv:14853` maps the ID to the exact stem; `curation/seed_scope.tsv:322593` supports membership and seed-event wording.

All four root-first ancestors match the pinned backbone: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), environmental samples (48479, NO_RANK). This short chain is authority-supported; absent phylum/class/genus assignments are not missing YAML entries.

The inspected [Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036344&retmode=xml) agrees with name, species rank, parent, code and ancestor labels/ranks; it has no `OtherNames` element. Its Environmental samples division is distinct from taxonomic domain and does not contradict BACTERIA. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036344) confirms root-inclusive ID order; EFetch omits root from `LineageEx`. EXACT identifies this clone taxon, not a named species inferred from a functional gene.

## Evidence

The attestation correctly counts one NAME assertion, not organisms or cultures. The automated seed event does not imply human review.

Exact Nuccore query `txid1036344[Organism:noexp]` returned UID 336092352. The full [HQ630142.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630142.1) is a 341-base partial `nosZ` CDS, not a 16S sequence. It gives exact organism, clone En_MET2_08 and `taxon:1036344`, an environmental-sample flag, microbial-fuel-cell cathode isolation source, and Na2S2O3-supplemented mineral-medium note. Gene/CDS features are partial at both ends with codon start 3 and translation table 11.

The complete linked [AEI00800.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00800.1) is a 113-amino-acid partial nitrous-oxide reductase explicitly produced by conceptual translation. Its clone/taxon/source qualifiers match, and `coded_by` links back to HQ630142.1. Both full sequences and feature tables were read; no independent alignment, functional reannotation or biochemical assay was performed. A partial annotation and medium note do not establish measured enzyme activity, substrate utilization, a complete denitrification pathway, pure-culture physiology or electrotrophy.

The submitted reference "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells" is marked unpublished and lists Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras as submitted. Direct submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016. The source feature has no strain, culture-deposit or geographic-location qualifier. The Girona institutional address is not an isolation location.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5) lists enrichment-derived `nosZ` accessions HQ630075-HQ630210 on printed page 54, a range containing HQ630142. Printed page 92 cautions that even a single DGGE band does not establish purity. Both complete pages were reread for this target. Searching all 164 pages' extracted text found neither exact HQ630142 nor En_MET2_08; this does not establish absence from raster figures or uninspected supplements. Relevant pages 88-100 and Table 24 had been inspected earlier in this continuing session. The table's band-position/reference similarities do not establish exact clone-to-species identity. Range membership supports study context, not transfer of a named species or community performance to this clone.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), DOI `10.1371/journal.pone.0063460`, was inspected earlier in this session and lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current searches found neither HQ630142 nor En_MET2_08 in retrieved main-article text. It is not an established exact-clone citation; supplements were not exhaustively audited.

## Completeness

No required-field omission was established. Complete exact-target scans of seven pinned inventories (BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits) found no additional target row. The full backbone has no child row; exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These are snapshot-bounded findings.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Exact taxon number, slug and clone-label variants found only the backbone, name and scope rows above. Expansion to HQ630142, AEI00800, the unpublished title and the PLOS DOI yielded the same three rows. All were read as complete parsed TSV/JSON records. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots.

An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report for its stem before this report was written. No absence beyond the named roots is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning, not proof that no genome exists. Zero BacDive strains agrees with inspected sources and does not deny sequence evidence. Optional literature, discussion, gene/trait assertions, culture links and graphs can remain empty: supplementary annotation does not establish a required missing representation in this taxonomy-only YAML.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. No wrong identity, broken stored reference, unsupported assertion or missing required representation was established. Named-species identity, culture purity and measured clone-specific activity remain unresolved and appropriately unasserted.

## Recommended Edits

None. Preserve the distinct environmental-clone identity, authority lineage and SEEDED status. Do not infer a named species from partial functional-gene evidence, transfer other clones' conditions, or treat conceptual translation as a functional assay.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. Seed transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Do not hand-edit generated YAML to bypass maintained inputs.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment should preserve accession-specific source/medium qualifiers and distinguish annotation from experimental function. New organism/activity claims require explicit linkage and direct evidence at that scope, not accession-range membership or nearest-reference similarity alone.

After any authorized curation change, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. Global gates remain unrun here.

## Additional Notes

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected earlier, including both pages of Table 24. This review repeated exact-target text search and full page 54/92 reading using PyMuPDF in the existing temporary no-project environment. No new download/rendering, PDF edit or repository dependency change occurred; this was not a full-thesis or exhaustive figure/supplement audit.

Exact-label web searches yielded taxonomy listings and an uninspected patent lead, neither used as new evidence. Exact accession/protein searches returned no results. The identical unpublished-title search from an earlier review was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this new timestamped report was written for the target. No YAML, maintained source, curation event, history, status or generated product was changed. No paid research, outreach, GitHub mutation, source refresh or regeneration occurred. Worktrees and Eukaryota were untouched. The target SHA-256 remained `fc6616d4431430225b98e11cf549ca95e717e98f04a3cfc8c749740332ddb5fb` through the pre-report check.
