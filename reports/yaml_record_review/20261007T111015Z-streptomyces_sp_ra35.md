# YAML Record Review: Streptomyces sp. RA35

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_ra35.yaml`
- Started UTC: 2026-10-07T11:05:32Z
- Finished UTC: 2026-10-07T11:10:15Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read: `NCBITaxon:1035877`,
`Streptomyces sp. RA35`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2593676` (unclassified Streptomyces). It has ten root-first
lineage entries, genetic code 11, `EXACT` grounding, `SEEDED` mapping
status, `strain_count: 0`, one NCBI name attestation, and one seed event.
It makes no phenotype, genome, gene-function, formal-nomenclature, or
causal-graph assertion.

The maintained source owners are the extraction and seeding transforms,
`src/taxonmech/extract.py` and `src/taxonmech/seed.py`, with scope recorded
in `curation/seed_scope.tsv`. The generated YAML is not a direct curation
target. No maintained inputs were changed.

## Validation

- `just validate data/taxa/bacteria/streptomyces_sp_ra35.yaml`: passed,
  exit 0, no schema issues.
- `just validate-strict data/taxa/bacteria/streptomyces_sp_ra35.yaml --out /private/tmp/strepRa35-strict.tsv`:
  passed, one file, zero errors; the output TSV contained only its header.
  Both focused commands used the existing environment with offline uv
  resolution and a temporary cache.
- Structured source comparison: the complete backbone row, all ten lineage
  entries, synonyms, parent, code, attestation, PATHS entry, and scope row
  agree. This is a bounded source check, not full-corpus reproduction.
- Live NCBI taxonomy EFetch and Datasets responses agree with the record's
  identifier, name, rank, parent, code, and lineage.
- OAK graph-term validation: not applicable; there is no curator graph.
  Carried NCBI lineage identifiers were checked against NCBI, not treated
  as a curator graph.
- External-history validation: not applicable to this target. The bounded
  ignored-inclusive history searches described below found no target
  artifact. The inline seed event was checked against source provenance.
- Not checked: full-corpus `verify-corpus`, QC, tests, provenance, rendered
  pages, docs, and vendored-sync gates. No focused replacement for those
  repository-wide gates is claimed.
- The target was byte-for-byte unchanged immediately before report creation.

## Identity and Grounding

The pinned row `data/raw/ncbitaxon_taxa.tsv:222180` and native name row
`data/catalog/ncbi_names-0005.jsonl.gz:31669` identify this exact node.
There are no source synonyms to carry. The live
[NCBI taxonomy record](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1035877)
also uses species rank despite the isolate-style label. Keeping
`SPECIES` is faithful to NCBI; it does not assert a validly published
species name. `EXACT` means the record matches this NCBI node.

The exact-target sequence
[AB634831.1](https://www.ncbi.nlm.nih.gov/nuccore/AB634831.1)
provides a 1,513-base partial 16S rRNA sequence, strain qualifier
`RA35`, taxon cross-reference `1035877`, and sample country Egypt.
Both sequence ends are partial. Its May 2011 submission and publication
reference distinguish this evidence trail from other uses of RA35.
The Saudi Arabian submission contact is not the sample country.

A separate primary
[2002 polyketide study](https://journals.asm.org/doi/10.1128/aem.68.9.4472-4479.2002)
uses RA35 in a European-soil isolate cohort and compares it with AUSA69.
Its inspected main text does not establish a connection to this
Egypt-linked accession. That is an unlinked same-name candidate, not
permission to transfer ketosynthase, biosynthesis, or culture claims.
This review does not claim to resolve whether the two designations
could have a relationship beyond the evidence inspected.

## Evidence

### Pinned record claims

- `data/raw/ncbitaxon_taxa.tsv:222180`: exact name, species rank, parent,
  genetic code 11, empty synonym lists, and snapshot 2026-09-13.
  Every root-first lineage entry matches the pinned backbone.
- `data/taxa/PATHS.tsv:14679`: identifier and exact lowercase filename stem.
- `curation/seed_scope.tsv:322441`: inclusion dated 2026-09-13, with one
  attesting source including NCBI.
- The sole attestation is correctly scoped to NCBI, source ID
  `NCBITaxon:1035877`, one assertion, unit `NAME`. It is not a genome
  or strain count.
- The seed event at `2026-09-13T17:54:04Z` is consistent with the inspected
  inventory manifests and latest contributing seeding snapshot timestamp.
  Its generic mention of inventory directories does not assert that this
  target has a match in every inventory.

### External corroboration and limits

Full source-feature and reference metadata for AB634831.1 were inspected;
sequence payload was not analyzed. The sequence cites
[PMID 22435113](https://pubmed.ncbi.nlm.nih.gov/22435113/) and
[DOI 10.1002/jobm.201100133](https://onlinelibrary.wiley.com/doi/abs/10.1002/jobm.201100133).
The citation, title, authors, and journal agree between NCBI sequence
metadata and PubMed. The study concerns isolates from roadside soil and
phylloplane samples in Sohag, Egypt.

Only the abstract and citation metadata of that study were available for
this review, not its full strain-level tables. The abstract describes
cohort susceptibility measurements and selects Pseudomonas aeruginosa
RA65 for plasmid work. Those are not exact RA35 measurements or a RA35
plasmid mechanism. No MIC, source compartment, plasmid, or remediation
performance is assigned to the target.

The exact-taxid NCBI searches returned one Nuccore item, UID
`334278928`, and zero Assembly items. The Assembly response also reported
the exact organism query as not found. This is a bounded current index
result, not proof that no genome exists under another label or taxon.
No BioSample, BioProject, assembly, or culture-deposit identifier was
present in the inspected sequence metadata.

iModulonDB is not applicable to the assertions in this record: no gene,
regulator, trait, or transcriptomics claim is present. No cross-strain
expression-module evidence was substituted.

## Completeness

No required representation was found missing for the current, narrowly
scoped seeded record. `strain_count: 0` is the BacDive-derived count,
not a claim that the named isolate does not exist.

All seven applicable raw enrichment inventories were searched by exact
taxon identifier: BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and
BactoTraits. No target rows were found. The backbone has no direct
children for the target. Exact rows in the type-material, merged-ID,
and dropped-record inventories also yielded no target entries.

The local candidate searches included ignored and hidden files and
compressed catalogs, using `rg --no-ignore --hidden -n -z -i` over
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation`, and `history`. Patterns covered the bounded taxid, RA35
label variants, exact slug, and then AB634831 and sequence UID 334278928.
The expanded search returned the same four rows, all fully inspected.

Three rows support this target: scope, backbone, and native NCBI name.
The fourth, `data/catalog/allthebacteria.tsv.xz:547118`, is an unrelated
Staphylococcus aureus entry whose run is `ERR1035877`, sample
`SAMEA3323178`, and assembly `ERZ3253878`. The numeric substring is
not taxonomic identity and cannot justify a genome join.

The five source metadata JSON files for BacDive, BV-BRC, GOLD, SeqCode,
and StrainInfo were separately parsed in full without a target match.
Ignored-independent history filename and content searches found no
matching target history artifact. These absence statements are limited
to the named local inventories and searches, not all external databases.

Optional synonyms, nomenclature, GTDB mappings, strain lists, genome
links, phenotype evidence, and graphs are appropriately unpopulated.
The external partial 16S sequence is not a whole genome and supplies
neither a BacDive owner nor a culture-deposit chain required for a
strain-linked genome import.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current record's assertions. The verdict does not
certify an inferred phenotype, a named species, the unrelated RA35
polyketide isolate, or comprehensive external genome absence.

## Recommended Edits

None required. Leave the generated YAML and seed history unchanged.

Future enrichment would require explicit target-level evidence first.
For a genome, establish a qualifying BacDive/culture-deposit ownership
chain and preserve accession scope and version. For phenotype or
isolation details, inspect the exact RA35 row and methods in the linked
study. Trace any supported addition through the maintained extraction
and seeding inputs, rather than directly editing the generated record.

## Follow-up Checks

- If new exact-target evidence becomes available, resolve its accession,
  taxon, strain designation, deposit chain, and provenance before joining.
  The 2002 RA35 name alone is insufficient.
- After a separately authorized maintained-input change, rerun the
  applicable extraction/seeding workflow and both focused validators.
  Then run the relevant documented full-corpus consistency gates.
- No blocking follow-up remains for the assertions currently present.

## Additional Notes

This was an individual read-only review. One timestamped report was
created; no YAML, status, history, generated pages, source inventory,
GitHub object, or worktree was changed. The parallel session is closed,
and existing worktrees were left untouched.

Primary literature access was bounded: the exact-linked 2012 article
was abstract-only, whereas the 2002 namesake paper's publisher main
text was inspected. Neither gap warrants inventing optional claims.
Live-source checks describe retrieval during this review; the YAML's
2026-09-13 source snapshot remains explicit.
