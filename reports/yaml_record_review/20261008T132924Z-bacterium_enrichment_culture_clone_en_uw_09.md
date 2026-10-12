# YAML Record Review: bacterium enrichment culture clone En_UW_09

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_09.yaml`
- Started UTC: 2026-10-08T13:26:33Z
- Finished UTC: 2026-10-08T13:29:24Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036395`, bacterium enrichment culture clone En_UW_09, with SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED mapping status. It stores zero linked BacDive strains, one NCBITAXON NAME assertion and an automated seed event dated 2026-09-13.

The authority's species rank is not evidence of a named species, pure isolate, deposited strain or whole-community identity. This verdict covers only the resolved clone; Eukaryota was untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_09.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_09.yaml --out /private/tmp/uw09-strict.tsv`: passed; one file, zero ERROR files/rows. The complete output TSV contains only its header.
- Structured comparisons checked identity, complete lineage, attestation, path index, scope and seed-event wording. Complete live taxonomy and nucleotide/protein responses were inspected.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. Bounded checks do not replace corpus-only gates.
- Graph validation is not applicable because no graph is stored. iModulonDB was not run: this taxonomy-only YAML makes no gene/transcriptomic claim, and no identified organism/dataset was established for the unidentified clone. This is not a claim that iModulonDB lacks coverage.

## Identity and Grounding

The full source row at `data/raw/ncbitaxon_taxa.tsv:222397` agrees with the identifier, label, rank, parent, code, empty synonyms and 2026-09-13 snapshot. The complete scientific-name record at `data/catalog/ncbi_names-0005.jsonl.gz:31941` agrees. Full rows at `data/taxa/PATHS.tsv:14904` and `curation/seed_scope.tsv:322644` verify the slug and scope reason; the stored seed-event wording matches.

All four ancestors match the pinned backbone in root-first order: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), environmental samples (48479, NO_RANK). No named phylum, class or genus is omitted from this authority-supported short chain.

The full [live NCBI Taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036395&retmode=xml) agrees with identity, rank, parent, code and lineage labels/ranks, with no `OtherNames` element. Its Environmental samples division is not a conflicting domain. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036395) confirms all four ancestor IDs, including root omitted from EFetch `LineageEx`. EXACT denotes this clone taxon, not a gene-based assignment to a named species.

## Evidence

The NAME assertion counts an upstream name record, not organisms or cultures. The automated seed event is not a human review.

Exact Nuccore search `txid1036395[Organism:noexp]` returned UID 336092390. The complete [HQ630161.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630161.1) is a 340-base partial `nosZ` CDS, not 16S. The organism, clone En_UW_09 and `taxon:1036395` match the target. Source qualifiers describe environmental DNA from a microbial-fuel-cell anode biofilm and H2-supplemented mineral medium. Gene/CDS annotations are partial at both ends, with codon start 3 and translation table 11. No strain, culture-deposit or geographic-location qualifier is present; the Girona submission address is not an isolation locality.

The complete linked [AEI00819.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00819.1) describes a 112-amino-acid partial nitrous-oxide reductase produced by conceptual translation. Its source identity and medium agree, and `coded_by` points to HQ630161.1. Both entire sequences and feature tables were read. The CDD region ends at residue 112; it is annotation rather than an assay. No independent translation, alignment, reannotation, assay or cross-clone sequence-equivalence claim was made. Neither source establishes measured activity, substrate utilization, culture purity, electrotrophy or a complete pathway.

The submitted reference "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells" is marked unpublished, with authors Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras. Direct submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, assigns HQ630075-HQ630210 to enrichment-derived `nosZ` sequences. Page 92 cautions that a single DGGE band does not assure purity. Both full pages were reread. Exact HQ630161/clone searches across 164 pages' extracted text found no hits. Earlier inspected pages 88-100 and Table 24 provide context, not exact-clone species or physiology assignments. Raster figures and supplements were not exhaustively searched.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), inspected earlier in this continuing session, lists a different JX accession series, including JX237213-JX237355 for `nosZ`. Current main-text searches found neither HQ630161 nor En_UW_09. It is not an established exact-clone citation; supplements were not exhaustively audited.

## Completeness

No required omission was established. Full exact-target scans found no additional row in seven pinned inventories: BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits. The complete backbone has no child row. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These are snapshot-bounded findings.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier, slug and clone-label variants returned three rows: backbone, scientific name and scope. Each was read as a complete parsed TSV/JSON record. Expansion to HQ630161, AEI00819, the unpublished title and PLOS DOI returned the same three rows. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots.

An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report for this stem before writing. No wider absence is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning, not proof that no genome exists. Zero linked BacDive strains agrees with inspected inputs and does not deny sequence evidence. Optional citations, discussion, genes, traits, culture links and graphs can remain empty for this taxonomy-only seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. No wrong identity, broken stored reference, unsupported assertion or required omission was demonstrated. Named-species identity, purity and measured clone-specific activity remain unresolved and appropriately unasserted.

## Recommended Edits

None. Preserve the environmental-clone identity, short authority lineage and SEEDED status. Do not infer species from the partial gene, transfer another clone's source or medium, or treat conceptual translation as an assay.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. Transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Do not hand-edit generated YAML.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment needs accession-specific qualifiers and explicit organism/activity evidence. Preserve the submitted H2 medium, anode-biofilm origin and partial-sequence scope unless a documented source correction establishes otherwise. Accession-range membership and nearest-reference similarity are insufficient for species or clone-specific physiology claims.

After authorized curation, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. Global gates remain unrun here.

## Additional Notes

The review/curation skills, checklist, repository guidance and relevant schema classes/enums were read in this unchanged-HEAD continuing session; the checklist was fully reread during the preceding individual review. The read-only review contract overrides curation history scaffolding and mutations.

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected earlier, including Table 24. This review repeated exact-target text search and complete page 54/92 reading in temporary no-project PyMuPDF. No PDF download, rendering, editing or repository dependency change occurred; this was not a full-thesis audit.

Web query `"En_UW_09" -site:ncbi.nlm.nih.gov/Taxonomy` excluded already-checked taxonomy listings and returned no results. Exact HQ630161 and AEI00819 queries also returned no results. The identical unpublished-title search from an earlier review was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this timestamped report was written for this target. No YAML, maintained source, history, curation event, status or generated product changed. No paid research, outreach, GitHub mutation, refresh or regeneration occurred. Worktrees and Eukaryota were untouched. The pre-report SHA-256 remained `98951d7a47f3d0ca0fcfa68bd08ac639a074bdd195b6733ffdcde64962055890`.

