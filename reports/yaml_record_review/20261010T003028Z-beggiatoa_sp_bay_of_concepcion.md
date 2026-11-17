# YAML Record Review: Beggiatoa sp. 'Bay of Concepcion'

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/beggiatoa_sp_bay_of_concepcion.yaml`
- Started UTC: 2026-10-10T00:28:38Z
- Finished UTC: 2026-10-10T00:30:28Z
- Verdict: pass

## Target

The entire 58-line generated `TaxonRecord` was read. `NCBITaxon:1037353` denotes Beggiatoa sp. 'Bay of Concepcion', rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:70273` (Candidatus Marithioploca araucensis), genetic code 11, grounding `EXACT`, status `SEEDED`.

It contains ten ancestors, one exact NCBI synonym, zero inventoried BacDive strains, one NCBITAXON name attestation and a seed event. This is the BC population, not either California canyon strain or the whole parent species.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/beggiatoa_sp_bay_of_concepcion.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/beggiatoa_sp_bay_of_concepcion.yaml --out /private/tmp/taxonmech-concepcion-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured scans matched pinned identity, full lineage, synonym, genetic code, own attestation, scope/index rows and seed-event text. Complete backbone scanning found no direct child; exact own-ID type-material, merged-ID and dropped scans found none.
- Own native NCBI name rows and live taxonomy API responses were read completely. Primary marker metadata and the complete relevant PubMed abstract/bibliographic identifiers were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Bounded source agreement does not prove corpus reproduction. No causal graph is asserted, so `just validate-products` has no applicable nodes.
- The complete experimental paper, independent phylogenetic reconstruction, genome comparison and exhaustive external sequence census were not audited. Search snippets supplied leads, not experimental proof.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222720` agrees with [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037353&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037353): exact scientific name, strain rank, parent 70273 and code 11.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Thiotrichales, Thiotrichaceae, Candidatus Marithioploca and Candidatus Marithioploca araucensis. Every stored ID, label and rank matches the pinned backbone; EFetch confirms the chain below root and Datasets includes root 1.

`data/catalog/ncbi_names-0005.jsonl.gz:32333` is the scientific-name row. Row 32334 and live EFetch explicitly retain Candidatus Marithioploca araucae (BC) as a synonym. Preserve the source's historical `araucae` spelling rather than silently replacing the synonym with the parent's current `araucensis` spelling.

The Beggiatoa label does not contradict the authority's Marithioploca placement: both describe the same NCBI concept. Exact grounding is not a claim of formally validated nomenclature or equivalence to every strain of the parent species.

## Evidence

The sole NCBITAXON attestation has exact own ID/label, count 1, unit `NAME`, snapshot 2026-09-13. This counts a source assertion, not a culture deposit or genome.

[AF035956 primary metadata](https://www.ncbi.nlm.nih.gov/nuccore/AF035956) explicitly names Beggiatoa sp. 'Bay of Concepcion', strain Bay of Concepcion, `taxon:1037353`, and a note locating the population in Chile. AF035956.1 is 1,457 bases and is described as a near-complete 16S rRNA sequence; its feature endpoints are partial. It is not a genome assembly or culture-collection accession and is not presently an asserted YAML link.

The marker retains a 1997 direct submission and an unpublished reference titled Phylogenetic position of a large marine Beggiatoa. This metadata is not proof that related research remained unpublished. The separately verified [Teske et al. 1999 paper, PMID 10188277](https://pubmed.ncbi.nlm.nih.gov/10188277/), DOI 10.1016/S0723-2020(99)80026-5, discusses the close relationship between the large Bay of Concepcion population and Thioploca araucae, and limitations of sheath-based generic distinctions. Its abstract provides historical context, not independent proof of every current taxonomic rank or a new phenotype claim. No full-paper sequence/accession audit is claimed.

The YAML itself asserts taxonomy and inventory provenance, not nitrate accumulation, sulfur metabolism, gene function or habitat mechanisms. Neither a phylogenetic neighbor nor later comparative reuse of the marker supplies a strain/genome equivalence.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1037353, Beggiatoa/Concepcion label context with an accented spelling alternative, the exact BC synonym and the slug. Its four matching lines were the own backbone row, two native name rows and scope row; all were inspected.

A follow-up ignored/compressed-inclusive AF035956 search over the same roots found no matches. Five SOURCE.json files were parsed separately without a target match. Gitignore-independent filename enumeration under the taxon corpus and review directory found the single target YAML and no prior report. History filename inspection found no target-specific filename. These bounded checks do not claim that no external sequence or publication exists.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. There is no direct backbone child to supply descendant strains. Thus `strain_count: 0` correctly counts inventoried BacDive entries, not the existence of this environmental population in research. No repository-supported deposit/genome identity chain was established.

Optional definition, record-level evidence, nomenclature, mappings and causal graphs need not be invented. iModulonDB was not applicable: the YAML asserts no gene, regulator, expression module, pathway or transcriptomics result. Marker-literature context does not introduce such claims; no adapter execution or dataset-absence assertion is made.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, strain rank, lineage, exact synonym, source count, provenance and seed status are supported. Skipped corpus checks and the uninspected full experimental paper remain limitations.

## Recommended Edits

None required. Preserve the BC synonym verbatim and the current authority lineage. Do not change the parent to Maribeggiatoa merely because the California records share the older generic label, infer a genome from AF035956, or invent a deposit from an environmental strain designation.

Any future authorized correction belongs in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect warrants such a change here; generated YAML must not be hand-edited.

## Follow-up Checks

Future biological or genomic enrichment requires population-specific primary evidence and an explicit identity chain. Retrieve the full experimental paper before relying on detailed methods, accession comparisons or phenotype results beyond the inspected abstract.

After an authorized source refresh, rerun schema/strict/history validation and the documented full-corpus reproduction/QC gates. A marker check alone does not replace those gates.

## Additional Notes

- YAML SHA-256: `8949f4c4ff23394ebe8070ef7f42523302b57d3e3ea594267c70bc00ee4f50a9`.
- `data/taxa/PATHS.tsv:15267` and `curation/seed_scope.tsv:322946` uniquely identify the target. The seed retains 2026-09-13T17:54:04Z and the exact one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, worktree, branch or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
