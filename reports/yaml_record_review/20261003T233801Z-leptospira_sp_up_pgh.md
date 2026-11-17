# YAML Record Review: Leptospira sp. UP-PGH

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/leptospira_sp_up_pgh.yaml`
- Started UTC: 2026-10-03T23:36:37Z
- Finished UTC: 2026-10-03T23:38:01Z
- Verdict: pass

## Target

Read all 54 lines of generated `TaxonRecord` NCBITaxon:103234,
Leptospira sp. UP-PGH. It carries `SPECIES`, `BACTERIA`, `EXACT`,
`SEEDED`, one NCBI name attestation, zero inventoried BacDive strains and
one seed event. No genome, phenotype, nomenclature, taxonomy mapping or
graph assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/leptospira_sp_up_pgh.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/leptospira_sp_up_pgh.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, full lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports, sequence alignment or per-genome
ortholog verification. Focused source comparisons do not prove corpus
reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18358`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103234&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103234)
agree on exact label, species rank, parent NCBITaxon:2633828 and code 11.
All ten root-first lineage entries agree through Pseudomonadati,
Spirochaetota, Leptospiria, Leptospirales, Leptospiraceae, Leptospira and
unclassified Leptospira. Datasets includes root. Preserve the exact
UP-PGH name; an institutional acronym or other UP-prefixed isolate does
not establish synonymy, collection origin or a replacement classification.

Native scientific-name row
`data/catalog/ncbi_names-0000.jsonl.gz:38376` supplies no synonym.
`data/taxa/PATHS.tsv:13207` and `curation/seed_scope.tsv:144018` support
the exact slug and seed reason. Species rank satisfies scope, not formal
nomenclatural publication or a type-culture claim. The taxonomy browser
was inaccessible; both structured authority reads succeeded.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid103234[Organism:noexp]` returned one sequence.
  Inspected [AB031509.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031509.1)
  is a 746-base partial flaB coding sequence annotated as flagellin, with
  exact organism, strain UP-PGH and taxon103234. It is not a 16S marker,
  genome assembly, culture-deposit registration or experimental proof of
  gene function in this review. The source feature supplies no geographic
  or isolation-source claim to transfer into this record.
- References identify a database-only 2000 entry by Kawabata, Dancel,
  Yanagihara and Watanabe and an August 25, 1999 direct submission,
  without DOI or PMID. No phenotype or virulence inference was added.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits and no backbone child.
  `strain_count: 0` counts inventoried BacDive records, not all isolates.
- Native culture-number matches are unrelated: CIP103234 belongs to
  Serratia rubidaea, not Leptospira; DSM103234 belongs to Paracoccus
  halotolerans. Their actual genome and deposit associations, detailed
  below, cannot be transferred by matching the number103234.
- The resolved `kg-microbe-sources imodulondb datasets` runner returned
  28 keys, none for Leptospira. iModulonDB was not applicable to the
  optional flaB annotation context; lack of coverage is not negative
  biological evidence, and no other organism's module was transferred.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. The partial coding sequence is optional
context, not a mandatory missing genome.

Ignored-inclusive identifier, exact label, slug and UP-PGH spelling
searches covered raw inventories, all catalog shards, BacDive, BV-BRC,
GOLD, SeqCode, StrainInfo, ATB strain/genome links and exclusions, curation
and history. After identity-scoping culture and numeric matches, no
target-associated assembly, type-material, culture-collection, merged-ID,
dropped-row or standalone history entry was found on these surfaces.
The raw/maintained target matches were the backbone and scope rows.

No inventoried BacDive strain or eligible own deposit starts a SI join;
no carried BIOSAMPLE assertion starts an ATB join. The native ATB catalog
was searched for target strings, but sample/FASTA eligibility and sequence
equivalence were not audited. No global ATB absence follows. Exact-name
and sequence-accession web searches produced no additional verified
identity evidence; search coverage is not proof of publication absence.
Empty optional synonyms, nomenclature, mappings, definitions, general
evidence, discussions and graphs are appropriate to the supported claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input fix is required.

## Recommended Edits

None required. Preserve generated YAML, exact isolate, lineage and `SEEDED`
status. Future taxonomy fixes belong in the pinned NCBI input,
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and the seeder.
Optional enrichment needs separately authorized maintained evidence at
the exact strain and claim scope, not a manual YAML edit, acronym
expansion or culture-number-only join.

## Follow-up Checks

- At refresh, verify the exact taxon and parent against explicit source
  identity, merge or replacement evidence. Preserve UP-PGH separately
  from similarly named isolates unless an authority supplies a bridge.
- For enrichment, establish own strain/deposit and assembly provenance;
  keep the partial flaB annotation distinct from experimental function.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:103234, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

CIP103234 occurs on BacDive5159 (native row5049, raw row5050), whose
classification distinguishes Serratia rubidaea species61652 and
strain1218096. Related LPSN780879/780886 entries concern Serratia, and
type/culture rows242116/242117 and43613 are not Leptospira evidence.
SI-ID323074/SI-DP21541 (native row250738, strain-link row91469,
assembly row9713) explicitly supplies unversioned GCA_001304675 for that
own CIP deposit. Preserve that supplied version syntax without treating
it as this target's assembly.

The same unrelated Serratia genome is GCA/GCF_001304675.1 in native
GenBank0000:48923, RefSeq0000:41299, GTDB0002:3052 and BV-BRC0025:39057
(patric61652.4). GOLD follows Go0119082, Gp0124642 and Ga0100840, with
IMG2645727870, sample SAMN04100244 and submission project PRJNA296548.
RefSeq/GTDB carry PRJNA224116. These explicit chains remain attached to
Serratia; GOLD Go/Gp/Ga references are not themselves genome identifiers.

DSM103234 instead occurs on BacDive168633 (native90865, raw90866),
Paracoccus halotolerans taxon2778531, LPSN799905, GOLDGo0620484 and
SI-ID407202/SI-DP914559 (native305091, strain-link70465). Its type rows
120925/120926 and culture row59488 do not identify NCBITaxon:103234.
No source grouping transfers either deposit's sequence evidence to UP-PGH.

Other excluded numeric matches include Pseudomonas aeruginosa
GCA_033091475.1 strain PSA-BAB-IMI-103234 and assembly statistics in
GTDB records GCF_040066975.1, GCF_027691585.1, GCF_000679275.1,
GCF_049944615.1, GCF_040684635.1, GCA_902495335.1 and GCF_002271405.1.
Their full identities are unrelated to Leptospira UP-PGH.

All absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No optional context was inserted into the YAML, and no
outbound message, GitHub mutation, history event or status promotion
occurred. Older reports and completed Eukaryota coverage were untouched.
