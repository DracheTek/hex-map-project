# 菜单参考

## 菜单按钮参考

要生成菜单按钮，调用函数

mb = Menubutton(parent, args**)

## 菜单对象参考

要生成菜单，调用函数

m = Menu(parent, args**)

要将菜单注册到菜单按钮：

parent.menu = m
parent["menu"] = m

菜单的添加内容有五种：
Cascade: 折叠菜单。点击显示另一组菜单
command: 指令。执行一个指令。
checkbutton: 复选按钮
radiobutton: 单选按钮
separator: 分割线
要向菜单添加内容，调用五个添加函数之一

.add(kind, coption, ...) 添加五种类别之一。
kind：字符串'cascade', 'checkbutton', 'command', 'radiobutton', 'separator'五选一
coption 见下文

.add_cascade(coption, ...)
.add_checkbutton(coption, ...)
.add_command(coption, ...)
.add_radiobutton(coption, ...)
.add_separator()

要在已有的菜单中间插入内容，使用以下五个函数。新内容会代替原有的值，原值向下顺延。

.insert_cascade(index, coption, ...)
.insert_checkbutton(index, coption, ...)
.insert_command(index, coption, ...)
.insert_radiobutton(index, coption, ...)
.insert_separator(index)

Table 23. Menu widget options

activebackground
The background color that will appear on a choice when it is under the mouse. See Section 5.3, “Colors”.
activeborderwidth
Specifies the width of a border drawn around a choice when it is under the mouse. Default is 1 pixel. For possible values, see Section 5.1, “Dimensions”.
activeforeground
The foreground color that will appear on a choice when it is under the mouse.
bg or background
The background color for choices not under the mouse.
bd or borderwidth
The width of the border around all the choices; see Section 5.1, “Dimensions”. The default is one pixel.
cursor
The cursor that appears when the mouse is over the choices, but only when the menu has been torn off. See Section 5.8, “Cursors”.
disabledforeground
The color of the text for items whose state is tk.DISABLED.
font
The default font for textual choices. See Section 5.4, “Type fonts”.
fg or foreground
The foreground color used for choices not under the mouse.
postcommand
You can set this option to a procedure, and that procedure will be called every time someone brings up this menu.
relief
The default 3-D effect for menus is relief=tk.RAISED. For other options, see Section 5.6, “Relief styles”.
selectcolor
Specifies the color displayed in checkbuttons and radiobuttons when they are selected.
tearoff
Normally, a menu can be torn off: the first position (position 0) in the list of choices is occupied by the tear-off element, and the additional choices are added starting at position 1. If you set tearoff=0, the menu will not have a tear-off feature, and choices will be added starting at position 0.
tearoffcommand
If you would like your program to be notified when the user clicks on the tear-off entry in a menu, set this option to your procedure. It will be called with two arguments: the window ID of the parent window, and the window ID of the new tear-off menu's root window.
title
Normally, the title of a tear-off menu window will be the same as the text of the menubutton or cascade that lead to this menu. If you want to change the title of that window, set the title option to that string.

以上没有提到的其他函数：

.delete(index1, index2=None)
This method deletes the choices numbered from index1 through index2, inclusive. To delete one choice, omit the index2 argument. You can't use this method to delete a tear-off choice, but you can do that by setting the menu object's tearoff option to 0.

.entrycget(index, coption)
To retrieve the current value of some coption for a choice, call this method with index set to the index of that choice and coption set to the name of the desired option.

.entryconfigure(index, coption, ...)
To change the current value of some coption for a choice, call this method with index set to the index of that choice and one or more coption=value arguments.

.index(i)
Returns the position of the choice specified by index i. For example, you can use .index(tk.END) to find the index of the last choice (or None if there are no choices).

.invoke(index)
Calls the command callback associated with the choice at position index. If a checkbutton, its state is toggled between set and cleared; if a radiobutton, that choice is set.

.post(x, y)
Display this menu at position (x, y) relative to the root window.

.type(index)
Returns the type of the choice specified by index: either tk.CASCADE, tk.CHECKBUTTON, tk.COMMAND, tk.RADIOBUTTON, tk.SEPARATOR, or tk.TEAROFF.

.yposition(n)
For the nth menu choice, return the vertical offset in pixels relative to the menu's top. The purpose of this method is to allow you to place a popup menu precisely relative to the current mouse position.

Table 24. Menu item coption values

accelerator
字符串：显示“加速键”，在菜单尾端显示快捷键。如果是Ctrl+按键，输入字符串"'^X'"
注意这个选项只是显示文字，并不实装快捷键。
To display an “accelerator” keystroke combination on the right side of a menu choice, use the option “accelerator=s” where s is a string containing the characters to be displayed. For example, to indicate that a command has Control-X as its accelerator, use the option “accelerator='^X'”. Note that this option does not actually implement the accelerator; use a keystroke binding to do that.
activebackground
鼠标指向时的背景色
The background color used for choices when they are under the mouse.
activeforeground
鼠标指向时的前景色
The foreground color used for choices when they are under the mouse.
background
没有指向时的背景色
The background color used for choices when they are not under the mouse. Note that this cannot be abbreviated as bg.
bitmap
显示一个位图作为该选项的图标
Display a bitmap for this choice; see Section 5.7, “Bitmaps”.
columnbreak
从此处截断菜单，在右边形成一个新菜单列
输入值可以是数字0、1或bool值True、False
command
要调用的过程
A procedure to be called when this choice is activated.
compound
If you want to display both text and a graphic (either a bitmap or an image) on a menu choice, use this coption to specify the location of the graphic relative to the text. Values may be any of tk.LEFT, tk.RIGHT, tk.TOP, tk.BOTTOM, tk.CENTER, or tk.NONE. For example, a value of “compound=tk.TOP” would position the graphic above the text.
font
The font used to render the label text. See Section 5.4, “Type fonts”
foreground
The foreground color used for choices when they are not under the mouse. Note that this cannot be abbreviated as fg.
hidemargin
By default, a small margin separates adjacent choices in a menu. Use the coption “hidemargin=True” to suppress this margin. For example, if your choices are color swatches on a palette, this option will make the swatches touch without any other intervening color.
image
Display an image for this choice; see Section 5.9, “Images”.
label
The text string to appear for this choice.
menu
This option is used only for cascade choices. Set it to a Menu object that displays the next level of choices.
offvalue
Normally, the control variable for a checkbutton is set to 0 when the checkbutton is off. You can change the off value by setting this option to the desired value. See Section 52, “Control variables: the values behind the widgets”.
onvalue
Normally, the control variable for a checkbutton is set to 1 when the checkbutton is on. You can change the on value by setting this option to the desired value.
selectcolor
Normally, the color displayed in a set checkbutton or radiobutton is red. Change that color by setting this option to the color you want; see Section 5.3, “Colors”.
selectimage
If you are using the image option to display a graphic instead of text on a menu radiobutton or checkbutton, if you use selectimage=I, image I will be displayed when the item is selected.
state
Normally, all choices react to mouse clicks, but you can set state=tk.DISABLED to gray it out and make it unresponsive. This coption will be tk.ACTIVE when the mouse is over the choice.
underline
Normally none of the letters in the label are underlined. Set this option to the index of a letter to underline that letter.
value
Specifies the value of the associated control variable (see Section 52, “Control variables: the values behind the widgets”) for a radiobutton. This can be an integer if the control variable is an IntVar, or a string if the control variable is a StringVar.
variable
For checkbuttons or radiobuttons, this option should be set to the control variable associated with the checkbutton or group of radiobuttons. See Section 52, “Control variables: the values behind the widgets”.