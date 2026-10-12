# YAML Record Review: bacterium endosymbiont of Penicillidia jenynsii

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_endosymbiont_of_penicillidia_jenynsii.yaml`
- Started UTC: 2026-10-07T04:47:54Z
- Finished UTC: 2026-10-07T04:55:11Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035582`, bacterium endosymbiont of Penicillidia jenynsii. The YAML represents a host-associated bacterial taxon, not the fly host, a culture deposit or the entire parent species. It carries `FORMA_SPECIALIS`, `BACTERIA`, parent `NCBITaxon:1485666`, code 11, `EXACT` grounding, `SEEDED` status, zero source-linked strains, one NCBITAXON NAME attestation and one seeding event.

Pinned inventories and `curation/seed_scope.tsv` own source content; `src/taxonmech/extract.py` and `src/taxonmech/seed.py` own extraction/emission behavior. Generated YAML and pages are not manual curation inputs. Eukaryota is outside this individual review.

## Validation

Commands used `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacterium_endosymbiont_of_penicillidia_jenynsii.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bacterium_endosymbiont_of_penicillidia_jenynsii.yaml --out /private/tmp/pje-strict.tsv`: exit 0, one file, zero error files and zero error rows. The actual TSV was read with `cat`; it contains only the tab-separated `file category detail path message` header.
- Bounded structured comparisons of the full source row, ten ancestor entries, scope/path rows, attestation and inline event passed. These are not corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-all`, `just provenance-check`, `just validate-products`, `just validate-history`, `just test`, `just render-check` and `just qc`. No focused substitute for a corpus-only gate was invented.
- No curator-added graph nodes, literature identifiers or separate target history documents required narrower term/reference/history validation. Schema and strict validation include the inline event.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:222110` supports the exact identifier, label, rank, parent, genetic code and 2026-09-13 snapshot. Its synonym fields are empty. All ten root-first ancestors match: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Candidatus Aschnera and Candidatus Aschnera chinzeii. No direct children were found in the parsed pinned backbone.

Fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035582&retmode=xml) and [taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035582) agree on identity, forma specialis rank and ancestry. XML confirms parent 1485666 and code 11; Datasets supplies the root-inclusive ancestor identifiers.

The inspected [NCBI browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1035582&lvl=3&mode=node) agrees on identity, code and lineage but displays no rank. The pinned row and both structured interfaces instead give forma specialis. This source-interface disagreement remains unresolved; it does not demonstrate an erroneous emission from the pinned input.

The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31589` supports the exact ID and label, with an empty unique-name field. Exact parsed checks found no target type-material, merged-ID or dropped-taxon row.

The shared host name does not identify the bacterium: `NCBITaxon:1034762`, Wolbachia endosymbiont of Penicillidia jenynsii, is a different species with parent 2640676. Its full backbone, scope and native-name rows were inspected and excluded, not merged with this Aschnera-associated taxon.

## Evidence

The NCBITAXON attestation accurately represents one NAME with the supported ID, label and snapshot. Its assertion count is not a strain, genome or experiment count.

Exact NCBI nuccore query `txid1035582[Organism:noexp]` returned 17 records. All GenBank metadata and features were inspected in lossless common-field/value-column output, excluding sequence bases and translated residue strings:

| Accessions, all version .1 | Marker | Isolates | Length |
|---|---|---|---|
| AB632432 through AB632438 | Partial 16S rRNA | PeJe1 through PeJe7 | PeJe1-2: 1464 nt; PeJe3-7: 1465 nt |
| AB632475 through AB632479 | Partial gyrB CDS | PeJe3 through PeJe7 | 967 nt each |
| AB632516 through AB632520 | Partial groEL CDS | PeJe3 through PeJe7 | PeJe4: 920 nt; others: 1604 nt |

The [GenBank source features](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=383212499,383212497,383212495,383212493,383212491,383212417,383212415,383212413,383212411,383212409,383212343,383212342,383212341,383212340,383212339,383212338,383212337) identify taxon 1035582 and host Penicillidia jenynsii. Localities are Hyogo/Sayou-gun for PeJe1-2, Mie/Tsu-shi for PeJe3, Gifu/Gujo-shi for PeJe4, Nagano/Nakano-shi for PeJe5 and Wakayama/Nishimuro-gun for PeJe6-7. The ten CDS annotations use code 11. No inspected marker source feature supplies a culture deposit, BioSample, BioProject or assembly. Seven isolate labels do not establish seven cultured strains.

The [2012 primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3280136) explicitly links PeJe3 to AB632434, AB632475 and AB632516 in Table 1. It reports P. jenynsii localization and genome-size experiments; milk-gland localization supports the authors' transmission interpretation, not a direct transfer experiment. The original supplementary specimen table was not inspected. No equivalence between these older isolates and a later genome sample is asserted.

A separate [genome paper](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1336919/full), DOI 10.3389/fmicb.2023.1336919 and PMID 38318130, describes pooled P. jenynsii bacteriomes and hybrid sequencing. Its proposed vitamin-provisioning role is based on retained biosynthetic capacity, not intervention-proven nutrient transfer. The DOI, PMID, title and abstract were cross-checked through PubMed.

The full native assembly row at `data/catalog/ncbi_genbank-0055.jsonl.gz:15431` and the complete [parent-species genome Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1485666/dataset_report?page_size=1000) identify one current GenBank assembly, `GCA_059737815.1`, classified under parent taxon 1485666, not exact child 1035582. It is metagenome-derived, labeled isolate `kw-01`, and totals 766,767 nt. The [assembly component response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_059737815.1/sequence_reports?page_size=1000) explicitly links chromosome AP028961.1 (748,020 nt) and plasmid pAchinz-1/AP028962.1 (18,747 nt).

The [two GenBank records](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=AP028961,AP028962) independently supply host P. jenynsii, bacteriome origin, parent taxon 1485666, `kw-01`, PRJDB16712, derived BioSample SAMD00647859 and reads DRR505509/DRR505510. Datasets embeds the BioSample's `derived_from` links to SAMD00647857 and SAMD00647858. Its isolate attribute says `not applicable`, whereas assembly and GenBank metadata say `kw-01`; these source fields are preserved, not silently reconciled. No culture-deposit or PeJe1-PeJe7 equivalence was established. Genome headers and source features were read; 1,274 chromosome and 20 plasmid non-source features, sequence bases and translated strings were not reviewed.

The inspected [LPSN parent-species page](https://lpsn.dsmz.de/species/aschnera-chinzeii) names NyAl1/AB632412, not a PeJe culture deposit. It leaves the parent's order and family unspecified, unlike NCBI's carried lineage. Neither parent nomenclature nor a different provider hierarchy is an exact child assertion.

The structured command `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded before open-ended research. All 28 rows were read; no covered organism matches. Component queries are inapplicable; noncoverage is not negative biological evidence.

## Completeness

The complete YAML has no optional nomenclature, taxonomy mappings, strain listing, genome links, related records, citations, phenotype evidence, datasets or causal graph. The checklist does not require filling optional slots. Exact target comparisons found no BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin or BactoTraits inventory row.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered numeric ID boundaries, exact label, stem and host name across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed text. All five SOURCE.json files were separately parsed in full; history filenames were independently searched.

All eight identity candidates were read: target and Wolbachia backbone/scope/native-name rows, plus two ATB collisions:

- `data/catalog/allthebacteria.tsv.xz:66227`: Staphylococcus aureus sample SAMEA1035582, run ERR083860, analysis ERZ3070758, META_FAIL. Shared digits are not taxon identity; the filter separately excludes an assembly join.
- `data/catalog/allthebacteria.tsv.xz:66860`: Streptococcus agalactiae sample SAMEA10369167, run ERR10672751, analysis ERZ25086779, PASS. Digits 1035582 appear only within checksum `seqkit.v0.1_DLS_k0_6b4ff69ee0d23c319722c1035582aeba`. Passing filters do not supply identity evidence.

Follow-up ignored-inclusive searches covered all seventeen markers, PeJe1-PeJe7, AP028961/AP028962, SAMD00647857-59, PRJDB16712, DRR505509/510, DRA017199/200 and GCA_059737815 with versions. They found the one native assembly row described above, with no other hits in those roots. Full metadata parsing and history filename checks found none. These are bounded local results, not global absence claims.

Exact Assembly search returned zero with a phrase-not-found warning; exact [child-taxon genome Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035582/dataset_report?page_size=1000) returned an empty object. The parent-classified genome nevertheless exists both publicly and locally. It must not be reported as absent.

Under `src/taxonmech/schema/taxonmech.yaml`, `strain_count` counts BacDive records; strain genome links require explicit identity evidence. `docs/STRAIN_GENOMES.md` likewise limits generated strain links to listed strains. The parent-classified metagenomic assembly does not justify inventing a cultured strain or increasing this count. Optional record-level `datasets` and literature evidence could capture supported context in an authorized curation workflow; their omission is not a missing required representation.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated record relative to inspected pinned evidence. The browser/API rank conflict, provider-specific parent hierarchy and source-specific isolate fields remain explicit limitations. Pass does not mean all upstream interfaces agree or that the optional literature/genome context is fully curated.

## Recommended Edits

None required. Do not manually edit generated YAML, replace the pinned rank from the browser alone, transfer parent nomenclature, promote sample/isolate labels to culture deposits, merge the Wolbachia near miss, or promote status to REVIEWED.

Optional future enrichment should preserve the supported publication, host, parent-taxon classification, assembly components and sample derivation in typed evidence. Its maintained input and extraction/seeding support must be established in an authorized curation change; use existing schema-supported dataset/evidence fields where appropriate. Any identity correction belongs in pinned source inputs or the extractor/seeder, not in this review report or generated record.

## Follow-up Checks

Before a rank change, reconcile the source dump and NCBI interfaces. For an authorized enrichment, verify assembly/sample/deposit provenance and the exact subject of each claim, regenerate through the seeder, and rerun schema, strict and corpus reproduction gates.

Inspect original supplementary specimen data before linking older PeJe markers to any new sample. Independently inspect raw-read/sample records and gene-level annotations before making new sequencing or pathway claims; this review did not validate sequence quality, pathway completeness or biological nutrient transfer.

## Additional Notes

`data/taxa/PATHS.tsv:14612` uniquely maps this ID to its stem; `curation/seed_scope.tsv:322380` agrees with the recorded inclusion reason/date. The inline event matches the source attestation and scope. Its 2026-09-13T17:54:04Z timestamp is the seeding provenance time, not a human-review date. `FORMA_SPECIALIS` is allowed by the species-or-below scope rule.

Baseline: branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target was reread before report creation; an ignore-independent filename search found no earlier report for this stem. Only this new report was written for this target. No YAML, inventory, generated page, prior report, lifecycle status or history entry was changed; no paid research or GitHub mutation was performed.
