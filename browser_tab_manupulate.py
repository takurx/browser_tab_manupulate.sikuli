import sys

def previous_tab():
    #前のタブへ
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    type(Key.TAB)
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)

def next_tab():
    #次のタブへ
    keyDown(Key.CTRL)
    type(Key.TAB)
    keyUp(Key.CTRL)



sleep(3)

for i in range(0, 5):
    previous_tab()
    sleep(1)
    #rightClick(Pattern("1536713727981.png").targetOffset(14,-19))
    rightClick(Pattern("1537606554951.png").targetOffset(-6,-67))
    sleep(1)
    #click("1536713781636.png")
    click("1537606634066.png")
    sleep(1)
    keyDown(Key.CTRL)
    type("w")
    keyUp(Key.CTRL)
    sleep(1)   
    # next_tab()
    keyDown(Key.CTRL)
    type("v")
    keyUp(Key.CTRL)
    sleep(1)
    type(Key.ENTER)
    sleep(1) 
    type(Key.ENTER)
    sleep(1)
