import warnings
warnings.warn("Importing grades.management.commands.recalculate_subsection_grades instead of lms.djangoapps.grades.management.commands.recalculate_subsection_grades is deprecated", stacklevel=2)

from lms.djangoapps.grades.management.commands.recalculate_subsection_grades import *
