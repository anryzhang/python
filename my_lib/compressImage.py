# coding:utf-8
from PIL import Image
import shutil
import os


# 图片压缩批处理
def compressImage(srcPath, dstPath):
    for filename in os.listdir(srcPath):
        # 如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)

        # 拼接完整的文件或文件夹路径
        srcFile = os.path.join(srcPath, filename)
        dstFile = os.path.join(dstPath, filename)

        # 如果是文件就处理
        if os.path.isfile(srcFile):
            print(srcFile);
            # 如果是需要改变的格式就处理，否则就原样写入
            if (srcFile.endswith(".jpg") or srcFile.endswith(".JPG") or
                    srcFile.endswith(".png") or srcFile.endswith(".PNG") or
                    srcFile.endswith(".jpeg") or srcFile.endswith(".JPEG") or
                    srcFile.endswith(".bmp") or srcFile.endswith(".BMP")
                ) is False:
                print("非图片路径检查    " + srcFile)
                shutil.copyfile(srcFile, dstFile)
                continue
            # 打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
            sImg = Image.open(srcFile)
            w, h = sImg.size
            print(w)
            print(h)
            dImg = sImg.resize((w/2, h/2), Image.ANTIALIAS)  # 设置压缩尺寸和选项，注意尺寸要用括号
            dImg.save(dstFile)  # 也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
            print(dstFile + " compressed succeeded")

        # 如果是文件夹就递归
        if os.path.isdir(srcFile):
            compressImage(srcFile, dstFile)


if __name__ == '__main__':
    compressImage("/Users/ziyu/Documents/AERON/系列信息/系列1-2018SS", "/Users/ziyu/Documents/AERON/系列信息/系列1-2018SS_bk")
