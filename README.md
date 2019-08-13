# make_icon
生成icon脚本

## 安装Pillow依赖
```
pip install -r requirements.txt
```

## make_icon.py 

根据个人所需的内容定制此配置文件
```
icon_count = 10 #设置生成纯背景图片个数
txt = '初  中\n古  诗' #设置生成图片上文字内容
app_main_color="#FF0000" #背景图片颜色-程序中随机替换颜色
icon_color_name ='' #icon名字 命名方式 (icon_颜色.png)
font_size = 180 #图片文字字体大小
x = 250 #图片文字起始位置X
y =250  #图片文字起始位置Y
fill_color ='white'  #图片文字颜色
spacing = 200  #图片文字间距
font_path = "/System/Library/Fonts/Hiragino Sans GB.ttc" #系统字体路径（以mac为例）
contents_json = "Contents.json" #生成iOS icon使用的json文件
```

## make_gradual_icon.py 生成渐变色icon 

根据个人所需的内容定制此配置文件
```
icon_count = 20 #设置生成纯背景图片个数
txt = '杨     过\n小  龙  女 ' #设置生成图片上文字内容
app_main_color="#FF0000" #背景图片颜色-程序中随机替换颜色
icon_color_name ='' #icon名字 命名方式 (icon_颜色.png)
font_size = 180 #图片文字字体大小
x = 150 #图片文字起始位置X
y =250  #图片文字起始位置Y
fill_color ='white'  #图片文字颜色
spacing = 200  #图片文字间距
contents_json = "Contents.json" #生成iOS icon使用的json文件
font_path = "/System/Library/Fonts/Hiragino Sans GB.ttc" #系统字体路径（以mac为例）
width = 1024 #图片宽
height = 1024  #图片高
```


## png
程序生成的图标文件和扩展图标大小目录，作者使用脚本生成20个icon文件放入其中


## Gradual
程序生成的渐变色图片

## Contents.json

生成iOS icon使用的json文件
