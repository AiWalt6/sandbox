from pathlib import Path


GRADES_FILE = Path(__file__).resolve().parent / 'grades.csv'

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2
COLUMN_COUNT = 11
MIN_SCORE = 0
MAX_SCORE = 100


def main():
    try:
        final_grades = read_grades(GRADES_FILE)
    except OSError as error:
        print(f'Error: Could not read grades.csv: {error}')
        return
    except ValueError as error:
        print(f'Error: {error}')
        return

    analyze_grade(final_grades)


def read_grades(filename):
    final_grades = []

    with open(filename, encoding='utf-8-sig') as grades_file:
        header = grades_file.readline().strip().split(',')
        if len(header) != COLUMN_COUNT or header[:2] != ['Name', 'StudentID']:
            raise ValueError('The grades file must begin with a valid header.')

        line_number = 1
        for line in grades_file:
            line_number += 1
            if not line.strip():
                continue

            row = line.strip().split(',')
            try:
                final_grades.append(process_row(row))
            except ValueError as error:
                raise ValueError(f'Line {line_number}: {error}') from error

    if not final_grades:
        raise ValueError('The grades file contains no student records.')

    return final_grades


def process_row(row):
    if len(row) != COLUMN_COUNT:
        raise ValueError(
            f'Each student row must contain {COLUMN_COUNT} columns.'
        )
    if not row[0].strip() or not row[1].strip():
        raise ValueError('Each student must have a name and StudentID.')

    scores = []
    for value in row[2:]:
        try:
            score = float(value.strip())
        except ValueError as error:
            raise ValueError('All scores must be numeric.') from error
        if not MIN_SCORE <= score <= MAX_SCORE:
            raise ValueError(
                f'All scores must be between {MIN_SCORE} and {MAX_SCORE}.'
            )
        scores.append(score)

    test_avg = average_subject(scores[:4])
    exam_avg = average_subject(scores[4:6])
    discussion_avg = average_subject(scores[6:8])
    return weight_final(test_avg, exam_avg, discussion_avg, scores[8])


def average_subject(subject_list):
    return sum(subject_list) / len(subject_list)


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    return (
        test_avg * TEST_WEIGHT
        + exam_avg * EXAM_WEIGHT
        + discussion_avg * DISCUSSION_WEIGHT
        + project_score * PROJECT_WEIGHT
    )


def analyze_grade(weight_final_list):
    grade_counts = [0, 0, 0, 0, 0]

    for final_grade in weight_final_list:
        if final_grade >= 90:
            grade_counts[0] += 1
        elif final_grade >= 80:
            grade_counts[1] += 1
        elif final_grade >= 70:
            grade_counts[2] += 1
        elif final_grade >= 60:
            grade_counts[3] += 1
        else:
            grade_counts[4] += 1

    grade_ranges = ['90 or above', '80–89', '70–79', '60–69', 'below 60']
    for index in range(len(grade_counts)):
        print(
            f'Number of students with final grade {grade_ranges[index]}: '
            f'{grade_counts[index]}'
        )


if __name__ == '__main__':
    main()
