# YAML Record Review: bacterium endosymbiont of Basilia rybini

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_endosymbiont_of_basilia_rybini.yaml`
- Started UTC: 2026-10-07T04:25:04Z
- Finished UTC: 2026-10-07T04:29:44Z
- Verdict: pass

## Target

Reviewed the entire generated `TaxonRecord` for `NCBITaxon:1035578`, label `bacterium endosymbiont of Basilia rybini`. The YAML carries rank `FORMA_SPECIALIS`, domain `BACTERIA`, parent `NCBITaxon:1485666`, grounding `EXACT`, mapping status `SEEDED`, genetic code 11, zero source-linked strains, one NCBITAXON name attestation, and one seeding event. This denotes a host-associated bacterial taxon, not the eukaryotic host, an entire parent species, or a culture deposit. Eukaryota records were not reopened.

The maintained inputs are the pinned inventories and `curation/seed_scope.tsv`; extraction and emission behavior belong to `src/taxonmech/extract.py` and `src/taxonmech/seed.py`. The YAML is not a hand-editable curation input.

## Validation

The documented single-record commands ran with `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacterium_endosymbiont_of_basilia_rybini.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bacterium_endosymbiont_of_basilia_rybini.yaml --out /private/tmp/bry-strict.tsv`: exit 0, one file scanned, zero files with errors and zero error rows. The actual TSV was read with `cat`; it contains only `file category detail path message` as tab-separated header fields.
- Bounded structured comparisons read the full applicable backbone, scope, path, native-name and inventory rows, followed all ten ancestors, and compared the sole source attestation. These checks passed; they are not a substitute for the documented corpus reproduction gate.
- Full-corpus gates `just verify-corpus`, `just validate-all`, `just provenance-check`, `just validate-products`, `just validate-history`, `just test`, `just render-check`, and `just qc` were not run for this individual review. No focused replacement was invented for a corpus-only gate.
- No causal graph, curator-added ontology node, literature citation, or separate target history record required a narrower identifier or history validation. The inline seeding event is covered by schema and strict validation.

## Identity and Grounding

The full row at `data/raw/ncbitaxon_taxa.tsv:222106` matches the identifier, label, rank, immediate parent, genetic code and 2026-09-13 snapshot. All ten ancestor identifiers, labels and ranks match the pinned parent chain: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Candidatus Aschnera and Candidatus Aschnera chinzeii. No direct children were found in that parsed backbone.

Fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035578&retmode=xml) and [NCBI taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035578) resolve the exact identifier and label, with rank forma specialis and the same placement. XML confirms code 11 and parent 1485666; Datasets includes the root-first ancestor identifiers.

There is an unresolved source-interface conflict: the inspected [NCBI Taxonomy browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1035578&lvl=3&mode=node) displays no rank, while the pinned row and both live structured interfaces give forma specialis. The browser agrees on identity, code and lineage. This discrepancy is preserved, not silently reconciled. It does not demonstrate an erroneous emission from the pinned input. The present pass is a judgement on this generated record, not a claim that all NCBI interfaces agree.

The complete native row at `data/catalog/ncbi_names-0005.jsonl.gz:31585` supplies the exact scientific name, exact taxon ID and an empty unique-name field. No target synonym, merged-ID, dropped-taxon or type-material row was found in the corresponding parsed pinned inputs. The parent name is lineage context, not evidence that this host-associated child has the parent's nomenclatural or type-strain assertions.

## Evidence

The single source attestation correctly counts one NCBITAXON NAME, not an isolate, genome or experiment. The full source and native-name rows support its source ID, source label, count, unit and snapshot note.

Exact NCBI nuccore search `txid1035578[Organism:noexp]` returned three records. Their complete GenBank metadata were inspected, excluding sequence bases and translated residue strings:

| Accession | Molecule represented | Length | Source isolate |
|---|---|---:|---|
| [AB632411.1](https://www.ncbi.nlm.nih.gov/nuccore/AB632411.1) | Partial 16S rRNA gene | 1478 nt | BaRy1 |
| [AB632454.1](https://www.ncbi.nlm.nih.gov/nuccore/AB632454.1) | Partial gyrB CDS | 964 nt | BaRy1 |
| [AB632495.1](https://www.ncbi.nlm.nih.gov/nuccore/AB632495.1) | Partial groEL CDS | 923 nt | BaRy1 |

Each source feature explicitly identifies taxon 1035578, host Basilia rybini (bat fly), isolate BaRy1, and locality Japan: Hokkaido, Notsuke-gun. They do not supply a culture-collection deposit, BioSample, BioProject or assembly linkage. The CDS metadata carry code 11 and protein accessions BAM09028.1 and BAM09069.1 respectively; these are translations, not genome identifiers. These observations establish bounded marker/isolate provenance, not three genomes or a cultured strain that must increase `strain_count`.

The GenBank bibliography labels the study reference unpublished and supplies a separate direct submission. A related [primary bat-fly symbiosis paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3280136) reports multilocus phylogenetic work, but the exact supplementary specimen/accession table was not inspected. Its genome-size experiment concerns P. jenynsii, and localization experiments concern P. jenynsii and N. allotopa. Those observations must not be transferred to B. rybini through shared parent taxonomy. No exact BaRy1-to-published-specimen join or host-bat identity is asserted here.

The resolved iModulonDB adapter's fresh dataset listing was read in full: 28 dataset rows, none applicable to this taxon or its parent organism. Component search was therefore inapplicable, not evidence against any biological function.

## Completeness

The complete record has no nomenclature, taxonomy mappings, strain listing, genome assemblies, genome records, related-record links, phenotype evidence, citations or causal graph. These optional slots need not be invented for a minimally attested taxon. Exact comparisons found no target rows in the pinned BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin or BactoTraits inventories.

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. They covered numeric ID boundaries, exact label, filename stem and the host-name form, including compressed text. All five SOURCE.json files were separately parsed in full, and history filenames were searched independently of ignore rules. All candidate native rows were fully inspected.

The identity search yielded four logical rows: the backbone, scope, native scientific name, and an unrelated ATB record. The ATB row at `data/catalog/allthebacteria.tsv.xz:66223` is Staphylococcus aureus with BioSample SAMEA1035578, run ERR083833 and ENA analysis ERZ3070742. The number is a namespace collision, not taxon evidence. Its META_FAIL assembly status also excludes a link independently of the identity mismatch. No genome join is justified.

A second ignored-inclusive, compressed-content search for AB632411, AB632454, AB632495 (including versions) and BaRy1 found no rows in those roots; separately parsed source metadata and history filenames also had no matches. These are bounded local misses, not a claim that such evidence cannot exist externally or elsewhere in the filesystem.

Exact NCBI Assembly search returned zero and an explicit phrase-not-found warning. The independently inspected [NCBI genome Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035578/dataset_report?page_size=1000) was an empty JSON object. Neither result proves biological absence of a genome; no supported assembly link was established in this review.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the emitted record relative to the inspected pinned evidence. The browser/API rank conflict is an explicit unresolved source limitation, not a silently resolved finding or a demonstrated YAML defect. Optional marker enrichment and the uninspected supplementary specimen table do not make the current minimal seeded record invalid.

## Recommended Edits

None required for this record. Do not hand-edit generated taxonomy, add BaRy1 as a culture deposit, count marker genes as genomes, or promote the mapping status.

For later investigation of the rank discrepancy, recheck NCBI's source dump and interfaces; a justified source refresh belongs in the extraction pipeline and pinned inventory, followed by the seeder. Any future marker representation requires a maintained, explicitly typed evidence path, not insertion into an unsupported strain or assembly join.

## Follow-up Checks

If upstream taxonomy changes, re-run extraction and review the exact source row before regenerating through the seeder, then run the documented schema, strict and corpus reproduction gates. Do not change the rank based solely on the browser while structured sources disagree.

Before any publication-backed specimen enrichment, inspect the original supplementary table and verify the exact BaRy1/accession chain. Before a future strain or genome link, obtain explicit deposit or assembly evidence and preserve its source identifiers and scope. Current exact assembly searches can be repeated without widening the query to the whole parent species.

## Additional Notes

`data/taxa/PATHS.tsv:14607` uniquely associates this identifier with its current stem. `curation/seed_scope.tsv:322376` records the attested-name inclusion and 2026-09-13 date. `FORMA_SPECIALIS` is explicitly an allowed species-or-below rank in `src/taxonmech/seed.py`.

The inline seeding event is dated 2026-09-13T17:54:04Z. The inspected raw, ATB and StrainInfo manifests have extraction times 17:50:44Z, 17:54:04Z and 17:29:00Z on that date, respectively. The generated event is compatible with the latest input-manifest time; it is not a later human review.

This is a read-only individual review on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The other session was reported closed and git lists only the original worktree. The target was reread and confirmed byte-identical before report creation. Only this new report was written; no YAML, source inventory, generated page, prior report, lifecycle status or history entry was changed. No paid research or GitHub mutation was performed. Passing this review does not imply full-corpus QC or human REVIEWED status.
