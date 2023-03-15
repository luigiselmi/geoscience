Geospatial Data Science
=======================
This repository contains Jupyter notebooks with Python code about geoscience and remote sensing. Many notebooks come from the book [*Geoprocessing with Python*](https://www.manning.com/books/geoprocessing-with-python) by Chris Garrard, others are my experiments with open geospatial datasets. The topics of the notebooks follows those in the book plus others common in geostatistics.

* [Coordinate reference systems](coordinate_reference_system.ipynb)
    * Unprojected and projected reference systems (Datums and projections)
    * How to transform a geospatial dataset from one CRS to another
* [Vector data](geospatial_vector_data.ipynb)
    * Formats (ESRI shape files, GeoPackage, GeoJson)
    * How to create geometries such as points, lines, polygons
    * [Spatial relationships](spatial_relationships.ipynb)
        * [Municipalities of the Marche region](topological_operators.ipynb)
    * Temporal relationships
    * [Spatial data integration](marche_flood_event_2022.ipynb)
    * Suitability analysis
    * Network analysis (roads)
    * Open Street Map
* [Raster data](geospatial_raster_data.ipynb)
    * Remote sensing data
        * Satellite or aerial imagery: optical, SAR, Lidar
        * Sub-setting
        * Resampling (image registration and co-registration)
        * Orthorectification
        * Random noise removal (salt and pepper noise)
        * Mosaicking
        * Geo-referencing
        * Spatial interpolation (bilinear, cubic, kriging)
        * [Image fusion (Pan-sharpening)](pan_sharpening.ipynb)
* Geospatial data visualization
    * [Matplotlib](geospatial_data_visualization.ipynb)
        * [Choropleth](unemployment_rate_visualization.ipynb)
    * Leaflet
    * Map Servers
* [Digital elevation models](dem_marche.ipynb)
* Digital surface models
* Map algebra
* Applications
    * Local analysis
    * Focal analysis (smoothing, gradient)
    * Zonal analysis
    * Global analysis
    * Change detection
* Machine learning (unsupervised and supervised)
    * [Map classification](map_classification.ipynb)
    * Segmentation
    * Downscaling, super-resolution
* Spatial data integration
* GIS and Remote Sensing Tools
    * QGIS
    * Orfeo-Toolbox
    * Sentinel Application Platform (SNAP)
    * Spatial databases
        * PostGIS
        * Sqlite

The notebooks are based on the following open source software packages
* [GDAL/OGR](https://gdal.org/) for raster to vector and vector to raster transformations
* [GeoPandas](https://geopandas.org/en/stable/index.html) to handle vector data
* [Rasterio](https://rasterio.readthedocs.io/en/stable/) for raster data
* [Shapely](https://shapely.readthedocs.io/en/stable/) for spatial relations
* [PROJ](https://proj.org/) for coordinates transformations
