# -*- coding: utf-8 -*-
from Types import DataType


class CalcDebtCount:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.debtCount: int = 0

    def calc(self) -> int:
        for student, grades in self.data.items():
            if sum(grade < 61 for _, grade in grades) == 2:
                self.debtCount += 1
        print("Number of students with debt in 2 subjects: ", self.debtCount)
        return self.debtCount
