# YAML Record Review: Methylobacterium sp. C23

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c23.yaml`
- Started UTC: 2026-10-06T15:06:41Z
- Finished UTC: 2026-10-06T15:08:34Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035202`, label `Methylobacterium sp. C23`, rank SPECIES, domain BACTERIA. The entire YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED, with ten root-first ancestors, genetic code 11, zero BacDive strain entries, one NCBI NAME attestation and one inline seed event. It carries no synonyms, equivalent xrefs, nomenclature, taxonomy mappings, genome links, definition, citations, phenotype assertions or causal graph. Review scope is this exact taxid, not all isolates bearing C23.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c23.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c23.yaml --out /private/tmp/mc23-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: identity, all lineage entries, code, attestation, scope and seed-event content agree with pinned inputs. This is not a replacement for corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- No curator-added ontology node needs a term check. `conf/id_label_targets.yaml` excludes taxonomy fields and delegates their inventory agreement to corpus reproduction.
- No separate target history file was found by an ignored-independent filename search. Inline history passed the record validators; no external history validator was run against an invented file.
- No DOI, PMID or quotation is asserted in this YAML. A publication linked from the sequence was inspected for completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221923`, [live NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035202&retmode=xml), and [NCBI taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035202) agree on the exact label and SPECIES rank. Both live responses were inspected in full. XML confirms bacterial division, parent 2615210, code 11 and no alternate names. Dataset metadata confirm the complete ten-identifier, root-inclusive ancestor chain; pinned ancestor labels/ranks agree with the YAML.

The direct parent is `unclassified Methylobacterium`, a no-rank grouping below genus taxid 407. This NCBI placement should remain carried verbatim. A sequence strain qualifier does not authorize replacing NCBI's SPECIES rank with STRAIN. EXACT identifies this NCBI concept, not a formally published binomial.

The [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was inspected in full. It names M. organophilum as type species and provides no C23 species-name or type-deposit attribution. Genus nomenclature is not evidence that this isolate is a type strain or a named species.

The pinned backbone has no children of this taxon. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target entry. The legacy NCBI Taxonomy browser route was inaccessible; the successful structured responses supplied the identity check.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221923` supports the label, rank, parent, code, empty synonym fields and NCBI-only provenance.
- Complete native `data/catalog/ncbi_names-0005.jsonl.gz:31391` contains the exact scientific name and taxid, with no unique-name disambiguator.
- `data/taxa/PATHS.tsv:14414` resolves this exact slug. `curation/seed_scope.tsv:322198` adds it on 2026-09-13 through the one-source attested rule.
- The inline 2026-09-13T17:54:04Z seed event agrees with the scope reason and source list. The attestation is one NAME, not one genome, deposit or phenotype.

Exact-taxid Entrez searches used `txid1035202[Organism:noexp]`. Assembly returned zero with phrases-not-found / no-items diagnostics. Nuccore returned one UID, 347300699, with the complete returned ID list equal to the result count. This bounded assembly no-hit is not proof of universal genome absence.

Complete [GenBank metadata for FR869798.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869798.1) identify a 1,335-nt partial 16S rRNA sequence, strain C23 and exact taxon 1035202. Source qualifiers describe host leaf surface and Cerastium holosteoides. The submission date is 18 May 2011, creation date 18 September 2011 and update date 6 December 2011. No culture-collection qualifier, BioSample, BioProject or assembly is present in the inspected metadata. All feature/source/reference metadata were read; sequence bases were omitted. This marker is not a genome.

The sequence cites Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The [complete PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml) were inspected and confirm that pairing. The study concerns phyllosphere communities across hosts, sites and land-use types. Its abstract does not identify C23 or establish an isolate-specific phenotype, site or growth requirement. Full text and supplements were not inspected, and no such claim is borrowed from the community-level results.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits entry. Taxid/label/slug searches, expanded Methylobacterium/Methylorubrum C23/C-23 searches, and the exact nucleotide accession search covered ignored and compressed sources. They found no additional eligible culture-deposit, genome-source or explicit StrainInfo sequence-deposit assertion for this target.

Zero listed strains is consistent with the BacDive-subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: there is no exact BacDive entry or descendant taxon to contribute one. This count is not a claim that the isolate was never cultured. The existing `normalize_culture_identifier` rejects both C23 and C-23 as unsupported bare designations.

Omission of FR869798.1 and its publication is not classified as a required-representation defect under the current model. There is no established existing strain entry or eligible own-deposit SI-DP association to receive the optional marker link. Future enrichment must establish an explicit identity and maintained import path; the bare label must not become a culture accession, genome or equivalence.

The structured iModulonDB adapter was run before browser follow-up and returned 28 datasets without Methylobacterium or Methylorubrum coverage. It is not applicable and is not negative biological evidence. Optional definition, phenotype and causal-graph fields may remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and evidence scope. Identity and provenance assertions are supported; the YAML does not overstate the sequence as a genome or inherit a formal species name or phenotype.

This pass does not certify full-corpus reproducibility, unasserted phenotypes or genome quality.

## Recommended Edits

None required for the current record.

If future source work supports a culture identity, use maintained upstream extraction and seeding logic, not a hand edit of generated YAML. Preserve FR869798.1 as a typed non-genome sequence if the importer/model supports it, with explicit provenance. Do not infer a culture accession or SI-DP from C23 alone.

Do not change SEEDED to REVIEWED or append history on the strength of this read-only report.

## Follow-up Checks

- On source refresh, repeat exact taxonomy, lineage, status and target schema/strict checks.
- After an authorized source/import change, run the real full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; the bounded comparisons here do not replace them.
- Inspect full text and supplements of PMID 22000032 before proposing any C23-specific phenotype or ecological conclusion.
- Require an eligible own-deposit identifier and explicit sequence association before adding a StrainInfo link. Keep FR869798.1 outside genome counts.
- Retry the legacy taxonomy browser only if needed; the two structured NCBI responses supplied the identity evidence.

## Additional Notes

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial identifier/label/slug search and expanded C23/C-23 context search each returned the same three rows. All were read completely through structured backbone/scope checks and a lossless native JSONL read. A separate FR869798 search returned no rows. Five SOURCE.json files were searched structurally; history filenames were checked independently. These absence findings include ignored files but remain bounded to the named sources.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Live NCBI taxonomy, exact-taxid sequence searches, full sequence metadata, PubMed metadata/abstract and the LPSN genus page were inspected. Search snippets were not used as evidence.

No record, code, generated-page, history or review-status edit was made. No paid research, outbound contact or Git/GitHub mutation occurred. Eukaryota reviews were not reopened.

