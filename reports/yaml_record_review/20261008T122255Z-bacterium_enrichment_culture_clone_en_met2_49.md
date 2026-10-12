# YAML Record Review: bacterium enrichment culture clone En_MET2_49

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_49.yaml`
- Started UTC: 2026-10-08T12:19:14Z
- Finished UTC: 2026-10-08T12:22:55Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036385`, bacterium enrichment culture clone En_MET2_49: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED mapping status. It stores zero linked BacDive strains, one NCBITAXON NAME assertion and one automated seed event dated 2026-09-13.

This environmental enrichment-culture clone is not an established named species, pure isolate, deposited strain or whole community merely because the authority uses SPECIES rank. Only this target was judged; Eukaryota was untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_49.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_49.yaml --out /private/tmp/em249-strict.tsv`: passed; one file, zero ERROR files/rows. The complete TSV is header-only.
- Structured checks matched source identity, full lineage, attestation, path index, scope and seed-event wording. Complete live taxonomy and nucleotide/protein responses were inspected.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. Bounded checks do not substitute for corpus-only gates.
- Graph validation is not applicable because the YAML stores no graph. iModulonDB was not run: the YAML asserts no gene/transcriptomic claim, and no identified organism/dataset was established for this unidentified clone's supplementary evidence. This is not a database-coverage absence claim.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222387` agrees with identity, label, rank, parent, code, empty synonyms and taxonomy snapshot 2026-09-13. The complete scientific-name record at `data/catalog/ncbi_names-0005.jsonl.gz:31931` agrees. `data/taxa/PATHS.tsv:14894` and `curation/seed_scope.tsv:322634` confirm the stem, scope membership and seed-event reason.

All four root-first ancestors match the backbone: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN) and environmental samples (48479, NO_RANK). Missing phylum/class/genus assignments are not omitted ancestors in this authority-supported short lineage.

The [live NCBI Taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036385&retmode=xml) agrees with ID, label, rank, parent, genetic code and lineage labels/ranks; no `OtherNames` element is present. Environmental samples is its division, not a conflicting taxon domain. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036385) confirms all four ancestor IDs in order, including root omitted from EFetch `LineageEx`. EXACT denotes this clone taxon, not a named species inferred from a functional gene.

## Evidence

The NAME count describes one upstream name record, not organisms or cultures. The automated seed event does not imply human review.

Exact Nuccore search `txid1036385[Organism:noexp]` returned UID 336092342. The full [HQ630137.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630137.1) contains a 341-base partial `nosZ` CDS, not 16S. Organism, clone En_MET2_49 and `taxon:1036385` agree. Source qualifiers describe an environmental sample from a microbial-fuel-cell cathode and H2S-supplemented mineral medium. H2S must not be replaced with H2 or Na2S2O3 from another clone. Gene/CDS features are partial at both ends; codon start is 3 and translation table is 11. No strain, culture-deposit or geographic-location qualifier is present. The Girona submission address is not an isolation locality.

The full linked [AEI00795.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00795.1) describes a 113-amino-acid partial nitrous-oxide reductase produced by conceptual translation. Its source identity and medium agree, and `coded_by` links to HQ630137.1. Both full sequences and feature tables were read. The CDD region annotation is not a clone-specific biochemical assay. No independent alignment, reannotation or assay was performed, and no equality with another clone's sequence is asserted. These annotations do not establish measured activity, substrate use, a complete pathway, purity or electrotrophy.

The submitted reference "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells" is marked unpublished. Submitted authors are Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras. Direct submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, places HQ630137 within enrichment-derived `nosZ` accessions HQ630075-HQ630210. Page 92 cautions that one DGGE band does not assure culture purity. Both full pages were reread. Exact accession/clone searches across 164 pages' extracted text found no hits; raster figures and supplements were not exhaustively searched. Earlier inspected pages 88-100 and Table 24 supply context, not an exact-clone species or physiology assignment.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), DOI `10.1371/journal.pone.0063460`, was inspected earlier in this session and lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current main-text searches found neither HQ630137 nor En_MET2_49. It is not an established exact-clone citation, and supplements were not exhaustively audited.

## Completeness

No required omission was established. Full exact-target scans found no additional row in seven pinned inventories: BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits. The full backbone has no child row. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These are snapshot-bounded findings.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. ID, slug and clone-label variants returned four rows: three identity rows (backbone, scientific name and scope), plus one numeric false match. Each was read as a complete parsed TSV/JSON record. Expansion to HQ630137, AEI00795, the unpublished title and PLOS DOI returned the same four. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots.

The complete row at `data/catalog/gtdb_genomes-0007.jsonl.gz:15578` describes `RS_GCF_026015685.1`, with GenBank assembly `GCA_026015685.1`, NCBI organism Segatella copri, strain F3-75 and taxid/species_taxid 165179. Its `ncbi_contig_n50` is 1036385. That is a sequence-length statistic, not this clone's taxon ID. The row supplies no genome or identity support for En_MET2_49.

An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report for its stem before writing. No wider absence is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning; this is not proof that no genome exists. Zero BacDive strains agrees with inspected inputs and does not deny sequence evidence. Optional literature, discussion, traits, genes, culture links and graphs can remain empty in this taxonomy-only record. Supplementary annotation does not establish a required missing representation.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. No wrong identity, broken stored reference, unsupported assertion or required omission was demonstrated. Named-species identity, purity and measured clone-specific activity remain unresolved and appropriately unasserted.

## Recommended Edits

None. Preserve the environmental-clone identity, short authority lineage and SEEDED status. Do not transfer another clone's medium or sequence identity, infer a named species from this partial gene, or treat conceptual translation as an assay.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. Transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Do not hand-edit generated YAML.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment needs accession-specific source/medium qualifiers and explicit evidence for organism/activity claims. Accession-range membership and nearest-reference similarity are insufficient. Preserve the submitted H2S qualifier and partial-sequence scope unless a documented source correction establishes otherwise.

After authorized curation, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. Global gates remain unrun here.

## Additional Notes

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected earlier, including both Table 24 pages. This review repeated exact-target extracted-text search and complete page 54/92 reading with PyMuPDF in a temporary no-project environment. No new PDF download, rendering, edit or repository dependency change occurred. This was not a full-thesis or exhaustive figure/supplement audit.

Exact-label web searches returned taxonomy listings and a CNGBdb result whose title and URL identify En_MET2_24 (taxon 1036360), not En_MET2_49. That sibling result was not inspected or used as target evidence. Exact accession/protein searches returned no results. The identical unpublished-title search from an earlier review was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this timestamped report was written for this target. No YAML, maintained source, history, curation event, status or generated product was changed. No paid research, outreach, GitHub mutation, refresh or regeneration occurred. Worktrees and Eukaryota were untouched. The pre-report SHA-256 remained `66a9aebd02e1e126fbcb0f8b6167423da6e91d2655dab7b39891f301eb4ac80d`.
