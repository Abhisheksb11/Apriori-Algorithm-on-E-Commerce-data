import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
dataset=[['Bread','Milk','Beer'],
        ['Bread','Diapers','Eggs'],
        ['Milk','Diapers','Beer','Cola'],
        ['Bread','Milk','Diapers','Beer'],
        ['Bread','Milk','Cola']]
te=TransactionEncoder()
te=te.fit(dataset)
te_ary=te.transform(dataset)
df=pd.DataFrame(te_ary,columns=te.columns_)
market=set(te.columns_)
Freq_itenset=apriori(df,min_support=0.5,use_colnames=True)
from mlxtend.frequent_patterns import association_rules
rules=association_rules(Freq_itenset,metric='support',min_threshold=0.5)
rules[rules['support']==rules['support'].max()]

*******************************************************************************

print('------------------------------Cart Addition App------------------------------\nPRESS EXIT TO LEAVE')
print('Items which can be bought : %s\nEnter first item :'%(market))
i,item=1,''
cart=set()
sugg=set()
while i>0:
    item=input('Enter an item :')
    item=item[0].upper()+item[1:].lower()
    if item in cart:
        print('already in cart')
    elif item in market:
        item=set([item])
        cart|=item
        market-=item
        g=rules[rules['antecedants'].apply(lambda x:set(item).issubset(set(x)))]
        le=g['consequents'].index
        a=set()
        for o in le:
            t=set(list(g['consequents'][o]))
            a|=t
        a-=cart
        a-=item
        sugg=a
        print('***********************************************************************')
        print('Your cart is ', cart)
        print('***********************************************************************')
        print('Available suggestions : %s'%(sugg))
        print('Remaining items in store : %s'%(market))
        sugg=set()
        if len(market)==0:
            print('All items taken! Leaving......')
            print('***********************************************************************')
            print('Your final cart is : %s'%(cart))
            print('***********************************************************************')
            break
    elif item=='Exit':
        print('***********************************************************************')
        print('Your final cart is : %s'%(cart))
        print('***********************************************************************')
        break
    else:
        print('item not available')
    

        
