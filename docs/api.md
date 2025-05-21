# API: Dinero Methods

::: dinero.Dinero
    options:
        members:
            - format
            - add
            - subtract
            - multiply
            - divide
            - convert
            - eq
            - gt
            - gte
            - lt
            - lte
            - to_dict
            - to_json
        show_root_toc_entry: False

::: dinero.tools.vat
    options:
        members:
            - calculate_net_amount
            - calculate_vat_portion
            - calculate_gross_amount
        show_root_toc_entry: False

::: dinero.tools.percentage
    options:
        members:
            - calculate_percentage
        show_root_toc_entry: False

::: dinero.tools.conversion
    options:
        members:
            - convert
        show_root_toc_entry: False

::: dinero.tools.interest
    options:
        members:
            - calculate_simple_interest
            - calculate_compound_interest
        show_root_toc_entry: False

::: dinero.tools.markup
    options:
        members:
            - calculate_base_amount
            - calculate_markup_portion
            - calculate_marked_up_amount
        show_root_toc_entry: False

::: dinero.tools.margin
    options:
        members:
            - calculate_cost_amount
            - calculate_margin_portion
            - calculate_selling_price
        show_root_toc_entry: False