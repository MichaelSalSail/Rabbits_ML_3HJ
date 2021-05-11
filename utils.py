
def qa_tc_explore(df):
    '''
    Prints the percent of rows in a dataframe with missing and non-missing values in the
    'QA_TemporalCoverage' column
    
    Args:
        df: a datamframe possessing a 'QA_TemporalCoverage' column.
        
    Returns:
        None
    '''
    total_rows=0

    for i in range(0,4):
        for j in range(0,4):
            for k in range(0,4):
                temp=str(i+1)+'.'+str(j+1)+'.'+str(k+1)
                total_rows+=df[df['QA_TemporalCoverage']==temp].shape[0]
    print("The total rows is",total_rows)
    print("This is",(total_rows/(df.shape[0]))*100,"% of the abundance dataset.")
    print("The other",100-(total_rows/(df.shape[0]))*100,"% has a NaN in one or more sections.")
    

def QA_Slice(df,first,second,third):
    '''
    Creates a list of all quality scores better than or equal to the provided parameters and
    prints the percentage of dataframe rows containing the derived quality scores.
    
    Args:
        df: a dataframe possessing a 'QA_TemporalCoverage' column
        first: an int; frequency of visit
        second: an int; seasonal frequency
        thrid: an int; year(s) covered

    Returns:
        A list of ints; the amount of slices from abundance.
    '''
    
    total_rows=0
    QATC=[]
    for A in range(1,5):
        if(A>first):
            continue
        for B in range(1,5):
            if(B>second):
                continue
            for C in range(1,5):
                if(C>third):
                    continue
                temp=str(A)+'.'+str(B)+'.'+str(C)
                QATC.append(temp)
                total_rows+=df[df['QA_TemporalCoverage']==temp].shape[0]
    print("The total rows is",total_rows)
    print("This is",(total_rows/(df.shape[0]))*100,"% of the abundance dataset.")
    print("The other",100-(total_rows/(df.shape[0]))*100,"% of abundance was not included in this slice.")
    return QATC