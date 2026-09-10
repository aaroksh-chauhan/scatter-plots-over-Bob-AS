# T-S Diagram Analysis: Arabian Sea vs Bay of Bengal

## Overview
This project constructs and compares Temperature-Salinity (T-S) diagrams for 
the Arabian Sea and the Bay of Bengal, using the TEOS-10 standard for seawater 
properties, to understand differences in water mass characteristics between 
the two basins.

## Objective
- Compare the temperature-salinity relationship between the Arabian Sea and 
  Bay of Bengal
- Visualize seawater density (sigma-0) using isopycnal contours on the T-S plots
- Mark the freezing point and temperature of maximum density on the diagrams
- Map the global thermal expansion coefficient of seawater

## Data
- **Source:** ORAS5 (Ocean Reanalysis System 5) SST and SSS (Sea Surface Salinity) 
  datasets
- **Time period:** 1990–2008
- **Regions:** Arabian Sea (8°N–27°N, 50°E–75°E) and Bay of Bengal (4°N–24°N, 
  76°E–100°E)

## Tools & Methods
- **Language:** Python
- **Key libraries:** xarray, numpy, matplotlib, cartopy, gsw (TEOS-10 seawater 
  toolbox)
- **Method:** Converted practical salinity and temperature to absolute salinity 
  and conservative temperature using the gsw library, computed potential density 
  (sigma-0), and plotted T-S scatter diagrams with density contour lines for 
  both regions

## Results
- The T-S diagrams show clear differences between the Arabian Sea and Bay of 
  Bengal, reflecting the Bay of Bengal's typically fresher surface waters 
  (due to river runoff and monsoon rainfall) compared to the more saline 
  Arabian Sea
- The thermal expansion coefficient map highlighted spatial variation in how 
  strongly seawater expands with temperature across the globe

## Skills Demonstrated
- Oceanographic data analysis using TEOS-10 seawater standards
- Working with gridded ocean reanalysis data (NetCDF)
- T-S diagram construction and interpretation
- Scientific visualization using Python

## Author
Aaroksh Chauhan — M.Sc. Atmospheric and Oceanic Sciences, IIT Bhubaneswar
