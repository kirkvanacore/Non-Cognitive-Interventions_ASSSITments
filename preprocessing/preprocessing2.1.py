# NOTE:
#  all problem sets have different structure and skbs are being reused across conditions
#  We need to go through and figure out the treatment and control conditions using the
#  decision that lead the students to the skb
# TODO: the key problem_ids are hard-coded in the README.md for now

import pandas as pd
import preprocessing_computemastery as computemastery


def parse_PSA2KQB(df):
    user_ids = df.loc[df.psa_id == "PSA2KQB"].user_id.unique()
    for user_id in user_ids:
        problem_ids = df.loc[((df.psa_id == "PSA2KQB") & (df.user_id == user_id))].problem_id.unique()
        df.loc[((df.psa_id == "PSA2KQB") & (
                    df.psa_id == user_id)), 'control_treatments'] = "control"
        if 1355695 in problem_ids:
            score_mean = df.loc[((df.psa_id == "PSA2KQB") & (df.user_id == user_id) &
                                 (df.problem_id.isin([189250, 189197])))].continuous_score.mean()
            if score_mean >= 2:
                df.loc[((df.psa_id == "PSA2KQB") & (df.psa_id == user_id)),
                       'control_treatments'] = "treatment1:same_diff_in_correctness"
            else:
                df.loc[((df.psa_id == "PSA2KQB") & (df.psa_id == user_id)),
                       'control_treatments'] = "treatment2:same_diff_in_correctness"
        df.loc[((df.psa_id == "PSA2KQB") & (df.user_id == user_id) &
                (df.problem_id.isin([1277136]))), "control_treatments"] = "ignore_guide_problems"
        df.loc[((df.psa_id == "PSA2KQB") & (df.user_id == user_id) &
                (df.problem_id.isin([1355456, 1355457]))), "control_treatments"] = "posttest"
    computemastery.check_for_mastery_wheel_spinning(df, "PSA2KQB")
    return df


def parse_PSAV89B(df):
    user_ids = df.loc[df.psa_id == "PSAV89B"].user_id.unique()
    for user_id in user_ids:
        problem_ids = df.loc[((df.psa_id == "PSAV89B") & (df.user_id == user_id))].problem_id.unique()
        treatment_competency = [525061, 525087, 525088]
        treatment_plain_message = [525091, 525050, 525090]
        assigned = False
        df.loc[((df.psa_id == "PSAV89B") & (df.psa_id == user_id)), 'control_treatments'] = "control"
        if any(x in treatment_competency for x in problem_ids):
            df.loc[
                ((df.psa_id == "PSAV89B") & (
                            df.psa_id == user_id)), 'control_treatments'] = "treatment1:competency_check"
            assigned = True

        if any(x in treatment_plain_message for x in problem_ids) and assigned:
            df.loc[
                ((df.psa_id == "PSAV89B") & (df.psa_id == user_id)), 'control_treatments'] = "both_treatments"
        else:
            df.loc[
                ((df.psa_id == "PSAV89B") & (df.psa_id == user_id)), 'control_treatments'] = "treatment2:plain_message"
    computemastery.check_for_mastery_wheel_spinning(df, "PSAV89B")
    return df


def parse_PSAWU6Z(df):
    user_ids = df.loc[df.psa_id == "PSAWU6Z"].user_id.unique()
    for user_id in user_ids:
        problem_ids = df.loc[((df.psa_id == "PSAWU6Z") & (df.user_id == user_id))].problem_id.unique()
        treatment_competency = [807728, 807754, 807755]
        treatment_plain_message = [807757, 807758, 807717]
        assigned = False
        df.loc[((df.psa_id == "PSAWU6Z") & (df.psa_id == user_id)), 'control_treatments'] = "control"
        if any(x in treatment_competency for x in problem_ids):
            df.loc[
                ((df.psa_id == "PSAWU6Z") & (
                            df.psa_id == user_id)), 'control_treatments'] = "treatment1:competency_check"
            assigned = True

        if any(x in treatment_plain_message for x in problem_ids) and assigned:
            df.loc[
                ((df.psa_id == "PSAWU6Z") & (df.psa_id == user_id)), 'control_treatments'] = "both_treatments"
        else:
            df.loc[
                ((df.psa_id == "PSAWU6Z") & (df.psa_id == user_id)), 'control_treatments'] = "treatment2:plain_message"
    computemastery.check_for_mastery_wheel_spinning(df, "PSAWU6Z")
    return df


df_v1 = pd.read_csv("../Data/raw0.1/motivational_v1_new.csv")
# df_v1 = df_v1[:2000]
df_v1["control_treatments"] = "unassigned"
df_v2 = pd.read_csv("../Data/raw0.1/motivational_v2_new.csv")
# df_v2 = df_v2[:2000]
df_v2["control_treatments"] = "unassigned"

df_v1['mastery'] = False
df_v1['skb_mastery_count'] = 0
df_v1['wheel_spinning'] = False
df_v1['skb_problem_count'] = 0

df_v2['mastery'] = False
df_v2['skb_mastery_count'] = 0
df_v2['wheel_spinning'] = False
df_v2['skb_problem_count'] = 0

df_v1.rename({'correct': 'continuous_score'}, axis=1, inplace=True)
df_v1.sort_values(by=['psa_id', 'user_id', 'assignment_id', 'problem_log_id'], inplace=True)
df_v1 = parse_PSA2KQB(df_v1)
print("DONE:: -> parse_PSA2KQB(df_v1)")
df_v1 = parse_PSAV89B(df_v1)
print("DONE:: -> parse_PSAV89B(df_v1)")
df_v1 = parse_PSAWU6Z(df_v1)
print("DONE:: -> parse_PSAWU6Z(df_v1)")
df_v1 = df_v1.loc[~(df_v1.control_treatments == 'unassigned')]

df_v2.rename({'user_xid': 'user_id'}, axis=1, inplace=True)
df_v2.sort_values(by=['psa_id', 'user_id', 'assignment_id', 'problem_log_id'], inplace=True)
df_v2 = parse_PSA2KQB(df_v2)
print("DONE:: -> parse_PSA2KQB(df_v2)")
df_v2 = parse_PSAV89B(df_v2)
print("DONE:: -> parse_PSAV89B(df_v2)")
df_v2 = parse_PSAWU6Z(df_v2)
print("DONE:: -> parse_PSAWU6Z(df_v2)")
df_v1 = df_v1.loc[~(df_v1.control_treatments == 'unassigned')]

# 'name', 'student_class_id', 'teacher_id',
# 'academic_year', 'pra_id', 'parent_ids', 'section_types',
# 'section_names', 'array_agg', 'psa_id', 'user_id', 'problem_log_id', 'control_treatments'
#
# 'owner_xid', 'group_context_xid',
# 'academic_year', 'assistment_id', 'pra_id', 'parent_ids',
# 'section_types', 'section_names', 'array_agg', 'psa_id', 'user_id', 'problem_log_id', 'control_treatments'

df_v1.rename({
    "start_time": "problem_log_start_time",
    "end_time": "problem_log_end_time"
}, axis=1, inplace=True)
df_v2.rename({
    "owner_xid": "teacher_id",
    "group_context_xid": "student_class_id",
    "first_action_type_id": "first_action"
}, axis=1, inplace=True)

df_v1_ = df_v1[['problem_log_id', 'assignment_id', 'problem_id', 'continuous_score', 'answer_text',
                'first_action', 'hint_count', 'bottom_hint',
                'attempt_count', 'problem_log_start_time', 'problem_log_end_time', 'first_response_time',
                'user_id', 'assistment_id',
                'sequence_id', 'name', 'student_class_id', 'teacher_id',
                'academic_year', 'psa_id', 'pra_id', 'parent_ids', 'section_types',
                'section_names', 'array_agg', 'control_treatments', 'mastery', 'skb_mastery_count',
                'wheel_spinning', 'skb_problem_count']]

df_v2_ = df_v2[['problem_log_id', 'assignment_id', 'problem_id', 'continuous_score', 'answer_text',
                'first_action', 'hint_count', 'bottom_hint',
                'attempt_count', 'problem_log_start_time', 'problem_log_end_time', 'first_response_time',
                'user_id', 'assistment_id',
                'sequence_id', 'name', 'student_class_id', 'teacher_id',
                'academic_year', 'psa_id', 'pra_id', 'parent_ids', 'section_types',
                'section_names', 'array_agg', 'control_treatments', 'mastery', 'skb_mastery_count',
                'wheel_spinning', 'skb_problem_count']]

df_v1_.to_csv("../Data/raw0.2/motivational_v1_new.csv", index=False)
df_v2_.to_csv("../Data/raw0.2/motivational_v2_new.csv", index=False)
