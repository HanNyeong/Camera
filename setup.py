from setuptools import setup
setup(
    name        ='Camera',
    version     ='0.0.1',
    description ='Camera ',
    url         ='',
    author      ='',
    author_email='',
    packages    =['Camera'],
    data_files=[('Camera/assets', ['Camera/main.kv','Camera/assets/detection.png','Camera/assets/list.png','Camera/assets/record.png'])],
    zip_safe    =False,
#    install_requires=['kivy','kivymd'],
    include_package_data=True,
)
