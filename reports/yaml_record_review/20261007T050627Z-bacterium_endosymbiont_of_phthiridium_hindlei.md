# YAML Record Review: bacterium endosymbiont of Phthiridium hindlei

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_endosymbiont_of_phthiridium_hindlei.yaml`
- Started UTC: 2026-10-07T05:02:56Z
- Finished UTC: 2026-10-07T05:06:27Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035584`, bacterium endosymbiont of Phthiridium hindlei. It denotes a host-associated bacterial taxon, not the fly host, a culture deposit or the entire parent species. The YAML carries `FORMA_SPECIALIS`, `BACTERIA`, parent `NCBITaxon:1485666`, code 11, `EXACT` grounding, `SEEDED` status, zero source-linked strains, one NCBITAXON NAME attestation and one seed event.

Pinned inventories and `curation/seed_scope.tsv` own source content; `src/taxonmech/extract.py` and `src/taxonmech/seed.py` own extraction/emission behavior. Generated YAML and pages are not manual curation inputs. Eukaryota is outside this individual review.

## Validation

Commands used `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacterium_endosymbiont_of_phthiridium_hindlei.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bacterium_endosymbiont_of_phthiridium_hindlei.yaml --out /private/tmp/phi-strict.tsv`: exit 0, one file, zero error files/rows. The actual TSV was read with `cat`; only the tab-separated `file category detail path message` header is present.
- Bounded structured comparisons passed for the full source row, all ten ancestors, path/scope rows, source attestation and inline event text. These are not corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-all`, `just provenance-check`, `just validate-products`, `just validate-history`, `just test`, `just render-check` and `just qc`. No focused substitute for a corpus-only gate was invented.
- No curator-added graph nodes, literature identifiers or separate target history documents require a narrower term/reference/history check. Schema and strict validation include the inline event.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:222112` supports the exact identifier, label, rank, parent, code and 2026-09-13 snapshot. Synonym fields are empty. All ten root-first ancestors match: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Candidatus Aschnera and Candidatus Aschnera chinzeii. No direct children were found in the parsed pinned backbone.

Fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035584&retmode=xml) and [taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035584) agree on identity, forma specialis rank and ancestry. XML confirms parent 1485666/code 11; Datasets supplies root-inclusive lineage identifiers.

The inspected [NCBI browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1035584&lvl=3&mode=node) agrees on identity, code and lineage but displays no rank, unlike the pinned row and both live structured interfaces. This unresolved source-interface conflict is retained; it does not demonstrate a wrong emission from the pinned input.

The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31591` supports the exact ID and label and has an empty unique-name field. Exact parsed checks found no target type-material, merged-ID or dropped-taxon row.

## Evidence

The single NCBITAXON attestation correctly represents one NAME. Its source ID, label, count, unit and snapshot match inspected evidence. One attested name is not a count of isolates, genomes or experiments.

Exact nuccore query `txid1035584[Organism:noexp]` returned nine records. All GenBank metadata and feature annotations were read through lossless common-field/value-column output, excluding sequence bases and translated residue strings:

| Accessions, all version .1 | Marker | Isolates | Length |
|---|---|---|---|
| AB632443 through AB632445 | Partial 16S rRNA | PhHi1 through PhHi3 | PhHi1/3: 1480 nt; PhHi2: 1479 nt |
| AB632484 through AB632486 | Partial gyrB CDS | PhHi1 through PhHi3 | 964 nt each |
| AB632525 through AB632527 | Partial groEL CDS | PhHi1 through PhHi3 | 1601 nt each |

All inspected [GenBank source features](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=383212513,383212511,383212509,383212431,383212429,383212427,383212350,383212349,383212348) explicitly identify taxon 1035584 and host Phthiridium hindlei. PhHi1 was recorded from Nagano/Kiso-gun; PhHi2-3 from Osaka/Sennan-gun. The six CDS annotations use code 11. Each marker retains an unpublished study reference and a separate 19-MAY-2011 direct submission. No source feature supplies a culture deposit, BioSample, BioProject or assembly link. Three isolate labels and nine marker records do not establish cultured-strain or genome counts.

The introduction and methods of the related [2012 primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3280136), inspected earlier in this review turn, provide multilocus context. Its genome-size experiment used P. jenynsii bacteriomes, not Phthiridium hindlei. No genome size or localization result is transferred to this target. Later full-text requests encountered a browser check and the publisher alternative failed. The original supplementary specimen table was not inspected; no publication-specific PhHi specimen join is asserted.

The [parent-species genome Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1485666/dataset_report?page_size=1000), freshly read during this turn, contains GCA_059737815.1. Project PRJDB16712 and BioSample SAMD00647859 identify P. jenynsii origin. A shared parent classification is not evidence that this is a Phthiridium hindlei-associated assembly.

The [LPSN parent-species page](https://lpsn.dsmz.de/species/aschnera-chinzeii), also inspected during this turn, names NyAl1/AB632412, not PhHi deposits. It leaves the parent's order/family unspecified, unlike NCBI's carried Enterobacterales/Enterobacteriaceae lineage. Parent nomenclature and provider hierarchy differences are preserved as context, not copied into this child.

The fresh structured command `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded before open-ended research. All 28 rows were read; no organism matches. Component queries are inapplicable, and noncoverage is not negative biological evidence.

## Completeness

Optional synonyms, nomenclature, taxonomy mappings, strain listing, genome links, related records, citations, datasets, phenotype evidence and causal graph are absent from the complete YAML. The checklist does not require invented optional values. Exact comparisons found no target BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin or BactoTraits inventory row.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered numeric ID boundaries, exact label, filename stem and host name across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed text. All five SOURCE.json files were separately parsed in full; history filenames were independently searched.

All five candidates were inspected completely: the target backbone/scope/native name and two ATB namespace collisions:

- `data/catalog/allthebacteria.tsv.xz:66229`: Staphylococcus aureus BioSample SAMEA1035584, run ERR083767, analysis ERZ3070750, META_FAIL. The shared digits are in a sample identifier, not a taxon identifier; the filter independently excludes a join.
- `data/catalog/allthebacteria.tsv.xz:1020978`: Salmonella enterica subsp. enterica serovar Newport, BioSample SAMN02345175, run SRR1035584, analysis ERZ4069837, PASS. Here the same digits identify a sequencing run. Passing filters do not supply missing biological identity.

A separate ignored-inclusive search for all nine marker accessions, including versions, and PhHi1-PhHi3 spelling variants found no rows in those roots. Separately parsed SOURCE.json metadata and history filenames also had no hits. These are bounded local misses, not claims of universal absence.

Exact NCBI Assembly search returned zero with a phrase-not-found warning. The independent [exact genome Datasets query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035584/dataset_report?page_size=1000) returned an empty object. No supported exact-target assembly association was established; a genome elsewhere cannot be ruled out.

The schema's `strain_count` counts BacDive records under the target/subtree. With no children or exact BacDive match, zero is supported. Marker isolate labels are not eligible culture-deposit links. Optional sequence enrichment is not a missing required representation.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated record relative to the inspected pinned evidence. NCBI's browser/API rank conflict and provider-specific parent hierarchy remain explicit limitations, not silently resolved discrepancies. Pass does not mean all upstream interfaces agree or that optional literature context is fully curated.

## Recommended Edits

None required. Do not manually edit rank/lineage, copy parent nomenclature, attach the P. jenynsii genome by shared taxonomy, count markers as genomes, promote isolate labels to culture deposits, or promote status to REVIEWED.

A justified future taxonomy correction belongs in the pinned inputs or extraction/seeding logic. Optional marker enrichment needs maintained typed evidence and generator support that preserve taxon, host, isolate, deposit, sequence, sample and genome identities.

## Follow-up Checks

Recheck the source dump and NCBI interfaces before an authorized rank correction. Inspect the original supplementary table before publication-specific specimen assertions. Obtain explicit source/deposit/assembly provenance before adding any genome link.

For an authorized enrichment, regenerate through the seeder and run schema, strict and corpus reproduction gates. Sequence quality, pathway completeness and causal biological mechanisms were not tested in this read-only review.

## Additional Notes

`data/taxa/PATHS.tsv:14614` uniquely maps the identifier to its stem. `curation/seed_scope.tsv:322382` agrees with the inline seed reason/date. The timestamp 2026-09-13T17:54:04Z matches the newest of the inspected raw, ATB and StrainInfo extraction times (17:50:44Z, 17:54:04Z and 17:29:00Z), following the inspected `_seed_timestamp` implementation. It is not a human-review date. `FORMA_SPECIALIS` is allowed by the species-or-below scope rule.

Baseline: branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target was reread unchanged, and an ignore-independent filename search found no earlier target report. Only this new report was written for this target; no YAML, inventory, generated page, previous report, lifecycle status or history entry was changed. No paid research or GitHub mutation was performed.
