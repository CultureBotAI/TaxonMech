# YAML Record Review: Campylobacter molothri

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_molothri.yaml`
- Started UTC: 2026-10-03T21:36:27Z
- Finished UTC: 2026-10-03T21:40:35Z
- Verdict: needs curation

## Target

Read all 220 lines of the generated `TaxonRecord`, `NCBITaxon:1032242`,
Campylobacter molothri, rank `SPECIES`, domain `BACTERIA`, grounding
`EXACT`, mapping status `SEEDED`. The target is the species, not the
RM10537 type strain alone. Its one BacDive strain has two culture deposits
and a supported type-strain flag, but no assembly, genome or related-record
assertions.

This read-only review changes no generated YAML, source inventory, scope,
history, status or earlier report. The completeness finding concerns
evidence acquisition and representation, not an incorrect taxon identity
or permission to relax automated identity matching.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/campylobacter_molothri.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/campylobacter_molothri.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured source comparisons | Identity, complete lineage, path, scope, source counts and embedded seed-event reason agree with the committed inventories. |
| Strain-link inventory comparisons | Exact full-field multisets match: zero assembly, zero non-ATB genome and zero related assertions in the raw and StrainInfo link inventories for this strain. |
| Embedded history | Strict validation passed; the six-source seed event remains consistent with the scope reason. |
| Standalone history | Not applicable: an identifier, label and slug search under `history/`, including ignored and hidden files, found no target entry. |
| Graph and ontology-product gates | Not applicable: the complete record contains no causal graph or curator-added ontology-product assertions. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports, sequence alignment or FASTA
checksum replay. Focused comparisons do not prove corpus reproduction.
No generator or history writer was run. Passing schema validation does not
resolve the missing genome representation below.

## Identity and Grounding

The primary identifier, species label, parent `NCBITaxon:194`, genetic code
11 and all nine root-first lineage entries match
`data/raw/ncbitaxon_taxa.tsv:220800`. Live NCBI EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032242)
corroborate them. Native names are in
`data/catalog/ncbi_names-0005.jsonl.gz` rows 30039-30072. The authority and
32 `includes` names are correctly represented as related synonyms, not
equivalent strains. A complete backbone scan found no children.

`data/taxa/PATHS.tsv:13162` and `curation/seed_scope.tsv:21534` agree.
The older five-source scope reason is preserved as historical scope
provenance; the current seed event lists six sources. The merged-ID
inventory retains 31 redirects into this species, including
NCBITaxon:2735753-2735780 and NCBITaxon:3233410-3233412. These are source
redirects, not evidence that all included isolates are the type strain.

[LPSN name 57801](https://lpsn.dsmz.de/species/campylobacter-molothri)
agrees on Miller et al. 2025, species rank, valid publication and correct-name
status. Its linked collection deposits are CCUG 75331 and LMG 32306;
the page additionally names RM 10537. `data/raw/lpsn_names.tsv:9189`
supports every carried nomenclatural field, publication and marker.
The two carried deposits validate under the pinned CAFI templates.
The missing bare laboratory designation is not a license to create a new
collection authority or genome-join key.

## Evidence

- **Type strain:** `data/raw/bacdive_strains.tsv:99687`, native
  `data/bacdive/records.jsonl.gz:99686` and the inspected
  [BacDive 177463 page](https://bacdive.dsmz.de/strain/177463) support the
  species classification and both deposits. Both intersect the local LPSN
  type-designation set, justifying `is_type_strain: true`. The native
  compact record has no designation or genome section and retains only
  MW131400 in its sequence section. NCBI type-material rows 1571-1582
  independently retain the deposits and RM10537 designations.
- **Original publication:** PMID:39913296 resolves through NCBI EFetch to
  DOI:10.1099/ijsem.0.006635 and PMC11801493. The publisher abstract and
  [open full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11801493/fullTextXML)
  were inspected. The species description explicitly equates RM10537 with
  LMG 32306 and CCUG 75331 and assigns chromosome accession CP059597 and
  marker MW131400 to the type strain. The genome section describes its
  complete chromosome and small plasmid. This is explicit strain-specific
  evidence, not a join based on a shared taxon or similar name.
- **Notification reference:** DOI:10.1099/ijsem.0.006728 resolves to the
  [Oren and Goker notification list](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.006728),
  published May 30, 2025. Its bibliographic identity and the LPSN citation
  were verified; the dynamically delivered full notification table was
  unavailable and was not used as independently inspected species evidence.
- **Marker:** Live NCBI Nuccore identifies MW131400.1 as a 1,501-base
  partial 16S rRNA sequence from RM10537, taxon 1032242, with type-material
  annotation. The unversioned `INSDC:MW131400` accurately preserves LPSN's
  accession. It is not a genome assembly.
- **Collection corroboration:** The inspected
  [CCUG 75331 page](https://www.ccug.se/strain?id=75331) lists RM 10537 and
  LMG 32306 as other designations, independently supporting the deposit
  identity. It also lists MW139755 and MW139813 as additional markers;
  those two accessions were not independently revalidated and are only
  follow-up leads, not evidence imported by this review.
- **GTDB mapping:** `data/raw/gtdb_mappings.tsv:1342` and
  `data/raw/gtdb_species.tsv:40520` support the carried closeMatch and count
  44. A full native GTDB scan found exactly 44 members of
  `s__Campylobacter_D molothri`: 34 classified by NCBI as 1032242 and ten
  as 3239825, Campylobacter sp. LH-2024. The representative is the RM10537
  type-strain assembly, `RS_GCF_022369435.1`, in shard 0016 row 48257.
  The species-level correspondence is defensible here; unlike a mapping
  on a strain record, it does not promote the species to one isolate's
  identity. The count means the entire GTDB cluster, not 44 type-strain
  genomes or 44 NCBI-1032242 genomes. Do not reconcile NCBI's hierarchy
  with GTDB's differing genus/class labels. The live GTDB tree page was
  unavailable; the complete native catalog supplied the count check.
- **Other attestations:** GOLD count one matches
  `data/raw/gold_organisms.tsv:419`; Madin count four matches
  `data/raw/madin_taxa.tsv:604`. They count source organisms and trait
  assertions respectively, not genomes, experiments or verified phenotypes.
  Full corresponding raw-table scans found no MediaDive or BactoTraits
  attestation. The BacDive strain count of one is uncapped and matches the
  complete inventory for this childless species.
- **Structured adapter:** The available `kg-microbe-sources imodulondb
  datasets` runner returned 28 dataset keys, none for Campylobacter.
  iModulonDB is not applicable; that absence is not negative biological
  evidence and no other organism's expression modules were transferred.

## Completeness

The following independently inspected native records converge on the
published RM10537 genome, but none supplies either carried culture deposit
in the automated culture-match field:

| Source | Exact record and source context |
| --- | --- |
| NCBI GenBank | `data/catalog/ncbi_genbank-0020.jsonl.gz:34082`: GCA_022369435.1, RM10537, SAMN03737978, PRJNA66815, complete type-material assembly. |
| NCBI RefSeq | `data/catalog/ncbi_refseq-0004.jsonl.gz:5211`: paired GCF_022369435.1, RM10537, same BioSample; native source project PRJNA224116 is preserved as a separate source assertion. |
| GTDB | `data/catalog/gtdb_genomes-0016.jsonl.gz:48257`: RS_GCF_022369435.1, paired GenBank accession, RM10537, same BioSample. |
| BV-BRC | `data/bvbrc/bvbrc-0000.jsonl.gz:3154`: patric:1032242.3 explicitly carries GCA_022369435.1, CP059597/CP059598, SAMN03737978 and PRJNA66815, with strain RM10537 but no culture-collection field. |
| GOLD | Organism row 10413: Go0011835, RM10537, empty culture-collection field. Project row 10271: Gp0011835 explicitly connects that organism, sample and project. Analysis row 458587: Ga0692500 follows Gp0011835 and associates CP059597/CP059598 with GCA_022369435.1; no IMG taxon ID is supplied. |

Live [NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_022369435.1,GCF_022369435.1/dataset_report)
confirms both current paired accessions, assembly ASM2236943v1, RM10537,
taxon 1032242 and the sample/project above. Live Nuccore separately confirms
CP059597.1 as the 1,513,382-base chromosome and CP059598.1 as the
3,526-base pMOL plasmid, both with that strain, sample and project. Do not
confuse these component sequences with two separate genome assemblies.

Gitignore-independent structured scans of 4,111,794 current/historical NCBI
assembly rows, 1,419,549 BV-BRC rows, 901,341 GTDB rows and 531,961 GOLD
organism rows found no whole CAFI-valid match for CCUG-75331 or LMG-32306
in the relevant strain/culture fields. A complete scan of 314,470 native
StrainInfo records found neither own deposit, taxon 1032242 nor SI-ID283921.
BacDive's SI-ID283921 cross-reference also returned HTTP 404 from the live
rich-record API. It is not carried in the YAML and is not a broken YAML
reference; a source cross-reference alone could not authorize a join anyway.

Full raw/StrainInfo link-table scans confirm the empty YAML link sets.
Ignored-inclusive searches of ATB and SI strain-link/exclusion tables found
no target identifier, label, slug or deposit entry. This does not establish
that no ATB assembly exists for RM10537's sample: the record has no eligible
BIOSAMPLE assertion to begin that join, and ATB native sample eligibility
was not assessed. No sample or genome crosslink should be added by name.

Optional definition, general evidence, discussions, causal graphs and
phenotype detail are correctly absent in this seeded identity record.
The paper's other isolates and tested traits are not missing BacDive
entries or mandatory taxon-level phenotype assertions. They must not be
transferred to every strain or converted into extra genomes for RM10537.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - The explicitly documented type-strain genome is not represented.**
The strain entry at YAML lines 172-180 has no genome links, despite the
inspected primary paper's deposit-to-RM10537-to-CP059597 chain and the
independently verified NCBI assembly pair. This is a consequential
completeness gap for the repository's primary strain-to-genome use case.
It is not a seeder omission of an existing eligible inventory row: the
inventories are equally empty, and the current name/deposit guards are
behaving as documented.

The maintained owner is upstream explicit strain-genome evidence consumed
through `src/taxonmech/extract.py:798` and the source-specific importers,
then `data/raw/strain_assemblies.tsv`, `strain_genome_records.tsv` and
`strain_related_records.tsv`; `src/taxonmech/seed.py:519` merely emits those
assertions. Prefer acquiring an explicit, provenance-backed assembly
assertion on BacDive 177463 or an eligible own culture-deposit source.
An alternative would require a separately authorized, maintained
literature-curation input with its own evidence contract. Do not change
`normalize_culture_identifier` to accept bare RM aliases, infer all
species genomes onto the type strain, or manually edit this generated YAML.

## Recommended Edits

1. Resolve M1 through maintained evidence acquisition: retain the paper's
   exact RM10537/LMG32306/CCUG75331 identity assertion, CP059597 component
   reference, and NCBI's GCA/GCF_022369435.1 assembly relationship. An
   upstream BacDive or own-deposit update would let the existing guarded
   importer carry the assembly without introducing name-based joins.
2. After authorized source curation, refresh the appropriate pinned source
   and extraction inputs, then regenerate raw link inventories and this
   record. Keep assembly components, BioSample, BioProject and GOLD IDs
   typed separately. Admit additional database links only when each has
   its own explicit chain; the table above is not permission for a
   cross-product join.
3. Keep the current taxon identity, lineage, nomenclature, related-synonym
   scopes, type flag and GTDB source count. Do not promote `mapping_status`
   or write a curation event merely because this read-only report exists.

## Follow-up Checks

- Confirm the new maintained input explicitly links the same culture
  deposit and assembly, with inspected source provenance. Test that other
  RM isolates, the ten LH-2024 genomes, unrelated collection numbers and
  another deposit's sequences remain unjoined.
- After authorization, follow extraction dry run, `just seed`, and
  `just seed-canary NCBITaxon:1032242`; inspect the generated assertions
  and their source fields. Run the two focused validators above, then
  `just verify-corpus` and `just qc` for any published curation change.
- If an eligible BIOSAMPLE link is introduced, reassess ATB from that
  exact accession and retain same-source-chain evidence for any genome
  crosslinks. No current ATB eligibility claim is made here.
- Revisit the unavailable SI-ID283921 source link and notification table
  only as bounded source checks. Neither justifies inventing a new record
  identity or adding a reference that does not resolve.

## Additional Notes

The full-paper sections concerning type identity, genomic characterization,
species description and accession disclosure were inspected through public
Europe PMC XML after publisher full-text delivery and PMC browser access
failed. Supplementary files were not downloaded; no claim depends on them.
The PMID-to-DOI match was checked in the article's own identifier list,
not in its cited references. Public source reads used no paid provider.

Searches used explicit files, complete structured scans or
`rg --no-ignore --hidden -z`; ignored files were included. Broad numeric
search hits from unrelated culture collections were inspected as leads and
excluded through whole-identifier comparisons. The findings do not claim a
global absence beyond the stated source fields and directories. The only
target-specific curation-directory hits were the existing scope and legacy
page-path rows. Existing reports and completed Eukaryota coverage were left
unchanged.
