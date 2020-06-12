import bimpy
import time
import random
from win32api import GetKeyState
import win32api
from pynput.mouse import Button, Controller

ctx = bimpy.Context();
MinCPS = bimpy.Float(8.5);
MaxCPS = bimpy.Float(10.9);
OnlyOneHeader = bimpy.Bool(True)
Toggle = 0;
mouseclick = Controller()
MinDelay = 1000;
MaxDelay = 1000;
BaseDelay = 1000;

BarColor = bimpy.Vec4(0.16078431,0.2901960,0.47843137,0.95);
HeaderColor = bimpy.Vec4(0.25882352,0.58823529,0.9803921568,0.95);
HeaderHoverColor = bimpy.Vec4(0.43529411,0.694117647,0.9803921568,0.95);
TextColor = bimpy.Vec4(1,1,1,1);
SliderColor = bimpy.Vec4(0.06078431,0.1901960,0.47843137,0.95);
SliderActiveColor = bimpy.Vec4(0.16078431,0.2901960,0.47843137,0.95);
CheckMarkColor = bimpy.Vec4(0.43529411,0.694117647,0.9803921568,0.95);

ctx.init(520, 320, "")
print("Loading...")
while(not ctx.should_close()):
    ctx.new_frame()

    if True:
        if bimpy.begin("", flags=(bimpy.WindowFlags.NoSavedSettings | bimpy.WindowFlags.NoMove | bimpy.WindowFlags.NoResize)): 
            bimpy.text("NeX")
            bimpy.push_style_var(bimpy.Style.Alpha, 255)
            bimpy.set_window_size("",bimpy.Vec2(450,250))
            bimpy.text("")
            #bimpy.set_style(bimpy.GuiStyle.alpha)
            if MinCPS.value > MaxCPS.value:
                		MinCPS = bimpy.Float(MaxCPS.value);
            if bimpy.collapsing_header("AutoClicker"):
            		bimpy.slider_float("CPS Min", MinCPS, 5.0, 25.0)
            		bimpy.slider_float("CPS Max", MaxCPS, 5.0, 25.0)
            		if bimpy.button("Toggle"):
                			Toggle = not Toggle
            if bimpy.collapsing_header("Colors"):
            		bimpy.color_edit("Main Bar",BarColor)
            		bimpy.color_edit("Headers",HeaderColor)
            		bimpy.color_edit("Hovered Header",HeaderHoverColor)
            		bimpy.color_edit("Text",TextColor)
            		bimpy.color_edit("Slider Thumbs",SliderColor)
            		bimpy.color_edit("Activated Thumbs",SliderActiveColor)
            		bimpy.color_edit("CheckBox Marks",CheckMarkColor)
            		bimpy.push_style_color(bimpy.Colors.TitleBgActive,BarColor)
            		bimpy.push_style_color(bimpy.Colors.Header,HeaderColor)
            		bimpy.push_style_color(bimpy.Colors.HeaderHovered,HeaderHoverColor)
            		bimpy.push_style_color(bimpy.Colors.Text,TextColor)
            		bimpy.push_style_color(bimpy.Colors.SliderGrab,SliderColor)
            		bimpy.push_style_color(bimpy.Colors.SliderGrabActive,SliderActiveColor)
            		bimpy.push_style_color(bimpy.Colors.CheckMark,CheckMarkColor)
            if bimpy.collapsing_header("Options"):
            		if bimpy.checkbox("Option 1",OnlyOneHeader):
            				if OnlyOneHeader.value:
            					print("option 1 toggled")
            if bimpy.collapsing_header("Delete"):
            	bimpy.text("This button will delete all traces of this software.")
            	bimpy.text("")
            	if bimpy.button("Destruct"):
            		print("destructed")
        bimpy.end()
        special_keys = [0x06]
        for i in range(1, 256):
        		if win32api.GetAsyncKeyState(i):
            			if i in special_keys:
                				if Toggle == True:
                						mouseclick.click(Button.left, 1)
                						BaseDelay == 1000
                						MinDelay = BaseDelay / MinCPS.value
                						MaxDelay = BaseDelay / MaxCPS.value
                						ClickDelay = random.uniform(MinDelay, MaxDelay)
                						time.sleep(ClickDelay / 1000)
    ctx.render()
