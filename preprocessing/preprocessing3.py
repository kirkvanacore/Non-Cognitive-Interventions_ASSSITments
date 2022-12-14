import pandas as pd

df_v1_new = pd.read_csv("../Data/raw0.2/motivational_v1_new.csv")
df_v2_new = pd.read_csv("../Data/raw0.2/motivational_v2_new.csv")
df_v1 = pd.read_csv("../Data/raw0.2/motivational_v1.csv")
df_v2 = pd.read_csv("../Data/raw0.2/motivational_v2.csv")

df_v1_new_count = df_v1_new.groupby(['psa_id', 'control_treatments', 'user_id', 'mastery',
                                     'skb_mastery_count']).size().reset_index(name='frequency')
df_v2_new_count = df_v2_new.groupby(['psa_id', 'control_treatments', 'user_id', 'mastery',
                                     'skb_mastery_count']).size().reset_index(name='frequency')
df_v1_count = df_v1.groupby(['psa_id', 'control_treatments', 'user_id', 'mastery',
                             'skb_mastery_count']).size().reset_index(name='frequency')
df_v2_count = df_v2.groupby(['psa_id', 'control_treatments', 'user_id', 'mastery',
                             'skb_mastery_count']).size().reset_index(name='frequency')
print(df_v1_new_count.groupby(['psa_id', 'control_treatments', 'skb_mastery_count']).size().reset_index(name='frequency'))
print(df_v2_new_count.groupby(['psa_id', 'control_treatments', 'skb_mastery_count']).size().reset_index(name='frequency'))
print(df_v1_count.groupby(['psa_id', 'control_treatments', 'skb_mastery_count']).size().reset_index(name='frequency'))
print(df_v2_count.groupby(['psa_id', 'control_treatments', 'skb_mastery_count']).size().reset_index(name='frequency'))

df_v1_new_count_morethan3 = df_v1_new_count.loc[df_v1_new_count.skb_mastery_count > 3]
df_v2_new_count_morethan3 = df_v2_new_count.loc[df_v2_new_count.skb_mastery_count > 3]
df_v1_count_morethan3 = df_v1_count.loc[df_v1_count.skb_mastery_count > 3]
df_v2_count_morethan3 = df_v2_count.loc[df_v2_count.skb_mastery_count > 3]

drop_values = ['ignore_guide_problems', 'posttest', 'video_check_passed', 'competency_check_problem', 'ignore_posttest']

df_v1_new_count_morethan3_ = df_v1_new_count_morethan3.loc[~df_v1_new_count_morethan3.control_treatments.isin(drop_values)]
df_v2_new_count_morethan3_ = df_v2_new_count_morethan3.loc[~df_v2_new_count_morethan3.control_treatments.isin(drop_values)]
df_v1_count_morethan3_ = df_v1_count_morethan3.loc[~df_v1_count_morethan3.control_treatments.isin(drop_values)]
df_v2_count_morethan3_ = df_v2_count_morethan3.loc[~df_v2_count_morethan3.control_treatments.isin(drop_values)]



# a = df_v2_new.loc[df_v2_new.psa_id == "PSAWU6Z"]
# a_test = a.groupby(['user_id', 'control_treatments', 'mastery']).size().reset_index(name='frequency')
# # print(a_test.groupby(['control_treatments']).size().reset_index(name='frequency'))
# print("df_v2_new", "PSAWU6Z")
# print(a_test.groupby(['control_treatments', 'mastery']).size().reset_index(name='frequency'))
#
# b = df_v2_new.loc[df_v2_new.psa_id == "PSAV89B"]
# b_test = b.groupby(['user_id', 'control_treatments', 'mastery']).size().reset_index(name='frequency')
# # print(b_test.groupby(['control_treatments']).size().reset_index(name='frequency'))
# print("df_v2_new", "PSAV89B")
# print(b_test.groupby(['control_treatments', 'mastery']).size().reset_index(name='frequency'))
#
# df_v1_new = pd.read_csv("../Data/raw0.2/motivational_v1_new.csv")
#
# a = df_v1_new.loc[df_v1_new.psa_id == "PSAWU6Z"]
# a_test = a.groupby(['user_id', 'control_treatments', 'mastery']).size().reset_index(name='frequency')
# # print(a_test.groupby(['control_treatments']).size().reset_index(name='frequency'))
# print("df_v1_new", "PSAWU6Z")
# print(a_test.groupby(['control_treatments', 'mastery']).size().reset_index(name='frequency'))
#
# b = df_v1_new.loc[df_v1_new.psa_id == "PSAV89B"]
# b_test = b.groupby(['user_id', 'control_treatments', 'mastery']).size().reset_index(name='frequency')
# # print(b_test.groupby(['control_treatments']).size().reset_index(name='frequency'))
# print("df_v1_new", "PSAV89B")
# print(b_test.groupby(['control_treatments', 'mastery']).size().reset_index(name='frequency'))
#
# treatment_competency = [807728, 807754, 807755]
# df_v1 = pd.read_csv("../Data/raw0.1/motivational_v1_new.csv")
# test_condition = df_v1.loc[df_v1.problem_id.isin(treatment_competency)]
# test_condition.groupby(['psa_id', 'user_id', 'section_names']).size().reset_index(name='frequency')
#
# abc = df_v2_new.loc[
#     df_v2_new.psa_id.isin(["PSAV89B", "PSAWU6Z"])
# ].groupby(['psa_id', 'user_id', 'control_treatments', 'section_names', 'mastery']).size().reset_index(name='frequency')
