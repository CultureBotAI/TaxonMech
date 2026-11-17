# YAML Record Review: bacterium enrichment culture clone En_UW_02

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_02.yaml`
- Started UTC: 2026-10-08T12:41:02Z
- Finished UTC: 2026-10-08T12:44:47Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036388`, bacterium enrichment culture clone En_UW_02: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED mapping status. It stores zero linked BacDive strains, one NCBITAXON NAME assertion and one automated seed event dated 2026-09-13.

The authority's SPECIES rank does not establish a named species, pure isolate, deposited strain or whole-community identity. Only this environmental-clone target was judged; Eukaryota was untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_02.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_02.yaml --out /private/tmp/uw02-strict.tsv`: passed; one file, zero ERROR files/rows. The complete TSV is header-only.
- Structured comparisons checked source identity, full lineage, attestation, path index, scope and seed-event wording. Full live taxonomy and nucleotide/protein responses were inspected. Declared sequence lengths equal actual XML sequence lengths, and the nucleotide record's submitted translation equals its linked protein sequence.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. Bounded checks do not substitute for corpus-only gates.
- Graph validation is not applicable because the YAML has no graph. iModulonDB was not run: the YAML makes no gene/transcriptomic claim, and no identified organism/dataset was established for this unidentified clone's supplementary evidence. This is not a database-coverage absence claim.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222390` agrees with identity, label, rank, parent, code, empty synonyms and taxonomy snapshot 2026-09-13. The full scientific-name record at `data/catalog/ncbi_names-0005.jsonl.gz:31934` agrees. `data/taxa/PATHS.tsv:14897` and `curation/seed_scope.tsv:322637` confirm the stem, scope membership and seed-event reason.

The four root-first ancestors match the backbone: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN) and environmental samples (48479, NO_RANK). A phylum, class or genus is not missing from this authority-supported short lineage.

The full [live NCBI Taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036388&retmode=xml) agrees with ID, label, rank, parent, code and lineage labels/ranks; no `OtherNames` element is present. Environmental samples is its division, not a conflicting domain. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036388) confirms the four ancestor IDs in order, including root omitted from EFetch `LineageEx`. EXACT denotes this clone taxon, not a species inferred from a functional gene.

## Evidence

The NAME count describes one upstream name record, not organisms or cultures. The automated seed event is not human review.

Exact Nuccore search `txid1036388[Organism:noexp]` returned UID 336092376. The full [HQ630154.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630154.1) is a 346-base partial `nosZ` CDS, not 16S. Organism, clone En_UW_02 and `taxon:1036388` agree. Qualifiers describe environmental DNA from a microbial-fuel-cell anode biofilm and H2-supplemented mineral medium. Gene/CDS features are partial at both ends, with codon start 3 and translation table 11. No strain, culture-deposit or geographic-location qualifier is present; the Girona submission address is not an isolation locality.

The full linked [AEI00812.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00812.1) describes a 115-amino-acid partial nitrous-oxide reductase produced by conceptual translation. Source identity and medium agree, and `coded_by` links to HQ630154.1. Both complete sequences and feature tables were read. The submitted nucleotide translation has 115 residues and matches this protein; that check does not independently translate or reannotate the DNA. The CDD region ends at residue 109 and is not an assay. These records do not establish measured activity, substrate use, a complete pathway, purity or electrotrophy. No independent alignment, assay or cross-clone sequence-equivalence claim was made.

The submitted reference "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells" is marked unpublished. Authors are Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras. Direct submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, places HQ630154 within enrichment-derived `nosZ` accessions HQ630075-HQ630210. Page 92 cautions that one DGGE band does not assure purity. Both full pages were reread. Exact accession/clone searches across 164 pages' extracted text found no hits. Earlier inspected pages 88-100 and Table 24 provide context, not exact-clone species or physiology assignments. Raster figures and supplements were not exhaustively searched.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), DOI `10.1371/journal.pone.0063460`, was inspected earlier in this session and lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current main-text searches found neither HQ630154 nor En_UW_02. It is not an established exact-clone citation; supplements were not exhaustively audited.

## Completeness

No required omission was established. Complete exact-target scans found no additional row in seven pinned inventories: BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits. The full backbone has no child row. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These findings are snapshot-bounded.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. ID, slug and clone-label variants returned three identity rows: backbone, scientific name and scope. All were read as complete parsed TSV/JSON records. Expansion to HQ630154, AEI00812, the unpublished title and PLOS DOI returned the same three. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots.

An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report for its stem before writing. No wider absence is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning; this is not proof that no genome exists. Zero BacDive strains agrees with inspected inputs and does not deny sequence evidence. Optional citations, discussion, traits, genes, culture links and graphs can remain empty in a taxonomy-only seed. Supplementary annotation does not establish a required missing representation.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. No wrong identity, broken stored reference, unsupported assertion or required omission was demonstrated. Named-species identity, purity and measured clone-specific activity remain unresolved and appropriately unasserted.

## Recommended Edits

None. Preserve the environmental-clone identity, short authority lineage and SEEDED status. Do not transfer another clone's source or medium, infer species from the partial gene, or treat conceptual translation as an assay.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. Transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Do not hand-edit generated YAML.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment needs accession-specific qualifiers and explicit organism/activity evidence. Preserve the submitted anode-biofilm origin, H2 medium and partial-sequence scope unless a documented source correction establishes otherwise. Range membership and nearest-reference similarity are insufficient for clone-specific physiology or species identity.

After authorized curation, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. Global gates remain unrun here.

## Additional Notes

The review/curation skills, repository guidance and relevant schema classes/enums were read in this continuing unchanged-HEAD session; the checklist was reread for this target. The read-only review contract overrides history scaffolding and curation mutations.

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected earlier, including both Table 24 pages. This review repeated exact-target text search and full page 54/92 reading in a temporary no-project PyMuPDF environment. No PDF download, rendering, edit or repository dependency change occurred; this was not a full-thesis audit.

Web query `"En_UW_02" -site:ncbi.nlm.nih.gov/Taxonomy` excluded already-checked NCBI taxonomy listings and returned no results. Exact accession/protein queries also returned no results. The identical unpublished-title search from an earlier review was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this timestamped report was written for this target. No YAML, maintained source, history, curation event, status or generated product changed. No paid research, outreach, GitHub mutation, refresh or regeneration occurred. Worktrees and Eukaryota were untouched. The pre-report SHA-256 remained `7734e1900de0637854e336be58243e1ebb45b8ca737eb622f9733f61fe849944`.
