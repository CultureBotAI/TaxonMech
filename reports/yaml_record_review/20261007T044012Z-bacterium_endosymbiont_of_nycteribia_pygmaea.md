# YAML Record Review: bacterium endosymbiont of Nycteribia pygmaea

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_endosymbiont_of_nycteribia_pygmaea.yaml`
- Started UTC: 2026-10-07T04:37:11Z
- Finished UTC: 2026-10-07T04:40:12Z
- Verdict: pass

## Target

Reviewed the entire generated `TaxonRecord` for `NCBITaxon:1035580`, bacterium endosymbiont of Nycteribia pygmaea. It denotes the host-associated bacterial taxon, not the host insect, a cultured strain, a sequence record or the whole parent species. Its seeded values are `FORMA_SPECIALIS`, `BACTERIA`, parent `NCBITaxon:1485666`, code 11, `EXACT` grounding, `SEEDED` status, zero source-linked strains, one NCBITAXON NAME attestation and one seeding event.

The maintained owners are pinned inventories, `curation/seed_scope.tsv`, and extraction/seeding behavior in `src/taxonmech/extract.py` and `src/taxonmech/seed.py`. The target YAML and generated pages are not manual curation inputs. Eukaryota was not reviewed again.

## Validation

The documented single-record commands used `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacterium_endosymbiont_of_nycteribia_pygmaea.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bacterium_endosymbiont_of_nycteribia_pygmaea.yaml --out /private/tmp/nyp-strict.tsv`: exit 0, one file scanned, zero files with errors and zero error rows. The actual TSV was read with `cat` and contained only the tab-separated header `file category detail path message`.
- Bounded structured checks read and compared the complete applicable backbone, ancestry, scope, path and source rows and the inline event text. These passed; they are not a substitute for corpus reproduction.
- Not run for this individual review: full-corpus `just verify-corpus`, `just validate-all`, `just provenance-check`, `just validate-products`, `just validate-history`, `just test`, `just render-check` and `just qc`. No focused reproduction or corpus-wide pass is claimed.
- There are no curator-added ontology nodes, causal edges, literature identifiers or separate target history documents to validate more narrowly. Schema and strict validation include the inline seeding event.

## Identity and Grounding

The full `data/raw/ncbitaxon_taxa.tsv:222108` row supports the exact identifier, label, rank, parent, code, source and 2026-09-13 snapshot. All ten ancestor rows match the full root-first lineage: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Candidatus Aschnera and Candidatus Aschnera chinzeii. The pinned backbone has no direct child rows for this taxon.

Fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035580&retmode=xml) and [taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035580) resolve the exact name and identifier with forma specialis rank and the same ancestry. XML confirms parent 1485666 and code 11; Datasets supplies the full ancestor identifiers including root.

The inspected [NCBI Taxonomy browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1035580&lvl=3&mode=node) agrees on identity, code and lineage but displays no rank. The pinned row and both live structured interfaces say forma specialis. This source-interface conflict is unresolved and retained here. It is not evidence of an erroneous emission from the pinned inventory, and the present pass does not assert universal live rank agreement.

The complete native object at `data/catalog/ncbi_names-0005.jsonl.gz:31587` is the exact scientific name with its taxon ID and an empty unique-name field. Source synonym fields are empty. Parsed target checks found no type-material, merged-ID or dropped-taxon row. No broader parent name is treated as an exact synonym of this child.

## Evidence

The one NCBITAXON NAME attestation matches its source identifier, label, count, unit and snapshot note. It is a count of name evidence, not of isolates, sequence accessions, genomes or experiments.

Exact NCBI nuccore search `txid1035580[Organism:noexp]` returned 14 records. Their full GenBank metadata were inspected through lossless common-field/value-column output, excluding only sequence bases and translated residue strings:

| Accessions, all version .1 | Marker | Count | Source isolate qualifiers | Length |
|---|---|---:|---|---|
| AB632423 through AB632426 | Partial 16S rRNA | 4 | NyPy1, NyPy2, NyPy4, NyPy5, respectively | 1475 nt each |
| AB632464 through AB632468 | Partial gyrB CDS | 5 | NyPy1 through NyPy5 | 964 nt each |
| AB632505 through AB632509 | Partial groEL CDS | 5 | NyPy1 through NyPy5 | NyPy1: 1601 nt; NyPy2-5: 923 nt |

Every inspected [GenBank source feature](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=383212477,383212475,383212473,383212471,383212469,383212395,383212393,383212391,383212389,383212387,383212331,383212330,383212329,383212328) explicitly links the record to taxon 1035580 and Nycteribia pygmaea as host. NyPy1 is recorded from Japan: Mie, Kumano-shi; NyPy2-5 from Japan: Hokkaido, Shari-gun. The metadata do not provide a culture-collection deposit, BioSample, BioProject or assembly link. The ten CDS features use code 11 and have protein translations; those protein identifiers are not genome identifiers. Five isolate labels and fourteen markers do not contradict zero supported strain associations in the pinned YAML.

The sequence bibliography retains an unpublished study reference and a separate direct submission. The related [primary 2012 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3280136) provides family-level multilocus context, but its genome-size measurement concerns P. jenynsii and its reported localization experiments concern P. jenynsii and N. allotopa. No such measurement is transferred to N. pygmaea. The exact supplementary specimen/accession table was not inspected, so a publication-level NyPy specimen join is not asserted.

The inspected [LPSN parent-species page](https://lpsn.dsmz.de/species/aschnera-chinzeii) identifies NyAl1 and AB632412, not any NyPy specimen or marker. Parent nomenclature and type evidence must not be copied onto this host-associated child.

The fresh structured check `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` ran successfully before open-ended research. All 28 listed datasets were read; none matches this organism. Component queries are inapplicable and noncoverage is not negative biological evidence.

## Completeness

No nomenclature, taxonomy mapping, strain listing, genome link, related-record link, phenotype evidence, citation or causal graph is present in the complete YAML. The local checklist does not require inventing optional values. Exact target checks found no rows in the pinned BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin or BactoTraits inventories.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered numeric ID boundaries, exact label, filename stem and host name across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed text. All five SOURCE.json files were separately parsed in full and history filenames were searched independently of ignore rules.

All four candidate rows were fully read: the target backbone, scope, native scientific name and an unrelated ATB row. The latter, `data/catalog/allthebacteria.tsv.xz:66225`, denotes Staphylococcus aureus BioSample SAMEA1035580, run ERR083713 and ENA analysis ERZ3070755. The numerical overlap with this taxon ID is not identity evidence. Its META_FAIL status independently excludes an assembly link.

A second ignored-inclusive search for all fourteen marker accessions, including versions, and NyPy1-NyPy5 found no content rows in those roots. Separately parsed metadata and history filenames also had no matches. These are bounded local misses, not claims that evidence is absent everywhere.

Exact NCBI Assembly search returned zero with a phrase-not-found warning, and an independent [genome Datasets query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035580/dataset_report?page_size=1000) returned an empty JSON object. No supported assembly link was established; these bounded results do not prove that a genome cannot exist.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated record relative to the inspected pinned evidence. The browser/API rank conflict remains an explicit external-source limitation. Optional sequence enrichment and the uninspected specimen supplement do not establish a required omission from this minimal taxon record.

## Recommended Edits

None required. Keep generated YAML unchanged and preserve the separation between taxon identity, host identity, isolate qualifier, cultured strain, marker, translation, sample, run, analysis and assembly.

A later source-supported rank change belongs in the pinned taxonomy input and extraction pipeline, followed by the seeder, not a manual record patch. Optional marker enrichment needs a maintained typed representation and cannot be placed in genome fields or unsupported culture-deposit joins.

## Follow-up Checks

Reconcile the conflicting NCBI interfaces against a freshly inspected source dump before any authorized rank refresh. After an upstream change, inspect the new exact inventory row, regenerate through the seeder and run schema, strict and corpus reproduction gates.

Inspect the original specimen supplement before adding publication-specific NyPy observations. Require explicit deposit or assembly provenance before adding strain/genome links; do not infer them from the shared host name or parent species.

## Additional Notes

`data/taxa/PATHS.tsv:14610` uniquely maps the identifier to its stem; `curation/seed_scope.tsv:322378` supplies the exact recorded scope reason and date. The inline event text agrees with the scope and source attestation.

The 2026-09-13T17:54:04Z seed timestamp matches the latest extraction time among the raw, ATB and StrainInfo manifests (17:50:44Z, 17:54:04Z and 17:29:00Z), as specified by the inspected `_seed_timestamp` function. The event is not a human review.

A broader literature search produced host-taxonomy and other bacterial-associate leads; those snippets were not used to support this bacterial record. The attempted PMC view of the 2013 comparative symbiont paper returned a browser challenge and was not used as evidence. No claim of a comprehensive literature census is made.

Baseline branch: `codex/record-review-extensimonas-20261003`; HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target was reread and confirmed unchanged before report creation. Only this new report was written for this target; no taxon YAML, inventory, generated page, previous report, lifecycle status or history entry was changed. No paid research or GitHub mutation was performed.
