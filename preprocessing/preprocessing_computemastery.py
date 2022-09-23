def check_for_mastery_wheel_spinning(df_temp, psa_id):
    user_ids = df_temp.loc[df_temp.psa_id == psa_id].user_id.unique()

    for user_id in user_ids:
        assignment_ids = df_temp.loc[(df_temp.psa_id == psa_id) & (df_temp.user_id == user_id)].assignment_id.unique()
        for assignment_id in assignment_ids:
            problem_log_ids = df_temp.loc[
                (df_temp.psa_id == psa_id) & (df_temp.user_id == user_id) & (df_temp.assignment_id == assignment_id)
                ].problem_log_id

            skb_mastery_count = 0
            skb_problem_count = 0
            for problem_log_id in problem_log_ids:
                control_treatment_info = df_temp.loc[df_temp.problem_log_id == problem_log_id].control_treatments.unique()[0]
                # print(control_treatment_info)
                if ('ignore' in control_treatment_info) or ('fail' in control_treatment_info) or \
                        ('pass' in control_treatment_info) or ('check' in control_treatment_info):
                    continue
                elif 'posttest' not in control_treatment_info:
                    continuous_score = df_temp.loc[df_temp.problem_log_id == problem_log_id].continuous_score.values
                    skb_problem_count += 1
                    if len(continuous_score) > 0:
                        if continuous_score[0] == 1:
                            skb_mastery_count += 1
                        else:
                            skb_mastery_count = 0
                    else:
                        skb_mastery_count = 0

            tags = df_temp.loc[
                (df_temp.psa_id == psa_id) & (df_temp.user_id == user_id) &
                (df_temp.assignment_id == assignment_id)].control_treatments
            if (skb_mastery_count >= 3) or ('posttest' in tags):
                df_temp.loc[(df_temp.psa_id == psa_id) & (df_temp.user_id == user_id) & (
                            df_temp.assignment_id == assignment_id), 'mastery'] = True
                df_temp.loc[(df_temp.psa_id == psa_id) & (df_temp.user_id == user_id) & (
                        df_temp.assignment_id == assignment_id), 'skb_mastery_count'] = skb_mastery_count

            if skb_problem_count >= 12:
                df_temp.loc[(df_temp.psa_id == psa_id) & (df_temp.user_id == user_id) & (
                            df_temp.assignment_id == assignment_id), 'wheel_spinning'] = True

            df_temp.loc[(df_temp.psa_id == psa_id) & (df_temp.user_id == user_id) & (
                        df_temp.assignment_id == assignment_id), 'skb_problem_count'] = skb_problem_count

    return df_temp


def check_for_duplicates(temp_df):
    both_true_false_counts = temp_df.groupby(
        ['user_assignment_combo', 'assignment_log_id']).size().reset_index(name='frequency')
    both_true_false_counts.sort_values(['user_assignment_combo', 'assignment_log_id'], inplace=True)
    both_true_false_counts = both_true_false_counts.drop_duplicates(['user_assignment_combo'])
    temp_df = temp_df.loc[temp_df.assignment_log_id.isin(both_true_false_counts.assignment_log_id.unique())]
    return temp_df
