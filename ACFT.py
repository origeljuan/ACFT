"""
ACFT Calculator Project
by Juan Origel
"""
from time import strptime
import string, json

with open("ACFTtime.json", "r") as acft_table:
    acft_data = json.load(acft_table)

def main():
    #Functions to enter variables
    mos = function_mos(input("Please enter MOS: "))
    dl = function_dl(input("Please enter weight used in Deadlift: "))
    spt = function_spt(input("Please enter distance obtained in Standing Power Throw: "))
    hrp = function_hrp(input(str("Please enter amount of Hand Release Push-ups: ")))
    sdc = function_sdc(input(str("Please enter time for Sprint Drag Carry in (M:S) format: ")))
    ltk = function_ltk(input("Please enter amount of Leg Tucks: "))
    tmr = function_tmr(input(str("Please enter time for 2 Mile Run in (M:S) format: ")))
    #functions to Calculate points
    dlpts = pass_fail_dl(mos[0], dl)
    spts = pass_fail_spt(mos[0], spt)
    hrpts = pass_fail_hrp(mos[0], hrp)
    sdcpts = pass_fail_sdc(mos[0], sdc)
    ltkpts = pass_fail_ltk(mos[0], ltk)
    tmrpts = pass_fail_tmr(mos[0], tmr)
    standard = function_color(mos[0])
    #Print Results
    dash = "-" * 80
    print(dash)
    print(f"{mos[1]} is part of the {standard} and you need {mos[0]} points in each event to Pass!")
    print(dash)
    print("{:^72}".format("Points Obtained"))
    print(dash)
    print("{:^17}{:^30s}{:^25s}".format("Deadlift ", "Standing-Power-Throw", "Hand-Release-Push-Up"))
    print("{:^17}{:^30s}{:^25s}".format(str(dl) + " " + str(dlpts), str(spt) + " " + str(spts), str(hrp) + " " + str(hrpts)))
    print(dash)
    print("{:^17}{:^30}{:^25}".format("Sprint Drag Carry", "LegTuck", "2 Mile Run"))
    print("{:^17}{:^30}{:^25}".format(str(sdc) + " " + str(sdcpts), str(ltk) + " " + str(ltkpts), str(tmr) + " " + str(tmrpts)))
    print(dash)
    pass_fail = (str(dlpts) + " " + str(spts) + " " + str(hrpts) + " " + str(sdcpts) + " " + str(ltkpts) + " " + str(tmrpts))
    if "Failed" in pass_fail:
        print("{:^72}".format("ACFT FAILED"))
    else:
        print("{:^72}".format("ACFT PASSED"))

#Functions to Calculate the MOS and which Standard they fall under
def function_mos(mos):
    if mos == "": #If MOS is empty, request MOS again
        mos = function_mos(input("Blank Input, Please enter MOS: "))
        return mos
    mos_str = str(mos).upper()
    mos = str(mos).upper()
    if mos_str not in acft_data["MOS"]: #if MOS entered is not in MOS list, ask again.
        mos = function_mos(input("MOS not found, Please enter MOS: "))
        return mos
    if mos_str in acft_data["MOS"]:
        return acft_data["MOS"][mos], mos_str

def function_color(mos):
    color = mos
    if color == 60:
        return "Gold Standard"
    if color == 65:
        return "Grey Standard"
    if color == 70:
        return "Black Standard"

#Functions to calculate Dead Lift score
def function_dl(dl):
    if dl == "":
        dl = function_dl(input("Blank Input, Please enter weight used in Deadlift: "))
        return dl
    if dl in acft_data["DL"]:
        if int(dl) > 340:
            return 100
        if int(dl) <= 80:
            return 0
        if int(dl) in range(90,350,10):
            return acft_data["DL"][str(dl)]
    # dl_pts = acft_data["DL"][str(dl)]
    else:
        dl = function_dl(input("Invalid weight, Please enter correct weight used in Deadlift: "))
        return dl

def pass_fail_dl(mos, dl):
    if dl >= mos:
        return "Pass"
    if dl <= mos:
        return "Failed"

#Functions to calculate Standing Power Throw
def function_spt(spt):
    if spt == "":
        spt = function_spt(input("Please enter distance obtained in Standing Power Throw: "))
        return spt
    if spt.isalpha():
        spt = function_spt(input("Please enter distance obtained in Standing Power Throw: "))
        return spt
    if spt not in acft_data["SPT"]:
        spt_pts = (spt_round(spt)[0])
        if float(spt) >= 12.5:
            return acft_data["SPT"][str(float(12.5))]
        if float(spt) <= 3.3:
            return acft_data["SPT"][str(float(3.3))]
        else:
            return acft_data["SPT"][str(spt_pts)]
    return

def pass_fail_spt(mos, spt):
    if spt >= mos:
        return "Pass"
    if spt <= mos:
        return "Failed"

#These functions rounds the floating number to the closest one on the list
def spt_round(spt):
    d = acft_data["SPT"]
    dlist = spt_keylist(d)
    flist = []
    for items in dlist:
        flist.append(float(items))
    diff = lambda list_value: abs(list_value - float(spt))
    closest = min(flist, key=diff)
    spt_pts = (acft_data["SPT"][str(closest)])
    spt = closest
    return spt, spt_pts

def spt_keylist(d):
    key_list = []
    for key in d.keys():
        key_list.append(key)
    return key_list

#These functions calculate the Hand Release Push up score

def function_hrp(hrp):
    if hrp == "":
        hrp = function_hrp(input(str("Please enter amount of Hand Release Push-ups: ")))
        return hrp
    if hrp.isalpha():
        hrp = function_hrp(input(str("Please enter amount of Hand Release Push-ups: ")))
        return hrp
    if int(hrp) >= 60:
        return acft_data["HRP"][str((60))]
    if int(hrp) <= 0:
        return acft_data["HRP"][str((0))]
    if int(hrp) > 0 and int(hrp) < 60:
        return acft_data["HRP"][str((hrp))]

def pass_fail_hrp(mos, hrp):
    if hrp >= mos:
        return "Pass"
    if hrp <= mos:
        return "Failed"

def function_sdc(sdc):
    if sdc == "":
        sdc = function_sdc(input(str("Blank Entry, Please enter time for Sprint Drag Carry in (M:S) format: ")))
        return sdc
    if sdc.isalpha():
        sdc = function_sdc(input(str("Blank Entry, Please enter time for Sprint Drag Carry in (M:S) format: ")))
        return sdc
    if str(sdc) in acft_data["SDC"]:
        return acft_data["SDC"][str(sdc)]
    elif time_format(sdc):
        minutes, seconds = sdc.split(":")
        minutes = int(minutes)
        seconds = int(seconds)
        if minutes == 1 and seconds < 34:
            return 100
        if minutes == 3 and seconds > 34:
            return 0
    else:
        sdc = function_sdc(input(str("Please enter time for Sprint Drag Carry in (M:S) format: ")))
def time_format(sdc):
    try:
        strptime(str(sdc), '%H:%M')
        return True
    except ValueError:
        return False

def pass_fail_sdc(mos, sdc):
    if sdc >= mos:
        return "Pass"
    if sdc <= mos:
        return "Failed"

#Functions for the leg tuck

def function_ltk(ltk):
    if ltk == "":
        ltk = function_ltk(input("Please enter amount of Leg Tucks: "))
        return ltk
    if ltk.isalpha():
        ltk = function_ltk(input("Please enter amount of Leg Tucks: "))
        return ltk
    if int(ltk) >= 20:
        return acft_data["LTK"][str(20)]
    if int(ltk) <= 0:
        return acft_data["LTK"][str(0)]
    if int(ltk) > 0 and int(ltk) <= 20:
        return acft_data["LTK"][str((ltk))]

def pass_fail_ltk(mos, ltk):
    if ltk >= mos:
        return "Pass"
    if ltk <= mos:
        return "Failed"

#These are functions to calculate 2MR points

def function_tmr(tmr):
    if tmr == "":
        tmr = function_tmr(input(str("Please enter time for 2 Mile Run in (M:S) format: ")))
        return tmr
    if tmr.isalpha():
        tmr = function_tmr(input(str("Please enter time for 2 Mile Run in (M:S) format: ")))
        return tmr
    tmr = convert_tmr(tmr)
    if str(tmr) in acft_data["2MileRun"]:
        return acft_data["2MileRun"][str(tmr)]
    elif int(tmr) < 810:
        return 100
    elif int(tmr) > 1368:
        return 0
    else:
        return round_2mr(tmr)

def time_format(tmr):
    try:
        strptime(str(tmr), '%H:%M')
        return True
    except ValueError:
        return False

def round_2mr(tmr):
    d = acft_data["2MileRun"]
    dlist = tmr_keylist(d)
    flist = []
    for items in dlist:
        flist.append(int(items))
    diff = lambda list_value: abs(list_value - int(tmr))
    closest = min(flist, key=diff)
    tmr_pts = (acft_data["2MileRun"][str(closest)])
    tmr = closest
    return tmr_pts

def tmr_keylist(d):
    key_list = []
    for key in d.keys():
        key_list.append(key)
    return key_list


def pass_fail_tmr(mos, tmr):
    if tmr >= mos:
        return "Pass"
    if tmr <= mos:
        return "Failed"

def convert_tmr(tmr):
    minutes, seconds = tmr.split(":")
    minutes = int(minutes)
    seconds = int(seconds)
    tis = (minutes * 60) + (seconds)
    return tis

if __name__ == "__main__":
    main()
