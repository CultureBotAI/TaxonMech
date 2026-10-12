# YAML Record Review: Methylobacterium sp. C14

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c14.yaml`
- Started UTC: 2026-10-06T15:00:40Z
- Finished UTC: 2026-10-06T15:03:05Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035201`, label `Methylobacterium sp. C14`, rank SPECIES, domain BACTERIA. The entire YAML was read before findings and checked byte-for-byte unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED, with ten root-first ancestors, genetic code 11, zero listed BacDive strains, one NCBI source attestation and one inline seed event. There are no synonyms, equivalent xrefs, GTDB mappings, nomenclature, genome links, definition, citations, phenotype assertions or causal graph. This report judges this exact taxid, not every isolate called C14.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c14.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c14.yaml --out /private/tmp/mc14-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: identity, all ten lineage entries, code, source count, scope and seed event match their pinned inputs. This is not a focused corpus-reproduction validator.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- No curator-added ontology graph requires term validation. The product checker excludes taxonomy fields and delegates those checks to corpus reproduction.
- No separate target history artifact was found by an ignored-independent filename search. Inline history passed schema validation; no history validator was run against an invented artifact.
- The YAML has no DOI, PMID or quoted evidence. Sequence-linked literature was checked for completeness context, not to validate an experimental assertion absent from the record.

## Identity and Grounding

Pinned backbone `data/raw/ncbitaxon_taxa.tsv:221922`, [live NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035201&retmode=xml), and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035201) agree on the exact label, SPECIES rank, bacterial domain, code 11 and parent `NCBITaxon:2615210`. Both API responses were inspected in full. The XML contains no alternate names. All ten root-inclusive lineage identifiers agree with the dataset response, and pinned labels/ranks agree with the YAML.

The parent is explicitly the no-rank group `unclassified Methylobacterium`, below genus taxid 407. It should remain in the carried NCBI lineage. The sequence's strain qualifier C14 does not authorize changing this NCBI taxon's SPECIES rank. EXACT identifies the NCBI concept; it does not establish valid publication of a formal species name.

The [LPSN Methylobacterium page](https://lpsn.dsmz.de/genus/methylobacterium), inspected during this review turn and rechecked for C14, is genus record 516060 and lists M. organophilum as type species. It does not identify C14 as a named species or type deposit. No genus nomenclature or named-species identity was inherited.

There is a distinct pinned taxon `NCBITaxon:267741`, `Methylobacterium sp. C-14`, at `data/raw/ncbitaxon_taxa.tsv:55255` and native name row `data/catalog/ncbi_names-0001.jsonl.gz:35082`. Neither target metadata nor the inspected source records provide an equivalence between these taxids. Punctuation normalization must not merge them. Reading this candidate for disambiguation did not reopen its review.

No target children, exact type-material entry, merged-ID entry or dropped entry were found in their pinned tables. Legacy browser routes for the target and C-14 were unavailable; the target's two NCBI API responses supply its identity and lineage evidence.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221922` supports the record's label, rank, parent, code, absence of aliases and NCBI-only source list.
- Complete native `data/catalog/ncbi_names-0005.jsonl.gz:31390` contains the exact scientific name, taxid and empty unique-name field.
- `data/taxa/PATHS.tsv:14413` resolves this slug. `curation/seed_scope.tsv:322197` adds the taxon on 2026-09-13 for its one-source NCBI attestation. The 2026-09-13T17:54:04Z seed event agrees.
- The sole attestation counts one NAME, not a genome, culture deposit or phenotype.

The exact-taxid Entrez query `txid1035201[Organism:noexp]` returned zero assemblies, with its "No items found" / phrases-not-found diagnostic, and one nucleotide UID, 347300698. The complete nucleotide ID list agrees with its returned count. The assembly query is a bounded no-hit, not proof of universal genome absence.

Complete [GenBank metadata for FR869797.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869797.1) identify a 1,335-nt partial 16S rRNA sequence, strain C14 and exact taxon 1035201. Source qualifiers state host leaf surface and Cerastium holosteoides. Submission was 18 May 2011; the record was created 18 September 2011 and updated 6 December 2011. No culture-collection identifier, BioSample, BioProject or assembly occurs in the inspected metadata. Bases were omitted, but all source/features/reference metadata were retained. This is a marker, not a genome.

Its publication is Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The complete [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml) were inspected in this turn and reread for this target. They confirm the bibliographic pairing and a phyllosphere community study across plant hosts, locations and land-use regimes. The abstract does not identify C14 or demonstrate a C14-specific phenotype or geographical conclusion. Full text/supplements were not inspected; no such assertion is added.

The expanded identity search found another C14 genome, which was investigated rather than transferred:

- Complete `data/bvbrc/bvbrc-0000.jsonl.gz:7454` identifies PATRIC 107400.7 as Methylobacterium fujisawaense C14, taxid 107400, with SAMN41163420 and PRJNA1107197.
- Complete GenBank `data/catalog/ncbi_genbank-0036.jsonl.gz:9141`, RefSeq `data/catalog/ncbi_refseq-0006.jsonl.gz:4158` and GTDB `data/catalog/gtdb_genomes-0012.jsonl.gz:11077` identify GCA_039619325.1 / GCF_039619325.1 / RS_GCF_039619325.1 for that named species, not taxid 1035201.
- The [live assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_039619325.1/dataset_report) confirms current assembly identity and the same sample/project. Complete [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN41163420&retmode=xml) identifies concrete exposed on a green roof, Delaware, collected 17 August 2014.
- That provenance differs from the leaf-surface C14 sequence submitted in 2011. Combined with distinct taxon identity and no explicit deposit bridge, the shared bare C14 label is insufficient to associate this genome with the reviewed taxon. This report rejects the join; it does not revise the other genome's classification.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/label/slug searches and accession/context expansion found no eligible target culture-deposit or explicit StrainInfo sequence-deposit link. The C-14 taxon and M. fujisawaense C14 genome are near matches, not qualifying target evidence.

Zero listed strains matches the BacDive-subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: there is neither an exact target BacDive row nor a descendant to contribute one. This does not deny existence of the original cultured isolate. Calls to the existing culture normalizer reject both C14 and C-14 as unqualified laboratory designations.

The absence of a nested FR869797 marker or publication is not independently classified as a missing required representation: no supported existing strain entry or explicit SI-DP attribution was established to receive that optional sequence link. A future authorized importer/model extension may preserve it, but it must not create a genome, culture accession or equivalence from a bare label.

The structured iModulonDB dataset adapter returned 28 datasets before browser follow-up, with no Methylobacterium or Methylorubrum dataset. It is not applicable; absence is not negative biological evidence. Optional definition, phenotype and causal-graph slots can remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and inspected source scope. The generated YAML makes supported identity/provenance assertions and does not conflate the similar C-14 taxon or the concrete-derived M. fujisawaense C14 genome.

This pass is not a full-corpus reproducibility result or a validation of unasserted phenotype, nomenclatural standing or genome quality.

## Recommended Edits

None required for the current record.

For future enrichment, establish explicit culture/source identity and an authorized maintained import path first. Preserve FR869797.1 as a typed non-genome marker if the model/importer supports it. Do not create a strain accession, SI-DP, genome or species equivalence from C14 alone. Any such extension belongs upstream of generated YAML, not in a manual edit of this file.

Do not promote the record to REVIEWED or append a curation-history event from this read-only report.

## Follow-up Checks

- On the next refresh, repeat exact target taxonomy/lineage/status checks and this record's schema and strict commands.
- After any authorized source/import change, run actual full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`. Bounded comparisons do not replace these gates.
- Preserve taxid 1035201 separately from 267741 and 107400; require explicit source/deposit evidence before any proposed merge or genome join.
- Inspect full text/supplements of PMID 22000032 before adding C14-specific phenotype or ecological assertions. Its abstract is community-level evidence only.
- Keep FR869797.1 outside genome counts. Retry unavailable browser routes only if needed; successful structured responses supplied this review's bounded evidence.

## Additional Notes

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial taxid/name/slug search found six rows, including the C-14 disambiguation candidate. Expansion using FR869797, UID 347300698 and C14/C-14 co-occurrence with Methylobacterium or Methylorubrum found ten rows, adding four complete genome-source candidates. All ten distinct rows were read in full through lossless native/TSV decoding. Separate exact checks covered backbone lineage/status, seven transformed source tables, PATHS and scope. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings are bounded to these sources and include ignored files.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Target taxonomy/sequence APIs, the conflicting candidate's assembly/BioSample APIs, and LPSN were inspected. The already fetched primary PubMed response was reread for the same paper explicitly cited by FR869797.1. Unavailable legacy browser pages were not substituted with search snippets.

No YAML/code/generated-page edits, history events, review-status promotions, paid research, outbound contact or Git/GitHub mutations were performed. Eukaryota reviews were not reopened.

