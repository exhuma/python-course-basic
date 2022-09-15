# Advanced Topics & Notes

## Imports & Caching

- Importing will cause .pyc files to be created (inside the `__pycache__`
  folder). They are auto-generated and don’t belong into revision control.
- Imports are cached. The code inside a module is only interpreted on first
  import. (Advanced: The cached modules are available in `sys.modules`).
- Therefore, modules can be abused as global variable storage & singletons
  (with all the risks this implies).
