def combineColumns(refCol, compCol):
    '''
    This function takes two unequal sized columns from different 
    data frames with the same ID's and shows which values in the
    larger column (refCol) are missing from the smaller column (compCol) 
    by imputing the missing ID's with NaN ineffienctly. Returns
    the combined df and a df of the missing values from the compCol
    '''  
    new_dict = {'refCol': [],
                'compCol': []}
    for i in refCol:
        found = False
        for j in compCol:
            if i == j:
                new_dict['compCol'].append(j)
                found = True
        if not found:
            new_dict['compCol'].append(np.nan)
        new_dict['refCol'].append(i)

    df = pd.DataFrame(new_dict)
    df_missing = df.loc[df['compCol'] == np.nan]
    return df , df_missing
