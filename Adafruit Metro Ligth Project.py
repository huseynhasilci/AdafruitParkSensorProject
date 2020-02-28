import time
import board
import adafruit_hcsr04
import digitalio

class ParkSensor:
    def __init__(self):
        self.green_led = digitalio.DigitalInOut(board.D7)
        self.yellow_led = digitalio.DigitalInOut(board.D8)
        self.red_led = digitalio.DigitalInOut(board.D9)
        self.buzzer = digitalio.DigitalInOut(board.D11)
        self.sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D2)
        self.green_led.direction = digitalio.Direction.OUTPUT
        self.yellow_led.direction = digitalio.Direction.OUTPUT
        self.red_led.direction = digitalio.Direction.OUTPUT
        self.buzzer.direction = digitalio.Direction.OUTPUT
        self.red_led.value = True
        time.sleep(0.5)
        self.red_led.value = False
        self.yellow_led.value = True
        time.sleep(0.5)
        self.yellow_led.value = False
        self.green_led.value = True
        time.sleep(0.5)
        self.green_led.value = False
        self.buzzer.value = True
        time.sleep(0.5)
        self.buzzer.value = False
        print("Obstacle Detecter Decive is Working")
        self.lets_start()
    def get_distance(self):
        return self.sonar.distance
    def ligth_red_led(self):
        self.red_led.value = True
        time.sleep(1)
        self.red_led.value = False
    def ligth_yellow_led(self):
        self.yellow_led.value = True
        time.sleep(1)
        self.yellow_led.value = False
    def ligth_green_led(self):
        self.green_led = True
        time.sleep(1)
        self.green_led.value = False
    def activate_buzzer(self):
        self.buzzer.value = True
        time.sleep(1)
        self.buzzer.value = False
    def lets_start(self):
        while True:
    try:
        if(120<int(self.get_distance())<=200):
            self.ligth_green_led()
            print("You are safe.")
        elif(50<int(self.get_distance())<=120):
            self.ligth_yellow_led()
            print("Slow down your speed")
        elif(25<int(self.get_distance())<=50):
            self.ligth_red_led()
            print("DANGER TOO CLOSE")
        elif(int(self.get_distance())<=25):
            self.ligth_red_led()
            self.active_buzzer()
            print("The device stopped! calling the emergency services.")
            break
        else:
            self.ligth_green_led()
            self.ligth_yellow_led()

    except:
        print("Distance Error!")

park_sensor_object = ParkSensor()
