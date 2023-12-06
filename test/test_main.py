# -*- coding: utf-8 -*-
import pytest
from main import get_path_from_arguments


@pytest.fixture()
def correct_txt_arguments_string() -> tuple[list[str], str]:
    return ["-p", "/home/user/file.txt"], "/home/user/file.txt"


@pytest.fixture()
def correct_xml_arguments_string() -> tuple[list[str], str]:
    return ["-p", "/home/user/file.xml"], "/home/user/file.xml"


@pytest.fixture()
def noncorrect_arguments_string() -> list[str]:
    return ["/home/user/file.txt"], ["/home/user/file.xml"]


def test_get_path_from_correct_txt_arguments(
        correct_txt_arguments_string: tuple[list[str], str]) -> None:
    path = get_path_from_arguments(correct_txt_arguments_string[0])
    assert path == correct_txt_arguments_string[1]


def test_get_path_from_correct_xml_arguments(
        correct_xml_arguments_string: tuple[list[str], str]) -> None:
    path = get_path_from_arguments(correct_xml_arguments_string[0])
    assert path == correct_xml_arguments_string[1]


def test_get_path_from_noncorrect_arguments(
        noncorrect_arguments_string: list[str]) -> None:
    for i in range(2):
        with pytest.raises(SystemExit) as e:
            get_path_from_arguments(noncorrect_arguments_string[i])
        assert e.type == SystemExit
