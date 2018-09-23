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


sleep_time = 2

sleep(5)

for i in range(0, 10):
    previous_tab()
    sleep(sleep_time)
    #rightClick(Pattern("1536713727981.png").targetOffset(14,-19))
    #rightClick(Pattern("1537606554951.png").targetOffset(-6,-67))
    rightClick(Pattern("1537680653361.png").similar(0.81).targetOffset(0,900))
    sleep(sleep_time)
    #click("1536713781636.png")
    #click("1537606634066.png")
    click("1537680825504.png")
    sleep(sleep_time)
    #keyDown(Key.CTRL)
    keyDown(Key.CMD)
    type("w")
    #keyUp(Key.CTRL)
    keyUp(Key.CMD)
    sleep(5)   
    # next_tab()
    #keyDown(Key.CTRL)
    keyDown(Key.CMD)
    type("v")
    #keyUp(Key.CTRL)
    keyUp(Key.CMD)
    #sleep(sleep_time)
    type(Key.ENTER)
    #sleep(sleep_time) 
    type(Key.ENTER)
    sleep(sleep_time)
