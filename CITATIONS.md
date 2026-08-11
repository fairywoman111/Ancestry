# Citations

Every dataset brought into the project gets an entry here. Record **source, access date,
version, and license** at minimum. This is the single place to check provenance for any
figure in the analysis.

## Template

```
### <Short name>
- **Full title / publisher:**
- **URL:**
- **Version / vintage:** (e.g. ACS 2023 5-year)
- **Accessed:** YYYY-MM-DD
- **License / terms:**
- **Required citation text:** (if the source mandates specific wording)
- **Used in:** (phase / notebook / table)
- **Notes:**
```

---

## Entries

### ACS 5-year — B03002 (Hispanic or Latino Origin by Race), state level
- **Full title / publisher:** U.S. Census Bureau, American Community Survey (ACS) 5-year
  estimates, table B03002 "Hispanic or Latino Origin by Race"
- **URL:** https://api.census.gov/data/2023/acs/acs5 (API); https://data.census.gov (portal)
- **Version / vintage:** ACS 2023 5-year (adjust `--year` for other vintages)
- **Accessed:** _pending first run_ (stamp the date when the data is actually pulled)
- **License / terms:** U.S. Government public domain data; cite the Census Bureau as source
- **Required citation text:** "U.S. Census Bureau, American Community Survey (ACS) 5-Year
  Estimates, Table B03002."
- **Used in:** Phase 1 — `scripts/fetch_census_baseline.py`,
  `notebooks/01_macro_census_baseline.ipynb`; output
  `data/tier1_census/acs2023_5yr_state_macro_race_ethnicity.csv`
- **Notes:** Chosen because it separates Hispanic/Latino origin from race, yielding
  mutually exclusive macro categories (OMB-1997 style).
