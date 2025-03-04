from unittest.mock import patch, mock_open, MagicMock
from src.file_reader import read_file_scv, read_file_xlsx

@patch("builtins.open")
@patch("csv.DictReader")
def test_read_file_scv(mock_dictreader, mock_open_file):
    mock_open_file.new = mock_open()
    mock_dictreader.return_value = [{"id": 123}, {"id": 321}]
    result = read_file_scv("")
    assert result == [{"id": 123}, {"id": 321}]


@patch("pandas.read_excel")
def test_read_file_xlsx(mock_read_excel):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 123}, {"id": 321}]
    mock_read_excel.return_value = mock_df

    result = read_file_xlsx("")
    assert result == [{"id": 123}, {"id": 321}]
