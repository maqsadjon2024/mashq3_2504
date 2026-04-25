class AgeCheck:
    def __init__(self, age):
        self.age = age

    def check(self):
        if self.age >= 18:
            print(f"{self.age} Voyaga yetgan")
        else:
            print(f"{self.age} Voyaga yetmagan")

x = AgeCheck(12)
x.check()



# Bir nechta metod

# 21 - misol
class MusicPlayer:
    def __init__(self, song):
        self.song = song

    def play(self):
        print(f"{self.song} chalinyapti")

    def stop(self):
        print("To‘xtatildi")


player = MusicPlayer("Song.mp3")

player.play()
player.stop()


# 22 - misol
class Fan:
    def __init__(self, speed):
        self.speed = speed

    def increase(self):
        print(f"{self.speed} Tezlik oshdi")

    def decrease(self):
        print(f"Tezlik kamaydi")

x = Fan(120)
x.increase()
x.decrease()


# 23 - misol
class TV:
    def __init__(self, channel):
        self.channel = channel
    def next_channel(self):
        print(f"{self.channel} Keyingi kanal")

    def prev_channel(self):
        print("Oldingi kanal")

a = TV(12)
a.next_channel()
a.prev_channel()
