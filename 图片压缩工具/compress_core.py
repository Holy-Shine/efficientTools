from PIL import Image
import os




def compress_by_ratio(img_path, output_path, ratio=2):
    """根据倍率压缩图片

    Args:
        img_path (str): 图片路径
        output_path (str): 保存路径
        ratio (int, optional): 压缩倍率. Defaults to 2.
    """
    image = Image.open(img_path)
    new_height = int((float(image.size[1])/ratio))
    new_width  = int((float(image.size[0])/ratio))

    # 调整图像大小
    compressed_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # 保存压缩后的图像
    file_name = os.path.basename(img_path)
    compressed_image.save(f'{output_path}/{file_name}')

    