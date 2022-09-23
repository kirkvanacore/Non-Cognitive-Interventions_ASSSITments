import pandas as pd

df_v1_13_14 = pd.read_csv("../Data/raw0.0/rds_dev_13_14_motivational_v1.csv")
df_v1_14_15 = pd.read_csv("../Data/raw0.0/rds_dev_14_15_motivational_v1.csv")
df_v1_15_16 = pd.read_csv("../Data/raw0.0/rds_dev_15_16_motivational_v1.csv")
df_v1_16_17 = pd.read_csv("../Data/raw0.0/rds_dev_16_17_motivational_v1.csv")
df_v1_17_18 = pd.read_csv("../Data/raw0.0/rds_dev_17_18_motivational_v1.csv")
df_v1_18_19 = pd.read_csv("../Data/raw0.0/rds_dev_18_19_motivational_v1.csv")
df_v1_19_20 = pd.read_csv("../Data/raw0.0/rds_dev_19_20_motivational_v1.csv")
df_v1_20_21 = pd.read_csv("../Data/raw0.0/rds_dev_20_21_motivational_v1.csv")
df_v1_21_22 = pd.read_csv("../Data/raw0.0/rds_dev_21_22_motivational_v1.csv")
df_v1_14_summer = pd.read_csv("../Data/raw0.0/rds_dev_14_motivational_v1.csv")
df_v1_15_summer = pd.read_csv("../Data/raw0.0/rds_dev_15_motivational_v1.csv")
df_v1_16_summer = pd.read_csv("../Data/raw0.0/rds_dev_16_motivational_v1.csv")
df_v1_17_summer = pd.read_csv("../Data/raw0.0/rds_dev_17_motivational_v1.csv")
df_v1_18_summer = pd.read_csv("../Data/raw0.0/rds_dev_18_motivational_v1.csv")
df_v1_19_summer = pd.read_csv("../Data/raw0.0/rds_dev_19_motivational_v1.csv")
df_v1_20_summer = pd.read_csv("../Data/raw0.0/rds_dev_20_motivational_v1.csv")
df_v1_21_summer = pd.read_csv("../Data/raw0.0/rds_dev_21_motivational_v1.csv")
df_v2_19_20 = pd.read_csv("../Data/raw0.0/rds_dev_19_20_motivational_v2.csv")
df_v2_20_21 = pd.read_csv("../Data/raw0.0/rds_dev_20_21_motivational_v2.csv")
df_v2_21_22 = pd.read_csv("../Data/raw0.0/rds_dev_21_22_motivational_v2.csv")
df_v2_20_summer = pd.read_csv("../Data/raw0.0/rds_dev_20_motivational_v2.csv")
df_v2_21_summer = pd.read_csv("../Data/raw0.0/rds_dev_21_motivational_v2.csv")
df_v2_22_summer = pd.read_csv("../Data/raw0.0/rds_dev_22_motivational_v2.csv")

# df_psa_info = pd.read_csv("../Data/raw0.0/rds_dev_PSA_motivational_v1_v2.csv")
# control_treatment_breakdown = df_psa_info.groupby(['sequence_id', 'psa_id', 'name', 'problem_id', 'pra_id']).size().reset_index(name="frequency")
# control_treatment_breakdown = control_treatment_breakdown[['sequence_id', 'psa_id', 'name', 'problem_id', 'pra_id', 'frequency']]
control_treatment_breakdown = pd.read_csv("../Data/raw0.0/rds_dev_PSA_agg_motivational_v1_v2.csv")

df_v1_13_14['academic_year'] = 'v1_13_14'
df_v1_14_15['academic_year'] = 'v1_14_15'
df_v1_15_16['academic_year'] = 'v1_15_16'
df_v1_16_17['academic_year'] = 'v1_16_17'
df_v1_17_18['academic_year'] = 'v1_17_18'
df_v1_18_19['academic_year'] = 'v1_18_19'
df_v1_19_20['academic_year'] = 'v1_19_20'
df_v1_20_21['academic_year'] = 'v1_20_21'
df_v1_21_22['academic_year'] = 'v1_21_22'
df_v1_14_summer['academic_year'] = 'v1_14_summer'
df_v1_15_summer['academic_year'] = 'v1_15_summer'
df_v1_16_summer['academic_year'] = 'v1_16_summer'
df_v1_17_summer['academic_year'] = 'v1_17_summer'
df_v1_18_summer['academic_year'] = 'v1_18_summer'
df_v1_19_summer['academic_year'] = 'v1_19_summer'
df_v1_20_summer['academic_year'] = 'v1_20_summer'
df_v1_21_summer['academic_year'] = 'v1_21_summer'
df_v2_19_20['academic_year'] = 'v2_19_20'
df_v2_20_21['academic_year'] = 'v2_20_21'
df_v2_21_22['academic_year'] = 'v2_21_22'
df_v2_20_summer['academic_year'] = 'v2_20_summer'
df_v2_21_summer['academic_year'] = 'v2_21_summer'
df_v2_22_summer['academic_year'] = 'v2_22_summer'

df_v1_13_14 = df_v1_13_14.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_14_15 = df_v1_14_15.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_15_16 = df_v1_15_16.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_16_17 = df_v1_16_17.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_17_18 = df_v1_17_18.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_18_19 = df_v1_18_19.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_19_20 = df_v1_19_20.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_20_21 = df_v1_20_21.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_21_22 = df_v1_21_22.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_14_summer = df_v1_14_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_15_summer = df_v1_15_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_16_summer = df_v1_16_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_17_summer = df_v1_17_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_18_summer = df_v1_18_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_19_summer = df_v1_19_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_20_summer = df_v1_20_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_21_summer = df_v1_21_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1 = pd.concat([
    df_v1_13_14, df_v1_14_15, df_v1_15_16, df_v1_16_17, df_v1_17_18, df_v1_18_19, df_v1_19_20, df_v1_20_21,
    df_v1_21_22, df_v1_14_summer, df_v1_15_summer, df_v1_16_summer, df_v1_17_summer, df_v1_18_summer,
    df_v1_19_summer, df_v1_20_summer, df_v1_21_summer], ignore_index=True)
skbps = ['PSA2KNM', 'PSA2KNP', 'PSA59TQ', 'PSA7GUA', 'PSA9XWV']
linearps = ['PSAH9CV', 'PSAJDQG', 'PSAJJXN']
# added new problems to the analysis
new_problems = ['PSA2KQB', 'PSAV89B', 'PSAWU6Z']


df_v1_skb = df_v1.loc[df_v1.psa_id.isin(skbps)]
df_v1_linear = df_v1.loc[df_v1.psa_id.isin(linearps)]
df_v1 = df_v1.loc[df_v1.psa_id.isin(skbps)]
df_v1.to_csv('../Data/raw0.1/motivational_v1.csv', index=False)

df_v2_19_20 = df_v2_19_20.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])
df_v2_20_21 = df_v2_20_21.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])
df_v2_21_22 = df_v2_21_22.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])
df_v2_20_summer = df_v2_20_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])
df_v2_21_summer = df_v2_21_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])
df_v2_22_summer = df_v2_22_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])
df_v2 = pd.concat([
    df_v2_19_20, df_v2_20_21, df_v2_21_22, df_v2_20_summer, df_v2_21_summer, df_v2_22_summer], ignore_index=True)

df_v2_skb = df_v2.loc[df_v2.psa_id.isin(skbps)]
df_v2_linear = df_v2.loc[df_v2.psa_id.isin(linearps)]
df_v2 = df_v2.loc[df_v2.psa_id.isin(skbps)]
df_v2.to_csv('../Data/raw0.1/motivational_v2.csv', index=False)


a = control_treatment_breakdown.loc[control_treatment_breakdown.psa_id.isin(skbps)]
b = control_treatment_breakdown.loc[control_treatment_breakdown.psa_id.isin(linearps)]
