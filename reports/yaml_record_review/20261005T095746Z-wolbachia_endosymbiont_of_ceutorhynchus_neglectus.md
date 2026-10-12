# YAML Record Review: Wolbachia endosymbiont of Ceutorhynchus neglectus

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_ceutorhynchus_neglectus.yaml`
- Started UTC: 2026-10-05T09:52:09Z
- Finished UTC: 2026-10-05T09:57:46Z
- Verdict: pass

## Target

Read the complete 57-line generated `TaxonRecord`, identifier `NCBITaxon:1034475`. It represents the bacterial Wolbachia taxon named for its association with Ceutorhynchus neglectus, not the host itself. The record has rank `SPECIES`, domain `BACTERIA`, grounding `EXACT`, mapping status `SEEDED`, genetic code 11, eleven lineage entries, and `strain_count: 0`.

Its single attestation is one NCBITAXON `NAME` from the 2026-09-13 snapshot. There are no listed strains, synonyms, nomenclature entries, taxonomy mappings, equivalent identifiers, literature evidence items, or causal graphs. The inline history contains the 2026-09-13T17:54:04Z `SEEDED_FROM_SOURCES` event. This review does not promote the record to `REVIEWED`.

## Validation

Both focused commands completed successfully, with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`:

```bash
just validate data/taxa/bacteria/wolbachia_endosymbiont_of_ceutorhynchus_neglectus.yaml
just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_ceutorhynchus_neglectus.yaml --out /private/tmp/w-neglectus-strict-20261005.tsv
```

The schema validator reported no issues. Strict validation scanned one file and reported zero error rows.

Not checked: full-corpus `just verify-corpus`, `just qc`, corpus tests, and generated-site drift. The repository does not expose a documented record-only reproduction gate; limiting reported differences does not restrict its scope. The source comparisons below are not a substitute for that gate.

`validate-products` is not applicable because the target contains no curator-added graph nodes. No target-specific external history record was found by ignored-inclusive filename and content searches in `history/`; consequently no focused external-history file was available to validate. The inline event was inspected. No history entry was created.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:221590` agrees with the target's identifier, exact label, rank, parent, genetic code, snapshot, and absent synonyms. All eleven root-first lineage entries agree with the pinned backbone. The source table contains no direct children of this target.

Live [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034475) was checked through taxonomy EFetch and the [NCBI Datasets taxonomy endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034475). These confirm species rank, Bacteria, genetic code 11, and parent `NCBITaxon:2640676`, unclassified Wolbachia. EFetch supplies the labeled parent chain and Datasets includes the root identifier, together corroborating the complete stored lineage. No alternate names appeared in the returned taxonomy object.

`EXACT` describes agreement with this NCBI concept. It does not establish a formally published species name, a pure culture, a unique whole-genome lineage, or equivalence to Wolbachia associated with another host. Complete local merged-ID, dropped-ID, and type-material tables contained no target rows.

The unique PATHS entry is at `data/taxa/PATHS.tsv:14056`; the unique scope row is at `curation/seed_scope.tsv:321901`. The latter's NCBI-only attestation reason agrees with the inline seed event. No identity or domain correction is indicated.

## Evidence

The NCBITAXON attestation, count of one, and `NAME` unit exactly match the backbone. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30978` independently preserves the same identifier and label within the pinned NCBI source. These are representations of the same source, not independent biological experiments.

An exact live nucleotide query, `txid1034475[Organism:noexp]`, returned six records. Complete feature and reference metadata for all six were inspected; nucleotide bases and translated protein sequences were not analyzed. Every source feature explicitly identifies taxon 1034475, host Ceutorhynchus neglectus, and location Canada: Alberta. All six coding sequences are partial and use translation table 11.

| Nucleotide accession | Length, bases | Gene or allele | Protein accession in CDS |
| --- | ---: | --- | --- |
| [HQ602874.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ602874.1) | 606 | wsp | AEI59656.1 |
| [HQ602875.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ602875.1) | 483 | coxA-6 | AEI59657.1 |
| [HQ602876.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ602876.1) | 517 | hcpA-7 | AEI59658.1 |
| [HQ602877.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ602877.1) | 522 | ftsZ-3 | AEI59659.1 |
| [HQ602878.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ602878.1) | 469 | gatB-7 | AEI59660.1 |
| [HQ602879.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ602879.1) | 499 | fbpA-8 | AEI59661.1 |

The wsp source feature explicitly names strain `Cneg-8`; the other five source features do not. The shared taxon and publication do not by themselves justify copying that strain qualifier to all five. The table records CDS annotations, not separately reviewed protein functions. These are six marker sequences, not six genomes, six culture deposits, or six independent sampling studies.

All six cite Floate, Coghlin, and Dosdall, Environmental Entomology 40(4):818-823 (August 2011), [PMID:22251682](https://pubmed.ncbi.nlm.nih.gov/22251682/), [DOI:10.1603/EN10315](https://doi.org/10.1603/EN10315). PubMed bibliographic metadata and the complete abstract were inspected. PubMed's 2012 indexing date is not the publication year.

The abstract concerns Wolbachia in Ceutorhynchus obstrictus. Its population comparisons and possible multiple infections cannot be transferred to C. neglectus. The explicit C. neglectus association above comes from the inspected sequence source features. The publisher full text could not be retrieved through the available web fetch; therefore this review does not claim to have checked its comparator sampling or tables. Later search-result leads concerning shared marker types were not used as evidence of strain or genome equivalence.

## Completeness

Complete local BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventory tables contained no rows for this taxon. Under the schema, `strain_count` counts classified BacDive records, not every biological strain known from sequence submissions. Zero is therefore consistent with the inventory despite the sequence-level Cneg-8 designation.

Additional searches used `rg --no-ignore --hidden -n -z -i`, including compressed catalogs, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Search terms covered the bounded taxon number, full bacterial name, record stem, host name, HQ602874-HQ602879, wCneg, Cneg-8, and AEI59656-AEI59661. `SOURCE.json` provenance metadata files were excluded. Only the backbone, scope row, and native NCBI scientific-name object matched the target and host terms. No marker accession, protein accession, wCneg, or Cneg-8 hits were found in those searched inventories and catalogs. Ignored and hidden files were included; this is a bounded local-source result, not worldwide absence.

The exact live Assembly query returned zero IDs with `phrasesnotfound` and `No items found` diagnostics. Those diagnostics are retained as a query limitation, not proof that no relevant assembly could exist under another taxon. None of the six inspected nucleotide objects supplied a culture deposit, BioSample, BioProject, or assembly accession establishing a missing eligible strain-to-genome link.

No consequential missing required representation was established. Optional literature, phenotype, nomenclature, mapping, and graph fields need not be invented for this NCBI seed. iModulonDB is not applicable to the claims in this record; discovery of marker annotations does not create a transcriptomic assertion requiring it.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checks performed. Current NCBI identity, pinned source fields, attestation semantics, scope inclusion, and the zero BacDive count are consistent. Full-corpus reproducibility and uninspected paper full text remain explicit limits, not findings against assertions the YAML does not make.

## Recommended Edits

None required. Do not hand-edit the generated YAML, add a genome from these marker accessions, transfer results from C. obstrictus, or promote the lifecycle status from this report.

If new evidence later warrants a change, inventory extraction belongs upstream or in `scripts/extract_source_inventory.py` and `src/taxonmech/extract.py`; transformation behavior belongs in `scripts/seed_from_sources.py` and its supporting code; inclusion belongs in `curation/seed_scope.tsv`. Any proposed literature enrichment needs an explicitly maintained input and source-scoped representation rather than a patch to generated output. No such change is requested by this review.

## Follow-up Checks

None required to resolve a finding. A future enrichment should inspect the primary paper's full text for its exact C. neglectus sampling context and independently verify any new deposit or assembly link. Preserve marker, protein, sample, strain, and genome identities separately.

After any authorized upstream correction, use the repository's canary-first generation workflow, rerun the focused schema and strict validators, and run full `just verify-corpus` and applicable corpus gates. These steps were not run as part of this read-only review.

## Additional Notes

This review writes only this timestamped report. It does not change YAML, source inventories, scope, code, pages, prior reports, curation history, or status. No paid research, outbound contact, or GitHub mutation was performed. No eukaryotic host record was assumed to exist or reviewed; the completed Eukaryota coverage was left untouched.
