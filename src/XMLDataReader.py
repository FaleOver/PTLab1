# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from Types import DataType
from DataReader import DataReader


class XMLDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()

        for child in root:
            self.key = child.get("name")
            self.students[self.key] = []
            for item in child:
                self.students[self.key].append(
                    (item.tag, int(item.text)))
        return self.students
