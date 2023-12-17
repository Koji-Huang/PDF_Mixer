# encoding=utf-8

import fitz
import os
import PIL


def extract_picture(doc: fitz.Document, scale: tuple[int, int], save_path: str, zoom: int = 1):
    total = doc.page_count

    for pg in range(total):
        page = doc[pg]
        zoom = int(zoom)  # 值越大，分辨率越高，文件越清晰
        rotate = int(0)

        rect = page.rect  # 页面大小
        mp = rect.tl  # 矩形区域
        clip = fitz.Rect(mp, rect.br)

        trans = fitz.Matrix(int((zoom * scale[0]) / 200), int((zoom * scale[1]) / 200)).prerotate(rotate)

        pm = page.get_pixmap(matrix=trans, alpha=False, clip=clip)

        if not os.path.exists(save_path):
            os.mkdir(save_path)
        save = os.path.join(save_path, '%s.png' % (pg + 1))
        pm.save(save)
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
        return tuple((put_size[0], int(picture_size[1] * picture_size[0] / put_size[0])))
    if put_size[0] / put_size[1] < picture_size[0] / picture_size[1]:
        # 短边太长了
        return tuple((int(put_size[0] * put_size[1] / put_size[1]), picture_size[1]))
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

    if image_file_path[-6:-5] == -1:
        return

    picture_size: tuple[float, float]
    picture_pos: tuple[float, float]

    match scale_mode:
        case 0:
            # 居中 + 自适应缩放
            picture_size = adaptive_scaling_size_make(resolution, margin)
            picture_pos = tuple(
                (int((resolution[0] - picture_size[0]) / 2), int((resolution[1] - picture_size[1]) / 2)))
        case _:
            # 强制缩放
            picture_size = adaptive_scaling_size_make(resolution, margin)
            picture_pos = margin

    picture_pos = tuple((picture_pos[0] + rel_pos[0], picture_pos[1] + rel_pos[1]))
    picture_size = tuple((picture_size[0] + rel_pos[0], picture_size[1] + rel_pos[1]))

    picture_pos = tuple(int(i) for i in picture_pos)
    picture_size = tuple(int(i) for i in picture_size)

    rect = fitz.Rect(picture_pos[0] * zoom, picture_pos[1] * zoom, picture_size[0] * zoom, picture_size[1] * zoom)
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
        i = page_range % 4 + 1
        result[i] = [i * 4 for _ in range(4)]
        match sort_mode:
            case _, 3:
                result[i][0] += 4
                result[i][1] = result[i][1] + 1 if i * 4 - 4 + 2 < page_range else -1
                result[i][2] = result[i][2] + 2 if i * 4 - 4 + 3 < page_range else -1
                result[i][3] = -1

    return tuple(result)


def new_file_make(resolution: tuple[int, int]):
    return fitz.Document()

