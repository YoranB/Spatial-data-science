# EPA 122A Spatial Data Science  
## Final Project: Urban Design and Crime Exposure in Amsterdam

This repository contains the code, data processing steps, exploratory spatial analysis, and modelling work for the final project of the course **EPA 122A Spatial Data Science (2025–2026)**.

The project follows the full spatial data science workflow as required in the course, including problem formulation, data collection, exploratory data analysis (EDA), spatial analysis, modelling, and interpretation.

## Project Description

This project is titled **A Spatial Analysis of How Urban Design Shapes Crime Exposure in Amsterdam**. It studies how neighbourhood crime in Amsterdam is distributed across space and whether specific features of the built environment help explain differences in neighbourhood-level crime exposure.

**What we know:** crime is spatially patterned and linked to urban form and socio-economic vulnerability.  
**What we do not know:** how specific elements of Amsterdam’s built environment contribute to neighbourhood crime exposure in a measurable way.

**Main research question:**  
**How is neighbourhood crime spatially clustered in Amsterdam, and how well can environmental design features (green space, lighting, distance to facilities) predict neighbourhood crime rates?**

The project uses **Exploratory Spatial Data Analysis** to test and visualise clustering (Global Moran’s I and LISA), and then applies a **regularised regression model (ridge regression)** to evaluate predictive performance under correlated predictors. The analysis uses neighbourhood-level crime rates and built-environment indicators including **tree density**, **streetlight density**, and **mean distance to groups of**


## Research Focus

The project addresses the following elements required by the course:

- a clearly formulated project question derived from the provided project theme  
- spatially explicit data sources  
- exploratory spatial data analysis  
- visualisation of spatial patterns  
- baseline modelling and interpretation of results  

The exact research question is refined during the EDA phase and documented in the notebooks.

## Repository Structure

Each notebook corresponds to a specific stage in the data science workflow and can be read independently.

## Methods and Techniques

The project applies the following spatial data science methods:

- data cleaning and reconciliation of spatial datasets  
- spatial joins and feature engineering  
- choropleth mapping and spatial visualisation  
- exploratory spatial data analysis  
- spatial autocorrelation analysis  
- baseline statistical or machine learning models using spatial features  

All analyses are conducted in Python using standard spatial data science libraries.

## Software and Environment

The project is implemented in Python. Key libraries include:

- pandas and numpy  
- geopandas  
- matplotlib and seaborn  
- scikit-learn  
- spatial analysis libraries where applicable  


