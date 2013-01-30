Product Variant Name Module
===========================

This OpenERP module change how the product name is computed in a order line.

If the product have variants description, use:

    name_template + variants

else use:

    name + variants

Without this module, when product have variants, the variant description
is added twice to the name.

Also when a product without variants is renamed, than the product template
is renamed too.

This sources are available in https://github.com/eoconsulting/product_variant_name

__________

[Enterprise Objects Consulting](http://www.eoconsulting.com.ar)
