import click
import os
import logging


from compress_core import compress_by_ratio



logger = logging.getLogger(__name__)

# 控制台处理器
console_handler = logging.StreamHandler()

# 日志格式化器
formatter = logging.Formatter(
    '[%(levelname)s] - %(message)s'
)
# 将格式化器添加到处理器
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

def count_files(directory: str) -> int:
    """获取文件个数

    Args:
        directory (str): 文件路径

    Returns:
        int: 文件个数
    """
    file_count = 0
    # 使用 os.listdir() 获取目录下的所有内容（文件和子目录）
    for item in os.listdir(directory):
        # 使用 os.path.isfile() 判断是否为文件
        if os.path.isfile(os.path.join(directory, item)):
            file_count += 1
    return file_count


@click.command()
@click.argument("path")
@click.option("--ratio", default=2.0, help="图片压缩倍率")
@click.option("--out", default=None, help="输出图片目录")
def run(path, ratio, out):
    logger.info(f"图片路径:{path}")
    logger.info(f"压缩倍率:{ratio}")
    output_path = os.path.join(path, "dst") if not out else out
    logger.info(f"输出路径:{output_path}")
    if not os.path.exists(output_path): 
        os.mkdir(output_path)
    logger.info("开始压缩")

    count = count_files(path)

    for i,file in enumerate([file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]):
        compress_by_ratio(
            img_path=os.path.join(path, file),
            output_path=output_path,
            ratio=float(ratio)
        )
        print(f"[INFO] - 压缩进度: {i+1}/{count}", end='\r')
    print("")

    logger.info("压缩完成!")



if __name__ == '__main__':
    run()