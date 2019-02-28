import hashlib
from datetime import datetime
from io import BytesIO
from random import randint
from settings import *
from PIL import ImageFont,Image,ImageDraw
class VerifyCode:
    def __init__(self,width=100,height=40,size=4):
        """
        # :param width: 验证码宽度
        # :param height: 验证码高度
        # :param size: 验证码长度
        """
        self.width = width if width > 0 else 100
        self.height = height if height > 0 else 40
        self.size = size if size > 0 else 4
        self.pen = None  # 画笔
        self.code = '' # 保存验证字符串


    def generate(self):
        # 1.生成画布
        im = Image.new('RGB',(self.width,self.height),self.randColor(160,255))

        # 2 生成画笔
        self.pen = ImageDraw.Draw(im)

        # 3 生成随机字符串
        self.randString()

        # 4 画字符串
        self.__drawCode()

        # 5 画干扰点
        self.__drawPoint()
        # 6 画干扰线
        self.__drawLine()

        # 7 保存图片
        # im.save('vc.jpg')
        buf = BytesIO()
        im.save(buf,'png')
        res = buf.getvalue()
        buf.close()
        return res
    def __drawLine(self):
        """
        画干扰线
        :return:
        """
        for i in range(5):
            start = (randint(1,self.width-1),randint(1,self.height-1))
            end = (randint(1,self.width-1),randint(1,self.height-1))
            self.pen.line([start,end],fill=self.randColor(50,150),width=1)
    def __drawPoint(self):
        """
        画干扰点
        :return:
        """
        for i in range(200):
            x = randint(1,self.width - 1)
            y = randint(1,self.height - 1)
            self.pen.point((x,y),fill=self.randColor(30,100))

    def __drawCode(self):
        """
        画验证码字符串
        :return:
        """
        myFont = ImageFont.truetype('STFANGSO.TTF',size=20,encoding='utf-8')
        for i in range(self.size):
            x = 15 + i * (self.width - 20)/self.size  # 字符等间距
            y =  randint(5,10)  # 随机高度
            self.pen.text((x,y),self.code[i],fill=self.randColor(0,60),font=myFont)

    def randString(self):
        """
        产生随机整数字符串
        :return: 无
        """
        result = ''
        for i in range(self.size):
            result += str(randint(0,9))
        self.code = result

    def randColor(self,low,high):
        """

        :param low:
        :param high:
        :return:
        """
        return randint(low,high), randint(low,high), randint(low,high)

# 子类化，扩展父类功能
class StrCode(VerifyCode):
    def randString(self):
        s1 = hashlib.md5(b'122').hexdigest()
        # print(s1)
        self.code =  s1[:self.size]

if __name__ == "__main__":
    # vc = VerifyCode()
    vc = StrCode()
    vc.generate()
    print(vc.code)