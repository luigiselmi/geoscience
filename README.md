Geospatial Data Science
=======================
This repository contains Jupyter notebooks with Python code about geoscience and remote sensing. Many notebooks come from the book [*Geoprocessing with Python*](https://www.manning.com/books/geoprocessing-with-python) by Chris Garrard, others are my experiments with open geospatial datasets. The topics of the notebooks follows those in the book plus others common in geostatistics.

* Coordinate reference systems (CRS)
    * Unprojected and projected reference systems (Datums and projections)
    * How to transform a geospatial dataset from one CRS to another
* [Vector data](geospatial_vector_data.ipynb)
    * Formats (ESRI shape files, GeoPackage, GeoJson)
    * How to create geometries such as points, lines, polygons
    * Spatial relationships
    * Temporal relationships
    * Spatial data integration
    * Suitability analysis
    * Network analysis (roads)
    * Open Street Map
* [Raster data](geospatial_raster_data.ipynb)
    * Remote sensing data
        * Satellite or aerial imagery: optical, SAR, Lidar
        * Sub-setting
        * Resampling
        * Mosaicking
        * Geo-referencing
        * Spatial interpolation (bilinear, cubic, kriging)
        * Image fusion (Pan-sharpening)
* Geospatial data visualization
    * Matplotlib
    * Leaflet
    * Map Servers
* Digital elevation models
* Map algebra
* Local analysis
* Focal analysis (smoothing, gradient)
* Zonal analysis
* Global analysis
* Machine learning (unsupervised and supervised)
    * Map classification
    * Segmentation
    * Downscaling, super-resolution
* Change detection
* GIS Tools
    * QGIS
    * Spatial databases
        * PostGIS
        * Sqlite

The notebooks are based on the [GDAL/OGR](https://gdal.org/) library and other Python packages such as [GeoPandas](https://geopandas.org/en/stable/index.html) and [Shapely](https://shapely.readthedocs.io/en/stable/).  
