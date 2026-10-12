# YAML Record Review: Candidatus Isobeggiatoa divolgata

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/candidatus_isobeggiatoa_divolgata.yaml`
- Started UTC: 2026-10-06T02:18:31Z
- Finished UTC: 2026-10-06T02:26:24Z
- Verdict: pass

## Target

The entire 58-line `TaxonRecord` was read. It denotes `NCBITaxon:1034940`,
`Candidatus Isobeggiatoa divolgata`, rank `SPECIES`, domain `BACTERIA`, with
parent `NCBITaxon:1034939` (`Candidatus Isobeggiatoa`). It has nine root-first
ancestors, genetic code 11, two NCBI synonyms, `grounding_status: EXACT`,
`mapping_status: SEEDED`, and `strain_count: 0`.

This is generated taxonomy output. Its sole attestation is one NCBITAXON
`NAME` from the 2026-09-13 snapshot. The inline seed event is dated
2026-09-13T17:54:04Z. There are no asserted strain, genome, nomenclature,
phenotype, mechanism, or causal-graph objects to validate as additional claims.

## Validation

The following documented focused validators completed successfully, using
`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

| Command | Result |
| --- | --- |
| `just validate data/taxa/bacteria/candidatus_isobeggiatoa_divolgata.yaml` | Exit 0; no schema issues. |
| `just validate-strict data/taxa/bacteria/candidatus_isobeggiatoa_divolgata.yaml --out /private/tmp/divolgata-validation.tsv` | Exit 0; one file scanned, zero ERROR rows. The full diagnostic TSV contains only its header. |

Additional bounded read-only checks completed:

- Parsed the full target and full owning backbone row, compared every lineage
  entry, synonyms, code, attestation, scope reason, and seed-history shape.
- Checked the complete seven supplementary taxon inventories for the exact ID;
  none has an exact-ID row for this target.
- Checked exact-ID type-material, merged-ID, and dropped-record inventories;
  none has a row for this target. The backbone has no immediate child of it.
- Confirmed its unique index entry in `data/taxa/PATHS.tsv:14228` and scope
  entry in `curation/seed_scope.tsv:322057`.
- Inspected NCBI Taxonomy EFetch and Datasets responses, all four exact-taxid
  nucleotide records' complete metadata/references/features, and the two
  candidate WGS masters. Sequence bases were not needed for this identity audit.
- Reconciled every local candidate address with a complete native-object read.
  Repeated native fields were sometimes displayed once per file, with an
  asserted lossless reconstruction of each row; no fields were dropped.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, full
strict/history gates, complete provenance/hash reproduction, render drift,
README statistics, publication-budget gates, and vendored-skill synchronization.
Focused success is not a claim that those corpus gates passed. No separate
undocumented focused history or ontology validator was invented; ancestor,
source-reference, and inline-history checks above were manual/structured
comparisons rather than substitutes for the full gates.

## Identity and Grounding

The complete owning row at `data/raw/ncbitaxon_taxa.tsv:221758` agrees with the
YAML's ID, label, rank, parent, code, two synonym scopes, and snapshot date.
Every root-first ancestor agrees with the pinned backbone. Live NCBI EFetch
agrees on the species and its eight non-root ancestors; Datasets supplies the
same nine ancestor IDs including root. The identity is active, not a retired
identifier requiring a successor. See the inspected
[NCBI Taxonomy record](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034940).

The native NCBI name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31167`
through 31169 distinguish authority, scientific name, and equivalent name.
`Isobeggiatoa divolgata` is the equivalent name and is correctly carried as
`EXACT_SYNONYM`. The quoted Salman et al. 2011 authority is carried as
`RELATED_SYNONYM`. This follows the inspected name-class policy in
`src/taxonmech/ncbi_taxdump.py` and scope-preserving seeding in
`src/taxonmech/seed.py`; it is not a misfiled exact synonym.

The inspected [LPSN species page](https://lpsn.dsmz.de/species/isobeggiatoa-divolgata)
identifies the same name and authority, nomenclatural type `Dangast A9`, and
16S accession `AF532769`. It labels the name not validly published, with
pro-validly published/pro-correct status. Those qualifications must not be
flattened to an unqualified valid-publication claim. The YAML makes no such
claim. `Dangast A9` is an isolate designation here, not evidence of a registered
culture-collection deposit.

There is an external classification difference, not a transcription error:
NCBI places the species in Thiotrichaceae, while the inspected abstract of
Salman et al. 2011 argues for retaining Beggiatoaceae. This review preserves
that difference and does not silently replace the NCBI lineage with the
paper's treatment.

## Evidence

The NCBITAXON attestation is supported at `NAME` scope. Its count of one is
neither a sequence count nor an estimate of biological strains. The scope row
and inline seed event both explain inclusion through one source including
NCBI. No claim of human-reviewed status is present.

Exact `txid1034940[Organism:noexp]` searches returned four Nuccore records and
zero Assembly records. Assembly also returned a phrase-not-found warning;
this is a bounded exact-query result, not proof that no relevant genome exists
under another taxon or name. All four returned nucleotide records were read:

| Accession | Direct source identity | Supported scope |
| --- | --- | --- |
| [FN561862.1](https://www.ncbi.nlm.nih.gov/nuccore/FN561862.1) | Clone `Station J S3678`; Svalbard, Smeerenburgfjorden marine sediment; 1,501 bp | Partial 16S marker assigned to taxon 1034940; not a genome or deposit. |
| [AB108786.1](https://www.ncbi.nlm.nih.gov/nuccore/AB108786.1) | Clone `Tokyo Bay D`; marine sediment; 1,368 bp | Partial 16S marker assigned to taxon 1034940; not a genome or deposit. |
| [AF532775.1](https://www.ncbi.nlm.nih.gov/nuccore/AF532775.1) | Isolate `Limfjorden L9`; marine sediment; 1,496 bp | Partial 16S marker assigned to taxon 1034940; distinct from the type isolate. |
| [AF532769.1](https://www.ncbi.nlm.nih.gov/nuccore/AF532769.1) | Isolate `Dangast A9`; Wadden Sea sediment; 1,502 bp | Partial 16S marker assigned to taxon 1034940 and matching LPSN's cited type marker. |

None of these four inspected metadata records provides a collection deposit,
BioSample, BioProject, or assembly crosslink. Their shared taxon does not make
the four isolate/clone designations equivalent cultures.

Primary bibliographic records and author abstracts were inspected for:

- [Salman et al. 2011, PMID 21498017](https://pubmed.ncbi.nlm.nih.gov/21498017/),
  DOI `10.1016/j.syapm.2011.02.001`: the naming study and its explicitly
  different family treatment. Full article text was not obtained; the DOI
  fetch failed and two public author-PDF attempts returned 403/timeout.
- [Oren et al. 2020, PMID 32603289](https://pubmed.ncbi.nlm.nih.gov/32603289/),
  DOI `10.1099/ijsem.0.003789`: the Candidatus-list reference linked by LPSN and
  NCBI. Its abstract is not evidence that every listed name is validly published.
- [Jorgensen et al. 2010, PMID 20608982](https://pubmed.ncbi.nlm.nih.gov/20608982/),
  DOI `10.1111/j.1574-6941.2010.00918.x`: the source publication for FN561862.
- [Kojima and Fukui 2003, PMID 14509709](https://pubmed.ncbi.nlm.nih.gov/14509709/),
  DOI `10.1016/S0043-1354(03)00206-9`: the source publication for AB108786.
- [Mussmann et al. 2003, PMID 12755720](https://pubmed.ncbi.nlm.nih.gov/12755720/),
  DOI `10.1046/j.1462-2920.2003.00440.x`: a source publication for both AF markers.

These studies concern sampled filamentous bacteria and their diversity. Their
site-level or multi-organism physiology is not silently promoted to a
species-wide phenotype, mechanism, nitrate-storage concentration, or habitat
assertion in this taxonomy-only YAML.

A bounded genome lead was also examined in the primary
[Mussmann et al. 2007 article](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0050230).
The inspected sampling, sequencing, phylogenetic, and accession passages
distinguish two single filaments, PS and SS; this was not a full functional
reanalysis of the paper. The corresponding complete GenBank master metadata
and local native records establish:

| Candidate | Recorded identifiers | Why it is not attached here |
| --- | --- | --- |
| Beggiatoa sp. SS | `ABBY00000000.1`, `NCBITaxon:422288`, `GCA_000170695.1`, `SAMN02470513`, `PRJNA18685` | Separate recorded taxon/isolate; no inspected deposit or curated identity bridge to 1034940. |
| Beggiatoa sp. PS | `ABBZ00000000.1`, `NCBITaxon:422289`, `GCA_000170715.1`, `SAMN02470514`, `PRJNA18683` | Separate recorded taxon/isolate; no inspected deposit or curated identity bridge to 1034940. |

The local GenBank summaries flag SS as fragmented and PS as contaminated and
fragmented. Their paired RefSeq assemblies occur in the historical catalog as
suppressed. These statuses must remain visible in any future use. Different
NCBI IDs alone do not disprove a possible taxonomic reassignment; the missing
evidence-supported bridge remains an explicit limit of this review, not a
license to invent equivalence or a demonstrated omitted required genome link.

## Completeness

The current record is complete enough for its supported, NCBI-only seeded
identity. Optional nomenclature, strains, mappings, and causal evidence need
not be filled merely because those schema slots exist. Zero imported strains
does not mean no filaments, isolates, sequences, or biological strains exist.

Gitignore-independent searches included `rg --no-ignore --hidden -n -z -i`
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`.
Compressed catalogs were searched; source-manifest `SOURCE.json` files were
excluded from the biological-candidate search. The conclusions below are
bounded to those roots and patterns, not a universal literature search.

- The target ID, full label, and slug search yielded 51 lines: the owning
  backbone/scope rows, three native NCBI names, and 46 unrelated numeric-token
  matches. All 49 non-backbone/scope native rows were read, including complete
  ATB rows. The distractors include Salmonella and Staphylococcus sample IDs,
  an M. tuberculosis run named `ERR1034940`, and unrelated assembly/strain
  identifiers. None establishes an exact target link.
- A genus, marker, and isolate-designation search yielded 106 lines, with 101
  additional native rows read. These include one SeqCode genus discovery
  object (`36806`), eight other NCBI name objects, six ancestor/adjacent
  backbone/scope rows, 18 GOLD project/analysis rows for nine Guadeloupe cell
  enrichments, and 68 unrelated Salmonella assemblies matching the `S3678`
  substring. Genus discovery, adjacent taxa, and cell-enrichment projects do
  not establish a species-level deposit or assembly link.
- An additional `ABBY00000000`, `ABBZ00000000`, and explicit PS/SS name search
  yielded 45 lines, all read. Eighteen concern the two candidate taxa and their
  native source chain; 27 are different organisms with longer WGS accessions
  containing those substrings. Partial identifier matches were not treated as
  identity evidence.
- The seven complete supplementary inventories searched were
  `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`,
  `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, and
  `bactotraits_taxa.tsv` under `data/raw`. No exact target-ID row was found.
- Ignored-inclusive ID/name/slug searches in reports/history and a filesystem
  filename search found no previous target report before this report was
  created. That is not an assertion that the inline seed event is missing.

The live LPSN page is a genuine nomenclature enrichment opportunity. However,
`docs/SOURCE_COVERAGE.md` defines local LPSN coverage as the complete pinned
kg-microbe transform, not a complete mirror of the current site. Its absence
from that inventory is not, by itself, a failed mandatory representation.
Similarly, the SeqCode discovery census does not authorize a species mapping
from a genus name. No exact GTDB mapping or eligible own culture deposit was
established in these checks.

iModulonDB is not applicable: the record asserts no strain-specific gene,
regulator, expression module, or transcriptomics result. There is no causal
graph to audit; none was invented to make the record appear richer.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the represented claims. The external Thiotrichaceae versus
Beggiatoaceae classification difference, optional LPSN enrichment opportunity,
and unresolved PS/SS identity bridges are preserved above. They are not
presented as proven defects in a faithful NCBI snapshot record. The pass is
limited to this record and the checks actually completed.

## Recommended Edits

None required for the supported current representation. Do not hand-edit the
generated YAML, increase `strain_count` from marker counts, assign PS/SS or
Guadeloupe genomes by name similarity, or relabel this record `REVIEWED`.

For future authorized nomenclature enrichment, maintain the source capture
and extraction inputs used by `scripts/extract_source_inventory.py`, preserve
LPSN's qualified publication status and type-marker evidence, and inspect the
resulting `data/raw/lpsn_names.tsv` assertion before regeneration. Any mapping
or synonym-policy change belongs in the maintained importer/harmonization
code, notably `src/taxonmech/ncbi_taxdump.py` and `src/taxonmech/seed.py`, not
this generated artifact. NCBI snapshot changes belong in the pinned inputs
configured by `conf/ncbi_taxdump.yaml`. Scope changes, if justified separately,
belong in `curation/seed_scope.tsv`; none is indicated here.

## Follow-up Checks

No blocking follow-up is required for this pass. Before a future enrichment:

1. Reinspect the full naming/type evidence and authoritative nomenclature
   status; retain the source-classification conflict instead of silently
   substituting one lineage for another.
2. Require an explicit identity/deposit bridge before attaching PS, SS, or a
   Guadeloupe genome. Preserve assembly version, quality, and historical
   status; do not count samples, projects, and assemblies as interchangeable.
3. Regenerate through the documented validated writer and
   `scripts/seed_from_sources.py`, rerun the same focused schema/strict
   validators, then run the documented full reproduction/history/provenance
   and publication gates before accepting a corpus change.

## Additional Notes

The review used the repository review skill, curation write boundaries, local
field checklist, source-coverage documentation, and relevant schema/importer
rules. Unavailable full article/PDF access is explicitly distinguished from
the primary metadata and abstracts actually inspected. No inaccessible text
was used as evidence.

Only this new report was authorized as a repository write. No taxon, source
inventory, scope, history, prior report, generated page, or shared index was
modified; no curation event or review-status promotion was made. Eukaryota
records and their existing reports were left untouched. The parallel session
was reported closed, and the existing sole worktree was retained.
