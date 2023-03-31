Geospatial Data Science
=======================
This repository contains Jupyter notebooks with Python code about geoscience and remote sensing. Many notebooks come from the book [*Geoprocessing with Python*](https://www.manning.com/books/geoprocessing-with-python) by Chris Garrard, others are my experiments with open geospatial datasets. The topics of the notebooks follows those in the book plus others common in geostatistics.

* [Coordinate reference systems](coordinate_reference_system.ipynb)
    * Unprojected and projected reference systems (Datums and projections)
    * How to transform a geospatial dataset from one CRS to another
* [Vector data](geospatial_vector_data.ipynb)
    * Formats (ESRI shape files, GeoPackage, GeoJson)
    * [Geometries: points, lines, polygons](vector_and_raster_data.ipynb)
    * [Spatial relationships](spatial_relationships.ipynb)
        * [Municipalities of the Marche region](topological_operators.ipynb)
    * Temporal relationships
    * [Spatial data integration](marche_flood_event_2022.ipynb)
    * Suitability analysis
    * Network analysis (roads)
    * [Open Street Map](openstreetmap.ipynb)
* [Raster data](geospatial_raster_data.ipynb)
    * Remote sensing data
        * Satellite and aerial imagery: optical, thermal, SAR, Lidar
        * [Sub-setting](raster_subsetting.ipynb)
        * Resampling (image registration and co-registration)
        * Orthorectification
        * Random noise removal (salt and pepper noise)
        * Mosaicking
        * Geo-referencing and warping
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
* GDAL Virtual Format
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
* [Cartopy](https://scitools.org.uk/cartopy/docs/latest/index.html) for geospatial data visualization
* [Folium](https://github.com/python-visualization/folium) for map visualization
* [Xarray](https://docs.xarray.dev/en/stable/) for multidimensional array processing
* [RasterVision](https://github.com/azavea/raster-vision) for ML and DL
* [TorchGeo](https://github.com/microsoft/torchgeo) for ML and DL
* [PyTorch](https://pytorch.org/) for ML and DL

Other tools used for testing and satellite imagery analysis
* [QGIS](https://qgis.org/en/site/) Vector and Raster data analysis
* [SNAP](https://step.esa.int/main/download/snap-download/) SAR and Optical data processing
* [Whitebox](https://www.whiteboxgeo.com/) LiDAR data processing.
* [Orfeo Toolbox](https://www.orfeo-toolbox.org/) Remote Sensing image processing
* [Rugged](https://www.orekit.org/site-rugged-3.0/index.html) Sensor to terrain mapping
* [Orekit](https://www.orekit.org/) space flight dynamics, orbit and attitude determination 
