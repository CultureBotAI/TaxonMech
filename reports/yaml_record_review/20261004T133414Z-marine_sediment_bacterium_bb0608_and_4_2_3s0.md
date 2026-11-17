# YAML Record Review: marine sediment bacterium BB0608_AND_4.2_3S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_3s0.yaml`
- Started UTC: 2026-10-04T13:33:19Z
- Finished UTC: 2026-10-04T13:34:14Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033549`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. BB0608_AND_4.2_3S0
distinguishes this record from neighboring AND_4.2 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_3s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_3s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221183 and scientific-name row 30491 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033549&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033549)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not establish valid
nomenclatural publication or finer taxonomic placement.

## Evidence

Exact Nuccore search returned one sequence, [JF750094.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750094.1),
UID 333384441, a 466-base partial 16S rRNA gene. Source qualifiers name
strain BB0608_AND_4.2_3S0, taxon 1033549, coastal marine sediment,
Australia: Gulf of Carpentaria and June 2008 collection. The qualifier is
strain, not clone or environmental sample. This locus is not a genome,
culture deposit or independent taxonomic classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither supplies a DOI
or PMID. Full manuscript text was not obtained; no phenotype was inferred
from the title. Exact Assembly search returned zero with phrase-not-found
and no-items warnings. The NAME attestation and 2026-09-13 snapshot match
the inventory; the count is not independent experiments.

## Completeness

Complete exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional slots reflect
bounded coverage; zero inventoried strains does not mean never cultured.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
numeric ID and complete label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All eleven matches were inspected: target scope, backbone and scientific
name, two unrelated ATB rows, and six unrelated BioProject collisions.
All six native JSON objects were read in full. Recursive structured
SOURCE.json scans found no matches. These checks do not establish
universal absence.

- ATB row 64905 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033549, run ERR068142, analysis ERZ3068941; scientific name and both Sylph fields Streptococcus pneumoniae. Only the BioSample suffix matches.
- ATB row 1020308: SAMN02335393, run SRR1033549, analysis ERZ4068956; scientific name Salmonella enterica subsp. enterica serovar Agona, both Sylph names Salmonella enterica. Only the run suffix matches. Both ATB rows have available FASTAs, assembly/Sylph/HQ filters PASS and prior-HQ T.
- BV-BRC `data/bvbrc/bvbrc-0018.jsonl.gz:45494` and GenBank `data/catalog/ncbi_genbank-0033.jsonl.gz:46857`: genome 3087176.3 explicitly links GCA_036281735.1, Francisella sp. 19S2-10, taxon 3087176, SAMN38054018. BV-BRC carries culture collection GDMCC:1.3393 and unversioned JAWRHS000000000; GenBank carries JAWRHS000000000.1, 94 contigs and a reported identical pair GCF_036281735.1.
- BV-BRC row 45495 and GenBank row 46856 in those same shards: genome 3087177.3 explicitly links GCA_036281725.1, Francisella sp. 19X1-34, taxon 3087177, SAMN38044047. BV-BRC carries GDMCC:1.3396 and unversioned JAWRHT000000000; GenBank carries JAWRHT000000000.1, 141 contigs and a reported identical pair GCF_036281725.1.
- BV-BRC row 45587 and GenBank row 46860: genome 3088361.3 explicitly links GCA_036281795.1, Francisella sp. 19S2-4, taxon 3088361, strain field GDMCC 1.3392, SAMN38034847. BV-BRC carries unversioned JAWUZH000000000; GenBank carries JAWUZH000000000.1, 93 contigs and a reported identical pair GCF_036281795.1.

All six BV-BRC/GenBank matches are solely to project PRJNA1033549, not
taxon 1033549. Their strain/deposit strings are recorded as source values,
not independently revalidated culture deposits or links to this target.
Their RefSeq counterparts were not fetched; pair assertions above are
explicit GenBank fields, not independent reciprocal verification.
Exclusions are identity-based. None supports a target strain/genome chain;
source versions and unversioned accessions are preserved.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321535`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033549 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13632`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.

