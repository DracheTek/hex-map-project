# 布局管理笔记

创建了任意小工具后，用variablename.grid()函数将小工具注册到几何关系管理器中，这样小工具才会显示。

## grid()函数

```python
    w.grid(option=value, ...)
```

函数的选项如下表：
This method registers a widget w with the grid geometry manager—if you don't do this, the widget will exist internally, but it will not be visible on the screen. For the options, see Table 1, “Arguments of the .grid() geometry manager”.

Table 1. Arguments of the .grid() geometry manager

column/row
整数，小工具所在的列/行。默认为0
The column number where you want the widget gridded, counting from zero. The default value is zero.
columnspan/rowspan
整数，小工具所跨的列/行数。默认为1
Normally a widget occupies only one cell in the grid. However, you can grab multiple cells of a row and merge them into one larger cell by setting the columnspan option to the number of cells. For example, w.grid(row=0, column=2, columnspan=3) would place widget w in a cell that spans columns 2, 3, and 4 of row 0.
in_
将小工具作为其他小工具的子项目显示，格式in_=w2。母项目w2必须先于子项目w创建**并**注册到其母项目。
To register w as a child of some widget w2, use in_=w2. The new parent w2 must be a descendant of the parent widget used when w was created.
ipadx
内部左右间隔
Internal x padding. This dimension is added inside the widget inside its left and right sides.
ipady
内部上下间隔
Internal y padding. This dimension is added inside the widget inside its top and bottom borders.
padx
外部左右间隔
External x padding. This dimension is added to the left and right outside the widget.
pady
外部上下间隔
External y padding. This dimension is added above and below the widget.
sticky
子widget如何占据母widget的空间。默认为居中放置，选项如下：
This option determines how to distribute any extra space within the cell that is not taken up by the widget at its natural size. See below.

If you do not provide a sticky attribute, the default behavior is to center the widget in the cell.

You can position the widget in a corner of the cell by using sticky=tk.NE (top right), tk.SE (bottom right), tk.SW (bottom left), or tk.NW (top left).

You can position the widget centered against one side of the cell by using sticky=tk.N (top center), tk.E (right center), tk.S (bottom center), or tk.W (left center).

Use sticky=tk.N+tk.S to stretch the widget vertically but leave it centered horizontally.

Use sticky=tk.E+tk.W to stretch it horizontally but leave it centered vertically.

Use sticky=tk.N+tk.E+tk.S+tk.W to stretch the widget both horizontally and vertically to fill the cell.

The other combinations will also work. For example, sticky=tk.N+tk.S+tk.W will stretch the widget vertically and place it against the west (left) wall.
