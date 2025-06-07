image blake_still_hide = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/blake/still_hide.png",
    "persistent.PC98_mode == True", "images/PC98/ch/blake/still_hide.png"
)