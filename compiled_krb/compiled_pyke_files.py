# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc_simple_rules.krb'):
           [1683809349.328528, 'bc_simple_rules_bc.py'],
         ('', '', 'malaria_diagnosis_rule_questions.krb'):
           [1683809349.3354619, 'malaria_diagnosis_rule_questions_bc.py'],
         ('', '', 'questions.kqb'):
           [1683809349.3499398, 'questions.qbc'],
         ('', '', 'facts.kfb'):
           [1683809349.3553686, 'facts.fbc'],
        },
        compiler_version)

