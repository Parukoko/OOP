def add_score(subject_score, student, subject, score):
	if student in subject_score:
		subject_score[student].update({subject:score})
	else:
		subject_score[student] = {subject:score}
	return subject_score
def calc_average_score(subject_score):
    average_scores = {student: sum(scores.values()) / len(scores) for student, scores in subject_score.items()}
    return {student: "{:.2f}".format(average) for student, average in average_scores.items()}



""" nested_dict = {'outer_key': {'inner_key': 'old_value'}}
update_dict = {'inner_key': 'new_value'}
nested_dict['outer_key'].update(update_dict)
 """
