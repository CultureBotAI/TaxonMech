# YAML Record Review: Haemophilus haemolyticus M19501

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/haemophilus_haemolyticus_m19501.yaml`
- Started UTC: 2026-10-03T13:11:49Z
- Finished UTC: 2026-10-03T13:13:03Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1028803`, Haemophilus haemolyticus
M19501, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:726`.
Grounding is `EXACT`; mapping status is `SEEDED`.

Read the entire 84-line YAML, including ten lineage entries, one GTDB
mapping, three synonyms, one xref, zero BacDive strains, three source
attestations and the seed event. No genome accession, publication or graph
is directly asserted. The principal issue is species/strain equivalence,
not an incorrect NCBI identifier or genome count.

Read-only review: only this report was manually written. No source,
generated YAML, history, status or page was changed. Eukaryota was excluded.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/haemophilus_haemolyticus_m19501.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/haemophilus_haemolyticus_m19501.yaml` | PASS; one file, zero errors. |
| Full identity, lineage and NCBI synonym comparison | PASS; all ten ancestors, label, rank, parent, code and both NCBI synonyms match the raw inventory. |
| Complete BacDive subtree check | PASS; subtree contains only taxon 1028803, with zero classified BacDive strains. |
| Full native GTDB species census | PASS for count: one genome, RS_GCF_000222025.1, taxid 1028803, strain M19501. |
| Complete raw GTDB target comparison | PASS for inventory fidelity: one mapping row, closeMatch, count one. This does not validate species/strain equivalence. |
| `just verify-corpus` | Not run: full-corpus reproduction check, not a focused record validator. |
| `just validate-history` | Not run: ignored-inclusive searches found no standalone target history; strict validation checked the embedded event. |
| Graph and generated products | No graph asserted; graph grounding not applicable. Generated pages and exports were not audited. |

The live GTDB species page did not yield usable text. The complete native
GTDB object and a census of all genome shards supplied snapshot evidence.
Initial NCBI access failures were resolved through linked authority pages.
No publication body or sequence payload was reassessed.

## Identity and Grounding

The inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028803)
and [current taxonomy summary](https://www.ncbi.nlm.nih.gov/taxonomy/1028803)
identify M19501 as a strain. The browser confirms both equivalent-name
variants, lineage and code 11. The retrieved full browser page says strain;
an earlier search excerpt saying no rank was not substituted for that
inspected page.

`data/raw/ncbitaxon_taxa.tsv:219208` matches the target. Read all three
native names at `data/catalog/ncbi_names-0005.jsonl.gz:28264` onward: the
scientific name and two equivalent names, both containing M19501. Those
two NCBI exact synonyms are supported.

GTDB's `s__Haemophilus haemolyticus_G` denotes a species cluster, whereas
this NCBI record denotes a strain beneath species 726. Having only one
sampled genome in the current cluster does not establish that these are
equivalent biological entities. The species-label exact synonym and xref
are unsupported promotions (M1).

## Evidence

**Raw provenance.** `data/raw/gtdb_species.tsv:72327` and
`data/raw/gtdb_mappings.tsv:1241` supply the source species, closeMatch and
count one. `data/raw/madin_taxa.tsv:535` supplies one trait assertion.
`curation/seed_scope.tsv:36102` agrees with the three-source selection and
embedded seed event. The NCBI name count is one; the record does not sum
synonyms as names or turn the Madin count into a specific phenotype.

**Singleton GTDB cluster.** Read the complete native genome object at
`data/catalog/gtdb_genomes-0014.jsonl.gz:4576`. It supplies representative
RS_GCF_000222025.1, strain M19501, target taxid 1028803, NCBI species taxid
726, GCA_000222025.2, SAMN02952884 and PRJNA224116. A structured scan of
every native GTDB genome shard found exactly this one member of the exact
species string. All raw mapping rows for the species were checked: one,
to the target. No additional members or targets were inferred.

The native object distinguishes GTDB order Enterobacterales from NCBI
Pasteurellales. Each is source classification context; the NCBI lineage
must not be overwritten with GTDB's. Representative status is not an
assertion that the species name is a strain alias.

**Genome and related-record context.** Complete native objects inspected:

| Source | Evidence |
| --- | --- |
| `data/catalog/ncbi_genbank-0000.jsonl.gz:3842` | GCA_000222025.2, latest, contig level, 22 contigs, M19501, taxid 1028803/species 726, SAMN02952884, PRJNA66573. |
| `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:1158` | GCA_000222025.1 is suppressed; source not-live date 2012-01-29. Do not collapse accession versions. |
| `data/catalog/ncbi_refseq-0000.jsonl.gz:3306` | GCF_000222025.1 is latest in the snapshot, paired identically to GCA_000222025.2, same sample/strain, project PRJNA224116. |
| `data/bvbrc/bvbrc-0000.jsonl.gz:2992` | Genome 1028803.3, WGS, M19501, GCA_000222025.2, PRJNA66573, SAMN02952884 and AFQO00000000. |
| `data/gold/organisms.jsonl.gz:10574` | Go0012007, taxid 1028803 and M19501; culture-collection field empty. |
| `data/gold/projects.jsonl.gz:10432` | Gp0012007 explicitly links Go0012007, PRJNA66573 and SAMN02952884. |
| `data/gold/analyses.jsonl.gz:7427` | Ga0013834 links Gp0012007, IMG 2529292793 and unversioned GCA_000222025. Keep the source accession unversioned. |

The inspected [BioProject record](https://www.ncbi.nlm.nih.gov/bioproject/66573)
confirms the target taxid and explicitly links GCA_000222025.2 at contig
level to SAMN02952884. Its linked BioSample view confirms strain M19501,
AFQO00000000.1 and PRJNA66573. These are genome/sample/project identities,
not interchangeable taxon identifiers.

The project also names the genome-sequencing publication identified by
PMID 21952546 in assembly metadata. No publication claim or phenotype was
added to the target, and the article body was not used as review evidence.

**Absent GOLD attestation is consistent with its input.** There is no
target count row in `data/raw/gold_organisms.tsv`, even though the native
workbook chain above exists. `docs/HARMONIZATION.md` separates KGX-derived
taxon attestations from native workbook genome joins. The latter require
supported collection-deposit matches; an empty culture field and bare
M19501 designation do not establish one. Do not invent a GOLD taxon count
or BacDive association by conflating these provenance routes.

## Completeness

No required identity, lineage, code or seed-provenance field is missing.
The zero BacDive count agrees with the complete subtree check. It is not
evidence that M19501 lacks a genome. Known native genome accessions are
outside the current BacDive-dependent representation when no supported
strain/deposit join is available.

Ignored-inclusive searches covered identifier, full strain token, scientific
name, slug, exact sample and assembly stem in `history/`, `data/raw/`,
`data/bacdive/`, `data/straininfo/` and `data/atb/`, with decompression where
needed. No target standalone history, native BacDive match, StrainInfo
match or ATB match was found in those bounded locations. No target LPSN
row was found in the raw nomenclature inventory. These are local-source
limits, not a worldwide absence claim.

No gene, regulator, transcriptomic dataset, explicit phenotype or graph is
asserted. iModulonDB is not applicable; its absence from this review is
not negative biological evidence.

## Findings

Blocker: 0. Major: 1. Minor: 0.

**M1 (major): singleton species membership is promoted to exact strain
identity.** Lines 46-49 declare Haemophilus haemolyticus G an exact synonym
of M19501; lines 56-57 add the GTDB species as an equivalent identifier.
The native source supports classification of one representative genome in
a species cluster, not an exact alias for the strain. A singleton sample
does not remove the species/strain scope distinction. This finding does
not allege that the count one is wrong or that other genomes were found.

Maintained owner: `src/taxonmech/seed.py:451` treats closeMatch as identity
without a rank/scope guard; lines 467-469 emit the xref and exact synonym.
The schema's `xrefs` definition permits true equivalences only, and its
`TaxonomyMapping` description scopes closeMatch to the same species.
Imported predicates are carried by `src/taxonmech/extract.py`; the policy
is documented in `docs/HARMONIZATION.md`. Generated YAML is not a manual
fix owner.

## Recommended Edits

1. In a separately authorized change, make GTDB identity promotion in
   `src/taxonmech/seed.py` rank/scope-aware. Remove the unsupported species
   exact synonym and equivalent xref on this strain through regeneration,
   retaining the two NCBI strain aliases and source mapping context.
2. Preserve source-cluster count one. Review the maintained predicate
   policy before assigning a different relationship, and document the
   distinction in `docs/HARMONIZATION.md`; do not guess a relation direction
   or patch raw/generated files manually.
3. Add `tests/test_seed.py` coverage for this singleton strain/species case,
   a multi-member cluster, and a valid same-scope species identity. A fix
   that only checks genome count would miss this target.

## Follow-up Checks

After the maintained fix, run focused seed tests, both target validators,
dry `just seed`, and `just seed-canary NCBITaxon:1028803`. Inspect the actual
result for retained NCBI aliases, preserved count/provenance, and absence of
the broader exact synonym/xref. Run full `just verify-corpus` before
accepting corpus-wide regeneration.

Retry the live GTDB page when accessible. Any future proposal to expose
non-BacDive genome evidence requires an explicit maintained schema/join
design; native accession presence alone cannot authorize a fabricated
strain association.

## Additional Notes

Schema validation does not detect this semantic scope error. The NCBI
grounding itself is sound. No review promotion or curation-history event
was written, and report filename coverage remains separate from a claim
that the full corpus has been reviewed.
