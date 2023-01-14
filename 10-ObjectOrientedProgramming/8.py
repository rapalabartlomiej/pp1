class TV:
    def __init__(self):
        self.is_on=False

    def turn_on(self):
        self.is_on = True
        self.channel_no = 1

    def turn_off(self):
        self.is_on = False
    
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self,channels_list):
        self.channels_list = channels_list

    def show_channels(self):
        print(self.channels_list) 




    def show_status(self):
        if self.is_on:
            print(f"tv is on chanell: {self.channel_no}")
        else:
            print("tv is off")
lg = TV()
lg.show_status()
lg.turn_on()
lg.show_status()
lg.set_channel(5)
lg.show_status()
lg.turn_off()
lg.show_status()
lg.set_channels(["TVP1","TVP2","Polsat","VN","Filmbox","Discovery"])
lg.show_channels()