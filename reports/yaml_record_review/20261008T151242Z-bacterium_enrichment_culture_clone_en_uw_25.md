# YAML Record Review: bacterium enrichment culture clone En_UW_25

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_25.yaml`
- Started UTC: 2026-10-08T15:08:34Z
- Finished UTC: 2026-10-08T15:12:42Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036411`, bacterium enrichment culture clone En_UW_25: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED status. It has zero linked BacDive strains, one NCBITAXON NAME assertion and one automated seed event dated 2026-09-13.

The authority's species rank does not establish a named species, pure isolate, deposited strain or whole-community identity. Only this resolved clone was reviewed; Eukaryota was untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_25.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_25.yaml --out /private/tmp/uw25-strict.tsv`: passed; one file, zero ERROR files/rows. The full TSV is header-only.
- Structured comparisons passed for identity, full lineage, attestation, index, scope and seed wording. Complete public taxonomy and sequence responses were read. XML checks confirmed declared/actual sequence lengths and agreement between the submitted CDS translation and its own protein.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. Bounded comparisons do not replace corpus-only gates.
- Graph validation is not applicable: no graph is stored. iModulonDB was not run because the YAML makes no gene/transcriptomic claim and no identified organism/dataset was established for this unidentified clone. This is not a database-coverage absence claim.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222413` agrees with identifier, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete scientific-name record at `data/catalog/ncbi_names-0005.jsonl.gz:31957` agrees. Complete rows at `data/taxa/PATHS.tsv:14920` and `curation/seed_scope.tsv:322660` confirm the slug and scope; the stored seed-event wording matches.

All four ancestors match the pinned backbone in root-first order: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), environmental samples (48479, NO_RANK). No named phylum, class or genus is omitted from this authority-supported short lineage.

The full [NCBI Taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036411&retmode=xml) agrees with identity, rank, parent, code and lineage labels/ranks; no `OtherNames` element is present. Environmental samples is its division, not a conflicting domain. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036411) confirms all four ancestor IDs, including root omitted from EFetch `LineageEx`. EXACT denotes this clone taxon, not a species inferred from a functional gene.

## Evidence

The NAME count describes one upstream name record, not organisms or cultures. The automated seed event does not claim human review.

Exact Nuccore search `txid1036411[Organism:noexp]` returned UID 336092236. The full [HQ630084.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630084.1) describes a 340-base partial `nosZ` CDS, not 16S. Organism, clone En_UW_25 and `taxon:1036411` agree. Source qualifiers describe environmental DNA from a microbial-fuel-cell anode biofilm and Na2S2O3-supplemented mineral medium. Gene/CDS annotations are partial at both ends, with codon start 3 and translation table 11. No strain, culture-deposit or geographic-location qualifier is present; the Girona submission address is not an isolation locality.

The full linked [AEI00742.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00742.1) describes a 112-amino-acid partial nitrous-oxide reductase produced by conceptual translation. Source identity and medium agree; `coded_by` points to HQ630084.1 with codon start 3 and translation table 11. Both complete sequences and feature tables were read. The PRK02888/CDD:235082 region ends at residue 112 and is annotation rather than a clone-specific assay.

The XML check confirmed 340 declared/actual nucleotide bases, 112 declared/actual protein residues and exact agreement between the submitted 112-residue CDS translation and its own protein sequence. No non-ACGT DNA or X/B/Z/J protein symbols were found. This is submitted-annotation consistency, not independent translation, alignment, reannotation, an assay or evidence of cross-clone equivalence. Neither sequence source establishes substrate utilization, culture purity, electrotrophy or a complete pathway.

The submitted reference "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells" is marked unpublished, with authors Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras. Submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, gives enrichment-derived `nosZ` range HQ630075-HQ630210, containing HQ630084. Exact accession/clone search across all 164 pages' extracted text found no match. Page 92 cautions against inferring purity from one DGGE band. Both full pages were reread. Earlier pages 88-100 and Table 24 supply context, not exact-clone species or physiology assignments; raster figures and supplements were not exhaustively searched.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), inspected earlier in this continuing session, lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current main-text searches found neither HQ630084 nor En_UW_25. It is not an established exact-clone citation; supplements were not exhaustively audited.

## Completeness

No required omission was established. Full exact-target scans found no additional row in seven pinned inventories: BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits. The full backbone has no child row. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These findings are snapshot-bounded.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier, slug and clone-label variants returned four rows, all read as complete parsed TSV/JSON records. Three are backbone, scientific name and scope. The fourth, `data/catalog/gtdb_genomes-0013.jsonl.gz:5110`, is RS_GCF_900125745.1 for Staphylococcus aureus, NCBI taxid 1280, strain 3688STDY6124862. The number 1036411 occurs in contig N50 and scaffold N50/N75, not its taxon fields. This is a numeric collision, not a clone mapping. Its unrelated project and sample were not pursued as target references.

Expansion to HQ630084, AEI00742, the unpublished title and PLOS DOI returned the same four rows. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots. An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report for this stem before writing. No wider absence is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning, not proof that no genome exists. Zero linked BacDive strains agrees with inspected inputs and does not deny sequence evidence. Optional citations, discussion, genes, traits, culture links and graphs can remain empty in this taxonomy-only seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. No wrong identity, broken stored reference, unsupported assertion or required omission was demonstrated. Named-species identity, purity and measured clone-specific activity remain unresolved and appropriately unasserted.

## Recommended Edits

None. Preserve the environmental-clone identity, short authority lineage and SEEDED status. Do not infer species from the partial gene, transfer another clone's qualifiers, attach the numerically matching unrelated GTDB assembly or treat conceptual translation as an assay.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. Transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Do not hand-edit generated YAML.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment needs accession-specific qualifiers and explicit organism/activity evidence. Preserve this accession's Na2S2O3 medium, anode-biofilm origin and partial-sequence scope unless a documented correction establishes otherwise. Accession-range membership and nearest-reference similarity are insufficient for species or clone-specific physiology claims.

After authorized curation, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. Global gates remain unrun here.

## Additional Notes

The review/curation skills, repository guidance and relevant schema classes/enums were read in this unchanged-HEAD continuing session. The review skill and checklist were fully reread this turn. The read-only review contract overrides curation mutations.

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected earlier, including Table 24. This review repeated exact-target text search and complete page 54/92 reading in temporary no-project PyMuPDF. No PDF download, rendering, editing or repository dependency change occurred; this was not a full-thesis audit.

Web query `"En_UW_25" -site:ncbi.nlm.nih.gov/Taxonomy` excluded already-checked taxonomy listings and returned no results. Exact HQ630084 and AEI00742 queries also returned no results. An earlier identical unpublished-title search was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this timestamped report was written for this target. No YAML, maintained source, history, curation event, status or generated product changed. No paid research, outreach, GitHub mutation, refresh or regeneration occurred. Worktrees and Eukaryota were untouched. The pre-report SHA-256 remained `e5b826e52790a358c9ffcc892ec96d0931d9d7eaecc8f7fc677bd1e43569baa9`.
