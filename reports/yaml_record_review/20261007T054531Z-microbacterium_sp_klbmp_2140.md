# YAML Record Review: Microbacterium sp. KLBMP 2140

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_klbmp_2140.yaml`
- Started UTC: 2026-10-07T05:42:42Z
- Finished UTC: 2026-10-07T05:45:31Z
- Verdict: pass

## Target

Complete generated `TaxonRecord` for `NCBITaxon:1035590`,
Microbacterium sp. KLBMP 2140: rank `SPECIES`, domain `BACTERIA`,
parent `NCBITaxon:2609290`, genetic code 11, ten root-first ancestors,
`grounding_status: EXACT`, `mapping_status: SEEDED`, and
`strain_count: 0`. One NCBITAXON name attestation and one seed event
are present. Optional synonyms, nomenclature, mappings, strains,
record-level evidence, datasets, discussions, and graphs are absent.

The entire YAML was read and compared unchanged before reporting.
This review writes only this report, not generated data or history.

## Validation

Completed with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`
and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/microbacterium_sp_klbmp_2140.yaml`:
  exit 0, no issues.
- `just validate-strict data/taxa/bacteria/microbacterium_sp_klbmp_2140.yaml --out /private/tmp/mt-strict.tsv`:
  exit 0, one file, zero errors. The actual TSV was read and is header-only.
- Bounded structured comparison of the complete backbone row, all
  ancestors, inventories, index/scope, attestation, and seed wording:
  pass; this is not corpus reproduction.
- Exact target checks of `data/raw/ncbi_type_material.tsv`,
  `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv`:
  no matching rows.

Not run: `just verify-corpus`, `just qc`, full-corpus tests,
`just validate-all`, provenance/site gates, and corpus-wide history
and product checks. No focused substitute is claimed. The record has no
curator-added graph nodes, and no target-specific append-only history
files were found in the bounded ignored-independent search.

## Identity and Grounding

The complete `data/raw/ncbitaxon_taxa.tsv:222118` row agrees with
the taxon ID, label, rank, parent, code, empty synonyms, and snapshot.
The complete native scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31597` agrees and has
no additional unique-name value.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035590&retmode=xml)
confirms label, species rank, bacterial division, parent 2609290,
code 11, and every labeled ancestor.
[Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035590)
confirms the ID, label, rank, and ancestor-ID chain including root 1.
The lineage agrees through Bacillati, Actinomycetota, Actinomycetes,
Micrococcales, Microbacteriaceae, Microbacterium, and unclassified
Microbacterium. No alternate name was returned. The browser endpoint
failed, but both primary API responses were fully inspected.

This is a species-ranked isolate concept eligible under the local scope
rule, not proof of a formally named Microbacterium species.

## Evidence

The NCBITAXON attestation correctly counts one `NAME` and supplies
the exact ID/label and 2026-09-13 snapshot.
`data/taxa/PATHS.tsv:14620` and `curation/seed_scope.tsv:322388`
uniquely identify the slug and scope reason. The embedded seed event
at 2026-09-13T17:54:04Z matches those inputs and is not a review promotion.

Exact-taxonomy nucleotide search returned only
[JF803742.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803742.1).
Complete GenBank metadata excluding sequence bases describe a 1,386-nt
partial 16S rRNA gene, strain KLBMP 2140, taxon 1035590, submitted
11 April 2011 and created/updated 30 May 2011. Its source feature says
rhizosphere and host Taxus chinensis. No culture-collection accession,
BioSample, BioProject, assembly, or isolation locality is supplied.
The submitting institution is not an isolation site; rhizosphere
provenance does not establish endophytism. This is a marker, not a genome.

The sequence's first reference is unpublished and concerns Taxus-associated
actinomycete diversity, bioactivity, and halogenase screening. Its title
does not establish those activities or genes in this particular strain.
The primary abstract for a related
[2016 study, PMID 27373072](https://pubmed.ncbi.nlm.nih.gov/27373072/),
was inspected through PubMed XML after the browser open failed.
It describes cohort-level activities and singles out Streptomyces
KLBMP 2170, not Microbacterium KLBMP 2140. An exact strain/accession link
was not established from the abstract. Full text was not obtained in
the bounded search, so the publication relationship remains unresolved.

An accession search surfaced
[PMID 22158848](https://pubmed.ncbi.nlm.nih.gov/22158848/).
Its complete primary PubMed XML, fetched during the immediately preceding
review and re-inspected here, associates JF803742 with a circovirus-like
agent paper. The freshly inspected
[publisher text](https://journals.asm.org/doi/10.1128/jvi.06469-11)
instead names JF803741 and the separate JF918541-44 range, not JF803742.
The metadata/article discrepancy is retained as an external warning;
it does not support a viral identity or genome for this bacterial record.

## Completeness

The pinned backbone has no children beneath this target. The seven
primary BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits
inventories contain no exact-taxonomy rows. Zero counted strains agrees
with classified BacDive inputs, not a universal absence of cultures.

All additional local candidates were fully read and rejected:

- `data/catalog/ncbi_genbank-0002.jsonl.gz:29371` describes
  GCA_003281565.1, Prochlorococcus sp. AG-347-I22, taxon 2162156.
  The matching number 1035590 is its genome length, not the target taxon.
- `data/catalog/gtdb_genomes-0005.jsonl.gz:4103` describes the same
  unrelated assembly and isolate under a GTDB Prochlorococcus concept.
  Its length fields, not taxon identity, supply the match.
- `data/catalog/allthebacteria.tsv.xz:66235` describes
  Staphylococcus aureus sample SAMEA1035590, run ERR083790,
  analysis ERZ3070765, with metadata-filter failure. The accession
  suffix is a namespace collision.

No applicable exact-target culture-deposit, genome, nomenclature, or
mapping assertion was found in the ignored-independent source search.
Exact Assembly query `txid1035590[Organism:noexp]` returned zero
with a phrase-not-found warning. These bounded results do not prove
global absence of assemblies or deposits.

No mandatory representation was established as missing. Optional
literature evidence and causal graphs need not be invented for this
seeded identity record. Phenotype, habitat, and medium claims belong
to the appropriate sibling repositories.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, lineage, grounding, source count,
strain count, and seeded history are supported within the checks run.
The misleading external association is not a claim made by this record.

## Recommended Edits

None required. Preserve the generated record and its seeded lifecycle.

A future authorized task could resolve the full 2016 article and an
explicit strain/deposit relationship. Durable additions belong in
maintained source inputs and extraction/seeding logic, including
`src/taxonmech/seed.py` where applicable, with tests.
Do not hand-edit YAML, infer activity from a cohort or title, or promote
a marker accession into genome counts.

## Follow-up Checks

Require an explicit KLBMP 2140/accession cross-reference before attaching
strain-specific literature evidence. Verify article-accession links
against sequence features and article text, not association metadata alone.

After a future source refresh, run documented extraction/seeding dry runs,
`just seed-canary NCBITaxon:1035590`, inspect the emitted canary,
repeat both single-record validators, then run `just verify-corpus`,
provenance, tests, history checks, and `just qc`.
No regeneration was performed in this review.

## Additional Notes

Local absence searches included ignored, hidden, and compressed source
content using `rg --no-ignore --hidden -n -z -i` across
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation`, and `history`.

Identifier/full-label/slug and KLBMP-separator searches returned six
lines: three identity/scope rows and the three rejected candidates above.
The separate JF803742 accession/version search returned zero matches.
All candidate native rows were fully read. Both stages also parsed all
five source-component `SOURCE.json` files and independently traversed
history filenames, without matching target metadata/history.
The search does not establish absence elsewhere on disk or the internet.

A fresh structured `kg-microbe-sources imodulondb datasets` listing
returned 28 datasets, none matching Microbacterium. iModulonDB is not
applicable; absence is not negative biological evidence.

No alignment, genome reconstruction, phenotype reassignment, paid
research, source contact, GitHub mutation, lifecycle promotion, or
append-only history creation was performed.

