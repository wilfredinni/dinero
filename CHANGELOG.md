# Changelog

## [0.4.0](https://github.com/wilfredinni/dinero/compare/0.2.1...master)

- Added currency conversion functionality with `convert()` method
- Added new tools:
    - `calculate_base_amount()`
    - `calculate_markup_portion()`
    - `calculate_marked_up_amount()`
    - `calculate_cost_amount()`
    - `calculate_margin_portion()`
    - `calculate_selling_price()`
    - `calculate_net_amount()`
    - `calculate_vat_portion()`
    - `calculate_gross_amount()`
    - `convert()`
- Comparison operators where renamed to `eq`, `gt`, `gte`, `lt`, and `lte`.
- Modularize tools validators.


## [0.2.1](https://github.com/wilfredinni/dinero/releases/tag/0.2.1)

- Modularized the codebase.
- Removed unused conversions to string.
- Fixed Circular imports.
- Fixed Type linting errors.

## [0.2.0](https://github.com/wilfredinni/dinero/releases/tag/0.2.0) (2023-05-14)

- Added new `tools` module.
- Added `calculate_simple_interest` tool.
- Added `calculate_compound_interest` tool.
- Added `calculate_vat` tool.
- Added `calculate_percentage` tool.
- Update documentation.
- Update dependencies to the latest versions.

## [0.1.8](https://github.com/wilfredinni/dinero/releases/tag/0.1.8) (2023-03-11)

- Update dependencies to the latest versions.
- Updated README and documentation.
- Fix security vulnerabilities.

## [0.1.7](https://github.com/wilfredinni/dinero/releases/tag/0.1.7) (2023-03-05)

- Update dependencies to the latest versions.
- Updated README and documentation.

## [0.1.6](https://github.com/wilfredinni/dinero/releases/tag/0.1.6) (2022-11-19)

- 100% code coverage 🎉
- Fixed Type Hints for `multiply` and `divide` methods.
- Fixed `InvalidOperationError` not raising when comparing against a non `Dinero` object.
- Removed orphan lines of code.
- Move validators to their own module.

## [0.1.5](https://github.com/wilfredinni/dinero/releases/tag/0.1.5) (2022-11-03)

- It is no longer possible to compare a `Dinero` instance to objects of other types ([796b9e2](https://github.com/wilfredinni/dinero/commit/796b9e2e1f344f20be14edffc9a0579192d9a93b)).
- Multiplication and division can be performed only with `int`, `float` and `Decimal` types ([326ad3a](https://github.com/wilfredinni/dinero/commit/326ad3a007c625e22fba2b265c093ee13f8a90d2)).
- Added GitHub community files: SECURITY, CHANGELOG and CONTRIBUTING.
- Added coverage and code quality checks.

## [0.1.4](https://github.com/wilfredinni/dinero/releases/tag/0.1.4) (2022-11-03)

- Added `typing-extensions` dependency.

## [0.1.3](https://github.com/wilfredinni/dinero/releases/tag/0.1.3) (2022-11-03)

Initial release
