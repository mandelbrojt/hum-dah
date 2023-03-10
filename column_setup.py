# Maps every column to their corresponding data type
col_to_dtypes = {
    "lei":"str",
    "state_code":"category",
    "county_code":"float32",
    "conforming_loan_limit":"category",
    "action_taken":"category",
    "purchaser_type":"category",
    "loan_type":"category",
    "loan_purpose":"category",
    "lien_status":"category",
    "loan_amount":"float32",
    "interest_rate":"float32",
    "rate_spread":"float32",
    "hoepa_status":"category",
    "total_loan_costs":"float32",
    "total_points_and_fees":"float32",
    "origination_charges":"float32",
    "discount_points":"float32",
    "lender_credits":"float32",
    "loan_term":"float32",
    "interest_only_payment":"category",
    "balloon_payment":"category",
    "property_value":"float32",
    "construction_method":"category",
    "occupancy_type":"category",
    "total_units":"category",
    "applicant_age":"category",
    "income":"float32",
    "applicant_credit_score_type":"category",
    "co-applicant_credit_score_type":"category",
    "applicant_ethnicity-1":"category",
    "co-applicant_ethnicity-1":"category",
    "applicant_race-1":"category",
    "co-applicant_race-1":"category",
    "applicant_sex":"category",
    "co-applicant_sex":"category",
    "co-applicant_sex_observed":"category",
    "co-applicant_age":"category",
    "aus-1":"category",
    "denial_reason-1":"category",
    "tract_population":"float32",
    "ffiec_msa_md_median_family_income":"float32"
}

# Selected column names
selected_cols = [col for col in col_to_dtypes.keys()]

# Maps every categorical column to their corresponding labels
cols_to_labels = {
    "conforming_loan_limit":{
        "C":"Conforming",
        "NC":"Nonconforming",
        "U":"Undetermined",
        "NA":"Not Applicable"
    },
    "action_taken":{
        1: "Loan originated",
        2: "Application approved but not accepted",
        3: "Application denied",
        4: "Application withdrawn by applicant",
        5: "File closed for incompleteness",
        6: "Purchased loan",
        7: "Preapproval request denied",
        8: "Preapproval request approved but not accepted"
    },
    "purchaser_type":{
        0:"Not applicable",
        1:"Fannie Mae",
        2:"Ginnie Mae",
        3:"Freddie Mac",
        4:"Farmer Mac",
        5:"Private securitizer",
        6:"Commercial bank, savings bank, or savings association",
        71:"Credit union, mortgage company, or finance company",
        72:"Life insurance company",
        8:"Affiliate institution",
        9:"Other type of purchaser"
    },
    "loan_type":{
        1:"Conventional",
        2:"FHA",
        3:"VA",
        4:"RHS or FSA"
    },
    "loan_purpose":{
        1:"Home purchase",
        2:"Home improvement",
        31:"Refinancing",
        32:"Cash-out refinancing",
        4:"Other purpose",
        5:"Not applicable"
    },
    "lien_status":{
        1:"Secured by a first lien",
        2:"Secured by a subordinate lien"
    },
    "hoepa_status":{
    1:"High-cost mortgage",
    2:"Not a high-cost mortgage",
    3:"Not applicable"
    },
    "interest_only_payment":{
    1:"Interest-only payments",
    2:"No interest-only payments",
    1111:"Exempt"
    },
    "balloon_payment":{
    1:"Balloon payment",
    2:"No balloon payment",
    1111:"Exempt"
    },
    "construction_method":{
    1:"Site-built",
    2:"Manufactured home"
    },
    "occupancy_type":{
    1:"Principal residence",
    2:"Second residence",
    3:"Investment property"
    },
    "applicant_credit_score_type":{
    1:"Equifax Beacon 5.0",
    2:"Experian Fair Isaac",
    3:"FICO Risk Score Classic 04",
    4:"FICO Risk Score Classic 98",
    5:"VantageScore 2.0",
    6:"VantageScore 3.0",
    7:"More than one credit scoring model",
    8:"Other credit scoring model",
    9:"Not applicable",
    1111:"Exempt"
    },
    "co-applicant_credit_score_type":{
    1:"Equifax Beacon 5.0",
    2:"Experian Fair Isaac",
    3:"FICO Risk Score Classic 04",
    4:"FICO Risk Score Classic 98",
    5:"VantageScore 2.0",
    6:"VantageScore 3.0",
    7:"More than one credit scoring model",
    8:"Other credit scoring model",
    9:"Not applicable",
    10:"No co-applicant",
    1111:"Exempt"
    },
    "applicant_ethnicity-1":{
    1:"Hispanic or Latino",
    11:"Mexican",
    12:"Puerto Rican",
    13:"Cuban",
    14:"Other Hispanic or Latino",
    2:"Not Hispanic or Latino",
    3:"Information not provided by applicant in mail, internet, or telephone application",
    4:"Not applicable"
    },
    "co-applicant_ethnicity-1":{
    1:"Hispanic or Latino",
    11:"Mexican",
    12:"Puerto Rican",
    13:"Cuban",
    14:"Other Hispanic or Latino",
    2:"Not Hispanic or Latino",
    3:"Information not provided by applicant in mail, internet, or telephone application",
    4:"Not applicable",
    5:"No co-applicant"
    },
    "applicant_race-1":{
    1:"American Indian or Alaska Native",
    2:"Asian",
    21:"Asian Indian",
    22:"Chinese",
    23:"Filipino",
    24:"Japanese",
    25:"Korean",
    26:"Vietnamese",
    27:"Other Asian",
    3:"Black or African American",
    4:"Native Hawaiian or Other Pacific Islander",
    41:"Native Hawaiian",
    42:"Guamanian or Chamorro",
    43:"Samoan",
    44:"Other Pacific Islander",
    5:"White",
    6:"Information not provided by applicant in mail, internet, or telephone application",
    7:"Not applicable"
    },
    "co-applicant_race-1":{
    1:"American Indian or Alaska Native",
    2:"Asian",
    21:"Asian Indian",
    22:"Chinese",
    23:"Filipino",
    24:"Japanese",
    25:"Korean",
    26:"Vietnamese",
    27:"Other Asian",
    3:"Black or African American",
    4:"Native Hawaiian or Other Pacific Islander",
    41:"Native Hawaiian",
    42:"Guamanian or Chamorro",
    43:"Samoan",
    44:"Other Pacific Islander",
    5:"White",
    6:"Information not provided by applicant in mail, internet, or telephone application",
    7:"Not applicable",
    8:"No co-applicant"
    },
    "applicant_sex":{
    1:"Male",
    2:"Female",
    3:"Information not provided by applicant in mail, internet, or telephone application",
    4:"Not applicable",
    6:"Applicant selected both male and female"
    },
    "co-applicant_sex":{
    1:"Male",
    2:"Female",
    3:"Information not provided by applicant in mail, internet, or telephone application",
    4:"Not applicable",
    5:"No co-applicant",
    6:"Co-applicant selected both male and female"
    },
    "aus-1":{
    1:"Desktop Underwriter (DU)",
    2:"Loan Prospector (LP) or Loan Product Advisor",
    3:"Technology Open to Approved Lenders (TOTAL) Scorecard",
    4:"Guaranteed Underwriting System (GUS)",
    5:"Other",
    6:"Not applicable",
    7:"Internal Proprietary System",
    1111:"Exempt"
    },
    "denial_reason-1":{
    1:"Debt-to-income ratio",
    2:"Employment history",
    3:"Credit history",
    4:"Collateral",
    5:"Insufficient cash (downpayment, closing costs)",
    6:"Unverifiable information",
    7:"Credit application incomplete",
    8:"Mortgage insurance denied",
    9:"Other",
    10:"Not applicable"
    }
}
