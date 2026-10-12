# YAML Record Review: Pseudonocardia sp. KSF27

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudonocardia_sp_ksf27.yaml`
- Started UTC: 2026-10-03T23:57:53Z
- Finished UTC: 2026-10-04T00:02:14Z
- Verdict: pass

## Target

Read all 54 lines of generated `TaxonRecord` NCBITaxon:1032349,
Pseudonocardia sp. KSF27. It carries `SPECIES`, `BACTERIA`, `EXACT`,
`SEEDED`, one NCBI name attestation, zero inventoried BacDive strains and
one seed event. No genome, phenotype, nomenclature, taxonomy mapping or
graph assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudonocardia_sp_ksf27.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudonocardia_sp_ksf27.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, complete lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Publisher full
text was inaccessible through the DOI and PubMed full-text links; PubMed
metadata and abstract were inspected. Focused source checks do not prove
corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220852`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032349&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032349)
agree on exact label, species rank, parent NCBITaxon:2619320 and code 11.
All ten root-first lineage entries agree through Bacillati,
Actinomycetota, Actinomycetes, Pseudonocardiales, Pseudonocardiaceae,
Pseudonocardia and unclassified Pseudonocardia. Datasets includes root.
The taxonomy browser failed, but both structured authority reads worked.

Native name row `data/catalog/ncbi_names-0005.jsonl.gz:30134` supplies
the scientific name. `data/taxa/PATHS.tsv:13217` and
`curation/seed_scope.tsv:321233` support the exact slug and seed reason.
No source synonym or backbone child was found in complete structured
scans. Species rank satisfies scope; it does not assert formal
nomenclatural publication or type-strain status.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid1032349[Organism:noexp]` returned two records;
  their source features and references were inspected.
  [AB630184.1](https://www.ncbi.nlm.nih.gov/nuccore/AB630184.1) is a
  1,517-base partial 16S sequence naming strain KSF27 and taxon1032349.
  Its source annotation identifies upland soil in Japan. Preserve its
  submitted partial-sequence status; it is not an assembly.
- AB630184.1 links Sakakibara, Takagi, Kataoka, Kiyota, Sato and Okada's
  2011 study, [PMID21708128](https://pubmed.ncbi.nlm.nih.gov/21708128/),
  [DOI10.1016/j.bbrc.2011.06.096](https://doi.org/10.1016/j.bbrc.2011.06.096),
  Biochem. Biophys. Res. Commun.411(1):76-81. PubMed independently
  confirms authors, title, journal and identifiers. The abstract identifies
  KSF27, its 16S-based Pseudonocardia placement and pesticide-degradation
  observations. These are strain-specific optional context, not claims
  carried by this YAML. The other reference is a May 12, 2011 submission.
- [HV958881.1](https://www.ncbi.nlm.nih.gov/nuccore/HV958881.1) is a
  1,517-base patent nucleotide record with exact organism and taxon1032349,
  annotated as unassigned DNA. It cites Takagi and Sakakibara's
  [JP2012200155A](https://patents.google.com/patent/JP2012200155A/en),
  published October 22, 2012. Inspected patent text explicitly identifies
  KSF27 and deposit `FERM AP-22071`, deposited February 22, 2011.
  This establishes patent-reported deposit context, not a whole genome,
  a current collection-catalog validation or a type-material designation.
- Complete scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and
  BactoTraits raw inventories found no exact target row. `strain_count: 0`
  correctly counts inventoried BacDive records, not all biological isolates.
- Numeric catalog hits concern GCA_036164455.1, Bacteroidota bacterium
  taxon1898104, isolate XB_MAG260, sample SAMN39283597 and PRJNA880762.
  GenBank0033:41115 and GTDB0008:30335 contain genome-length value
  1032349, not the target taxon ID. The GTDB classification is MED-G16
  sp002701745. No target mapping or genome link follows from this collision.
- The resolved `kg-microbe-sources imodulondb datasets` runner returned
  28 keys, none for Pseudonocardia. iModulonDB was not applicable to the
  optional trait context; lack of coverage is not negative biological
  evidence. No unrelated expression-module evidence was transferred.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings; this is
not global proof of genome absence. Neither nucleotide record is a genome,
and the unrelated Bacteroidota catalog entry supplies no own-strain link.

Ignored-inclusive identifier, exact-label, slug and KSF27 spelling
searches covered raw inventories, all catalog shards, BacDive, BV-BRC,
GOLD, SeqCode, StrainInfo, ATB strain/genome links and exclusions, curation
and history. After excluding the numeric genome-length collision, no own
native genome, type-material, culture-collection, merged-ID, dropped-row
or standalone history entry was found on those surfaces. The target raw
and maintained matches were the backbone and scope rows.

A separate completed ignored-inclusive search over those same surfaces
found no `FERM AP-22071` entry, either sequence accession, patent number,
PMID or DOI. Complete inspection of the pinned CAFI registry found no
FERM authority or acronym synonym. Do not invent a supported authority,
replace the AP prefix, or join on bare KSF27 or 22071. Patent-reported
deposit context remains an optional enrichment lead, not proof that a
required eligible BacDive/StrainInfo join was lost.

No inventoried BacDive strain or eligible own deposit starts a SI join;
no carried BIOSAMPLE assertion starts an ATB join. Sample/FASTA
eligibility and sequence equivalence were not audited, and no global ATB
absence is claimed. Empty optional synonyms, nomenclature, mappings,
definitions, general evidence, discussion and graphs are appropriate for
the current NCBI-only assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input correction is
required by the inspected evidence. The external deposit and literature
are bounded follow-up leads rather than required fields left unsupported.

## Recommended Edits

None required. Preserve generated YAML, exact isolate, NCBI lineage and
`SEEDED` status. Future taxonomy fixes belong in the upstream NCBI source
and pinned inventory; extraction/seeding fixes belong in
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
`src/taxonmech/seed.py`, with regression tests. Optional publication,
patent or deposit enrichment requires separately authorized maintained
evidence and authority validation, not a direct generated-YAML edit.

## Follow-up Checks

- At refresh, verify the exact taxon and parent and retain the distinction
  between a sequence, patent deposit and whole-genome assembly.
- Before optional enrichment, inspect full publication text and current
  deposit authority evidence. Resolve source sequence-length differences
  by inspecting actual sequence listings, not by assuming equivalence.
- Keep any sequence or patent links in appropriately typed related records
  outside genome counts, with explicit own-deposit evidence for SI joins.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:1032349, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

The patent's inspected prose describes 1,441 consecutive 16S bases and
SEQ ID NO:1, whereas HV958881.1 is annotated as 1,517 bases. No sequence
alignment or patent PDF/listing comparison was performed. Preserve this
source-level distinction without asserting that the two nucleotide
records are identical or that the discrepancy is a YAML defect. The
patent page exposes Japanese text and a machine translation; its deposit
identifier is explicit in both. No legal-status conclusion is drawn.

All local absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files; the CAFI check
inspected the complete JSON and an ignored-inclusive text search. Only
free public sources were used. No optional context was inserted into
YAML, and no outbound message, GitHub mutation, history event or status
promotion occurred. Older reports and completed Eukaryota coverage were
untouched.
