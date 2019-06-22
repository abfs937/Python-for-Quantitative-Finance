import pandas as pd

#-----------------
# QUESTION 2A
#-----------------
def get_dataframe(file_name):
    # Code for question 2a goes here
    # Read the xlsx file and return a pandas DataFrame

    df = pd.read_excel(file_name)
    return df


def validate_df(df, ccy_list):
    # Code for question 2a goes here
    df2 = pd.read_csv('parties.csv')
    clean_df = df[df[['l1_ccy', 'l2_ccy']].isin(ccy_list).all(axis=1)]
    LEGAL_ENTITY_NAME = df2['LEGAL_ENTITY_NAME']
    clean_df = clean_df[clean_df[['entity', 'counter_party']].isin(list(LEGAL_ENTITY_NAME)).all(axis=1)]
    clean_df = clean_df[(clean_df['l1_notional'] > 0) & (clean_df['l2_notional'] > 0)]
    clean_df = clean_df.merge(df2, left_on=['entity', 'lei'], right_on=['LEGAL_ENTITY_NAME', 'LEI'], how='inner')
    error_df = df[~df[['Trade_id']].isin(list(clean_df['Trade_id'])).all(axis=1)]
    clean_df = clean_df[['entity', 'lei', 'Trade_id', 'counter_party', 'cp_lei', 'l1_notional', 'l1_ccy', 'l2_notional', 'l2_ccy']]

    return clean_df, error_df
    
#-----------------
# QUESTION 2B
#-----------------
def generate_match_df(clean_dfs):
    dfA = pd.DataFrame(clean_dfs[0])
    dfB = pd.DataFrame(clean_dfs[1])
    match_df = pd.concat([dfA, dfB], join='inner').sort_values(by=['Trade_id'])
    match_df = match_df.drop(columns=['lei', 'cp_lei'])
    match_df_2 = match_df.copy()
    match_df['ccy_pair'] = match_df['l1_ccy'] + match_df['l2_ccy']

    match_df = match_df.merge(match_df_2, left_on=['entity', 'counter_party', 'l1_notional', 'l2_notional'],
                              right_on=['counter_party', 'entity', 'l2_notional', 'l1_notional'], how='left',
                              indicator=True)
    match_df = match_df.drop(columns=['entity_y', 'Trade_id_y', 'counter_party_y', 'l1_ccy_y', 'l2_ccy_y'])
    match_df = match_df[
        ['entity_x', 'Trade_id_x', 'counter_party_x', 'l1_notional_x', 'l2_notional_y', 'l1_ccy_x', 'l2_notional_x',
         'l1_notional_y', 'l2_ccy_x', 'ccy_pair', '_merge']]
    match_df.columns = ['party', 'trade_id', 'cp', 'l1_notional', 'cp_l1_notional', 'l1_ccy', 'l2_notional',
                        'cp_l2_notional', 'l2_ccy', 'ccy_pair', 'match_status']
    match_df = match_df.replace(['both', 'left_only'], ['Matched', 'Not matched - Notional Mismatch'])
    vc = match_df.trade_id.value_counts() == 1
    vc = vc[vc == 1].index.tolist()
    for i in vc:
        match_df.loc[match_df.trade_id == i, 'match_status'] = 'Not Matched - One Side'
    return match_df
    
#-----------------
# QUESTION 2C
#-----------------
def save_matched_df(matched_df):
    matched_df.to_excel('matched_df.xlsx', index=False)
    pass

# -------------------------------------------
# Main
# -------------------------------------------
if __name__ == '__main__':
    ccy_list = ['USD', 'EUR']
    file_names = ['TradeDetailsBankA.xlsx', 'TradeDetailsBankB.xlsx']
    clean_dfs = []
    
    # QUESTION 2A 
    for file_name in file_names:
        df = get_dataframe(file_name)
        clean_df, error_df = validate_df(df, ccy_list)
        print(clean_df)
        print(error_df)
        clean_dfs.append(clean_df)

# QUESTION 2B
    matched_df = generate_match_df(clean_dfs)

# QUESTION 2C
    save_matched_df(matched_df)
