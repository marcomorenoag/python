print(f'Invoking __init__.py for {__name__}')

'''__all__ is used by both packages and modules to control what is imported when import * is specified'''
'''
  For a package, when __all__ is not defined, import * does not import anything.
  For a module, when __all__ is not defined, import * imports everything (except names starting with an underscore).
'''
__all__ = [
  'func_performance'
]