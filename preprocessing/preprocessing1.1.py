# warning:
#  this code was added after the fact as we expanded on the number of PSAs we were
#  focusing on the preprocessing1 and 2 need to be run before running the
#  equivalent 1.1 and 2.1 code

import pandas as pd

df_v1_15_16 = pd.read_csv("../Data/raw0.0.new/rds_dev_15_16_new_motivational_v1.csv")
df_v1_16_17 = pd.read_csv("../Data/raw0.0.new/rds_dev_16_17_new_motivational_v1.csv")
df_v1_17_18 = pd.read_csv("../Data/raw0.0.new/rds_dev_17_18_new_motivational_v1.csv")
df_v1_18_19 = pd.read_csv("../Data/raw0.0.new/rds_dev_18_19_new_motivational_v1.csv")
df_v1_19_20 = pd.read_csv("../Data/raw0.0.new/rds_dev_19_20_new_motivational_v1.csv")
df_v1_20_21 = pd.read_csv("../Data/raw0.0.new/rds_dev_20_21_new_motivational_v1.csv")
df_v1_21_22 = pd.read_csv("../Data/raw0.0.new/rds_dev_21_22_new_motivational_v1.csv")
df_v1_16_summer = pd.read_csv("../Data/raw0.0.new/rds_dev_16_new_motivational_v1.csv")
df_v1_17_summer = pd.read_csv("../Data/raw0.0.new/rds_dev_17_new_motivational_v1.csv")
df_v1_18_summer = pd.read_csv("../Data/raw0.0.new/rds_dev_18_new_motivational_v1.csv")
df_v1_19_summer = pd.read_csv("../Data/raw0.0.new/rds_dev_19_new_motivational_v1.csv")
df_v1_20_summer = pd.read_csv("../Data/raw0.0.new/rds_dev_20_new_motivational_v1.csv")
df_v1_21_summer = pd.read_csv("../Data/raw0.0.new/rds_dev_21_new_motivational_v1.csv")
df_v1_22_summer = pd.read_csv("../Data/raw0.0.new/rds_dev_22_new_motivational_v1.csv")

df_v2_19_20 = pd.read_csv("../Data/raw0.0.new/rds_dev_19_20_new_motivational_v2.csv")
df_v2_20_21 = pd.read_csv("../Data/raw0.0.new/rds_dev_20_21_new_motivational_v2.csv")
df_v2_21_22 = pd.read_csv("../Data/raw0.0.new/rds_dev_21_22_new_motivational_v2.csv")
df_v2_20_summer = pd.read_csv("../Data/raw0.0.new/rds_dev_20_new_motivational_v2.csv")
df_v2_21_summer = pd.read_csv("../Data/raw0.0.new/rds_dev_21_new_motivational_v2.csv")
df_v2_22_summer = pd.read_csv("../Data/raw0.0.new/rds_dev_22_new_motivational_v2.csv")

df_v1_15_16['academic_year'] = 'v1_15_16'
df_v1_16_17['academic_year'] = 'v1_16_17'
df_v1_17_18['academic_year'] = 'v1_17_18'
df_v1_18_19['academic_year'] = 'v1_18_19'
df_v1_19_20['academic_year'] = 'v1_19_20'
df_v1_20_21['academic_year'] = 'v1_20_21'
df_v1_21_22['academic_year'] = 'v1_21_22'
df_v1_16_summer['academic_year'] = 'v1_16_summer'
df_v1_17_summer['academic_year'] = 'v1_17_summer'
df_v1_18_summer['academic_year'] = 'v1_18_summer'
df_v1_19_summer['academic_year'] = 'v1_19_summer'
df_v1_20_summer['academic_year'] = 'v1_20_summer'
df_v1_21_summer['academic_year'] = 'v1_21_summer'
df_v1_22_summer['academic_year'] = 'v1_22_summer'
df_v2_19_20['academic_year'] = 'v2_19_20'
df_v2_20_21['academic_year'] = 'v2_20_21'
df_v2_21_22['academic_year'] = 'v2_21_22'
df_v2_20_summer['academic_year'] = 'v2_20_summer'
df_v2_21_summer['academic_year'] = 'v2_21_summer'
df_v2_22_summer['academic_year'] = 'v2_22_summer'


# NOTE: added new problems to the analysis
new_problems = ['PSA2KQB', 'PSAV89B', 'PSAWU6Z']
control_treatment_breakdown = pd.read_csv("../Data/raw0.0/rds_dev_PSA_agg_motivational_v1_v2.csv")
control_treatment_breakdown = control_treatment_breakdown.loc[control_treatment_breakdown.psa_id.isin(new_problems)]

df_v1_15_16 = df_v1_15_16.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_16_17 = df_v1_16_17.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_17_18 = df_v1_17_18.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_18_19 = df_v1_18_19.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_19_20 = df_v1_19_20.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_20_21 = df_v1_20_21.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_21_22 = df_v1_21_22.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_16_summer = df_v1_16_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_17_summer = df_v1_17_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_18_summer = df_v1_18_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_19_summer = df_v1_19_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_20_summer = df_v1_20_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_21_summer = df_v1_21_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])
df_v1_22_summer = df_v1_22_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'assistment_id', 'problem_id'])

df_v2_19_20 = df_v2_19_20.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])
df_v2_20_21 = df_v2_20_21.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])
df_v2_21_22 = df_v2_21_22.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])
df_v2_20_summer = df_v2_20_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])
df_v2_21_summer = df_v2_21_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])
df_v2_22_summer = df_v2_22_summer.merge(control_treatment_breakdown, how='left', on=['sequence_id', 'problem_id'])

df_v1 = pd.concat([
    df_v1_15_16, df_v1_16_17, df_v1_17_18, df_v1_18_19, df_v1_19_20, df_v1_20_21, df_v1_21_22,
    df_v1_16_summer, df_v1_17_summer, df_v1_18_summer, df_v1_19_summer, df_v1_20_summer,
    df_v1_21_summer, df_v1_22_summer], ignore_index=True)

df_v2 = pd.concat([
    df_v2_19_20, df_v2_20_21, df_v2_21_22, df_v2_20_summer, df_v2_21_summer, df_v2_22_summer], ignore_index=True)

df_v1.to_csv('../Data/raw0.1/motivational_v1_new.csv', index=False)
df_v2.to_csv('../Data/raw0.1/motivational_v2_new.csv', index=False)
