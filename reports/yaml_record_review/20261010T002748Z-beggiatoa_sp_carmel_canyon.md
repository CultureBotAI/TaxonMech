# YAML Record Review: Beggiatoa sp. 'Carmel Canyon'

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/beggiatoa_sp_carmel_canyon.yaml`
- Started UTC: 2026-10-10T00:25:33Z
- Finished UTC: 2026-10-10T00:27:48Z
- Verdict: pass

## Target

The full 58-line generated `TaxonRecord` was read. `NCBITaxon:1037351` denotes Beggiatoa sp. 'Carmel Canyon', rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:76865` (Candidatus Maribeggiatoa vulgaris), genetic code 11, grounding `EXACT`, status `SEEDED`.

The record carries ten ancestors, one exact NCBI synonym, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. It is distinct from the Monterey Canyon strain, the parent species and the White Point filamentous bacterium.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/beggiatoa_sp_carmel_canyon.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/beggiatoa_sp_carmel_canyon.yaml --out /private/tmp/taxonmech-carmel-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Complete structured source scans matched the target, all ancestors, synonym, code, own attestation, PATHS/scope entries and seed explanation. The full backbone has no immediate child; exact own-ID type-material, merged-ID and dropped scans found none.
- Every native candidate row from the bounded identity search was read in full. Live taxonomy API responses and primary marker metadata were inspected completely. Relevant primary-paper methods, accession and results paragraphs were read, including a focused reread of the locality and sample distinctions.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused comparison is not corpus reproduction. No causal graph nodes are asserted, so `just validate-products` has no applicable target.
- No independent genome analysis, experimental replication, exhaustive external sequence census or formal nomenclature reconciliation was performed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222719` agrees with [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037351&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037351): Beggiatoa sp. 'Carmel Canyon', strain rank, parent 76865 and code 11.

The stored root-first chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Thiotrichales, Thiotrichaceae, Candidatus Maribeggiatoa and Candidatus Maribeggiatoa vulgaris. All identifiers, labels and ranks match the pinned backbone. EFetch confirms the chain below root and Datasets includes root 1.

`data/catalog/ncbi_names-0005.jsonl.gz:32331` is the scientific-name row; row 32332 classifies Candidatus Maribeggiatoa vulgaris (CC) as a synonym. The older generic scientific name and current Maribeggiatoa placement both belong to this authority concept. Exact grounding does not assert formal nomenclatural validity, identity with Monterey Canyon or equivalence to every population of the parent species.

## Evidence

The only asserted source is NCBITAXON: exact own ID and label, one `NAME`, snapshot 2026-09-13. Its count is neither a cultured-deposit count nor a genome count.

[AY580013 primary sequence metadata](https://www.ncbi.nlm.nih.gov/nuccore/AY580013) explicitly names Beggiatoa sp. 'Carmel Canyon', isolate Carmel Canyon and `taxon:1037351`. AY580013.1 is a 1,463-base partial 16S rRNA marker with partial feature endpoints, not a genome assembly or culture-collection accession. Its bibliography identifies Kalanetra, Huston and Nelson (2004), PMID 15574952, DOI 10.1128/AEM.70.12.7487-7496.2004.

The inspected [primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC535177/) describes Carmel Canyon sampling at about 900 m and explicitly assigns AY580013 to that sample, separately from White Point accession AY496953. It reports nitrate detected in Carmel Canyon preparations, unlike the White Point preparations. The title's absence-of-nitrate result must not be transferred to the Carmel Canyon control.

There is an unresolved external metadata conflict: AY580013's source qualifiers say intertidal hydrothermal vent and USA:California, White Point, whereas the publication's Carmel Canyon collection and accession assignment describe the deep-water sample. The explicit organism/taxon link supports marker identity, but the locality qualifiers are not silently accepted as Carmel Canyon habitat evidence. This conflict is supplementary review context: neither marker nor habitat qualifier is an asserted YAML field. No unsupported nitrate, vacuole mechanism or habitat claim is present in the record.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It used bounded 1037351, Beggiatoa/Carmel label context, the CC synonym and the slug. Seven matching lines comprised the own backbone/scope/name rows and three unrelated native records:

- BV-BRC `492670.2084` and GenBank `GCA_033808435.1` describe Bacillus velezensis AYGS-17, taxon 492670. They match BioProject `PRJNA1037351`, not the target taxon.
- GTDB `RS_GCF_023703335.1` describes Bacillus stercoris PSM7, taxon 2054641. Its contig N50 is 1037351, a statistic rather than an identifier.

All matching native rows were inspected completely. A follow-up search for AY580013 over the same roots returned no matches, including ignored/compressed files. Five SOURCE.json files were separately parsed with no target match. Gitignore-independent filename enumeration under the taxon corpus and review directory found only the target YAML and no prior report; history filename inspection found no target-specific filename. These are bounded repository results, not a claim that no other external marker, genome or publication exists.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. With no child in the backbone, there is no descendant inventory to aggregate. Zero correctly describes inventoried BacDive strains, not whether the environmental population was studied.

Optional biological definition, record-level evidence, nomenclature, taxonomy mappings and causal graphs need not be invented. No eligible repository deposit/genome identity chain was established. iModulonDB was not applicable to the YAML's taxonomy-only claims: the marker and contextual physiological study do not create gene/regulator/transcriptomics assertions. No adapter execution or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the present record's identity, lineage, synonym, provenance, count semantics or seeded status. The external sequence-locality disagreement remains explicitly unresolved above; it is not a defect in an unasserted YAML field. Skipped full-corpus checks remain limitations.

## Recommended Edits

None required to the current record. Preserve the strain rank, exact CC synonym, separate Carmel/Monterey identities and zero BacDive inventory count. Do not import the unrelated Bacillus genomes or turn a 16S marker into a genome.

Before future habitat enrichment, resolve or explicitly retain the AY580013 source-qualifier conflict against the original submission/publication evidence. A source correction belongs with the source authority and maintained harmonization inputs, not a hand edit to generated YAML. Any authorized TaxonMech change belongs in `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding.

## Follow-up Checks

Future biological claims must retain the paper's sample-specific distinctions; its negative White Point nitrate result is not a Carmel Canyon result. Marker or genome additions require an explicit source-supported identity chain, and locality evidence must preserve the unresolved conflict until reconciled.

After any authorized source refresh, rerun schema/strict/history validation and the documented full-corpus reproduction/QC gates. Focused source matching alone does not prove reproducibility.

## Additional Notes

- YAML SHA-256: `b19d3d4d954fe30dd3e2f9b8885179962cef14d35bb9749b66af34bffc47925f`.
- `data/taxa/PATHS.tsv:15266` and `curation/seed_scope.tsv:322945` uniquely resolve the target. The seed event retains 2026-09-13T17:54:04Z and the exact one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, worktree, branch or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
