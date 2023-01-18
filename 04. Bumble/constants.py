"""File containing the constants used on the bumble assignment project"""

"""List of categorical features on the data"""
CATEGORICAL_VAR = [
    'body_type', 'drinks', 'drugs', 'ethnicity', 'offspring',
    'religion', 'sign', 'smokes', 'job', 'pets'
]

"""List of categorical features on the data after processing"""
CATEGORICAL_VAR_PROCESSED = [
    'body_type', 'drinks', 'drugs', 'offspring', 'pets',
    'religion', 'sex', 'sign', 'smokes', 'religion_importance', 'sign_importance'
]

"""List of continuous features on the data"""
CONTINUOUS_VAR = ['age', 'height_cm', 'income']

"""Dictionary of Essay features and their description"""
ESSAYS ={
    'essay0': 'My self summary',
    'essay1': 'What I’m doing with my life',
    'essay2': 'I’m really good at',
    'essay3': 'The first thing people usually notice about me',
    'essay4': 'Favorite books, movies, show, music, and food',
    'essay5': 'The six things I could never do without',
    'essay6': 'I spend a lot of time thinking about',
    'essay7': 'On a typical Friday night I am',
    'essay8': 'The most private thing I am willing to admit',
    'essay9': 'You should message me if...'
}