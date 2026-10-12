# YAML Record Review: Methylobacterium sp. C65

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c65.yaml`
- Started UTC: 2026-10-06T15:21:03Z
- Finished UTC: 2026-10-06T15:22:55Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035206`, label `Methylobacterium sp. C65`, SPECIES / BACTERIA. The whole YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record has EXACT grounding, SEEDED status, ten root-first ancestors, genetic code 11, zero BacDive strains, one NCBI NAME attestation and one seed event. No synonyms, equivalent xrefs, nomenclature, taxonomy mappings, genome links, definition, citations, phenotype assertions or causal graph are present. The review resolves this exact taxid, not arbitrary uses of the short designation C65.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c65.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c65.yaml --out /private/tmp/mc65-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: identity, complete lineage, genetic code, attestation, scope and seed-event content agree with pinned inputs. This does not replace corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc` and the test suite. No full-corpus pass is claimed.
- No curator-added ontology graph needs term validation. The product-check configuration excludes taxonomy fields and delegates inventory agreement to corpus reproduction.
- No separate history artifact for this target was found by an ignored-independent filename search. Inline history passed record validation; no external validator was run against an invented artifact.
- No DOI, PMID or quotation is asserted by the YAML. A marker-linked publication was inspected for completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221927`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035206&retmode=xml) and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035206) agree on the exact identifier, label and SPECIES rank. Both live responses were inspected in full. XML confirms bacterial division, parent 2615210, code 11 and no alternate names. Dataset metadata confirm all ten root-inclusive ancestor identifiers; their pinned labels/ranks match the YAML.

The parent is the no-rank grouping `unclassified Methylobacterium`, below genus 407. It should remain in the carried NCBI lineage. A sequence's strain qualifier does not authorize rewriting NCBI's SPECIES rank. EXACT denotes the NCBI concept, not a claim that this placeholder is a validly published binomial.

The complete [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was inspected during this turn and rechecked for C65. It names M. organophilum as type species and supplies no C65 species-name or type-deposit attribution. No genus-level nomenclature was inherited.

Pinned checks found no children, exact type-material row, merged-ID row or dropped row for the target. The legacy taxonomy-browser route was unavailable; the two successful structured NCBI responses supplied the identity and lineage check.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221927` supports the exact name, rank, parent, genetic code, empty synonym fields and NCBI-only provenance.
- Complete native `data/catalog/ncbi_names-0005.jsonl.gz:31395` contains the exact scientific name and taxid with an empty unique-name field.
- `data/taxa/PATHS.tsv:14418` resolves the slug. `curation/seed_scope.tsv:322202` adds it on 2026-09-13 under its one-source attested rule.
- The 2026-09-13T17:54:04Z seed event agrees with the scope reason and source list. The attestation counts one NAME, not a genome, deposit or biological observation.

The initial taxid search matched `data/catalog/ncbi_genbank-0064.jsonl.gz:40122`. Full native inspection identifies GCA_977230735.1, isolate MarMAG_020552, as an uncultured bacterium, taxid 77133. Its `genome_size_ungapped` is 1035206. This number is not its taxid and does not support an assembly link for C65.

Exact Entrez searches `txid1035206[Organism:noexp]` returned zero assemblies with phrases-not-found / no-items diagnostics, and one Nuccore UID, 347300703. The complete nucleotide ID list equals the query count. The assembly no-hit is bounded to that exact query, not proof of universal genome absence.

Complete [GenBank metadata for FR869802.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869802.1) identify a 1,335-nt partial 16S rRNA sequence, strain C65 and exact taxon 1035206. The source describes host leaf surface and Cerastium holosteoides. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. The metadata contain no culture-collection qualifier, BioSample, BioProject or assembly. Every feature, source qualifier and reference was inspected; bases were omitted. This is a marker, not a genome.

The sequence cites Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. Full [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml), fetched in this turn, were reread against that exact reference. They confirm the pairing and a phyllosphere-community study across plant hosts, locations and land-use regimes. The abstract does not identify C65 or establish an isolate-specific phenotype, sampling locality or growth requirement. Full text and supplements were not inspected. No community result is transferred to C65.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded C65/C-65 context and accession searches found no eligible target culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit assertion.

Zero listed strains matches `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: there is no exact target BacDive row or descendant to contribute an entry. This does not imply that the original isolate was never cultured. The existing culture normalizer rejects C65 and C-65 as unqualified designations.

The missing optional FR869802.1 link is not a required-representation defect under the current contract. No supported existing strain entry or eligible SI-DP association was established to receive it. Future enrichment requires explicit identity and a maintained import path; a bare designation or numeric coincidence cannot create a deposit, genome or equivalence.

The structured iModulonDB adapter ran before browser follow-up and returned 28 datasets without Methylobacterium or Methylorubrum coverage. It is not applicable and not negative biological evidence. Optional definition, phenotype and causal-graph fields may remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and inspected evidence scope. The generated YAML supports its exact identity and provenance, without treating the unrelated genome statistic as a taxonomic match or the 16S marker as a genome.

This pass does not certify full-corpus reproducibility or unasserted biological properties.

## Recommended Edits

None required for this record.

Future sequence enrichment belongs in maintained source extraction and seeding logic after explicit identity is established. Preserve FR869802.1 as a typed non-genome marker if the importer/model supports it. Never create a culture accession or SI-DP from C65 alone, or a genome link from a numeric text hit. Generated YAML must remain read-only.

Do not promote SEEDED to REVIEWED or append curation history from this report.

## Follow-up Checks

- On source refresh, repeat exact taxonomy, complete lineage, status and target schema/strict checks.
- After any authorized source/import change, run real full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded target comparisons do not replace these gates.
- Require an eligible own-deposit identifier and explicit sequence attribution before adding a StrainInfo link. Keep FR869802.1 outside genome counts.
- Inspect full text and supplements of PMID 22000032 before proposing C65-specific phenotype or ecological assertions.
- Match taxids by their fields, not arbitrary occurrences in sequence statistics.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial identifier/label/slug query returned four rows, including the unrelated genome-size match. Expanded Methylobacterium/Methylorubrum C65/C-65 context search returned the three target identity/scope rows, adding none. All four distinct rows were read fully via structured pinned comparisons and lossless native JSONL decoding. A separate FR869802 / 347300703 search returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored files and remain bounded to these sources.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Successful NCBI taxonomy and sequence APIs, complete marker metadata, the primary PubMed response and LPSN genus text supplied evidence. The same-paper response already fetched in this turn was reread for C65's explicit citation. Failed browser output and search snippets were not used as biological evidence.

No YAML/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota reviews were not reopened.

