# malaria_diagnosis_rule_questions_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def infant_case1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case1: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case1: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case1: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case1: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case2: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case2: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case2: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case2: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case3: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case3: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case3: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case3: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case4: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case4: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case4: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case4: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case5: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case5: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case5: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case5: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case6: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case6: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case6: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case6: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case7(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case7: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case7: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case7: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case7: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case8(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case8: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case8: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case8: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case8: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case9(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case9: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case9: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case9: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case9: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case10(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case10: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case10: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case10: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case10: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case11(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case11: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case11: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case11: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case11: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case12: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case12: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case12: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case12: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case13(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case13: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case13: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case13: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case13: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case14(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case14: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case14: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case14: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case14: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case15(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case15: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case15: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case15: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case15: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def infant_case16(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'poor_feeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.infant_case16: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.infant_case16: got unexpected plan from when clause 2"
                with engine.prove('facts', 'is_restless', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.infant_case16: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fever', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.infant_case16: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case1: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case1: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case1: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case1: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case1: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case1: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case1: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case1: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case2: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case2: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case2: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case2: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case2: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case2: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case2: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case2: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case3: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case3: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case3: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case3: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case3: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case3: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case3: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case3: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case4: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case4: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case4: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case4: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case4: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case4: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case4: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case4: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case5: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case5: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case5: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case5: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case5: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case5: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case5: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case5: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case6: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case6: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case6: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case6: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case6: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case6: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case6: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case6: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case7(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case7: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case7: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case7: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case7: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case7: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case7: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case7: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case7: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case8(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case8: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case8: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case8: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case8: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case8: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case8: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case8: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case8: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case9(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case9: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case9: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case9: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case9: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case9: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case9: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case9: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case9: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case10(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case10: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case10: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case10: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case10: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case10: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case10: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case10: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case10: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case11(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case11: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case11: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case11: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case11: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case11: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case11: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case11: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case11: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case12: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case12: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case12: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case12: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case12: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case12: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case12: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case12: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case13(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case13: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case13: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case13: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case13: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case13: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case13: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case13: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case13: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case14(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case14: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case14: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case14: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case14: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case14: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case14: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case14: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case14: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case15(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case15: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case15: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case15: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case15: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case15: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case15: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case15: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case15: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case16(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case16: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case16: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case16: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case16: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case16: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case16: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case16: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case16: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case17(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case17: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case17: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case17: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case17: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case17: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case17: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case17: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case17: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case18(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case18: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case18: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case18: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case18: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case18: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case18: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case18: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case18: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case19(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case19: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case19: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case19: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case19: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case19: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case19: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case19: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case19: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case20(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case20: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case20: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case20: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case20: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case20: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case20: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case20: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case20: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case21(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case21: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case21: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case21: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case21: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case21: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case21: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case21: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case21: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case22(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case22: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case22: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case22: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case22: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case22: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case22: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case22: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case22: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case23(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case23: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case23: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case23: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case23: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case23: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case23: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case23: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case23: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case24(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case24: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case24: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case24: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case24: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case24: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case24: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case24: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case24: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case25(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case25: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case25: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case25: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case25: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case25: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case25: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case25: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case25: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case26(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case26: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case26: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case26: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case26: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case26: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case26: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case26: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case26: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case27(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case27: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case27: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case27: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case27: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case27: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case27: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case27: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case27: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case28(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case28: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case28: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case28: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case28: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case28: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case28: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case28: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case28: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case29(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case29: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case29: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case29: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case29: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case29: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case29: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case29: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case29: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case30(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case30: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case30: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case30: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case30: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case30: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case30: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case30: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case30: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case31(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case31: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case31: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case31: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case31: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case31: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case31: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case31: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case31: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case32(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case32: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case32: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case32: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case32: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case32: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case32: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case32: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case32: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case33(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case33: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case33: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case33: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case33: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case33: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case33: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case33: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case33: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case35(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case35: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case35: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case35: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case35: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case35: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case35: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case35: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case35: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case36(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case36: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case36: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case36: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case36: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case36: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case36: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case36: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case36: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case37(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case37: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case37: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case37: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case37: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case37: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case37: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case37: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case37: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case39(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case39: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case39: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case39: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case39: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case39: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case39: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case39: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case39: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case40(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case40: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case40: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case40: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case40: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case40: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case40: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case40: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case40: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case41(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case41: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case41: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case41: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case41: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case41: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case41: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case41: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case41: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case42(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case42: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case42: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case42: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case42: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case42: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case42: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case42: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case42: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case43(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case43: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case43: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case43: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case43: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case43: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case43: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case43: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case43: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case44(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case44: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case44: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case44: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case44: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case44: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case44: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case44: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case44: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case45(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case45: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case45: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case45: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case45: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case45: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case45: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case45: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case45: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case46(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case46: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case46: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case46: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case46: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case46: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case46: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case46: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case46: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case47(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case47: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case47: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case47: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case47: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case47: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case47: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case47: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case47: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case48(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case48: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case48: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case48: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case48: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case48: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case48: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case48: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case48: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case49(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case49: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case49: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case49: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case49: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case49: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case49: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case49: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case49: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case50(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case50: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case50: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case50: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case50: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case50: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case50: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case50: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case50: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case51(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case51: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case51: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case51: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case51: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case51: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case51: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case51: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case51: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case52(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case52: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case52: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case52: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case52: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case52: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case52: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case52: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case52: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case53(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case53: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case53: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case53: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case53: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case53: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case53: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case53: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case53: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case54(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case54: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case54: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case54: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case54: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case54: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case54: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case54: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case54: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case55(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case55: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case55: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case55: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case55: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case55: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case55: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case55: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case55: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case56(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case56: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case56: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case56: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case56: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case56: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case56: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case56: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case56: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def adult_case57(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'has_loss_of_apetite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "malaria_diagnosis_rule_questions.adult_case57: got unexpected plan from when clause 1"
            with engine.prove('facts', 'is_vomiting', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "malaria_diagnosis_rule_questions.adult_case57: got unexpected plan from when clause 2"
                with engine.prove('facts', 'has_yellowish_skin', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "malaria_diagnosis_rule_questions.adult_case57: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'has_fatigue', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "malaria_diagnosis_rule_questions.adult_case57: got unexpected plan from when clause 4"
                        with engine.prove('facts', 'has_headache', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "malaria_diagnosis_rule_questions.adult_case57: got unexpected plan from when clause 5"
                            with engine.prove('facts', 'has_pain_in_joint_and_muscles', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "malaria_diagnosis_rule_questions.adult_case57: got unexpected plan from when clause 6"
                                with engine.prove('facts', 'has_chills', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "malaria_diagnosis_rule_questions.adult_case57: got unexpected plan from when clause 7"
                                    with engine.prove('facts', 'has_fever', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "malaria_diagnosis_rule_questions.adult_case57: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('malaria_diagnosis_rule_questions')
  
  bc_rule.bc_rule('infant_case1', This_rule_base, 'diagnosis_result',
                  infant_case1, None,
                  (pattern.pattern_literal("It doesn't appear that the child is malaria infected. However, you can contact doctor your doctor if you feel this response is not fine"),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('infant_case2', This_rule_base, 'diagnosis_result',
                  infant_case2, None,
                  (pattern.pattern_literal("It's uncertain that the child has malaria, Consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('infant_case3', This_rule_base, 'diagnosis_result',
                  infant_case3, None,
                  (pattern.pattern_literal("It's uncertain that the child has malaria, Consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('infant_case4', This_rule_base, 'diagnosis_result',
                  infant_case4, None,
                  (pattern.pattern_literal("It's uncertain that the child has malaria, Consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('infant_case5', This_rule_base, 'diagnosis_result',
                  infant_case5, None,
                  (pattern.pattern_literal("Fever is a strong symptoms of malaria. HOwever, consult your doctor for further medical care"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('infant_case6', This_rule_base, 'diagnosis_result',
                  infant_case6, None,
                  (pattern.pattern_literal("It's likely the baby has malaria, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('infant_case7', This_rule_base, 'diagnosis_result',
                  infant_case7, None,
                  (pattern.pattern_literal("It's likely the baby has malaria, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('infant_case8', This_rule_base, 'diagnosis_result',
                  infant_case8, None,
                  (pattern.pattern_literal("It's likely the baby has malaria, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('infant_case9', This_rule_base, 'diagnosis_result',
                  infant_case9, None,
                  (pattern.pattern_literal("It's likely the baby has malaria, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('infant_case10', This_rule_base, 'diagnosis_result',
                  infant_case10, None,
                  (pattern.pattern_literal("It's likely the baby has malaria, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('infant_case11', This_rule_base, 'diagnosis_result',
                  infant_case11, None,
                  (pattern.pattern_literal("It's likely the baby has malaria, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('infant_case12', This_rule_base, 'diagnosis_result',
                  infant_case12, None,
                  (pattern.pattern_literal("There is high chance the baby has malaria, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('infant_case13', This_rule_base, 'diagnosis_result',
                  infant_case13, None,
                  (pattern.pattern_literal("There is high chance the baby has malaria, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('infant_case14', This_rule_base, 'diagnosis_result',
                  infant_case14, None,
                  (pattern.pattern_literal("There is high chance the baby has malaria, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('infant_case15', This_rule_base, 'diagnosis_result',
                  infant_case15, None,
                  (pattern.pattern_literal("There is high chance the baby has malaria, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('infant_case16', This_rule_base, 'diagnosis_result',
                  infant_case16, None,
                  (pattern.pattern_literal("There is high chance the baby has malaria, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case1', This_rule_base, 'diagnosis_result',
                  adult_case1, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case2', This_rule_base, 'diagnosis_result',
                  adult_case2, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case3', This_rule_base, 'diagnosis_result',
                  adult_case3, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case4', This_rule_base, 'diagnosis_result',
                  adult_case4, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case5', This_rule_base, 'diagnosis_result',
                  adult_case5, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case6', This_rule_base, 'diagnosis_result',
                  adult_case6, None,
                  (pattern.pattern_literal("There is high chance the baby has malaria, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case7', This_rule_base, 'diagnosis_result',
                  adult_case7, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case8', This_rule_base, 'diagnosis_result',
                  adult_case8, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case9', This_rule_base, 'diagnosis_result',
                  adult_case9, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case10', This_rule_base, 'diagnosis_result',
                  adult_case10, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case11', This_rule_base, 'diagnosis_result',
                  adult_case11, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case12', This_rule_base, 'diagnosis_result',
                  adult_case12, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case13', This_rule_base, 'diagnosis_result',
                  adult_case13, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case14', This_rule_base, 'diagnosis_result',
                  adult_case14, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case15', This_rule_base, 'diagnosis_result',
                  adult_case15, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case16', This_rule_base, 'diagnosis_result',
                  adult_case16, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case17', This_rule_base, 'diagnosis_result',
                  adult_case17, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case18', This_rule_base, 'diagnosis_result',
                  adult_case18, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case19', This_rule_base, 'diagnosis_result',
                  adult_case19, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case20', This_rule_base, 'diagnosis_result',
                  adult_case20, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case21', This_rule_base, 'diagnosis_result',
                  adult_case21, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case22', This_rule_base, 'diagnosis_result',
                  adult_case22, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case23', This_rule_base, 'diagnosis_result',
                  adult_case23, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case24', This_rule_base, 'diagnosis_result',
                  adult_case24, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case25', This_rule_base, 'diagnosis_result',
                  adult_case25, None,
                  (pattern.pattern_literal("It's likely you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case26', This_rule_base, 'diagnosis_result',
                  adult_case26, None,
                  (pattern.pattern_literal("It's likely you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case27', This_rule_base, 'diagnosis_result',
                  adult_case27, None,
                  (pattern.pattern_literal("It's likely you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case28', This_rule_base, 'diagnosis_result',
                  adult_case28, None,
                  (pattern.pattern_literal("It's likely you are malaria infected, please consult your doctorr"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case29', This_rule_base, 'diagnosis_result',
                  adult_case29, None,
                  (pattern.pattern_literal("It's likely you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case30', This_rule_base, 'diagnosis_result',
                  adult_case30, None,
                  (pattern.pattern_literal("yellowish skin is a sign of possible malaria infection, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case31', This_rule_base, 'diagnosis_result',
                  adult_case31, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case32', This_rule_base, 'diagnosis_result',
                  adult_case32, None,
                  (pattern.pattern_literal("fever is a sign of possible malaria infection, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case33', This_rule_base, 'diagnosis_result',
                  adult_case33, None,
                  (pattern.pattern_literal("It appears you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case35', This_rule_base, 'diagnosis_result',
                  adult_case35, None,
                  (pattern.pattern_literal("It's unclear you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case36', This_rule_base, 'diagnosis_result',
                  adult_case36, None,
                  (pattern.pattern_literal("fever is a sign of possible malaria infection, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case37', This_rule_base, 'diagnosis_result',
                  adult_case37, None,
                  (pattern.pattern_literal("fever is a strong sign of possible malaria infection, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case39', This_rule_base, 'diagnosis_result',
                  adult_case39, None,
                  (pattern.pattern_literal("It appears you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case40', This_rule_base, 'diagnosis_result',
                  adult_case40, None,
                  (pattern.pattern_literal("fever is a sign of possible malaria infection, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case41', This_rule_base, 'diagnosis_result',
                  adult_case41, None,
                  (pattern.pattern_literal("fever is a sign of possible malaria infection, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case42', This_rule_base, 'diagnosis_result',
                  adult_case42, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case43', This_rule_base, 'diagnosis_result',
                  adult_case43, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case44', This_rule_base, 'diagnosis_result',
                  adult_case44, None,
                  (pattern.pattern_literal("It's unclear you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case45', This_rule_base, 'diagnosis_result',
                  adult_case45, None,
                  (pattern.pattern_literal("yellowish skin is a sign of possible malaria infection, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case46', This_rule_base, 'diagnosis_result',
                  adult_case46, None,
                  (pattern.pattern_literal("fever is a sign of possible malaria infection, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case47', This_rule_base, 'diagnosis_result',
                  adult_case47, None,
                  (pattern.pattern_literal("fever is a sign of possible malaria infection, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case48', This_rule_base, 'diagnosis_result',
                  adult_case48, None,
                  (pattern.pattern_literal("It appears you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case49', This_rule_base, 'diagnosis_result',
                  adult_case49, None,
                  (pattern.pattern_literal("It's unclear you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case50', This_rule_base, 'diagnosis_result',
                  adult_case50, None,
                  (pattern.pattern_literal("fever is a sign of possible malaria infection, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case51', This_rule_base, 'diagnosis_result',
                  adult_case51, None,
                  (pattern.pattern_literal("It does not appear you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case52', This_rule_base, 'diagnosis_result',
                  adult_case52, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case53', This_rule_base, 'diagnosis_result',
                  adult_case53, None,
                  (pattern.pattern_literal("fever is a sign of possible malaria infection, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case54', This_rule_base, 'diagnosis_result',
                  adult_case54, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case55', This_rule_base, 'diagnosis_result',
                  adult_case55, None,
                  (pattern.pattern_literal("It appears you are malaria infected, please consult your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('adult_case56', This_rule_base, 'diagnosis_result',
                  adult_case56, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('adult_case57', This_rule_base, 'diagnosis_result',
                  adult_case57, None,
                  (pattern.pattern_literal("There is high chance you are malaria infected, please see your doctor"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))


Krb_filename = '../malaria_diagnosis_rule_questions.krb'
Krb_lineno_map = (
    ((14, 18), (163, 163)),
    ((20, 25), (165, 165)),
    ((26, 31), (166, 166)),
    ((32, 37), (167, 167)),
    ((38, 43), (168, 168)),
    ((56, 60), (171, 171)),
    ((62, 67), (173, 173)),
    ((68, 73), (174, 174)),
    ((74, 79), (175, 175)),
    ((80, 85), (176, 176)),
    ((98, 102), (179, 179)),
    ((104, 109), (181, 181)),
    ((110, 115), (182, 182)),
    ((116, 121), (183, 183)),
    ((122, 127), (184, 184)),
    ((140, 144), (187, 187)),
    ((146, 151), (189, 189)),
    ((152, 157), (190, 190)),
    ((158, 163), (191, 191)),
    ((164, 169), (192, 192)),
    ((182, 186), (195, 195)),
    ((188, 193), (197, 197)),
    ((194, 199), (198, 198)),
    ((200, 205), (199, 199)),
    ((206, 211), (200, 200)),
    ((224, 228), (203, 203)),
    ((230, 235), (205, 205)),
    ((236, 241), (206, 206)),
    ((242, 247), (207, 207)),
    ((248, 253), (208, 208)),
    ((266, 270), (211, 211)),
    ((272, 277), (213, 213)),
    ((278, 283), (214, 214)),
    ((284, 289), (215, 215)),
    ((290, 295), (216, 216)),
    ((308, 312), (219, 219)),
    ((314, 319), (221, 221)),
    ((320, 325), (222, 222)),
    ((326, 331), (223, 223)),
    ((332, 337), (224, 224)),
    ((350, 354), (227, 227)),
    ((356, 361), (229, 229)),
    ((362, 367), (230, 230)),
    ((368, 373), (231, 231)),
    ((374, 379), (232, 232)),
    ((392, 396), (235, 235)),
    ((398, 403), (237, 237)),
    ((404, 409), (238, 238)),
    ((410, 415), (239, 239)),
    ((416, 421), (240, 240)),
    ((434, 438), (243, 243)),
    ((440, 445), (245, 245)),
    ((446, 451), (246, 246)),
    ((452, 457), (247, 247)),
    ((458, 463), (248, 248)),
    ((476, 480), (251, 251)),
    ((482, 487), (253, 253)),
    ((488, 493), (254, 254)),
    ((494, 499), (255, 255)),
    ((500, 505), (256, 256)),
    ((518, 522), (259, 259)),
    ((524, 529), (261, 261)),
    ((530, 535), (262, 262)),
    ((536, 541), (263, 263)),
    ((542, 547), (264, 264)),
    ((560, 564), (267, 267)),
    ((566, 571), (269, 269)),
    ((572, 577), (270, 270)),
    ((578, 583), (271, 271)),
    ((584, 589), (272, 272)),
    ((602, 606), (275, 275)),
    ((608, 613), (277, 277)),
    ((614, 619), (278, 278)),
    ((620, 625), (279, 279)),
    ((626, 631), (280, 280)),
    ((644, 648), (284, 284)),
    ((650, 655), (286, 286)),
    ((656, 661), (287, 287)),
    ((662, 667), (288, 288)),
    ((668, 673), (289, 289)),
    ((686, 690), (299, 299)),
    ((692, 697), (301, 301)),
    ((698, 703), (302, 302)),
    ((704, 709), (303, 303)),
    ((710, 715), (304, 304)),
    ((716, 721), (305, 305)),
    ((722, 727), (306, 306)),
    ((728, 733), (307, 307)),
    ((734, 739), (308, 308)),
    ((752, 756), (311, 311)),
    ((758, 763), (313, 313)),
    ((764, 769), (314, 314)),
    ((770, 775), (315, 315)),
    ((776, 781), (316, 316)),
    ((782, 787), (317, 317)),
    ((788, 793), (318, 318)),
    ((794, 799), (319, 319)),
    ((800, 805), (320, 320)),
    ((818, 822), (324, 324)),
    ((824, 829), (326, 326)),
    ((830, 835), (327, 327)),
    ((836, 841), (328, 328)),
    ((842, 847), (329, 329)),
    ((848, 853), (330, 330)),
    ((854, 859), (331, 331)),
    ((860, 865), (332, 332)),
    ((866, 871), (333, 333)),
    ((884, 888), (336, 336)),
    ((890, 895), (338, 338)),
    ((896, 901), (339, 339)),
    ((902, 907), (340, 340)),
    ((908, 913), (341, 341)),
    ((914, 919), (342, 342)),
    ((920, 925), (343, 343)),
    ((926, 931), (344, 344)),
    ((932, 937), (345, 345)),
    ((950, 954), (348, 348)),
    ((956, 961), (350, 350)),
    ((962, 967), (351, 351)),
    ((968, 973), (352, 352)),
    ((974, 979), (353, 353)),
    ((980, 985), (354, 354)),
    ((986, 991), (355, 355)),
    ((992, 997), (356, 356)),
    ((998, 1003), (357, 357)),
    ((1016, 1020), (360, 360)),
    ((1022, 1027), (362, 362)),
    ((1028, 1033), (363, 363)),
    ((1034, 1039), (364, 364)),
    ((1040, 1045), (365, 365)),
    ((1046, 1051), (366, 366)),
    ((1052, 1057), (367, 367)),
    ((1058, 1063), (368, 368)),
    ((1064, 1069), (369, 369)),
    ((1082, 1086), (372, 372)),
    ((1088, 1093), (374, 374)),
    ((1094, 1099), (375, 375)),
    ((1100, 1105), (376, 376)),
    ((1106, 1111), (377, 377)),
    ((1112, 1117), (378, 378)),
    ((1118, 1123), (379, 379)),
    ((1124, 1129), (380, 380)),
    ((1130, 1135), (381, 381)),
    ((1148, 1152), (384, 384)),
    ((1154, 1159), (386, 386)),
    ((1160, 1165), (387, 387)),
    ((1166, 1171), (388, 388)),
    ((1172, 1177), (389, 389)),
    ((1178, 1183), (390, 390)),
    ((1184, 1189), (391, 391)),
    ((1190, 1195), (392, 392)),
    ((1196, 1201), (393, 393)),
    ((1214, 1218), (396, 396)),
    ((1220, 1225), (398, 398)),
    ((1226, 1231), (399, 399)),
    ((1232, 1237), (400, 400)),
    ((1238, 1243), (401, 401)),
    ((1244, 1249), (402, 402)),
    ((1250, 1255), (403, 403)),
    ((1256, 1261), (404, 404)),
    ((1262, 1267), (405, 405)),
    ((1280, 1284), (408, 408)),
    ((1286, 1291), (410, 410)),
    ((1292, 1297), (411, 411)),
    ((1298, 1303), (412, 412)),
    ((1304, 1309), (413, 413)),
    ((1310, 1315), (414, 414)),
    ((1316, 1321), (415, 415)),
    ((1322, 1327), (416, 416)),
    ((1328, 1333), (417, 417)),
    ((1346, 1350), (420, 420)),
    ((1352, 1357), (422, 422)),
    ((1358, 1363), (423, 423)),
    ((1364, 1369), (424, 424)),
    ((1370, 1375), (425, 425)),
    ((1376, 1381), (426, 426)),
    ((1382, 1387), (427, 427)),
    ((1388, 1393), (428, 428)),
    ((1394, 1399), (429, 429)),
    ((1412, 1416), (432, 432)),
    ((1418, 1423), (434, 434)),
    ((1424, 1429), (435, 435)),
    ((1430, 1435), (436, 436)),
    ((1436, 1441), (437, 437)),
    ((1442, 1447), (438, 438)),
    ((1448, 1453), (439, 439)),
    ((1454, 1459), (440, 440)),
    ((1460, 1465), (441, 441)),
    ((1478, 1482), (444, 444)),
    ((1484, 1489), (446, 446)),
    ((1490, 1495), (447, 447)),
    ((1496, 1501), (448, 448)),
    ((1502, 1507), (449, 449)),
    ((1508, 1513), (450, 450)),
    ((1514, 1519), (451, 451)),
    ((1520, 1525), (452, 452)),
    ((1526, 1531), (453, 453)),
    ((1544, 1548), (456, 456)),
    ((1550, 1555), (458, 458)),
    ((1556, 1561), (459, 459)),
    ((1562, 1567), (460, 460)),
    ((1568, 1573), (461, 461)),
    ((1574, 1579), (462, 462)),
    ((1580, 1585), (463, 463)),
    ((1586, 1591), (464, 464)),
    ((1592, 1597), (465, 465)),
    ((1610, 1614), (468, 468)),
    ((1616, 1621), (470, 470)),
    ((1622, 1627), (471, 471)),
    ((1628, 1633), (472, 472)),
    ((1634, 1639), (473, 473)),
    ((1640, 1645), (474, 474)),
    ((1646, 1651), (475, 475)),
    ((1652, 1657), (476, 476)),
    ((1658, 1663), (477, 477)),
    ((1676, 1680), (480, 480)),
    ((1682, 1687), (482, 482)),
    ((1688, 1693), (483, 483)),
    ((1694, 1699), (484, 484)),
    ((1700, 1705), (485, 485)),
    ((1706, 1711), (486, 486)),
    ((1712, 1717), (487, 487)),
    ((1718, 1723), (488, 488)),
    ((1724, 1729), (489, 489)),
    ((1742, 1746), (492, 492)),
    ((1748, 1753), (494, 494)),
    ((1754, 1759), (495, 495)),
    ((1760, 1765), (496, 496)),
    ((1766, 1771), (497, 497)),
    ((1772, 1777), (498, 498)),
    ((1778, 1783), (499, 499)),
    ((1784, 1789), (500, 500)),
    ((1790, 1795), (501, 501)),
    ((1808, 1812), (504, 504)),
    ((1814, 1819), (506, 506)),
    ((1820, 1825), (507, 507)),
    ((1826, 1831), (508, 508)),
    ((1832, 1837), (509, 509)),
    ((1838, 1843), (510, 510)),
    ((1844, 1849), (511, 511)),
    ((1850, 1855), (512, 512)),
    ((1856, 1861), (513, 513)),
    ((1874, 1878), (516, 516)),
    ((1880, 1885), (518, 518)),
    ((1886, 1891), (519, 519)),
    ((1892, 1897), (520, 520)),
    ((1898, 1903), (521, 521)),
    ((1904, 1909), (522, 522)),
    ((1910, 1915), (523, 523)),
    ((1916, 1921), (524, 524)),
    ((1922, 1927), (525, 525)),
    ((1940, 1944), (528, 528)),
    ((1946, 1951), (530, 530)),
    ((1952, 1957), (531, 531)),
    ((1958, 1963), (532, 532)),
    ((1964, 1969), (533, 533)),
    ((1970, 1975), (534, 534)),
    ((1976, 1981), (535, 535)),
    ((1982, 1987), (536, 536)),
    ((1988, 1993), (537, 537)),
    ((2006, 2010), (540, 540)),
    ((2012, 2017), (542, 542)),
    ((2018, 2023), (543, 543)),
    ((2024, 2029), (544, 544)),
    ((2030, 2035), (545, 545)),
    ((2036, 2041), (546, 546)),
    ((2042, 2047), (547, 547)),
    ((2048, 2053), (548, 548)),
    ((2054, 2059), (549, 549)),
    ((2072, 2076), (552, 552)),
    ((2078, 2083), (554, 554)),
    ((2084, 2089), (555, 555)),
    ((2090, 2095), (556, 556)),
    ((2096, 2101), (557, 557)),
    ((2102, 2107), (558, 558)),
    ((2108, 2113), (559, 559)),
    ((2114, 2119), (560, 560)),
    ((2120, 2125), (561, 561)),
    ((2138, 2142), (564, 564)),
    ((2144, 2149), (566, 566)),
    ((2150, 2155), (567, 567)),
    ((2156, 2161), (568, 568)),
    ((2162, 2167), (569, 569)),
    ((2168, 2173), (570, 570)),
    ((2174, 2179), (571, 571)),
    ((2180, 2185), (572, 572)),
    ((2186, 2191), (573, 573)),
    ((2204, 2208), (576, 576)),
    ((2210, 2215), (578, 578)),
    ((2216, 2221), (579, 579)),
    ((2222, 2227), (580, 580)),
    ((2228, 2233), (581, 581)),
    ((2234, 2239), (582, 582)),
    ((2240, 2245), (583, 583)),
    ((2246, 2251), (584, 584)),
    ((2252, 2257), (585, 585)),
    ((2270, 2274), (588, 588)),
    ((2276, 2281), (590, 590)),
    ((2282, 2287), (591, 591)),
    ((2288, 2293), (592, 592)),
    ((2294, 2299), (593, 593)),
    ((2300, 2305), (594, 594)),
    ((2306, 2311), (595, 595)),
    ((2312, 2317), (596, 596)),
    ((2318, 2323), (597, 597)),
    ((2336, 2340), (600, 600)),
    ((2342, 2347), (602, 602)),
    ((2348, 2353), (603, 603)),
    ((2354, 2359), (604, 604)),
    ((2360, 2365), (605, 605)),
    ((2366, 2371), (606, 606)),
    ((2372, 2377), (607, 607)),
    ((2378, 2383), (608, 608)),
    ((2384, 2389), (609, 609)),
    ((2402, 2406), (612, 612)),
    ((2408, 2413), (614, 614)),
    ((2414, 2419), (615, 615)),
    ((2420, 2425), (616, 616)),
    ((2426, 2431), (617, 617)),
    ((2432, 2437), (618, 618)),
    ((2438, 2443), (619, 619)),
    ((2444, 2449), (620, 620)),
    ((2450, 2455), (621, 621)),
    ((2468, 2472), (624, 624)),
    ((2474, 2479), (626, 626)),
    ((2480, 2485), (627, 627)),
    ((2486, 2491), (628, 628)),
    ((2492, 2497), (629, 629)),
    ((2498, 2503), (630, 630)),
    ((2504, 2509), (631, 631)),
    ((2510, 2515), (632, 632)),
    ((2516, 2521), (633, 633)),
    ((2534, 2538), (636, 636)),
    ((2540, 2545), (638, 638)),
    ((2546, 2551), (639, 639)),
    ((2552, 2557), (640, 640)),
    ((2558, 2563), (641, 641)),
    ((2564, 2569), (642, 642)),
    ((2570, 2575), (643, 643)),
    ((2576, 2581), (644, 644)),
    ((2582, 2587), (645, 645)),
    ((2600, 2604), (648, 648)),
    ((2606, 2611), (650, 650)),
    ((2612, 2617), (651, 651)),
    ((2618, 2623), (652, 652)),
    ((2624, 2629), (653, 653)),
    ((2630, 2635), (654, 654)),
    ((2636, 2641), (655, 655)),
    ((2642, 2647), (656, 656)),
    ((2648, 2653), (657, 657)),
    ((2666, 2670), (660, 660)),
    ((2672, 2677), (662, 662)),
    ((2678, 2683), (663, 663)),
    ((2684, 2689), (664, 664)),
    ((2690, 2695), (665, 665)),
    ((2696, 2701), (666, 666)),
    ((2702, 2707), (667, 667)),
    ((2708, 2713), (668, 668)),
    ((2714, 2719), (669, 669)),
    ((2732, 2736), (672, 672)),
    ((2738, 2743), (674, 674)),
    ((2744, 2749), (675, 675)),
    ((2750, 2755), (676, 676)),
    ((2756, 2761), (677, 677)),
    ((2762, 2767), (678, 678)),
    ((2768, 2773), (679, 679)),
    ((2774, 2779), (680, 680)),
    ((2780, 2785), (681, 681)),
    ((2798, 2802), (685, 685)),
    ((2804, 2809), (687, 687)),
    ((2810, 2815), (688, 688)),
    ((2816, 2821), (689, 689)),
    ((2822, 2827), (690, 690)),
    ((2828, 2833), (691, 691)),
    ((2834, 2839), (692, 692)),
    ((2840, 2845), (693, 693)),
    ((2846, 2851), (694, 694)),
    ((2864, 2868), (698, 698)),
    ((2870, 2875), (700, 700)),
    ((2876, 2881), (701, 701)),
    ((2882, 2887), (702, 702)),
    ((2888, 2893), (703, 703)),
    ((2894, 2899), (704, 704)),
    ((2900, 2905), (705, 705)),
    ((2906, 2911), (706, 706)),
    ((2912, 2917), (707, 707)),
    ((2930, 2934), (710, 710)),
    ((2936, 2941), (712, 712)),
    ((2942, 2947), (713, 713)),
    ((2948, 2953), (714, 714)),
    ((2954, 2959), (715, 715)),
    ((2960, 2965), (716, 716)),
    ((2966, 2971), (717, 717)),
    ((2972, 2977), (718, 718)),
    ((2978, 2983), (719, 719)),
    ((2996, 3000), (722, 722)),
    ((3002, 3007), (724, 724)),
    ((3008, 3013), (725, 725)),
    ((3014, 3019), (726, 726)),
    ((3020, 3025), (727, 727)),
    ((3026, 3031), (728, 728)),
    ((3032, 3037), (729, 729)),
    ((3038, 3043), (730, 730)),
    ((3044, 3049), (731, 731)),
    ((3062, 3066), (735, 735)),
    ((3068, 3073), (737, 737)),
    ((3074, 3079), (738, 738)),
    ((3080, 3085), (739, 739)),
    ((3086, 3091), (740, 740)),
    ((3092, 3097), (741, 741)),
    ((3098, 3103), (742, 742)),
    ((3104, 3109), (743, 743)),
    ((3110, 3115), (744, 744)),
    ((3128, 3132), (747, 747)),
    ((3134, 3139), (749, 749)),
    ((3140, 3145), (750, 750)),
    ((3146, 3151), (751, 751)),
    ((3152, 3157), (752, 752)),
    ((3158, 3163), (753, 753)),
    ((3164, 3169), (754, 754)),
    ((3170, 3175), (755, 755)),
    ((3176, 3181), (756, 756)),
    ((3194, 3198), (759, 759)),
    ((3200, 3205), (761, 761)),
    ((3206, 3211), (762, 762)),
    ((3212, 3217), (763, 763)),
    ((3218, 3223), (764, 764)),
    ((3224, 3229), (765, 765)),
    ((3230, 3235), (766, 766)),
    ((3236, 3241), (767, 767)),
    ((3242, 3247), (768, 768)),
    ((3260, 3264), (771, 771)),
    ((3266, 3271), (773, 773)),
    ((3272, 3277), (774, 774)),
    ((3278, 3283), (775, 775)),
    ((3284, 3289), (776, 776)),
    ((3290, 3295), (777, 777)),
    ((3296, 3301), (778, 778)),
    ((3302, 3307), (779, 779)),
    ((3308, 3313), (780, 780)),
    ((3326, 3330), (783, 783)),
    ((3332, 3337), (785, 785)),
    ((3338, 3343), (786, 786)),
    ((3344, 3349), (787, 787)),
    ((3350, 3355), (788, 788)),
    ((3356, 3361), (789, 789)),
    ((3362, 3367), (790, 790)),
    ((3368, 3373), (791, 791)),
    ((3374, 3379), (792, 792)),
    ((3392, 3396), (795, 795)),
    ((3398, 3403), (797, 797)),
    ((3404, 3409), (798, 798)),
    ((3410, 3415), (799, 799)),
    ((3416, 3421), (800, 800)),
    ((3422, 3427), (801, 801)),
    ((3428, 3433), (802, 802)),
    ((3434, 3439), (803, 803)),
    ((3440, 3445), (804, 804)),
    ((3458, 3462), (807, 807)),
    ((3464, 3469), (809, 809)),
    ((3470, 3475), (810, 810)),
    ((3476, 3481), (811, 811)),
    ((3482, 3487), (812, 812)),
    ((3488, 3493), (813, 813)),
    ((3494, 3499), (814, 814)),
    ((3500, 3505), (815, 815)),
    ((3506, 3511), (816, 816)),
    ((3524, 3528), (819, 819)),
    ((3530, 3535), (821, 821)),
    ((3536, 3541), (822, 822)),
    ((3542, 3547), (823, 823)),
    ((3548, 3553), (824, 824)),
    ((3554, 3559), (825, 825)),
    ((3560, 3565), (826, 826)),
    ((3566, 3571), (827, 827)),
    ((3572, 3577), (828, 828)),
    ((3590, 3594), (831, 831)),
    ((3596, 3601), (833, 833)),
    ((3602, 3607), (834, 834)),
    ((3608, 3613), (835, 835)),
    ((3614, 3619), (836, 836)),
    ((3620, 3625), (837, 837)),
    ((3626, 3631), (838, 838)),
    ((3632, 3637), (839, 839)),
    ((3638, 3643), (840, 840)),
    ((3656, 3660), (843, 843)),
    ((3662, 3667), (845, 845)),
    ((3668, 3673), (846, 846)),
    ((3674, 3679), (847, 847)),
    ((3680, 3685), (848, 848)),
    ((3686, 3691), (849, 849)),
    ((3692, 3697), (850, 850)),
    ((3698, 3703), (851, 851)),
    ((3704, 3709), (852, 852)),
    ((3722, 3726), (855, 855)),
    ((3728, 3733), (857, 857)),
    ((3734, 3739), (858, 858)),
    ((3740, 3745), (859, 859)),
    ((3746, 3751), (860, 860)),
    ((3752, 3757), (861, 861)),
    ((3758, 3763), (862, 862)),
    ((3764, 3769), (863, 863)),
    ((3770, 3775), (864, 864)),
    ((3788, 3792), (867, 867)),
    ((3794, 3799), (869, 869)),
    ((3800, 3805), (870, 870)),
    ((3806, 3811), (871, 871)),
    ((3812, 3817), (872, 872)),
    ((3818, 3823), (873, 873)),
    ((3824, 3829), (874, 874)),
    ((3830, 3835), (875, 875)),
    ((3836, 3841), (876, 876)),
    ((3854, 3858), (879, 879)),
    ((3860, 3865), (881, 881)),
    ((3866, 3871), (882, 882)),
    ((3872, 3877), (883, 883)),
    ((3878, 3883), (884, 884)),
    ((3884, 3889), (885, 885)),
    ((3890, 3895), (886, 886)),
    ((3896, 3901), (887, 887)),
    ((3902, 3907), (888, 888)),
    ((3920, 3924), (891, 891)),
    ((3926, 3931), (893, 893)),
    ((3932, 3937), (894, 894)),
    ((3938, 3943), (895, 895)),
    ((3944, 3949), (896, 896)),
    ((3950, 3955), (897, 897)),
    ((3956, 3961), (898, 898)),
    ((3962, 3967), (899, 899)),
    ((3968, 3973), (900, 900)),
    ((3986, 3990), (903, 903)),
    ((3992, 3997), (905, 905)),
    ((3998, 4003), (906, 906)),
    ((4004, 4009), (907, 907)),
    ((4010, 4015), (908, 908)),
    ((4016, 4021), (909, 909)),
    ((4022, 4027), (910, 910)),
    ((4028, 4033), (911, 911)),
    ((4034, 4039), (912, 912)),
    ((4052, 4056), (915, 915)),
    ((4058, 4063), (917, 917)),
    ((4064, 4069), (918, 918)),
    ((4070, 4075), (919, 919)),
    ((4076, 4081), (920, 920)),
    ((4082, 4087), (921, 921)),
    ((4088, 4093), (922, 922)),
    ((4094, 4099), (923, 923)),
    ((4100, 4105), (924, 924)),
    ((4118, 4122), (927, 927)),
    ((4124, 4129), (929, 929)),
    ((4130, 4135), (930, 930)),
    ((4136, 4141), (931, 931)),
    ((4142, 4147), (932, 932)),
    ((4148, 4153), (933, 933)),
    ((4154, 4159), (934, 934)),
    ((4160, 4165), (935, 935)),
    ((4166, 4171), (936, 936)),
    ((4184, 4188), (939, 939)),
    ((4190, 4195), (941, 941)),
    ((4196, 4201), (942, 942)),
    ((4202, 4207), (943, 943)),
    ((4208, 4213), (944, 944)),
    ((4214, 4219), (945, 945)),
    ((4220, 4225), (946, 946)),
    ((4226, 4231), (947, 947)),
    ((4232, 4237), (948, 948)),
    ((4250, 4254), (951, 951)),
    ((4256, 4261), (953, 953)),
    ((4262, 4267), (954, 954)),
    ((4268, 4273), (955, 955)),
    ((4274, 4279), (956, 956)),
    ((4280, 4285), (957, 957)),
    ((4286, 4291), (958, 958)),
    ((4292, 4297), (959, 959)),
    ((4298, 4303), (960, 960)),
)
