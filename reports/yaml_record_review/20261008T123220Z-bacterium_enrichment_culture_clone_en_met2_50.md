# YAML Record Review: bacterium enrichment culture clone En_MET2_50

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_50.yaml`
- Started UTC: 2026-10-08T12:28:37Z
- Finished UTC: 2026-10-08T12:32:20Z
- Verdict: pass

## Target

The complete YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036386`, bacterium enrichment culture clone En_MET2_50: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED mapping status. It contains zero linked BacDive strains, one NCBITAXON NAME assertion and one automated seed event dated 2026-09-13.

SPECIES is the authority's rank for this environmental clone, not proof of a named species, pure isolate, deposited strain or whole-community identity. Only this target was judged; Eukaryota was untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_50.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_50.yaml --out /private/tmp/em250-strict.tsv`: passed; one file, zero ERROR files/rows. The complete TSV is header-only.
- Structured comparisons verified source identity, full lineage, attestation, path index, scope and seed-event wording. Complete live taxonomy and nucleotide/protein responses were inspected.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. Bounded checks do not substitute for corpus-only gates.
- Graph validation is not applicable because the YAML has no graph. iModulonDB was not run: the YAML makes no gene/transcriptomic claim, and no identified organism/dataset was established for this unidentified clone's supplementary evidence. This is not a database-coverage absence claim.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222388` agrees with identity, label, rank, parent, code, empty synonyms and taxonomy snapshot 2026-09-13. The complete scientific-name record at `data/catalog/ncbi_names-0005.jsonl.gz:31932` agrees. `data/taxa/PATHS.tsv:14895` and `curation/seed_scope.tsv:322635` confirm the file stem, scope membership and seed-event reason.

All four root-first ancestors match the backbone: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN) and environmental samples (48479, NO_RANK). A phylum, class or genus is not missing from this authority-supported short chain.

The complete [live NCBI Taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036386&retmode=xml) agrees with ID, label, rank, parent, genetic code and lineage labels/ranks; it has no `OtherNames` element. Environmental samples is a division, not a conflicting domain. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036386) confirms all four ancestor IDs in order, including root omitted from EFetch `LineageEx`. EXACT refers to the clone taxon, not a species inferred from a functional gene.

## Evidence

The NAME count describes one upstream name record, not organisms or cultures. The seed event is automated provenance, not human sign-off.

Exact Nuccore search `txid1036386[Organism:noexp]` returned UID 336092344. The full [HQ630138.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630138.1) is a 341-base partial `nosZ` CDS, not 16S. Its organism, clone En_MET2_50 and `taxon:1036386` agree. Qualifiers describe an environmental sample from a microbial-fuel-cell cathode and H2S-supplemented mineral medium. Gene/CDS features are partial at both ends, with codon start 3 and translation table 11. No strain, culture-deposit or geographic-location qualifier is present; the Girona submission address is not an isolation locality.

The full linked [AEI00796.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00796.1) describes a 113-amino-acid partial nitrous-oxide reductase produced by conceptual translation. Its source identity and medium agree; `coded_by` points to HQ630138.1. Both full sequences and feature tables were read. The CDD region annotation is not a biochemical assay. These records do not establish measured activity, substrate use, a complete pathway, purity or electrotrophy. No independent alignment, reannotation, assay or cross-clone sequence-equivalence claim was made.

The submitted reference "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells" is marked unpublished, with authors Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras. Direct submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, places HQ630138 within enrichment-derived `nosZ` accessions HQ630075-HQ630210. Page 92 warns that a single DGGE band does not assure purity. Both full pages were reread. Exact accession/clone searches across 164 pages' extracted text found no hits. Earlier inspected pages 88-100 and Table 24 supply context, not exact-clone species or physiology assignments; raster figures and supplements were not exhaustively searched.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), DOI `10.1371/journal.pone.0063460`, was inspected earlier in this session and lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current main-text searches found neither HQ630138 nor En_MET2_50. It is not an established exact-clone citation; supplements were not exhaustively audited.

## Completeness

No required omission was established. Full exact-target scans found no additional row in seven pinned inventories: BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits. The full backbone has no child row. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These are snapshot-bounded findings.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. ID, slug and clone-label variants returned only three identity rows: backbone, scientific name and scope. All were read as complete parsed TSV/JSON records. Expansion to HQ630138, AEI00796, the unpublished title and PLOS DOI returned the same three rows. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry in these roots.

An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report for this stem before writing. No wider absence is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning; this does not prove that no genome exists. Zero BacDive strains agrees with inspected inputs and does not deny sequence evidence. Optional citations, discussion, traits, genes, culture links and graphs can remain empty in this taxonomy-only seed. Supplementary annotation does not establish a required missing representation.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. No wrong identity, broken stored reference, unsupported assertion or required omission was demonstrated. Named-species identity, purity and measured clone-specific activity remain unresolved and appropriately unasserted.

## Recommended Edits

None. Preserve the environmental-clone identity, short authority lineage and SEEDED status. Do not infer a named species from the partial gene, substitute another clone's medium, or treat conceptual translation as an assay.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. Transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Do not hand-edit generated YAML.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment needs accession-specific source/medium qualifiers and explicit organism/activity evidence. Accession-range membership and nearest-reference similarity are insufficient. Preserve the H2S qualifier and partial-sequence scope unless a documented source correction establishes otherwise.

After authorized curation, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. Global gates remain unrun here.

## Additional Notes

The review and curation skills, checklist, CLAUDE.md, justfile, curation/harmonization/schema guides, relevant schema classes/enums, history guidance and PDF skill were read in this continuing unchanged-HEAD session. The read-only review contract overrides history scaffolding and curation mutations.

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected earlier, including both Table 24 pages. This review repeated exact-target text search and full page 54/92 reading using a temporary no-project PyMuPDF environment. No PDF download, rendering, edit or repository dependency change occurred; this was not a full-thesis audit.

Exact-clone web search returned taxonomy listings. Exact accession/protein searches returned no results. The identical unpublished-title search from an earlier review was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this timestamped report was written for this target. No YAML, maintained source, history, curation event, status or generated product changed. No paid research, outreach, GitHub mutation, refresh or regeneration occurred. Worktrees and Eukaryota were untouched. The pre-report SHA-256 remained `105661520624cd61a1ca0cc99f7759c684de94166683c98b23f7f50c5839ebd4`.
