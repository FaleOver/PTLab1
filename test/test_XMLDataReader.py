# -*- coding: utf-8 -*-
import pytest
import os
from Types import DataType
from XMLDataReader import XMLDataReader


class TestTextDataReader:
    @pytest.fixture()
    def filepath_and_data(self) -> tuple[str, DataType]:
        filepath = os.path.abspath(__file__).join("xmlData.xml")
        data = {
            "Иванов Иван Иванович": [
                ("математика", 67), ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78), ("химия", 87),
                ("социология", 61)
            ]
        }
        return filepath, data

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
