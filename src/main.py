import os
import shutil
from generate import generate_page
from generate import generate_pages_recursive

import sys

dir_path_static = "../static"
dir_path_public = "../docs"
dir_path_content = "../content"
template_path = "../template.html"
default_basepath = "../"

def copy_files(dir_path_static,dir_path_public):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    os.makedirs(dir_path_public)
    shutil.copytree(dir_path_static, dir_path_public, dirs_exist_ok=True)

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_files(dir_path_static,dir_path_public)

    #generate_page(os.path.join(dir_path_content, "index.md"), template_path, os.path.join(dir_path_public, "index.html"))
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

main()