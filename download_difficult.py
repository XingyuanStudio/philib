import pathlib

import requests


def download_difficult():
    """
    从GitHub自动下载difficulty.tsv文件。

    将文件保存到level_data.tsv
    """
    # GitHub原始文件URL
    # 请求头
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    url = "https://raw.githubusercontent.com/7aGiven/Phigros_Resource/info/difficulty.tsv"

    output_path = pathlib.Path(__file__).parent / "Library" / "level_data.tsv"

    try:
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()

        # 保存文件
        with open(output_path, 'wb') as f:
            f.write(response.content)

        return output_path

    except requests.exceptions.RequestException as e:
        raise Exception(f"下载失败: {e}")
    except IOError as e:
        raise Exception(f"文件保存失败: {e}")


if __name__ == "__main__":
    # 测试示例
    download_difficult()
    print("download is ok.")