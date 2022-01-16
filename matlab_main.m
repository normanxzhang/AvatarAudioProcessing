function a = matlab_main()
    a = 69;
    
   
    fprintf("hello world\n");
    VAD = voiceActivityDetector;
    
    
    framelength = 1024;
    devices = getAudioDevices(audioDeviceReader);
    
    %Create objects for audion input
    micReader = audioDeviceReader('SamplesPerFrame', framelength, 'Device', devices{3});
    spectAnalyzer = dsp.SpectrumAnalyzer;
    %fileWriter = dsp.AudioFileWriter('SampleRate', micReader.SampleRate)
    
    %Create object for audio processing
    lms = dsp.LMSFilter;
    
    %Audio stream loop
    tic;
    while(toc < inf)
        audio = micReader();
                spectAnalyzer(audio);
        %perform audio proccessing here
        %lms(audio, double);
        
        [probability,noiseEstimate] = VAD(audio);
        disp(probability);
    end
    
    release(micReader)
    %release(fileWriter)
end
