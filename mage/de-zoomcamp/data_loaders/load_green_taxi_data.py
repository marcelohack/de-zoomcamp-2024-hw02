import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def parse_datasets(datasets):
    pairs = datasets.split(',')
    return [(pair.split('-')[0], pair.split('-')[1]) for pair in pairs]


@data_loader
def load_data(*args, **kwargs):

    # Update kwargs with default values
    kwargs['datasets'] = kwargs.get('datasets', '2020-10,2020-11,2020-12')
    input_datasets = kwargs['datasets']

    datasets = parse_datasets(input_datasets)

    green_taxy_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),        
        'trip_distance': float,
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'ehail_fee': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'payment_type': pd.Int64Dtype(),
        'trip_type': pd.Int64Dtype(),
        'congestion_surcharge': float
    }

    green_taxy_parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    dfs = []

    for year, month in datasets:
        url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_{year}-{month}.csv.gz"
        df = pd.read_csv(url, sep=',', compression='gzip', dtype=green_taxy_dtypes, parse_dates=green_taxy_parse_dates)
        dfs.append(df)

    result_df = pd.concat(dfs, ignore_index=True)
    return result_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
