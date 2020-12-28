# Canvas 参考

画布是用来绘图的矩形控件

A canvas is a rectangular area intended for drawing pictures or other complex layouts. On it you can place graphics, text, widgets, or frames. See the following sections for methods that create objects on canvases:

函数：

- create_bitmap():
- create_image:
- create_arc():绘制圆弧
- create_line(x0, y0, x1, y1, ..., xn, yn, option, ...):绘制连接点p1,p2...pn的折线。详见option
- create_oval():绘制椭圆
- create_polygon(x0, y0, x1, y1, ..., option, ...):绘制以点p1,p2...pn为顶点的多边形
- create_rectangle():绘制矩形
- create_text():插入文本
- create_window():制作子窗口

TK的原型形状不支持RGBA，但是可以通过位图填充 stipple 选项填充“gray50”等位图来模拟不透明度。

如果要用真正的不透明度，可以用pillow生成图片。

To create a Canvas object:


w = tk.Canvas(parent, option=value, ...)
The constructor returns the new Canvas widget. Supported options include:

Table 6. Canvas widget options

bd or borderwidth
数值，画布边缘的宽度。默认2像素
Width of the border around the outside of the canvas; see Section 5.1, “Dimensions”. The default is two pixels.
bg or background
“颜色”字符串，画布背景颜色，默认浅灰色"#E4E4E4"
Background color of the canvas. Default is a light gray, about '#E4E4E4'.
closeenough
浮点数。图块激活阈值。默认为1.0
A float that specifies how close the mouse must be to an item to be considered inside it. Default is 1.0.
confine
卷动限制。设为true时不能卷动到图画范围之外。
If true (the default), the canvas cannot be scrolled outside of the scrollregion (see below).
cursor
光标
Cursor used in the canvas. See Section 5.8, “Cursors”.
height
画布高度
Size of the canvas in the Y dimension. See Section 5.1, “Dimensions”.
highlightbackground
画布失焦时的背景颜色
Color of the focus highlight when the widget does not have focus. See Section 53, “Focus: routing keyboard input”.
highlightcolor
画布高亮时的背景颜色
Color shown in the focus highlight.
highlightthickness
高亮颜色厚度。默认值为1
Thickness of the focus highlight. The default value is 1.
relief
The relief style of the canvas. Default is tk.FLAT. See Section 5.6, “Relief styles”.
scrollregion
A tuple (w, n, e, s) that defines over how large an area the canvas can be scrolled, where w is the left side, n the top, e the right side, and s the bottom.
selectbackground
The background color to use displaying selected items.
selectborderwidth
The width of the border to use around selected items.
selectforeground
The foreground color to use displaying selected items.
takefocus
Normally, focus (see Section 53, “Focus: routing keyboard input”) will cycle through this widget with the tab key only if there are keyboard bindings set for it (see Section 54, “Events” for an overview of keyboard bindings). If you set this option to 1, focus will always visit this widget. Set it to '' to get the default behavior.
width
Size of the canvas in the X dimension. See Section 5.1, “Dimensions”.
xscrollincrement
Normally, canvases can be scrolled horizontally to any position. You can get this behavior by setting xscrollincrement to zero. If you set this option to some positive dimension, the canvas can be positioned only on multiples of that distance, and the value will be used for scrolling by scrolling units, such as when the user clicks on the arrows at the ends of a scrollbar. For more information on scrolling units, see Section 22, “The Scrollbar widget”.
xscrollcommand
If the canvas is scrollable, set this option to the .set() method of the horizontal scrollbar.
yscrollincrement
Works like xscrollincrement, but governs vertical movement.
yscrollcommand
If the canvas is scrollable, this option should be the .set() method of the vertical scrollbar.
