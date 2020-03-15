# -*- coding: utf-8 -*-
import xlrd
import json
import os

import shutil


def read_template(template="excel2py.json"):
    with open(template, "r") as fd:
        data = json.load(fd)
    return data



def parse_xlsx_opaque(filename, znumber):
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_index(0)
    no_rows = sh.nrows
    parsed_data = {}
    parsed_data["opaque_rows" + znumber] = no_rows

    for column_index in range(0, 16):
        key = f"opaque_column{column_index + 1}" + znumber
        try:
            values = sh.col_values(column_index)
            values = ",".join(str(v) for v in values)
            values = values + str(",")
        except IndexError:
            values = "," * no_rows
        parsed_data[key] = values
    return parsed_data


def parse_xlsx_transp(filename,znumber):
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_index(1)
    no_rows = sh.nrows
    parsed_data = {}
    parsed_data["transparent_rows" + znumber] = no_rows

    for column_index in range(0, 15):
        key = f"transparent_column{column_index + 1}" + znumber
        try:
            values = sh.col_values(column_index)
            values = ",".join(str(v) for v in values)
            values = values + str(",")
        except IndexError:
            values = "," * no_rows
        parsed_data[key] = values
    return parsed_data


def parse_xlsx_etc(filename, znumber):
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_index(2)
    try:
        parsed_data = {}
        parsed_data["zn_parameter6" + znumber] = sh.cell(0, 0).value
        parsed_data["blg_parameter11"] = sh.cell(1, 0).value
        parsed_data["blg_parameter15"] = "1111"
    except IndexError:
        parsed_data["blg_parameter11"] =""


    #print(sh.cell(0, 0).value)

    return parsed_data


def generate_json(excel_file, output_file, znumber):
    data = read_template()
    parsed_data_opaque = parse_xlsx_opaque(excel_file, znumber)
    parsed_data_transp = parse_xlsx_transp(excel_file, znumber)
    parsed_data_etc = parse_xlsx_etc(excel_file, znumber)
    data.update(**parsed_data_opaque)
    data.update(**parsed_data_transp)
    data.update(**parsed_data_etc)
    with open(output_file, "w") as fd:
        json.dump(data, fd, indent=2)
    print(parsed_data_etc)
    #print(parsed_data_opaque)


generate_json("zone1.xlsm", "out.json", "z1")
generate_json("zone2.xlsm", "out.json", "z2")
