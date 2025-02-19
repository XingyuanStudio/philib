from setuptools import setup, find_packages

setup(
    name="philib",
    packages=find_packages(),
    include_package_data=True,  # 这很重要
    # ... 其他配置
) 