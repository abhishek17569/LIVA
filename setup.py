import setuptools
from setuptools import setup
import os

DATA_FOLDERS = ['img',
                'sounds',
                'config',
                'logs',
                'skills',
                'speech',
                'utilities',
                'wake_word',
                'custom_skills',
                'usr'
                ]
data = []


def dfs(path, file_folder):
    """
    this will go inside every folder search for each folder and subfolder and put that in data
    :param path:
    :param file_folder:
    :return:
    """

    if file_folder == '__pycache__':
        """pycache directory causes build failed if it we complile the file which include this dirctory. SO it need 
        to be skipped """
        return
    if os.path.isfile(os.path.join(path, file_folder)):
        data.append(('lib/liva/' + path, [os.path.join(path, file_folder)]))
        return
    else:
        files = os.listdir(os.path.join(path, file_folder))
        for file in files:
            dfs(os.path.join(path, file_folder), file)


def get_files_recursively() -> list:
    """
    This will take app root directory parent folder list and can go to depth to find all the files.
    :return: All non python folder or say data folder that you wanted to include in deb package
    """
    for folder in DATA_FOLDERS:
        files = os.listdir(folder)
        for file in files:
            dfs(folder, file)
    # print("all data files are {data}".format(data=data))
    return data


def get_root_data_files() -> list:
    data = [
        ('bin/', ['liva']),
        ('lib/liva/', ['config.ini', 'requirements.txt', 'sentences.ini', 'voice2intent.py', 'README.md', '__main__.py']),
        ('/lib/systemd/system/', ['liva.service'])
    ]
    return data


def get_data_files():
    return list(get_root_data_files()) + list(get_files_recursively())


setup(
    name='L.I.V.A',
    version='1.0',
    packages=setuptools.find_packages(),
    url='',
    license='MIT',
    author='Abhishek',
    author_email='',
    description='Linux Virtual Assistant',
    data_files=get_data_files(),
    include_package_data=True
)
