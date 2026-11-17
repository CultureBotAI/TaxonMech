# YAML Record Review: Wolbachia endosymbiont of Circoniscus bezzii

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_circoniscus_bezzii.yaml`
- Started UTC: 2026-10-08T00:17:33Z
- Finished UTC: 2026-10-08T00:25:38Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036170`, label `Wolbachia endosymbiont of Circoniscus bezzii`, rank `SPECIES`, domain `BACTERIA`. This is a bacterial host-associated taxon, not the animal host or a particular cultured isolate. The record has `EXACT` grounding, `SEEDED` mapping status, genetic code 11, zero inventory strains, one NCBITAXON name attestation, and one seed event. Optional synonyms, nomenclature, mappings, strain entries, evidence, discussion and causal graph are absent.

Resolution searched `data/taxa`, `curation`, `history` and `reports` with `rg --no-ignore --hidden`, using the digit-bounded identifier, label component and slug. It resolved one YAML and its index/scope entries, with no prior report for this target. This review does not change the record or its review status.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_circoniscus_bezzii.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_circoniscus_bezzii.yaml --out /private/tmp/wcb-strict.tsv`: exit 0; one file, zero error rows. Read the complete header-only TSV.
- Structured comparisons against the pinned backbone verified identity, rank, parent, code, every lineage entry, name attestation, snapshot and scope-derived event text. No direct children occur in the pinned backbone. Exact-ID checks of all seven additional raw taxon inventories returned no target rows; type-material, merged-ID and dropped inventories also returned no target rows.
- Inspected live NCBI Taxonomy EFetch and Datasets responses, exact-taxonomy Assembly/Nuccore searches, and complete metadata for all six matching nucleotide entries, excluding nucleotide strings and protein translations.
- Not run: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, provenance, rendering, documentation, test and vendored gates. These focused checks are not a claim of full-corpus reproducibility or publication readiness.
- No independent history record was found in the bounded ignored-inclusive history searches, so there was no target history file to validate. Inline history passed the record validators. No curator-added graph grounding invokes `just validate-products`; no separate focused term/reference validator is exposed for this identity-only record.

## Identity and Grounding

The pinned `data/raw/ncbitaxon_taxa.tsv:222296` matches the YAML's label, species rank, parent `NCBITaxon:2640676`, code 11, empty synonym sets and 2026-09-13 snapshot. The complete root-first chain of 11 ancestors matches, including `NCBITaxon:952` Wolbachieae at tribe rank. Lineage is carried from NCBI, not flattened or reconciled with another taxonomy.

[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036170) and the inspected [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036170) independently retain this ID and label at species rank. EFetch supplies the same parent, bacterial division, genetic code and ancestor identities/ranks; Datasets also includes root in its lineage. No identity conflict was found.

`data/taxa/PATHS.tsv:14801` supplies the exact slug. `curation/seed_scope.tsv:322550` provides the one-source admission reason used verbatim by the seed event. The sole NCBITAXON attestation counts one name, not six sequences, two biological variants or a culture deposit. Native catalog row `data/catalog/ncbi_names-0005.jsonl.gz:31814` independently preserves the scientific name.

## Evidence

The YAML makes identity and inventory assertions, not experimental phenotype claims. Its supporting pinned NCBI row agrees with the live authority. The following external evidence was checked for identity and possible material omissions; it is not silently promoted into new YAML claims.

- [JF799950.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799950.1) is an 857-nt partial 16S sequence, isolate `wCir1`, clone C. [JF799951.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799951.1) is an 866-nt partial 16S sequence, isolate `wCir2`, clone D. Both explicitly reference taxon 1036170 and host Circoniscus bezzii, list Porto Alegre and 17-Mar-2011, and link PMID 24031883 and DOI 10.1590/S1517-83822012000200036. They were submitted 12-Apr-2011, created 05-Jun-2011 and last updated 28-May-2015.
- [KJ814209.1](https://www.ncbi.nlm.nih.gov/nuccore/KJ814209.1) and [KJ814225.1](https://www.ncbi.nlm.nih.gov/nuccore/KJ814225.1) are clone L: 813-nt partial 16S and 383-nt partial dnaA, respectively. [KJ814210.1](https://www.ncbi.nlm.nih.gov/nuccore/KJ814210.1) and [KJ814226.1](https://www.ncbi.nlm.nih.gov/nuccore/KJ814226.1) are the corresponding clone M markers, with the same respective lengths. Their host fields embed vouchers UFRGS 50011 and UFRGS 50012; these are not bacterial culture deposits. Both pairs list Presidente Olegario, 18.41 S 46.41 W, 03-Sep-2010, and link PMID 25764472 and DOI 10.1093/femsec/fiv025. The dnaA feature tables name proteins AIG17933.1 and AIG17934.1 and translation table 11. The entries were submitted 12-May-2014, created 23-Jul-2014 and updated 29-Apr-2015. Their forest-soil source field does not demonstrate free-living bacterial growth.
- The [2012 primary article](https://new.scielo.br/j/bjm/a/3tMnDg5R75sMMvwLQ8TQSpS/?ilang=pt_BR&lang=en), inspected in full main text, reports three positive female C. bezzii and two distinct 16S sequences from different individuals, named wBez1 and wBez2. Its methods place C. bezzii collection in Presidente Olegario, not Porto Alegre. It explicitly lists JF799948-JF799951. Thus both variant naming and locality differ from the target JF entries. Preserve these discrepancies; do not silently equate labels, correct source coordinates, or infer coinfection in one individual. They concern prospective enrichment, not any current YAML assertion.
- The [2015 primary article](https://academic.oup.com/femsec/article/91/4/fiv025/598436), read through its public publisher CDN, has target rows in Tables 1 and 2 and relevant methods/results/discussion. Table 1 reports three positive females among seven tested and no males tested at Presidente Olegario. This is a sampled cohort, not taxon-wide prevalence. Table 2 assigns ST416 to C. bezzii 1 and an incomplete profile to C. bezzii 2. The authors infer recombination involving gatB and fbpA in variant 1 and describe inconsistent marker-tree placement. This is computational evidence, not an observed transfer experiment or grounds to collapse both variants into one supergroup. Their screen did not detect mixed infections within individual hosts. Live PubMLST records, supplementary files and figure images were not independently audited; no extra claims are made from them.

PubMed citation metadata and complete abstracts for both linked PMIDs were inspected and agree with the publication titles and DOIs. The original OUP URL failed in the web fetcher; its public redirect at `https://oup.silverchair-cdn.com/article-minimal/598436` was readable with a normal HTTP request. No access restriction was bypassed.

## Completeness

`strain_count: 0` is consistent with the BacDive classified-subtree inventory rule in `src/taxonmech/seed.py`: no direct matching strain rows and no descendant taxa exist in the pinned inputs. Sequence variants described as strains in papers are not automatically BacDive inventory entries. Empty strain and genome lists therefore do not imply that Wolbachia was absent from the hosts or that no marker sequences exist.

An ignored-inclusive, compressed-file-aware search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It searched the bounded taxon ID, name, slug, all six nucleotide accessions, both protein identifiers, wCir1/wCir2, wBez1/wBez2 and both UFRGS vouchers. All nine candidate rows were read completely: three JSON objects and six TSV rows. Three are this taxon's name/backbone/scope evidence; six concern unrelated actinobacteria WCIR2 (`NCBITaxon:223968`) and WCIR1 (`NCBITaxon:223969`). Case-insensitive short-name coincidence does not establish identity.

All five `SOURCE.json` metadata objects were separately parsed; no additional target match occurred. History filenames were searched independently of ignore rules and had no matches. These are bounded local absence findings, not an assertion that every external database lacks evidence.

Exact NCBI Assembly search returned zero, including its no-items/phrase-not-found warning; exact Nuccore search returned the six marker entries above. Their inspected metadata contain no BioSample, BioProject, assembly or eligible bacterial culture-deposit link. No missing source-supported strain-genome chain was established. A zero exact Assembly result is not proof that no relevant genome could exist under another taxonomic assignment.

Optional nomenclature, mappings, causal graph and literature evidence need not be invented for an identity-only seeded record. iModulonDB is not applicable: the YAML asserts no gene, regulator, pathway, stress response or expression-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed YAML. The external variant-name/locality discrepancies and marker-dependent phylogenetic uncertainty remain explicit limits for future enrichment, not unsupported claims in this record.

## Recommended Edits

None required. Do not edit generated YAML or promote `SEEDED` to a reviewed status from this report.

Future identity corrections belong in the authoritative NCBI source and the extractor `scripts/extract_source_inventory.py`; projection/count corrections belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Any new literature/variant representation would require an explicitly designed maintained input and generator support, preserving the source discrepancies. Do not treat this report as an existing curator overlay or use host vouchers, partial genes or bare variant labels as genome-join keys.

## Follow-up Checks

For an authorized source refresh or curation change, resolve the source naming/locality discrepancy before adding strain-level claims; inspect relevant accession histories and PubMLST evidence if those claims are proposed. Then use the documented dry-run/canary workflow, focused schema/strict validators, full `just verify-corpus` and `just qc`. No regeneration or history mutation was performed here.

## Additional Notes

Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`. The YAML remained byte-identical before report creation. The report is the sole new repository artifact for this review; existing reports, branches and worktrees are preserved. Eukaryota is already fully covered and was not reviewed or changed.

The seed timestamp `2026-09-13T17:54:04Z` is reproducible provenance, not a review time. It matches the maximum extracted-at timestamp across the raw, ATB and StrainInfo manifests, as implemented by `_seed_timestamp` in `src/taxonmech/seed.py`.
