# YAML Record Review: Rhizobium nepotum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhizobium_nepotum.yaml`
- Started UTC: 2026-10-06T19:19:28Z
- Finished UTC: 2026-10-06T19:28:08Z
- Verdict: pass with minor issues

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035271`, Rhizobium nepotum, species-rank Bacteria under Rhizobium (`NCBITaxon:379`). It contains ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, one LPSN nomenclature entry, two GTDB mappings, nine source-specific synonyms and one BacDive strain. That strain has three culture deposits, one GOLD-supported NCBI assembly, one GOLD-supported IMG identifier and 17 related-record assertions. Seven source attestations and one seed event are present. No phenotype or causal graph is asserted.

Generated YAML is read-only. Maintained acquisition/extraction, source transforms, `src/taxonmech/seed.py` and scope own future changes. This review did not reopen the separate descendant records.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/rhizobium_nepotum.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/rhizobium_nepotum.yaml --out /private/tmp/rn-strict.tsv`: exit 0, one record, zero errors. The actual output TSV was read and contains only its header.
- Bounded manual comparisons checked identity, full lineage, synonyms, inventories, nomenclature, mappings, every stored strain-link assertion, scope and history. These are not a target-level corpus-reproduction validator.
- SHA-256 checks independently matched the native GOLD organism catalog and transformed GOLD count table to `data/raw/MANIFEST.yaml`. This is not a full provenance gate.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, corpus-wide provenance and history gates. The reproduction script has no target selector; `--max-diffs` limits diagnostics only.
- Not applicable: `just validate-products` for added graph nodes; none are stored. Authority references were checked through pinned source rows and the live sources described below.
- The iModulonDB dataset adapter ran before web follow-up; all 28 rows were read. No matching Rhizobium/Agrobacterium dataset was present, so no target component query was applicable. This is not negative biological evidence.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221980`, path lock `data/taxa/PATHS.tsv:14471` and scope `curation/seed_scope.tsv:10800` agree with the record. Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035271&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035271) confirm its active identity, parent and genetic code. The full pinned lineage matches: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Rhizobiaceae, Rhizobium/Agrobacterium group and Rhizobium.

NCBI's Agrobacterium nepotum synonym, two authority labels and five includes names are preserved with the stored exact/related distinctions. The three children are 1368418 (39/7), 1368419 (AGR18) and 1368420 (AGR19). Historical IDs 1035272 through 1035275 merge into this species; it is not itself dropped. Seven pinned type-material assertions support 39/7, CFBP 7436 and LMG 26435 with source-specific spellings.

[LPSN Rhizobium nepotum](https://lpsn.dsmz.de/species/rhizobium-nepotum), record 790042, confirms a validly published synonym. [LPSN Agrobacterium nepotum](https://lpsn.dsmz.de/species/agrobacterium-nepotum), record 794717, is its homotypic correct name. The old-name status and related LPSN synonym are accurately retained. The nomenclature authority and flags match `data/raw/lpsn_names.tsv:27033`. NCBI's Rhizobium placement and LPSN's Agrobacterium treatment differ; the record preserves the distinction without changing NCBI lineage.

Both stored LPSN type-deposit IDs are supported. Live LPSN additionally lists CFBP 7436 and HAMBI 3456; the latter is not a current local BacDive deposit and cannot be used as an existing join key. The correct-name LPSN row at line 31189 lacks a direct NCBITaxon mapping, explaining why it supplies a synonym but not another nomenclature entry.

## Evidence

[BacDive 130598](https://bacdive.dsmz.de/strain/130598), its complete native projection at `data/bacdive/records.jsonl.gz:52910`, and [DSM 29844](https://www.dsmz.de/collection/catalogue/details/culture/DSM-29844) support type strain 39/7 and deposits CFBP 7436, DSM 29844 and LMG 26435. The raw BacDive row at line 52911 matches the one listed strain. No additional BacDive strains were found under the three descendants in the bounded source checks. The type flag is supported for this species, not inherited from a broader taxon.

[PMID:22463808](https://pubmed.ncbi.nlm.nih.gov/22463808/), retrieved through NCBI EFetch, resolves the stored DOI `10.1016/j.syapm.2012.03.001` and species description. Its abstract identifies 39/7 as the type, equating LMG 26435 and CFBP 7436, and distinguishes the five isolates' pathogenicity. Only strain 0 caused crown gall in that study. The 2012 full article was not inspected; no additional assay claims are inferred.

The [publisher's validation-list record](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.046342-0) verifies the second stored DOI and September 2012 publication metadata. LPSN identifies it as Validation List 147. The publisher's dynamic full-text table was unavailable, so this review does not claim to have inspected that table.

Full [FR870231.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR870231.1) identify the 1,371-nt partial 16S sequence of type strain 39/7, taxon 1035271, Hungary, and the same PMID/DOI. The stored unversioned `INSDC:FR870231` is preserved; it is not a genome assembly.

The stored GOLD chain is explicit in full native rows: `Go0044949` names CFBP 7436 and child taxon 1368418; `Gp0144454` points to that organism, PRJNA270495 and SAMN03266536; `Ga0124447` points to that project and supplies GCA_000949865.1 plus IMG 2711768133. The separate `Gp0044949` supplies PRJNA213097, not another assembly. `Go0618729` and `Go0618730` explicitly name LMG 26435 and DSM 29844. Repeated organism assertions retain two different source fields rather than being accidental duplicates.

The live [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000949865.1/dataset_report) confirms current GCA_000949865.1, explicit paired GCF_000949865.1, 39/7, taxon 1368418, 79 contigs, 5,328,872 bases, SAMN03266536 and PRJNA270495. Both stored [BioProjects were read through EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=213097,270495&retmode=xml). PRJNA213097 explicitly names both culture deposits. PRJNA270495 also contains another sample; shared project membership does not transfer that sample or its genome to 39/7.

The complete [2015 genome announcement](https://europepmc.org/articles/PMC4408340), DOI `10.1128/genomeA.00331-15`, was inspected through Europe PMC's full-text XML. It links 39/7 and its two deposits to JWJH00000000, describes this strain as nonpathogenic, and distinguishes the other sequenced strain, KFB 330. Its genome size and contig count agree with the stored assembly's NCBI metadata. BacDive's general plant-pathogen wording must not override the strain-specific experimental distinction; no pathogenicity claim is stored here.

Full pinned and [live StrainInfo 377577](https://api.straininfo.dsmz.de/v2/data/strain/max/377577) agree on DOI `10.60712/SI-ID377577.3`, published status, BacDive 130598 and the three available deposits: SI-DP865963/LMG 26435, SI-DP873138/CFBP 7436 and SI-DP910177/DSM 29844. Each stored nested evidence object matches its own deposit. Neither record supplies a deposit-specific sequence assertion. The live record's literature link is not such an assertion, so no genome is transferred through StrainInfo.

GTDB mappings reproduce raw lines 1425 and 1426: A. nepotum, four genomes, and A. tumefaciens, 296, both broadMatch. Native GTDB rows show four A. nepotum genomes, including representative RS_GCF_000949865.1, and place NCBI-labeled R. nepotum CC213 in A. tumefaciens. NCBI flags CC213's organism as unverified. These are source classification conflicts, not equivalence claims. The 296 value is the entire source pool's inventory count, not 296 genomes of this type strain. No broad mapping has leaked into exact synonyms or xrefs.

## Completeness

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The first search covered identifier, label, slug, child 39/7 taxid, exact culture numbers and stored sequence/project/genome identifiers and returned 148 rows. A follow-up for BacDive/SI identifiers, HAMBI 3456 and JWJH returned 45 rows, adding 17 unrelated WGS substring matches. All 165 distinct candidate rows were read in full native or TSV form. Five SOURCE.json files and history filenames were inspected separately. No target-specific external history entry or local HAMBI 3456 match was found within these bounds.

The 17 stored related assertions match 11 GOLD and six StrainInfo inventory rows. Exact culture normalization accepts CFBP 7436, DSM 29844 and LMG 26435; it rejects bare 39/7, 7, 39, CC213, DAN6, 0d and GR12. GTDB's type-genome row carries `7;39`, NCBI carries bare `39/7`, and BV-BRC 1368418.3 carries the same bare designation. They therefore do not satisfy current culture-deposit matching. The explicit NCBI assembly pair is a useful future crosslink candidate, not permission to invent a culture match or replace prefixes heuristically.

No ATB candidate had the retained BioSample SAMN03266536; the twelve ATB hits were unrelated numeric/hash collisions, including an ineligible removed-run record. Empty ATB links are appropriate for this snapshot. Ten other native StrainInfo groups denote other deposits and are not automatically BacDive strains. SeqCode records 1800 and 29772 are name-catalog entries, not genome or strain links.

MediaDive's one direct medium and BactoTraits' one trait assertion match their complete raw rows. No Madin row was found. GOLD's transformed count is 15, but the native catalog contains 14 direct organism records; see the minor finding. Counts across sources, deposits and descendant taxa must not be summed.

The scope's six-source explanation is dated 2026-09-12; the seeded record correctly lists seven currently attesting sources. The seed event timestamp 2026-09-13T17:54:04Z matches the newest of the three source manifests, as `_seed_timestamp` requires. Lifecycle remains SEEDED.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**Minor: unresolved GOLD count provenance.** The GOLD attestation presents 15 directly classified organism records. This faithfully reproduces `data/raw/gold_organisms.tsv:482`, but a complete exact-taxid scan of the hash-verified native organism catalog yields 14 rows and 14 distinct IDs: Go0229666 through Go0229677, Go0618729 and Go0618730. The three descendant organism rows are separate and do not resolve the difference.

`src/taxonmech/extract.py:403` counts KGX subclass edges and line 676 supplies that result; the native workbook instead supplies the strain links. `docs/HARMONIZATION.md` documents the two paths, but the attestation does not identify its KGX count basis or expose the discrepancy. The configured upstream `data/transformed/gold/edges.tsv` was unavailable at its configured path, so the extra counted assertion could not be identified. This is a bounded provenance/interpretation gap, not proof that 15 should simply be replaced with 14, nor a defect in the verified genome chain.

Maintained owners: the upstream GOLD transform and `src/taxonmech/extract.py` for counted inputs, `src/taxonmech/seed.py:611` for attestation wording. Do not patch generated YAML or infer the missing row's identity.

## Recommended Edits

Clarify the GOLD attestation's count basis and source snapshot through maintained generation inputs. When the exact hashed KGX input is available, compare its 15 counted edges with the 14 primary direct organism IDs. Preserve any genuine snapshot or classification difference explicitly; correct duplicates or stale classifications upstream only after identifying them.

Optional future enrichment can refresh LPSN's additional type-deposit designations and add evidence-preserving exact assembly-pair crosslinks. It must retain explicit source provenance and cannot relax the whole-deposit matcher. No required identity, lineage, type-strain, stored-genome or deposit correction was found.

## Follow-up Checks

Recover the GOLD edge input whose SHA-256 is `b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12`, enumerate exact taxon 1035271 subclass edges and their distinct organism IDs, and compare classifications against the primary workbook pin. Test direct-only counting and explicit source-basis wording; do not gather descendants silently.

For any authorized enrichment, test exact GCA/GCF versions and source chains, nonmatching bare designations, StrainInfo deposit scoping and ATB sample identity. After maintained input changes, regenerate through the validated writer and rerun target schema/strict checks, full `just verify-corpus` and `just qc`. No regeneration or lifecycle promotion occurred in this review.

## Additional Notes

GTDB taxon pages, GOLD organism/analysis pages and the IMG detail page could not be read live with the web tool. Their stored assertions were assessed from inspected pinned native metadata; IMG's current service availability remains unverified. NCBI/PMC browser challenges were handled through independent public NCBI and Europe PMC APIs, not by claiming challenged pages were read. The LMG catalog page was unavailable; its deposit is independently supported by LPSN, BacDive, DSMZ and StrainInfo.

The native GOLD source and transformed count table both match their committed manifest hashes. This rules out local drift in those two files only. GTDB's 296 pool count and the MediaDive/BactoTraits counts were checked against committed transformed inventories, not rebuilt from unavailable upstream KGX inputs.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Ignored-inclusive report-filename searches found no previous report for this stem. The complete YAML was reread byte-unchanged. Only this new report was written for this target; records, history, lifecycle, site, Git and GitHub state were not changed. Eukaryota remained untouched.

