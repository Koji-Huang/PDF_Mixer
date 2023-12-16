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
    # ��ҳ����
    mode_collection = ("One_Direction", "Different_Direction", "Default", "0", "1")
    print("")
    print("Rebuild Mod")
    print("For the details\nyou can go to the folder of this software\nthen you can find the docs")

    while True:
        RebuildMode = input(">>> ")
        if RebuildMode in mode_collection:
            return RebuildMode
        else:
            print("Inputted mode is not in set\nPlease retry again")


def init_page_resolution() -> tuple[int, int]:
    # ÿҳ PDF �ķֱ���
    print("\n")
    print("Big Page page_resolution")
    # ���� A4
    print("1 for A4 (Vertical)")
    # ���� A4
    print("2 for A4 (horizontal)")
    # ���� A5
    print("3 for A5 (Vertical)")
    # ���� A5
    print("4 for A5 (horizontal)")
    # �Զ���ֱ���
    print("Other for Custom Setting")

    match int(input(">>> ")):
        case 1:
            ...
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
        case _:
            while True:
                Resolution_X: int
                Resolution_Y: int
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

                return tuple((Resolution_X, Resolution_Y))


def init_margins() -> tuple[int, int]:
    # ҳ�߾�
    print("\n")
    print("Page Margins")
    print("0 for No margins")
    print("1 for Standard margins")
    print("2 for low margins")
    print("3 for normal margins")
    print("4 for large margins")
    print("Other for custom margins")
    match int(input(">>> ")):
        case 0:
            ...
        case 1:
            ...
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
        case _:
            while True:
                Empty_X: int
                Empty_Y: int
                try:
                    Empty_X = int(input("X:"))
                    Empty_Y = int(input("Y:"))
                except Exception as err:
                    print(err)
                    print("Please retry again")
                    continue

                if Empty_X <= 0 or Empty_Y <= 0:
                    print("Margins can't lower than 1 !")
                    continue

                return tuple((Empty_X, Empty_Y))


def init_scale_mode() -> int:
    # ����ģʽ
    print("\n")
    print("Scale Mode")
    # ǿ������
    print("0 for Force Zoom")
    # ���� + ����Ӧ
    print("1 for Keep to theCentered and Adaptive scaling")
    # ���� + ����Ӧ
    print("2 for Keep to the Right and Adaptive scaling")
    # ���� + ����Ӧ
    print("3 for Keep to the Left and Adaptive scaling")
    # ���� + ����Ӧ
    print("4 for Keep to the Top and Adaptive scaling")
    # ���� + ����Ӧ
    print("5 for Keep to the Button and Adaptive scaling")
    while True:
        try:
            PlaceMode = int(input(">>> "))
            if PlaceMode not in [0, 1, 2, 3, 4, 5]:
                print("Unexpect Parameter, please retry")
                continue
            return PlaceMode
        except Exception as err:
            print(err)
            print("Please retry again")


def init_tmp_folder() -> str:
    # ��ʱ�ļ���Ŵ�
    print("\n")
    print("TMP file folder:")
    print("No Input will put on ./")
    TmpPath = input(">>> ")
    if TmpPath:
        return TmpPath
    else:
        return "./"


def init_output_path() -> str:
    # ����ļ�·��
    print("\n")
    print("Output file folder")
    print("No Input will put on ./")
    OutputPath = input(">>> ")
    if OutputPath:
        return OutputPath
    else:
        return "./"
