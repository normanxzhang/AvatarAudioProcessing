import pyaudio
import audioop

class Audio:

    def __init__(self, chunck, format, channels, rate, seconds):
        self.chunck = chunck
        self.format = format
        self.channels = channels
        self.rate = rate
        self.seconds = seconds
        
        self.p = None
        self.stream = None
        self.taling = False

    def init(self):
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        inputDevices = -1
        for i in range(0, numdevices):
            if ((p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0):
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
                inputDevices = inputDevices + 1
        
        id = int(input("Enter Device ID: "))
        while(id < 0 or id > inputDevices):
            id = int(input("Invalid ID\nEnter Device ID: "))
        
        stream = p.open(
            format = self.format,
            channels = self.channels,
            rate = self.rate,
            input = True,
            output = False,
            input_device_index = id,
            frames_per_buffer = self.chunck
        )
        self.stream = stream
        self.p = p
        print("Audio Initialized")

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        print("Audio Closed")

    def listen(self):
        for i in range(0, int(self.rate / self.chunck*self.seconds)):
            data = self.stream.read(self.chunck)
            rms = audioop.rms(data, 2)
        if(rms > 425):
            print(rms,"talking")
            if(self.talking is False):
                self.talking = True

        else:
            self.talking = False