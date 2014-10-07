#This file is auto-generated by Eddex.
from dexen_libs.moea.individual import (
    ALIVE,
    GENOTYPE,
    PHENOTYPE,
    GeneFloatRange,
    GeneIntRange,
    GeneIntChoice,
    GeneStringChoice,
    GenotypeMeta)

from dexen_libs.moea.executors import Condition

from dexen_libs.feedback.ranking import (
    MIN, MAX,
    ScoreMeta,
    ScoresMeta)

from dexen_libs.feedback.fitness import (
    SINGLE_CRITERIA, 
    SINGLE_CRITERIA_RANKING, 
    PARETO_MULTI_RANKING, 
    PARETO_GOLDBERG_RANKING, 
    PARETO_FONSECA_FLEMMING_RANKING)

from dexen_libs.feedback.selection import (
    RANDOMLY,
    OLDEST, YOUNGEST, 
    BEST, WORST,
    ROULETTE_BEST, ROULETTE_WORST,
    TOURNAMENT_BEST, TOURNAMENT_WORST,
    TOURNAMENT_RTS_BEST, TOURNAMENT_RTS_WORST)

#Lists to store eval settings
EVALUATE_NAMES = []
EVALUATE_INPUT_SIZES = []
EVALUATE_IN_PATHS = []
EVALUATE_OUT_PATHS = []
EVALUATE_ANIMS = []
EVALUATE_SCORE_GOALS = []
EVALUATE_SCORE_NAMES = []
EVALUATE_CONDS = []
EVALUATE_ARGS = []

#Meta info for scores
scores_meta = ScoresMeta()

#Meta info for genes
genotype_meta = GenotypeMeta()


#GENERAL
VERBOSE = False
MAX_BIRTHS = 1000
HIP_FILE_NAME = 'procedures.hipnc'
HIP_FILE_PATH = 'C:/GitHub/eddex/houdini/examples/houdini_ea_basic2/procedures.hipnc'
CODE_FOLDER_PATH = 'C:/GitHub/eddex/houdini/examples/houdini_ea_basic2/code'

#INITIALIZE
INITIALIZE_NAME = 'initialize'
POP_SIZE = 50
INITIALIZE_ARGS = ['python', 'tasks.py', 'initialize']

#DEVELOPMENT
DEVELOP_NAME = 'develop'
DEVELOP_INPUT_SIZE = 10
DEVELOP_IN_PATH = '/obj/develop/GENOTYPE'
DEVELOP_OUT_PATH = '/obj/develop/PHENOTYPE'
DEVELOP_ANIM = None
DEVELOP_COND = Condition().exists(GENOTYPE).not_exists(PHENOTYPE).get()
DEVELOP_ARGS = ['hython', 'tasks.py', 'develop']

#EVALUATION: area
EVALUATE_NAME = 'evaluate'
EVALUATE_NAMES.append('area')
EVALUATE_INPUT_SIZES.append(10)
EVALUATE_IN_PATHS.append('/obj/eval_area/PHENOTYPE')
EVALUATE_OUT_PATHS.append('/obj/eval_area/SCORE')
EVALUATE_SCORE_GOALS.append([MIN])
EVALUATE_SCORE_NAMES.append(['score_area'])
EVALUATE_ANIMS.append([])
EVALUATE_CONDS.append(Condition().exists(PHENOTYPE).not_exists('score_area').get())
EVALUATE_ARGS.append(['hython', 'tasks.py', 'evaluate', '0'])
scores_meta.append(ScoreMeta('score_area', MIN))

#EVALUATION: volume
EVALUATE_NAME = 'evaluate'
EVALUATE_NAMES.append('volume')
EVALUATE_INPUT_SIZES.append(10)
EVALUATE_IN_PATHS.append('/obj/eval_volume/PHENOTYPE')
EVALUATE_OUT_PATHS.append('/obj/eval_volume/SCORE')
EVALUATE_SCORE_GOALS.append([MAX])
EVALUATE_SCORE_NAMES.append(['score_volume'])
EVALUATE_ANIMS.append([])
EVALUATE_CONDS.append(Condition().exists(PHENOTYPE).not_exists('score_volume').get())
EVALUATE_ARGS.append(['hython', 'tasks.py', 'evaluate', '1'])
scores_meta.append(ScoreMeta('score_volume', MAX))

#FEEDBACK
FEEDBACK_NAME = 'feedback'
FEEDBACK_INPUT_SIZE = 20
FITNESS_TYPE = PARETO_GOLDBERG_RANKING
NUM_DEATHS = 2
DEATHS_SELECT_TYPE = WORST
NUM_BIRTHS = 2
BIRTHS_SELECT_TYPE = BEST
MUTATION_PROB = 0.1
CROSSOVER_PROB = 0.9
FEEDBACK_COND = Condition().equals(ALIVE,True).exists('score_area').exists('score_volume').get()
FEEDBACK_ARGS = ['python', 'tasks.py', 'feedback']

#TERMINATE
TERMINATE_NAME = 'terminate'
MAX_BIRTHS = 1000
TERMINATE_ARGS = ['python', 'tasks.py', 'terminate']

#GENOTYPE
genotype_meta.append(GeneFloatRange(0.0,10.0))
genotype_meta.append(GeneFloatRange(0.0,10.0))
genotype_meta.append(GeneFloatRange(0.0,10.0))
