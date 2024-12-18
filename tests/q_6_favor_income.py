
test = {
  'name': 'Question 6_favor_income',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'favor_income'
          >>> 'favor_income' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'favor_income'
          >>> # from its initial state (of ...)
          >>> favor_income is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert len(favor_income) == np.count_nonzero(death == 'Favor')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert favor_income.median() == 32499.5
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
