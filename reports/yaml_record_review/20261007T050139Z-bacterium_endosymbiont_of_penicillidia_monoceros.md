# YAML Record Review: bacterium endosymbiont of Penicillidia monoceros

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_endosymbiont_of_penicillidia_monoceros.yaml`
- Started UTC: 2026-10-07T04:58:01Z
- Finished UTC: 2026-10-07T05:01:39Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035583`, bacterium endosymbiont of Penicillidia monoceros. It denotes an NCBI bacterial taxon, not the fly host, a culture deposit or the whole parent species. It has rank `FORMA_SPECIALIS`, domain `BACTERIA`, parent `NCBITaxon:1485666`, code 11, `EXACT` grounding, `SEEDED` status, zero source-linked strains, one NCBITAXON NAME attestation and one seed event.

Pinned inventories and `curation/seed_scope.tsv` own input content; `src/taxonmech/extract.py` and `src/taxonmech/seed.py` own extraction/emission behavior. Generated YAML and pages are not manual curation inputs. Eukaryota is outside this review.

## Validation

Commands used `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacterium_endosymbiont_of_penicillidia_monoceros.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bacterium_endosymbiont_of_penicillidia_monoceros.yaml --out /private/tmp/pmo-strict.tsv`: exit 0, one file, zero error files/rows. The actual TSV was read with `cat`; only the tab-separated `file category detail path message` header is present.
- Bounded structured comparisons checked the full source row, all ten ancestors, scope/path rows, source attestation and inline event text. They passed but do not replace corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-all`, `just provenance-check`, `just validate-products`, `just validate-history`, `just test`, `just render-check` and `just qc`. No focused substitute for a corpus-only gate was invented.
- No curator-added graph nodes, literature identifiers or separate target history documents require a narrower term/reference/history check. Schema and strict validation include the inline event.

## Identity and Grounding

The complete pinned row at `data/raw/ncbitaxon_taxa.tsv:222111` supports the exact ID, label, rank, parent, genetic code and 2026-09-13 snapshot. Synonym fields are empty. All ten root-first ancestor entries match the YAML: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Candidatus Aschnera and Candidatus Aschnera chinzeii. The parsed backbone has no direct children for this target.

Fresh [NCBI XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035583&retmode=xml) and [taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035583) confirm identity, forma specialis rank and ancestry. XML confirms parent 1485666/code 11; Datasets supplies the root-inclusive lineage IDs.

The [NCBI browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1035583&lvl=3&mode=node) agrees on name, code and lineage but displays no rank. This conflicts with the pinned inventory and both live structured interfaces. The disagreement is unresolved, not a demonstrated error in emitting the pinned input.

The full scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31590` matches, with an empty unique-name field. Exact parsed type-material, merged-ID and dropped-taxon checks found no target row.

A separate [NCBI taxon 634122](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=634122&lvl=3&mode=node) is Candidatus Aschnera symbiont of Penicillidia monoceros, with an Arsenophonus synonym and the same parent species. Its complete pinned row at `data/raw/ncbitaxon_taxa.tsv:146330`, scope row and native names were read. NCBI retains two IDs; neither a shared host nor common parent authorizes synonym transfer, record merger or an assertion that their individual samples are identical. This report reviews 1035583 only.

## Evidence

The single NCBITAXON attestation correctly counts one NAME. Its ID, label, count, unit and snapshot agree with the inspected source; it does not count isolates, genomes or experiments.

Exact nuccore query `txid1035583[Organism:noexp]` returned twelve records. Every record's GenBank metadata and feature annotations were read through lossless common-field/value-column output, excluding sequence bases and translated residue strings:

| Accessions, all version .1 | Marker | Isolates | Length |
|---|---|---|---|
| AB632439 through AB632442 | Partial 16S rRNA | PeMo1 through PeMo4 | 1470 nt each |
| AB632480 through AB632483 | Partial gyrB CDS | PeMo1 through PeMo4 | 967 nt each |
| AB632521 through AB632524 | Partial groEL CDS | PeMo1 through PeMo4 | PeMo1-2: 1604 nt; PeMo3-4: 923 nt |

All [GenBank source features](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=383212507,383212505,383212503,383212501,383212425,383212423,383212421,383212419,383212347,383212346,383212345,383212344) explicitly identify taxon 1035583 and host Penicillidia monoceros. PeMo1, PeMo3 and PeMo4 were recorded from Hokkaido/Nemuro-shi; PeMo2 from Hokkaido/Shari-gun. The eight CDS annotations use code 11. Records retain an unpublished study reference and a separate 19-MAY-2011 direct submission. None supplies a culture deposit, BioSample, BioProject or assembly link. Four isolate labels and twelve marker records do not establish cultured-strain or genome counts.

The complete [FJ265817.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FJ265817) were separately read to resolve the near match. This 1060-nt 16S marker has source taxon 634122, not 1035583. Its older definition uses Arsenophonus while its current organism/source feature uses Candidatus Aschnera; it is not silently added to the target's twelve sequences.

The inspected introduction and methods of the [2012 primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3280136) distinguish the earlier FJ265817 work from Japanese multilocus sampling. Its genome-size experiment used P. jenynsii bacteriomes. That experiment is not transferred to P. monoceros. Later page reads encountered a browser check, and the publisher alternative failed; the original supplementary specimen table was not inspected. No publication-specific PeMo specimen mapping beyond the inspected GenBank qualifiers is asserted.

The fresh [parent-species genome Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1485666/dataset_report?page_size=1000) contains one assembly, GCA_059737815.1. Its project PRJDB16712 and BioSample SAMD00647859 identify P. jenynsii origin. Parent classification does not make it a P. monoceros genome.

The inspected [LPSN parent-species page](https://lpsn.dsmz.de/species/aschnera-chinzeii) names NyAl1 and AB632412, not PeMo deposits. Its order/family are unspecified, unlike NCBI's carried Enterobacterales/Enterobacteriaceae chain. Parent nomenclature and provider-specific hierarchies are retained as context, not copied into the child.

The structured command `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded before open-ended research. All 28 rows were read; none covers this organism. Component queries are inapplicable; noncoverage is not negative biological evidence.

## Completeness

Optional synonyms, nomenclature, taxonomy mappings, strain listing, genome links, related records, citations, datasets, phenotype evidence and causal graph are absent from the full YAML. The checklist does not require invented optional values. Exact inventory comparisons found no target BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin or BactoTraits row.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered numeric ID boundaries, exact label, stem and host name across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed text. All five SOURCE.json files were separately parsed in full, and history filenames searched independently.

All eight initial candidates were read: the target's three identity rows, the sibling's backbone/scope and two native names, and ATB row `data/catalog/allthebacteria.tsv.xz:66228`. The ATB record denotes Staphylococcus aureus BioSample SAMEA1035583, run ERR083726 and analysis ERZ3070754, with META_FAIL. A numerical namespace collision cannot establish taxon identity; its metadata filter independently excludes a join.

A separate ignored-inclusive search for all twelve marker accessions, versions, PeMo1-PeMo4 variants and FJ265817 found three rows, all inspected in full:

- `data/catalog/ncbi_genbank-0057.jsonl.gz:46023`: GCA_902713755.1, current GenBank assembly named PEMO_1.
- `data/catalog/ncbi_refseq_historical-0002.jsonl.gz:4761`: GCF_902713755.1, suppressed RefSeq record, not live since 2026-02-16.
- `data/catalog/gtdb_genomes-0003.jsonl.gz:12528`: RS_GCF_902713755.1, GTDB Portiera aleyrodidarum_C.

All three denote Candidatus Portiera aleyrodidarum, taxon 91844, with BioSample SAMEA6444016 and isolate PeMo. The assembly name PEMO_1 triggered the case-insensitive isolate search. This is not the target's PeMo1 isolate. The GTDB designation is not a culture-deposit match. No target marker/isolate association was established in those rows; separately parsed metadata/history names had no hits. These are bounded local results, not global absence claims.

Exact NCBI Assembly search returned zero with a phrase-not-found warning; the independent [exact genome Datasets query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035583/dataset_report?page_size=1000) returned an empty object. No supported exact-target assembly link was established. These results do not prove that a genome cannot exist elsewhere.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated record relative to inspected pinned evidence. NCBI's interface-level rank disagreement, the separately retained sibling taxon and provider hierarchy differences remain explicit limitations. Optional marker/literature enrichment is not a required omission.

## Recommended Edits

None required. Do not hand-edit rank/lineage, merge NCBI IDs from shared labels, copy parent nomenclature, invent cultured-strain links, join the Portiera assembly-name collision, or promote status to REVIEWED.

A justified taxonomy correction belongs in pinned source inputs or extraction/seeding logic. Optional future marker evidence requires maintained typed input and generator support preserving taxon, host, isolate, culture deposit, sequence, sample and genome identities.

## Follow-up Checks

Recheck NCBI's source dump and interfaces before an authorized rank correction. Any proposed merger requires authoritative taxon reconciliation, not shared host or parent membership. Inspect original specimen tables before publication-specific isolate claims.

For an authorized enrichment, verify exact provenance and eligible culture identifiers, regenerate through the seeder and run schema, strict and corpus reproduction gates. Sequence quality and biological mechanism claims were not independently tested here.

## Additional Notes

`data/taxa/PATHS.tsv:14613` uniquely maps the ID to the stem. `curation/seed_scope.tsv:322381` matches the inline seed reason/date. The event at 2026-09-13T17:54:04Z is seeding provenance, not human review. `FORMA_SPECIALIS` is allowed under the species-or-below scope rule.

Baseline: branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. An ignore-independent filename search found no earlier target report. The target was reread unchanged before report creation. Only this new report was written; no target YAML, inventory, generated page, earlier report, lifecycle status or history entry was changed. No paid research or GitHub mutation occurred.
