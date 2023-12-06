# -*- coding: utf-8 -*-
import pytest
import os.path as osp
from Types import DataType
from XMLDataReader import XMLDataReader


class TestTextDataReader:
    @pytest.fixture()
    def file_and_data(self) -> tuple[str, DataType]:
        text = '<?xml version="1.0" encoding="UTF-8" ?>\n' + \
                '<root>\n' + \
                '  <student name="Иванов Иван Иванович">\n' + \
                '    <математика>67</математика>\n' + \
                '    <литература>100</литература>\n' + \
                '    <программирование>91</программирование>\n' + \
                '  </student>\n' + \
                '  <student name="Петров Петр Петрович">\n' + \
                '    <математика>78</математика>\n' + \
                '    <химия>87</химия>\n' + \
                '    <социология>61</социология>\n' + \
                '  </student>\n' + \
                '</root>'
        data = {
            "Иванов Иван Иванович":
            [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович":
            [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data[0], encoding='utf-8')
        return str(p), file_and_data[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
