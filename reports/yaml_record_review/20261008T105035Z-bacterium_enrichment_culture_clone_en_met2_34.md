# YAML Record Review: bacterium enrichment culture clone En_MET2_34

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_34.yaml`
- Started UTC: 2026-10-08T10:44:41Z
- Finished UTC: 2026-10-08T10:50:35Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036370`, bacterium enrichment culture clone En_MET2_34: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding, SEEDED mapping status, zero linked BacDive strains, one NCBITAXON NAME assertion and one automated seed event dated 2026-09-13.

This is an environmental enrichment-culture clone. Authority rank SPECIES does not establish a named species, pure isolate, deposited strain or whole-community identity. Only this YAML was reviewed; Eukaryota was untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_34.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_34.yaml --out /private/tmp/em234-strict.tsv`: passed; one file, zero ERROR files/rows. The complete TSV is header-only.
- Structured comparisons matched identity, every ancestor ID/label/rank/order, attestation, path index, scope and seed-event wording. Live taxonomy responses and complete nucleotide/protein records were inspected.
- An XML-parser check confirmed declared and actual nucleotide/protein lengths, and agreement between the nucleotide record's annotated translation and linked protein sequence. This did not independently translate or reannotate the DNA.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. Bounded checks do not replace corpus-only gates.
- Graph validation is not applicable: no graph is stored. iModulonDB was not run: the YAML has no gene/transcriptomic assertion, and no identified organism/dataset was established for this unidentified clone's supplementary evidence. This is not evidence of absence from database coverage.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222372` matches ID, label, rank, parent, code, empty synonyms and taxonomy snapshot 2026-09-13. The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31916` agrees. `data/taxa/PATHS.tsv:14879` and `curation/seed_scope.tsv:322619` confirm the stem, membership and seed-event reason.

All four root-first ancestors match the pinned backbone: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), environmental samples (48479, NO_RANK). Absent phylum/class/genus assignments are not omitted ancestors in this authority-supported short lineage.

The [live Taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036370&retmode=xml) agrees with identity, species rank, parent, code and lineage labels/ranks; it has no `OtherNames` element. Environmental samples is its division, not a conflicting domain. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036370) confirms root-inclusive lineage order; EFetch omits root from `LineageEx`. EXACT resolves this clone taxon, not a named species inferred from functional-gene similarity.

## Evidence

The one NAME assertion counts an upstream name record, not organisms or cultures. The seed event does not imply human review.

Exact Nuccore query `txid1036370[Organism:noexp]` returned UID 336092312. The complete [HQ630122.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630122.1) is a 340-base partial `nosZ` CDS, not 16S. Organism, clone En_MET2_34 and `taxon:1036370` agree. It describes an environmental sample from a microbial-fuel-cell cathode and H2S-supplemented mineral medium. The submitted qualifier is H2S, not H2 or Na2S2O3. Gene/CDS features are partial at both ends, with codon start 3 and translation table 11. No strain, culture-deposit or geographic-location qualifier is present; the Girona submission address is not an isolation location.

The complete linked [AEI00780.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00780.1) describes a 113-amino-acid partial nitrous-oxide reductase produced by conceptual translation. Its source identity and H2S note agree; `coded_by` links to HQ630122.1. Both complete sequences and feature tables were read. The 113-residue length was checked directly, not inferred from neighboring clones. Its CDD region annotation is not a clone-specific biochemical assay. No independent alignment, reannotation or assay was performed. Annotation and medium context do not establish measured activity, substrate use, a complete pathway, purity or electrotrophy; no equality with another clone's sequence is asserted.

The submitted reference "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells" is marked unpublished. Authors are Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras as submitted. Direct submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, lists enrichment-derived `nosZ` accessions HQ630075-HQ630210, including this accession by range. Page 92 explains why a single DGGE band does not assure culture purity. Both complete pages were reread. Exact HQ630122 and En_MET2_34 searches across all 164 pages' extracted text returned no hits, not proof of absence from raster figures or uninspected supplements. Relevant pages 88-100 and Table 24 were inspected earlier in this continuing session. That band-position/reference-similarity table does not identify this exact clone as a named species. Range membership supports study context, not clone-specific physiology.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), DOI `10.1371/journal.pone.0063460`, was inspected earlier in this session and lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current main-text searches found neither HQ630122 nor En_MET2_34. It is not an established exact-clone citation; supplements were not exhaustively audited.

## Completeness

No required omission was established. Full exact-target scans found no additional row in seven pinned inventories: BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits. The full backbone has no child row. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These findings are snapshot-bounded.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. ID, slug and clone-label variants returned three identity rows, all read as complete parsed TSV/JSON records: backbone, scientific name and scope. Expansion to HQ630122, AEI00780, the unpublished title and PLOS DOI returned the same three. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots.

An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report for its stem before writing. No wider absence is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning, not proof that no genome exists. Zero BacDive strains agrees with inspected inputs and does not deny sequence evidence. Optional literature, discussion, traits, genes, culture links and graphs may remain empty in this taxonomy-only record; supplementary annotation establishes no required missing representation.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. No wrong identity, broken stored reference, unsupported assertion or required omission was established. Named-species identity, purity and measured clone-specific activity remain unresolved and appropriately unasserted.

## Recommended Edits

None. Preserve the environmental-clone identity, authority lineage and SEEDED status. Do not transfer another clone's source conditions or sequence identity, infer a named species from this partial gene, or treat conceptual translation as an assay.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. Transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Do not hand-edit generated YAML.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment needs accession-specific source/medium qualifiers and explicit evidence for organism/activity claims. Accession-range membership and nearest-reference similarity are insufficient. Preserve the submitted H2S qualifier and partial-sequence scope unless a documented source correction establishes otherwise.

After authorized curation, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. Global gates remain unrun here.

## Additional Notes

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected earlier, including both Table 24 pages. This review repeated exact-target extracted-text search and complete page 54/92 reading with PyMuPDF in a temporary no-project environment. No new PDF download, rendering, edit or repository dependency change occurred; this was not a full-thesis or exhaustive figure/supplement audit.

Exact-label web searches returned taxonomy listings and an uninspected patent lead, not additional inspected clone-specific research. Exact accession/protein searches returned no results. The identical unpublished-title search from an earlier review was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this timestamped report was written for this target. No YAML, maintained source, history, curation event, status or generated product was changed. No paid research, outreach, GitHub mutation, refresh or regeneration occurred. Worktrees and Eukaryota were untouched. The pre-report SHA-256 remained `ae64b98bc46359857b588b4a70b980a4a50ffbce60e22bb9f6330f14c8fbd1b9`.
