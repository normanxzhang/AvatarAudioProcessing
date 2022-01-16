function a = matlab_main()
   % a = getInputDevices()
    a =2
    getInputDevices()
end

function devices = getInputDevices()
    deviceReader = audioDeviceReader;
    devices = getAudioDevices(deviceReader);
    
end

