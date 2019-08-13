import requests
import time
import os
import json
import re
#pip3 install pillow
from PIL import Image,ImageDraw,ImageFont,ImageColor
import glob
from math import ceil, floor
import random
from biplist import *
from datetime import datetime
import shutil
import chardet
import codecs

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = BASE_DIR + '/png/'

icon_count = 20 #设置生成纯背景图片个数
txt = '初   中 \n古   诗 ' #设置生成图片上文字内容
app_main_color="#FF0000" #背景图片颜色-程序中随机替换颜色
icon_color_name ='' #icon名字 命名方式 (icon_颜色.png)
font_size = 180 #图片文字字体大小
x = 250 #图片文字起始位置X
y =250  #图片文字起始位置Y
fill_color ='white'  #图片文字颜色
spacing = 200  #图片文字间距
contents_json = "Contents.json" #生成iOS icon使用的json文件
font_path = "/System/Library/Fonts/Hiragino Sans GB.ttc" #系统字体路径（以mac为例）

a = {
    '20':20,
    '29':29,
    '40-1':40,
    '40-2':40,
    '40':40,
    '58-1': 58,
    '58': 58,
    '60': 60,
    '76': 76,
    '80-1': 80,
    '80': 80,
    '87': 87,
    '120-1': 120,
    '120': 120,
    '152': 152,
    '167': 167,
    '180': 180,
    '1024': 1024,
}

def setup_download_dir(directory):
    """ 设置文件夹，文件夹名为传入的 directory 参数，若不存在会自动创建 """
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except Exception as e:
            pass
    return True

def make_image_and_bg(str,txt):
    color = ImageColor.getrgb(str)
    img = Image.new("RGBA",(1024,1024),color)
    img.save(path +icon_color_name)
    make_image_text(img,txt)


#mac系统字体
def make_image_text(img,txt):
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path,size = font_size,encoding='unic')
    #“unic”（Unicode），“symb”（Microsoft Symbol），“ADOB”（Adobe Standard），“ADBE”（Adobe Expert）和“armn”（Apple Roman）
    #fill=(255, 255, 255, 0)
    d.text((x, y), txt, fill=fill_color,font=font ,spacing=spacing)
    #font是个imagefont实例 spacing字体间距 direction rtl ttb
    img.save(path + icon_color_name)
    # img.show()
    img.close()


def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    global icon_color_name
    icon_color_name = 'icon_' + color + '.png'
    return "#"+color

def make_app_all_icon():
   for pidImage in glob.glob(path + "/*.[jp][pn]g"):
        url = pidImage
        p1 = r'png/(.*)'
        pattern1 = re.compile(p1)  # 同样是编译
        matcher1 = re.search(pattern1, url)  # 同样是查询
        str1 = matcher1.group(0)
        b = str1.replace('png/', '')
        b = b.replace('.png', '')
        name = b
        new_path = path + name + '/';

        setup_download_dir(new_path)
        time.sleep(0.3)
        img = Image.open(pidImage)
        (x1, y1) = img.size  # read image size
        for key, value in a.items():
            out = img.resize((value, value), Image.ANTIALIAS)
            # 图片保存
            out.save(new_path + key+'.png')

        to_name_path = new_path + contents_json
        from_name_path = BASE_DIR + '/' + contents_json
        shutil.copyfile(from_name_path,to_name_path)



def make_icon_with_count(count):
    for i in range(count):
        color=randomcolor()
        app_main_color=color
        print(color)
        make_image_and_bg(color,txt)
    time.sleep(1)


if __name__ == "__main__":
    make_icon_with_count(icon_count)
    make_app_all_icon()



