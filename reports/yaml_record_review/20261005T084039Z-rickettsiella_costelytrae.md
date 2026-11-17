# YAML Record Review: Rickettsiella costelytrae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rickettsiella_costelytrae.yaml`
- Started UTC: 2026-10-05T08:37:27Z
- Finished UTC: 2026-10-05T08:40:39Z
- Verdict: pass

## Target

The entire 64-line `TaxonRecord` was read before judgment. It denotes `NCBITaxon:1034382`, Rickettsiella costelytrae, rank `SPECIES`, domain `BACTERIA`, with `grounding_status: EXACT` and `mapping_status: SEEDED`. It is generated from the inventories and scope, not a manually maintained species description. Future fixes belong to the responsible source capture/transform, `src/taxonmech/extract.py`, `src/taxonmech/seed.py`, or `curation/seed_scope.tsv`, according to ownership; the generated YAML must not be hand-edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/rickettsiella_costelytrae.yaml`: exit 0, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/rickettsiella_costelytrae.yaml --out /private/tmp/rickettsiella-costelytrae-strict-20261005.tsv`: exit 0; one file scanned, zero error rows.
- Read-only structured full-table comparisons checked the identity, complete lineage, synonyms, direct source inventory rows, unique PATHS/scope entries, attestation, and inline seed event. No child taxon was found in the complete pinned backbone. Complete scans of the merged, dropped, and type-material tables found no target row.
- `just verify-corpus`: not run because this is a full-corpus reproduction gate, not a documented single-record validator. Its `--max-diffs` option limits diagnostics, not scope. The bounded comparisons above do not substitute for that gate.
- `validate-products`: not applicable; no curator-added causal graph. `validate-history`: not run; ignored-inclusive filename and content searches of `history/` found no target history artifact. The inline seed event was checked separately. No focused term/reference validator was invented.

## Identity and Grounding

The pinned row at `data/raw/ncbitaxon_taxa.tsv:221581`, live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034382&retmode=xml), and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034382) agree on identity, species rank, parent `NCBITaxon:59195` (Rickettsiella), and bacterial placement. EFetch also confirms genetic code 11. All nine root-first ancestors match the pinned backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Legionellales, Coxiellaceae, Rickettsiella. The live Datasets lineage includes the same ancestor IDs.

The three exact synonyms are actual NCBI synonym-class names, not a transfer from a different organism: the pathotype wording, Rickettsiella sp. 'Costelytra zealandica', and Rickettsiella symbiont of Costelytra zealandica. The quoted Leclerque et al. 2012 authority is correctly kept as `RELATED_SYNONYM`. Full native name objects at `data/catalog/ncbi_names-0005.jsonl.gz:30950` through line 30954 and the live EFetch response agree on all four names and their classes.

NCBI identity is not nomenclatural validity. [LPSN record 31824](https://lpsn.dsmz.de/species/rickettsiella-costelytrae) treats this as a species name that is not validly published and is preferred rather than correct. It identifies JKI ANZ2008-1 as nomenclatural type and JF490030 as its 16S marker. These qualifications do not invalidate the exact NCBI grounding, and the YAML makes no contrary valid-publication claim.

## Evidence

- The sole attestation is supported by the complete NCBI backbone row: source `NCBITAXON`, ID `NCBITaxon:1034382`, the matching label, one `NAME`, and snapshot date 2026-09-13. This counts a source concept, not isolates, sequences, or biological replication.
- All seven other direct inventory scans returned no target row: BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin, and BactoTraits. An additional full scan of `data/raw/lpsn_names.tsv` found neither `lpsn:31824` nor the name. Thus the missing nomenclature is not a seeder omission of an available mapped inventory row. The live LPSN page is an enrichment lead, not an existing source attestation that can simply be copied into the generated file.
- The original study's [publisher abstract](https://academic.oup.com/jambio/article/113/5/1228/6715649) and PubMed EFetch for [PMID 22856625](https://pubmed.ncbi.nlm.nih.gov/22856625/) agree on DOI `10.1111/j.1365-2672.2012.05419.x`, authors, year, journal, and pages. The authors used microscopy and multilocus markers, distinguished the Costelytra-associated and Pyronota-associated organisms, and proposed treating them as pathotypes synonymous with R. popilliae under the classification then accepted. This taxonomic interpretation differs from NCBI's separate species node; it is preserved here rather than used to merge taxa or assert present-day equivalence. Only the abstract and bibliographic metadata were accessible, not the full study.
- The exact-taxid NCBI Assembly query `txid1034382[Organism:noexp]` returned zero items with a phrases-not-found warning. This is only a negative result for that query, not proof that the organism has never been sequenced. The matching Nuccore query returned seven IDs; all seven records' metadata, source qualifiers, references, and features were inspected.
- All seven Nuccore records explicitly identify taxon 1034382 and strain JKI ANZ2008-1. They are [JF490030.1](https://www.ncbi.nlm.nih.gov/nuccore/JF490030.1), 1,357 bp partial 16S; [JF490031.1](https://www.ncbi.nlm.nih.gov/nuccore/JF490031.1), 925 bp partial 23S; [JF708247.1](https://www.ncbi.nlm.nih.gov/nuccore/JF708247.1), 249 bp partial 23S with an intervening sequence; [JF490032.1](https://www.ncbi.nlm.nih.gov/nuccore/JF490032.1), 996 bp complete ftsY CDS; [JN565689.1](https://www.ncbi.nlm.nih.gov/nuccore/JN565689.1), 786 bp partial gidA; [JN565690.1](https://www.ncbi.nlm.nih.gov/nuccore/JN565690.1), 885 bp partial sucB; and [JN695774.1](https://www.ncbi.nlm.nih.gov/nuccore/JN695774.1), 894 bp partial rpsA. None is an assembly; a complete CDS is not a complete genome. The five 16S/protein-marker records cite the inspected study. The two 23S entries instead retain an unpublished reference and direct submission.
- The full native SeqCode object at `data/seqcode/names.jsonl.gz:34914` contains ID 36801, the matching name, and resource/API URLs. It does not itself supply an NCBI mapping or type-genome assertion. It is retained as a catalog lead, not promoted to a record identity or genome association.

## Completeness

The zero strain count matches the BacDive inventory, and the complete backbone has no descendants from which BacDive strains could be gathered. JKI ANZ2008-1 is a source strain designation, not evidence of an inventoried BacDive strain or an eligible culture-deposit join. Seven gene accessions do not justify creating a strain entry, incrementing a genome count, or transferring genomes from R. popilliae.

Gitignore-independent, compressed-aware searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. They covered the taxon CURIE/numeric ID, scientific name, old names, filename stem, JKI ANZ2008-1 variants, and JF490030. The first search returned eight contexts; the expanded search returned twelve. Neither found a target-specific local LPSN row, GTDB mapping/genome, BacDive strain, GOLD/BV-BRC genome, StrainInfo deposit, ATB sample chain, or history artifact. Numeric matches to unrelated genome sizes and BioSample SAMEA1034382 were explicitly rejected; that sample belongs to Streptococcus equi subsp. zooepidemicus and is not this taxonomy ID.

Optional record-level literature, phenotype, and causal-graph slots need not be populated. The missing live LPSN name is a bounded source-enrichment opportunity, not evidence that the current generated record misrepresents an imported row. The report does not claim complete external literature or genome discovery.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed scope. The current record faithfully represents the NCBI concept and committed inventories. The separate NCBI species node, LPSN publication qualification, and primary study's pathotype interpretation are distinct source assertions, not silently reconciled. This pass does not promote `mapping_status` to `REVIEWED`.

## Recommended Edits

None required for the current record. As optional future enrichment, investigate the upstream kg-microbe LPSN/LPSN-API capture and mapping for record 31824. The local importer is `src/taxonmech/extract.py:420` (`extract_lpsn`), feeding derived `data/raw/lpsn_names.tsv`; `src/taxonmech/seed.py:386` emits mapped nomenclature. Establish an explicit source mapping before attachment, preserve non-valid/preferred status without marking the name correct, and keep JF490030 as a marker. The current local evidence cannot determine why that LPSN name is absent upstream.

Do not merge this NCBI record into R. popilliae, relabel its rank, invent culture deposits, or add genome equivalence from the study's interpretation. Any future taxonomy correction belongs at the taxonomy authority and in a separately authorized source refresh.

## Follow-up Checks

For a separately authorized LPSN refresh, inspect its native name/status and mapping, compare the resulting inventory row, verify status parsing, and rerun both focused validators above. Use `just verify-corpus` after authorized regeneration to establish full reproduction. Recheck exact-taxid assembly results and explicit deposit/sample provenance before adding any genome association. No additional action is required to accept this bounded review.

## Additional Notes

- `data/taxa/PATHS.tsv:14045` uniquely maps the ID to the target stem. `curation/seed_scope.tsv:321893` supplies the 2026-09-13 one-source scope reason. The inline 2026-09-13T17:54:04Z seed event correctly cites NCBITAXON and that reason.
- An ignored-inclusive pre-write filename search found no target report or target history path; an existing R. armadillidii report was not treated as this record's review. History content was also searched independently of gitignore.
- The NCBI browser and SeqCode live endpoints failed through the browser tool. NCBI's public structured endpoints succeeded. Wiley returned 403 and PubMed's browser page displayed a challenge, but Oxford's abstract and PubMed's structured EFetch supplied the inspected bibliographic evidence. No claim of full-text review or live SeqCode status verification is made.
- An ignored-inclusive filename search throughout the configured kg-microbe checkout found no `nodes.tsv` or `edges.tsv`. Original LPSN transform inputs were therefore unavailable there; their absence was not inferred from the derived inventory alone.
- iModulonDB is not applicable: the YAML has no gene, regulator, pathway, stress-response, or transcriptomic claim. Gene records were checked only to distinguish marker evidence from genome evidence.
- Tracked and staged diffs were empty before report creation. No record, source inventory, code, page, status, curation event, prior report, or history entry was edited. No paid research, external contact, or GitHub mutation was performed.
