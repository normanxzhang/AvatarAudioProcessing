import matlab.engine


if __name__ == '__main__':

    eng = matlab.engine.start_matlab()

    
    a = eng.matlab_main()
    print(a)
    
    eng.quit()