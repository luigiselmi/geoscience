def make_raster(driver, in_ds, fn, data, data_type, nodata=None):
    """Creates a one-band GeoTIFF from a NumPy array.
    driver: the GeoTIFF driver
    in_ds: datasource to copy projection and geotransform from
    fn: path to the file to create
    data: NumPy array containing data to write
    data_type: output data type
    nodata: optional NoData value
    """
    out_ds = driver.Create(fn, in_ds.RasterXSize, in_ds.RasterYSize, 1, data_type)
    out_ds.SetProjection(in_ds.GetProjection())
    out_ds.SetGeoTransform(in_ds.GetGeoTransform())
    out_band = out_ds.GetRasterBand(1)
    if nodata is not None:
        out_band.SetNoDataValue(nodata)
    out_band.WriteArray(data)
    out_band.FlushCache()
    out_band.ComputeStatistics(False)
    return out_ds
