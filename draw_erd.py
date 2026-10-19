from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).resolve().parent
image = Image.new('RGB', (2400, 1700), 'white')
d = ImageDraw.Draw(image)
font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 27)
bold = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 29)
small = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 25)
title = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 45)
ink = '#17324d'
line_color = '#60758a'

def text(x, y, value, f=font, fill=ink):
    d.text((x, y), value, font=f, fill=fill, anchor='mm')

def line(points):
    d.line(points, fill=line_color, width=4)

def entity(x, y, label, w=270):
    d.rectangle((x-w/2, y-38, x+w/2, y+38), fill='#deedff', outline='#28609b', width=4)
    text(x,y,label,bold)

def relation(x,y,label,w=170,h=60):
    d.polygon([(x,y-h),(x+w,y),(x,y+h),(x-w,y)], fill='#e5f3eb', outline='#2e7654', width=4)
    text(x,y,label,bold)

def attribute(x,y,label,w=130,key=False,derived=False):
    box=(x-w,y-35,x+w,y+35)
    d.ellipse(box,fill='#fff6df',outline='#aa7b26',width=3)
    if derived:
        # Dashed inner ellipse identifies a derived attribute.
        inner=(x-w+7,y-28,x+w-7,y+28)
        for angle in range(0,360,24):
            d.arc(inner,angle,angle+13,fill='#aa7b26',width=2)
    text(x,y,label)
    if key:
        width=d.textlength(label,font=font)
        d.line((x-width/2,y+16,x+width/2,y+16),fill=ink,width=2)

text(1200,60,'ERD QUẢN LÝ ĐƠN ĐẶT HÀNG',title)
text(1200,112,'Mô hình khái niệm sau khi gộp Đơn vị đặt hàng và Đơn vị khách hàng',small)

# Connectors are drawn first to keep the node labels clear.
for points in [
    [(1200,270),(920,170)],[(1200,270),(1200,160)],
    [(1200,270),(1470,170)],[(1200,270),(1550,290)],
    [(1080,308),(650,440)],[(1320,308),(1750,440)],
    [(650,500),(650,592)],[(1750,500),(1750,592)],
    [(515,630),(290,560)],[(515,630),(290,685)],
    [(1885,630),(2140,560)],[(1885,630),(2140,685)],
    [(650,668),(650,820)],[(650,940),(650,1162)],
    [(480,880),(300,805)],[(480,880),(300,945)],[(650,940),(860,1010)],
    [(515,1200),(260,1110)],[(515,1200),(240,1260)],
    [(650,1238),(460,1400)],[(650,1238),(800,1400)],
    [(785,1200),(1160,1050)],
    [(1750,668),(1750,785),(1415,1020)],
    [(1330,1110),(1330,1342)],[(1500,1050),(1915,1200)],
    [(1330,990),(1160,850)],[(1330,990),(1420,850)],
    [(1500,1050),(1710,935)],[(1500,1050),(1720,1090)],
    [(1500,1050),(1720,1270)],
    [(1330,1418),(1130,1510)],[(1330,1418),(1460,1510)],
    [(2050,1162),(2170,1010)],[(2050,1238),(2140,1400)],
]: line(points)

entity(1200,270,'ĐƠN VỊ KHÁCH',300)
attribute(920,170,'Mã ĐV',key=True)
attribute(1200,160,'Tên ĐV')
attribute(1470,170,'Địa chỉ')
attribute(1550,290,'Điện thoại')
relation(650,440,'THUỘC',140)
relation(1750,440,'THUỘC',140)
text(1010,330,'1',bold)
text(1390,330,'1',bold)
text(685,550,'N',bold)
text(1785,550,'N',bold)

entity(650,630,'NGƯỜI ĐẶT')
attribute(290,560,'Mã số NĐ',key=True)
attribute(290,685,'Họ tên NĐ')
entity(1750,630,'NGƯỜI NHẬN')
attribute(2140,560,'Mã số NN',key=True)
attribute(2140,685,'Họ tên NN')

relation(650,880,'ĐẶT')
attribute(300,805,'Số ĐH',key=True)
attribute(300,945,'Ngày đặt')
attribute(860,1010,'Số lượng đặt',w=145)
entity(650,1200,'HÀNG')
attribute(260,1110,'Mã hàng',key=True)
attribute(240,1260,'Tên hàng')
attribute(460,1400,'Đơn vị tính')
attribute(800,1400,'Mô tả hàng')

relation(1330,1050,'GIAO')
attribute(1160,850,'Số PG',key=True)
attribute(1420,850,'Ngày giao')
attribute(1710,935,'Số lượng giao',w=150)
attribute(1720,1090,'Đơn giá')
attribute(1720,1270,'Thành tiền',derived=True)
entity(1330,1380,'NGƯỜI GIAO')
attribute(1130,1510,'Mã số NG',key=True)
attribute(1460,1510,'Họ tên NG')
entity(2050,1200,'NƠI GIAO')
attribute(2170,1010,'Tên nơi giao',w=150)
attribute(2140,1400,'Mã số ĐĐG',key=True)

d.line((100,1595,2300,1595),fill='#cbd5df',width=2)
text(1200,1630,'Hình chữ nhật: thực thể  |  Hình thoi: quan hệ  |  Hình elip: thuộc tính  |  Gạch chân: định danh',small)
text(1200,1670,'Thành tiền là thuộc tính suy ra: Số lượng giao × Đơn giá. Quan hệ GIAO liên kết đồng thời 4 thực thể.',small)
image.save(ROOT/'erd-quan-ly-don-dat-hang.png',optimize=True)
