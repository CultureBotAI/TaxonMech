# YAML Record Review: Streptomyces sp. SCSIO 01127

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_scsio_01127.yaml`
- Started UTC: 2026-10-06T09:41:42Z
- Finished UTC: 2026-10-06T09:44:44Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035052`, Streptomyces sp. SCSIO 01127. It asserts species rank, bacterial domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No optional synonyms, nomenclature, mappings, strain list, genome links, causal graph, evidence objects or discussions are asserted. This is a read-only record review, not a curation event or lifecycle promotion.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_scsio_01127.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptomyces_sp_scsio_01127.yaml --out /private/tmp/scsio01127-validation.tsv`: exit 0, one file scanned, zero errors; read the header-only diagnostic TSV.
- Structured comparisons verified the full source lineage, identity, genetic code, unique PATHS/scope rows, sole attestation and inline event wording. Exact scans of type-material, merged-ID and dropped-record inventories found no target rows.
- An ignored-inclusive identifier/name/slug search of `reports/yaml_record_review/` and `history/` found no prior report or separate history artifact before this report was written. The inline seed event is present and schema-valid; no review history is appended.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and publication gates. Focused checks do not certify whole-corpus reproduction or release readiness. No focused term/reference/history validator was invented. `just validate-products` is inapplicable without curator-added graph nodes.

## Identity and Grounding

The complete backbone at `data/raw/ncbitaxon_taxa.tsv:221863` and native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31289` agree with the target. The index is `data/taxa/PATHS.tsv:14344`; maintained scope is `curation/seed_scope.tsv:322155`. The pinned backbone supplies no target synonyms, retirement target or classified children.

Read the [NCBI taxonomy browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1035052&lvl=&mode=node), complete [NCBI EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035052&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035052). They confirm this designation, species rank, bacterial placement and genetic code 11. The parent is unclassified Streptomyces (`2593676`). The full stored chain agrees: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Bacillati (`1783272`), Actinomycetota (`201174`), Actinomycetes (`1760`), Kitasatosporales (`85011`), Streptomycetaceae (`2062`), Streptomyces (`1883`) and unclassified Streptomyces (`2593676`). Datasets includes root; EFetch supplies the remaining labels and ranks. Exact NCBI grounding does not establish validly published species nomenclature or equivalence to a named Streptomyces species.

## Evidence

The sole NCBITAXON attestation correctly counts one imported `NAME` from snapshot `2026-09-13`. The `2026-09-13T17:54:04Z` `SEEDED_FROM_SOURCES` event agrees with the maintained scope reason. Source counts describe imported coverage, not biological abundance or global source absence.

Exact non-expanded searches for `txid1035052[Organism:noexp]` returned zero NCBI Assembly entries and two Nuccore entries, with both returned UIDs accounted for:

| Sequence | Inspected primary evidence and scope |
| --- | --- |
| [JF794566.1](https://www.ncbi.nlm.nih.gov/nuccore/JF794566.1), UID `333601500` | 1,434-base partial 16S rRNA, partial at both ends. Complete metadata, references and features were read, excluding sequence bases. Source explicitly names SCSIO 01127 and `taxon:1035052`, with South China Sea isolation context, 1,350-meter depth and coordinates `8.93338 N 111.91155 E`. Created 25 May 2011, updated 14 June 2012; direct submission 8 April 2011. It cites PMID `21897400`, DOI `10.1038/ja.2011.78`. |
| [KC013978.1](https://www.ncbi.nlm.nih.gov/nuccore/KC013978.1), UID `478434365` | 103,006-base lobophorin biosynthetic cluster and flanking genes, not a whole-genome assembly. Read all header metadata, references and source qualifiers, plus feature counts: one source, 40 CDS, 36 gene and one miscellaneous feature. Individual CDS annotations/translations and bases were not functionally re-audited. Source explicitly names SCSIO 01127, deep-sea sediment and `taxon:1035052`; created/updated 16 April 2013, submitted 26 October 2012. It cites PMID `23432710`, DOI `10.1021/ol400342e`. The SOAPdenovo/454 assembly comment does not turn this locus into a genome. |

Neither inspected source feature supplies a culture-collection, BioSample or assembly identifier. The 2011 [primary article preview and accession section](https://www.nature.com/articles/ja201178) explicitly connect the isolate to `JF794566`; its abstract describes isolation of lobophorins from this strain. Complete PubMed bibliographic records and abstracts were retrieved through EFetch for [PMID 21897400](https://pubmed.ncbi.nlm.nih.gov/21897400/) and [PMID 23432710](https://pubmed.ncbi.nlm.nih.gov/23432710/), verifying both DOI/title pairs. The latter describes gene-inactivation experiments on lobophorin glycosylation in this isolate. These support literature identity and locus context, not culture-deposit equivalence or a whole-genome association. No compound activity values or mechanistic claims are added to the YAML.

Read the primary curated [MIBiG BGC0001004 version 5 page](https://mibig.secondarymetabolites.org/repository/BGC0001004.5/). It links the same isolate and `KC013978.1`, with locus bounds 2,344-100,910 within the 103,006-base sequence. Its status is active, pathway completeness is complete, and its quality is marked questionable. Those source qualifications are preserved: pathway completeness is not genome completeness, and no blanket functional endorsement is inferred. The page's additional references and gene-level annotations were not individually revalidated because the TaxonRecord asserts none of them.

The YAML contains no gene, regulatory or transcriptomic claims, so iModulonDB is inapplicable to the target. Finding biosynthesis literature during a completeness check does not make an expression-module analysis necessary for this identity-only record.

## Completeness

Exact scans found no target entries in the imported BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits tables. The native GOLD catalog does contain two relevant rows, which must not be erased by that statement:

- `data/gold/organisms.jsonl.gz:56852`: `Go0098955`, taxon `1035052`, organism Streptomyces sp. SCSIO 01127, strain SCSIO 01127, empty culture-collection field.
- `data/gold/projects.jsonl.gz:57762`: `Gp0098955`, explicitly linked to `Go0098955`, same organism designation, empty NCBI BioProject and BioSample fields.

The broader GOLD-ID search found no associated analysis row in the searched native catalogs. These rows support source identity but not a deposit-to-genome chain. `docs/HARMONIZATION.md:44` documents that taxon-level GOLD attestations come from KGX, whereas primary workbook rows provide explicitly linked strain resources. `src/taxonmech/seed.py:255` loads the imported organism-count table, and the attestation loop at line 615 uses that table. Thus the absent GOLD attestation accurately reflects the configured imported table; it does not mean GOLD lacks this organism. There is no demonstrated required strain/genome loss under the documented model, and the zero imported strain count should not be interpreted as absence of the experimental isolate.

The candidate search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. It included ignored and compressed data, the numeric taxon ID, designation, slug and separator variants of SCSIO 01127, then expanded to both nucleotide accessions, both GOLD IDs and `BGC0001004`. Only `SOURCE.json` provenance sidecars were excluded from this candidate-data search; unrelated directories and external unindexed resources are outside the exhaustive-search claim.

Both searches returned the same 23 rows. Every complete candidate was read with header-aware TSV or native JSON parsers, and address reconciliation found no unread or extra rows. Five rows concern the target: backbone, native name, scope and the two GOLD rows. Eighteen unrelated hits are resolved below. No eligible missing genome or explicit culture deposit was identified. The two non-genome sequences and optional natural-product literature do not require invented nomenclature, genome links or a causal graph.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The bounded identity and imported-provenance claims agree with inspected evidence. Native GOLD coverage is richer than the configured attestation table, but that documented distinction and the absence of a deposit/genome chain do not establish a record defect.

## Recommended Edits

None required. Leave generated YAML, `SEEDED` status and curation history unchanged. Do not add a whole genome from `KC013978.1`, or infer a named-species/deposit equivalence from sequence similarity or a laboratory designation. A future decision to broaden taxon-level GOLD provenance belongs in maintained extraction/harmonization inputs and `src/taxonmech/seed.py` with regression tests, not a hand-edited attestation. Verified scope changes belong in `curation/seed_scope.tsv`; taxonomy corrections belong upstream.

## Follow-up Checks

No blocking follow-up. A later source refresh can recheck `Go0098955`/`Gp0098955` for an explicit culture deposit, sample or genome analysis, then validate any verified association through its complete source chain. After an actual curation change, run the two focused validators and documented corpus reproduction, history, test and publication gates. Literature enrichment would require inspecting the relevant full experimental text before asserting additional phenotype or mechanism claims.

## Additional Notes

The initial NCBI browser URL failed, but its explicit node URL succeeded. PubMed web pages returned a rate limit/browser challenge; official EFetch abstracts succeeded. The ACS article page returned 403; its linked PubMed and GenBank metadata verified the DOI and abstract. The 2011 publisher page exposed a preview and accession section, not subscription full text. Neither paper's full text or supplementary material was audited. Initial unversioned MIBiG paths failed; the versioned primary page succeeded. Live GOLD organism/project pages were inaccessible through the web tool; GOLD conclusions are limited to the inspected committed native snapshot. No paid access, messages or source mutations were used.

Full-row dispositions of eight unrelated bacterial-source candidates:

| Source rows | Identity and exclusion |
| --- | --- |
| `data/bvbrc/bvbrc-0001.jsonl.gz:18146`; `data/catalog/ncbi_genbank-0000.jsonl.gz:45487`; `data/gold/projects.jsonl.gz:87400`; `data/catalog/allthebacteria.tsv.xz:66032` | Four rows concern Staphylococcus haemolyticus 51-11, taxon 1283, sample `SAMEA1035052`, `GCA_001230985.1`, BV-BRC `1283.128`, GOLD `Gp0140458`/`Go0134575`, study `PRJEB2705`, and ATB run `ERR085182`/analysis `ERZ3070491`. GenBank has no RefSeq partner and records low-quality-sequence exclusion. Sample-number substring only. |
| `data/bvbrc/bvbrc-0006.jsonl.gz:8505`; `data/catalog/allthebacteria.tsv.xz:569522` | Mycobacterium tuberculosis run/designation `ERR1035052`, BV-BRC `1773.20490`, ATB sample `SAMEA3558585`/analysis `ERZ3501781`. Run-number substring only. |
| `data/catalog/ncbi_genbank-0037.jsonl.gz:21044` | Bacteroides uniformis, taxon 820, strain `2201st1_A12_2201SCRN_220225`, `GCA_040928805.1`, sample `SAMN41035052`, project `PRJNA1093465`; no RefSeq partner and a large multi-isolate project exclusion. Unrelated sample digits. |
| `data/catalog/ncbi_genbank-0009.jsonl.gz:6362` | Campylobacter jejuni FSIS11926476, taxon 197, `GCA_010350525.1`, `SAMN13447817`, `PRJNA287430`; no RefSeq partner and large multi-isolate project exclusion. Unrelated assembly digits. |

Both ATB rows retain available FASTAs and passing pipeline, HQ and Sylph filters. Their full SeqKit sums and OSF/AWS location fields were inspected, not recomputed or downloaded. SeqKit sum is not MD5. The Staphylococcus NCBI exclusion and ATB passing filters are separate source properties, not a basis for conflating assemblies. None of these rows concerns the reviewed Streptomyces isolate.

The other ten candidates are distinct GOLD community/plant/fungal metatranscriptome projects with empty organism GOLD fields, not strain-genome chains:

| `data/gold/projects.jsonl.gz` line | GOLD project | BioProject | BioSample | Inspected project context |
| --- | --- | --- | --- | --- |
| 196902 | `Gp0294635` | `PRJNA502391` | `SAMN10350529` | Altamaha River freshwater microbial community, Georgia; Atl_Atl_RepC_8d |
| 227408 | `Gp0332979` | `PRJNA502238` | `SAMN10350521` | Fagus sylvatica/Lactarius subdulcis mycorrhizal community, Martinvelle, Grand Est, France; post bud break R4 |
| 227410 | `Gp0332981` | `PRJNA502240` | `SAMN10350520` | Separate Fagus/Lactarius community from the same source locality; post bud break R6 |
| 228114 | `Gp0333719` | `PRJNA502255` | `SAMN10350528` | Pinaceae seedling/Suillus ectomycorrhiza, Michigan; A225 |
| 228123 | `Gp0333728` | `PRJNA502264` | `SAMN10350527` | Pinaceae/Suillus, California; A246 |
| 228126 | `Gp0333731` | `PRJNA502267` | `SAMN10350526` | Separate Pinaceae/Suillus project, California; A249 |
| 228138 | `Gp0333743` | `PRJNA502186` | `SAMN10350525` | Non-inoculated Pinaceae root tips, Minnesota; Pstro_rep3 |
| 228142 | `Gp0333747` | `PRJNA502190` | `SAMN10350524` | Non-inoculated Pinaceae root tips, Saskatchewan; Llari_rep1 |
| 228143 | `Gp0333748` | `PRJNA502191` | `SAMN10350523` | Separate non-inoculated root-tip project, Saskatchewan; Llari_rep2 |
| 228152 | `Gp0333757` | `PRJNA501998` | `SAMN10350522` | Pinaceae/Suillus, Pennsylvania; Slut/Psyl_rep2 |

These are review diagnostics only. No record, maintained input, generated product, curation history or completed Eukaryota review is changed.
