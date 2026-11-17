# YAML Record Review: bacterium enrichment culture clone En_MET2_03

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_03.yaml`
- Started UTC: 2026-10-08T07:31:39Z
- Finished UTC: 2026-10-08T07:35:58Z
- Verdict: pass

## Target

The entire YAML was read before judgment. This generated `TaxonRecord` is `NCBITaxon:1036339`, bacterium enrichment culture clone En_MET2_03: SPECIES rank, BACTERIA domain, parent `NCBITaxon:48479` (environmental samples), genetic code 11, EXACT grounding and SEEDED mapping status. It has zero linked BacDive strains, one NCBITAXON NAME assertion and one seed event dated 2026-09-13.

The identifier, label and stem uniquely resolve this environmental enrichment-culture clone. NCBI's species rank does not make it a named species, deposited strain, demonstrated pure isolate or whole enrichment community. This report reviews only this YAML; Eukaryota was left alone.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_03.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_met2_03.yaml --out /private/tmp/em203-strict.tsv`: passed, one file scanned, zero ERROR files/rows. The output TSV was read and contains only its header.
- Read-only structured comparisons matched the complete pinned backbone row, every ancestor ID/label/rank/order, attestation, path index, scope membership and seed-event wording. These bounded checks do not replace corpus reproduction.
- Live checks inspected NCBI Taxonomy EFetch and Datasets, plus complete nucleotide and linked protein records.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests and rendering/site/docs builds. No focused equivalent of a corpus-only gate is claimed.
- Graph validation is not applicable because the YAML contains no graph. iModulonDB was not run: the YAML has no gene or transcriptomic claim, and supplementary sequence evidence concerns an unidentified clone without an identified organism/dataset for expression-module comparison. This is not negative evidence about database coverage.

## Identity and Grounding

The full row at `data/raw/ncbitaxon_taxa.tsv:222341` agrees with ID, label, rank, parent, genetic code and 2026-09-13 snapshot. Empty synonym fields agree with the YAML. The full scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31885` confirms the same identity. `data/taxa/PATHS.tsv:14848` maps the ID to this stem; `curation/seed_scope.tsv:322588` supports membership and seed-event text.

The complete root-first lineage is root (1, NO_RANK), cellular organisms (131567, CELLULAR_ROOT), Bacteria (2, DOMAIN), environmental samples (48479, NO_RANK). All four entries match the pinned backbone. The lack of phylum/class/genus entries reflects the authority's placement, not an incomplete YAML chain.

The inspected [Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036339&retmode=xml) agrees with the current name, species rank, parent, code and lineage labels/ranks; it has no `OtherNames` element. Its Environmental samples division is distinct from taxonomic domain and does not conflict with BACTERIA. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036339) confirms the root-inclusive ID order; EFetch omits root from `LineageEx`. EXACT means this clone's NCBI identity, not a named-species assignment inferred from a gene.

## Evidence

The attestation correctly counts one NAME assertion. It does not count biological organisms or cultures. The seed event documents automated provenance without implying human review.

Exact Nuccore query `txid1036339[Organism:noexp]` returned UID 336092278. The full inspected [HQ630105.1 record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630105.1) is a 341-base partial `nosZ` CDS, not a 16S sequence. Its source gives exact organism, clone En_MET2_03 and `taxon:1036339`, an environmental-sample flag, a microbial-fuel-cell cathode isolation source, and an H2-supplemented mineral-medium note. Gene/CDS coordinates are partial at both ends; codon start is 3 and translation table is 11.

The linked [AEI00763.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00763.1), read in full, is a 113-amino-acid partial nitrous-oxide reductase explicitly produced by conceptual translation. It links back to HQ630105.1 and matches the clone/taxon/source qualifiers. Both full sequences and feature tables were read; no independent alignment, reannotation or biochemical assay was performed. This supports an annotated partial functional-gene sequence, not demonstrated enzyme activity, a complete denitrification pathway, pure-culture physiology or electrotrophy.

The submitted reference, "Enrichments of chemolithoautotrophic denitrifiers from microbial fuel cells", is marked unpublished and lists Vilar-Sanz, Garcia-Lledo, Puig, Balaguer, Jesus and Baneras as submitted. Direct submission is dated 17-NOV-2010; sequence creation is 20-JUN-2011 and update 25-JUL-2016. No strain, culture-deposit or geographic-location qualifier occurs in the inspected source feature. The submitting institution's Girona address is not an isolation location.

Ariadna Vilar Sanz's [2015 dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), on nitrite respiration and electrotrophy, lists enrichment-derived `nosZ` accessions HQ630075-HQ630210 on printed page 54; HQ630105 lies in that range. Printed page 92 warns that even a single DGGE band does not assure culture purity. Both complete pages were reread for this target. Searching all 164 pages' extracted text found neither exact HQ630105 nor En_MET2_03; raster figures and supplements are not covered by that negative result. Relevant pages 88-100 and Table 24 were inspected earlier in this continuing session. The table's band-position similarities do not establish an exact clone-to-species identity. The accession range is a study-context link, not justification to transfer community activity or a reference species name to the clone.

The related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460), DOI `10.1371/journal.pone.0063460`, was inspected earlier in this session. It lists different JX accessions, including JX237213-JX237355 for `nosZ`. Current searches of the retrieved main article found neither HQ630105 nor En_MET2_03. It is not an established exact-clone citation; supplements were not exhaustively audited.

## Completeness

No required-field omission was established. Full exact-target scans of seven pinned inventories (BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin and BactoTraits) found no additional target row. Full backbone scanning found no child; exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. These are snapshot-bounded findings.

Compressed-aware `rg --no-ignore --hidden -z` searched ignored/hidden files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxon number, slug and clone-label variants found only the backbone, name and scope rows above. Expanding to HQ630105, AEI00763, the unpublished title and the PLOS DOI yielded the same three rows. All were read as complete parsed TSV/JSON records. Five `SOURCE.json` files were separately parsed without an identity match; history filename/content searches found no target entry within these roots.

An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found the one target YAML and no prior report for its stem before this report was created. No absence beyond the bounded roots is claimed.

Exact-taxonomy Assembly search returned zero with a phrase-not-found warning; this is not proof that no genome exists. Zero BacDive strains agrees with pinned inputs and does not deny sequence evidence. Optional literature, discussion, gene/trait assertions, culture links and graphs can remain empty. No required representation is missing merely because supplementary annotation evidence exists.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. No wrong identity, broken stored reference, unsupported assertion or missing required representation was established. Named-species identity, culture purity and measured clone-specific activity remain unresolved, appropriately unasserted by the record.

## Recommended Edits

None. Preserve the environmental-clone identity, authority lineage and SEEDED status. Do not infer a named species from partial `nosZ` evidence, a pure culture from DGGE, or measured activity from conceptual translation.

A future confirmed taxonomy correction belongs first at NCBI, then in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py` through documented refresh/seed commands. A seed transformation defect belongs in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. No such defect was found. Generated YAML should not be hand-edited to bypass maintained inputs.

## Follow-up Checks

None required for this verdict. Separately authorized enrichment should preserve accession-level provenance and distinguish annotation from direct functional evidence. New organism/activity claims require explicit clone-to-organism linkage and evidence at that scope, not range membership or nearest-reference similarity alone.

After any authorized curation change, rerun both focused validators and applicable corpus, provenance, history and generated-product gates. The global gates remain unrun here.

## Additional Notes

The PDF was reused from `/private/tmp/em201-thesis.pdf`, previously downloaded over verified TLS. Printed pages 54, 92, 95 and 96 had been rendered and visually inspected during the preceding individual review sequence, including both pages of Table 24. This review repeated exact-target text search and complete page 54/92 reading with PyMuPDF in the existing temporary no-project environment; no new download, rendering, dependency change or PDF edit occurred. This was not a full-thesis or exhaustive figure/supplement audit.

Exact-label web searches yielded taxonomy leads, not additional inspected clone-specific research; exact accession/protein searches returned no results. The identical unpublished-title search from the earlier review was reused as context, not represented as a new query. No universal publication-absence claim is made.

Only this new timestamped review report was written. No YAML, source, curation event, history, status or generated product was changed; no paid research, outreach, GitHub mutation, source refresh or regeneration occurred. Worktrees and Eukaryota remain untouched. The target SHA-256 remained `0d75afe9682ccc159ad0513c470f4ad4ff5e8758e5c988b3f4582681d596d42e` through the pre-report check.
