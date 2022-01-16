import matlab.engine


if __name__ == '__main__':

    eng = matlab.engine.start_matlab()

    
    a = eng.getInputDevices()
    print(a)

    eng.quit()