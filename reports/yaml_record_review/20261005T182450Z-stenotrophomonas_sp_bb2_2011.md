# YAML Record Review: Stenotrophomonas sp. bB2(2011)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/stenotrophomonas_sp_bb2_2011.yaml`
- Started UTC: 2026-10-05T18:16:15Z
- Finished UTC: 2026-10-05T18:24:50Z
- Verdict: pass

## Target

The full 54-line generated `TaxonRecord` was read, and reread after
the status interruption. It denotes `NCBITaxon:1034559`,
Stenotrophomonas sp. bB2(2011): `SPECIES`, `BACTERIA`,
parent `NCBITaxon:196198`, genetic code 11, `EXACT`
grounding, `SEEDED` status, and `strain_count: 0`.
It is a taxon record, not a genome or culture-deposit record.

Owning inventory and scope rows are
`data/raw/ncbitaxon_taxa.tsv:221668` and
`curation/seed_scope.tsv:321979`.
`data/taxa/PATHS.tsv:14134` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/stenotrophomonas_sp_bb2_2011.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/stenotrophomonas_sp_bb2_2011.yaml --out /private/tmp/sbb2-strict-20261005.tsv`: exit 0; one file, zero files with errors and zero error rows.
- Structured reads verified the full backbone row and ten ancestors, PATHS, scope, source attestation, and seed event. Exact-ID comparisons covered seven raw source inventories plus type material, merged IDs, and dropped records.
- `rg --no-ignore --hidden -n -z -i` searched target ID, full label, slug, and BB2 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All 114 matches were read in full with TSV headers or JSON decoding and reconciled by path and line: 26 raw/scope, 12 name, two BacDive, four StrainInfo, 17 GOLD, 11 BV-BRC, 29 assembly, 12 GTDB, and one AllTheBacteria row.
- A separate ignored-inclusive marker search across those roots found no JF772547 row. Ignored-inclusive filename and content searches under `reports` and `history` found no prior target report or separate target history artifact, including marker searches, before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, full sequence metadata, and three bounded PubMed queries completed. A relevant primary paper was inspected from its publisher PDF after web HTML access failed; the identity-bearing page was also visually checked.
- Not checked in this focused review: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused source agreement does not prove corpus reproduction.
- iModulonDB and curator-added graph ID/label checks are not applicable: the record asserts no gene, regulator, protein, phenotype, transcriptomic result, or causal graph. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

NCBI Taxonomy EFetch and Datasets agree on taxon 1034559, exact label,
species rank, parent 196198, Bacteria division, and code 11.
The complete root-first lineage agrees:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 135614 > 32033 > 40323 > 196198`.
These are root, cellular organisms, Bacteria, Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Lysobacterales, Lysobacteraceae,
Stenotrophomonas, and unclassified Stenotrophomonas.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034559);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034559).

The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31056`.
The backbone supplies no synonyms, retirement target, or direct children.
Exact type-material, merged-ID, and dropped-record checks found no target
rows. The provisional species rank is not evidence of valid nomenclatural
publication; `EXACT` grounds the taxon, not genomic species equivalence.

## Evidence

The sole NCBITAXON attestation agrees in identifier, label, snapshot
2026-09-13, count 1, and unit `NAME`. That count is a source-name
assertion, not a strain or genome count. Scope and the
2026-09-13T17:54:04Z `seed_from_sources` /
`SEEDED_FROM_SOURCES` event agree.

The exact query `txid1034559[Organism:noexp]` returned zero Assembly
items with missing-phrase/no-items diagnostics and one Nuccore item,
UID 333981241. Complete metadata identifies `JF772547.1`,
a 1,514-base partial 16S rRNA sequence, strain bB2, taxon 1034559,
with isolation source rhizosphere. Huang J.'s direct submission is
dated 1 April 2011. Its weathering-related reference is unpublished.
Neither that title nor the submitter address proves a measured
weathering phenotype, host, isolation locality, or culture deposit.
A marker sequence is not a whole-genome accession.
[GenBank JF772547.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772547.1).

PubMed searches for `JF772547[All Fields]`,
`"bB2"[All Fields] AND Stenotrophomonas[All Fields]`, and the
complete weathering-reference title returned zero items, with the
returned query translations and diagnostics inspected. These bounded
misses do not prove that no relevant publication exists.

Exact-name, marker, and strain/genus web searches found a plausible
BB2/BB3 bioremediation lead. Dzionek, Taskin, and Siupka (2025),
DOI `10.3390/app152212052`, identify their BB2 as Raoultella
terrigena and their BB3 as Stenotrophomonas terrae, isolated from
activated sludge in Poland. Publisher PDF pages 3 and 10 explicitly
separate their identities and sequence submissions. GenBank retains
the broader labels: `PP972776.1` is Raoultella sp. BB2,
taxon 1873496, 1,283 bases; `PP972778.1` is Stenotrophomonas
sp. BB3, taxon 69392, 1,293 bases. Both records describe 2023 collection
and 2024 submission. Preserve the paper/GenBank resolution difference.
Neither accession is the target's `JF772547.1`; no degradation,
resistance, locality, or other phenotype is transferred.
[Primary paper](https://doi.org/10.3390/app152212052);
[PP972776.1](https://www.ncbi.nlm.nih.gov/nuccore/PP972776.1);
[PP972778.1](https://www.ncbi.nlm.nih.gov/nuccore/PP972778.1).

## Completeness

The seven exact raw-source checks found no target BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin, or BacTraits row. The wider native search
yielded no independently grounded target deposit, type material,
assembly, or GTDB mapping. Optional nomenclature, synonyms, mappings,
strains, traits, and graphs are appropriately empty for this seeded
record. `strain_count: 0` describes classified inventory coverage;
it does not deny the isolate evidenced by GenBank.

The directly linked marker is a useful bounded enrichment lead, not
a mandatory whole-genome or deposit representation under the local
checklist. It must not be added by hand to generated YAML. No
consequential missing required field was demonstrated. Native BB2
collisions are distinguished below rather than treated as matches.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. Classification disagreements and
suppressed accessions below concern excluded source candidates, not
claims this record makes. Full-corpus reproducibility remains untested.

## Recommended Edits

No required edit is demonstrated. Preserve the generated record and
`SEEDED` status.

For a separately authorized sequence-enrichment task, first define and
test an exact `taxon:1034559` / bB2 / `JF772547.1` association
in maintained extraction inputs and logic
(`scripts/extract_source_inventory.py`, `src/taxonmech/extract.py`),
then update `scripts/seed_from_sources.py` only if needed.
`curation/seed_scope.tsv` owns scope, not inferred strain identity.
Do not turn a marker into an assembly, a sample/project into a strain,
or a bare BB2 string into an equivalence. Do not patch YAML or pages.

## Follow-up Checks

For any future enrichment, re-read versioned GenBank features and
preserve taxon/strain identity; test that the foreign BB2 candidates
remain excluded. Regenerate through the documented maintained pipeline,
then rerun focused schema and strict validation.

Before publishing regenerated corpus products, run the documented
full-corpus reproduction, QC, tests, strict validation, provenance,
history, and site gates. This read-only review neither supplies those
results nor promotes the record.

## Additional Notes

All local matches below were read as full source-native rows. These are
exclusion diagnostics, not additions to the target. Assembly versions,
sample/project distinctions, and classifier disagreements are retained.

**Name and culture collisions.** Besides the target name, native names
identify Pseudomonas BB2-1-31 (taxon 298816), Flavobacterium BB2-3-14
(299267), Pseudomonas BB2-2-35 (380705), Bacteriovorax BB2 (390554),
Halobacillus KK-Bb2 (445794), Rhodobacteraceae BB2 (888405), Enterobacter
BB2 (992912), Paenibacillus BB2 (1285397), Bizionia BB2 (1603301), and
Campylobacter JWC-BB2 (2511998). Their raw backbone/scope rows are not
target evidence.

Lactobacillus panisapium (2012495) has the Bb2-3 name/type-material
collision: backbone line 510036, names shard 0012 line 2428,
type-material lines 77756-77757. BacDive 158390
(`data/bacdive/records.jsonl.gz:80627`) calls the designation Bb203,
lists DSM 102188 / ACCC 19955, type status, and the distinct marker
`KX447147` (1,437 bases, strain Bb2-3). Preserve these source
spellings; no target equivalence follows.

BacDive 17145 (native line 16957; raw line 16958) is Pectinatus
frisingensis BB2, taxon 865, non-type DSM 20761. StrainInfo SI-ID 49679
(native line 37524; DOI `10.60712/SI-ID49679.2`) is published online
and links the available SI-DP 164263 / DSM 20761 to that BacDive ID.
Neither supplies a target sequence.

Other fully read StrainInfo rows are:
- Line 13936: published-online SI-ID 13936, DOI `10.60712/SI-ID13936.2`, Ornithobacterium rhinotracheale (28251), BB2-3263-3 aliases; available SI-DP 54535 / LMG 12591 and SI-DP 54536 / CCUG 30447, the latter tracing origin to 54535; BacDive 146142.
- Line 34281: published-online SI-ID 46289, DOI `10.60712/SI-ID46289.1`, Corynebacterium glutamicum (1718), CNCTC Bb 2/85 alias. Available SI-DP 125652 / ATCC 21798, 218271 / CCM 3856, and 218272 / CECT 70 use taxon 1718, whereas SI-DP 313705 / KCTC 1846 is classified as Brevibacterium (1696). This foreign strain/deposit classification disagreement is preserved.
- Line 138881: published-offline SI-ID 187026, DOI `10.60712/SI-ID187026.1`, Aspergillus wentii (5066), LSHB BB2 / UC 4242 aliases, available SI-DP 466953 / IMI 094146. This incidental native-source collision did not reopen any Eukaryota YAML.

**Assembly and genome-record collisions.** Each pair below is explicitly
paired with identical assembly comparison unless stated otherwise.
All listed assembly rows have latest status except the explicitly
suppressed historical RefSeq. RefSeq rows use umbrella project
`PRJNA224116`; distinct GenBank projects are specified below.
A shared project is not an identity bridge.

| Foreign entity | Assembly, sample, and GenBank project | Further source distinctions |
| --- | --- | --- |
| Photobacterium leiognathi subsp. mandapamensis Ph.BB2, taxon 48408 / species 553611 | `GCA_033447945.1` / `GCF_033447945.1`; `SAMN37845227`; `PRJNA1028546` | Scaffold, 89 contigs / 84 scaffolds; `JAWQHN000000000.1`; BV-BRC 48408.72; GTDB `RS_GCF_033447945.1`, nonrepresentative P. leiognathi, Enterobacterales versus NCBI Vibrionales. |
| Pediococcus inopinatus BB2, taxon 114090 | `GCA_033554055.1` / `GCF_033554055.1`; `SAMN30915678`; `PRJNA881777` | Complete genome, four contigs, no WGS master; BV-BRC 114090.24 with unversioned CP104774-CP104777; GTDB `RS_GCF_033554055.1`, nonrepresentative. |
| Pediococcus acidilactici BB2-4M, taxon 1254 | `GCA_023221555.1` / `GCF_023221555.1`; `SAMN27775835`; `PRJNA832049` | Complete genome, two contigs, no WGS master; BV-BRC 1254.620 with unversioned CP096571/CP096572; GTDB `RS_GCF_023221555.1`, nonrepresentative. |
| Chromobacterium Bb2 | `GCA_014788985.1` / `GCF_014788985.1`; `SAMN16223692`; `PRJNA664546` | Complete genome, one contig, no WGS master. NCBI/GOLD classify C. haemolyticum (394935); BV-BRC 1778675.5 calls C. rhizoryzae (1778675), explicitly linking this assembly/sample and unversioned CP061849. GTDB `RS_GCF_014788985.1` is nonrepresentative C. haemolyticum, Gammaproteobacteria/Burkholderiales versus NCBI Betaproteobacteria/Neisseriales. |
| Brucella melitensis bv. 1 BB2, taxon 644337 / species 29459 | `GCA_003993905.1` / `GCF_003993905.1`; `SAMN03380773`; `PRJNA266086` | Contig, 25 contigs; `JZHK00000000.1`; BV-BRC 644337.10; GTDB `RS_GCF_003993905.1`, nonrepresentative B. melitensis, Rhizobiales/Rhizobiaceae versus NCBI Hyphomicrobiales/Brucellaceae. |
| Brachyspira pulli BB2, taxon 310721 | `GCA_037002885.1` / `GCF_037002885.1`; `SAMN37904148`; `PRJNA1030309` | Contig, 190 contigs; `JAWLQJ000000000.1`; BV-BRC 310721.4; GTDB `RS_GCF_037002885.1`, nonrepresentative, Brachyspiria versus NCBI Spirochaetia. |
| Brevibacillus borstelensis BB2, taxon 45462 | `GCA_058574875.1` / `GCF_058574875.1`; `SAMN54969686`; `PRJNA1416467` | Contig, 187 contigs; `JBUBWW000000000.1`; no target bridge. |
| Staphylococcus aureus UKST63/485, isolate BB2, taxon 1280 | `GCA_001351315.1` / `GCF_001351315.1`; `SAMEA1569618`; `PRJEB2812` | Contig, 22 contigs; `CVHT00000000.1`; GTDB `RS_GCF_001351315.1`, nonrepresentative, Staphylococcales versus NCBI Bacillales. |
| S. aureus BB2-I1-E1, taxon 1280 | `GCA_026831105.1`; `SAMN17580147`; `PRJNA514245` | Contig, 41 contigs; `DAKWNO000000000.1`; no paired RefSeq; large multi-isolate exclusion. Distinct from UKST63/485. |
| Mycoplasmopsis bovis BB-2, taxon 28903 | `GCA_018594575.1` / historical `GCF_018594575.1`; `SAMN11487519`; `PRJNA534329` | Contig, 61 contigs; `SVZW00000000.1`. RefSeq is suppressed, not-live date 2021-06-01; large multi-isolate exclusion. BV-BRC 28903.481 uses Mycoplasma bovis, supplies sample/project/unversioned WGS but no assembly field. |
| Klebsiella variicola subsp. variicola ST3029, isolate BB2, taxon 2590157 / species 244366 | `GCA_050994255.1`; `SAMN43931407`; `PRJNA514245` | Contig, 162 contigs; `DBJDTX000000000.1`; no paired RefSeq; large multi-isolate exclusion. |
| Campylobacter jejuni JWC-BB2, taxon 197 | `GCA_019298015.1`; `SAMN20331730`; `PRJNA327813` | Contig, 63 contigs; `ABBKJH000000000.1`; no paired RefSeq; large multi-isolate exclusion. Do not equate by name with taxon 2511998 or the different ATB sample below. |

The metagenome candidates likewise denote different organisms:
- Thiotrichales bacterium BB2 (2026796): `GCA_016745035.1`, `SAMN16086328`, `PRJNA606180`, `JADGDE000000000.1`, scaffold with 108 contigs / 90 scaffolds, no pair; metagenome/genus-undefined flags. BV-BRC 2026796.40 links those identifiers. GTDB `GB_GCA_016745035.1` is representative `BB2 sp016745035` in Beggiatoales/Beggiatoaceae; its placeholder genus BB2 is not Stenotrophomonas.
- Nitrospina ETSP2013-BB2-NOB-2 (2024844): `GCA_005239385.1`, `SAMN10411419`, `PRJNA505148`, `RSAC00000000.1`, 186 contigs, no pair; BV-BRC 2024844.16. GTDB `GB_GCA_005239385.1` is nonrepresentative `Nitromaritima sp002731985`.
- Nitrospina ETSP2013-BB2-NOB-1 (2024844): `GCA_005239395.1`, `SAMN10411459`, the same project, `RSAB00000000.1`, 213 contigs, no pair; BV-BRC 2024844.17. GTDB `GB_GCA_005239395.1` is nonrepresentative `Nitromaritima sp003451695`. These two samples and GTDB species remain distinct.
- Lutibacter MAG-BB-2 (1925666): `GCA_004195315.1`, `SAMN10805734`, `PRJNA510104`, `SDWL00000000.1`, scaffold with 539 contigs / 538 scaffolds, no pair; metagenome and failed MAG-completeness annotation flags. BV-BRC 1925666.9 links it; GTDB `GB_GCA_004195315.1` is representative `Lutibacter sp004195315`, Bacteroidia versus NCBI Flavobacteriia.

Numeric 1034559 matches are genome-length fields, not target taxon IDs:
Mycoplasmopsis bovis WB11 (28903), `GCA_056106205.1` /
`GCF_056106205.1`, `SAMN50701155`, `PRJNA820789`,
`JBWBCD000000000.1`, complete genome with one contig; uncultured
bacterium MarMAG_046729 (77133), `GCA_977311165.1`,
`SAMEA120697810`, `PRJEB104710`, `CDTEIH000000000.1`,
scaffold with 110 contigs / 105 scaffolds, no pair; and uncultured
Actinomycetes LaPlata-5m-b_bin-487 (152507), `GCA_903871375.1`,
`SAMEA6950384`, `PRJEB38681`, `CAIQGO000000000.1`,
153 contigs, no pair. The last two are metagenome/genus-undefined
candidates. GTDB `GB_GCA_903871375.1` is nonrepresentative
`Nanopelagicus sp903897475`. WB11 is not the BB-2 sample above.

**GOLD chains.** Full organisms/project/analysis rows distinguish:
- `Go0501959 > Gp0386185 > Ga0363998`: S. aureus UKST63/485/BB2; `PRJEB2812`, `SAMEA1569618`, explicit `GCA_001351315.1` and unversioned CVHT00000000; isolate analysis.
- `Go0540194 > Gp0491037 > Ga0445892`: B. melitensis BB2; `PRJNA266086`, `SAMN03380773`, explicit `GCA_003993905.1`, unversioned JZHK00000000, IMG 2978364937; isolate analysis.
- `Go0635530 > Gp0652993 > Ga0561818`: C. haemolyticum Bb2; `PRJNA664546`, `SAMN16223692`, explicit `GCA_014788985.1`, unversioned CP061849; isolate analysis. This preserves, not resolves, the BV-BRC classification disagreement.
- `Gp0489745 > Ga0438677 / Ga0438715`: fungal community Bb2; `PRJNA650613`, `SAMN15719995`; metatranscriptome and self-mapping analyses, IMG 3300039280 only on Ga0438677, empty assembly lists and organism links.
- `Gp0631125 > Ga0555791`: forest-soil community BB2.s.6.1; `PRJEB21441`, `SAMEA104135872`; metagenome analysis, empty assembly list and organism link.
- Organism-only collisions are `Go0182858` C. glutamicum CNCTC Bb 2/85 (1718), `Go0235115` O. rhinotracheale BB 2-3263-3 (28251), and `Go0235117` O. rhinotracheale du Preez BB 2-3263-3 (28251). Culture-collection fields are empty; similar names alone do not establish a target deposit.

**AllTheBacteria.** Full TSV row
`data/catalog/allthebacteria.tsv.xz:1543697` describes
Campylobacter sp. JWC-BB2, `ERZ25535630`, `SAMN10869125`,
run `SRR8526912`, dataset r0.2, assembly pipeline PASS.
Current HQ/Sylph filters are `SYLPH_RESULTS_FAIL`, current Sylph
species unknown, while pre-202505 species is Campylobacter_D jejuni
and prior HQ flag is T. Its sample differs from the JWC-BB2 assembly
sample `SAMN20331730`; no unsupported same-name bridge is made.

The strongest primary literature lead and exact public sequence queries
were checked, not every generic web co-occurrence. No paid research,
outbound contact, GitHub mutation, YAML/inventory/scope/history edit,
status promotion, regeneration, or Eukaryota-record review occurred.
