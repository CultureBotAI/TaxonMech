# YAML Record Review: Firmicutes bacterium BCOT-6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/firmicutes_bacterium_bcot_6.yaml`
- Started UTC: 2026-10-04T17:23:41Z
- Finished UTC: 2026-10-04T17:24:39Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was inspected for NCBITaxon:1033676, Firmicutes bacterium BCOT-6. It is a species-ranked BACTERIA placeholder, not a formally named species or one of the other BCOT isolates. The record has `EXACT` grounding, `SEEDED` mapping status, code 11, zero BacDive strains, one NCBITAXON NAME attestation and a seed event dated 2026-09-13T17:54:04Z. This review did not change any generated field.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/firmicutes_bacterium_bcot_6.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/firmicutes_bacterium_bcot_6.yaml`: passed, one file and zero errors.
- Ignored-inclusive exact-identifier search across `data/taxa` returned only the target; an ignored-inclusive report-filename search found no prior report for this stem.
- Structured checks matched the target backbone, complete lineage, child scan, seven source inventories, PATHS, scope, NCBI attestation and embedded seed text. Exact type-material, merged-ID and dropped-row scans also completed.
- Not run: full-corpus `just qc`, `just verify-corpus`, tests, provenance, documentation and render gates. Global term/reference and history validation were skipped; this YAML asserts no curator-added graph terms or literature references, and no separate history record was created. Strict validation covered embedded history shape. Focused comparisons do not substitute for corpus reproduction.

## Identity and Grounding

The target row is `data/raw/ncbitaxon_taxa.tsv:221286`; the complete native name object is `data/catalog/ncbi_names-0005.jsonl.gz:30594`. Both agree with the YAML. `data/taxa/PATHS.tsv:13739` pins the slug and `curation/seed_scope.tsv:321638` records the 2026-09-13 attested-rule inclusion.

Inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1033676&lvl=3&mode=node), [taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033676&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033676) responses agree on canonical name, species rank, parent 84086 and code 11. No live alternate name was returned. The complete root-first lineage is root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Bacillota 1239 (PHYLUM), unclassified Bacillota 84086 (NO_RANK). Datasets explicitly includes root 1.

The canonical label's Firmicutes wording and lineage's Bacillota wording are both current source fields. They should not be harmonized by a local rename. The record's rank does not establish nomenclatural validity, and the lineage does not imply a genus-level identification.

## Evidence

The NCBI source attestation correctly counts one NAME from snapshot 2026-09-13. Exact source scans returned no BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits rows and no child taxa. Type-material, merged-ID and dropped inventories had no target row. Thus zero strains is the supported BacDive inventory count, not evidence that BCOT-6 was never cultured.

The exact-taxid Assembly search returned zero hits, with no-items/phrase warnings. Nuccore returned one record, [HQ616504.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616504.1), UID 333408584. The inspected GenBank XML describes a 689-base partial 16S sequence, with genomic-DNA source qualifiers explicitly naming BCOT-6 and taxon 1033676. It records Mexico, collection on 2010-02-01 by R. Flores-Magallon, and PCR primers. It does not supply an isolation-source qualifier or a culture-collection deposit. This marker does not establish a genome link.

Both sequence references were inspected. They identify an unpublished Cotija-cheese study and a direct submission on 2010-11-10 by Flores-Magallon, Oliva-Hernandez and Narvaez-Zapata, Instituto Politecnico Nacional, Reynosa. [DOI 10.1007/s10068-011-0137-z](https://link.springer.com/article/10.1007/s10068-011-0137-z) was inspected at its publisher during the earlier BCOT-15 review in this same session: its 2011 metadata and abstract match the authors and broad study context, but the accessible text does not name BCOT-6 or HQ616504. Full text was not accessible. No isolate-specific phenotype, maturation stage or finer identification is inferred from the shared context or from the unretrieved thesis lead.

The non-target local hit at `data/catalog/allthebacteria.tsv.xz:65036` is SAMEA1033676, ERR068079, ERZ3069113. Scientific and both Sylph names are Streptococcus pneumoniae. Available FASTA, assembly PASS, Sylph PASS, HQ PASS and prior HQ T are retained accurately; they do not establish identity. The digits occur in a BioSample and download URL, not an NCBI taxon field. No source chain associates this sample with BCOT-6. The row's SeqKit sum, batch-600 OSF archive and mutable AWS URL therefore do not supply target genome evidence.

## Completeness

The completed ignored-inclusive compressed search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded taxid, BCOT-6 separator variants and label/slug forms. Four lines matched: the target backbone, scope, native name and unrelated ATB row. A structured SOURCE.json scan found no matching manifest evidence in those source roots.

No missing required representation was found. Optional strains, nomenclature, mappings, evidence, datasets, discussions and causal graphs may remain empty. This bounded review found no supported genome relationship; the exact-taxid search does not prove there are no sequences elsewhere under another identifier. A common collection date, author list or BCOT prefix does not merge separate isolates.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's asserted fields. Optional literature enrichment remains limited by unavailable primary full text.

## Recommended Edits

None required. Any future supported enrichment belongs in the configured upstream source, `scripts/extract_source_inventory.py`, or a tested `src/taxonmech/seed.py` rule. Do not hand-edit generated YAML, invent a BacDive ID or culture deposit, add the unrelated BioSample, or reclassify this taxon using a study-level description.

## Follow-up Checks

Before importing optional literature, inspect source text explicitly linking BCOT-6 or HQ616504 to the claimed identity or observation. For later source changes, use the seed dry-run and one-record canary, inspect the generated result, and rerun open/strict validation followed by full reproduction/QC. No seed command or history mutation was performed here.

## Additional Notes

iModulonDB was not applicable because no gene, locus, regulator, pathway or expression-module claim is asserted. No paid research, author contact, GitHub mutation or lifecycle promotion occurred. Only the new review report was written for this target; Eukaryota was left untouched.
