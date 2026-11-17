# YAML Record Review: marine sediment bacterium BB0608_AND_7.1_10G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_10g0.yaml`
- Started UTC: 2026-10-04T15:03:41Z
- Finished UTC: 2026-10-04T15:04:40Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:1033595, species, Bacteria,
EXACT/SEEDED, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. The complete designation
BB0608_AND_7.1_10G0 distinguishes this target from other BB0608 strains.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_10g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_10g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons are not substitutes.

## Identity and Grounding

Backbone row 221229 and native scientific-name row 30537 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033595&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033595)
confirm name and rank; EFetch confirms parent 49928 and code 11. Root-first
lineage is root (1), cellular organisms (131567), Bacteria (2), unclassified
Bacteria (49928), with matching ranks. Species rank is not evidence of
valid publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one [JF750141.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750141.1)
record, UID 333384488, containing 513 bases of partial 16S rRNA. Inspected
source qualifiers identify strain BB0608_AND_7.1_10G0, taxon 1033595,
genomic DNA, coastal marine sediment, Australia: Gulf of Carpentaria and
June 2008. The qualifier is strain, not clone or environmental sample.
This locus is not a genome, culture deposit or independent classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's cryopreservation study is unpublished, and Cornall's
direct submission is dated 2011-04-01. Neither supplies DOI/PMID. Full
manuscript text was not obtained; no phenotype was inferred from its title.
Exact Assembly search returned zero with phrase-not-found/no-items warnings.
The one NAME attestation and snapshot 2026-09-13 agree with the inventory;
the count denotes a name, not an experiment.

## Completeness

Full exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Optional slots may remain
empty; zero inventoried strains does not establish absence of cultivation.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID and full designation with dot/underscore variants, covering label/slug
forms, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and
`history`. All eight matches were inspected: target scope/backbone/name,
two ATB rows and three native JSON objects, each read in full. Structured
recursive SOURCE.json scans found zero matches. These are bounded searches.

- `data/catalog/allthebacteria.tsv.xz:64951`: SAMEA1033595, ERR064606 and ERR085865, ERZ3069001; scientific name and both Sylph fields Streptococcus pneumoniae. Only the sample suffix and AWS URL match.
- `data/catalog/allthebacteria.tsv.xz:1028702`: SAMN02404616, SRR1033595, ERZ4056342; scientific name Pseudomonas syringae KCTC 12500 and both Sylph fields Pseudomonas_E syringae. Only the run suffix matches. Both ATB rows have available FASTA, assembly/Sylph/HQ PASS and prior-HQ T.
- `data/catalog/ncbi_genbank-0047.jsonl.gz:7381` and `data/catalog/ncbi_refseq-0007.jsonl.gz:33195`: GCA_051053435.1 and GCF_051053435.1 are explicitly reciprocal identical pairs; Mycoplasma capricolum subsp. capricolum strain 9298-G5, taxon 40479, species 2095, SAMN39617654. GenBank project is PRJNA1069633; RefSeq project is PRJNA224116. Complete Genome, one contig/scaffold/replicon, no WGS master. Only total/ungapped size 1033595 matches. Separate source annotation counts are not equated by the sequence-pair relationship.
- `data/catalog/gtdb_genomes-0016.jsonl.gz:8872`: RS_GCF_051053435.1 explicitly links GCA_051053435.1 and carries the same strain/taxon/species/sample and RefSeq project. Matches are total/ungapped length and scaffold N50/N75/N90. GTDB uses Bacillota_I/Bacilli_A; carried NCBI classification uses Mycoplasmatota/Mollicutes and retains the subspecies in its unfiltered lineage. Both concern Mycoplasma capricolum, not this target. Translation table 4 differs from the target's 11. These classifications are preserved, not reconciled.

Exclusions are identity-based, not quality-based. Neither numeric matches
nor accession suffixes establish a target strain/deposit/genome chain.
Explicit assembly links and accession versions are preserved without
transferring evidence; sample identity is separate from assembly identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321581`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized fix, verify exact source identity and inventory deltas,
run `just seed-canary NCBITaxon:1033595 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. No canary or regeneration ran.

## Additional Notes

Unique PATHS entry: `data/taxa/PATHS.tsv:13678`. Seed event remains
2026-09-13T17:54:04Z. NCBI browser access failed; EFetch and Datasets
succeeded. iModulonDB is not applicable to this taxonomy-only record.
Only this report and the validation TSV were written; YAML, maintained
inputs, scope, status, history and GitHub were not changed.
