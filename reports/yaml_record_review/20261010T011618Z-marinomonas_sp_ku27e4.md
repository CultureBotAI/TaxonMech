# YAML Record Review: Marinomonas sp. KU27E4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marinomonas_sp_ku27e4.yaml`
- Started UTC: 2026-10-10T01:13:12Z
- Finished UTC: 2026-10-10T01:16:18Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:1037365` denotes Marinomonas sp. KU27E4, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196814` (unclassified Marinomonas), genetic code 11, grounding `EXACT`, status `SEEDED`.

It contains ten ancestors, no synonym list, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. The isolate-style name does not override NCBI's species rank.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/marinomonas_sp_ku27e4.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/marinomonas_sp_ku27e4.yaml --out /private/tmp/taxonmech-ku27e4-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links, run during this turn before this target; history was not changed.
- Structured comparisons verified own identity, full lineage, code, empty synonym columns, attestation, index/scope entries and seed reason. Complete backbone scanning found no direct child. Exact own-ID type-material, merged-ID and dropped scans found none.
- Complete native candidate rows, live NCBI taxonomy responses and marker metadata were inspected. The linked PubMed abstract and identifiers were read during this turn; this target's bibliographic connection was independently verified in its own marker entry.
- The relevant annual-report section, printed pages 244-245, was read in full and visually checked, including Figures 4 and 5. The web tool rejected the 14 MB PDF; direct public download and isolated temporary PyMuPDF parsing/rendering succeeded. No repository dependency was changed.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. No causal graph is asserted, so `just validate-products` has no applicable nodes. Focused matching does not reproduce the corpus.
- The complete phthalate paper, strain-level assay tables, independent phylogeny and genome comparisons were not audited. The unrelated sections of the 304-page annual report were not reviewed in full.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222731`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037365&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037365) agree on exact scientific name, species rank, parent and code.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Oceanospirillales, Oceanospirillaceae, Marinomonas and unclassified Marinomonas. Every stored ancestor ID, label and rank matches the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1.

`data/catalog/ncbi_names-0005.jsonl.gz:32350` is the exact own scientific-name row. Pinned synonym columns are empty and live EFetch supplies no synonym. Exact grounding concerns this NCBI concept, not formal nomenclatural validity or equivalence to a neighboring named species.

## Evidence

The sole NCBITAXON attestation has exact own ID/label, count 1, unit `NAME`, snapshot 2026-09-13. It counts a name assertion, not genomes, deposits or phenotypes.

A live exact nucleotide query, `txid1037365[Organism:exp]`, returned one entry. Complete [AB636143 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AB636143) identifies AB636143.1, a 1,430-base partial 16S rRNA sequence with partial feature endpoints, organism Marinomonas sp. KU27E4, strain KU27E4 and `taxon:1037365`. Its source qualifier gives Japan:Okinawa. Sequence length agrees with the annotation; ambiguous N bases are present. It is a marker, not a genome or culture-collection accession. The query is not a global sequence census.

The marker bibliography explicitly links [Iwaki, Nishimura and Hasegawa, PMID 22805854](https://pubmed.ncbi.nlm.nih.gov/22805854/), DOI 10.1007/s11274-011-0925-x, World Journal of Microbiology and Biotechnology 28:1321-1325 (2012). The inspected abstract describes eleven Japanese seawater isolates, phthalate utilization and assay/PCR observations. It does not name KU27E4 individually; the marker bibliography supplies the identity connection. This does not establish a complete genome or a fully resolved strain-specific pathway.

A separate [Rajiv Gandhi Centre for Biotechnology annual report](https://rgcb.res.in/documents/annualreports/Annual%20Report2013-14.pdf), printed pages 244-245, reports work by Arjun J.K. and Hari Krishnan K. on marine-sediment isolates from Kerala. The section identifies 27 isolates, ten showing enzyme activity, and experimental isolate TVS 38 with the highest reported L-asparaginase activity. Figure 4 names TVS 38; Figure 5 places TVS 38 and Marinomonas sp. KU27E4 (AB636143.1) as distinct tree tips. Its text explains comparison with database sequences. Thus KU27E4 is a reference sequence here, not demonstrated to be the enzyme-tested isolate. No TVS 38 identity, Kerala isolation or L-asparaginase phenotype is transferred to this target.

The YAML asserts taxonomy and provenance only. No growth, enzyme, gene, habitat or causal claim is currently represented or newly inferred.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1037365, KU27E4 with optional space/hyphen/underscore separators, and the slug. All five matching lines were inspected: own backbone, native name and scope rows, plus two unrelated assembly rows.

The complete candidate rows at `data/catalog/ncbi_genbank-0050.jsonl.gz:11927` and `data/catalog/ncbi_refseq-0008.jsonl.gz:14204` describe GCA_054355735.1/GCF_054355735.1, Mesomycoplasma ovipneumoniae taxon 29562, strain MoS5L23A, BioSample SAMN54369262. Both contain 1037365 as genome length, not taxon ID. Neither supports a target genome link.

A follow-up ignored/compressed-inclusive AB636143 search over the same roots returned no matches. Five SOURCE.json files were separately parsed without a target match. Gitignore-independent filename enumeration under the taxon corpus and report directory found only this YAML and no prior report. History filename inspection found no target-specific filename. These are bounded repository checks, not global absence claims.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. No immediate backbone child supplies descendant inventory. Zero correctly counts inventoried BacDive strains, not whether an isolate was studied. No repository-supported deposit/genome chain was established.

Optional definitions, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable to the taxonomy-only YAML; neither the study abstract nor the unrelated TVS 38 enzyme work creates a record gene or transcriptomics assertion. No adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, provenance, source-count semantics and seeded status are supported. The unrelated genome-length matches and phylogenetic-reference use provide no basis for enrichment. Skipped corpus checks and uninspected phthalate assay detail remain limitations.

## Recommended Edits

None required. Preserve authority rank, unclassified placement and zero BacDive count. Do not treat AB636143 as a genome, conflate TVS 38 with KU27E4, or transfer a genome based on a numeric length match.

Future authorized corrections belong in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect requires a change here; generated YAML must not be hand-edited.

## Follow-up Checks

Before phenotype or mechanism enrichment, inspect the complete primary study and target-specific assays. A phylogenetic reference tip is not experimental-strain equivalence. New deposit/genome links require an explicit source-supported identity chain and whole culture accessions.

After an authorized source refresh, rerun schema/strict/history validation and documented full-corpus reproduction/QC gates. Focused matching does not replace those checks.

## Additional Notes

- YAML SHA-256: `69ca6d10272a8d892c734f442d73b19ad16cce4669ca0962860039919770d479`.
- `data/taxa/PATHS.tsv:15279` and `curation/seed_scope.tsv:322956` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and the exact one-source scope reason.
- PDF text extraction did not contain the KU27E4 figure label; visual inspection of the rendered page established its exact accession and separate-tip placement. The printed page numbers are 244-245, zero-based PDF indices 243-244.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
