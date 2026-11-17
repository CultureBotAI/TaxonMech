# YAML Record Review: Anoxybacillus sp. enrichment culture clone GXS-3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/anoxybacillus_sp_enrichment_culture_clone_gxs_3.yaml`
- Started UTC: 2026-10-07T17:06:52Z
- Finished UTC: 2026-10-07T17:13:17Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036017`,
Anoxybacillus sp. enrichment culture clone GXS-3. It asserts species
rank, bacterial domain, parent 263859, ten ancestors, code 11,
`EXACT` grounding, `SEEDED` lifecycle, zero inventoried BacDive
strains, one NCBITAXON name attestation and one inline seed event.
No synonyms, nomenclature, taxonomy mappings, strain/genome objects,
literature evidence, phenotypes or causal graph are asserted.
The target is a named enrichment-culture clone, not an assumed
deposited pure strain.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/anoxybacillus_sp_enrichment_culture_clone_gxs_3.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/anoxybacillus_sp_enrichment_culture_clone_gxs_3.yaml --out /private/tmp/gxs3-strict.tsv`: passed, one file, zero errors; complete header-only diagnostics read.
- Structured backbone, lineage, scope, path, attestation and inline wording checks passed. These are bounded checks, not full corpus reproduction.
- NCBI taxonomy XML/Datasets JSON, exact Assembly/Nuccore indexes, full target marker metadata, complete GXS-BL gene metadata, GXS-BL live taxonomy and full PMID 30652633 abstract/identifier metadata were read.
- The 2019 primary manuscript's Materials, experimental context and reference 25 were inspected through its author-uploaded full text. Direct PMC open returned a browser challenge; it was not bypassed.
- `just validate-products`: not applicable, no curator-added graph terms; taxonomy correspondence checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content/path searches; inline history passed schema, strict and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- Not checked: independent sequencing/culture authentication, experimental reproducibility, a rendered manuscript PDF, or the full 2017 AmyGX paper cited by reference 25. Bounded searches did not retrieve that original paper.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036017&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036017)
confirm active exact identity, species rank, parent 263859 and code 11.
EFetch's Environmental samples division does not contradict
`taxon_domain: BACTERIA`, which is lineage-derived.

Pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222255`,
`data/catalog/ncbi_names-0005.jsonl.gz:31768`,
`data/taxa/PATHS.tsv:14753` and `curation/seed_scope.tsv:322512`.
The native scientific-name row has empty unique name. Source synonym
columns, live alternate-name fields and retirement are empty; the
snapshot is 2026-09-13.

All ten ancestors agree in order, labels, ranks and parent links:
root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli,
Caryophanales, Anoxybacillaceae, Anoxybacillus and environmental samples.
No target children, type-material, merged-ID or dropped rows occur in
the parsed inventories. Species rank does not assert valid publication
of a formal species name or convert the clone into a type strain.
Exact grounding is distinct from curatorial lifecycle.

## Evidence

The attestation correctly counts one NCBITAXON `NAME`. Exact-target
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories
contain no rows. With no descendants, zero inventoried BacDive strains
is supported, without implying biological absence of cultures.

The scope and attestation reproduce the inline event wording.
The seed function and three source-manifest timestamps reread this
turn support 2026-09-13T17:54:04Z as the newest extraction timestamp,
not review time: `src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1036017[Organism:noexp]` returns UID
334085711, [JF831203.1](https://www.ncbi.nlm.nih.gov/nuccore/JF831203.1).
Complete metadata describes a 1,520-nt partial 16S marker with
clone GXS-3, taxon 1036017, environmental-sample flag, hot spring,
and location China: Guangxi. Its sole reference is Liao and colleagues'
direct submission on 14 April 2011; creation/update are 31 May 2011.
There is no strain qualifier, culture collection, BioSample,
BioProject, publication DOI or PMID in that metadata.
The marker is neither an assembly nor evidence testing translation code.

The inspected [2019 primary manuscript, section 2.1](https://www.researchgate.net/publication/330474893_Influence_of_Calcium_Ions_on_the_Thermal_Characteristics_of_a-amylase_from_Thermophilic_Anoxybacillus_sp_GXS-BL)
cites JF831203 for its Anoxybacillus sp. GXS-BL gene donor, described
as isolated at Tengchong hot spring in Yunnan. This is an exact-accession
link but disagrees with GenBank's clone designation and Guangxi location.
[PubMed](https://pubmed.ncbi.nlm.nih.gov/30652633/) confirms PMID 30652633,
PMCID PMC6416487 and DOI 10.2174/0929866526666190116162958.
The experiment concerns recombinant alpha-amylase expressed in E. coli,
not a demonstrated whole-organism phenotype of clone GXS-3.

Searching Nuccore for the exact GXS-BL name returns UID 351000213,
[JF946749.1](https://www.ncbi.nlm.nih.gov/nuccore/JF946749.1).
Its complete metadata describes a 1,518-nt alpha-amylase CDS,
protein AEQ38578.1, strain GXS-BL, and taxon 1094758. The location
string combines Tengchong hot spring, Guangxi and Yunnan province;
that wording does not resolve the discrepancy. Direct submission
is 11 May 2011, creation/update 18 October 2011. No culture deposit,
BioSample, BioProject or publication identifier is supplied.

[Live GXS-BL taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1094758&retmode=xml)
confirms a separate active species-rank taxon under unclassified
Anoxybacillus, parent 2639704, rather than environmental parent 263859.
Local backbone, scientific-name and scope rows independently retain
that separate identity. Shared authors, a paper's marker citation and
similar names do not authorize taxon equivalence or an enzyme/genome
transfer. The gene accession is not a genome assembly.

Exact Assembly search for the target returned zero with
phrase-not-found/no-items warnings, not proof of worldwide absence.

## Completeness

The generated NCBI identity representation is sound. The consequential
uncertainty is the accession-linked donor/clone provenance conflict
below, not an established missing strain, synonym, genome or phenotype.

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/` and `history/`, including ignored, hidden and compressed
content. Searches covered taxid, full-name slug, GXS-3 separator
variants, JF831203, GXS-BL, PMID/DOI, JF946749 and AEQ38578.
The initial 76 candidates expanded to 79; every candidate row was
fully read, using lossless common-fields/value-columns displays:

- Three rows describe the target backbone, scope and native name.
- Eight name/backbone/scope/legacy-path rows concern Pseudomonas sp. GXS3, taxid 1849457, or Thaumarchaeota archaeon JGI MDM2 GXS-3-L12, taxid 1955636, including its Aigarchaeota synonym. Neither is the target.
- Twenty-two GOLD rows are seven organism/project chains and eight screened/unscreened analyses for JGI MDM2 GXS-3-L12, E14, E6, G14, I8, L14 and M13. Their taxa are 1955636 or 77133, their culture-collection fields are empty, and their explicit Go/Gp/Ga and IMG chains do not name Anoxybacillus clone GXS-3.
- Thirty-three rows, comprising 14 BV-BRC, nine GTDB and ten GenBank entries, concern pig-gut MAGs in PRJEB52643 with BioSamples SAMEA110360170 through SAMEA110360179. Sample digits cause the taxid substring match; their full metadata instead identifies uncultured Bacillota, Bacteroidales, Clostridia, Anaerosporobacter or Ruminococcus.
- Nine GenBank/historical RefSeq rows concern Salmonella GXS379, GXS378, GXS340, gxS391, gxS351 and gxS384, taxa 28901/440524. Longer strain names match the permissive search; the three historical RefSeq rows are suppressed. None establishes the target identity.
- GenBank shard 0054 line 17276 describes Streptococcus pneumoniae, taxid 1313, GCA_058711325.1, SAMEA120831650 and PRJNA514245. Its isolate string is 1036017, not its taxonomy identifier.
- The three added rows describe GXS-BL: `data/raw/ncbitaxon_taxa.tsv:235402`, `data/catalog/ncbi_names-0005.jsonl.gz:47694`, and `curation/seed_scope.tsv:333665`, all taxid 1094758.

Adding JF946749/AEQ38578 produced no further rows. Five native
`SOURCE.json` objects were fully parsed at all three stages, with
independent history-filename searches. No target history artifact or
additional supported deposit/strain-genome relationship was found
in these bounded roots. No global absence is claimed.

iModulonDB is not applicable: the reviewed record asserts no gene,
regulator, expression module or transcriptomic dataset. The unresolved
GXS-BL enzyme relationship does not establish a covered target dataset.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**Minor: unresolved accession-linked strain/clone provenance conflict.**
The literature associates the target marker with another donor name
and location, while NCBI retains distinct GXS-3 and GXS-BL taxon IDs.
Their equivalence and precise isolation provenance remain unverified.
This is an external-source/provenance issue, not proof that the
generated taxon denotes the wrong NCBI concept. It blocks confident
GXS-BL synonym or functional enrichment, not retention of this record.

Owner: primary NCBI sequence/taxonomy provenance and the originating
study, followed only after resolution by maintained extraction or
seeding logic in `src/taxonmech/extract.py` and
`src/taxonmech/seed.py`. A future evidence-preserving curator overlay
would require explicit implementation/authorization; generated YAML
and pages are not the correction surface.

## Recommended Edits

Do not rename, merge, add GXS-BL as an exact synonym, add the
alpha-amylase as a target assertion, or fabricate a deposit/genome link.
Retain both source accounts in this report pending accession-specific
clarification. A separately authorized source correction should
identify which clone/strain and sampling location each accession
represents before changing maintained inputs. Preserve `SEEDED`.

## Follow-up Checks

Inspect the original 2017 AmyGX study and any public corrected
submission metadata for an explicit GXS-3-to-GXS-BL identity chain.
Recheck both accession records and both taxon IDs, including clone,
strain, collection and location qualifiers. Shared submitters alone
are insufficient; no contact with authors or maintainers was made.

After an authorized upstream correction, refresh the owning inputs,
rerun the generator and schema/strict checks, then applicable corpus
reproduction/provenance gates. New history requires
`just validate-history`; new graph terms/evidence require
`just validate-products`. Preserve unresolved alternatives rather
than selecting a convenient location or taxon.

## Additional Notes

The whole YAML was reread and remained byte-identical before report
creation. All retrievals and full candidate reads reached terminal
outcomes. Only this new report is added. No source, YAML, lifecycle,
history, page, GitHub, branch or worktree was changed, and Eukaryota
was not re-reviewed. GXS-BL was inspected solely to disambiguate this
record; this is not a separate review of its generated YAML.
