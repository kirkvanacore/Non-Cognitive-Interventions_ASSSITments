# NOTE:
#  all problem sets have different structure and skbs are being reused across conditions
#  We need to go through and figure out the treatment and control conditions using the
#  decision that lead the students to the skb
# TODO: the key problem_ids are hard-coded in the README.md for now

import pandas as pd
import preprocessing_computemastery as computemastery


def parse_PSA2KNM(df):
    user_ids = df.loc[df.psa_id == "PSA2KNM"].user_id.unique()
    for user_id in user_ids:
        video_check_answer = df.loc[((df.user_id == user_id) & (df.problem_id == 1352945))].answer_text.unique()
        if video_check_answer.size > 0:
            if video_check_answer[0].lower() == 'wpi':
                problem_ids = df.loc[((df.psa_id == "PSA2KNM") & (df.user_id == user_id))].problem_id.unique()
                assigned = False
                df.loc[((df.psa_id == "PSA2KNM") & (df.user_id == user_id)), "control_treatments"] = "control"
                if 1356358 in problem_ids:
                    df.loc[
                        ((df.psa_id == "PSA2KNM") & (df.user_id == user_id)), "control_treatments"] = "treatment1:text"
                    assigned = True
                if (1356360 in problem_ids) and (not assigned):
                    df.loc[
                        ((df.psa_id == "PSA2KNM") & (df.user_id == user_id)), "control_treatments"] = "treatment2:video"
                elif (1356360 in problem_ids) and assigned:
                    df.loc[
                        ((df.psa_id == "PSA2KNM") & (df.user_id == user_id)), "control_treatments"] = "both_treatments"

                df.loc[((df.psa_id == "PSA2KNM") & (df.user_id == user_id) &
                        (df.problem_id.isin([1352945]))), "control_treatments"] = "video_check_passed"
                df.loc[((df.psa_id == "PSA2KNM") & (df.user_id == user_id) &
                        (df.problem_id.isin([1277136, 1390194]))), "control_treatments"] = "ignore_guide_problems"
                df.loc[((df.psa_id == "PSA2KNM") & (df.user_id == user_id) &
                        (df.problem_id.isin([1221518, 1221527]))), "control_treatments"] = "posttest"
            else:
                df.loc[((df.psa_id == "PSA2KNM") & (df.user_id == user_id)), "control_treatments"] = "video_check_fail"

    df = computemastery.check_for_mastery_wheel_spinning(df, "PSA2KNM")
    return df


def parse_PSA2KNP(df):
    user_ids = df.loc[df.psa_id == "PSA2KNP"].user_id.unique()
    for user_id in user_ids:
        video_check_answer = df.loc[((df.user_id == user_id) & (df.problem_id == 1352945))].answer_text.unique()
        if video_check_answer.size > 0:
            if video_check_answer[0].lower() == 'wpi':
                problem_ids = df.loc[((df.psa_id == "PSA2KNP") & (df.user_id == user_id))].problem_id.unique()
                assigned = False
                df.loc[((df.psa_id == "PSA2KNP") & (df.user_id == user_id)), "control_treatments"] = "control"
                if 1356358 in problem_ids:
                    df.loc[
                        ((df.psa_id == "PSA2KNP") & (df.user_id == user_id)), "control_treatments"] = "treatment1:text"
                    assigned = True
                if (1356360 in problem_ids) and (not assigned):
                    df.loc[
                        ((df.psa_id == "PSA2KNP") & (df.user_id == user_id)), "control_treatments"] = "treatment2:video"
                elif (1356360 in problem_ids) and assigned:
                    df.loc[
                        ((df.psa_id == "PSA2KNP") & (df.user_id == user_id)), "control_treatments"] = "both_treatments"

                df.loc[((df.psa_id == "PSA2KNP") & (df.user_id == user_id) &
                        (df.problem_id.isin([1352945]))), "control_treatments"] = "video_check_passed"
                df.loc[((df.psa_id == "PSA2KNP") & (df.user_id == user_id) &
                        (df.problem_id.isin([1277136, 1390194, 1356358]))), "control_treatments"] = "ignore_guide_problems"
                df.loc[((df.psa_id == "PSA2KNP") & (df.user_id == user_id) &
                        (df.problem_id.isin([1222222, 1222224]))), "control_treatments"] = "posttest"
            else:
                df.loc[((df.psa_id == "PSA2KNP") & (df.user_id == user_id)), "control_treatments"] = "video_check_fail"

    df = computemastery.check_for_mastery_wheel_spinning(df, "PSA2KNP")
    return df


def parse_PSA9XWV(df):
    user_ids = df.loc[df.psa_id == "PSA9XWV"].user_id.unique()
    for user_id in user_ids:
        problem_ids = df.loc[((df.psa_id == "PSA9XWV") & (df.user_id == user_id))].problem_id.unique()
        assigned = False
        if 1641481 in problem_ids:
            df.loc[((df.psa_id == "PSA9XWV") & (df.user_id == user_id)), "control_treatments"] = "control_message"
            assigned = True
        if 1641482 in problem_ids and not assigned:
            df.loc[
                ((df.psa_id == "PSA9XWV") & (df.user_id == user_id)), "control_treatments"] = "treatment1:10_to_mastery"
        elif 1641482 in problem_ids and assigned:
            df.loc[((df.psa_id == "PSA9XWV") & (df.user_id == user_id)), "control_treatments"] = "both_treatments"
        if 1641483 in problem_ids and not assigned:
            df.loc[((df.psa_id == "PSA9XWV") & (
                        df.user_id == user_id)), "control_treatments"] = "treatment2:high_hint_usage"
        elif 1641483 in problem_ids and assigned:
            df.loc[((df.psa_id == "PSA9XWV") & (df.user_id == user_id)), "control_treatments"] = "both_treatments"

        df.loc[((df.psa_id == "PSA9XWV") & (df.user_id == user_id) &
                (df.problem_id.isin([1641490]))), "control_treatments"] = "ignore_posttest"
        df.loc[((df.psa_id == "PSA9XWV") & (df.user_id == user_id) &
                (df.problem_id.isin([1523968, 1523974, 1523981]))), "control_treatments"] = "posttest"

    df = computemastery.check_for_mastery_wheel_spinning(df, "PSA9XWV")
    return df


def parse_PSA59TQ(df):
    user_ids = df.loc[df.psa_id == "PSA59TQ"].user_id.unique()
    for user_id in user_ids:
        problem_ids = df.loc[((df.psa_id == "PSA59TQ") & (df.user_id == user_id))].problem_id.unique()
        treatment_ids = [1495245, 1495246, 1495247]
        if any(x in treatment_ids for x in problem_ids):
            df.loc[
                ((df.psa_id == "PSA59TQ") & (df.user_id == user_id)), "control_treatments"] = "treatment:encouragement"
        else:
            df.loc[
                ((df.psa_id == "PSA59TQ") & (df.user_id == user_id)), "control_treatments"] = "control:no_encouragement"

        df.loc[((df.psa_id == "PSA59TQ") & (df.user_id == user_id) &
                (df.problem_id.isin([1498223]))), "control_treatments"] = "competency_check_problem"
        df.loc[((df.psa_id == "PSA59TQ") & (df.user_id == user_id) &
                (df.problem_id.isin([1505320]))), "control_treatments"] = "ignore_posttest"
        df.loc[((df.psa_id == "PSA59TQ") & (df.user_id == user_id) &
                (df.problem_id.isin([1059308, 1198778, 386818]))), "control_treatments"] = "posttest"

    df = computemastery.check_for_mastery_wheel_spinning(df, "PSA59TQ")
    return df


def parse_PSA7GUA(df):
    user_ids = df.loc[df.psa_id == "PSA7GUA"].user_id.unique()
    for user_id in user_ids:
        problem_ids = df.loc[((df.psa_id == "PSA7GUA") & (df.user_id == user_id))].problem_id.unique()
        treatment_ids = [1495245, 1495246, 1495247]
        if any(x in treatment_ids for x in problem_ids):
            df.loc[
                ((df.psa_id == "PSA7GUA") & (df.user_id == user_id)), "control_treatments"] = "treatment:encouragement"
        else:
            df.loc[
                ((df.psa_id == "PSA7GUA") & (df.user_id == user_id)), "control_treatments"] = "control:no_encouragement"

        df.loc[((df.psa_id == "PSA7GUA") & (df.user_id == user_id) &
                (df.problem_id.isin([1498223]))), "control_treatments"] = "competency_check_problem"
        df.loc[((df.psa_id == "PSA7GUA") & (df.user_id == user_id) &
                (df.problem_id.isin([1505320]))), "control_treatments"] = "ignore_posttest"
        df.loc[((df.psa_id == "PSA7GUA") & (df.user_id == user_id) &
                (df.problem_id.isin([1215094, 1215093]))), "control_treatments"] = "posttest"

    df = computemastery.check_for_mastery_wheel_spinning(df, "PSA7GUA")
    return df


df_v1 = pd.read_csv("../Data/raw0.1/motivational_v1.csv")
# df_v1 = df_v1[:2000]
df_v1["control_treatments"] = "unassigned"
df_v2 = pd.read_csv("../Data/raw0.1/motivational_v2.csv")
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
df_v1 = parse_PSA2KNM(df_v1)
print("DONE:: -> parse_PSA2KNM(df_v1)")
df_v1 = parse_PSA2KNP(df_v1)
print("DONE:: -> parse_PSA2KNP(df_v1)")
df_v1 = parse_PSA9XWV(df_v1)
print("DONE:: -> parse_PSA9XWV(df_v1)")
df_v1 = parse_PSA59TQ(df_v1)
print("DONE:: -> parse_PSA59TQ(df_v1)")
df_v1 = parse_PSA7GUA(df_v1)
print("DONE:: -> parse_PSA7GUA(df_v1)")
df_v1 = df_v1.loc[~(df_v1.control_treatments == 'unassigned')]

df_v2.rename({'user_xid': 'user_id'}, axis=1, inplace=True)
df_v2.sort_values(by=['psa_id', 'user_id', 'assignment_id', 'problem_log_id'], inplace=True)
df_v2 = parse_PSA2KNM(df_v2)
print("DONE:: -> parse_PSA2KNM(df_v2)")
df_v2 = parse_PSA2KNP(df_v2)
print("DONE:: -> parse_PSA2KNP(df_v2)")
df_v2 = parse_PSA9XWV(df_v2)
print("DONE:: -> parse_PSA9XWV(df_v2)")
df_v2 = parse_PSA59TQ(df_v2)
print("DONE:: -> parse_PSA59TQ(df_v2)")
df_v2 = parse_PSA7GUA(df_v2)
print("DONE:: -> parse_PSA7GUA(df_v2)")
df_v2 = df_v2.loc[~(df_v2.control_treatments == 'unassigned')]

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


df_v1_.to_csv("../Data/raw0.2/motivational_v1.csv", index=False)
df_v2_.to_csv("../Data/raw0.2/motivational_v2.csv", index=False)

print(df_v1_.groupby(['psa_id', 'control_treatments']).size().reset_index(name='frequency'))
print(df_v2_.groupby(['psa_id', 'control_treatments']).size().reset_index(name='frequency'))

# control_treatment_breakdown = pd.read_csv("../Data/raw0.0/rds_dev_PSA_agg_motivational_v1_v2.csv")
# control_treatment_breakdown = control_treatment_breakdown.loc[control_treatment_breakdown.psa_id.isin(["PSAWU6Z", "PSAV89B", "PSA2KQB"])]
# control_treatment_breakdown_ = control_treatment_breakdown.loc[
#     (control_treatment_breakdown.assistment_id.isin([
#         1355695,189250, 189197,1277136, 1355456, 1355457,
#         525061, 525087, 525088, 525091, 525050, 525090,
#         807728, 807754, 807755, 807757, 807758, 807717
#     ])) |
#     (control_treatment_breakdown.problem_id.isin([
#         1355695,189250, 189197,1277136, 1355456, 1355457,
#         525061, 525087, 525088, 525091, 525050, 525090,
#         807728, 807754, 807755, 807757, 807758, 807717
#     ]))]


