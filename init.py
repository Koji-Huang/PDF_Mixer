# encoding=utf-8

import os.path
import fitz


def init_input_file() -> fitz.Document:
    print("Please input file's path: ")

    while True:
        FILE_PATH = input(">>>")
        # FILE_PATH = r"C:\Users\Administrator\Downloads\National Olympiad in Infomatics.pdf"
        try:

            if not os.path.exists(FILE_PATH):
                print("FileNotFoundError:\nNo such file: \"", FILE_PATH, "\"")
                print("Please input file's path: ")
                continue

            FILE = fitz.open(FILE_PATH)
            FILE.metadata: dict

            print("\n Now reading parameter...")
            for i in FILE.metadata.items():
                print("| ", i[0], "-> ", i[1])

            if input("Confirm ? Y(1) or N(0): ") in ("Y", 'y', "yes", "Yes", "YES", '1', "True"):
                print("\nFile Load Success\n")
                return FILE
            else:
                print("Please input file's path: ")
                continue

        except Exception as err:
            print(err)
            print("Please retry again")


def init_rebuild_mode() -> str:
    # 分页规律
    mode_collection = ("One_Direction", "Different_Direction", "Default", "0", "1")
    print("")
    print("Rebuild Mod")
    print("For the details\nyou can go to the folder of this software\nthen you can find the docs\nDefault: Default")

    while True:
        RebuildMode = input(">>> ")
        if RebuildMode in mode_collection:
            return RebuildMode
        if RebuildMode == '':
            return 'Default'
        else:
            print("Inputted mode is not in set\nPlease retry again")


def init_page_resolution() -> tuple[float, float]:
    # 每页 PDF 的分辨率
    print("\n")
    print("Big Page page_resolution")
    # 纵向 A4
    print("1 for A4 (Vertical)")
    # 横向 A4
    print("2 for A4 (horizontal)")
    # 纵向 A5
    print("3 for A5 (Vertical)")
    # 横向 A5
    print("4 for A5 (horizontal)")
    # 自定义分辨率
    print("Other for Custom Setting")

    print("Default x = 21, y = 29.7 (A4 Vertical)")

    Resolution_X: float
    Resolution_Y: float

    match input(">>> "):
        case '1':
            Resolution_X = 21.0
            Resolution_Y = 29.7
        case '2':
            Resolution_X = 29.7
            Resolution_Y = 21.0
        case '3':
            Resolution_X = 14.8
            Resolution_Y = 21.0
        case '4':
            Resolution_X = 21.0
            Resolution_Y = 14.8
        case '':
            Resolution_X = 21.0
            Resolution_Y = 29.7
        case _:
            while True:
                try:
                    Resolution_X = int(input("X:"))
                    Resolution_Y = int(input("Y:"))
                except Exception as err:
                    print("\n")
                    print("Error")
                    print(err)
                    print("Please retry again\n")
                    continue

                if Resolution_X <= 0 or Resolution_Y <= 0:
                    print("Resolution can't lower than 1 !")
                    continue
                else:
                    break

    return tuple((Resolution_X, Resolution_Y))


def init_margins() -> tuple[float, float]:
    # 页边距
    print("\n")
    print("Page Margins")
    print("0 for No margins")
    print("1 for Standard margins")
    print("2 for low margins")
    print("3 for large margins")
    print("Other for custom margins")
    print("Default x = 2.54, y = 2.8")
    Empty_X: float
    Empty_Y: float
    match input(">>> "):
        case '0':
            Empty_X = 0
            Empty_Y = 0
        case '1':
            Empty_X = 2.54
            Empty_Y = 2.8
        case '2':
            Empty_X = 2.54 / 2.4
            Empty_Y = 2.8 / 2.4
        case '3':
            Empty_X = 2.54 * 2
            Empty_Y = 2.8 * 2
        case '':
            Empty_X = 2.54
            Empty_Y = 2.8
        case _:
            while True:
                try:
                    Empty_X = float(input("X:"))
                    Empty_Y = float(input("Y:"))
                except Exception as err:
                    print(err)
                    print("Please retry again")
                    continue

                if Empty_X <= 0 or Empty_Y <= 0:
                    print("Margins can't lower than 1 !")
                    continue
                else:
                    break

    return tuple((Empty_X, Empty_Y))


def init_scale_mode() -> int:
    # 缩放模式
    print("\n")
    print("Scale Mode")
    # 强制缩放
    print("0 for Force Zoom")
    # 居中 + 自适应
    print("1 for Keep to theCentered and Adaptive scaling")
    print("Default 0")
    while True:
        try:
            PlaceMode = input(">>> ")
            if PlaceMode not in ['0', '1', '']:
                print("Unexpect Parameter, please retry")
                continue
            elif PlaceMode == '':
                return 0
            else:
                return int(PlaceMode)
        except Exception as err:
            print(err)
            print("Please retry again")


def init_tmp_folder() -> str:
    # 临时文件存放处
    print("\n")
    print("TMP file folder:")
    print("No Input will put on ./tmp")
    TmpPath = input(">>> ")
    if TmpPath:
        return TmpPath
    else:
        return "./tmp"


def init_output_path() -> str:
    # 输出文件路径
    print("\n")
    print("Output file folder")
    print("No Input will put on output.pdf")
    OutputPath = input(">>> ")
    if OutputPath:
        return OutputPath
    else:
        return "./output.pdf"
