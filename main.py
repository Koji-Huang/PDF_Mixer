import fitz
import init
import PIL

File: fitz.Document
scale_mode: int
build_mode: str
page_resolution: tuple[int, int]
margins: tuple[int, int]
scale_mode: int
tmp_file_path: str
output_file_path: str


def Init():
    global File, build_mode, page_resolution, margins, scale_mode, tmp_file_path, output_file_path

    print("\n")
    print("PDF Mixer")
    print("Powered by Koji")
    print("\n")

    File = init.init_input_file()

    print("---------------------------------")
    print("Output Parameter:")

    build_mode = init.init_rebuild_mode()
    page_resolution = init.init_page_resolution()
    margins = init.init_margins()
    scale_mode = init.init_scale_mode()
    tmp_file_path = init.init_tmp_folder()
    output_file_path = init.init_output_path()

    print("")
    print("Parameter Input Complete.")
    print("")
    print("--------------------------------")


Init()
