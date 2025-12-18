from src.processing import filter_by_state

def test_filter_by_state_executed(sample_data):
    # Тест фильтрации по умолчанию (EXECUTED)
    result = filter_by_state(sample_data)
    assert len(result) == 2
    assert all(item['state'] == 'EXECUTED' for item in result)