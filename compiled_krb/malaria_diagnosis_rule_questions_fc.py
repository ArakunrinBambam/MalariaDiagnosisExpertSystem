# malaria_diagnosis_rule_questions_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def check_age(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'age',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_fever(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'has_fever', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'has_fever',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_fever(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'has_fever', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'has_fever',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_poor_feeding(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'poor_feeding', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'poor_feeding',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_poor_feeding(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'poor_feeding', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'poor_feeding',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_restlessness(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'is_restless', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'is_restless',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_restlessness(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'is_restless', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'is_restless',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_vomiting(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'is_vomiting', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'is_vomiting',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_vomiting(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'is_vomiting', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'is_vomiting',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_pain_in_joint_and_muscles(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_pain_in_joint_and_muscles', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_pain_in_joint_and_muscles',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_pain_in_joint_and_muscles(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_pain_in_joint_and_muscles', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_pain_in_joint_and_muscles',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_chills(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_chills', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_chills',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_chills(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_chills', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_chills',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_headache(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_headache', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_headache',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_headache(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_headache', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_headache',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_fatigue(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_fatigue', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_fatigue',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_fatigue(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_fatigue', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_fatigue',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_yellowish_skin(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_yellowish_skin', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_yellowish_skin',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_yellowish_skin(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_yellowish_skin', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_yellowish_skin',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def loss_of_apetite(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_loss_of_apetite', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_loss_of_apetite',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_loss_of_apetite(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'age', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'has_loss_of_apetite', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'has_loss_of_apetite',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('malaria_diagnosis_rule_questions')
  
  fc_rule.fc_rule('check_age', This_rule_base, check_age,
    (('questions', 'age',
      (contexts.variable('ans'),),
      False),),
    (contexts.variable('ans'),))
  
  fc_rule.fc_rule('has_fever', This_rule_base, has_fever,
    (('questions', 'has_fever',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_fever', This_rule_base, no_fever,
    (('questions', 'has_fever',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('has_poor_feeding', This_rule_base, has_poor_feeding,
    (('facts', 'age',
      (pattern.pattern_literal('children'),),
      False),
     ('questions', 'poor_feeding',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_poor_feeding', This_rule_base, no_poor_feeding,
    (('facts', 'age',
      (pattern.pattern_literal('children'),),
      False),
     ('questions', 'poor_feeding',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('has_restlessness', This_rule_base, has_restlessness,
    (('facts', 'age',
      (pattern.pattern_literal('children'),),
      False),
     ('questions', 'is_restless',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_restlessness', This_rule_base, no_restlessness,
    (('facts', 'age',
      (pattern.pattern_literal('children'),),
      False),
     ('questions', 'is_restless',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('has_vomiting', This_rule_base, has_vomiting,
    (('questions', 'is_vomiting',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_vomiting', This_rule_base, no_vomiting,
    (('questions', 'is_vomiting',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('has_pain_in_joint_and_muscles', This_rule_base, has_pain_in_joint_and_muscles,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_pain_in_joint_and_muscles',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_pain_in_joint_and_muscles', This_rule_base, no_pain_in_joint_and_muscles,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_pain_in_joint_and_muscles',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('has_chills', This_rule_base, has_chills,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_chills',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_chills', This_rule_base, no_chills,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_chills',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('has_headache', This_rule_base, has_headache,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_headache',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_headache', This_rule_base, no_headache,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_headache',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('has_fatigue', This_rule_base, has_fatigue,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_fatigue',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_fatigue', This_rule_base, no_fatigue,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_fatigue',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('has_yellowish_skin', This_rule_base, has_yellowish_skin,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_yellowish_skin',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_yellowish_skin', This_rule_base, no_yellowish_skin,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_yellowish_skin',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('loss_of_apetite', This_rule_base, loss_of_apetite,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_loss_of_apetite',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_loss_of_apetite', This_rule_base, no_loss_of_apetite,
    (('facts', 'age',
      (pattern.pattern_literal('adult'),),
      False),
     ('questions', 'has_loss_of_apetite',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))


Krb_filename = '../malaria_diagnosis_rule_questions.krb'
Krb_lineno_map = (
    ((12, 16), (5, 5)),
    ((17, 18), (7, 7)),
    ((27, 31), (11, 11)),
    ((32, 33), (13, 13)),
    ((42, 46), (17, 17)),
    ((47, 48), (19, 19)),
    ((57, 61), (23, 23)),
    ((62, 66), (24, 24)),
    ((67, 68), (26, 26)),
    ((77, 81), (30, 30)),
    ((82, 86), (31, 31)),
    ((87, 88), (33, 33)),
    ((97, 101), (38, 38)),
    ((102, 106), (39, 39)),
    ((107, 108), (41, 41)),
    ((117, 121), (45, 45)),
    ((122, 126), (46, 46)),
    ((127, 128), (48, 48)),
    ((137, 141), (52, 52)),
    ((142, 143), (54, 54)),
    ((152, 156), (58, 58)),
    ((157, 158), (60, 60)),
    ((167, 171), (64, 64)),
    ((172, 176), (65, 65)),
    ((177, 178), (67, 67)),
    ((187, 191), (71, 71)),
    ((192, 196), (72, 72)),
    ((197, 198), (74, 74)),
    ((207, 211), (78, 78)),
    ((212, 216), (79, 79)),
    ((217, 218), (81, 81)),
    ((227, 231), (86, 86)),
    ((232, 236), (87, 87)),
    ((237, 238), (89, 89)),
    ((247, 251), (93, 93)),
    ((252, 256), (94, 94)),
    ((257, 258), (96, 96)),
    ((267, 271), (101, 101)),
    ((272, 276), (102, 102)),
    ((277, 278), (104, 104)),
    ((287, 291), (109, 109)),
    ((292, 296), (110, 110)),
    ((297, 298), (112, 112)),
    ((307, 311), (117, 117)),
    ((312, 316), (118, 118)),
    ((317, 318), (120, 120)),
    ((327, 331), (125, 125)),
    ((332, 336), (126, 126)),
    ((337, 338), (128, 128)),
    ((347, 351), (133, 133)),
    ((352, 356), (134, 134)),
    ((357, 358), (136, 136)),
    ((367, 371), (141, 141)),
    ((372, 376), (142, 142)),
    ((377, 378), (144, 144)),
    ((387, 391), (149, 149)),
    ((392, 396), (150, 150)),
    ((397, 398), (152, 152)),
)
