if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    
    # Rename columns from pascal case to snake case
    data.rename(columns={
        'VendorID': 'vendor_id',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id',
    }, inplace=True)

    data.columns = (data.columns
        .str.replace(' ', '_')
        .str.lower()
    )

    # Create a new column for the pickup date with the date only
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    print(f"Number of records before filtering: {data.shape[0]}")
    print("Number of duplicates:", data.duplicated().sum())
    print("Number of NaN values in 'passenger_count':", data['passenger_count'].isna().sum())
    print("Number of NaN values in 'trip_distance':", data['trip_distance'].isna().sum())

    print(f"Rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")
    print(f"Rows with trip distance equal to zero: {data['trip_distance'].isin([0]).sum()}")

    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    # data = data[(data['passenger_count'] == 0) | (data['trip_distance'] == 0)]
    # data = data[~(data['passenger_count'] == 0) | (data['trip_distance'] == 0)]

    # data = data[data['passenger_count'] > 0] 

    # print(f"Number of records after filtering passenger_count: {data.shape[0]}")
    # print(f"Rows with trip distance equal to zero: {data['trip_distance'].isin([0]).sum()}")
    # print("Number of NaN values in 'trip_distance':", data['trip_distance'].isna().sum())

    # data = data[data['trip_distance'] > 0]

    print(f"Number of records after filtering: {data.shape[0]}")

    return data


@test
def test_output(output, *args) -> None:
    assert (output['vendor_id'].isin([1, 2]).all() | output['vendor_id'].isna().any()), "Invalid values found in the Vendor ID column."
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with trip distance equal to zero'

    # assert ~output['passenger_count'].isin([0]).sum() > 0, 'There are rides with zero passengers'
    # assert ~output['trip_distance'].isin([0]).sum() > 0, 'There are rides with trip distance equal to zero'
