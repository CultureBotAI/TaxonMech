# YAML Record Review: bacterium enrichment culture clone En_UW_33

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_33.yaml`
- Started UTC: 2026-10-08T16:13:09Z
- Finished UTC: 2026-10-08T16:24:15Z
- Verdict: pass

## Target

The entire YAML was read before judgment and reread on resumption. This generated `TaxonRecord` denotes `NCBITaxon:1036419`, bacterium enrichment culture clone En_UW_33: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED status. It contains zero linked BacDive strains, one NCBITAXON NAME assertion and one automated seed event dated 2026-09-13.

The authority's species rank does not establish a named species, pure culture or deposited strain. This review concerns exactly this clone. Eukaryota was untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_33.yaml`: passed, no issues found; repeated after resumption.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_33.yaml --out /private/tmp/uw33-strict.tsv`: passed; one file, zero ERROR files/rows. The complete TSV is header-only; repeated after resumption.
- Structured comparisons passed for identity, full lineage, source attestation, index, scope and seed-event wording. Full public taxonomy and sequence responses were inspected; submitted sequence lengths and CDS-translation/protein agreement were checked.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. Bounded comparisons do not replace corpus-only gates.
- Graph checks are not applicable because no graph is stored. iModulonDB was not run: the YAML makes no gene/transcriptomic claim, and no identified organism/dataset was established for this environmental clone. This is not a database-coverage absence claim.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222421` agrees with identifier, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31965` agrees. Complete rows at `data/taxa/PATHS.tsv:14928` and `curation/seed_scope.tsv:322668` confirm the slug and scope; the stored seed-event wording matches.

All four ancestors match the pinned root-first lineage: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), environmental samples (48479, NO_RANK). No named phylum, class or genus is omitted from this authority-supported short lineage.

The full [NCBI Taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036419&retmode=xml) agrees with identity, rank, parent, code and lineage labels/ranks; no `OtherNames` element is present. Environmental samples is its division, not a conflicting domain. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036419) confirms all four ancestor IDs, including root omitted from EFetch `LineageEx`. EXACT denotes the clone taxon, not an inferred named species.

## Evidence

The NAME assertion counts one upstream name record, not organisms or cultures. The automated seed event does not claim human review.

Exact Nuccore search `txid1036419[Organism:noexp]` returned UID 336092252. The full [HQ630092.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630092.1) describes a 333-base partial `nosZ` CDS, not 16S. Organism, clone En_UW_33 and `taxon:1036419` agree. Source qualifiers identify environmental DNA from a microbial-fuel-cell anode biofilm and Na2S2O3-supplemented mineral medium. Both CDS ends are partial, with codon start 3 and translation table 11. No strain, culture-deposit or geographic-location qualifier is present; the Girona submission address is not an isolation locality.

The full linked [AEI00750.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00750.1) describes a 110-residue partial nitrous-oxide reductase produced by conceptual translation. Source identity and medium agree; `coded_by` points to HQ630092.1 with codon start 3 and translation table 11. The PRK02888/CDD:235082 region ends at residue 110. These annotations do not establish an enzyme assay, culture purity, electrotrophy or a complete pathway.

Both full sequences and feature tables were read. XML checks confirmed 333 declared/actual nucleotide bases, 110 declared/actual protein residues and exact agreement between the submitted CDS translation and its own protein. The DNA contains an ambiguous R at position 39, and the protein contains X at residue 13. This is submitted-annotation consistency, not independent translation, alignment or reannotation. The ambiguity is an external sequence limitation, not a defect in this taxonomy-only YAML, which asserts no sequence or functional result.

The sequence reference, "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells," is marked unpublished, with authors Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras. Submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, gives enrichment-derived `nosZ` range HQ630075-HQ630210, containing HQ630092. Exact accession/clone search across all 164 pages' extracted text found no match. Page 92 cautions against inferring purity from one DGGE band. Both complete pages were reread. Previously inspected pages 88-100 and Table 24 provide context, not exact-clone assignments; raster figures and supplements were not exhaustively searched.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), inspected earlier in this continuing session, lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current main-text searches found neither HQ630092 nor En_UW_33. It is not an established exact-clone citation; supplements were not exhaustively audited.

## Completeness

No required omission was established. Full exact-target scans found no additional row in seven pinned inventories: BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits. The full backbone has no child row. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These findings are snapshot-bounded.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier, slug and clone-label variants returned five rows, all read completely. Three are the backbone, scientific-name and scope rows above. The other two describe the same unrelated assembly, GCA_038114325.1, in `data/catalog/gtdb_genomes-0010.jsonl.gz:908` and `data/catalog/ncbi_genbank-0035.jsonl.gz:33686`. Their total genome length is 1036419, but both taxon/species IDs are 2026775 and their isolate is 139539_COM_maxbin_bins.tsv.134. GTDB's row names Pelagibacteraceae bacterium and classifies it as Pelagilacustribacter brisbanensis; GenBank names Candidatus Pelagibacteraceae bacterium. These are numeric collisions and naming differences concerning another organism, not target genome links or a target taxonomy conflict.

Expansion to HQ630092, AEI00750, the unpublished title and PLOS DOI returned the same five rows. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots. An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report before writing. No wider absence is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning, not proof that no genome exists. Zero linked BacDive strains agrees with inspected inputs and does not deny sequence evidence. Optional citations, discussion, genes, traits, culture links and graphs can remain empty in this taxonomy-only seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. No wrong identity, broken stored reference, unsupported assertion or required omission was demonstrated. Named-species identity, culture purity and measured clone-specific activity remain unresolved and appropriately unasserted. Sequence ambiguity does not contradict a stored YAML claim.

## Recommended Edits

None. Preserve the environmental-clone identity, authority lineage and SEEDED status. Do not infer species or physiology from the partial gene, transfer another clone's qualifiers or treat conceptual translation as an assay.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. Transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Do not hand-edit generated YAML.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment would need accession-specific evidence and must preserve this fragment's partial status and ambiguity. Accession-range membership and nearest-reference similarity are insufficient for species or clone-specific physiology claims.

After authorized curation, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. Global gates remain unrun here.

## Additional Notes

The review/curation skills, local checklist, `CLAUDE.md` and `justfile` were reread on resumption. Other curation, harmonization, schema and history guidance and relevant schema classes/enums were read earlier in this unchanged-HEAD continuing session. The read-only review contract overrides curation mutations.

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected earlier, including Table 24. This review repeated exact-target text search and complete page 54/92 reading with temporary no-project PyMuPDF. No PDF download, rendering, editing or repository dependency change occurred; this was not a full-thesis audit.

The exact clone web query excluded already-checked NCBI Taxonomy listings and returned no results. Exact HQ630092 and AEI00750 queries also returned no results. An earlier unpublished-title search was reused as context, not represented as a new query. No universal publication-absence claim is made. The previously running exact NCBI search handle was resumed to completion rather than restarted.

Only this timestamped report was written for this target. No YAML, maintained source, history, curation event, status or generated product changed. No paid research, outreach, GitHub mutation, refresh or regeneration occurred. Worktrees and Eukaryota were untouched. The pre-report SHA-256 remained `dedf456c9fbb17d887de5dae0c5b220a2eeac32aa3f830c9b7a27c723c54d34e`.
