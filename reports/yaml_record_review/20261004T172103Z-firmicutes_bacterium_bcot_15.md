# YAML Record Review: Firmicutes bacterium BCOT-15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/firmicutes_bacterium_bcot_15.yaml`
- Started UTC: 2026-10-04T17:19:32Z
- Finished UTC: 2026-10-04T17:21:03Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read. NCBITaxon:1033674 denotes the species-ranked placeholder Firmicutes bacterium BCOT-15 in BACTERIA. It carries `EXACT` grounding, `SEEDED` mapping status, genetic code 11, zero inventoried BacDive strains, one NCBITAXON NAME attestation and a seed event dated 2026-09-13T17:54:04Z. Species rank does not establish valid nomenclatural publication.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/firmicutes_bacterium_bcot_15.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/firmicutes_bacterium_bcot_15.yaml`: passed, one file and zero errors.
- Ignored-inclusive exact-identifier search across `data/taxa`: only this YAML. Exact ignored-inclusive report search found no prior report for the stem.
- Structured comparison of the backbone, complete lineage, children, seven inventories, PATHS, scope, attestation and embedded seed text passed. Type-material, merged-ID and dropped inventories were checked separately.
- Not run: full-corpus `just qc`, `just verify-corpus`, tests, provenance, render and documentation checks. Global term/reference and history validation were skipped; no curator-added graph term, literature citation or separate history artifact is asserted here. Strict validation checked embedded history shape. Bounded source comparisons are not corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221284`, the complete native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30592`, `data/taxa/PATHS.tsv:13737` and `curation/seed_scope.tsv:321636` consistently resolve the identifier, label, slug and scope. The latter records the 2026-09-13 attested-rule inclusion.

The inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1033674&lvl=3&mode=node), [taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033674&retmode=xml) and [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033674) agree on species rank, canonical name, parent 84086 and genetic code 11. The complete root-first chain matches: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Bacillota 1239 (PHYLUM), unclassified Bacillota 84086 (NO_RANK). Datasets explicitly supplies root 1. No live alternate name was returned.

The canonical name still uses Firmicutes while its lineage uses Bacillota. Both are verbatim NCBI fields, not an internal inconsistency to repair by renaming or inferring finer placement.

## Evidence

The single NCBITAXON attestation agrees with the 2026-09-13 source row and correctly counts a NAME. No exact rows were found in BacDive, LPSN, GTDB mappings, GOLD, MediaDive, Madin or BactoTraits inventories. There are no child taxa, so the zero BacDive count is not hiding descendant entries. Type-material, merged-ID and dropped inventories had no exact target rows.

Exact-taxid NCBI searches returned zero Assembly hits with no-items/phrase warnings and one Nuccore hit. [HQ616513.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616513.1), UID 333408593, is a 584-base partial 16S sequence. Source qualifiers explicitly identify BCOT-15, taxon 1033674, genomic DNA, Mexico, collection on 2010-02-01 by R. Flores-Magallon, and PCR primers. They do not supply a culture-collection deposit or an isolation-source qualifier. A marker is not a genome assembly.

Both sequence references were inspected: an unpublished study of artisanal Cotija cheese and a direct submission on 2010-11-10 by Flores-Magallon, Oliva-Hernandez and Narvaez-Zapata from Instituto Politecnico Nacional, Reynosa. The inspected publisher page for [DOI 10.1007/s10068-011-0137-z](https://link.springer.com/article/10.1007/s10068-011-0137-z) confirms a 2011 Cotija study by those authors, but its accessible abstract does not identify BCOT-15 or HQ616513. Full text was subscription-only and ResearchGate offered no full text. Author/topic agreement alone does not establish the target's experimental phenotype or a published strain identity.

An institutional thesis was a search lead for this label. Its [IPN PDF URL](https://tesis.ipn.mx/bitstream/handle/123456789/12233/BARRERA%20CHAVEZ%20HUGO%20-%20B081033.pdf?isAllowed=y&sequence=1) failed web retrieval and returned HTTP 404 through a direct request. Neither the indexed snippet nor a third-party preview was treated as inspected thesis evidence. No thesis sequence alignment or figure/table audit was performed.

The complete native GTDB object at `data/catalog/gtdb_genomes-0015.jsonl.gz:39840` is RS_GCF_019037205.1 / GCA_019037205.1, Bacillus subtilis taxon 1423, strain 179-J 10A2 HS, BioSample SAMN19102939. It matches only because its contig N50 is 1033674. Its cleanroom-floor source and 3,995,942-base genome do not link it to BCOT-15.

`data/catalog/allthebacteria.tsv.xz:65034` is another numeric collision: SAMEA1033674, ERR064770, ERZ3069107, scientifically labelled Streptococcus pneumoniae with both Sylph classifications agreeing. Assembly/FASTA and quality flags are available/PASS, with prior HQ T. Eligibility is not a strain association: no source chain connects this BioSample to BCOT-15. The sample suffix is not a taxid. Its batch-600 archive, mutable AWS URL and SeqKit sum remain source context, not inferred target genome evidence.

## Completeness

The ignored-inclusive compressed search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`; structured SOURCE.json searches supplemented it. The query included bounded taxid, BCOT-15 spacing/separator variants and label/slug forms. Five lines matched: backbone, scope, native name and the two unrelated numeric collisions. No matching manifest evidence was found within those roots.

No required representation is missing from the inspected source inventories. Optional evidence, nomenclature, mappings, strains, datasets, discussions and causal graphs are appropriately absent. `strain_count: 0` is an inventory count, not a claim that BCOT-15 was never cultivated. The exact-taxid Assembly result is bounded and does not prove global genome absence under other identifiers.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The unavailable primary thesis and article body limit optional literature enrichment, not verification of the currently asserted seeded fields.

## Recommended Edits

None required. If future literature or deposit evidence supports enrichment, maintain the configured upstream source and `scripts/extract_source_inventory.py`, or a tested rule in `src/taxonmech/seed.py`. Do not hand-edit generated YAML, fabricate a deposit, recast marker sequences as genomes, or change NCBI lineage using a cheese-study label.

## Follow-up Checks

Before adding literature claims, obtain inspected primary text explicitly linking BCOT-15 or HQ616513 to the claimed result. Future source changes require a seed dry-run, one-record canary, emitted-file inspection, open/strict validation and full reproduction/QC. No seed mutation was run in this review.

## Additional Notes

iModulonDB was not applicable because the record asserts no gene, regulator, pathway or expression module. No paid access, author contact, GitHub operation, status promotion or history write occurred. The current branch was retained; only this new report was written for the target. Eukaryota was not revisited.
