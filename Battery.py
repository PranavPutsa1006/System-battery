import psutil


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return hh, mm, ss


def battery_check():
    # gives the current battery and charging status of the system
    battery = psutil.sensors_battery()
    h, m, s = secs2hours(battery.secsleft)
    if battery.power_plugged:
        if battery.percent != 100:
            chrg_stat = "charging"
        else:
            chrg_stat = "Fully charged"
        desc = "."
    else:
        if battery.percent >= 30:
            chrg_stat = "discharging"
        else:
            chrg_stat = "running on backup power, connect to a power source"
        desc = ". Should last for " + str(h) + " hours " + str(m) + " minutes"
    print("Power at " + str(battery.percent) + "% and " + chrg_stat + desc)


battery_check()
