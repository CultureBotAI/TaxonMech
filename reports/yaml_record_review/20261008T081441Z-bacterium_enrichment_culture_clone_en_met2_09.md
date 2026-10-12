# YAML Record Review: bacterium enrichment culture clone En_MET2_09

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_09.yaml`
- Started UTC: 2026-10-08T08:10:45Z
- Finished UTC: 2026-10-08T08:14:41Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036345`, bacterium enrichment culture clone En_MET2_09: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED mapping status. It has zero linked BacDive strains, one NCBITAXON NAME assertion and one seed event dated 2026-09-13.

ID, label and stem resolve one environmental enrichment-culture clone. Authority rank SPECIES does not establish a named species, pure isolate, deposited strain or whole-community identity. Only this YAML was reviewed; Eukaryota was untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_09.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_09.yaml --out /private/tmp/em209-strict.tsv`: passed; one file, zero ERROR files/rows. The inspected TSV contains only its header.
- Read-only structured comparisons matched the full backbone row, every ancestor ID/label/rank/order, attestation, scope membership, path index and seed-event text. These bounded checks do not replace corpus reproduction.
- Live checks inspected NCBI Taxonomy EFetch and Datasets, plus full nucleotide and linked protein records.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. No focused equivalent of a corpus-only gate is claimed.
- Graph validation is not applicable because no graph is present. iModulonDB was not run: the YAML has no gene or transcriptomic assertion and supplementary evidence concerns an unidentified clone without an identified organism/dataset for expression-module comparison. This is not negative evidence about database coverage.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:222347` agrees with ID, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31891` confirms identity. `data/taxa/PATHS.tsv:14854` maps the ID to this stem; `curation/seed_scope.tsv:322594` supports membership and seed-event wording.

All four root-first ancestors match the pinned backbone: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), environmental samples (48479, NO_RANK). The short lineage is authority-supported; absent phylum/class/genus assignments are not missing YAML entries.

The inspected [Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036345&retmode=xml) agrees with name, rank, parent, code and ancestor labels/ranks, with no `OtherNames` element. Its Environmental samples division is distinct from taxonomic domain and does not contradict BACTERIA. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036345) confirms root-inclusive ID order; EFetch omits root from `LineageEx`. EXACT identifies this clone taxon, not a named species inferred from a functional gene.

## Evidence

The attestation correctly counts one NAME assertion, not organisms or cultures. The automated seed event does not imply human review.

Exact Nuccore query `txid1036345[Organism:noexp]` returned UID 336092354. The complete [HQ630143.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630143.1) is a 341-base partial `nosZ` CDS, not a 16S sequence. It gives exact organism, clone En_MET2_09 and `taxon:1036345`, an environmental-sample flag, microbial-fuel-cell cathode isolation source, and Na2S2O3-supplemented mineral-medium note. Gene/CDS features are partial at both ends with codon start 3 and translation table 11.

The complete linked [AEI00801.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00801.1) is a 113-amino-acid partial nitrous-oxide reductase explicitly produced by conceptual translation. Its clone/taxon/source qualifiers agree and `coded_by` points to HQ630143.1. Both full sequences and feature tables were read; no independent alignment, reannotation or biochemical assay was performed. This partial annotation and medium note do not establish measured enzyme activity, substrate utilization, a complete denitrification pathway, pure-culture physiology or electrotrophy.

The reference "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells" is marked unpublished and lists Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras as submitted. Direct submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016. The source feature has no strain, culture-deposit or geographic-location qualifier. The Girona institutional address is not an isolation location.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5) lists enrichment-derived `nosZ` accessions HQ630075-HQ630210 on printed page 54, a range containing HQ630143. Page 92 cautions that even a single DGGE band does not establish purity. Both complete pages were reread for this target. Searching all 164 pages' extracted text found neither exact HQ630143 nor En_MET2_09; this does not establish absence from raster figures or uninspected supplements. Relevant pages 88-100 and Table 24 had been inspected earlier in this continuing session. The band-position/reference-similarity table does not establish exact clone-to-species identity. Range membership supports study context, not transfer of a named species or community performance to the clone.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), DOI `10.1371/journal.pone.0063460`, was inspected earlier in this session and lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current searches found neither HQ630143 nor En_MET2_09 in retrieved main-article text. It is not an established exact-clone citation; supplements were not exhaustively audited.

## Completeness

No required-field omission was established. Full exact-target scans of seven pinned inventories (BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits) found no additional target row. The full backbone has no child row; exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These are snapshot-bounded findings.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxon number, slug and clone-label variants yielded four rows. Expansion to HQ630143, AEI00801, the unpublished title and the PLOS DOI yielded the same four. All were read as complete parsed TSV/JSON records. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots.

Three rows support identity: backbone, scientific name and scope. The fourth, `data/catalog/ncbi_genbank-0064.jsonl.gz:27392`, describes GCA_975963805.1, Bipolaricaulia bacterium (SeqCode), taxon 3121610, isolate BH_metabat2_bin668. Its total and ungapped genome sizes are both 1036345, causing the match. Those metrics are not taxon links. The unrelated assembly was not independently audited and supplies no target mapping, genome or phenotype.

An ignored-independent filename inventory across `data/taxa`, `reports/yaml_record_review` and `history` found the one target YAML and no prior report for its stem before this report was written. No absence beyond the named roots is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning, not proof that no genome exists. Zero BacDive strains agrees with inspected inputs and does not deny sequence evidence. Optional literature, discussion, gene/trait assertions, culture links and graphs may remain empty: supplementary annotation does not establish a required missing representation in this taxonomy-only record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. No wrong identity, broken stored reference, unsupported assertion or missing required representation was established. Named-species identity, culture purity and measured clone-specific activity remain unresolved and appropriately unasserted.

## Recommended Edits

None. Preserve the distinct environmental-clone identity, authority lineage and SEEDED status. Do not attach the unrelated metric-matched genome, infer a named species from partial functional-gene evidence, transfer other clones' conditions, or treat conceptual translation as an assay.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. Seed transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Do not hand-edit generated YAML to bypass maintained inputs.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment should preserve accession-specific source/medium qualifiers and distinguish annotation from experimental function. New organism/activity claims require explicit linkage and direct evidence at that scope, not accession-range membership or nearest-reference similarity alone.

After an authorized curation change, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. Global gates remain unrun here.

## Additional Notes

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected earlier, including both pages of Table 24. This review repeated exact-target text search and full page 54/92 reading with PyMuPDF in the existing temporary no-project environment. No new download/rendering, PDF edit or repository dependency change occurred; this was not a full-thesis or exhaustive figure/supplement audit.

Exact-label web searches yielded taxonomy listings, not additional inspected clone-specific research; exact accession/protein searches returned no results. The identical unpublished-title search from an earlier review was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this new timestamped report was written for the target. No YAML, maintained source, curation event, history, status or generated product was changed. No paid research, outreach, GitHub mutation, source refresh or regeneration occurred. Worktrees and Eukaryota were untouched. The target SHA-256 remained `e552ef334af6474f96b9a878eff5b36cca59f951cdfe14a9b003eb36dd7f1b9f` through the pre-report check.
