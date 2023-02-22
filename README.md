Geospatial Data Science
=======================
This repository contains Jupyter notebooks with Python code about geoscience and remote sensing. Many notebooks come from the book [*Geoprocessing with Python*](https://www.manning.com/books/geoprocessing-with-python) by Chris Garrard, others are my experiments with open geospatial datasets. The topics of the notebooks follows those in the book plus others common in geostatistics.

* Coordinate reference systems (CRS)
    * Unprojected and projected reference systems (Datums and projections)
    * How to transform a geospatial dataset from one CRS to another
* Geospatial data visualization
    * Matplotlib
    * Leaflet
* Vector data
    * Formats (ESRI shape files, GeoPackage, GeoJson)
    * How to create geometries such as points, lines, polygons
    * Spatial relationships
    * Temporal relationships
    * Spatial data integration
    * Suitability analysis
* Raster data
    * Remote sensing data
        * Satellite or aerial imagery: optical, SAR, Lidar
        * Sub-setting
        * Resampling
        * Mosaicking
        * Geo-referencing
        * Pan-sharpening (downscaling, super-resolution)
* Digital elevation models
* Spatial interpolation (bilinear, cubic, kriging)
* Map algebra
* Local analysis
* Focal analysis (smoothing, gradient)
* Zonal analysis
* Global analysis
* Map classification (unsupervised and supervised)
* Change detection

The notebooks are based on the [GDAL/OGR](https://gdal.org/) library and other Python packages such as [GeoPandas](https://geopandas.org/en/stable/index.html) and [Shapely](https://shapely.readthedocs.io/en/stable/).  
