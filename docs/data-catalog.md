# Data Catalog

## Raw Data

- [`data/raw/Kerncijfers_2023.csv`](../data/raw/Kerncijfers_2023.csv)
  Source: neighborhood key figures used during dataset assembly.
  Used by: [`01_build-analysis-dataset.ipynb`](../notebooks/01_core/01_build-analysis-dataset.ipynb)
- [`data/raw/boundaries/wijken_en_gemeenten.gpkg`](../data/raw/boundaries/wijken_en_gemeenten.gpkg)
  Source: canonical Amsterdam neighborhood and municipality boundaries.
  Used by: [`02_crime-choropleth.ipynb`](../notebooks/01_core/02_crime-choropleth.ipynb), [`03_spatial-autocorrelation.ipynb`](../notebooks/01_core/03_spatial-autocorrelation.ipynb), [`04_ridge-model.ipynb`](../notebooks/01_core/04_ridge-model.ipynb)
- [`data/raw/crime_monthly/`](../data/raw/crime_monthly/)
  Source: monthly neighborhood crime extracts used in the early crime aggregation workflow.
  Used by: archived crime preparation notebooks
- [`data/raw/trees/bomen-stamgegevens.csv`](../data/raw/trees/bomen-stamgegevens.csv)
  Source: tree point dataset used to derive neighborhood tree indicators.
  Used by: archived tree preparation notebooks

## Intermediate Data

- [`data/intermediate/total_table.csv`](../data/intermediate/total_table.csv)
  Role: assembled working table used during dataset construction.
  Used by: [`01_build-analysis-dataset.ipynb`](../notebooks/01_core/01_build-analysis-dataset.ipynb)
- [`data/intermediate/bomen_per_wijk.csv`](../data/intermediate/bomen_per_wijk.csv)
  Role: neighborhood tree aggregation.
  Used by: [`01_build-analysis-dataset.ipynb`](../notebooks/01_core/01_build-analysis-dataset.ipynb)
- [`data/intermediate/df_crime_average_per_year.csv`](../data/intermediate/df_crime_average_per_year.csv)
  Role: aggregated neighborhood crime table from the monthly source files.
  Used by: archived crime and matching notebooks
- [`data/intermediate/licht_met_wijk.csv`](../data/intermediate/licht_met_wijk.csv)
  Role: intermediate lighting join output.
  Used by: archived lighting notebooks
- [`data/intermediate/LICHTPUNTEN_met_wijk.csv`](../data/intermediate/LICHTPUNTEN_met_wijk.csv)
  Role: lighting points assigned to neighborhoods.
  Used by: archived lighting and matching notebooks
- [`data/intermediate/LICHTPUNTEN_met_wijkdata_merged.csv`](../data/intermediate/LICHTPUNTEN_met_wijkdata_merged.csv)
  Role: merged lighting-neighborhood table used during exploratory analysis.
  Used by: archived ideation notebook
- [`data/intermediate/datapoging2.csv`](../data/intermediate/datapoging2.csv)
  Role: exploratory intermediate table used during distance-feature development.
  Used by: archived distance-feature notebook
- [`data/intermediate/total_final_df.csv`](../data/intermediate/total_final_df.csv)
  Role: near-final analysis table used before creating the model-ready dataset.
  Used by: [`01_build-analysis-dataset.ipynb`](../notebooks/01_core/01_build-analysis-dataset.ipynb) and archived distance-feature notebook

## Final Data

- [`data/final/df_final_model.csv`](../data/final/df_final_model.csv)
  Role: final neighborhood-level model dataset.
  Used by: [`02_crime-choropleth.ipynb`](../notebooks/01_core/02_crime-choropleth.ipynb), [`03_spatial-autocorrelation.ipynb`](../notebooks/01_core/03_spatial-autocorrelation.ipynb), [`04_ridge-model.ipynb`](../notebooks/01_core/04_ridge-model.ipynb)

## Archive

- [`data/archive/wijken_en_gemeenten_crime_source.gpkg`](../data/archive/wijken_en_gemeenten_crime_source.gpkg)
  Role: second historical geopackage retained because it differs from the canonical boundary source.
  Used by: none of the curated notebooks
