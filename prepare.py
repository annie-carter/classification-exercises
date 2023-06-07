mport pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


# ---- IRIS-----

def prep_iris(df):
    # Drop unnecessary columns
    df = df.drop(['species_id', 'measurement_id'], axis=1)
    
    # Rename the species_name column
    df = df.rename(columns={'species_name': 'species'})
    
   # Create dummy variables for species
    dumb_species = pd.get_dummies(df['species'], prefix='species')

# Concatenate the dummy variables onto the iris DataFrame
    df = pd.concat([df, dumb_species], axis=1)
    return df

def my_train_test_split(df, target = None):
    if target:
        train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[target])
        train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train[target])
    else:
        train, test = train_test_split(df, test_size=.2, random_state=123)
        train, validate = train_test_split(train, test_size=.25, random_state=123)
    return train, validate, test

target = 'species_name'
train_iris, validate_iris, test_iris = my_train_test_split(iris, target)

# --------TITANIC  --------

def prep_titanic(titanic):
    titanic = titanic.drop(columns=['Unnamed: 0', 'embarked','class', 'age','deck'])
    dumb_ship = pd.get_dummies(data=titanic[['sex','embark_town']], drop_first=True)
    titanic = pd.concat([titanic, dumb_ship], axis=1)
    
    return titanic

target = 'survived'
train_titanic, validate_titanic, test_titanic = my_train_test_split(titanic, target)

#----- TELCO ---------

def prep_telco(telco):
    telco = telco.drop(columns=['internet_service_type_id', 'contract_type_id', 'payment_type_id'])

    telco['gender_encoded'] = telco.gender.map({'Female': 1, 'Male': 0})
    telco['partner_encoded'] = telco.partner.map({'Yes': 1, 'No': 0})
    telco['dependents_encoded'] = telco.dependents.map({'Yes': 1, 'No': 0})
    telco['phone_service_encoded'] = telco.phone_service.map({'Yes': 1, 'No': 0})
    telco['paperless_billing_encoded'] = telco.paperless_billing.map({'Yes': 1, 'No': 0})
    telco['churn_encoded'] = telco.churn.map({'Yes': 1, 'No': 0})
    
    dummy_df = pd.get_dummies(telco[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type'
                            ]],
                              drop_first=True)
    telco = pd.concat( [telco, dummy_df], axis=1 )
    
    return telco
target = 'churn'
train_telco, validate_telco, test_telco = my_train_test_split(telco, target)