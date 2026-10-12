# YAML Record Review: uncultured marine bacterium D019

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d019.yaml`
- Started UTC: 2026-10-09T12:28:40Z
- Finished UTC: 2026-10-09T12:32:20Z
- Verdict: pass

## Target

Reviewed the entire 39-line generated TaxonRecord for `NCBITaxon:103671`, `uncultured marine bacterium D019`, including a final numbered reread. It is an environmental clone concept assigned SPECIES rank by NCBI, not a cultured isolate or formally named species. Domain BACTERIA, EXACT grounding, SEEDED mapping, code 11, zero represented strains, one NCBI NAME attestation and one embedded seed event are asserted. No synonyms, nomenclature, taxonomy mappings, xrefs, literature or causal graphs are asserted. This review resolves the own ID and clone, independently of adjacent D-series records.

## Validation

Both commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d019.yaml`: exit 0; no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d019.yaml --out /private/tmp/taxonmech-d019-review-strict.tsv`: exit 0; one file scanned, zero errors; the full TSV is header-only.

Read-only structured comparisons passed for the own backbone, full local ancestor chain, attestation, PATHS, scope and seed-event text. Exact-field status scans completed.

Not checked: `just verify-corpus`, corpus tests/full QC, generated-product label validation and global history validation. These bounded comparisons do not certify corpus reproduction. No generated product was edited. There is no literature or curator-added graph reference in the YAML requiring another focused validator; the externally discovered PMID, DOI and sequence were checked as evidence below. The embedded event was inspected; no separate target history artifact was found in the bounded ignored-independent search.

## Identity and Grounding

Own backbone `data/raw/ncbitaxon_taxa.tsv:18536` and native scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38552` agree with the exact clone label and ID. The backbone has SPECIES, parent `NCBITaxon:150608`, code 11, NCBI-only attestation and snapshot 2026-09-13, with empty synonym and retirement values.

Complete [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103671&retmode=xml) confirms the identity, species rank, parent and code. Its source division is Environmental samples; the BACTERIA domain is supported by the actual ancestor chain, not an assumed equality between division and domain. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103671) confirms the root-first IDs 1, 131567, 2, 48479, 150608. All five stored labels/ranks agree: root, cellular organisms, Bacteria, environmental samples and marine bacteria D ensemble. This deliberately unresolved lineage is carried from NCBI and must not be replaced by an inferred cultured-genus assignment.

Complete candidate-row inspection excluded distinct identifiers that share the number 103671: BacDive 103671 is Rhodococcus sp. ST018045 (taxon 194249); CIP 103671 is Pseudoalteromonas atlantica 512-W (taxon 288); DSM 103671 is Parendozoicomonas haliclonae S-B4-1U (taxon 1960125); StrainInfo deposit 103671 is ATCC 25129, Mycobacterium intracellulare (taxon 1767). Their nomenclature, type status, deposits and genome links do not belong to D019.

## Evidence

The own NCBI source attestation correctly counts one NAME at the pinned snapshot. `data/taxa/PATHS.tsv:15124` and `curation/seed_scope.tsv:144180` agree with the identifier and scope reason. The 2026-09-13T17:54:04Z SEEDED_FROM_SOURCES event matches the NCBI-only support and own scope text. It is not a human-review event.

The exact non-expanded nuccore query returned UID 5882273. Complete [GenBank XML for AF177558.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=5882273&rettype=gb&retmode=xml) identifies a 559-base partial 16S sequence, explicitly linked to taxon 103671, clone D019 and an environmental sample. It describes an uncultured surface-associated marine bacterium, not a strain deposit. Both rRNA ends are partial. The record cites Dang and Lovell's article, PMID 10653705, and their 13 August 1999 direct submission. All 559 DNA bases are A/C/G/T and match the submitted rRNA transcription after case normalization. These checks do not independently align or classify the sequence.

The full [PubMed abstract and bibliographic record](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10653705&retmode=xml) verifies the cited 2000 Applied and Environmental Microbiology article and DOI 10.1128/AEM.66.2.467-475.2000. The [publisher's methods, Table 1, results and discussion](https://journals.asm.org/doi/10.1128/AEM.66.2.467-475.2000) were inspected. Surfaces were exposed in a South Carolina salt-marsh creek and sampled after 24 or 72 hours. D019's Table 1 frequencies are PEG-S/72 h 4.8%, PEG-L/72 h 1.5%, PEG-M/24 h 1.9%, PEG-M/72 h 1.8% and PU/72 h 3.7%. These describe ARDRA-pattern representation in clone libraries, not measured organism abundance. The authors discuss PCR bias and rRNA-copy variation. No clone-specific figure placement or inferred lineage correction is claimed here.

A separate primary [2005 FEMS study, DOI 10.1016/j.femsec.2005.04.005](https://academic.oup.com/femsec/article/54/2/257/465913), was inspected at its methods, Table 2 and relevant results. Its culture-associated DGGE band BH13 has AF177558/D019 as the closest database match, at 97.9% over 514 bases. That is a comparison to D019, not identification of BH13 as the same clone or specimen. Community substrate-use measurements and bloom associations therefore cannot be assigned to D019. No traits or causal edge were transferred from that later study.

## Completeness

No consequential omission was established for this sparse taxonomic seed. Optional literature and source-context enrichment is possible, but the record makes no unsupported ecological or mechanistic claim. `strain_count: 0` is appropriate for the represented upstream strain entries and is not contradicted by an environmental clone.

Exact own-ID checks found no children or rows in the seven non-NCBI inventory tables or three status tables below. Ignored-inclusive content searches returned 30 complete candidate rows, all read and disambiguated: three own rows and 27 unrelated culture, source-ID or genome-statistic matches. Adding AF177558 returned exactly the same candidate addresses. Full structured parsing of all five SOURCE.json files found only a BacDive-native request for ID 103671, consistent with the unrelated Rhodococcus record. History filename inspection found no target match. These are bounded search conclusions.

The exact assembly query returned zero with a phrase-not-found warning, establishing no observed exact indexed association rather than universal absence. Name-based web leads were broad conference-document hits and were not adopted as biology. The accession search found the inspected later primary study. iModulonDB was not applicable because the record contains no gene, regulator, expression-module or transcriptomic assertion.

## Findings

None found.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

None required. Retain the clone label, own NCBI ID, carried environmental lineage and SEEDED status. Do not add cultured-strain links or infer BH13 equivalence.

Any future supported identity/lineage correction belongs in `data/raw/ncbitaxon_taxa.tsv` and its maintained import process, not the generated YAML. Scope is owned by `curation/seed_scope.tsv`; construction is owned by `src/taxonmech/seed.py` (identity/lineage, code, strain count, attestation and history), invoked through `scripts/seed_from_sources.py`. Literature context would require an authorized maintained representation with claim-specific evidence, not a hand patch to the seed.

## Follow-up Checks

No blocking follow-up. New culture/genome mappings require an explicit source identity chain for D019. Any proposed phylogenetic enrichment must distinguish published sequence inference from the carried NCBI lineage; this review did not rerun the published phylogeny. Future authorized maintained-source corrections should rerun the two focused validators and documented reproduction, product and applicable history gates.

## Additional Notes

- Ignored-inclusive filename inventory covered `data/taxa reports/yaml_record_review history`, using `103671|(^|[/_-])d019([_.-]|$)`; only the selected YAML matched. No neighboring YAML was reviewed for this verdict.
- Initial content expression: `\b103671\b|\bD019\b|uncultured_marine_bacterium_d019\b`; expansion added `\bAF177558(?:\.1)?\b`.
- Content search used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` over `data/raw data/catalog data/bacdive data/bvbrc data/gold data/seqcode data/straininfo data/atb curation history`. SOURCE.json files were separately discovered with ignored-inclusive search and fully parsed.
- Own content matches: backbone line 18536, scope line 144180 and native name `ncbi_names-0000.jsonl.gz:38552`.
- BacDive exclusions: complete native `data/bacdive/records.jsonl.gz` lines 27792, 57638, 90955 and corresponding `data/raw/bacdive_strains.tsv` lines 27793, 57639, 90956. These are BacDive 103671, 135333 and 168723 respectively.
- CIP 103671 exclusions: complete `data/gold/organisms.jsonl.gz:204951` identifies Go0266903, taxon 288; `data/raw/strain_related_records.tsv:101113` and `:101114` preserve that organism relationship, not a genome. StrainInfo strain 65563/deposit 154029 and its IAM/JCM deposits also belong to taxon 288.
- DSM 103671 exclusions: `data/raw/lpsn_names.tsv:32747` is LPSN 797598, Parendozoicomonas haliclonae; `data/raw/ncbi_type_material.tsv:74857` and `:74858` are that species' type material, not D019. Its StrainInfo strain/deposit are 403457/910532. KX611231 and GCA_900174585 in its BacDive metadata were not transferred.
- Remaining deposit evidence read fully: `data/raw/culture_collection_strains.tsv` lines 43994, 59719; `data/straininfo/strain_links.tsv` lines 18223, 70568; `data/straininfo/related_records.tsv.gz` lines 44759, 44762, 167033, 167034; `data/straininfo/records.jsonl.gz` lines 34608, 52889, 301346. Line 34608 is the unrelated ATCC 25129/StrainInfo strain 46634/deposit 103671 record.
- Four complete GTDB metadata exclusions under `data/catalog`: `gtdb_genomes-0016.jsonl.gz:37006`, RS_GCF_002233235.1, taxon 562, contig N50 103671; `gtdb_genomes-0004.jsonl.gz:14046`, RS_GCF_047742845.1, taxon 573, scaffold N75 103671; `gtdb_genomes-0003.jsonl.gz:11037`, RS_GCF_005281055.1, taxon 2576425, scaffold N75 103671; `gtdb_genomes-0015.jsonl.gz:8652`, RS_GCF_019040655.1, taxon 28095, contig N50 103671. These are numeric statistic matches, not taxon mappings.
- BacDive SOURCE.json `responses/278/requested_ids/91` and its request URL contain BacDive ID 103671. The other four metadata files (BV-BRC, GOLD, SeqCode, StrainInfo) have no match to the expressions. No metadata value establishes target identity.
- Exact-ID scans covered `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, `bactotraits_taxa.tsv`, `ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv`.
- Before/after YAML SHA-256: `a4ee845c53697b5b3b516ab6a7124526614a830f487e263d75201a5724b81be4`.
- This review added only this report. It did not modify YAML, inventories, scope, generated products, history, review status, branch or worktree. No Eukaryota YAML was reviewed.
