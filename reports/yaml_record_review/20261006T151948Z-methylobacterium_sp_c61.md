# YAML Record Review: Methylobacterium sp. C61

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c61.yaml`
- Started UTC: 2026-10-06T15:16:03Z
- Finished UTC: 2026-10-06T15:19:48Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035205`, label `Methylobacterium sp. C61`, SPECIES / BACTERIA. The entire YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED, with ten root-first ancestors, code 11, zero BacDive strains, one NCBI NAME attestation and one inline seed event. No synonyms, equivalent xrefs, nomenclature, taxonomy mappings, genome links, definition, citations, phenotype claims or causal graph are asserted. The near designation C61+2-34 was investigated separately rather than silently treated as an alias.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c61.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c61.yaml --out /private/tmp/mc61-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: exact identity, complete lineage, code, attestation, scope reason and seed-event content agree with pinned inputs. This is not corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc` and the test suite. No full-corpus success is claimed.
- There are no curator-added ontology nodes. The product-check configuration excludes taxonomic fields and delegates inventory correspondence to corpus reproduction.
- No separate target history artifact was found by an ignored-independent filename search. Inline history passed record validation; no external history validator was run against an invented artifact.
- No DOI, PMID or quote is asserted by the YAML. Sequence-linked literature and a near-deposit publication were checked as completeness/disambiguation evidence.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221926`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035205&retmode=xml) and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035205) agree on the exact taxid, label and SPECIES rank. Both responses were read fully. XML confirms bacterial division, parent 2615210, genetic code 11 and no alternate names. Dataset metadata include the full ten-ID root-inclusive chain, whose pinned labels/ranks agree with the YAML.

The parent is `unclassified Methylobacterium`, a no-rank grouping below genus 407. Carrying that NCBI lineage does not assign a named species. A strain qualifier in sequence metadata does not authorize changing NCBI's taxon rank. EXACT identifies the NCBI concept, not nomenclatural standing.

The complete [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, names M. organophilum as type species and does not attribute a species name or type deposit to C61. Pinned checks found no target children, type-material row, merged-ID row or dropped row.

The legacy NCBI browser route was inaccessible; the successful XML and dataset responses supplied identity evidence. No mismatch in the carried target identity was found.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221926` supports label, rank, parent, code, empty synonym fields and NCBI-only provenance.
- Complete `data/catalog/ncbi_names-0005.jsonl.gz:31394` contains the exact scientific name and taxid, with an empty unique-name field.
- `data/taxa/PATHS.tsv:14417` resolves the slug. `curation/seed_scope.tsv:322201` adds the record on 2026-09-13 under the one-source attested rule.
- The 2026-09-13T17:54:04Z seed event matches that reason and source list. The attestation counts one NAME, not a biological strain or genome.

Exact Entrez searches `txid1035205[Organism:noexp]` returned zero assemblies with phrases-not-found / no-items diagnostics, and one nucleotide UID, 347300702. The complete nucleotide ID list equals the returned count. The assembly no-hit is bounded to this query.

Full [GenBank metadata for FR869801.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869801.1) identify a 1,333-nt partial 16S rRNA sequence, strain C61 and exact taxon 1035205. The source states host leaf surface and Cerastium holosteoides. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. There is no culture-collection qualifier, BioSample, BioProject or assembly in these metadata. All features, source qualifiers and references were read; bases were omitted.

The sequence cites Wellner, Lodders and Kampfer, PMID 22000032 and DOI 10.1016/j.syapm.2011.08.005. The full [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml) confirm the pairing and a phyllosphere-community study. The abstract does not identify C61 or establish isolate-specific phenotype, locality or culture-deposit equivalence. Its full text and supplements were not inspected.

An initial numeric match, `data/catalog/ncbi_genbank-0001.jsonl.gz:44213`, was read completely. It identifies GCA_002340665.1 as Micrococcales bacterium UBA2544, taxid 1951166; 1035205 is the genome size. It is not target evidence.

A consequential near-deposit candidate was investigated:

- Complete `data/bacdive/records.jsonl.gz:53292` is BacDive 130982, designation C61+2-34, deposit DSM 23674, filed under taxid 409. Its direct genome fields name unversioned GCA_022179645, PATRIC 1003091.3 and IMG 8069157833, classified as Methylobacterium thuringiense, taxid 1003091. The native type flag is no.
- Complete `data/straininfo/records.jsonl.gz:297830` is SI-ID 399941, DOI 10.60712/SI-ID399941.2, with available DSM 23674 deposit SI-DP 906770 and designation C61+2-34. It uses genus taxid 407 and has no sequence list. Its DOI identifies a source-record version, not a publication.
- The inspected [BacDive page](https://bacdive.dsmz.de/strain/130982) and [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-23674) retain C61+2-34, the same plant host and a Wellner/Kampfer provenance chain. DSMZ dates collection to 2 July 2008 in Germany. These are reasons to investigate, not explicit evidence that C61 equals C61+2-34.
- Complete native NCBI, BV-BRC, GTDB and GOLD rows consistently support DSM 23674's genome links. The [live NCBI assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_022179645.1/dataset_report), including nested sample metadata, confirms current GCA/GCF_022179645.1, taxid 1003091, strain DSM 23674, SAMD00388949 and PRJDB11873. It supplies no FR869801 or taxid 1035205 bridge.
- GOLD Go0644741 links through Gp0680703 to Ga0580295, which supplies IMG 8069157833 and GCA_022179645.1. These supported DSM deposit chains are already retained in the pinned strain-link inventories; they are not evidence for attaching the deposit to this C61 taxon.
- The inspected [primary article's General Considerations section](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.740610/full) explicitly treats DSM 23674 / C61+2-34 as a non-type M. thuringiense strain. Full PubMed metadata verified PMID 34737731 / DOI 10.3389/fmicb.2021.740610. The [LPSN species page](https://lpsn.dsmz.de/species/methylobacterium-thuringiense) names C34 / CCM 7787 / LMG 25777 as the type. DSMZ's proposed-type wording must not be promoted into type status for C61.

No inspected source explicitly equates C61, taxid 1035205 or FR869801.1 with DSM 23674. The relationship remains unresolved, not disproved. No deposit, genome, named-species identity or phenotype is transferred.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. There are no target descendants. Zero listed strains is therefore consistent with `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`; it is not a statement that the original isolate was uncultured.

`data/raw/bacdive_strains.tsv:53293` files DSM 23674 under taxid 409, not this target. Its culture row, eight assembly assertions, six genome-record assertions, sample/project/GOLD references and StrainInfo links were read completely. They remain source-specific evidence for the longer designation. A C61 prefix cannot replace the required identity proof. Existing culture normalization rejects C61 and C-61.

FR869801.1 is an optional non-genome marker, not a missing required genome. No supported target strain entry or eligible own-deposit SI-DP association was established to receive it. Any future importer/model extension requires explicit evidence and maintained ownership, not a hand edit of generated YAML.

The structured iModulonDB inventory returned 28 datasets before web follow-up, without Methylobacterium or Methylorubrum coverage. It is not applicable and not negative biological evidence. Optional definition, phenotype and graph fields may stay empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the assertions of the reviewed record within the inspected scope. The exact NCBI identity and provenance are supported. The unproven C61-to-DSM-23674 association is a bounded research follow-up, not an established missing representation or evidence that the record denotes the wrong organism.

This pass does not certify full-corpus reproducibility, resolve that candidate relationship or validate unasserted phenotypes.

## Recommended Edits

None required for the current record.

Before proposing DSM 23674 enrichment, obtain explicit provenance connecting the short designation or FR869801.1 to C61+2-34. If established, route classification/mapping corrections upstream to the relevant source and kg-microbe, then use maintained extraction/seeding code with a regression test. Preserve the complete deposit spelling and source-specific genome/sample/project chains. Do not transfer a type flag from proposed-type catalogue prose.

Do not manually edit the YAML, promote SEEDED to REVIEWED or append history from this read-only report.

## Follow-up Checks

- Recheck the original 2011 paper's full text and supplements for a C61-to-C61+2-34 designation table; an explicit link is required before any identity enrichment.
- Recheck source taxonomy and deposit records if that link is established. Taxids 1035205, 409, 407 and 1003091 have different scopes and cannot substitute for one another.
- Preserve FR869801.1 as a non-genome marker and preserve the unversioned BacDive assembly identifier alongside independently versioned source assertions.
- After any authorized upstream/import change, run target schema/strict checks and actual full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`.
- Do not infer a species reassignment from the candidate assembly's inconclusive, below-threshold ANI result. The reported best match does not resolve C61's identity.

## Additional Notes

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial taxid/name/slug search returned four rows. Expanded C61/C-61 context search returned five, adding the two longer-designation native records. A deposit/accession expansion returned 62 rows. All 66 distinct rows across those searches were read completely with structured pinned comparisons and lossless native/TSV decoding.

Broad numeric expansion also hit unrelated taxids, sequence statistics and SI deposit IDs. These were rejected by inspecting the actual fields; reading incidental source rows did not reopen reviews of those taxa, including eukaryotic candidates. A separate FR869801 / 347300702 search returned no rows. Five SOURCE.json files were searched structurally and history filenames checked independently. Absence findings include ignored files but remain bounded to the named sources.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Target NCBI APIs, full marker metadata, PubMed metadata/abstracts, LPSN, DSMZ, BacDive and the relevant primary-article section were inspected. The PMC route returned a browser challenge; the publisher's inspected text supplied the candidate's non-type statement. Search snippets and unrelated phenotypic predictions were not used as target evidence.

No record/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota reviews were not reopened.

