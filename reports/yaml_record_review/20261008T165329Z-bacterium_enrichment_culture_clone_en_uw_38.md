# YAML Record Review: bacterium enrichment culture clone En_UW_38

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_38.yaml`
- Started UTC: 2026-10-08T16:48:55Z
- Finished UTC: 2026-10-08T16:53:29Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036424`, bacterium enrichment culture clone En_UW_38: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED status. It stores zero linked BacDive strains, one NCBITAXON NAME assertion and one automated seed event dated 2026-09-13.

The authority's species rank does not establish a named species, pure isolate or deposited strain. This review concerns exactly this clone. Eukaryota was untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_38.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_38.yaml --out /private/tmp/uw38-strict.tsv`: passed; one file, zero ERROR files/rows. The complete TSV is header-only.
- Structured comparisons passed for identity, full lineage, attestation, index, scope and seed-event wording. Full public taxonomy, nucleotide, protein, UniProt and UniParc responses were read. Submitted sequence lengths, CDS-translation/protein agreement and the UniParc/NCBI protein-sequence match were checked.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. Bounded comparisons do not replace corpus-only gates.
- Graph checks are not applicable because no graph is stored. iModulonDB was not run: the YAML makes no gene/transcriptomic claim and no identified organism/dataset was established for this clone. This is not a database-coverage absence claim.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222426` agrees with identifier, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31970` agrees. Complete rows at `data/taxa/PATHS.tsv:14933` and `curation/seed_scope.tsv:322673` confirm the slug and scope; seed-event wording matches.

All four ancestors match the pinned root-first lineage: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), environmental samples (48479, NO_RANK). No named phylum, class or genus is omitted from this authority-supported short lineage.

The full [NCBI Taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036424&retmode=xml) agrees with identity, rank, parent, code and lineage labels/ranks; no `OtherNames` element is present. Environmental samples is its division, not a conflicting domain. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036424) confirms all four ancestor IDs, including root omitted from EFetch `LineageEx`. EXACT denotes this clone taxon, not an inferred named species.

## Evidence

The NAME assertion counts one upstream name record, not organisms or cultures. The automated seed event does not claim human review.

Exact Nuccore search `txid1036424[Organism:noexp]` returned UID 336092262. The full [HQ630097.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630097.1) describes a 341-base partial `nosZ` CDS, not 16S. Organism, clone En_UW_38 and `taxon:1036424` agree. Source qualifiers identify environmental DNA from a microbial-fuel-cell anode biofilm and Na2S2O3-supplemented mineral medium. Both CDS ends are partial, with codon start 3 and translation table 11. No strain, culture-deposit or geographic-location qualifier is present; the Girona submission address is not an isolation locality.

The full linked [AEI00755.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00755.1) describes a 113-residue partial nitrous-oxide reductase produced by conceptual translation. Source identity and medium agree; `coded_by` points to HQ630097.1 with codon start 3 and translation table 11. The PRK02888/CDD:235082 region ends at residue 113. These annotations do not establish an enzyme assay, substrate utilization, culture purity, electrotrophy or a complete pathway.

Both full sequences and feature tables were read. XML checks confirmed 341 declared/actual nucleotide bases, 113 declared/actual protein residues and exact agreement between the submitted CDS translation and its own protein. No non-ACGT DNA or X/B/Z/J protein symbols were found. This is submitted-annotation consistency, not independent translation, alignment or reannotation.

The submitted reference, "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells," is marked unpublished, with authors Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras. Submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016.

A clone search surfaced a secondary CNGBdb lead for F8SIS2; the snippet was used only to locate the primary source. The complete [UniProt F8SIS2 response](https://rest.uniprot.org/uniprotkb/F8SIS2.json) marks the entry inactive/deleted because it is not part of a reference proteome, and links UPI0002130E9E. It is not a current active UniProtKB annotation. This YAML does not store that accession, so its deletion is not a broken YAML reference.

The full [UniParc UPI0002130E9E response](https://rest.uniprot.org/uniparc/UPI0002130E9E.json) has an inactive F8SIS2 cross-reference and an active EMBL AEI00755 cross-reference, both explicitly naming this clone and taxon ID. Its complete 113-residue sequence exactly matches AEI00755.1. The same archive also carries En_UW_39 and En_UW_40 cross-references under distinct taxon IDs 1036425 and 1036426. That shared fragment does not prove whole-organism equivalence or justify merging clone taxa. Sequence-family annotations are computational context, not organism-level phenotype evidence.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, gives enrichment-derived `nosZ` range HQ630075-HQ630210, containing HQ630097. Exact accession/clone search across all 164 pages' extracted text found no match. Page 92 cautions against inferring purity from one DGGE band. Both complete pages were reread. Previously inspected pages 88-100 and Table 24 provide context, not exact-clone assignments; raster figures and supplements were not exhaustively searched.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), inspected earlier in this continuing session, lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current main-text searches found neither HQ630097 nor En_UW_38. It is not an established exact-clone citation; supplements were not exhaustively audited.

## Completeness

No required omission was established. Full exact-target scans found no additional row in seven pinned inventories: BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits. The full backbone has no child row. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These findings are snapshot-bounded.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier, slug and clone-label variants returned six rows, all read completely. Three are the backbone, scientific-name and scope rows above. The others are unrelated numeric matches:

- `data/catalog/ncbi_genbank-0064.jsonl.gz:2184`: GCA_965036285.1, Candidatus Planktophila sp., taxon/species ID 2175601, isolate PELAGICS-MAG-m2-bin117206-RIMVE-SM-04apr22. Both genome lengths are 1036424; its taxonomy is not the target.
- `data/catalog/gtdb_genomes-0006.jsonl.gz:11510`: RS_GCF_044756905.1, Streptomyces sp. NPDC091406, taxon/species ID 3366001, classified by GTDB as Streptomyces durocortorensis. The matching 1036424 is scaffold N50, not its taxon ID or total genome length (7981881).
- `data/catalog/ncbi_genbank-0054.jsonl.gz:17265`: GCA_058711105.1, Streptococcus pneumoniae, taxon/species ID 1313. Its isolate code is 1036424; its genome length is 2089221. It is not this environmental clone.

Expansion to HQ630097, AEI00755, F8SIS2, UPI0002130E9E, the unpublished title and PLOS DOI returned the same six rows. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots.

An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report before writing. No wider absence is claimed. Exact-taxonomy Assembly search returned zero with a phrase-not-found warning, not proof that no genome exists.

Zero linked BacDive strains agrees with inspected inputs and does not deny sequence evidence. Optional citations, discussion, genes, traits, culture links and graphs can remain empty in this taxonomy-only seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. No wrong identity, broken stored reference, unsupported assertion or required omission was demonstrated. Named-species identity, culture purity and measured clone-specific activity remain unresolved and appropriately unasserted. The inactive external UniProt entry is not referenced by the YAML.

## Recommended Edits

None. Preserve the environmental-clone identity, short authority lineage and SEEDED status. Do not infer species from the partial gene, merge clone taxa because of an identical fragment, transfer another clone's qualifiers or treat conceptual translation as an assay.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. Transformation defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Do not hand-edit generated YAML.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment needs accession-specific qualifiers and explicit organism/activity evidence. Preserve the partial-sequence scope and distinguish inactive UniProtKB accessions from retained UniParc sequence evidence. Accession-range membership and shared fragment sequence are insufficient for species or clone-specific physiology claims.

After authorized curation, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. Global gates remain unrun here.

## Additional Notes

The review/curation skills, repository guidance and relevant schema classes/enums were read earlier in this unchanged-HEAD continuing session. The local checklist was fully reread for this target. The read-only review contract overrides curation mutations.

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected earlier, including Table 24. This review repeated exact-target text search and complete page 54/92 reading in temporary no-project PyMuPDF. No PDF download, rendering, editing or repository dependency change occurred; this was not a full-thesis audit.

Web query `"En_UW_38" -site:ncbi.nlm.nih.gov/Taxonomy` excluded already-checked taxonomy listings and returned the CNGBdb lead described above. Exact HQ630097 and AEI00755 queries returned no results. An earlier unpublished-title search was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this timestamped report was written for this target. No YAML, maintained source, history, curation event, status or generated product changed. No paid research, outreach, GitHub mutation, refresh or regeneration occurred. Worktrees and Eukaryota were untouched. The pre-report SHA-256 remained `699bb46a01a60af185c65cbcdf6d1f3c2e60d89719e41a15647a4d2815f59994`.
