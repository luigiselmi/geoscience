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
        * [Mosaicking](geospatial_raster_data.ipynb)
        * Geo-referencing and warping
        * Spatial interpolation (bilinear, cubic, kriging)
        * [Image fusion (Pan-sharpening)](pan_sharpening.ipynb)
* Geospatial data visualization
    * [Matplotlib](geospatial_data_visualization.ipynb)
        * [Choropleth](unemployment_rate_visualization.ipynb)
    * [Leaflet](web_mapping.ipynb)
    * Map Servers
* [Digital elevation models](dem_marche.ipynb)
* Digital surface and terrain models
* Map algebra
* GDAL Virtual Format
* Applications
    * [Local analysis](geospatial_raster_data.ipynb)
    * [Focal analysis](geospatial_raster_data.ipynb) (smoothing, gradient)
    * [Zonal analysis](geospatial_raster_data.ipynb)
    * [Global analysis](geospatial_raster_data.ipynb)
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
* [SciPy](https://scipy.org/), interpolation, linear algebra, numerical integration, optimization
* [PyKRIGE](https://geostat-framework.readthedocs.io/projects/pykrige/en/stable/), geostatistics, kriging
* [pyGIMLi](https://www.pygimli.org/), inversion for geophysics
* [xESMF](https://xesmf.readthedocs.io/en/stable/), regridding
* [FiPy](https://www.ctcms.nist.gov/fipy/), partial differential equations solver
* [scikit-image](https://scikit-image.org/) for digital image processing
* [RasterVision](https://github.com/azavea/raster-vision) for ML and DL
* [TorchGeo](https://github.com/microsoft/torchgeo) for ML and DL
* [PyTorch](https://pytorch.org/) for ML and DL
* [GeoWombat](https://geowombat.readthedocs.io/en/latest/) geospatial and time series at scale
* [rio-mucho](https://github.com/mapbox/rio-mucho) windowed parallel processing wrapper for rasterio
* [The Generic Mapping Tools](https://www.generic-mapping-tools.org/) Earth science data manipulation and visualization  
* [HoloViz](https://holoviz.org/) high-level tools for visualization

Other tools used for testing and satellite imagery analysis and processing
* [QGIS](https://qgis.org/en/site/) Vector and Raster data analysis
* [SNAP](https://step.esa.int/main/download/snap-download/) SAR and Optical data processing
* [Whitebox](https://www.whiteboxgeo.com/) LiDAR data processing.
* [Orfeo Toolbox](https://www.orfeo-toolbox.org/) Remote Sensing image processing
* [Rugged](https://www.orekit.org/site-rugged-3.0/index.html) Sensor to terrain mapping, orthorectification   
* [Orekit](https://www.orekit.org/) space flight dynamics, orbit and attitude determination
* [Panoply](https://www.giss.nasa.gov/tools/panoply/) netCDF data viewer  
* [SAGA](https://saga-gis.sourceforge.io/en/index.html) System for Automated Geoscientific Analysis  
* [ImageJ](https://imagej.net/ij/index.html) Image Processing and Analysis in Java
* [SIFT - Satellite Information Familiarization Tool](https://sift.ssec.wisc.edu/) meteorological satellite imagery visualization tool
* [hale>>studio](https://wetransform.to/halestudio/) spatial data harmonisation tool
* [MicMac](https://github.com/micmacIGN/micmac?tab=readme-ov-file) photogrammetry  
* [Atmospheric Toolbox](https://atmospherictoolbox.org/)  
* [xEOFs - Empirical Orthogonal Functions](https://xeofs.readthedocs.io/en/latest/index.html)  
* [COLMAP](https://colmap.github.io/) stereo image processing, 3D reconstruction, photogrammetry  
* [AliceVision - Photogrammetric Computer Vision Framework](https://alicevision.org/)  
* [scikit-eo](https://yotarazona.github.io/scikit-eo/), a Python package for Remote Sensing tools  

Geoscience tools
* [The Hydrologic Modeling System](https://www.hec.usace.army.mil/software/hec-hms/)  
* [MODFLOW USGS Modular Hydrologic Model](https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model)  
* [NASA GISS G.Projector](https://www.giss.nasa.gov/tools/gprojector/) Map projections
* [H3 - Hexagonal hierarchical geospatial indexing system](https://h3geo.org/) geospatial indexing  
* [OPeNDAP](https://www.opendap.org/), client-server software for geospatial data distribution  
* [NCO](https://nco.sourceforge.net/), command-line toolkit for netCDF, Zarr, HDF5 files  
* [Zarr](https://zarr.dev/), file format for n-dimensional arrays and tensors  
* [Spyder](https://www.spyder-ide.org/), Python integrated development environment, an alternative to Jupyter notebooks 

Geospatial Datasets
* [OpenTopography](https://opentopography.org/), Digital elevation models
* [Nevada Geodetic Laboratory - The MAGNET GPS Network](http://geodesy.unr.edu/magnet.php), Land positioning and motion data
