import usb_hid 
import supervisor

# this to disable autoreload when you upload code in storage
supervisor.disable_autoreload()
usb_hid.enable(usb_hid.Device.MOUSE)




