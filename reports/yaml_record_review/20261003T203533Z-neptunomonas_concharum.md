# YAML Record Review: Neptunomonas concharum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/neptunomonas_concharum.yaml`
- Started UTC: 2026-10-03T20:33:07Z
- Finished UTC: 2026-10-03T20:35:33Z
- Verdict: pass with minor issues

## Target

Reviewed all 723 lines of this generated `TaxonRecord`: `NCBITaxon:1031538`,
Neptunomonas concharum, rank `SPECIES`, domain `BACTERIA`, grounding `EXACT`,
mapping status `SEEDED`. One BacDive strain carries thirteen assembly
assertions, twelve genome-record assertions and 32 related-record assertions.
These are source assertions, not distinct biological genome counts.

Maintained ownership lies in the source inventories and their extraction/
seeding transforms. The YAML is generated and remains read-only. The only
review artifacts are this report and the standard validator diagnostic.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/neptunomonas_concharum.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/neptunomonas_concharum.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured comparisons | Exact backbone and nine-entry lineage match; source counts and seed reason verified; full-field multiset equality for all 13/12/32 assertions against raw inventories and the empty target StrainInfo overlay. |
| Culture-identifier checks | All three inventoried deposits normalize under the pinned authority/template policy; compact `JCM17730` and bare `LHW37` correctly do not. |
| Embedded history | Strict validation passed; seed event agrees with the inventory and seed-scope reason. |
| Standalone history | Not applicable: identifier, label and slug searches including ignored/hidden files found no target history under `history/`. |
| Causal graph and ontology-product gates | Not applicable: no causal graph in the complete YAML. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports and FASTA replay. The focused
checks do not replace those gates. No generator, history writer or status
promotion was run.

## Identity and Grounding

The identifier, label, parent `NCBITaxon:75687`, species rank, genetic code
11, two related names and root-first lineage match
`data/raw/ncbitaxon_taxa.tsv:220743`. Live taxonomy EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1031538)
confirm them. The full local backbone scan finds no child taxa.
`data/taxa/PATHS.tsv:13069` and `curation/seed_scope.tsv:10789` agree with
the identifier and slug. Native NCBI name rows 29906-29908 in
`data/catalog/ncbi_names-0005.jsonl.gz` support the scientific name,
authority and includes-name; the latter two are not promoted to exact synonyms.

The inspected [LPSN page](https://lpsn.dsmz.de/species/neptunomonas-concharum)
supports identifier 790300, authority Lee et al. 2012, valid publication,
correct-name status, JF748732 and the JCM type deposit. The raw row at
`data/raw/lpsn_names.tsv:27278` agrees with the generated nomenclature,
but both omit the additional registered KACC type deposit; see N1.

GTDB mapping row `data/raw/gtdb_mappings.tsv:1307` supplies the supported
species identifier, `skos:closeMatch` and count two. Both native members
are type-material assemblies of this species. GTDB places the genus in
Pseudomonadales/Balneatricaceae, whereas NCBI uses
Oceanospirillales/Oceanospirillaceae. The source-specific NCBI lineage is
correctly preserved rather than reconciled by the seeder.

## Evidence

- **Strain identity:** `data/raw/bacdive_strains.tsv:56098`, native
  `data/bacdive/records.jsonl.gz:56097` and the inspected
  [BacDive record](https://bacdive.dsmz.de/strain/133788) support LHW37,
  JCM 17730, KACC 15543, BCRC 81037 and type-strain status. Raw culture
  inventory rows 10538, 103251 and 113321 corroborate the three deposits.
  The one-medium count is a raw strain-level count, not a direct species
  MediaDive attestation.
- **Direct BacDive genome provenance:** Reference 67770 supplies scaffold
  assembly GCA_006148955, PATRIC 1031538.3 and IMG 8065619331. Reference
  66792 separately supplies complete assembly GCA_008630635, PATRIC
  1031538.4 and IMG 2989281803. These source-specific references and
  unversioned assembly identifiers are preserved without conflating the
  two sequencing efforts.
- **BV-BRC:** Native `data/bvbrc/bvbrc-0000.jsonl.gz:3066` supports the
  scaffold assembly through both `JCM 17730` and `JCM:17730` fields.
  Row 3067 supports the complete assembly through its valid culture field
  `JCM:17730`; its separate strain spelling `JCM17730` is not a join key.
  The records supply their own samples/projects, not cross-products.
- **GOLD:** Native organism rows 37282 and 407549, project rows 403185 and
  400359, and analysis rows 315157 and 313767 in `data/gold/` establish two
  complete chains. Go0044448 -> Gp0549420 -> Ga0487756 supplies
  GCA_006148955.1, IMG 8065619331, PRJNA542572 and SAMN11633701.
  Go0572076 -> Gp0546580 -> Ga0486355 supplies GCA_008630635.1,
  IMG 2989281803, PRJNA563618 and SAMN12684172. Both eligible organism
  fields explicitly identify the JCM deposit.
- **NCBI assemblies:** Native GenBank
  `data/catalog/ncbi_genbank-0005.jsonl.gz:6089` and
  `ncbi_genbank-0007.jsonl.gz:26936`, plus RefSeq rows 22576 and 30779 in
  `ncbi_refseq-0002.jsonl.gz`, support both current GCA/GCF pairs. Live
  [NCBI genome reports](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_006148955.1,GCA_008630635.1/dataset_report)
  independently confirm type material, scaffold versus complete levels,
  assembly names, samples, projects and explicit BioSample culture fields.
  GenBank projects remain separate from RefSeq's PRJNA224116.
- **GTDB members:** Native
  `data/catalog/gtdb_genomes-0002.jsonl.gz:28690` identifies
  RS_GCF_006148955.1 with eligible `JCM 17730` metadata. Native
  `gtdb_genomes-0017.jsonl.gz:20288` identifies representative
  RS_GCF_008630635.1 with compact `JCM17730`, which does not meet the
  cross-source join policy. The complete native name/cluster search finds
  these two members, supporting the species-level count without implying
  both have eligible GTDB strain links.
- **Inventory fidelity:** Raw assembly rows 32154-32166, genome-record
  rows 25341-25352 and related-record rows 86807-86838 match all fields
  in the YAML. Multiple source-field assertions remain distinct provenance,
  not extra strains or genome identities.
- **Literature:** The full abstract of
  [PubMed 22199221](https://pubmed.ncbi.nlm.nih.gov/22199221/) and
  [Crossref metadata](https://api.crossref.org/works/10.1099/ijs.0.037473-0)
  verify the species description and DOI. The abstract explicitly identifies
  LHW37 = KACC 15543 = JCM 17730. The second DOI resolves to the expected
  [notification list](https://api.crossref.org/works/10.1099/ijs.0.050401-0),
  volume 63, pages 399-400, published in 2013. This notification does not
  change the original 2012 authority. Full articles were not read.
- **Marker:** Inspected [JF748732.1](https://www.ncbi.nlm.nih.gov/nuccore/JF748732.1)
  metadata confirm a 1,472-base partial 16S sequence from LHW37, taxon
  1031538, with explicit type-material annotation. The record preserves the
  source's unversioned accession. No sequence alignment was performed.
- **Attestations:** Complete source inventory scans corroborate NCBI NAME
  1, LPSN NAME 1, GTDB GENOME 2, BacDive STRAIN 1, GOLD ORGANISM 2 and
  MADIN TRAIT_ASSERTION 5. No direct MediaDive or BactoTraits target row
  was found in those complete inventories. Counts alone are not biological
  phenotype assertions.
- **iModulonDB:** The resolved `culturebotai-claw/.venv/bin/kg-microbe-sources
  imodulondb datasets` adapter returned 28 keys, none covering Neptunomonas.
  No organism-matched query applies; that absence is not negative evidence
  about the organism or its marker.

## Completeness

The one-strain listing is complete for the local species subtree, not capped.
Ignored-inclusive compressed searches covered native catalog, BacDive,
BV-BRC, GOLD, SeqCode and StrainInfo snapshots using current name, historical
includes-name, whole deposit identifiers and typed taxon identity. Complete
structured target scans covered raw source inventories, type material,
merged IDs and dropped rows. No additional eligible deposit-backed genome
association was identified within those boundaries.

The absent NCBI and GTDB source assertions for GCA/GCF_008630635.1 are
consistent with the existing source-field contract: native assembly
`infraspecific_name` and GTDB `ncbi_strain_identifiers` use `JCM17730`,
which the pinned normalizer rejects because it lacks a separator. This
does not imply that the genome is unavailable or wrongly assigned.
BacDive, GOLD and BV-BRC independently support the complete assembly
already present. The live BioSample's eligible culture field would require
a separately maintained source ingestion path, not silently rewriting the
record's existing provenance or pretending the native strain field differed.

BacDive's SI-ID 133380 link returns HTTP 404 from the public StrainInfo API.
Ignored-inclusive searches over native/overlay StrainInfo files using the
exact SI-ID, names, LHW37 and all three culture designations found no target
evidence. A BacDive cross-reference alone does not justify SI deposit,
sequence or assembly assertions.

Searches including ignored files covered `data/atb/` and the complete
compressed `data/catalog/allthebacteria.tsv.xz`, using both BioSamples,
all three deposit identifiers, LHW37, target name, slug and typed IDs.
No target ATB row or association was found within those sources. This
is a bounded snapshot result, not a claim that no other genome exists.
SeqCode's name hit corroborates nomenclature only. Optional phenotype
and causal-graph slots need not be populated for this identity record.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**N1 - Minor: the nomenclature type-deposit list omits KACC 15543.** YAML
line 48 lists only JCM 17730. LPSN, the original description's inspected
abstract and NCBI type-material rows 1525-1526 all identify KACC 15543
as another registered deposit of type strain LHW37. The deposit is already
correctly present in the strain's culture identifiers at YAML line 83.
Species identity, type flag and genome associations are therefore unaffected.

Maintained owner: the upstream LPSN source transform feeding
`data/raw/lpsn_names.tsv:27278`. That row already omits KACC;
`src/taxonmech/extract.py:420` collects transformed type-deposit edges,
and `src/taxonmech/seed.py:405` faithfully copies them. Locate the exact
loss point in the maintained upstream LPSN evidence/transform before fixing
it. Upstream KGX edge contents were not inspected in this review.
Do not patch generated YAML or invent a culture CURIE for bare LHW37.

## Recommended Edits

1. In a later curation change, retain the explicitly evidenced KACC 15543
   type deposit in the maintained LPSN source/transform and re-extract the
   inventory. Inspect the upstream edge set to decide whether the correction
   belongs in kg-microbe or TaxonMech extraction. Do not infer an LPSN
   assertion for BCRC 81037 solely from its BacDive co-occurrence.
2. Add a focused extraction regression preserving multiple registered type
   deposits and a seeder regression confirming both appear in nomenclature
   without changing the supported strain/genome evidence.
3. After an authorized implementation and tests, regenerate through the
   documented workflow. No such edits or regeneration occurred here.

## Follow-up Checks

- Run the focused extraction/seeding tests. Inspect
  `just seed --only NCBITaxon:1031538`, then an authorized
  `just seed-canary NCBITaxon:1031538` and its diff.
- Rerun both target validators and full-field source comparisons. Confirm
  nomenclature retains JCM 17730 and adds KACC 15543 while all 13/12/32
  assertions preserve identifiers, versions, source fields and deposit matches.
- A shared transform fix also requires full tests, corpus reproduction,
  provenance and generated-product checks in its own curation workflow.
- Recheck the live GTDB authority page when accessible; its browser request
  failed, so classification verification used inspected pinned native records.
  Retry SI-ID 133380 if later source state provides a real own-deposit record.

## Additional Notes

The live scaffold assembly's BioSample description calls it a reference
strain for another study; its explicit organism and deposit attributes are
JCM 17730 and taxon 1031538. No identity is inferred from that free-text
study label. Two sequencing efforts, shared deposit identity and high ANI
do not establish identical assemblies.

BacDive displays both experimentally reported oxygen tolerance and model
predictions. Those are not claims in this YAML, and this review does not
convert them or the MADIN count into species-level physiology. All absence
statements are bounded to the named complete structured reads or
ignored-inclusive searches. One new report was written; the record, source
code, prior reports, history and curation status were not edited.
Eukaryota was left untouched.
