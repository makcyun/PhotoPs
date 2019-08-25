from removebg import RemoveBg
import os

from PIL import Image
from tkinter.filedialog import askdirectory  # 调用 tkinter 库直接选择路径而不是输出路径
import tkinter as tk

root = tk.Tk()    # 创建一个Tkinter.Tk()实例
root.withdraw()       # 将Tkinter.Tk()实例隐藏

"""
    可用api pMx4gP2zzQcBtkHAJnBXAL3Z
    # https://blog.csdn.net/zjiang1994/article/details/53513377

    添加下面两行代码让程序运行后不出现小框：
    root = tk.Tk()    # 创建一个Tkinter.Tk()实例
    root.withdraw()       # 将Tkinter.Tk()实例隐藏

    https://blog.csdn.net/weixin_40283816/article/details/83387965

"""
star = '* ' * 10
print(star * 3)
print(star * 3, '\n')

print("%s-%s-%s" % (' ' * 10, ' 欢迎使用一键抠图小程序 by「莱蒙」 ', ' ' * 10))
print("%s-%s-%s" % (' ' * 15, ' 公众号「佳软神器」 ', ' ' * 15))
print("%s-%s-%s" % (' ' * 20, ' 2019/07/18 ', '\n'))

print(star * 3)
print(star * 3, '\n')

api = input('请输入你的 API key：')

class Koutu():
    """docstring for koutu"""
    def __init__(self):
        self.open_times = 1 # 设置文件夹打开次数，避免输入错文件夹程序无限循环

    def check_path(self):
        # while self.open_times <4: # 输错三次就推出程序
        try:
            self.path = askdirectory() # 弹出文件夹选择框
            # self.path = input('请输入图片所在文件夹：')

            if not os.listdir(self.path):
                while self.open_times <4: # 输错三次就退出程序
                    print('文件夹没有图片,请重新选择')
                    self.open_times +=1
                    self.check_path()
                    break
                # return None

        except OSError:
            while self.open_times <4: # 输错三次就退出程序
                print('文件夹路径不存在，请重新选择')
                self.open_times +=1
                self.check_path()
                break


    def koutu(self):
        rmbg = RemoveBg(api, "error.log")
        # rmbg = RemoveBg("pMx4gP2zzQcBtkHAJnBXAL3Z", "error.log")

        # path = '%s\picture' % os.getcwd()
        # path = 'C:\\Users\\sony\\Desktop\\picture'

        print('请稍等正在抠图中...', '\n')

        for num,pic in enumerate(os.listdir(self.path),start=1):
            rmbg.remove_background_from_img_file("%s/%s" % (self.path, pic))
            print('第 %s 张图片抠图完成'%num)

        print('图片抠图完成', '\n')
        choice = (input("若要继续抠图请按 y ; 结束请按任意键..."))

        if choice != 'y':
            pass
        else:
            self.check_path()
            self.koutu()

    def change_background(self):
        path = os.listdir(self.path)
        color = input("更换蓝色背景按 b；红色背景按 r；白色背景按 w \n...")
        for pic in path:
            picturename = "%s/%s" % (self.path, pic)

            im = Image.open(picturename)
            x, y = im.size
            # (alpha band as paste mask).
            try:
                if color == 'b':
                    change_color = (1, 104, 179)  # blue

                elif color == 'r':
                    change_color = (240, 0, 0)  # red

                elif color == 'w':
                    change_color = (255, 255, 255)  # blue
                p = Image.new('RGB', im.size, change_color)
                p.paste(im, (0, 0, x, y), im)

                p.save('%s_%s.png' %
                       (picturename.rstrip('.jpg_no_bg.png'), color))
            except:
                pass

        choice = (input("若要继续更换背景请按 y ; 结束请按任意键\n..."))
        if choice != 'y':
            pass
        else:
            self.change_background()


if __name__ == '__main__':

    koutu = Koutu()
    koutu.check_path()
    if api:
        try:
            koutu.koutu()
            koutu.change_background()
        except:
            pass

    # 直接换背景
    else:
        try:
            koutu.change_background()
        except:
            pass


