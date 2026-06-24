# Data

Datasets are organized into **tiers** that match the phases in [`../ROADMAP.md`](../ROADMAP.md)
and the source catalog in [`../DATA_SOURCES.md`](../DATA_SOURCES.md).

| Folder | Tier | Used in | Contents |
| --- | --- | --- | --- |
| `tier1_census/` | 1 — Census / demographic | Phase 1 | Census, ACS, IPUMS, Pew, ARDA, CDC |
| `tier2_genetics/` | 2 — Modern population genetics | Phase 2 | 1000 Genomes, HGDP, gnomAD, ALFRED |
| `tier3_historical/` | 3 — Historical / origins | Phase 3 | SlaveVoyages, immigration records, Maddison, UN migration |
| `tier4_ancient/` | 4 — Ancient / deep-time genetics | Phase 4 | AADR, archaic genomes, ISOGG / PhyloTree / YFull |

## Conventions

- **Everything lives in the repo.** Census tables, historical extracts, and *derived*
  genetic tables (allele frequencies, admixture proportions, haplogroup counts) are all
  small — commit them normally, alongside the scripts/notebooks that produce them. The repo
  is meant to be self-contained and reproducible from a clone.
- **The one exception: raw genomic dumps.** Full VCFs / BAMs / ancient-DNA source files are
  gigabytes+ and exceed GitHub's 100MB-per-file limit, so they are gitignored. Instead of
  the file, commit a **citation + download pointer** in [`../CITATIONS.md`](../CITATIONS.md)
  and the code that turns the raw source into the small derived table we keep.
- **Every dataset gets a citation entry** in [`../CITATIONS.md`](../CITATIONS.md) — source,
  access date, version, and license.
- **Mark interpretation.** Derived or inferred figures are labeled as such, never presented
  as reported fact (see the honesty note in `../ROADMAP.md`).
