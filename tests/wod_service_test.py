import pytest
from unittest.mock import MagicMock
from app.services.wod_service import get_all, get_by_id
from app.models.wod import Wod

@pytest.fixture
def mock_db():
    # Mocking the database session
    mock_db = MagicMock()
    return mock_db

def test_get_all(mock_db):
    # Creating mock objects that simulate the query results
    mock_wods = [
        Wod(id=1, type="AMRAP", time_cap=20, description="Test WOD 1"),
        Wod(id=2, type="FOR_TIME", time_cap=15, description="Test WOD 2"),
    ]
    
    # Mocking the db.query().all() method to return our mock_wods
    mock_db.query.return_value.all.return_value = mock_wods
    
    # Calling the service function
    result = get_all(mock_db)
    
    # Assertions
    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].description == "Test WOD 1"
    assert result[1].id == 2
    assert result[1].description == "Test WOD 2"

    mock_db.query.return_value.all.assert_called_once()

def test_get_by_id(mock_db):
    # Creating a mock object for a single WOD
    mock_wod = Wod(id=1, type="TABATA", time_cap=25, description="Test WOD 1")
    
    # Mocking the db.query().filter().first() method to return our mock_wod
    mock_db.query.return_value.filter.return_value.first.return_value = mock_wod
    
    # Calling the service function
    result = get_by_id(mock_db, 1)
    
    # Assertions
    assert result is not None
    assert result.id == 1
    assert result.type == "TABATA"
    assert result.description == "Test WOD 1"
    mock_db.query.return_value.filter.return_value.first.assert_called_once_with()
    
def test_get_by_id_not_found(mock_db):
    # Mocking the db.query().filter().first() method to return None (no result found)
    mock_db.query.return_value.filter.return_value.first.return_value = None
    
    # Calling the service function with an ID that doesn't exist
    result = get_by_id(mock_db, 999)
    
    # Assertions
    assert result is None
    mock_db.query.return_value.filter.return_value.first.assert_called_once_with()
