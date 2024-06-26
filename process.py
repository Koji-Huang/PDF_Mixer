# encoding=utf-8

import fitz
import os


def extract_picture(doc: fitz.Document, scale: tuple[float, float], save_path: str, zoom: int = 1):
    total = doc.page_count

    print("")
    print("--------------------------------")
    print("")
    for pg in range(total):
        percent = int(pg * 100 / total)

        print("\r", end='')
        print("Extracting Picture: {}%: ".format(percent), "▋" * (percent // 2), 'page: %d - %d' % (pg, total), end="")

        page = doc[pg]

        rect = page.rect  # 页面大小
        mp = rect.tl  # 矩形区域
        clip = fitz.Rect(mp, rect.br)

        pm = page.get_pixmap(clip=clip, dpi=zoom)

        if not os.path.exists(save_path):
            os.mkdir(save_path)
        save = os.path.join(save_path, '%s.png' % (pg + 1))
        pm.save(save)

    print("")
    print("Extract Picture Finished")
    print("")
    print("--------------------------------")

    return


def adaptive_scaling_size_make(picture_size: tuple[float, float], cut_size: tuple[float, float],
                               put_size: tuple[float, float] = None):
    """
    图片页边距自适应大小调整
    :param picture_size: 初始图片大小
    :param cut_size: 页边距
    :param put_size: 可放置的区域大小
    :return: 图片修改过后的大小
    """
    if not put_size:
        put_size = tuple((picture_size[0] - cut_size[0] * 2, picture_size[1] - cut_size[1] * 2))
    if put_size[0] / put_size[1] > picture_size[0] / picture_size[1]:
        # 长边太长了
        return tuple((put_size[0], picture_size[1] * picture_size[0] / put_size[0]))
    if put_size[0] / put_size[1] < picture_size[0] / picture_size[1]:
        # 短边太长了
        return tuple((put_size[0] * put_size[1] / put_size[1], picture_size[1]))
    if put_size[0] / put_size[1] == picture_size[0] / picture_size[1]:
        # 比例恰好合适
        return tuple((picture_size[0] - cut_size[0] * 2, picture_size[1] - cut_size[1] * 2))


def page_make(page: fitz.Page, image_file_path: str,
              resolution: tuple[float, float], margin: tuple[float, float],
              scale_mode: int, zoom: float = 100, rel_pos: tuple[float, float] = (0, 0)) -> None:
    """
    图像放置 (单张)
    :param rel_pos:
    :param zoom:
    :param page: Page 对象
    :param image_file_path: 图片路径
    :param resolution: 页分辨率
    :param margin: 页边距
    :param scale_mode: 缩放模式
    :return: None
    """

    if image_file_path[-6:-4] == '-1':
        return

    picture_size: tuple[float, float]
    picture_pos: tuple[float, float]

    match scale_mode:
        case 0:
            # 强制缩放
            picture_size = resolution
            picture_pos = margin
        case _:
            # 居中 + 自适应缩放
            picture_size = adaptive_scaling_size_make(resolution, margin)
            picture_pos = tuple(((resolution[0] - picture_size[0]) / 2, (resolution[1] - picture_size[1]) / 2))

    # picture_pos = tuple((picture_pos[0] + rel_pos[0], picture_pos[1] + rel_pos[1]))
    # picture_size = tuple((picture_size[0] + rel_pos[0], picture_size[1] + rel_pos[1]))

    # 0, 0
    # 1.48......

    picture_pos = tuple(int(i * zoom) for i in picture_pos)
    picture_size = tuple(int(i * zoom) for i in picture_size)

    rect = fitz.Rect(picture_pos, picture_size)

    rect[0] += rel_pos[0] * zoom
    rect[2] += rel_pos[0] * zoom

    page.insert_image(rect, filename=image_file_path)


def page_sort(sort_mode: str, page_range: int) -> tuple[tuple[int, int, int, int], ...]:
    """
    注: 仅限短边翻转
    3: 折打
    :param sort_mode:
    :param page_range:
    :return:
    """
    result = list()
    for i in range(int(page_range / 4)):
        result.append([i * 4 for _ in range(4)])
        match sort_mode:
            case _:
                result[i][0] += 4
                result[i][1] += 1
                result[i][2] += 2
                result[i][3] += 3
                result[i] = tuple(result[i])

    if page_range % 4:
        i = int( page_range / 4 )
        result.append([i * 4 for _ in range(4)])
        match sort_mode:
            case _:
                result[i][0] = result[i][0] + 4 if i * 4 + 3 < page_range else -1
                result[i][1] = result[i][1] + 1 if i * 4 + 0 < page_range else -1
                result[i][2] = result[i][2] + 2 if i * 4 + 1 < page_range else -1
                result[i][3] = result[i][3] + 3 if i * 4 + 2 < page_range else -1

    return tuple(result)


def new_file_make(resolution: tuple[float, float]):
    return fitz.Document()

