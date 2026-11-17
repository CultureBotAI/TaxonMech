# YAML Record Review: bacterium endosymbiont of Nycteribia pleuralis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_endosymbiont_of_nycteribia_pleuralis.yaml`
- Started UTC: 2026-10-07T04:42:28Z
- Finished UTC: 2026-10-07T04:45:37Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035581`, bacterium endosymbiont of Nycteribia pleuralis. This is a host-associated bacterial taxon, not the fly host, a culture deposit, a marker accession or the entire parent species. The YAML carries `FORMA_SPECIALIS`, `BACTERIA`, parent `NCBITaxon:1485666`, code 11, `EXACT` grounding, `SEEDED` status, zero source-linked strains, one NCBITAXON NAME attestation and one seeding event.

Pinned inventories and `curation/seed_scope.tsv` own source content; `src/taxonmech/extract.py` and `src/taxonmech/seed.py` own extraction/emission behavior. Generated YAML and pages are not manual curation inputs. Eukaryota remains outside this individual review.

## Validation

Commands used `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacterium_endosymbiont_of_nycteribia_pleuralis.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bacterium_endosymbiont_of_nycteribia_pleuralis.yaml --out /private/tmp/npl-strict.tsv`: exit 0, one file, zero error files and zero error rows. The actual TSV was read with `cat`; only the tab-separated `file category detail path message` header is present.
- Bounded structured checks compared the full target source row, all ten ancestor entries, scope/path rows, attestation and inline event text. They passed and do not substitute for corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-all`, `just provenance-check`, `just validate-products`, `just validate-history`, `just test`, `just render-check` and `just qc`. No focused substitute for a corpus-only gate was invented.
- No curator-added graph nodes, literature identifiers or separate target history documents required narrower term/reference/history validation. The inline event is included in schema and strict validation.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:222109` supports the exact identifier, label, rank, parent, genetic code and 2026-09-13 snapshot. Its synonym fields are empty. All ten root-first ancestor entries match the YAML: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Candidatus Aschnera and Candidatus Aschnera chinzeii. No direct children were found in the parsed pinned backbone.

Fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035581&retmode=xml) and [taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035581) agree on exact identity, forma specialis rank and ancestry. XML confirms parent 1485666 and code 11; Datasets supplies the root-inclusive ancestor identifiers.

The inspected [NCBI browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1035581&lvl=3&mode=node) agrees on identity, code and lineage but displays no rank. The pinned row and both live structured interfaces instead give forma specialis. This unresolved source-interface conflict is retained, not silently reconciled. It does not establish an erroneous emission from the pinned input; the pass does not imply that every NCBI interface agrees.

The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31588` supports the exact label and ID and has an empty unique-name field. Exact parsed checks found no target type-material, merged-ID or dropped-taxon row.

## Evidence

The sole NCBITAXON attestation correctly represents one NAME. Its source ID, label, count, unit and snapshot note match inspected evidence; the count does not represent isolates, genomes or experiments.

Exact NCBI nuccore query `txid1035581[Organism:noexp]` returned 17 records. Every record's full GenBank metadata was read using lossless common-field/value-column output, excluding sequence bases and translated residue strings:

| Accessions, all version .1 | Marker | Count | Source isolate qualifiers | Length |
|---|---|---:|---|---|
| AB632427 through AB632431 | Partial 16S rRNA | 5 | NyPl1, NyPl3, NyPl4, NyPl5, NyPl6, respectively | 1473 nt each |
| AB632469 through AB632474 | Partial gyrB CDS | 6 | NyPl1 through NyPl6 | 964 nt each |
| AB632510 through AB632515 | Partial groEL CDS | 6 | NyPl1 through NyPl6 | NyPl1-4: 1601 nt; NyPl5-6: 923 nt |

All inspected [GenBank source features](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=383212489,383212487,383212485,383212483,383212481,383212479,383212407,383212405,383212403,383212401,383212399,383212397,383212336,383212335,383212334,383212333,383212332) explicitly identify taxon 1035581 and host Nycteribia pleuralis. The recorded Japanese localities are Wakayama/Tanabe-shi for NyPl1-2, Mie/Kumano-shi for NyPl3, Hokkaido/Kato-gun for NyPl4, Hokkaido/Nemuro-shi for NyPl5, and Hokkaido/Notsuke-gun for NyPl6. The twelve CDS annotations use code 11. No inspected source feature provides a culture-collection deposit, BioSample, BioProject or assembly link. Six isolate labels and seventeen markers do not establish cultured-strain or genome counts.

GenBank retains an unpublished study reference and a separate direct submission. The related [primary 2012 paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3280136) supplies multilocus context, but its genome-size experiment concerns P. jenynsii and its reported localization experiments concern P. jenynsii and N. allotopa. Those observations are not transferred to N. pleuralis. The original supplementary specimen/accession table was not inspected; no publication-specific NyPl specimen join is asserted.

The inspected [LPSN parent-species page](https://lpsn.dsmz.de/species/aschnera-chinzeii) lists NyAl1 and marker AB632412, not the NyPl labels or markers. It also leaves the parent's order and family unspecified, unlike NCBI's Enterobacterales/Enterobacteriaceae chain. TaxonMech explicitly carries NCBI lineage rather than reconciling provider hierarchies, so this difference is preserved as source context, not grounds to rewrite the lineage. Parent nomenclature/type evidence is not an exact child assertion.

The fresh structured command `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded before open-ended research. All 28 rows were read; none matches this organism. Component queries are inapplicable and noncoverage is not negative biological evidence.

## Completeness

Optional nomenclature, taxonomy mappings, strain listing, genome links, related records, citations, phenotype evidence and causal graph are absent from the complete YAML. The checklist does not require invented optional values. Exact target comparisons found no BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin or BactoTraits inventory row.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered numeric ID boundaries, exact label, filename stem and host name across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed text. All five SOURCE.json files were separately parsed in full; history filenames were searched independently of ignore rules.

All five candidate rows were fully inspected: the target backbone, scope and native scientific name plus two unrelated ATB records:

- `data/catalog/allthebacteria.tsv.xz:66226`: Staphylococcus aureus BioSample SAMEA1035581, run ERR083775 and analysis ERZ3070753, with META_FAIL status. The shared number is a namespace collision, not taxon identity; the filter independently excludes an assembly join.
- `data/catalog/allthebacteria.tsv.xz:1469620`: BioSample SAMN09932417, run SRR7783708 and analysis ERZ9048349, source label Streptomyces pharetrae and Sylph label Streptomyces glaucescens. Its statuses are PASS, but the target digits occur only inside the SeqKit checksum `seqkit.v0.1_DLS_k0_143c0480e3c672ec687d1035581bd6ff`. Neither source species label denotes this symbiont; eligibility filters cannot supply missing identity evidence.

A separate ignored-inclusive search for all seventeen marker accessions, including versions, and NyPl1-NyPl6 found no rows in those roots. Separately parsed metadata and history filenames also had no matches. These are bounded local misses, not global absence claims.

Exact NCBI Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035581/dataset_report?page_size=1000) returned an empty JSON object. No supported assembly association was established; these results do not prove that a genome cannot exist elsewhere.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated record relative to the inspected pinned evidence. NCBI's browser/API rank disagreement and LPSN's different parent hierarchy remain explicit source limitations, not silently resolved discrepancies or demonstrated YAML defects. Optional sequence enrichment is not a required omission from this minimal record.

## Recommended Edits

None required. Do not hand-edit rank or lineage, copy parent nomenclature to the child, promote isolate labels to culture deposits, count markers as genomes, or promote status to REVIEWED.

A justified future taxonomy refresh belongs in the pinned inputs and extraction pipeline, then the seeder. Any future marker representation needs a maintained typed evidence path preserving taxon, host, isolate, deposit, sequence, sample, run, analysis and genome roles.

## Follow-up Checks

Recheck the source dump and NCBI interfaces before an authorized rank change. Inspect any new exact inventory row, regenerate through the seeder and run schema, strict and corpus reproduction gates.

Before publication-specific specimen claims, inspect the original supplementary table and accession/isolate chain. Before adding a strain/genome association, obtain explicit deposit or assembly provenance rather than relying on shared taxonomy, host name or numerical substrings.

## Additional Notes

`data/taxa/PATHS.tsv:14611` uniquely maps the identifier to its stem; `curation/seed_scope.tsv:322379` matches the recorded inclusion reason/date. The inline event text matches that scope and the single attestation.

The event timestamp, 2026-09-13T17:54:04Z, matches the latest extraction time among the inspected raw, ATB and StrainInfo manifests (17:50:44Z, 17:54:04Z and 17:29:00Z), following the inspected `_seed_timestamp` implementation. It is not a human-review date. `FORMA_SPECIALIS` is explicitly permitted by the species-or-below scope rule.

Baseline: branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target was reread unchanged before report creation. Only this new report was written for this target; no YAML, inventory, generated page, prior report, lifecycle status or history entry was changed. No paid research or GitHub mutation was performed.
