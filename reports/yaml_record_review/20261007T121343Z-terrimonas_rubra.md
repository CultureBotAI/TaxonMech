# YAML Record Review: Terrimonas rubra

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/terrimonas_rubra.yaml`
- Started UTC: 2026-10-07T12:06:34Z
- Finished UTC: 2026-10-07T12:13:43Z
- Verdict: pass

## Target

Complete generated `TaxonRecord` for `NCBITaxon:1035890`, species
Terrimonas rubra, domain BACTERIA, parent `NCBITaxon:296051` (Terrimonas).
The entire YAML was read, including all eleven lineage entries,
nomenclature, two related synonyms, one GTDB mapping, two xrefs, one
BacDive strain, all genome/related assertions, six source attestations
and the inline seed event.

The single strain is `kgmicrobe.strain:bacdive_133766`, designation M-8,
with CCTCC AB 2010401 and KCTC 23299 deposits and a derived type-strain flag.
It carries eight assembly assertions, four other genome-record assertions
and eighteen typed related-record assertions. These are provenance-bearing
assertions, not thirty distinct genomes.

The maintained owners are the committed inventories, their source adapters,
`src/taxonmech/seed.py` and `curation/seed_scope.tsv`. The generated YAML
is read-only; `scripts/seed_from_sources.py` is the seeder CLI wrapper.

## Validation

- `just validate data/taxa/bacteria/terrimonas_rubra.yaml`: passed with
  no LinkML issues.
- `just validate-strict data/taxa/bacteria/terrimonas_rubra.yaml --out /private/tmp/terrimonas-rubra-strict.tsv`:
  passed; one file, zero errors. The resulting TSV contains its header only.
- Complete target/backbone, eleven-ancestor, synonym, scope, path-index,
  attestation and inline-history comparisons passed.
- Field-for-field structured comparison of all eight assembly, four
  genome-record and eighteen related-record assertions against their raw
  inventory rows passed. All deposit-based links passed the existing CAFI
  whole-accession matcher against an actual listed deposit.
- Live NCBI taxonomy, NCBI assembly reports, ENA sample, BV-BRC genome,
  LPSN, BacDive, KCTC, PubMed and GenBank checks are described below.
- `just validate-products`: not applicable; no curator-added graph nodes.
- Separate `just validate-history`: not applicable; ignored-inclusive
  history content and filename searches found no matching standalone record.
  The existing inline event was checked without changing it.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`,
  `just validate-all`, `just provenance-check`, `just render-check`,
  `just docs-check` and `just vendored-check`. Focused comparisons do not
  prove whole-corpus reproducibility, source hashes or publication freshness.

## Identity and Grounding

Backbone row `data/raw/ncbitaxon_taxa.tsv:222190` and all three native
name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31681` onward agree
with the target. The authority spelling and former M-8 name are represented
as RELATED_SYNONYM, consistent with native authority and includes classes;
type-material strings are not promoted to taxon synonyms.

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035890&retmode=xml)
confirms identifier, name, rank, bacterial division, parent, genetic code 11,
related names and type material.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035890)
agrees on identity and the full ancestor identifier chain, including root.
All ancestor labels and ranks were checked against the backbone and EFetch.
The record appropriately carries NCBI's FCB and Bacteroidota/Chlorobiota
clades and Chitinophagia class rather than substituting GTDB's Bacteroidia.

No local child nodes, merged-ID row or dropped-record row were found for
the target. Seven native type-material inventory rows retain alternate
representations of CCTCC AB 2010401, KCTC 23299 and M-8; they do not
represent seven strains.

[LPSN record 790270](https://lpsn.dsmz.de/species/terrimonas-rubra)
confirms the species name, Zhang et al. 2012 authority, ICNP publication
and correct-name status. Its type designations include M-8, CCTCC AB
2010401 and KCTC 23299, with marker JF803808. The raw LPSN inventory
retains KCTC 23299 as its linked designation; that supported designation
is sufficient for the derived type flag. CCTCC is also retained in the
strain's deposit list. The status text and all three booleans match the
complete inventory row at `data/raw/lpsn_names.tsv:27248`.

## Evidence

The raw BacDive row at `data/raw/bacdive_strains.tsv:56076`, complete
native projection at `data/bacdive/records.jsonl.gz:56075`, and
[live BacDive 133766](https://bacdive.dsmz.de/strain/133766) agree on
M-8, taxon 1035890, both deposits and type status.
[KCTC's own 23299 record](https://kctc.kribb.re.kr/en/collection/view?sn=23299)
independently identifies Terrimonas rubra, type status, M-8 and CCTCC AB
2010401. The percent-encoded CCTCC whitespace is correctly preserved.
Both deposit CURIEs satisfy the pinned CAFI authority/accession templates;
all cross-source genome joins here use the complete KCTC 23299 accession,
not the bare M-8 label.

The original description's
[publisher abstract](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.036079-0)
and
[PubMed EFetch for PMID 22199223](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22199223&retmode=xml)
agree on DOI `10.1099/ijs.0.036079-0`, the species proposal and
M-8 = CCTCC AB 2010401 = KCTC 23299 as type-strain designations.
The
[second cited DOI](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.050401-0)
resolves to the 2013 IJSEM notification list for volume 62, part 11.
Its publisher metadata and abstract were inspected; LPSN explicitly
associates that notification with this name. The notification is not a
second experimental characterization. Publisher full-text fragments did
not load, so full methods, figures and the notification table were not
independently inspected.

[GenBank JF803808](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=JF803808)
currently resolves to JF803808.1, a 1,418-base partial 16S rRNA record
explicitly assigned to M-8, taxon 1035890 and type material, citing the
same description DOI and PMID. Complete metadata/features/references
were read, excluding the sequence payload. The YAML correctly keeps the
source's unversioned INSDC accession in nomenclature, outside genome counts.

The GTDB species and mapping rows at `data/raw/gtdb_species.tsv:175486`
and `data/raw/gtdb_mappings.tsv:1445` support one genome and closeMatch.
The complete native genome row at
`data/catalog/gtdb_genomes-0007.jsonl.gz:16693` classifies the
representative `RS_GCF_042686025.1` as Terrimonas rubra and explicitly
supplies KCTC 23299, GCA_042686025.1, SAMN43282323 and PRJNA224116.
The species mapping and genome accession remain distinct concepts.

Assembly provenance was checked as follows:

- BacDive directly supplies unversioned GCA_042686025, description, scaffold
  level and reference 124043. Its live reference identifies automated
  designation/taxonomy matching. The record preserves that source assertion,
  rather than silently appending a version or claiming manual sequencing.
- Native NCBI GenBank and RefSeq rows at
  `data/catalog/ncbi_genbank-0039.jsonl.gz:5988` and
  `data/catalog/ncbi_refseq-0006.jsonl.gz:31646` explicitly identify
  KCTC 23299, the paired assemblies, sample and their respective projects.
  Both are current type-material assemblies in those rows.
- Live [GenBank assembly data](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_042686025.1/dataset_report)
  and [RefSeq assembly data](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_042686025.1/dataset_report)
  confirm the current accession versions, reciprocal pairing, scaffold level,
  ASM4268602v1 name, KCTC 23299 and SAMN43282323. Pairing is explicit,
  not inferred by swapping GCA/GCF prefixes.
- The complete native BV-BRC row at
  `data/bvbrc/bvbrc-0000.jsonl.gz:3345` and
  [live BV-BRC API record](https://www.bv-brc.org/api/genome/?eq(genome_id,1035890.3)&http_accept=application/json)
  agree on `1035890.3`, KCTC 23299, GCA_042686025.1, SAMN43282323
  and PRJNA595761. The PATRIC suffix is part of its opaque identifier.
- Complete GOLD native organism, project and analysis rows at
  `data/gold/organisms.jsonl.gz:36669`,
  `data/gold/projects.jsonl.gz:634400` and
  `data/gold/analyses.jsonl.gz:457374` establish
  Go0043751 -> Gp0880654 -> Ga0689350. Both organism strain fields
  explicitly supply KCTC 23299. The project supplies sample and BioProject;
  the isolate-genome analysis explicitly supplies IMG 8144085798 and
  GCA_042686025.1. Its direct organism field is empty, but its project
  resolves unambiguously to the organism. The two source-field paths are
  preserved as separate assertions, not duplicate biological genomes.

The [ENA sample record](https://www.ebi.ac.uk/ena/browser/api/xml/SAMN43282323)
agrees with NCBI's sample metadata on taxon, KCTC 23299 and type material.
The native RefSeq/GTDB project PRJNA224116 resolves to the
[RefSeq annotation project](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA224116).
Live Datasets instead presents the submission project PRJNA595761, the
GCM type-strain sequencing project, for both assembly reports.
The YAML preserves these source-specific contexts; neither project is
asserted to be a genome or unique to Terrimonas.

All thirty link assertions exactly match the nonempty fields of their raw
rows in `strain_assemblies.tsv`, `strain_genome_records.tsv` and
`strain_related_records.tsv`. Source field names, reference IDs,
accession versions, culture matches and GOLD chain IDs are retained.

The six attestations match the inventories: NCBI 1 NAME, LPSN 1 NAME,
GTDB 1 GENOME, BacDive 1 STRAIN, GOLD 1 ORGANISM and Madin 20
TRAIT_ASSERTION. These unlike units must not be summed as observations
of one kind. No MediaDive or BactoTraits target rows were found.
The absent medium count is consistent with zero in the BacDive inventory,
not a claim that no cultivation medium exists.

## Completeness

No consequential missing representation was established. The sole
BacDive strain is listed in full. The record does not assert phenotypes,
growth conditions, gene functions or causal mechanisms; those optional
surfaces need not be invented from the literature or Madin count.
iModulonDB is not applicable to the claims in this taxon/strain identity record.

Ignored and hidden files, including compressed text, were included using
`rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`.
Queries covered the numeric taxon ID, scientific name, slug, former name,
culture deposits, marker, assembly, sample, GOLD chain and IMG identifiers,
then the BacDive/LPSN identifiers and BacDive-linked StrainInfo lead.
All 72 matching rows were read in full. Five native `SOURCE.json` files
were parsed separately, and history filenames were checked independently.

Two native catalog hits concern an unrelated Thermoplasmata archaeon:
1035890 is their sequence length, not their taxon ID. Ten StrainInfo
prefix matches are SI-ID255740 through SI-ID255749, not SI-ID25574;
they also supply no matching target deposit. Those search hits are not
additional target evidence and were excluded without reviewing those taxa.

BacDive links to SI-ID25574, but no matching rich source or eligible
deposit path was found in the searched StrainInfo snapshot. Its live
rich-record API returned 404 and its browser view only a JavaScript shell.
That unresolved external cross-reference is not present in this YAML
and cannot supply a StrainInfo sequence join. A name-only SeqCode
catalog entry (21263) likewise does not establish a new NCBI mapping.
No target ATB evidence was found in the searched committed component.
These are bounded findings, not claims about all external databases or
binary source snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, nomenclature, type-strain derivation, mapping,
source counts and all imported links have supporting inspected evidence.
Live access limits do not invalidate the faithfully retained native
source assertions.

## Recommended Edits

None required. Do not edit the generated YAML, replace source-supplied
unversioned accessions, merge repeated provenance paths or promote
SEEDED status based on this review.

For a future source refresh, investigate BacDive's unresolved StrainInfo
cross-reference at its source before adding any link. Any new SI assertion
must have its own eligible deposit and sequence-specific ownership.
Preserve the existing NCBI and other-source assertions independently.

## Follow-up Checks

Recheck GOLD, IMG and GTDB live availability during a later source refresh.
Their web pages were not accessible in this review; full local
source-native rows supplied the inspected evidence. Sequence-level
equivalence across IMG, BV-BRC and NCBI was not inferred or tested.

If source or matching behavior changes, update the owning source adapters
and inventories, add focused regression tests, then use the documented
seed dry-run and canary workflow. Rerun schema and strict validation,
full corpus reproduction and the required QC/publication gates.
Do not treat this individual review as having run those gates.

## Additional Notes

Scope row `curation/seed_scope.tsv:10801`, path-index row 14689 and
the legacy page path agree with the target. The inline history wording
matches the six sources and scope reason. Its 2026-09-13T17:54:04Z
timestamp is the latest raw/ATB/StrainInfo manifest extraction timestamp,
as required by `_seed_timestamp`.

Reviewed on `codex/record-review-extensimonas-20261003` at
`b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target YAML remained
byte-identical. Only this new report was written; source inventories,
scope, generated pages, statuses, history, worktrees and GitHub were
not modified.

