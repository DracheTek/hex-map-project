# 指令与事件笔记

## 将应用逻辑连接到小工具

有两种方法做事件响应：

1. 有的控制（例如“键盘按下”）具有command属性，可以定义一段过程，调用一个句柄。
2. 使用按钮小工具的事件序列。按钮小工具需求：1. 用户在左键放开状态下将鼠标移到小工具上；2. 用户在小工具上单击左键；3. 用户将鼠标保持在小工具上放开左键。

使用事件处理机制则可以应对更加一般的输入和操作。

许多小工具具有“控制变量”，允许直接用小工具控制其他小工具的变量。

## 控制变量

控制变量由小工具储存，被本身或其他小工具使用。控制变量提供者会记住哪些小工具在使用哪个控制变量。

复选框的控制变量是选中与否
一群单选框会储存一个控制变量，指示哪个单选框被选中了。
文本框，标签，按钮等会保持一个字符串作为控制变量。

要获得控制变量，使用以下构造函数

```python
    v = tk.DoubleVar()   # Holds a float; default value 0.0 双精度浮点数。默认0
    v = tk.IntVar()      # Holds an int; default value 0 整数。默认0
    v = tk.StringVar()   # Holds a string; default value '' 字符串，默认空字符串
```

控制变量有get和set两个函数用来读写值。set在主循环的下一个空闲时间进行。see .update_idletasks() in Section 26, “Universal widget methods” for more information on controlling this update cycle.

具体小工具的具体控制变量的作用如下：

Here are some comments on how control variables are used with specific widgets:

Button
You can set its textvariable to a StringVar. Anytime that variable is changed, the text on the button will be updated to display the new value. This is not necessary unless the button's text is actually going to change: use the text attribute if the button's label is static.

Checkbutton
Normally, you will set the widget's variable option to an IntVar, and that variable will be set to 1 when the checkbutton is turned on and to 0 when it is turned off. However, you can pick different values for those two states with the onvalue and offvalue options, respectively.

You can even use a StringVar as the checkbutton's variable, and supply string values for the offvalue and onvalue. Here's an example:

    self.spamVar = tk.StringVar()
    self.spamCB  = tk.Checkbutton(self, text='Spam?',
        variable=self.spamVar, onvalue='yes', offvalue='no')
If this checkbutton is on, self.spamVar.get() will return the string 'yes'; if the checkbutton is off, that same call will return the string 'no'. Furthermore, your program can turn the checkbutton on by calling .set('yes').

You can also the textvariable option of a checkbutton to a StringVar. Then you can change the text label on that checkbutton using the .set() method on that variable.

Entry
Set its textvariable option to a StringVar. Use that variable's .get() method to retrieve the text currently displayed in the widget. You can also the variable's .set() method to change the text displayed in the widget.

Label
You can set its textvariable option to a StringVar. Then any call to the variable's .set() method will change the text displayed on the label. This is not necessary if the label's text is static; use the text attribute for labels that don't change while the application is running.

Menubutton
If you want to be able to change the text displayed on the menu button, set its textvariable option to a StringVar and use that variable's .set() method to change the displayed text.

Radiobutton
The variable option must be set to a control variable, either an IntVar or a StringVar. All the radiobuttons in a functional group must share the same control variable.

Set the value option of each radiobutton in the group to a different value. Whenever the user sets a radiobutton, the variable will be set to the value option of that radiobutton, and all the other radiobuttons that share the group will be cleared.

You might wonder, what state is a group of radiobuttons in when the control variable has never been set and the user has never clicked on them? Each control variable has a default value: 0 for an IntVar, 0.0 for a DoubleVar, and '' for a StringVar. If one of the radiobuttons has that value, that radiobutton will be set initially. If no radiobutton's value option matches the value of the variable, the radiobuttons will all appear to be cleared.

If you want to change the text label on a radiobutton during the execution of your application, set its textvariable option to a StringVar. Then your program can change the text label by passing the new label text to the variable's .set() method.

Scale
For a scale widget, set its variable option to a control variable of any class, and set its from_ and to options to the limiting values for the opposite ends of the scale.

For example, you could use an IntVar and set the scale's from_=0 and to=100. Then every user change to the widget would change the variable's value to some value between 0 and 100 inclusive.

Your program can also move the slider by using the .set() method on the control variable. To continue the above example, .set(75) would move the slider to a position three-fourths of the way along its trough.

To set up a Scale widget for float values, use a DoubleVar.

You can use a StringVar as the control variable of a Scale widget. You will still need to provide numeric from_ and to values, but the numeric value of the widget will be converted to a string for storage in the StringVar. Use the scale's digits option to control the precision of this conversion.

## 焦点与键盘输入

某个小工具“被高亮”表示键盘输入在该小工具上有效

“焦点转移顺序”表示按tab键切换小工具焦点的顺序。按shift+tab逆序切换。具体顺序如下

文本框和输入框有焦点时，键盘输入默认被记载在框内，左右等编辑按键可以移动光标。

在文本框焦点条件下按tab输入\t符号。按ctrl+tab转移焦点。

按钮作为焦点时，默认按空格调用“按动”事件

复选框用空格勾选和取消。

下拉列表/列表框中按上下键上下滚动。按pageup和pagedn键滚动一页。按空格选中或取消选中当前内容

按空格键选中单选框

垂直缩放条和滚动条会响应上下键，水平则会响应左右键。按pageup和pagedn滚动一页（滚动条的一滑块长度）

多数小工具具有高亮提示功能，可以设置。

Frame, Label, Menu一般不会被作为焦点。将takefocus置为1可以将其插入焦点序列。默认在焦点序列内的widget也可以通过将takefocus设为0取出焦点序列。

默认的焦点序列如下：

同一母工具的子工具，按照创建顺序移动焦点。
带有子工具的母工具，焦点会先移动到这些母工具，之后移动到该母工具的子工具。之后按照创建顺序移动到下一个母工具。
总之，焦点按照工具创建的顺序移动。
用鼠标指引焦点的方法，见26, “Universal widget methods”, refer to the .tk_focusFollowsMouse() method.

If you create a ttk widget and do not specify its takefocus option, by default, all ttk widgets get focus except for Frame, Label, LabelFrame, PanedWindow, Progressbar, Scrollbar, Separator, and Sizegrip.

## 事件

An event is something that happens to your application—for example, the user presses a key or clicks or drags the mouse—to which the application needs to react.

The widgets normally have a lot of built-in behaviors. For example, a button will react to a mouse click by calling its command callback. For another example, if you move the focus to an entry widget and press a letter, that letter gets added to the content of the widget.

However, the event binding capability of Tkinter allows you to add, change, or delete behaviors.

First, some definitions:

An event is some occurrence that your application needs to know about.

An event handler is a function in your application that gets called when an event occurs.

### 事件的绑定

在调用事件句柄之前要先将事件对象绑定到小工具或应用上。

对象层：绑定到特定的小工具对象上。

例如，将一个事件绑定到画布上，条件是“鼠标按钮2按下”，内容是“绘制橙色球形”，这样做：

```python
    self.canv.bind('<Button-2>', self.__drawOrangeBlob)
```

类层：绑定到一个类的所有实例。

例如，给所有的画布绑定一个功能，按下鼠标中键是绘制橙色球体。这样做：

```python
    self.bind_class('Canvas', '<Button-2>', self.__drawOrangeBlob)
```

应用层：绑定一个事件到应用，不管现在的焦点在何处都先处理这种输入。

```python
    self.bind_all('<Key-Print>', self.__printScreen)
```

### 事件的顺序

事件通过事件模板生成。模板的形式是"<[修正若干个-]类别[-细节若干个]>"

修正的种类见下一章，类别的种类见下两章，细节的种类见“按键名”。

### 事件的类型

The full set of event types is rather large, but a lot of them are not commonly used. Here are most of the ones you'll need:

Type	Name	Description
36	Activate	A widget is changing from being inactive to being active. This refers to changes in the state option of a widget such as a button changing from inactive (grayed out) to active.
4	Button	The user pressed one of the mouse buttons. The detail part specifies which button. For mouse wheel support under Linux, use Button-4 (scroll up) and Button-5 (scroll down). Under Linux, your handler for mouse wheel bindings will distinguish between scroll-up and scroll-down by examining the .num field of the Event instance; see Section 54.6, “Writing your handler: The Event class”.
5	ButtonRelease	The user let up on a mouse button. This is probably a better choice in most cases than the Button event, because if the user accidentally presses the button, they can move the mouse off the widget to avoid setting off the event.
22	Configure	The user changed the size of a widget, for example by dragging a corner or side of the window.
37	Deactivate	A widget is changing from being active to being inactive. This refers to changes in the state option of a widget such as a radiobutton changing from active to inactive (grayed out).
17	Destroy	A widget is being destroyed.
7	Enter	The user moved the mouse pointer into a visible part of a widget. (This is different than the enter key, which is a KeyPress event for a key whose name is actually 'return'.)
12	Expose	This event occurs whenever at least some part of your application or widget becomes visible after having been covered up by another window.
9	FocusIn	A widget got the input focus (see Section 53, “Focus: routing keyboard input” for a general introduction to input focus.) This can happen either in response to a user event (like using the tab key to move focus between widgets) or programmatically (for example, your program calls the .focus_set() on a widget).
10	FocusOut	The input focus was moved out of a widget. As with FocusIn, the user can cause this event, or your program can cause it.
2	KeyPress	The user pressed a key on the keyboard. The detail part specifies which key. This keyword may be abbreviated Key.
3	KeyRelease	The user let up on a key.
8	Leave	The user moved the mouse pointer out of a widget.
19	Map	A widget is being mapped, that is, made visible in the application. This will happen, for example, when you call the widget's .grid() method.
6	Motion	The user moved the mouse pointer entirely within a widget.
38	MouseWheel	The user moved the mouse wheel up or down. At present, this binding works on Windows and MacOS, but not under Linux. For Windows and MacOS, see the discussion of the .delta field of the Event instance in Section 54.6, “Writing your handler: The Event class”. For Linux, see the note above under Button.
18	Unmap	A widget is being unmapped and is no longer visible. This happens, for example, when you use the widget's .grid_remove() method.
15	Visibility	Happens when at least some part of the application window becomes visible on the screen.


### 事件的修正变量

The modifier names that you can use in event sequences include:

Alt	True when the user is holding the alt key down.
Control	True when the user is holding the control key down.
Shift	True when the user is holding down the shift key.
Any	This modifier generalizes an event type. For example, the event pattern '<Any-KeyPress>' applies to the pressing of any key.
Double	Specifies two events happening close together in time. For example, <Double-Button-1> describes two presses of button 1 in rapid succession.
Lock	True when the user has pressed shift lock.
Triple	Like Double, but specifies three events in rapid succession.
You can use shorter forms of the events. Here are some examples:

'<1>' is the same as '<Button-1>'.

'x' is the same as '<KeyPress-x>'.

Note that you can leave out the enclosing '<…>' for most single-character keypresses, but you can't do that for the space character (whose name is '<space>') or the less-than (<) character (whose name is '<less>').

### 按键名

The detail part of an event pattern for a KeyPress or KeyRelease event specifies which key you're binding. (See the Any modifier, above, if you want to get all keypresses or key releases).

The table below shows several different ways to name keys. See Section 54.6, “Writing your handler: The Event class”, below, for more information on Event objects, whose attributes will describe keys in these same ways.

The .keysym column shows the “key symbol”, a string name for the key. This corresponds to the .keysym attribute of the Event object.

The .keycode column is the “key code.” This identifies which key was pressed, but the code does not reflect the state of various modifiers like the shift and control keys and the NumLock key. So, for example, both a and A have the same key code.

The .keysym_num column shows a numeric code equivalent to the key symbol. Unlike .keycode, these codes are different for different modifiers. For example, the digit 2 on the numeric keypad (key symbol KP_2) and the down arrow on the numeric keypad (key symbol KP_Down) have the same key code (88), but different .keysym_num values (65433 and 65458, respectively).

The “Key” column shows the text you will usually find on the physical key, such as tab.

There are many more key names for international character sets. This table shows only the “Latin-1” set for the usual USA-type 101-key keyboard. For the currently supported set, see the manual page for Tk keysym values.

.keysym	.keycode	.keysym_num	Key
Alt_L	64	65513	The left-hand alt key
Alt_R	113	65514	The right-hand alt key
BackSpace	22	65288	backspace
Cancel	110	65387	break
Caps_Lock	66	65549	CapsLock
Control_L	37	65507	The left-hand control key
Control_R	109	65508	The right-hand control key
Delete	107	65535	Delete
Down	104	65364	↓
End	103	65367	end
Escape	9	65307	esc
Execute	111	65378	SysReq
F1	67	65470	Function key F1
F2	68	65471	Function key F2
Fi	66+i	65469+i	Function key Fi
F12	96	65481	Function key F12
Home	97	65360	home
Insert	106	65379	insert
Left	100	65361	←
Linefeed	54	106	Linefeed (control-J)
KP_0	90	65438	0 on the keypad
KP_1	87	65436	1 on the keypad
KP_2	88	65433	2 on the keypad
KP_3	89	65435	3 on the keypad
KP_4	83	65430	4 on the keypad
KP_5	84	65437	5 on the keypad
KP_6	85	65432	6 on the keypad
KP_7	79	65429	7 on the keypad
KP_8	80	65431	8 on the keypad
KP_9	81	65434	9 on the keypad
KP_Add	86	65451	+ on the keypad
KP_Begin	84	65437	The center key (same key as 5) on the keypad
KP_Decimal	91	65439	Decimal (.) on the keypad
KP_Delete	91	65439	delete on the keypad
KP_Divide	112	65455	/ on the keypad
KP_Down	88	65433	↓ on the keypad
KP_End	87	65436	end on the keypad
KP_Enter	108	65421	enter on the keypad
KP_Home	79	65429	home on the keypad
KP_Insert	90	65438	insert on the keypad
KP_Left	83	65430	← on the keypad
KP_Multiply	63	65450	× on the keypad
KP_Next	89	65435	PageDown on the keypad
KP_Prior	81	65434	PageUp on the keypad
KP_Right	85	65432	→ on the keypad
KP_Subtract	82	65453	- on the keypad
KP_Up	80	65431	↑ on the keypad
Next	105	65366	PageDown
Num_Lock	77	65407	NumLock
Pause	110	65299	pause
Print	111	65377	PrintScrn
Prior	99	65365	PageUp
Return	36	65293	The enter key (control-M). The name Enter refers to a mouse-related event, not a keypress; see Section 54, “Events”
Right	102	65363	→
Scroll_Lock	78	65300	ScrollLock
Shift_L	50	65505	The left-hand shift key
Shift_R	62	65506	The right-hand shift key
Tab	23	65289	The tab key
Up	98	65362	↑

### 事件句柄

The sections above tell you how to describe what events you want to handle, and how to bind them. Now let us turn to the writing of the handler that will be called when the event actually happens.

The handler will be passed an Event object that describes what happened. The handler can be either a function or a method. Here is the calling sequence for a regular function:

def handlerName(event):
And as a method:

    def handlerName(self, event):
The attributes of the Event object passed to the handler are described below. Some of these attributes are always set, but some are set only for certain types of events.

.char	If the event was related to a KeyPress or KeyRelease for a key that produces a regular ASCII character, this string will be set to that character. (For special keys like delete, see the .keysym attribute, below.)
.delta	For MouseWheel events, this attribute contains an integer whose sign is positive to scroll up, negative to scroll down. Under Windows, this value will be a multiple of 120; for example, 120 means scroll up one step, and -240 means scroll down two steps. Under MacOS, it will be a multiple of 1, so 1 means scroll up one step, and -2 means scroll down two steps. For Linux mouse wheel support, see the note on the Button event binding in Section 54.3, “Event types”.
.height	If the event was a Configure, this attribute is set to the widget's new height in pixels.
.keycode	For KeyPress or KeyRelease events, this attribute is set to a numeric code that identifies the key. However, it does not identify which of the characters on that key were produced, so that “x” and “X” have the same .keyCode value. For the possible values of this field, see Section 54.5, “Key names”.
.keysym	For KeyPress or KeyRelease events involving a special key, this attribute is set to the key's string name, e.g., 'Prior' for the PageUp key. See Section 54.5, “Key names” for a complete list of .keysym names.
.keysym_num	For KeyPress or KeyRelease events, this is set to a numeric version of the .keysym field. For regular keys that produce a single character, this field is set to the integer value of the key's ASCII code. For special keys, refer to Section 54.5, “Key names”.
.num	If the event was related to a mouse button, this attribute is set to the button number (1, 2, or 3). For mouse wheel support under Linux, bind Button-4 and Button-5 events; when the mouse wheel is scrolled up, this field will be 4, or 5 when scrolled down.
.serial	An integer serial number that is incremented every time the server processes a client request. You can use .serial values to find the exact time sequence of events: those with lower values happened sooner.
.state	
An integer describing the state of all the modifier keys. See the table of modifier masks below for the interpretation of this value.

.time	This attribute is set to an integer which has no absolute meaning, but is incremented every millisecond. This allows your application to determine, for example, the length of time between two mouse clicks.
.type	A numeric code describing the type of event. For the interpretation of this code, see Section 54.3, “Event types”.
.widget	Always set to the widget that caused the event. For example, if the event was a mouse click that happened on a canvas, this attribute will be the actual Canvas widget.
.width	If the event was a Configure, this attribute is set to the widget's new width in pixels.
.x	The x coordinate of the mouse at the time of the event, relative to the upper left corner of the widget.
.y	The y coordinate of the mouse at the time of the event, relative to the upper left corner of the widget.
.x_root	The x coordinate of the mouse at the time of the event, relative to the upper left corner of the screen.
.y_root	The y coordinate of the mouse at the time of the event, relative to the upper left corner of the screen.
Use these masks to test the bits of the .state value to see what modifier keys and buttons were pressed during the event:

Mask	Modifier
0x0001	Shift.
0x0002	Caps Lock.
0x0004	Control.
0x0008	Left-hand Alt.
0x0010	Num Lock.
0x0080	Right-hand Alt.
0x0100	Mouse button 1.
0x0200	Mouse button 2.
0x0400	Mouse button 3.
Here's an example of an event handler. Under Section 54.1, “Levels of binding”, above, there is an example showing how to bind mouse button 2 clicks on a canvas named self.canv to a handler called self.__drawOrangeBlob(). Here is that handler:

    def __drawOrangeBlob(self, event):
        '''Draws an orange blob in self.canv where the mouse is.
        '''
        r = 5   # Blob radius
        self.canv.create_oval(event.x-r, event.y-r,
            event.x+r, event.y+r, fill='orange')
When this handler is called, the current mouse position is (event.x, event.y). The .create_oval() method draws a circle whose bounding box is square and centered on that position and has sides of length 2*r.

### 外加变量小技巧

Sometimes you would like to pass other arguments to a handler besides the event.

Here is an example. Suppose your application has an array of ten checkbuttons whose widgets are stored in a list self.cbList, indexed by the checkbutton number in range(10).

Suppose further that you want to write one handler named .__cbHandler for <Button-1> events in all ten of these checkbuttons. The handler can get the actual Checkbutton widget that triggered it by referring to the .widget attribute of the Event object that gets passed in, but how does it find out that checkbutton's index in self.cbList?

It would be nice to write our handler with an extra argument for the checkbutton number, something like this:

    def __cbHandler(self, event, cbNumber):
But event handlers are passed only one argument, the event. So we can't use the function above because of a mismatch in the number of arguments.

Fortunately, Python's ability to provide default values for function arguments gives us a way out. Have a look at this code:

    def __createWidgets(self):
        …
        self.cbList = []    # Create the checkbutton list
        for i in range(10):
            cb = tk.Checkbutton(self, …)
            self.cbList.append(cb)
            cb.grid( row=1, column=i)
            def handler(event, self=self, i=i):   1
                return self.__cbHandler(event, i)
            cb.bind('<Button-1>', handler)
        …
    def __cbHandler(self, event, cbNumber):
        …
1	These lines define a new function handler that expects three arguments. The first argument is the Event object passed to all event handlers, and the second and third arguments will be set to their default values—the extra arguments we need to pass it.
This technique can be extended to supply any number of additional arguments to handlers.

### 虚拟事件

You can create your own new kinds of events called virtual events. You can give them any name you want so long as it is enclosed in double pairs of <<…>>.

For example, suppose you want to create a new event called <<panic>>, that is triggered either by mouse button 3 or by the pause key. To create this event, call this method on any widget w:

    w.event_add('<<panic>>', '<Button-3>',
                  '<KeyPress-Pause>')
You can then use '<<panic>>' in any event sequence. For example, if you use this call:

    w.bind('<<panic>>', h)
any mouse button 3 or pause keypress in widget w will trigger the handler h.

See .event_add(), .event_delete(), and .event_info() under Section 26, “Universal widget methods” for more information about creating and managing virtual events.