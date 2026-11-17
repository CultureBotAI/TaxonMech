# YAML Record Review: Wolbachia endosymbiont of Ceutorhynchus subpubescens

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_ceutorhynchus_subpubescens.yaml`
- Started UTC: 2026-10-05T10:00:23Z
- Finished UTC: 2026-10-05T10:02:41Z
- Verdict: pass

## Target

Read the entire 57-line generated `TaxonRecord`, identifier `NCBITaxon:1034476`. This is the bacterial Wolbachia concept named for its association with Ceutorhynchus subpubescens, not the host taxon. It carries `SPECIES` rank, `BACTERIA` domain, `EXACT` grounding, `SEEDED` lifecycle status, genetic code 11, eleven lineage entries, and `strain_count: 0`.

The only source attestation is one NCBITAXON `NAME` from the 2026-09-13 snapshot. No strains, synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence, or causal graphs are listed. The inline seed event is dated 2026-09-13T17:54:04Z. This review does not change that event or promote the lifecycle status.

## Validation

Both focused commands passed with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`:

```bash
just validate data/taxa/bacteria/wolbachia_endosymbiont_of_ceutorhynchus_subpubescens.yaml
just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_ceutorhynchus_subpubescens.yaml --out /private/tmp/w-subpubescens-strict-20261005.tsv
```

Schema validation reported no issues. Strict validation scanned one file with zero errors.

Not checked: full `just verify-corpus`, `just qc`, corpus tests, and generated-site drift. No documented record-only reproduction gate exists; `--max-diffs` limits diagnostics rather than corpus scope. The bounded source comparisons below do not prove full reproduction.

`validate-products` is not applicable because no curator-added graph nodes occur. Ignored-inclusive filename and content searches found no target-specific external history record in `history/`, so no focused external-history file was available to validate. The inline event was inspected, and no new history entry was created.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:221591` agrees with the record's identifier, label, rank, parent, genetic code, absent synonyms, and snapshot. All eleven root-first lineage entries agree with the pinned backbone. The table contains no direct children of this target.

Live [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034476) was inspected through taxonomy EFetch and the [Datasets taxonomy endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034476). They confirm the exact target name, species rank, bacterial placement, parent `NCBITaxon:2640676` (unclassified Wolbachia), and lineage identifiers. EFetch confirms the labeled ancestors and genetic code 11; Datasets includes the root identifier. No alternate name appeared in the returned taxonomy object.

The complete local merged-ID, dropped-ID, and type-material tables contained no target rows. `EXACT` is agreement with an NCBI concept, not a claim of formally published nomenclature, a pure culture, or genomic equivalence to another host-associated Wolbachia.

The unique PATHS entry is `data/taxa/PATHS.tsv:14057`; the unique scope row is `curation/seed_scope.tsv:321902`. Its NCBI-only attestation reason agrees with the inline `SEEDED_FROM_SOURCES` event. No identity, lineage, rank, or scope error was established.

## Evidence

The source attestation's identifier, label, count of one, and `NAME` unit agree with the backbone. The complete native object at `data/catalog/ncbi_names-0005.jsonl.gz:30979` preserves the same scientific name and taxon identifier. This is another representation of the pinned NCBI source, not an independent experiment.

The exact live nucleotide query `txid1034476[Organism:noexp]` returned one sequence, [HQ602873.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ602873.1). Its complete feature and reference metadata were inspected, without analyzing nucleotide bases or translated sequence. It is a 568-base partial wsp coding sequence, annotated as an outer surface protein, with both coding ends partial, translation table 11, and CDS protein identifier AEI59655.1. The source feature explicitly names strain Csub-2, host Ceutorhynchus subpubescens, location Canada: Alberta, and `taxon:1034476`. It was submitted on 2010-11-05, released on 2011-06-26, and last updated on 2016-07-25. This is gene-marker evidence, not a genome assembly or a culture-deposit identity.

The sequence cites Floate, Coghlin, and Dosdall, Environmental Entomology 40(4):818-823 (August 2011), [PMID:22251682](https://pubmed.ncbi.nlm.nih.gov/22251682/), [DOI:10.1603/EN10315](https://doi.org/10.1603/EN10315). PubMed bibliography and the complete abstract were inspected. The abstract describes Wolbachia population comparisons in Ceutorhynchus obstrictus, not C. subpubescens. Neither its population findings nor its possible multiple infections are transferred to this target. The target-specific host association comes from the inspected sequence source feature. Publisher full-text retrieval failed, so the original paper's comparator sampling and tables were not checked. PubMed's 2012 indexing date is not the publication year.

A later primary paper, [PMCID:PMC5371936](https://pmc.ncbi.nlm.nih.gov/articles/PMC5371936/), PMID:28085049, DOI:10.3390/insects8010008, was inspected through its abstract, relevant methods and results text, and Table A1. Europe PMC full-text XML supplied the table after a subsequent PMC HTML request encountered a browser check. Table A1 associates C. subpubescens with HQ602873 and supergroup A; section 2.3.1 establishes that it was a reference marker for a study of Hypothenemus hampei. This documents reuse of the marker, not a new experiment on this target or an independently established whole-genome classification. The coffee-borer reproduction and antibiotic-treatment results do not support a phenotype or causal graph for this record. No figure topology or phylogenetic analysis was independently re-evaluated.

## Completeness

Complete local BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventory tables contained no target rows. The schema defines `strain_count` as classified BacDive records, not all named biological strains. Zero is consistent with these inputs despite the explicit Csub-2 sequence qualifier.

Additional searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. These included ignored, hidden, and compressed files, excluding `SOURCE.json` provenance metadata. Terms covered the bounded taxon number, full bacterial name, record stem, host name, HQ602873, Csub-2, and AEI59655. The target and host terms matched only the backbone, scope row, and native scientific-name object. The accession and strain-alias search completed with no matches. These are bounded local-source results, not claims of worldwide absence.

The exact Assembly query returned zero IDs, with `phrasesnotfound` and `No items found` diagnostics. This does not exclude relevant assemblies classified elsewhere. The inspected nucleotide object contains no deposit, BioSample, BioProject, or assembly accession establishing a missing eligible strain-to-genome relationship.

No missing required representation was established. Literature evidence, nomenclature, mappings, and graphs are optional for this NCBI seed. A single reference marker and a later table's supergroup annotation do not require altering the carried NCBI lineage. iModulonDB is not applicable to this record's claims; a discovered marker annotation is not a transcriptomic claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checks performed. Identity, lineage, source attestation, BacDive count, scope, and seed-event provenance are consistent. The incomplete original-paper full-text check and skipped corpus gates remain explicit limits, not evidence of an error in the YAML.

## Recommended Edits

None required. Do not hand-edit the generated record, treat HQ602873.1 as a genome, copy other hosts' experimental results, or promote the record to `REVIEWED` from this report.

Future source corrections belong upstream or in `scripts/extract_source_inventory.py` and `src/taxonmech/extract.py`; transformation corrections belong in `scripts/seed_from_sources.py` and supporting code; scope changes belong in `curation/seed_scope.tsv`. Any literature enrichment needs an explicitly maintained input and narrowly supported assertions, not direct edits to generated YAML.

## Follow-up Checks

None required to resolve a finding. Before optional enrichment, inspect the original paper's full text for its C. subpubescens sampling context and independently verify any proposed deposit or assembly chain. Marker similarity and reference-table co-occurrence must remain separate from strain and genome identity.

After any authorized upstream change, use canary-first generation, rerun focused schema and strict validation, and run full `just verify-corpus` and applicable corpus gates. Those generation and full-corpus steps were not performed here.

## Additional Notes

Only this new timestamped report is written. YAML, inventories, scope, code, pages, earlier reports, history, and lifecycle status remain unchanged. No paid research, outbound contact, or GitHub mutation occurred. Eukaryota reviews were left untouched; no host record was assumed to exist or reviewed.
