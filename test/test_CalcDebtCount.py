# -*- coding: utf-8 -*-
import pytest
from Types import DataType
from CalcDebtCount import CalcDebtCount


class TestCalcRating:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
            [
                ("математика", 61),
                ("русский язык", 60),
                ("программирование", 100)
            ],
            "Петров Игорь Владимирович":
            [
                ("математика", 60),
                ("русский язык", 60),
                ("программирование", 78),
                ("литература", 97)
            ],
            "Иванов Иван Иванович":
            [
                ("математика", 60),
                ("литература", 60),
                ("программирование", 60)
            ]
        }
        debtCount: int = 1
        return data, debtCount

    def test_calc(self, input_data: tuple[DataType, int]) -> None:
        debtCount = CalcDebtCount(input_data[0]).calc()
        assert input_data[1] == debtCount
