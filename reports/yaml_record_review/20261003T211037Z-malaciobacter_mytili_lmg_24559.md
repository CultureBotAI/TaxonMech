# YAML Record Review: Malaciobacter mytili LMG 24559

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/malaciobacter_mytili_lmg_24559.yaml`
- Started UTC: 2026-10-03T21:08:37Z
- Finished UTC: 2026-10-03T21:10:37Z
- Verdict: needs curation

## Target

Read all 1,036 lines of this generated `TaxonRecord`: `NCBITaxon:1032238`,
Malaciobacter mytili LMG 24559, rank `STRAIN`, domain `BACTERIA`, grounding
`EXACT`, mapping status `SEEDED`. Its one BacDive strain has 18 assembly,
11 genome-record and 45 related-record assertions. These are separate
provenance assertions, not numbers of distinct biological genomes.

The target is the strain, not its parent species `NCBITaxon:603050`.
Maintained owners include `src/taxonmech/seed.py`,
`src/taxonmech/extract.py` and the source inventories. Generated YAML and
curation history remain untouched in this read-only review.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/malaciobacter_mytili_lmg_24559.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/malaciobacter_mytili_lmg_24559.yaml` | Passed; one file, zero ERROR rows. Standard diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured source comparisons | Backbone, complete lineage, path index, scope reason and all source attestations agree with their inventories. Exact full-field multiset equality for all 18/11/45 strain assertions. |
| StrainInfo evidence | All 15 evidence objects match native eligible deposits, statuses, source taxonomy, DOI and explicit same-deposit sequence links. |
| Embedded history | Strict validation passed; the seven-source seed event and seed-scope reason agree. |
| Standalone history | Not applicable: identifier, label and slug searches including ignored and hidden files found no target entry under `history/`. |
| Causal graph and ontology-product gates | Not applicable: the full YAML contains no causal graph. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
rendered-page freshness, exports, FASTA replay and the full test suite.
Focused comparisons do not substitute for full-corpus reproduction. No
generator, status promotion or history writer was run. Schema validity does
not resolve the scope error in M1.

## Identity and Grounding

The identifier, label, parent, four NCBI equivalent names, genetic code 11
and all ten root-first lineage entries agree with
`data/raw/ncbitaxon_taxa.tsv:220796`. Live EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032238,603050)
corroborate the strain and parent species. A complete backbone scan found no
children of this strain. Native names in
`data/catalog/ncbi_names-0005.jsonl.gz:30018` and the next four rows,
`data/taxa/PATHS.tsv:13158` and `curation/seed_scope.tsv:7207` agree.

Preserve a real source disagreement: NCBI uses Malaciobacter mytili, whereas
[LPSN Malaciobacter mytili](https://lpsn.dsmz.de/species/malaciobacter-mytili)
marks name 798498 as a validly published synonym and identifies
[Arcobacter mytili](https://lpsn.dsmz.de/species/arcobacter-mytili), name
787909, as the correct name. LPSN recognizes the combinations as homotypic.
Its type designations include CECT 7386, DSM 23625, F2075 and LMG 24559.
This naming disagreement does not authorize rewriting the NCBI label or
lineage. The maintained parent-name row is
`data/raw/lpsn_names.tsv:33607`; there is no direct LPSN row for 1032238.

The NCBI strain synonyms preserve the Arcobacter wording appropriately.
The GTDB species name is a different matter: it is not an exact synonym of
this single strain. That identity promotion is M1.

## Evidence

- **BacDive:** `data/raw/bacdive_strains.tsv:2093`, native
  `data/bacdive/records.jsonl.gz:2092` and the inspected
  [BacDive 2098 page](https://bacdive.dsmz.de/strain/2098) agree on F2075,
  CECT 7386, CIP 110066, DSM 23625 and LMG 24559. Genome reference 66792
  supports unversioned GCA_003346775 and GCA_004116555, IMG 2795385496 and
  2871078930, and PATRIC 1032238.5 and 1032238.6. That reference belongs
  to those genome assertions, not to the whole record.
- **Inventory fidelity:** All assertions exactly reproduce raw assembly
  rows 106338-106352 plus StrainInfo assembly rows 7708-7710; raw genome
  rows 85556-85566; and raw related rows 307630-307662 plus StrainInfo
  related rows 190791-190802. Files are
  `data/raw/strain_assemblies.tsv`, `data/straininfo/assemblies.tsv`,
  `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`
  and `data/straininfo/related_records.tsv.gz`.
- **BV-BRC:** Native `data/bvbrc/bvbrc-0000.jsonl.gz:3142` and row 3143
  support the two genome/sample/project chains via whole strain values
  LMG 24559 and CECT 7386. The first row's `LMG culture` field is not a
  deposit accession and correctly supplies no second match.
- **GOLD:** Native organism rows 9918 and 365076, project rows 9780 and
  314826 and analysis rows 179142 and 250356 in
  `data/gold/{organisms,projects,analyses}.jsonl.gz` support
  Go0011292 -> Gp0011292 -> Ga0310359 and
  Go0519052 -> Gp0443187 -> Ga0396093. The first chain matches both
  `F2075, LMG 24559` and the LMG collection field using the actual LMG
  token, not the F2075 alias; the second matches CECT 7386 through the
  organism strain field. The two GenBank sequence entries in Ga0310359
  cite the same assembly, not two distinct assemblies. DSM organism
  Go0613026 is supported by row 443769; complete own-ID searches found no
  further project/analysis chain for it, so organism-only evidence is right.
- **NCBI assemblies:** Native GenBank rows 32020 in
  `data/catalog/ncbi_genbank-0002.jsonl.gz` and 9687 in shard 0003, and
  RefSeq rows 47810 in `ncbi_refseq-0001.jsonl.gz` and 12304 in shard 0002,
  support GCA/GCF_003346775.1 and GCA/GCF_004116555.1. Live
  [NCBI genome metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_003346775.1,GCF_003346775.1,GCA_004116555.1,GCF_004116555.1/dataset_report)
  confirm current complete ASM334677v1 for LMG 24559, SAMN03737955 and
  PRJNA66823, and current contig-level ASM411655v1 for CECT 7386,
  SAMN07709798 and PRJNA412344. Native RefSeq PRJNA224116 remains a
  source-specific assertion even though the live API reports the original
  project for each paired accession. Unversioned source accessions are
  preserved without inventing a version.
- **GTDB genomes:** Native `data/catalog/gtdb_genomes-0014.jsonl.gz:39840`
  and `gtdb_genomes-0012.jsonl.gz:19743` support the two deposit-specific
  genome links, assembly levels and sample/project assertions. They do not
  establish equivalence between the strain and the species cluster.
- **StrainInfo:** Native `data/straininfo/records.jsonl.gz:281673` and the
  [live SI-ID 360196 API record](https://api.straininfo.dsmz.de/v2/data/strain/max/360196)
  corroborate DOI `10.60712/SI-ID360196.3`, BacDive 2098, published status
  and available deposits 836133 (LMG), 841950 (CECT), 900078 (CIP) and
  906532 (DSM). All are nondeprecated and nonerroneous. Their own taxonomy
  is 603050; the LMG deposit uses the Malaciobacter name while the others
  use Arcobacter. The four exact matches are in
  `data/straininfo/strain_links.tsv:79499` and the next three rows.
- **Own-deposit sequences:** GCA_003346775 explicitly names LMG deposit
  836133; GCA_004116555 explicitly names both LMG and CECT deposits.
  Consequently its two overlay associations are supported, not inferred
  through shared group membership. Nuccore EFetch metadata confirm
  [FN257299.1](https://www.ncbi.nlm.nih.gov/nuccore/FN257299.1), partial
  hsp60, and [FN600705.1](https://www.ncbi.nlm.nih.gov/nuccore/FN600705.1),
  partial 23S rRNA, for LMG 24559; and
  [GU291969.1](https://www.ncbi.nlm.nih.gov/nuccore/GU291969.1), partial
  gyrB, and [MG256023.1](https://www.ncbi.nlm.nih.gov/nuccore/MG256023.1),
  rRNA/intergenic-spacer sequence, for CECT 7386. StrainInfo's `gene`
  sequence type for FN600705 is retained as source vocabulary, not a claim
  that rRNA encodes a protein. No sequence alignment or functional assay
  was performed.
- **Attestations:** Structured scans reproduce NCBI NAME 1, BacDive STRAIN
  1, MediaDive MEDIUM 1 (medium 693), GOLD ORGANISM 2, MADIN
  TRAIT_ASSERTION 1 and BACTOTRAITS TRAIT_ASSERTION 18. The relevant raw
  source row numbers are 2093, 96, 417, 600 and 70. GTDB mapping row 1338
  reproduces count 5, which describes the full cluster, not five genomes
  established as this strain.
- **iModulonDB:** The resolved `culturebotai-claw/.venv/bin/kg-microbe-sources
  imodulondb datasets` adapter returned 28 dataset keys, with no
  Malaciobacter or Arcobacter dataset. No organism-matched marker query
  applies; this absence is not negative evidence about the record.

## Completeness

Ignored-inclusive compressed searches covered all native catalog, BacDive,
BV-BRC, GOLD and SeqCode data using the taxon ID, both species names, all
four whole collection designations, F2075 and both own BioSamples. Complete
structured scans covered source inventories, type material, merged IDs,
dropped records and StrainInfo eligibility. No additional eligible genome
association was found within those boundaries.

The F2075 alias also occurs on Pseudomonas aeruginosa records in BV-BRC.
Those hits, a bare-F2075 GOLD organism and the separate T234, S36 and
VLC_008 species members were correctly not joined to this strain. Neither
a name match nor a type-strain flag substitutes for a whole culture deposit.
SeqCode's two name entries are nomenclatural leads, not new genome evidence.

AllTheBacteria sample SAMN03737955 has an available FASTA but carries
`META_FAIL`. Its native row 1097522 in `data/catalog/allthebacteria.tsv.xz`
agrees with `data/atb/assemblies.tsv:3784`; exclusion row 2071 records
`metadata_identity_flags:META_FAIL`. This is an identity filter, not a
quality-only threshold that can be bypassed. Own sample SAMN07709798 is
absent from the fully searched native catalog and committed ATB data. The
eligible but unrelated species-labelled SAMEA5613859 is not an own sample
match. No ATB association is required here.

The record-local LPSN nomenclature and type flag are omitted under current
schema/seeder policy, not because this is a non-type strain. Native BacDive,
all four StrainInfo deposits, NCBI parent type-material rows 241087-241093
and live BioSamples support its biological type status. The optional strain
medium count follows raw value zero; the taxon-level medium attestation
does not replace that source field. Phenotypes and causal graphs are not
required additions to this identity/provenance record.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Major: GTDB species identity is incorrectly promoted onto a strain.**
At target lines 58-61, `Malaciobacter mytili` is an `EXACT_SYNONYM`, and
line 63 makes `GTDB:s__Malaciobacter_mytili` an identity xref. The native
cluster census found five genomes: two with NCBI strain taxon 1032238 and
three with species taxon 603050. The latter are T234, S36 and VLC_008,
not deposit evidence for LMG 24559. Thus the species name and cluster-wide
count cannot establish exact strain identity.

Maintained owner: `src/taxonmech/seed.py:451` treats `skos:closeMatch` as
identity without checking rank, then emits the synonym and xref.
`src/taxonmech/extract.py:755` supplies the cluster-wide count. The raw
predicate can be preserved as an upstream mapping observation without
promoting it to exact identity. These are manifestations of one scope
defect, not a wrong NCBI identifier or an invalid YAML record.

## Recommended Edits

1. Make GTDB identity promotion rank-aware in `src/taxonmech/seed.py`.
   Suppress the species exact synonym and identity xref on this strain
   while preserving supported NCBI strain synonyms and scoped mappings.
2. Explain that five is a species-cluster count. Any count-policy change
   belongs in the maintained extractor with explicit provenance semantics;
   do not hand-edit raw mappings or generated YAML to manufacture a count.
3. Add a regression in `tests/test_seed.py` for strain versus species
   identity, retaining legitimate species-level mappings and all 18/11/45
   strain assertions. After curation authorization, use the documented dry
   run and `just seed-canary NCBITaxon:1032238` before any bulk regeneration.

## Follow-up Checks

Run the focused seed regression, both recorded single-file validators,
and the native five-member cluster census. Confirm loss of the unsupported
identity promotion without loss of any deposit-backed assertion. Recheck
all 15 StrainInfo evidence objects and retain the ATB META_FAIL exclusion.
Full-corpus reproduction, strict validation, provenance/QC and rendered
product checks remain release gates, not checks claimed by this review.

## Additional Notes

- LPSN's current-name preference and NCBI's carried classification are
  explicitly preserved above. This review does not adjudicate the genus
  split or prescribe a medical name.
- `is_type_strain` is defined by record-local LPSN names at
  `src/taxonmech/schema/taxonmech.yaml:477`; `seed.py` collects those
  designations before matching deposits. Ancestor-qualified type evidence
  would require an explicit policy/schema extension, not a silent flag
  copied from any native source.
- BacDive's EU669904 16S association is not a StrainInfo own-deposit
  sequence in this snapshot. Its absence from this overlay is not a
  broken reference or permission to attribute it to StrainInfo.
- The live GTDB tree request failed; the complete pinned native cluster
  was inspected successfully. Full literature texts, FASTAs and protein
  annotations were not reanalysed. The target has no paper DOI/PMID claim;
  its StrainInfo version DOI was verified at the source API.
- Only this target was judged. Other strain rows were identity candidates,
  not reviews of their YAML. Eukaryota and previous reports were untouched.
