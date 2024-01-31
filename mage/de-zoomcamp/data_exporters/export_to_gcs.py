import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/gcp-de-zoomcamp.json'
bucket_name = 'de-zoomcamp-412103-data-lake'
object_key = 'green_taxi'

@data_exporter
def export_data(data, *args, **kwargs):

    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table, 
        root_path=f"{bucket_name}/{object_key}", 
        filesystem=gcs, 
        partition_cols=['lpep_pickup_date']
    )
