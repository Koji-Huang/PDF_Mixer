# encoding=utf-8
import os.path

import fitz
import init
import process

File: fitz.Document
file_path: str
scale_mode: int
build_mode: str
page_resolution: tuple[float, float]
margins: tuple[float, float]
tmp_file_path: str
output_file_path: str


def default_parameter_setting_load():
    global File, build_mode, page_resolution, margins, scale_mode, tmp_file_path, output_file_path
    build_mode = "Default"
    # A4 规格
    # 单位: cm
    page_resolution = tuple((21., 29.7))

    # # 常规页边距
    # margins = tuple((2.54, 2.8))

    # 无页边距
    margins = tuple((0, 0))

    # 居中 + 自适应缩放模式
    scale_mode = 1
    # 默认为启动目录
    tmp_file_path = "./tmp"
    # 默认为启动目录
    output_file_path = "./output.pdf"


def show_parameter():
    print(f"File: \n\t{File}\n")
    print(f"Scale mode: \n\t{scale_mode}\n")
    print(f"Build mode: \n\t{build_mode}\n")
    print(f"Page resolution: \n\t{page_resolution}\n")
    print(f"Margins: \n\t{margins}\n")
    print(f"Tmp file path: \n\t{tmp_file_path}\n")
    print(f"Output file path: \n\t{output_file_path}\n")


def Init():
    global File, build_mode, page_resolution, margins, scale_mode, tmp_file_path, output_file_path, file_path

    print("\n")
    print("PDF Mixer")
    print("Powered by Koji")
    print("\n")

    File = init.init_input_file()
    file_path = File.name
    print("---------------------------------")
    print("Output Parameter:")

    # build_mode = init.init_rebuild_mode()
    # page_resolution = init.init_page_resolution()
    # margins = init.init_margins()
    # scale_mode = init.init_scale_mode()
    # tmp_file_path = init.init_tmp_folder()
    # output_file_path = init.init_output_path()

    default_parameter_setting_load()

    print("")
    print("Parameter Input Complete.")
    print("")
    print("--------------------------------")

    show_parameter()


def start_process():
    global page_resolution, margins

    zoom: int = 5
    basic_page_resolution = tuple((int(page_resolution[0]), int(page_resolution[1])))
    rotate_page_resolution = tuple((int(page_resolution[1]), int(page_resolution[0])))
    fix_page_resolution = tuple((int(page_resolution[1] / 2), int(page_resolution[0])))
    margins = tuple((int(margins[0]), int(margins[1])))

    process.extract_picture(File, basic_page_resolution, tmp_file_path, zoom= zoom)

    new_doc = process.new_file_make(rotate_page_resolution)
    new_doc: fitz.Document

    index = process.page_sort(build_mode, File.page_count)

    for i in range(index.__len__()):
        new_doc._newPage(width=rotate_page_resolution[0] * zoom, height=rotate_page_resolution[1] * zoom)
        new_doc._newPage(width=rotate_page_resolution[0] * zoom, height=rotate_page_resolution[1] * zoom)

        process.page_make(new_doc[int(i / 4)], f"{tmp_file_path}/{index[i][0]}.png",
                          fix_page_resolution, margins, scale_mode, zoom=zoom)

        process.page_make(new_doc[int(i / 4)], f"{tmp_file_path}/{index[i][1]}.png",
                          (fix_page_resolution[0], fix_page_resolution[1]),
                          margins, scale_mode, zoom=zoom, rel_pos=(rotate_page_resolution[0] / 2, 0))

        process.page_make(new_doc[int(i / 4 + 1)], f"{tmp_file_path}/{index[i][2]}.png",
                          (fix_page_resolution[0], fix_page_resolution[1]),
                          margins, scale_mode, zoom=zoom)

        process.page_make(new_doc[int(i / 4 + 1)], f"{tmp_file_path}/{index[i][3]}.png",
                          (fix_page_resolution[0], fix_page_resolution[1]),
                          margins, scale_mode, zoom=zoom, rel_pos=(rotate_page_resolution[0] / 2, 0))

    new_doc.save(output_file_path)


Init()
start_process()
