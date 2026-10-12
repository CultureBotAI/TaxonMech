# YAML Record Review: Thiomicrospira sp. V2501

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thiomicrospira_sp_v2501.yaml`
- Started UTC: 2026-10-07T05:07:49Z
- Finished UTC: 2026-10-07T05:19:05Z
- Verdict: pass with minor issues

## Target

Complete generated `TaxonRecord` for `NCBITaxon:1035585`, label
`Thiomicrospira sp. V2501`, rank `SPECIES`, domain `BACTERIA`.
The record has `grounding_status: EXACT`, `mapping_status: SEEDED`,
genetic code 11, ten root-first lineage entries, and `strain_count: 0`.
It contains one NCBITAXON name attestation and one seeding event, not a
human-reviewed status. No YAML, inventory, generated page, or history entry
was changed.

## Validation

Commands completed with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`
and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/thiomicrospira_sp_v2501.yaml`:
  exit 0, no issues.
- `just validate-strict data/taxa/bacteria/thiomicrospira_sp_v2501.yaml --out /private/tmp/tv-strict.tsv`:
  exit 0, one file, zero errors. The actual TSV was read and contains only
  its header.
- Read-only structured comparisons of the complete backbone row, all ten
  ancestors, scope row, path index, source attestation, and embedded event:
  agree. These are bounded diagnostics, not corpus reproduction.
- Exact identifier scans of `ncbi_type_material.tsv`,
  `ncbi_merged_ids.tsv`, and `dropped.tsv`: no target rows.

Not run: full-corpus `just verify-corpus`, `just qc`,
`just validate-all`, `just test`, `just provenance-check`,
`just render-check`, and corpus-wide history/product gates. No focused
substitute is claimed. No curator-added graph nodes or target-specific
append-only history files were found within the searches described below.

## Identity and Grounding

The complete pinned backbone row at `data/raw/ncbitaxon_taxa.tsv:222113`
agrees with live [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1035585),
Taxonomy XML, and the Datasets taxonomy response: species-level V2501 under
`NCBITaxon:2643099` (unclassified Thiomicrospira), in Bacteria, genetic
code 11. Datasets includes root 1; the remaining live parent chain matches
the YAML. The record denotes the NCBI species-ranked isolate taxon, not the
genus or an accepted named species inferred from its designation.

The native NCBI scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31592`, path-index row 14615, and
scope row 322383 agree. No NCBI synonyms are supplied. The snapshot date
2026-09-13 and embedded seeding event 2026-09-13T17:54:04Z are consistent
with those inputs.

The [LPSN genus page](https://lpsn.dsmz.de/genus/thiomicrospira) concerns
genus 517438, not an exact V2501 name. Its Beggiatoales placement differs
from NCBI's Thiotrichales; TaxonMech correctly carries NCBI lineage.
Genus synonyms and the genus type species must not be transferred here.
An unpublished GenBank reference mentions the candidate name
Thiomicrospira horonobensis; that does not authorize a renamed record or
an exact synonym. That epithet was not present in the inspected LPSN child
list; this is a page-bounded observation, not a global nomenclature census.

## Evidence

**Culture identity and classification.** Complete native
`data/bacdive/records.jsonl.gz:82727` identifies BacDive 160491 as V2501,
DSM 25470. Its primary classification is taxon 935, while its 16S
accession AB634592 explicitly names taxon 1035585.
The current [BacDive record](https://bacdive.dsmz.de/strain/160491)
agrees; its DOI is `10.13145/bacdive160491.20260601.11`.
The independently inspected [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-25470)
also associates this deposit, designation, and marker.

**Deposit overlay.** Complete native StrainInfo row 295004 and the
[public rich API record](https://api.straininfo.dsmz.de/v2/data/strain/max/397115)
identify SI-ID397115, version DOI `10.60712/SI-ID397115.2`, and its own
non-erroneous DSM 25470 deposit SI-DP903720. Source taxonomy is genus 933.
The native record has no sequence assertions. Local
`strain_links.tsv:59835` and `related_records.tsv.gz:140642-140643`
retain the culture-identifier match and separate strain/deposit identities.

**Marker evidence.** Complete GenBank metadata, excluding sequence bases
and protein residues, were read for
[AB634592.1](https://www.ncbi.nlm.nih.gov/nuccore/AB634592.1) and
[AB634593.1](https://www.ncbi.nlm.nih.gov/nuccore/AB634593.1).
Both explicitly identify strain V2501 and taxon 1035585. They are,
respectively, a 1,492-nt partial 16S sequence and a 778-nt partial
`cbbL-2` sequence with protein accession BAK26807.1, not genome assemblies.
Neither inspected source feature provides a culture-collection qualifier.
The latter records collection in Mar-2010.

**Published genome versus public identifiers.**
[Ueno et al. 2024, DOI 10.1128/mra.00108-24, PMID 39436068](https://journals.asm.org/doi/10.1128/mra.00108-24)
reports a 2,240,851-bp single circular assembly and chemolithoautotrophic
growth for V2501. Its data-availability section supplies marker, run,
sample, and project identifiers, not a GCA/GCF or chromosome accession.
The visually inspected figure labels V2501 with DRR522933. The paper's
reported assembly is not evidence that this run identifier is an assembly.

The complete [ENA run XML](https://www.ebi.ac.uk/ena/browser/api/xml/DRR522933)
and [experiment XML](https://www.ebi.ac.uk/ena/browser/api/xml/DRX506819)
connect public DRR522933 through DRX506819 to DRS356359/SAMD00726318 and
DRP010985/PRJDB17264. The experiment is WGS, GENOMIC, PacBio; it does not
identify a culture deposit. The exact-taxonomy BioSample search returned
two complete records:
[SAMD00726318](https://www.ncbi.nlm.nih.gov/biosample/39273265) and
[SAMN43358926](https://www.ncbi.nlm.nih.gov/biosample/43358926).
Both explicitly identify taxon 1035585 and strain V2501, with cultured
MIGS packages and collection date 2009-12-15. Their XML links PRJDB17264.
Do not equate two sample accessions or infer deposit identity solely from
shared strain wording.

[PRJDB17264](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJDB17264)
uses taxon 935 and environmental/metagenomic project classifications,
unlike the cultured samples and GENOMIC experiment. The separately inspected
[genome project PRJNA1152272](https://www.ncbi.nlm.nih.gov/bioproject/1152272)
uses taxon 1035585 but reported no linked public sequence data.
These source differences remain unresolved; neither changes this YAML.

## Completeness

The zero count follows the maintained importer, not biological absence of
a culture. `src/taxonmech/bacdive_v2.py:56` classifies from
`General.NCBI tax id`, not marker taxonomy.
`src/taxonmech/seed.py:483` collects only that taxon's strains and
descendants. Taxa 935 and 1035585 are siblings, not ancestor and descendant.
The complete sibling `data/taxa/bacteria/thiomicrospira_sp.yaml` was read:
it already retains this deposit and its StrainInfo links. This was a
placement check, not a full independent review of that sibling.

Exact NCBI Assembly search `txid1035585[Organism:noexp]` returned zero,
with a phrase-not-found warning; the corresponding genome Datasets response
was empty. An additional Assembly query for V2501, SAMD00726318,
PRJDB17264, or PRJNA1152272 also returned zero with phrase warnings.
A resolvable public assembled-sequence identifier was not established by
these bounded checks. This does not refute the published assembly or prove
global absence.

The full ATB native row at `data/catalog/allthebacteria.tsv.xz:43422`
does contain SAMD00726318, but has `NOT_PROCESSED`,
`asm_fasta_on_osf: 0`, and no assembly, run, checksum, or download.
It cannot supply an eligible genome link. Sample/project/run identifiers
and partial markers must remain outside genome counts.

No additional exact-taxonomy rows appeared in the seven primary BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories. The culture
matches above are explicitly preserved despite their different taxonomies.
No required synonym, exact nomenclature, GTDB mapping, causal graph, or
phenotype assertion was established as omitted. Optional fields should not
be populated by transferring genus or adjacent-taxon facts.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. **Minor: unresolved culture-to-taxon provenance gap.** The corroborated
   deposit-to-marker path reaches this exact taxon, but primary source
   classification files the culture under sibling 935. Consequently,
   someone inspecting only this record cannot follow that culture path.
   This is a non-blocking source reconciliation/traceability issue, not an
   incorrect generated count or a demonstrated seeder defect.
   Future ownership is the BacDive primary assertion and its maintained
   adapter `src/taxonmech/bacdive_v2.py`, with placement in
   `src/taxonmech/seed.py`. Do not override primary taxonomy automatically
   from a marker or patch generated records.

## Recommended Edits

No immediate YAML edits. Retain current identity, lineage, and source counts
while the primary classification discrepancy is unresolved.

A later authorized curation task should first establish whether the primary
source classification should change. If corrected upstream, refresh through
the maintained source/extraction pipeline; if a separate source-conflict
representation is desired, design and test that explicitly before changing
the adapter or seeder. Do not silently reclassify the deposit or manufacture
an assembly identifier.

Resolve assembled-sequence accessibility and the Mar-2010 versus 2009-12-15
collection dates as separate source questions. This review does not invent
an explanation or treat either as a false YAML claim.

## Follow-up Checks

After an authorized source or implementation change, add a focused regression
test preserving the distinction between primary classification, marker
taxonomy, matched deposits, raw reads, and eligible assemblies. Exercise
both sibling placements and verify that strain counts remain deduplicated.

Follow the documented extraction dry run, source refresh and overlay rebuild,
then `just seed` and `just seed-canary NCBITaxon:1035585`; inspect the
canary and affected sibling before broader generation. Repeat the two
record validators and run `just verify-corpus`, provenance, tests, history,
and the full `just qc` gates. None of these mutating steps was performed.

For genome follow-up, require a resolvable assembled-sequence accession and
an explicit source-supported culture path. A paper figure, BioSample match,
or raw sequencing run alone does not prove assembly equivalence.

## Additional Notes

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i`
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation`, and `history`. Compressed and ignored content was included.
Separate structured scans read all five source-component `SOURCE.json`
files completely, and an ignored-independent history filename traversal
was performed. Generated pages and report prose were not substitutes for
these source searches.

Search stages covered identifier 1035585, full label, slug, V2501 separator
variants; then DSM 25470, BacDive 160491, AB634592 and SI identifiers; then
AB634593, the run/experiment/study/submission IDs above, both BioProjects,
SAMD00726318, and the candidate epithet. The second BioSample,
SAMN43358926, was searched separately: no local content or metadata/history
filename matches in those bounds. Every candidate native row was read in
full, not judged from a projected search snippet.

Numeric/accession collisions were excluded after full-row inspection:
ATB SAMEA1035585 (Staphylococcus aureus), SRR1035585 (Salmonella), and
DRR356359 (Streptococcus pneumoniae, not the target's DRS356359).
The final archive search used exact accession namespaces.

The fresh structured `kg-microbe-sources imodulondb datasets` listing
contained 28 datasets and no matching target organism. iModulonDB was not
applicable; this is not negative phenotype evidence.

The DSMZ page contained a mismatched footer link label; following its URL
resolved to the correct BacDive record. No identity was inferred from that
label. Intermittent browser failures were supplemented by successful
primary-page reads and structured API responses. No genome FASTA/raw-read
reassembly, paid research, source contact, GitHub mutation, lifecycle
promotion, or append-only curation history was performed.

