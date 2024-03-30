'''
Если я правильно понимаю, то даны две таблицы products и categories,
связанные многие-ко-многим через промежуточную таблицу с парами
соответствующих id. Тогда следующий код вернет пары продукт - категория и
продукт - null, если у продукта нет категории.
'''
products.join(
    product_categories, products.id == product_categories.product_id, 'left'
).join(
    categories, categories.id == product_categories.category_id, 'left'
).select('product', 'category')
