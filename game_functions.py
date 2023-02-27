import pandas as pd
def dynamics_pandemics(cases):
    data = {'comp': ['er','hosp','icu'],
            'cases': [cases * 0.6,cases * 0.2,cases*0.2],
            'death': [cases * 0.6 * 0.8,cases * 0.2 * 0.6,cases * 0.2 * 0.8]}
    df = pd.DataFrame(data)
    return df

def hosp_dynamics(cases,er_res,beds_res,icu_res):
    data_input = {'comp': ['er','hosp','icu'],
                  'beds': [er_res,beds_res,icu_res]}
    df_input = pd.DataFrame(data_input)
    df = dynamics_pandemics(cases)
    df_res = (df['cases'] - df['death']) - df_input['beds']
    return df_res
