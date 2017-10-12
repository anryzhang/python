# coding:utf-8
import xlwt
from xlwt import *
import xlrd
import time
import datetime, calendar
from imp import reload

import sys

reload(sys)
# sys.setdefaultencoding('utf-8')

writeIndexDict = {}

womanFrance = {'32.0': '154', '34.0': '155', '36.0': '156', '38.0': '157', '40.0': '158', '42.0': '159', '44.0': '160',
               'OZ': '1'}

categoryId = {"Dress": "1014",
              "Coat": "1000",
              "Top": "1013",
              "Accessory": "1025",
              "Jacket": "1009",
              "Bag": "1043",
              "Pants": "1021",
              "Skirt": "1015",
              "Jumpsuit": "1023"}

colourId = {"ecru ": "#FFFACD",
            "baby blue": "#63B8FF",
            "olive": "#C0FF3E",
            "azure blue": "#1E90FF",
            "mallow": "#FFF68F",
            "brandy brown": "#EEE9E9",
            "pomodoro": "#EE7600",
            "cream": "#EEE9E9",
            "rose": "#FFE4C4",
            "pink sand": "#EECBAD",
            "dark blue": "#00008B",
            "golden oak": "#FFC125",
            "black": "#000000",
            "shadow grey": "#838B83",
            "white": "#FFFFFF",
            "red": "#FF0000",
            "dusty green": "#00FF11",
            "brown": "#A52A2A",
            "floral": "#FFFAF0",
            "silver": "#F8F8FF",
            "red-orange": "#EE7942",
            "dark olive green": "#228B22",
            "biscuit": "#CDBE70",
            "dijon": "#CDCDCD",
            "grey": "#CCCCCC",
            "sand": "#F4A460",
            "cream melange": "#F5FFFA",
            "beige": "#F5F5DC",
            "melange rosette": "#EED5D2",
            "dusty rose": "#EED5D3",
            "rust": "#8B4500"}

# 映射关系， 下次分析时，只需要改此即可， 数字对应的是列的位置
k_brand_name = 1  # 名字
k_brand_code = 8  # 唯一码
k_composition = 9  # 材料
k_category = 4  # 类别
k_colour = 5  # 颜色
k_size = 7  # 尺寸
k_WSP = 11  # 批发价
k_RSP = 11  # 零售价


# COAT=女外套 top=女上衣 dress=连衣裙 jacket=女夹克 skirt=半身裙 pants=裤子
# 女装法国码。 女装法国码  女装法国码  女装法国码  女装法国码。女裤美国码
# 1021是美国码，其他为法国码
# 更新，全部用法国码（陈挺sucre）

def read_excel(sheetIndex):
    # 打开文件
    workbook = xlrd.open_workbook(r'./ordersheet.xlsx')
    # 获取所有sheet
    # # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(sheetIndex)  # sheet索引从0开始

    ## 每行
    # for row in xrange(2, sheet1.nrows):
    for row in list(range(2, sheet1.nrows)):
        style = sheet1.row_values(row)
        styleName = style[k_brand_code]  # 根据款号去重
        if writeIndexDict.get(styleName, 0):
            cols = writeIndexDict.get(styleName, 0)
            if (style[k_composition] in cols["composition"]) and (str(style[k_WSP]) in cols["WSP"]) and (
                        str(style[k_RSP]) in cols["RSP"]):  # 材质
                name = str(style[k_composition]) + str(style[k_WSP]) + str(style[k_RSP])

                if style[k_colour] not in cols["diff"][name]["colour"]:
                    cols["diff"][name]["colour"].append(style[k_colour])

                if style[k_colour] not in cols["diff"][name]["size"]:
                    cols["diff"][name]["size"].append(str(style[k_size]))
                continue

            cols["composition"].append(style[k_composition])
            cols["WSP"].append(str(style[k_WSP]))
            cols["RSP"].append(str(style[k_RSP]))
            diffDict = {}
            diffDict["Brand_name"] = style[k_brand_name]
            diffDict["brand_code"] = style[k_brand_code]
            diffDict["composition"] = style[k_composition]
            diffDict["category"] = style[k_category]
            diffDict["colour"] = [style[k_colour]]
            diffDict["size"] = [str(style[k_size])]
            diffDict["WSP"] = str(style[k_WSP])  # 批发价
            diffDict["RSP"] = str(style[k_RSP])  # 零售价
            name = str(style[k_composition]) + str(style[k_WSP]) + str(style[k_RSP])
            cols["diff"][name] = diffDict

        else:
            cols, diffAll, diffDict = {}, {}, {}
            cols["composition"] = [style[k_composition]]
            cols["WSP"] = [str(style[k_WSP])]
            cols["RSP"] = [str(style[k_RSP])]

            diffDict["Brand_name"] = style[k_brand_name]
            diffDict["brand_code"] = style[k_brand_code]
            diffDict["composition"] = style[k_composition]
            diffDict["category"] = style[k_category]
            diffDict["colour"] = [style[k_colour]]
            diffDict["size"] = [str(style[k_size])]
            diffDict["WSP"] = str(style[k_WSP])
            diffDict["RSP"] = str(style[k_RSP])
            # 保存原始数据
            name = str(style[k_composition]) + str(style[k_WSP]) + str(style[k_WSP])
            diffAll[name] = diffDict
            # 保存原始数据和差异数据
            cols["diff"] = diffAll
            # 保存所有数据，第一次初始化
            writeIndexDict[styleName] = cols

    for item in writeIndexDict:
        writeIndexDict[item]["composition"] = list(set(writeIndexDict[item]["composition"]))
        writeIndexDict[item]["WSP"] = list(set(writeIndexDict[item]["WSP"]))
        writeIndexDict[item]["RSP"] = list(set(writeIndexDict[item]["RSP"]))


def init(workshell):
    workshell.write(0, 0, '款式惟一 id(用来作为款式图片的文件夹名称)')
    workshell.write(0, 1, '款式名称')
    workshell.write(0, 2, '款式编号')
    workshell.write(0, 3, '款式备注(简介)')
    workshell.write(0, 4, '款式类目 id')
    workshell.write(0, 5, '款式尺码 id(多个时用逗号隔开)')
    workshell.write(0, 6, '材质成分')
    workshell.write(0, 7, '币种')
    workshell.write(0, 8, '批发价')
    workshell.write(0, 9, '零售价')
    workshell.write(0, 10, '颜色1')
    workshell.write(0, 11, '颜色2')
    return workshell


def query_fengxian(workbook):
    # risk_score.score  fengxian
    # localtion_score.score  diyu
    workshell = init(workbook.add_sheet('sheet1', cell_overwrite_ok=True))
    # 索引，从第一行开始，第零行是标题
    p = 1
    for data in writeIndexDict:
        sheel(workshell, writeIndexDict[data], p)
        p += 1


# 偏移
deviation = 0


def sheel(workshell, data, p):
    global deviation

    # 真实数据
    colsAll = data["diff"]
    p = p + deviation
    # 保证唯一标示
    codeIndex = 0
    # 表示循环一次之后需要每次加 1, 因为一个code有多个子数据，每个子数据的col都应该 +1，然而第一次不用 +1
    loopIndex = 0

    for colsData in colsAll.values():
        p = p + loopIndex
        loopIndex = 1
        workshell.write(p, 0, colsData["brand_code"] + str(codeIndex))
        codeIndex += 1
        c = colsData["Brand_name"]
        style = xlwt.XFStyle()  # Create the Style
        if len(c) > 100:
            pattern = Pattern()  # 创建一个模式
            pattern.pattern = Pattern.SOLID_PATTERN  # 设置其模式为实型
            pattern.pattern_fore_colour = 2
            # 设置单元格背景颜色 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta,  the list goes on...
            style.pattern = pattern
            c = c[:100] + "==========" + c[100:]
            # lowstand neck blouse with lily-like two layered long sleeves with adjustable shirring on shoulder line

        workshell.write(p, 1, c, style)
        workshell.write(p, 2, colsData["brand_code"])
        workshell.write(p, 3, "-")
        workshell.write(p, 4, categoryId[colsData["category"]])
        workshell.write(p, 6, colsData["composition"])
        workshell.write(p, 7, "EUR")
        workshell.write(p, 8, colsData["WSP"])
        workshell.write(p, 9, "0")

        allSize = ''

        for size in colsData["size"]:
            if size == 'FREESIZE':
                allSize = allSize + '1' + ","
            else:
                allSize = allSize + womanFrance[size] + ","
        workshell.write(p, 5, allSize[:-1])

        colorIndex = 0
        for x in colsData["colour"]:
            workshell.write(p, 10 + colorIndex, x + ":" + colourId[x])
            colorIndex += 1
    # 每次 +1 后，需要统计加的总数， 作为一个基数，然后记录下次使用，
    deviation += len(colsAll) - 1


def saveXls(workbook):
    workbook.save("./款式.xls")


def article():
    workbook = None
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=True)
    query_fengxian(workbook)
    saveXls(workbook)


if __name__ == '__main__':
    read_excel(0)
    # lists = []
    # for x in writeIndexDict:
    #     for z in writeIndexDict[x]["size"]:
    #         lists.append(z)
    # for x in list(set(lists)): print x
    article()
