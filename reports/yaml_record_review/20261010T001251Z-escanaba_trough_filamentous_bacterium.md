# YAML Record Review: Escanaba Trough filamentous bacterium

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/escanaba_trough_filamentous_bacterium.yaml`
- Started UTC: 2026-10-10T00:11:20Z
- Finished UTC: 2026-10-10T00:12:51Z
- Verdict: pass

## Target

The entire 58-line generated `TaxonRecord` was read. `NCBITaxon:1037348` denotes Escanaba Trough filamentous bacterium, rank `ISOLATE`, domain `BACTERIA`, parent `NCBITaxon:991901` (Candidatus Marithrix sessilis), genetic code 11, grounding `EXACT`, status `SEEDED`.

The record contains ten ancestors, the ET-qualified exact synonym, zero BacDive strains, one NCBITAXON name attestation and the seed event. It is not the parent species, the JdF isolate or the WP isolate.

## Validation

Repository commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/escanaba_trough_filamentous_bacterium.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/escanaba_trough_filamentous_bacterium.yaml --out /private/tmp/taxonmech-escanaba-trough-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: run earlier in this same review turn, 17 valid records and zero invalid links. History/schema/guidance were subsequently checked for tracked changes; none were present.
- Structured scans matched identity, complete pinned lineage, synonym, genetic code, own source attestation, scope/index entries and seed text. A complete backbone scan found no child; exact own-ID scans found no type-material, merge or drop row.
- All 13 ignored-inclusive source-search candidates were read in full. Live NCBI EFetch and Datasets independently verified the taxon; primary marker metadata verified its separate accession.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused inventory agreement is not full-corpus reproducibility. `just validate-products` has no applicable causal-graph nodes.
- NCBI browser retrieval failed; direct taxonomy APIs succeeded. The public paper page did not provide usable text through the browser tool, and PMC access had presented a challenge earlier this turn. The complete PubMed abstract and bibliography were inspected through EFetch. No full-paper experimental review or genome-sequence comparison is claimed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222716` agrees with [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037348&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037348): isolate 1037348, label Escanaba Trough filamentous bacterium, parent 991901 and code 11.

The complete root-first chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Thiotrichales, Thiotrichaceae, Candidatus Marithrix and Candidatus Marithrix sessilis. The pinned identifiers, labels and ranks match the YAML. Live EFetch confirms the chain below root and Datasets includes root ID 1.

`data/catalog/ncbi_names-0005.jsonl.gz:32325` supplies Candidatus Marithrix sessilis (ET) as an NCBI synonym; row 32326 supplies the scientific name. Its ET qualifier is essential to the exact synonym's scope. The parent species and siblings have distinct IDs and name rows: 991901, Juan de Fuca/1037347 and White Point/1037349. Their identities were not substituted for this isolate.

## Evidence

The only attestation is NCBITAXON, source ID 1037348, count 1 `NAME`, snapshot 2026-09-13. Its label and note match the backbone. A name attestation does not assert cultivation, genome availability or a phenotype.

Live [AY883934 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AY883934) identifies AY883934.1, a 1,461-base partial 16S sequence, with explicit organism Escanaba Trough filamentous bacterium and `taxon:1037348`. Its source qualifier identifies Escanaba Trough along the Gorda Ridge. This is independent identity context, not an assembly and not an accession currently asserted in the YAML.

The marker reference matches [PMID 24391244](https://pubmed.ncbi.nlm.nih.gov/24391244/), Kalanetra and Nelson, DOI 10.1007/s00227-009-1362-3. The complete abstract, retrieved earlier in this same turn, describes both Escanaba Trough sediment-surface material and Juan de Fuca collections. The marker's explicit taxon binding supports the Escanaba identity; it does not transfer Juan de Fuca tube-associated abundance or productivity measurements to the ET isolate.

The inspected [LPSN parent-species page](https://lpsn.dsmz.de/species/marithrix-sessilis), name 800539, concerns Candidatus Marithrix sessilis, not an exact equivalent of this isolate. Its nomenclatural type is JdF and its marker is AY883933, distinct from ET/AY883934. Its Beggiatoales/Beggiatoaceae classification also differs from NCBI's Thiotrichales/Thiotrichaceae. Both distinctions are retained; no type assertion or replacement lineage is inferred for ET.

The [Salman et al. classification abstract](https://pubmed.ncbi.nlm.nih.gov/21498017/), DOI 10.1016/j.syapm.2011.02.001, inspected earlier this turn, gives historical 16S/ITS and morphological context. It is not culture-deposit or genome-link evidence. The YAML relies on NCBI provenance rather than claiming these literature results.

## Completeness

An ignored-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded ID 1037348, spaced/slug variants of the target label, Marithrix sessilis and AY883934. Thirteen matches consisted of seven native NCBI name rows, four backbone rows and two scope rows. All were read completely; no target strain/genome link or marker-bearing source row was found in those roots.

Separate complete structured scans found no own-ID BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits taxon inventory row. The full backbone has no child to supply descendant strains. Thus `strain_count: 0` correctly counts inventoried BacDive entries, not published sequences or environmental collections.

Five SOURCE.json files were parsed separately without a target match. Gitignore-independent filename searching found the target YAML and no previous report; history filename inspection found no target-specific filename. These absence statements are bounded to the named repository surfaces, not the entire literature or every external database. Eukaryota YAMLs were not opened.

Optional definition, record-level evidence, nomenclature, mappings and causal graphs need not be invented where the maintained inputs supply none. No unsupported genome or type-strain representation was added merely because a marker or parent species is known.

iModulonDB searches were not applicable to this identity/inventory record, which asserts no gene, regulator, pathway or transcriptomics result. No adapter call or dataset-absence conclusion is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. The isolate identity, ET-qualified synonym, parentage, count semantics and source provenance are supported. Cross-source classification differences and full-paper access limitations are documented, not silently resolved.

## Recommended Edits

None required. Retain ET as distinct from JdF and WP, preserve NCBI lineage, and keep the marker outside genome counts. Do not add the parent species' nomenclatural type to this isolate.

Future authorized corrections belong in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. Generated YAML must not be hand-edited. No correction is established here.

## Follow-up Checks

For any future enrichment, verify the exact isolate and collection-specific evidence. Obtain primary deposit/assembly evidence before proposing a genome relationship; a shared parent species is insufficient.

After a source refresh, repeat schema/strict/history validation and the documented full-corpus reproduction/QC gates. Full-paper access may improve experimental context but is not needed to support an experimental claim in this record, because none is present.

## Additional Notes

- SHA-256: `9700da33567cfef47993198adf8fa742181709be133ae30c06e014e9d8ea2d08`.
- `data/taxa/PATHS.tsv:15262` and `curation/seed_scope.tsv:322942` uniquely identify this target. The seed retains 2026-09-13T17:54:04Z and its matching one-source scope reason.
- Supporting source rows include parent backbone 206576, JdF/WP backbone rows 222715/222717, parent native name rows 14247-14249 and sibling synonyms 32323/32327 in NCBI names shard 0005.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. This is the sole new report for this target. No record, source input, schema, history, page, branch, worktree or GitHub state was changed; no status was promoted.
