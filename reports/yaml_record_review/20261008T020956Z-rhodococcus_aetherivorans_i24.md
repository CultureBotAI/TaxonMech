# YAML Record Review: Rhodococcus aetherivorans I24

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhodococcus_aetherivorans_i24.yaml`
- Started UTC: 2026-10-08T01:58:17Z
- Finished UTC: 2026-10-08T02:09:56Z
- Verdict: pass

## Target

The entire 66-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1036179`, Rhodococcus aetherivorans I24, rank STRAIN, domain BACTERIA, parent `NCBITaxon:191292` (Rhodococcus aetherivorans). Its ten root-first ancestors, two NCBI exact synonyms, EXACT grounding, SEEDED status, code 11, zero listed strains, two attestations and inline seed event were checked.

Identifier, label and slug resolve one target. Historical Rhodococcus sp. I24 and unrelated short-name matches were examined only to prevent incorrect joins, not as additional YAML reviews.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/rhodococcus_aetherivorans_i24.yaml` | Passed; no LinkML issues. |
| `just validate-strict data/taxa/bacteria/rhodococcus_aetherivorans_i24.yaml --out /private/tmp/i24-strict.tsv` | Passed; one file, zero errors; TSV header only. |
| Structured pinned-source comparison | Identity, rank, parent, code, all ancestors, both synonyms, attestations, scope and slug agree. |
| Exact status checks | No target child, type-material, merged-ID or dropped-ID row. |
| Current NCBI Taxonomy EFetch and Datasets | Target identity, strain rank, lineage, parent, code and equivalent names agree. |
| Exact-taxon sequence search | Assembly: zero with no-items/phrase-not-found warning. Nuccore: 25 records. |
| Nucleotide identity metadata | All 25 records' top-level identity, source-feature and citation metadata inspected; sequences and non-source feature annotations were not reviewed. |
| Plasmid BioSample and assembly lead | SAMN14225691 resolves to I24 and DQ629589.1. GCF_009951065.1 returned an empty Datasets report and no Assembly search result. |

Not run: whole-corpus `just verify-corpus`, QC, provenance, product-label, rendering and documentation gates. Focused validation is not full-corpus reproduction. There is no curator-added ontology graph or literature assertion requiring a separate term/reference check. Ignored-inclusive bounded searches found no separate target history artifact; schema validation covered inline history shape.

## Identity and Grounding

Current NCBI agrees with the record's strain-level concept and its complete carried lineage. Both `str. I24` and `strain I24` names are equivalent-name forms, consistent with the pinned exact-synonym classification. EXACT denotes grounding to this concept, not equivalence to the parent species or to every organism called I24. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036179)

Pinned identity and aliases occur at `data/raw/ncbitaxon_taxa.tsv:222305` and `data/catalog/ncbi_names-0005.jsonl.gz:31832` through the following two objects. The parent and all ten ancestors match their backbone rows.

NCBI still separately resolves `NCBITaxon:91380`, Rhodococcus sp. I24, as a species-ranked concept under unclassified Rhodococcus. Its native GOLD organism/project are Go0001819/Gp0001819; the target's are Go0023416/Gp0023416. Historical papers use the shorter name, but this does not authorize merging the current taxonomy concepts or declaring the underlying cultures biologically different. [Separate current NCBI concept](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=91380)

## Evidence

The NCBITAXON attestation is one NAME at snapshot 2026-09-13. The MADIN attestation is one TRAIT_ASSERTION, matching `data/raw/madin_taxa.tsv:684`. These count different upstream units and are not summed or interpreted as a named physiological trait.

The exact BV-BRC object at `data/bvbrc/bvbrc-0000.jsonl.gz:3357` identifies genome record 1036179.5 as a plasmid with accession DQ629589. Native GOLD objects at `data/gold/organisms.jsonl.gz:19809` and `data/gold/projects.jsonl.gz:19285` identify the target and its project, but provide no culture-collection, BioSample or BioProject bridge.

NC_010882.1 is the complete 9,372-base pRA1 plasmid; RefSeq explicitly identifies its sequence as DQ629589.1. The BioSample XML links SAMN14225691 to that accession, strain I24 and taxon 1036179. The annotation name contains GCF_009951065.1, but neither queried assembly API resolved it. This supports a plasmid/sample association, not a verified public whole-genome assembly. [RefSeq plasmid](https://www.ncbi.nlm.nih.gov/nuccore/NC_010882.1), [GenBank plasmid](https://www.ncbi.nlm.nih.gov/nuccore/DQ629589.1), [BioSample](https://www.ncbi.nlm.nih.gov/biosample/SAMN14225691)

The other nucleotide records include marker genes, partial loci, patent sequences and cosmid inserts. Their inspected source features provide no culture-collection qualifier. AF452375.2 and AF452376.1 cite PMID 15069586, DOI 10.1007/s00253-004-1589-3. Its inspected abstract concerns indene bioconversion under the historical Rhodococcus sp. I24 name and includes heterologous enzyme assays. The current accession metadata supplies a target-specific lead; it does not establish a taxonomy merge. Publisher full text was inaccessible. [Primary abstract](https://pubmed.ncbi.nlm.nih.gov/15069586/)

HQ130734.1 and HQ130735.1 cite PMID 21398488, DOI 10.1128/AEM.02429-10. The inspected primary methods, strain table and accession section identify I24 as the gene donor; polymer-production experiments use engineered Ralstonia eutropha. A supplied draft I24 genome is mentioned without establishing a deposited assembly. Do not transfer production yields or recipient cultivation conditions to wild-type I24. [Primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3126409/)

The YAML itself asserts no gene function, phenotype, DOI/PMID, quotation or causal edge. iModulonDB was not applicable to its identity/count-only content; sequence-associated literature leads create no expression-module claim.

## Completeness

The six other raw BacDive, LPSN, GTDB, GOLD, MediaDive and BactoTraits inventories contain no exact-target row. Native GOLD availability is not equivalent to a seeded GOLD organism-count attestation: `src/taxonmech/extract.py` obtains that count from transformed kg-microbe GOLD edges, while its native workbook relationships serve separate joins. The present attestations faithfully reflect the pinned inventory.

Zero listed strains means zero eligible BacDive entries in the seeder, not absence of this biological strain. Genome links currently attach to those entries. Neither the BioSample nor the inspected native target objects establishes a BacDive/culture-deposit bridge. Omitting unsupported deposits, type status, LPSN nomenclature and GTDB mappings is appropriate.

Ignored-inclusive compressed-input searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxon ID, bounded I24 and slug produced 108 candidate rows/objects, all read in full using lossless structured output. Expanding to the sequence accessions, BioSample, assembly annotation and GOLD IDs produced the same 108 addresses, with no additional candidate.

BacDive 160629 and StrainInfo 396707 concern Spirosoma endbachense I24/I-24, with DSM 111055/KCTC 72613; StrainInfo 65475 concerns Sordaria fimicola. Other candidates explicitly concern different genera, environmental station names or suffixed isolates. Rhodococcus sp. LAA-2009-i24 is another distinct named concept. None is a deposit bridge based only on I24.

Resolution additionally searched `data/taxa` and `reports`, including ignored files, with no previous target report. All five source metadata JSON files and history filenames were checked. These are bounded negative findings, not claims that no additional sequence, collection deposit or publication exists globally.

The plasmid/sample association and experimental literature are optional enrichment, not missing required representations in the present identity record. The unresolved assembly annotation must remain a limitation rather than be converted into a genome link or a claim that no assembly exists.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the asserted identity, lineage, synonyms, source counts or audit state. The historical-name relationship and unresolved assembly annotation limit future enrichment but do not invalidate the current assertions.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Any authorized enrichment must establish the intended strain/deposit representation before adding the plasmid, sample or project relationship. Maintained source transformations and join logic in `src/taxonmech/extract.py`, the relevant source adapter and `src/taxonmech/seed.py` own such changes; kg-microbe owns changes to its transformed attestation inputs. Do not patch the generated YAML, count native GOLD projects as seeded organism assertions, or infer culture equivalence from a short label.

## Follow-up Checks

Resolve GCF_009951065.1 through an authoritative assembly record before using it as an assembly link. Any taxonomy reconciliation with 91380 requires explicit authority evidence. Any biological enrichment must preserve donor versus recipient, natural versus engineered strain and assay conditions.

For authorized input/generator changes, run the seed dry-run and `just seed-canary NCBITaxon:1036179`, inspect the biological diff and repeat both focused validators. Test short-name exclusions and plasmid-versus-assembly handling in changed join logic. Shared changes require the documented full-corpus, QC, provenance, product, rendering and documentation gates. No regeneration was performed here.

## Additional Notes

Scope: `curation/seed_scope.tsv:57257`, added 2026-09-12. Slug: `data/taxa/PATHS.tsv:14810`; legacy page mapping: `curation/legacy_page_paths.tsv:886`. Seed event remains `2026-09-13T17:54:04Z`.

The BioSample browser endpoint failed, but complete public EFetch XML was retrieved. The first PMC redirect returned a browser check; the canonical PMC article then opened successfully. No paywalled text was treated as inspected evidence.

Reviewed HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Unchanged target SHA256: `98faa9cf13c3bf9d0fff5e8369a31deb24bde2955ca4c402f635b6cf072337ba`. Only this new Markdown report was added for the individual review. No YAML, history, lifecycle, source snapshot, GitHub or worktree changes occurred. Eukaryota was not re-reviewed.
