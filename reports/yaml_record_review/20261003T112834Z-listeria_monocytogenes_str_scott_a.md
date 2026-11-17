# YAML Record Review: Listeria monocytogenes str. Scott A

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/listeria_monocytogenes_str_scott_a.yaml`
- Started UTC: 2026-10-03T11:26:39Z
- Finished UTC: 2026-10-03T11:28:34Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1027396`, Listeria monocytogenes
str. Scott A, rank STRAIN, domain BACTERIA, parent `NCBITaxon:1639`.
The entire 86-line YAML was read. It has EXACT grounding, SEEDED mapping
status, one GTDB mapping, two exact synonyms, one GTDB xref, zero listed
BacDive strains, four source attestations and an embedded seed event.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/listeria_monocytogenes_str_scott_a.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/listeria_monocytogenes_str_scott_a.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive identifier, label and slug searches found no target history entry. Strict validation covered the embedded event. |

All ten lineage entries matched the complete pinned taxonomy table.
Full subtree traversal found the target alone; complete BacDive inventory
inspection found no strain classified within that subtree. These checks
support the listing/count contract, not GTDB species/strain equivalence.

## Identity and Grounding

Raw taxonomy row 218807 supports the target identifier, label, STRAIN rank,
parent, code 11 and the expanded Scott A name. The inspected
[NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1027396)
confirms ID, name, code, equivalent form and lineage. Its browser rank
is no rank rather than the snapshot's STRAIN. The original configured
taxdump archive is unavailable under the inspected `data/` tree, so
this source-version difference is not attributed to an importer defect
without replay. No taxonomic rank is inferred from the label itself.

Native NCBI names contain the scientific name and one equivalent name,
matching the YAML's NCBI synonym. The exact GTDB synonym is different:
`Listeria monocytogenes B` represents the source cluster
`s__Listeria monocytogenes_B`, not an alternate name for Scott A alone.
The NCBI Caryophanales lineage is retained even though native GTDB
uses Lactobacillales; the repository does not reconcile the two trees.

## Evidence

**GTDB cluster.** Ignored-inclusive decompressed search across all native
GTDB genome shards, followed by exact terminal-species filtering, found
2,321 members of `s__Listeria monocytogenes_B` across 56 NCBI taxids.
Of those, 2,262 bear species taxid 1639, one bears target taxid 1027396,
and 58 bear other taxids. The representative is RS_GCF_000307025.1,
ATCC 19117, taxid 882095, not Scott A.

The sole target-taxid member, RS_GCF_000212455.1, names Scott A,
GCA_000212455.1, SAMN02415240 and PRJNA224116. Raw mapping row 1214
supplies the closeMatch and 2,321 count used in the YAML. The count
reproduces species-cluster membership, not Scott A genome coverage.
The GTDB web endpoint was inaccessible; the complete inspected native
cluster nevertheless disproves exact species/strain identity.

**Native NCBI genome context.** Current GenBank/RefSeq objects retain the
paired GCA/GCF_000212455.1 chromosome assembly ASM21245v1, `strain=Scott A`,
target taxid 1027396, species taxid 1639 and SAMN02415240. Projects are
PRJNA66415/PRJNA224116 respectively. Both retain AFGI00000000.1 and
PMID 21685277. The NCBI taxonomy page identifies the associated genome
publication, but the direct PubMed request returned a browser challenge;
no uninspected publication text supports this verdict.

The same native GenBank taxid search also found GCA_923172565.1, LMN-5,
and GCA_923174355.1, LMN-28. They bear the target taxid but different
verbatim strain identifiers and small assembly sizes; their RefSeq
exclusion fields retain source quality warnings. These are source
classification facts, not evidence that the three submissions are
equivalent genomes or interchangeable cultures. They are not asserted
as links in the target YAML.

**GOLD organism count and join boundary.** Raw GOLD row 333 attests one
ORGANISM directly under the target. Native Go0010773 explicitly names
Listeria monocytogenes sv. 4b Scott A, target taxid 1027396 and culture
CCUG 32843. Gp0010773 links that organism to PRJNA66415 and SAMN02415240.
Ga0019593 names the project and supplies GCA_000212455.1, CM001159 and
IMG 2547132095. Its empty organism field does not conflict with the
explicit project chain. Other native objects named Scott A, including
Go0287316, Go0288883, Go0289322 and Go0289630, are classified under the
parent species; Go0288826 says Petite Scott A. Neither names nor
co-occurrence authorize summing them into this target's direct count.

The culture parser recognizes CCUG 32843, but ignored-inclusive searches
found no such deposit in the raw BacDive/culture inventories or the native
BacDive catalog. The direct CCUG page request was inaccessible. The
recognized token alone therefore cannot create a link to an existing
BacDive strain. Bare Scott A also fails the culture-accession matcher.
The unjoined GOLD chain remains available in its native source catalog.

**Where the BacDive strain is retained.** Raw BacDive row 57597 and the
full native object 135291 classify designation Scott A at parent species
taxid 1639, not this child. They supply CIP 103575 and CECT 5672,
explicit native type status no, and the CECT 5672 AJ515514 16S reference.
The inspected [BacDive page](https://bacdive.dsmz.de/strain/135291)
confirms the designation, those deposits and species classification.
Its extracted heading text alone is not used to override the explicit
native type boolean or LPSN's type identity.

Native StrainInfo 69212.2, DOI 10.60712/SI-ID69212.2, owns available
CIP 103575 (DP152547) and CECT 5672 (DP295665), both type false at
species taxid 1639. AJ515514 explicitly names both deposits. A structured
projection of the parent record confirms BacDive 135291 is retained
there with both cultures, four GOLD organism assertions, two AJ515514
assertions and four StrainInfo strain/deposit assertions. It has no
assembly or genome-record links. This projection is contextual evidence,
not a review of the full parent record.

**Nomenclature and audit.** Raw LPSN row 17903 and the inspected
[LPSN species page](https://lpsn.dsmz.de/species/listeria-monocytogenes)
concern parent taxid 1639, name 777590. Type deposits include ATCC 15313,
DSM 20600 and CCUG 15526, not Scott A's deposits. The raw LPSN GTDB
cross-reference is the unsuffixed species concept, not proof of identity
between the `_B` cluster and this strain. No own nomenclature or type
flag should be invented for Scott A from the species-type linkouts.

Madin row 514 contributes five TRAIT_ASSERTIONs; NCBI contributes one
NAME, GOLD one ORGANISM and GTDB the cluster-sized GENOME count above.
Scope row 26049 and the embedded event name those same four sources.
The units remain separate and do not themselves assert strain phenotypes.

## Completeness

Zero listed strains follows the complete source-classified subtree.
It does not mean the biological strain has no BacDive entry or genome:
the species record holds the BacDive/StrainInfo deposits, and the native
NCBI/GOLD/GTDB catalogs hold genome context. Moving parent-classified
strains or joining genomes by the shared Scott A name would cross the
documented identity boundary. The target has no supported listed-strain
BioSample assertion from which an ATB join could be derived.

Ignored-inclusive searches covered the target ID, label and slug in
raw inventories, curation and history. There was no target history entry
or earlier report. Searches for CCUG 32843 covered raw strain and culture
inventories, raw link inventories and the decompressed native BacDive
catalog. Source absence is claimed only for those inspected inputs.
The ignored-inclusive filename search of `data/` found neither the
pinned original taxdump archive nor `nodes.dmp`.

Optional definition, discussion, curator evidence and graph slots are
appropriately empty. iModulonDB was not applicable to the target YAML:
it asserts no gene, regulator, pathway or transcriptomic dataset. A
browser's GEO links are not themselves such an assertion.

## Findings

**Major M1: a GTDB species cluster becomes exact strain identity.** The
2,321-member, 56-taxid `_B` cluster becomes an EXACT_SYNONYM and an
equivalence xref on Scott A. Only one native member has this target
taxid. This loses the essential distinction between a strain and its
wider species cluster. The GENOME attestation must not be interpreted
as strain-specific coverage either.

Maintained owners: the upstream kg-microbe GTDB transform feeding
`data/raw/gtdb_mappings.tsv`, and the rank-agnostic identity block in
`src/taxonmech/seed.py:438`. The condition at line 451 accepts closeMatch
as identity; xref and exact-synonym emission follow from line 467.
A generated YAML edit would leave that behavior reproducible.

Finding counts: 0 blocker, 1 major, 0 minor. Browser/snapshot rank
differences, inaccessible CCUG/publication pages and unjoined native
genome context are preserved as limitations, not extra proven defects.

## Recommended Edits

1. Make GTDB identity promotion rank- and scope-aware in the maintained
   seeder. Keep `_B` species-cluster context without treating it as an
   exact name or equivalent identifier for Scott A.
2. Correct upstream mapping semantics and explicitly retain cluster
   scope on counts. Use Scott A and its 2,321-member cluster as a
   regression fixture, preserving a valid species-level positive control.
3. Resolve the NCBI rank difference from the hash-verified pinned
   taxdump before a separate inventory correction. Do not fill strain
   or genome gaps through bare-name or type-strain-linkout transfers.

## Follow-up Checks

1. Verify removal of unsupported exact species equivalence while
   retaining the target's valid NCBI identity, lineage and name.
2. After maintained fixes, run the documented dry-run/canary workflow,
   both focused validators and `just verify-corpus`. Confirm parent
   BacDive/StrainInfo associations and native GOLD context remain intact.
3. Inspect authoritative CCUG source text if proposing a future explicit
   deposit association. Any broader source-identity model needs its own
   provenance and tests, not an ad hoc record patch.

## Additional Notes

Only this new report was manually written. No YAML, inventory, scope,
status or history event was changed. Strict validation emitted its normal
diagnostic TSV. No paid research or GitHub mutation was performed.
Eukaryota was outside the target.
