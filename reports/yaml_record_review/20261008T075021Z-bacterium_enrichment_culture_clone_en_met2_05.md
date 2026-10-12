# YAML Record Review: bacterium enrichment culture clone En_MET2_05

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_05.yaml`
- Started UTC: 2026-10-08T07:45:58Z
- Finished UTC: 2026-10-08T07:50:21Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036341`, bacterium enrichment culture clone En_MET2_05: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED mapping status. It has zero linked BacDive strains, one NCBITAXON NAME assertion and one seed event dated 2026-09-13.

The ID, label and stem resolve one environmental enrichment-culture clone, not a named species, demonstrated pure isolate, culture deposit or whole community. NCBI's species rank does not establish those broader identities. This report covers only this YAML; Eukaryota was untouched.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_05.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_05.yaml --out /private/tmp/em205-strict.tsv`: passed; one file, zero ERROR files/rows. The inspected TSV contains only its header.
- Read-only structured comparisons matched the full pinned backbone row, every ancestor ID/label/rank/order, attestation, path index, scope membership and seed-event text. These bounded comparisons are not corpus reproduction.
- Live checks inspected NCBI Taxonomy EFetch, Datasets, and full nucleotide/protein entries.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. No focused replacement for a corpus-only gate is claimed.
- Graph validation is not applicable: no graph is present. iModulonDB was not run because the YAML asserts no gene or transcriptomic finding and the supplementary sequence belongs to an unidentified clone without an identified organism/dataset for expression-module comparison. This is not negative database-coverage evidence.

## Identity and Grounding

The full row at `data/raw/ncbitaxon_taxa.tsv:222343` matches ID, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete name row at `data/catalog/ncbi_names-0005.jsonl.gz:31887` confirms identity. `data/taxa/PATHS.tsv:14850` maps the ID to this stem; `curation/seed_scope.tsv:322590` supports membership and seed-event wording.

All four root-first ancestors match the pinned source: root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), environmental samples (48479, NO_RANK). Absent phylum/class/genus assignments reflect authority placement, not omitted YAML entries.

The inspected [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036341&retmode=xml) agrees with name, rank, parent, code and lineage labels/ranks; it has no `OtherNames` element. Its Environmental samples division is distinct from taxonomic domain and does not contradict BACTERIA. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036341) confirms root-inclusive ID order; EFetch omits root from `LineageEx`. EXACT identifies this clone taxon, not a named species inferred from a gene.

## Evidence

The sole attestation correctly counts one NAME assertion, not organisms or cultures. The seed event documents automated provenance without implying human review.

Exact Nuccore query `txid1036341[Organism:noexp]` returned UID 336092346. The complete [HQ630139.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630139.1) is a 341-base partial `nosZ` CDS, not a 16S sequence. Its source gives exact organism, clone En_MET2_05 and `taxon:1036341`, an environmental-sample flag and microbial-fuel-cell cathode isolation source. Its medium note specifies Na2S2O3 supplementation, not H2. Gene/CDS features are partial at both ends, with codon start 3 and translation table 11.

The complete linked [AEI00797.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00797.1) is a 113-amino-acid partial nitrous-oxide reductase explicitly produced by conceptual translation. Source qualifiers agree, including the Na2S2O3 note, and `coded_by` points back to HQ630139.1. Both full sequences and feature tables were inspected. No independent reannotation or biochemical assay was performed. A partial gene annotation and medium note do not establish measured enzyme activity, substrate utilization, a complete denitrification pathway, pure-culture physiology or electrotrophy.

Parsed nucleotide-string comparison found HQ630139.1 identical to [HQ630106.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ630106.1), the En_MET2_04 entry inspected previously. The entries have different clone/taxon identities and different medium notes. Sequence equality does not authorize transferring the H2 condition or merging these TaxonRecords. No deduplication or synonym assertion was made.

The submitted reference, "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells", is marked unpublished and lists Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras as submitted. Direct submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016. The source feature has no strain, culture-deposit or geographic-location qualifier. The Girona institutional address is not an isolation location.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5) lists enrichment-derived `nosZ` accessions HQ630075-HQ630210 on printed page 54, a range containing HQ630139. Printed page 92 cautions that even a single DGGE band does not prove purity. Both complete pages were reread for this target. Searching all 164 pages' extracted text found no exact HQ630139 or En_MET2_05 match, without establishing absence from raster figures or uninspected supplements. Relevant pages 88-100 and Table 24 had been inspected earlier in this continuing session. The table's band-position/reference similarities do not establish exact clone-to-species identity. Range membership supports study context, not transfer of a reference species or community performance to the clone.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), DOI `10.1371/journal.pone.0063460`, was inspected earlier in this session and lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current searches of retrieved main-article text found neither HQ630139 nor En_MET2_05. It is not an established exact-clone citation; supplements were not exhaustively audited.

## Completeness

No required-field omission was found. Full exact-target scans of seven pinned inventories (BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits) found no additional target row. Full backbone scanning found no child; exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These findings are snapshot-bounded.

Compressed-aware `rg --no-ignore --hidden -z` included ignored/hidden files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxon number, slug and clone-label variants yielded six rows. Expansion to HQ630139, AEI00797, the unpublished title and the PLOS DOI yielded the same six. All were read as complete parsed TSV/JSON records. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots.

Three rows support identity (backbone, scientific name and scope). The other three are numeric coincidences, not target genome evidence:

- `data/catalog/ncbi_genbank-0025.jsonl.gz:4598`: GCA_027011185.1 is Flavobacteriales bacterium, taxon 2021391, isolate 132-544_metabat2_scaf2bin.083. Genome size and ungapped size equal 1036341.
- `data/catalog/ncbi_genbank-0035.jsonl.gz:35356`: GCA_038147535.1 is Gammaproteobacteria bacterium, taxon 1913989, isolate SD9012_S6_metabat_bins_sens.tsv.092. Its ungapped size equals 1036341, while total size is 1040141.
- `data/catalog/gtdb_genomes-0011.jsonl.gz:39876`: GB_GCA_038147535.1 is the same second assembly, with `ncbi_taxid` 1913989 and `ncbi_ungapped_length` 1036341. GTDB places it in VMDH01 sp008080945.

These unrelated assemblies and their linked publications were not independently audited; none supplies a target mapping, phenotype or target NCBI-versus-GTDB conflict.

An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report for its stem before this report was written. No absence beyond the named roots is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning, not proof that no genome exists. Zero BacDive strains agrees with the inspected inputs and does not deny sequence evidence. Optional literature, discussion, culture links, gene/trait assertions and graphs may remain empty: supplementary annotation does not establish a required missing representation.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. No wrong identity, broken stored reference, unsupported assertion or missing required representation was established. Named-species identity, culture purity and measured clone-specific activity remain unresolved and appropriately unasserted.

## Recommended Edits

None. Preserve the distinct environmental-clone identity, authority lineage and SEEDED status. Do not attach unrelated metric-matched genomes, transfer another clone's H2 medium note, infer species identity from a shared partial gene, or treat conceptual translation as a functional assay.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. A seed defect belongs in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect is established here. Do not hand-edit generated YAML to bypass maintained inputs.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment should preserve the accession-specific medium/source qualifiers and distinguish annotation from experimental function. Organism/activity claims require explicit linkage and direct evidence at that scope, not range membership or a shared short marker.

After an authorized curation change, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. The global gates remain unrun here.

## Additional Notes

The dissertation was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected in the earlier review sequence, including both pages of Table 24. This review repeated exact-target text search and complete page 54/92 reading using PyMuPDF in the existing temporary no-project environment. No new download/rendering, PDF edit or repository dependency change occurred; this is not a full-thesis or exhaustive figure/supplement audit.

Exact-label web searches yielded taxonomy listings and an uninspected patent lead, not additional evidence used for a claim. Exact accession/protein searches returned no results. The identical unpublished-title search from an earlier review was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this new timestamped report was written for the target. No YAML, maintained source, curation event, history, status or generated product was changed. No paid research, outreach, GitHub mutation, refresh or regeneration occurred. Existing worktrees and Eukaryota were untouched. The target SHA-256 remained `90772d8ecb17f580db3e3cf3dd88b21bfc80686bb7d2a4dbd77458eec289ba77` through the pre-report check.
