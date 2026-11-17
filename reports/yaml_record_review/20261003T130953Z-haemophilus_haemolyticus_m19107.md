# YAML Record Review: Haemophilus haemolyticus M19107

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/haemophilus_haemolyticus_m19107.yaml`
- Started UTC: 2026-10-03T13:08:29Z
- Finished UTC: 2026-10-03T13:09:53Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1028802`, Haemophilus haemolyticus
M19107, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:726`.
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read the full 66-line YAML: ten lineage entries, two NCBI synonyms, code
11, zero BacDive strains, two source attestations and one embedded seed
event. There is no GTDB mapping, identity xref, nomenclature entry,
publication citation, genome accession or causal graph in the target.

Read-only review. No source, generated YAML, history, status or page was
changed. Only this review report was manually written. Eukaryota was not
reviewed or modified.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/haemophilus_haemolyticus_m19107.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/haemophilus_haemolyticus_m19107.yaml` | PASS; one file, zero errors. |
| Complete identity, lineage and synonym comparison | PASS; identity, parent, code, both synonyms and all ten ancestor objects agree with the raw taxonomy. |
| Complete BacDive subtree membership | PASS; target is its only subtree member and no classified BacDive row falls in that subtree. |
| Raw source scope | PASS; one Madin assertion; no target GTDB mapping, GOLD count or LPSN row in the inspected inventories. |
| Native source checks | Current GenBank, historical GenBank/RefSeq, BV-BRC and the complete relevant GOLD chain were inspected; current GTDB/RefSeq searches found no target match. |
| `just verify-corpus` | Not run: full-corpus reproduction check, not a focused validator. |
| `just validate-history` | Not run: ignored-inclusive identifier/name/slug searches found no standalone target history; strict validation checked the embedded event. |
| Graph and generated products | Graph grounding not applicable; no graph asserted. Generated pages and exports were outside this review. |

Initial NCBI access failures were resolved through linked Taxonomy,
BioSample and BioProject pages. PubMed returned a browser challenge or an
empty result on direct/linked attempts; the publication body was not
verified. No publication is directly asserted in the reviewed YAML, so this
does not block its identity/evidence review. No sequence payload was read.

## Identity and Grounding

The [current NCBI summary](https://ncbi.nlm.nih.gov/taxonomy/1028802)
identifies M19107 as a strain. The inspected
[legacy browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1028802&lvl=3&mode=node)
confirms taxid, scientific name, both equivalent strain names, parent
species, lineage and translation table 11, although its served page still
says `no rank`. The current summary and pinned inventory support `STRAIN`;
the discrepancy does not justify changing the YAML to match the older
surface.

`data/raw/ncbitaxon_taxa.tsv:219207` matches the target. The complete native
name objects at `data/catalog/ncbi_names-0005.jsonl.gz:28261` onward contain
one scientific name and two equivalent names. Both synonyms are specific
to M19107, not species-wide exact synonyms.

Raw and native substring searches also returned unrelated samples,
isolates and assembly names containing the digits 1028802 or M19107.
Those hits were rejected using exact source fields and full names; for
example SAMEA1028802 belongs to Streptococcus pneumoniae and is not this
taxon or its BioSample.

## Evidence

**Asserted counts and provenance.** The NCBI name count is one, not a count
of all synonym strings. `data/raw/madin_taxa.tsv:534` supplies one trait
assertion; the YAML does not turn that count into an unspecified phenotype.
`curation/seed_scope.tsv:57227` agrees with the two-source selection and
embedded seed event dated 2026-09-13T17:54:04Z. The NCBI attestation records
the pinned 2026-09-13 taxonomy snapshot.

**Genome evidence exists outside the linked record.** Complete source
objects were read, including the following distinctions:

| Source object | Checked evidence |
| --- | --- |
| `data/catalog/ncbi_genbank-0000.jsonl.gz:3841` | GCA_000222005.2, latest in the native catalog, taxid 1028802/species 726, strain M19107, SAMN02952883, PRJNA66571, contig-level assembly with 123 contigs. |
| `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:1157` | GCA_000222005.1 is suppressed; its source not-live date is 2012-01-29. Do not merge the two accession versions. |
| `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:1094` | GCF_000222005.1 is suppressed, not-live date 2020-07-29, paired to GCA_000222005.2. Source exclusions report annotation completeness failure and many frameshifted proteins. |
| `data/bvbrc/bvbrc-0000.jsonl.gz:2991` | Genome 1028802.3, WGS, M19107, GCA_000222005.2, SAMN02952883, PRJNA66571 and AFQN00000000. |
| `data/gold/organisms.jsonl.gz:10573` | Go0012006, exact target taxid and strain; culture-collection field empty. |
| `data/gold/projects.jsonl.gz:10431` | Gp0012006 explicitly joins Go0012006 to PRJNA66571 and SAMN02952883. |
| `data/gold/analyses.jsonl.gz:7426` | Ga0013833 joins Gp0012006, names IMG 2529292792 and unversioned GCA_000222005 through its structured GenBank field. |

The GenBank row's historical RefSeq pairing does not make the paired
accession current. Ignored-inclusive, decompressed searches across every
current `ncbi_refseq-*.jsonl.gz` and `gtdb_genomes-*.jsonl.gz` shard found
no target taxid, full strain token, assembly stem or exact BioSample match.
This is bounded snapshot absence, not proof of worldwide source absence.
No specific explanation for GTDB exclusion was inferred.

The [BioSample authority page](https://ncbi.nlm.nih.gov/biosample/SAMN02952883)
confirms strain M19107, AFQN00000000.1 and PRJNA66571. The
[BioProject authority page](https://ncbi.nlm.nih.gov/bioproject/66571)
links GCA_000222005.2 at contig level to the same sample and target taxid.
Its general project background was not interpreted as a phenotype or
clinical property of M19107.

The project lists the genome-sequencing publication also named by PMID
21952546 in GenBank metadata. That relationship was checked at the project
page; the article itself was not read and supplies no additional reviewed
biological claim here.

**Native GOLD coverage is not a KGX attestation.** The source-native
organism/project/analysis chain exists, but no target row is present in
`data/raw/gold_organisms.tsv`. `docs/HARMONIZATION.md` explicitly separates
KGX-derived taxon counts from native workbook genome-link evidence. The
record's absent GOLD count matches its maintained inputs. Moreover, the
native organism has no culture-collection identifier and a bare M19107
designation is not a supported collection-deposit join key.

## Completeness

The asserted identity, lineage, synonyms and provenance are complete for
this seeded record. No consequential required-field omission was found.
No GTDB mapping should be invented from membership of the parent species;
no type-strain nomenclature should be borrowed from another strain.

Zero BacDive strains means no classified BacDive row in this NCBI subtree,
not that M19107 is unsequenced. Under the documented model, genome links
attach to supported BacDive/culture-deposit identities. The known native
genomes do not by themselves authorize a new strain row or a taxonomy/name
join. This is a representation boundary rather than a demonstrated defect
in the current generated record.

Ignored-inclusive identifier, scientific-name, slug, strain-token, sample
and assembly searches covered `history/`, `data/raw/`, `data/bacdive/`,
`data/straininfo/` and `data/atb/`, including compressed records where
present. No target standalone history, BacDive record, StrainInfo match or
ATB match was found in those bounded locations. The native GOLD and genome
objects above were retained as positive source context rather than erased
by the lack of overlap links.

No trait, gene, regulator, transcriptomic dataset, publication claim or
causal graph is asserted in the YAML. iModulonDB and graph checks are not
applicable; no negative biological inference follows from that scope.

## Findings

None found. Blocker: 0. Major: 0. Minor: 0.

The pass applies to the reviewed record and its current model contract,
with the validation/source-access limits above. It is not full-corpus
reproduction certification or proof that every possible source is exposed
in the YAML.

## Recommended Edits

None required by this review. Preserve the generated record unchanged.

A separately authorized effort to expose non-BacDive genome evidence or
native GOLD taxon coverage would belong in the maintained extractor,
seeder, schema and harmonization policy with tests, not a manual edit to
this YAML. Such a change must retain accession versions, suppression
statuses and provenance-specific attestation semantics.

## Follow-up Checks

Run full `just verify-corpus` for a corpus-wide reproduction claim. On a
future source refresh, recheck current/historical assembly status, exact
strain/sample matches and source selection before adding any genome link.
Repeat both focused validators and inspect a dry-run/canary if an authorized
upstream change affects this target.

Retrieve the publication through an available primary endpoint only if
future curation needs claims beyond the inspected identity/genome metadata.
The current YAML does not require an invented phenotype or mechanism.

## Additional Notes

The record stays `SEEDED`; no human-review status or audit event was added.
The entire target was inspected, not sampled. Search false positives were
disambiguated by structured identifiers rather than counted as support.
Report presence is tracked separately from full-corpus review completion.
