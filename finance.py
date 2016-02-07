

def future_value (pv, number_of_periods, interest_rate, payment = 0):
    simple_fv = pv*(1 + interest_rate)**number_of_periods
    pmt_fv = payment*(sum([(1+interest_rate)**i for i in range(0, number_of_periods)]))

    return simple_fv + pmt_fv

def payment (fv, number_of_periods, interest_rate, pv = 0):
    dividend = (fv - pv*(1+interest_rate)**number_of_periods)
    devisor = sum([(1+interest_rate)**i for i in range(0, number_of_periods)]) 

    return dividend / devisor

