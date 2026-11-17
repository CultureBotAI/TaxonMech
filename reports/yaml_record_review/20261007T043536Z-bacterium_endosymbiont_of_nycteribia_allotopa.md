# YAML Record Review: bacterium endosymbiont of Nycteribia allotopa

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_endosymbiont_of_nycteribia_allotopa.yaml`
- Started UTC: 2026-10-07T04:32:11Z
- Finished UTC: 2026-10-07T04:35:36Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035579`, bacterium endosymbiont of Nycteribia allotopa. It is a host-associated bacterial taxon, not the eukaryotic fly, a culture deposit or the entire parent species. The record has rank `FORMA_SPECIALIS`, domain `BACTERIA`, parent `NCBITaxon:1485666`, code 11, grounding `EXACT`, status `SEEDED`, zero source-linked strains, one NCBITAXON NAME attestation and one seeding event.

Generated fields are owned by pinned inventories and `curation/seed_scope.tsv`, with extraction and emission behavior in `src/taxonmech/extract.py` and `src/taxonmech/seed.py`. No generated YAML or page may be hand-edited to implement future corrections.

## Validation

Commands used the prefix `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacterium_endosymbiont_of_nycteribia_allotopa.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bacterium_endosymbiont_of_nycteribia_allotopa.yaml --out /private/tmp/nya-strict.tsv`: exit 0, one file, zero error files and zero error rows. `cat /private/tmp/nya-strict.tsv` confirmed only the tab-separated header `file category detail path message`.
- Bounded structured source checks compared the target backbone row, all ten ancestor rows, path and scope rows, source attestation, inventory membership and inline event text. All passed. These checks are not a focused replacement for corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-all`, `just provenance-check`, `just validate-products`, `just validate-history`, `just test`, `just render-check` and `just qc`. This review does not claim their coverage.
- No curator-added ontology node, causal edge, cited DOI/PMID or separate target history document occurs in the record. The inline event was checked by the schema and strict validators.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:222107` supports the exact identifier, name, rank, parent, code, source and 2026-09-13 snapshot. Its synonym fields are empty. The full ten-ancestor chain matches the YAML, from root and cellular organisms through Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Candidatus Aschnera and Candidatus Aschnera chinzeii. The parsed pinned backbone has no direct children of this taxon.

Fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035579&retmode=xml) and [taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035579) support the same identity, rank and placement. XML confirms parent 1485666 and code 11; Datasets preserves the root-first ancestor identifiers.

The inspected [NCBI browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1035579&lvl=3&mode=node) agrees on identity, code and lineage but displays no rank. The pinned inventory and both structured interfaces instead give forma specialis. This unresolved interface conflict is preserved. It does not demonstrate a wrong emission from the pinned inventory; the pass does not assert agreement among every live NCBI interface.

The full native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31586` has the exact taxon ID and label and an empty unique-name field. Exact parsed checks found no target type-material, merged-ID or dropped-taxon row.

## Evidence

The sole NCBITAXON attestation correctly represents one NAME, not a count of isolates, genomes or experiments. Its identifier, label, unit, count and snapshot note match the inspected native and transformed rows.

Exact NCBI nuccore search `txid1035579[Organism:noexp]` returned 29 records. Every record's GenBank metadata was read, using lossless common-field and value-column output after excluding sequence bases and translated residue strings:

| Accessions, all version .1 | Marker | Count | Isolate qualifiers | Length |
|---|---|---:|---|---|
| AB632412 through AB632422 | Partial 16S rRNA | 11 | NyAl1 through NyAl11 | 1473 nt each |
| AB632455 through AB632463 | Partial gyrB CDS | 9 | NyAl3 through NyAl11 | 964 nt each |
| AB632496 through AB632504 | Partial groEL CDS | 9 | NyAl3 through NyAl11 | 1601 nt, except NyAl8 at 923 nt |

The [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=383212467,383212465,383212463,383212461,383212459,383212457,383212455,383212453,383212451,383212385,383212383,383212381,383212379,383212377,383212375,383212373,383212371,383212369,383212327,383212326,383212325,383212324,383212323,383212322,383212321,383212320,383212319,383212318,383212317) explicitly name taxon 1035579 and Nycteribia allotopa as host. Localities are Hyogo/Sayou-gun for NyAl1-2, Okinawa/OkinawaIs. for NyAl3-7, Gifu/Gujo-shi for NyAl8-9, and Wakayama/Nishimuro-gun for NyAl10-11. No source feature supplies a culture-collection deposit, BioSample, BioProject or assembly link. The 18 CDS annotations use code 11. Marker and protein accessions do not count as genomes, and an isolate qualifier alone does not establish a cultured strain association.

The inspected [LPSN parent-species page](https://lpsn.dsmz.de/species/aschnera-chinzeii) names NyAl1 as nomenclatural type and AB632412 as its 16S marker. The independently read [AB632412.1 record](https://www.ncbi.nlm.nih.gov/nuccore/AB632412.1) provides the exact NyAl1-to-target-taxonomy connection. LPSN distinguishes not-validly-published nomenclatural status from pro-valid publication and a pro-correct name. These species-level assertions do not make this child taxon equivalent to its parent or demonstrate a culture deposit. No corresponding pinned child LPSN row was found.

The [primary 2012 paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3280136) directly lists AB632414, AB632455 and AB632496 in Table 1; the inspected GenBank records identify all three as NyAl3 markers. The paper reports N. allotopa bacteriocyte localization, but its genome-size measurement concerns P. jenynsii. It describes vitamin provisioning as a hypothesis, not an established function. No such functional or genome-size claim belongs on this child merely through shared taxonomy. Supplementary specimen tables and figures were not inspected in this review.

Before open-ended web research, the resolved runner `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` was attempted. The sandboxed attempt failed DNS resolution; the approved read-only network retry succeeded. All 28 fresh dataset rows were read. None matches this organism, so component queries are inapplicable, not negative biological evidence.

## Completeness

Optional nomenclature, taxonomy mappings, strain listing, genome links, related-record links, citations, phenotype evidence and causal graph are empty. Exact target checks found no BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin or BactoTraits inventory row. Zero source-linked strains is consistent with those inputs; the 11 external isolate designations do not automatically belong in the source-linked strain count.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered numeric taxon boundaries, exact name, filename stem and host name in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed text. All five SOURCE.json files were separately parsed in full, and history filenames were searched independently of ignore rules.

Four identity candidates were fully read: the backbone, scope, native scientific name and an unrelated ATB row. At `data/catalog/allthebacteria.tsv.xz:66224`, SAMEA1035579 is a Staphylococcus aureus BioSample with run ERR083737 and ENA analysis ERZ3070745, not this taxon. Its assembly metadata also carry META_FAIL. The shared numeric suffix is not a join key.

A separate ignored-inclusive search for all 29 accessions, including versions, and NyAl1-NyAl11 found no rows in those roots; separately parsed metadata and history filenames also had no matches. These are bounded local misses, not assertions of global absence.

Exact NCBI Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035579/dataset_report?page_size=1000) returned an empty JSON object. No supported assembly association was established, but these responses do not prove that no genome could exist elsewhere.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated record relative to the inspected pinned evidence. The live browser/API rank disagreement is an explicit source limitation, not a resolved conflict or demonstrated YAML defect. Optional marker/type-material enrichment and uninspected supplements do not invalidate the current minimally attested record.

## Recommended Edits

None required. Do not hand-edit the generated rank, copy the parent nomenclature wholesale, treat NyAl1 as a culture-collection accession, count marker genes as genomes, or promote status to REVIEWED.

A future justified source refresh belongs in the extractor and pinned inputs, then the seeder. Future marker or type-material enrichment requires a maintained representation preserving taxon, isolate, parent-species type and sequence roles separately.

## Follow-up Checks

Recheck the source taxonomy dump and all NCBI interfaces before resolving the rank discrepancy. For an authorized upstream refresh, inspect the exact new inventory row, regenerate through the seeder, and run the documented schema, strict and corpus reproduction gates.

Before additional specimen-level claims, inspect the original supplements and retain exact accession/isolate linkage. Before strain/genome joins, obtain explicit culture-deposit or assembly provenance rather than promoting the isolate labels.

## Additional Notes

`data/taxa/PATHS.tsv:14608` uniquely maps the identifier to its stem. `curation/seed_scope.tsv:322377` matches the recorded inclusion reason and date. The inline event text matches that scope and the single source attestation.

The event timestamp, 2026-09-13T17:54:04Z, equals the latest inspected extraction timestamp among the raw, ATB and StrainInfo manifests (17:50:44Z, 17:54:04Z and 17:29:00Z). This follows the inspected `_seed_timestamp` implementation; it is not a later human review.

Review baseline: branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target was reread unchanged before report creation. Only this new report was written for this target. No YAML, inventory, generated page, previous report, history entry or lifecycle status changed. No paid research or GitHub mutation occurred. Eukaryota remains out of this review's scope.
