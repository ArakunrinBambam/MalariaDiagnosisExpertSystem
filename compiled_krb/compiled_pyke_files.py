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
         ('', '', 'malaria_diagnosis_rule_questions.krb'):
           [1683997531.578397, 'malaria_diagnosis_rule_questions_fc.py', 'malaria_diagnosis_rule_questions_bc.py'],
         ('', '', 'bc_simple_rules.krb'):
           [1683997531.583869, 'bc_simple_rules_bc.py'],
         ('', '', 'questions.kqb'):
           [1683997531.594469, 'questions.qbc'],
         ('', '', 'facts.kfb'):
           [1683997531.5973105, 'facts.fbc'],
        },
        compiler_version)

