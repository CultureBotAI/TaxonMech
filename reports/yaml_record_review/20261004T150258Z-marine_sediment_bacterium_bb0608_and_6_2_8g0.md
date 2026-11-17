# YAML Record Review: marine sediment bacterium BB0608_AND_6.2_8G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_8g0.yaml`
- Started UTC: 2026-10-04T15:02:01Z
- Finished UTC: 2026-10-04T15:02:58Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:1033594, species, Bacteria,
EXACT/SEEDED, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_6.2_8G0 distinguishes the target from neighboring strains.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_8g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_8g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; no direct children.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded checks do not replace those gates.

## Identity and Grounding

Backbone row 221228 and scientific-name row 30536 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033594&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033594)
confirm the name and rank; EFetch confirms parent 49928 and code 11.
Root-first lineage is root (1), cellular organisms (131567), Bacteria (2),
unclassified Bacteria (49928), with matching ranks. Species rank alone
does not establish valid publication or finer placement.

## Evidence

Exact Nuccore search returned one [JF750139.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750139.1)
record, UID 333384486, containing 514 bases of partial 16S rRNA. Source
qualifiers explicitly identify strain BB0608_AND_6.2_8G0, taxon 1033594,
genomic DNA, coastal marine sediment, Australia: Gulf of Carpentaria and
June 2008. The qualifier is strain, not clone or environmental sample;
this locus is not a genome, culture deposit or independent classification.

Both references were inspected: the Cornall, Beyer, Streten-Joyce,
McGuinness, Parry and Gibb cryopreservation study is unpublished; Cornall's
direct submission is dated 2011-04-01. Neither supplies DOI/PMID. Full
manuscript text was not obtained and no phenotype was inferred from its
title. Exact Assembly search returned zero with phrase-not-found/no-items
warnings. The one NAME assertion and snapshot 2026-09-13 match the inventory;
one name is not one experiment.

## Completeness

Full exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional slots are
appropriate; zero inventoried strains does not mean never cultivated.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID and full designation with dot/underscore variants, covering label/slug
forms, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and
`history`. All seven matches were inspected: target scope/backbone/name,
one ATB row and three native JSON objects, each read in full. Structured
recursive SOURCE.json scans found zero matches. Absence is bounded to
these local searches and the exact public queries.

- `data/catalog/allthebacteria.tsv.xz:64950`: SAMEA1033594, ERR064607 and ERR085866, ERZ3069002; scientific name and both Sylph fields Streptococcus pneumoniae. FASTA available, assembly/Sylph/HQ PASS, prior-HQ T. Only the sample suffix and AWS URL match.
- `data/catalog/ncbi_genbank-0047.jsonl.gz:1070` and `data/catalog/ncbi_refseq-0007.jsonl.gz:32088`: GCA_050920795.1 and GCF_050920795.1 are explicitly reciprocal identical pairs, Mycoplasmopsis bovis strain AMSJ16, taxon/species 28903, SAMN48737548; GenBank project PRJNA1125005, RefSeq PRJNA224116. Complete Genome, one contig/scaffold/replicon, no WGS master. Only total/ungapped size 1033594 matches.
- `data/catalog/gtdb_genomes-0008.jsonl.gz:26135`: RS_GCF_050920795.1 explicitly links GCA_050920795.1, the same organism/strain/taxon/sample and RefSeq project. Matches are total/ungapped length and scaffold N50/N75/N90. GTDB classification uses Bacillota_I, Bacilli_A and Mycoplasmatales; carried NCBI classification uses Mycoplasmatota and Mycoplasmoidales. Both concern Mycoplasmopsis bovis, not this target. Translation table 4 also differs from the target's 11. Source classifications are preserved, not reconciled.

Exclusions are identity-based, not quality-based. Neither numerical size
matches nor accession suffixes supply a target strain/deposit/genome chain.
Explicit assembly links and versions are preserved without transferring
evidence to the target; sample identity is distinct from assembly identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future fixes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321580`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized fix, verify exact identity and inventory deltas, run
`just seed-canary NCBITaxon:1033594 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. No canary or regeneration ran.

## Additional Notes

Unique PATHS entry: `data/taxa/PATHS.tsv:13677`. Seed event remains
2026-09-13T17:54:04Z. NCBI browser access failed; EFetch and Datasets
succeeded. iModulonDB is not applicable to this taxonomy-only record.
Only this report and the validation TSV were written; YAML, inputs, scope,
status, history and GitHub were not changed.
