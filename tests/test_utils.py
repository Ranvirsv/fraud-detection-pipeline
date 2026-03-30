def test_sample_data(sample_data):
    assert sample_data.shape == (5, 3)
    assert sample_data['col1'].dtype == 'int64'
    assert sample_data.isnull().sum().sum() == 0