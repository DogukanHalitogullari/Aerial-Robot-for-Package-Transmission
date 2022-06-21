def close_hands():
    flag_while = False
    flag_p = False
    flag_p2 = False
    cycle_step = 0.1
    p_open_cycle = 10
    p2_open_cycle = 6.5
    while not flag_while:
        buttonState = GPIO.input(buttonPIN)
        if buttonState == GPIO.LOW:
            flag_p = True
        
        buttonState2 = GPIO.input(buttonPIN2)
        if buttonState2 == GPIO.LOW:
            flag_p2 = True
        
        if not flag_p:
            p_open_cycle -= cycle_step
            p.ChangeDutyCycle(p_open_cycle)
        
        if not flag_p2:
            p2_open_cycle -= cycle_step
            p2.ChangeDutyCycle(p2_open_cycle)
          
        if flag_p and flag_p2:
            flag_while = True
        elif p_open_cycle < 8.3 and p2_open_cycle <4.5:
            flag_while = True
        time.sleep(0.05)
