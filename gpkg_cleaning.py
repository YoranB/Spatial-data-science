import geopandas as gpd


# Input file is deleted, because it was too big to upload to Github
input_file = "data/wijkenbuurten_2023_v3.gpkg"
output_file = "alleen_wijken.gpkg"

gdf = gpd.read_file(input_file, layer='wijken', engine='pyogrio')

gdf.to_file(output_file, driver='GPKG', engine='pyogrio')

print(f"Klaar! Opgeslagen als {output_file}")