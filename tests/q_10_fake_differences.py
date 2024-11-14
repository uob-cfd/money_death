
test = {
  'name': 'Question 10_fake_differences',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'fake_differences'
          >>> assert 'fake_differences' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'fake_differences'
          >>> # from its initial state (of ...)
          >>> assert fake_differences is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Some of your fake differences seem very high.
          >>> np.all(fake_differences < 12500)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Some of your fake differences seem very low.
          >>> assert np.all(fake_differences > -12500)
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
