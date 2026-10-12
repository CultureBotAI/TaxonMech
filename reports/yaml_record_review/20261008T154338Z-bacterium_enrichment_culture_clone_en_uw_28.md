# YAML Record Review: bacterium enrichment culture clone En_UW_28

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_28.yaml`
- Started UTC: 2026-10-08T15:33:04Z
- Finished UTC: 2026-10-08T15:43:38Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036414`, bacterium enrichment culture clone En_UW_28: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED status. It stores zero linked BacDive strains, one NCBITAXON NAME assertion and one automated seed event dated 2026-09-13.

NCBI's species rank does not establish a named species, pure isolate or deposited strain. The target is this clone, not the entire enrichment culture or a different clone recovered from that culture. Eukaryota was untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_28.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_28.yaml --out /private/tmp/uw28-strict.tsv`: passed; one file, zero ERROR files/rows. The complete TSV is header-only.
- Structured comparisons passed for identity, full lineage, attestation, index, scope and seed-event wording. Full public taxonomy and sequence responses were inspected; submitted sequence lengths and translation/protein agreement were checked.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. Bounded comparisons do not replace corpus-only checks.
- Graph checks are not applicable: no graph is stored. iModulonDB was not run because the YAML makes no gene/transcriptomic claim and no identified organism/dataset was established for this unidentified clone. This is not a database-coverage absence claim.
- Literature limitation: the newly located Lebrero manuscript's relevant table could not be inspected visually. Initial manuscript text was partially readable, but subsequent web retrieval/find/screenshot attempts failed and direct download exhausted three connection attempts with curl exit 28. Its search snippet was treated only as a lead; independent NCBI records were inspected instead.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222416` agrees with identifier, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31960` agrees. Complete rows at `data/taxa/PATHS.tsv:14923` and `curation/seed_scope.tsv:322663` confirm the slug and scope; stored seed-event wording matches.

All four ancestors match the pinned root-first lineage: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), environmental samples (48479, NO_RANK). No named phylum, class or genus is missing from this authority-supported short lineage.

The full [NCBI Taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036414&retmode=xml) agrees with identity, rank, parent, code and lineage labels/ranks; no `OtherNames` element is present. Environmental samples is its division, not a conflicting domain. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036414) confirms all four ancestor IDs, including root omitted from EFetch `LineageEx`. EXACT denotes this clone taxon, not a species or genus inferred from enrichment-culture membership.

## Evidence

The NAME assertion counts one upstream name record, not organisms or cultures. The automated seed event does not claim human review.

Exact Nuccore search `txid1036414[Organism:noexp]` returned UID 336092242. The full [HQ630087.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630087.1) describes a 340-base partial `nosZ` CDS, not 16S. Organism, clone En_UW_28 and `taxon:1036414` agree. Source qualifiers identify environmental DNA from a microbial-fuel-cell anode biofilm and Na2S2O3-supplemented mineral medium. Both CDS ends are partial, with codon start 3 and translation table 11. No strain, culture-deposit or geographic-location qualifier is present; the Girona submission address is not an isolation locality.

The full linked [AEI00745.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00745.1) describes a 112-residue partial nitrous-oxide reductase produced by conceptual translation. Source identity and medium agree; `coded_by` points to HQ630087.1 with codon start 3 and translation table 11. The PRK02888/CDD:235082 region ends at residue 112. Both full sequences and feature tables were read. These annotations do not establish an enzyme assay, substrate utilization, culture purity, electrotrophy or a complete pathway.

XML checks confirmed 340 declared/actual nucleotide bases, 112 declared/actual protein residues and exact agreement between the submitted CDS translation and its own protein. No non-ACGT DNA or X/B/Z/J protein symbols were found. This checks submitted-annotation consistency only, not independent translation, alignment or reannotation.

The submitted reference, "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells," is marked unpublished, with authors Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras. Submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, gives enrichment-derived `nosZ` range HQ630075-HQ630210, containing HQ630087. Exact HQ630087, En_UW_28, HQ694759 and E98 searches across all 164 pages' extracted text found no match. Page 92 cautions against inferring purity from one DGGE band. Both complete pages were reread. Previously inspected pages 88-100 and Table 24 supply context, not exact-clone assignments; raster figures and supplements were not exhaustively searched.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), inspected earlier in this continuing session, lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current main-text searches found neither HQ630087 nor En_UW_28. It is not an established exact-clone citation; supplements were not exhaustively audited.

The clone-name search surfaced a [Lebrero manuscript](https://uvadoc.uva.es/bitstream/10324/23453/1/Lebrero-et-al-2017-JEMA.pdf) whose search snippet mentions En_UW_28 and HQ694759 in a DGGE comparison table. Title, abstract and early methods text were initially readable; the table itself remains unverified because of the access failures above. The full [PubMed record](https://pubmed.ncbi.nlm.nih.gov/27623370/) confirms PMID 27623370, DOI 10.1016/j.jenvman.2016.09.016, publication in 2016, and a community-scale toluene-biodegradation study. The repository PDF's 2017 filename is not its publication year. No table percentage or clone-specific activity is asserted from the snippet.

Following that lead independently, the full [HQ694759.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ694759.1) was inspected, including features and sequence. It is a 904-base partial 16S rRNA sequence for Azospirillum sp. enrichment culture clone E98, `taxon:1109680`, with clone qualifier E98. Its isolation-source qualifier explicitly names autotrophic enrichment culture En_UW_28 and Na2S2O3 as electron donor. It has a different unpublished submitted reference concerning isolates from microbial-fuel-cell anodes and cathodes, submitted 02-DEC-2010. The complete [E98 taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1109680&retmode=xml) and NCBI Datasets response confirm that distinct taxon under Azospirillum.

This establishes a culture-context lead, not identity between E98's 16S sequence and this taxon's `nosZ` clone. Neither inspected accession cross-links the other, and the inspected material does not establish organism-level co-occurrence of these two genes in a pure isolate. Do not merge the taxa, assign Azospirillum to this YAML, or transfer community-level toluene results to it. The separate E98 taxon was checked only to disambiguate this review, not given its own review verdict.

## Completeness

No required omission was established. Complete exact-target scans found no additional row in the pinned BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin or BactoTraits inventories. The full backbone has no child row. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These findings are snapshot-bounded.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier, slug and clone-label variants returned four rows, all inspected as complete parsed TSV/JSON records. Three are backbone, scientific name and scope. The fourth, `data/catalog/ncbi_genbank-0051.jsonl.gz:31444`, is GCA_055876345.1, Nitrospirota bacterium, taxid/species taxid 2026887, isolate HHBFW-2_201803_bins_282. Its ungapped genome size is 1036414; its genome size is 1036578. This is a numeric collision, not a target mapping. Its unrelated project/sample references were not pursued as clone evidence.

Expansion to HQ630087, AEI00745, HQ694759, the unpublished title, PLOS DOI, Lebrero DOI and PMID 27623370 returned the same four rows. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots. An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report for this stem before writing. No wider absence is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning, not proof that no genome exists. Zero linked BacDive strains agrees with inspected inputs and does not deny sequence evidence. Optional citations, discussion, genes, traits, culture links and graphs can remain empty in this taxonomy-only seed; the culture-context lead does not make a required field missing.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. No wrong identity, broken stored reference, unsupported assertion or required omission was demonstrated. Named-species identity, pure-culture status and organism-level linkage to E98 remain unresolved and appropriately unasserted. The inaccessible literature table limits optional enrichment, not verification of the claims currently stored.

## Recommended Edits

None required. Preserve the environmental-clone identity, authority lineage and SEEDED status. Do not attach the numerically matching assembly or merge this taxon with E98 based on a shared enrichment label.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. Transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Do not hand-edit generated YAML.

## Follow-up Checks

None required for the current taxonomy-only verdict. For separately authorized enrichment, inspect the complete Lebrero Table 1 and its sequence methods when accessible, and seek explicit accession-to-organism evidence linking HQ630087 to HQ694759. A shared culture label, nearest-reference similarity or culture-wide activity alone is insufficient. Preserve the distinction between the `nosZ` clone, E98 and the enrichment culture.

After authorized curation, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. Global gates remain unrun here.

## Additional Notes

The review/curation skills, repository guidance and relevant schema classes/enums were read in this unchanged-HEAD continuing session. The review skill was reread this turn; the checklist was reread for this target. The read-only review contract overrides curation mutations. The PDF skill was reread for the new manuscript lead.

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected earlier, including Table 24. This review repeated exact-target/lead text searches and complete page 54/92 reading in temporary no-project PyMuPDF. The new manuscript download to temporary storage failed; no manuscript rendering was completed. No PDF was edited and no repository dependency changed.

Web query `"En_UW_28" -site:ncbi.nlm.nih.gov/Taxonomy` excluded already-checked taxonomy listings and produced the manuscript lead. Exact HQ630087 and AEI00745 queries returned no results. The title search was restricted to primary publisher/repository/PubMed domains and led to the independently read PubMed XML. Failed web finds against the manuscript are access errors, not verified text absences. An earlier unpublished-title search was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this timestamped report was written for this target. No YAML, maintained source, history, curation event, status or generated product changed. No paid research, outreach, GitHub mutation, refresh or regeneration occurred. Worktrees and Eukaryota were untouched. The pre-report SHA-256 remained `8377f8f3a7c6ae6842de91a0d067f1e479a43e5e6581af0916d80220181d5143`.
