# YAML Record Review: Deinococcus sp. LT7CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/deinococcus_sp_lt7cd.yaml`
- Started UTC: 2026-10-06T01:03:32Z
- Finished UTC: 2026-10-06T01:05:30Z
- Verdict: pass

## Target

Reviewed the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034910`, label `Deinococcus sp. LT7CD`, rank `SPECIES`, domain `BACTERIA`. It has parent `NCBITaxon:2623546`, ten root-first ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, and `strain_count: 0`. It contains one NCBITAXON NAME attestation and one embedded seed event. There are no synonyms, nomenclature entries, mappings, listed strains, literature evidence, discussions, or causal graphs.

The resolved target is the exact NCBI node bearing the LT7CD designation, not every Deinococcus isolate or a named species inferred from relatedness. The species rank is NCBI's; it does not itself establish a formally described species or a culture-collection deposit.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/deinococcus_sp_lt7cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/deinococcus_sp_lt7cd.yaml --out /private/tmp/lt7cd-validation.tsv`: exit 0; one file, zero errors. The complete TSV contains only its header.
- The complete backbone row, all lineage entries, seven inventories, PATHS entry, scope row, attestation, and embedded event were compared using structured readers. All comparisons passed. These bounded checks do not claim full corpus reproduction.
- Every ignored-inclusive candidate address was resolved to its full native JSON or header-aware TSV row; the backbone and scope were read by the source-comparison check. Live Taxonomy EFetch/Datasets, exact sequence-index responses, and the entire GenBank metadata object were inspected.
- Not checked: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, full history validation, provenance hashes, render drift, README statistics, publication budget, and vendored sync. These wider gates were not run for a report-only review, and no replacement focused validator is claimed.
- LPSN/GTDB identifier checks, causal-edge review, and iModulonDB are not applicable to this record's assertions. No corresponding mapping, nomenclature identifier, graph, gene-function claim, regulator, or expression module is present.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221738` agrees with the record on ID, exact label, species rank, parent, genetic code, and taxonomy snapshot. The full scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31141` supplies the same name and `NCBITaxon:1034910`.

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034910&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034910) confirm the source node and lineage. The ten ancestor IDs are root 1, cellular organisms 131567, Bacteria 2, Thermotogati 3384194, Deinococcota 1297, Deinococci 188787, Deinococcales 118964, Deinococcaceae 183710, Deinococcus 1298, and unclassified Deinococcus 2623546. Every label and rank matches the YAML. The root is explicitly present in the pinned backbone and Datasets response.

No alternative name appears in the inspected backbone or live taxonomy response. Complete exact-ID reads of the local type-material, merged-ID, and dropped-ID inventories found no target row, and the pinned backbone contains no descendants directly below this node. The report preserves NCBI's placement rather than inferring a different taxonomy from a partial marker or from genus-level literature. EXACT is a supported identity match, not evidence of physiological properties.

## Evidence

The one NCBITAXON NAME attestation is supported by the 2026-09-13 snapshot. `curation/seed_scope.tsv:322040` supplies the exact one-source attested rule. `data/taxa/PATHS.tsv:14208` uniquely maps the ID to this stem. The seed event at `2026-09-13T17:54:04Z` matches the source attestation and scope reason. Its count is not a genome count or a count of biological strains.

The exact query `txid1034910[Organism:noexp]` returned one Nuccore hit, UID 333496489. Full metadata, reference, comment, source qualifiers, and rRNA feature annotations were inspected for [JF778658.1](https://www.ncbi.nlm.nih.gov/nuccore/JF778658.1). It is an 892-bp partial 16S rRNA sequence, with source organism `Deinococcus sp. LT7CD`, strain `LT7CD`, isolation source `freshwater lake`, and `taxon:1034910`. Its rRNA feature is partial at both ends. The source was created and updated on 25-May-2011 and cites a direct submission dated 23-Mar-2011 by Huang, Swain, Thacker, Ravindra, Andersen, and Bej. Bellerophon chimera screening is a submitter-reported comment, not an independently repeated analysis.

The complete metadata does not provide a culture-collection deposit, BioSample, BioProject, genome assembly, DOI, PMID, geographical qualifier, or collection date. The PCR primer annotation and partial rRNA feature do not identify a complete genome. Its shortened taxonomy string ends at Deinococcus, while the dedicated taxonomy response explicitly includes the unclassified intermediate node; this is not a contradiction in the target's lineage.

[Huang et al. 2013](https://link.springer.com/article/10.1186/2046-9063-9-4), DOI `10.1186/2046-9063-9-4`, lists JF778652-JF778667, including this accession. Its main text was inspected earlier in this turn; it provides study context, not isolate-specific physiology or a formal name. The source author set also matches the GenBank submission. Supplementary tables and figure images were not independently inspected, and sequence bases were not reclassified.

## Completeness

No required gap was identified. The seven complete exact-taxon inventory reads found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin, or BactoTraits row for this taxon. With no child taxa in the backbone, the BacDive-derived `strain_count: 0` agrees with the represented inventory scope. It does not mean the LT7CD isolate or its marker sequence does not exist.

Ignored-inclusive, hidden-inclusive searches with compressed-content inspection covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding `SOURCE.json` provenance descriptors. The ID/full-label/slug/designation search returned 19 lines. Three were the target backbone, scope, and native scientific name; the remaining 16 were unrelated numeric matches, rejected after complete native-row reads. A further search for JF778658 and spacing/hyphen variants of LT7CD returned only those three target identity rows. No additional target-linked culture, strain overlay, genome, or marker assertion was established within these roots, including ignored files.

The exact-taxon Assembly search returned zero and a phrase-not-found warning. This only describes that index query; it is not proof that no genome could exist under a reclassified name. There is no verified culture-deposit assertion enabling a strain-to-genome join under the repository's rules. Bare strain names and numeric substrings are not join keys.

Ignored-inclusive report/history searches by identifier, label, and slug, plus a filesystem report-stem search, found no earlier target report before this report was created. Optional record-level citations and graphs are not mandatory for this seeded record. No literature result requires inventing a type strain, species name, growth optimum, radiation-tolerance claim, or causal mechanism.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The full record is consistent with the pinned source and live NCBI identity, rank, lineage, code, source count, and seed provenance. There is no unsupported taxonomy mapping, type-strain designation, deposit, assembly, phenotype, or causal edge to correct.

## Recommended Edits

None required. Preserve the generated source-grounded identity and current lifecycle. Do not convert the marker accession to a genome assembly, LT7CD to a registered deposit, or general Deinococcus properties to isolate-level assertions.

Future primary-source corrections belong in the maintained inputs and extraction workflow behind `scripts/extract_source_inventory.py`; harmonization changes belong in `src/taxonmech/seed.py` with tests. `curation/seed_scope.tsv` owns actual scope decisions. A future literature annotation requires a supported maintained input consumed by the seeder. Regenerate using `scripts/seed_from_sources.py`, never by editing the generated record directly. No such change was made here.

## Follow-up Checks

No unresolved blocker remains. If a culture or assembly link is proposed later, require an explicit source-supported relationship meeting the repository's whole-deposit and provenance rules. If a phenotype is proposed, obtain isolate-specific experimental support instead of extrapolating from the taxon name or an environmental setting.

For any authorized curation change, rerun the single-record schema and strict commands, relevant extractor/seeder regression tests, and the documented seed dry-run/canary workflow. Accept regenerated outputs only after the applicable `just verify-corpus`, `just qc`, history/provenance, and render gates. This report is not a human REVIEWED promotion.

## Additional Notes

Rejected full-row collisions include Mycobacterium tuberculosis ERR1034910 in BV-BRC and ATB; Campylobacter jejuni PNUSAC013690, assembly GCA_010349105.1; Caldilineaceae bacterium CHLO-8, BioSample SAMN31034910 and assembly GCA_048499055.1; Staphylococcus aureus sample SAMEA1034910, assembly GCA_027160445.1 and ATB analysis ERZ3070306; and Shigella sonnei ATB samples SAMEA110349100-SAMEA110349109. The scientific identities and explicit identifiers distinguish them from LT7CD. No source annotation or quality flag was transferred from those rows.

This review followed the completed LT15CD review but independently resolved and checked LT7CD, its source rows, taxonomy, sequence, and candidate matches. The current worktree remains on `codex/record-review-extensimonas-20261003` at `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No parallel session is active according to the user; no additional worktree was created.

Only this new report was written for this target. The validation TSV is under `/private/tmp`. Target YAML, Eukaryota, source inventories, scope, history, prior reports, and generated pages were unchanged. No regeneration, commit, lifecycle promotion, history event, external contact, or GitHub mutation occurred.
