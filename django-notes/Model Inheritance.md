Found in #chapter12 of **Django 5 By Example**
## Types
#### Abstract Models:
```
class Meta:
	abstract = True
```

#### Multi-table Inheritance:
Each class has a table, sub-model has a pointer to the original model.

#### Proxy Models:
For customizing behavior for different models without creating tables for each model.
```
class Meta:
	proxy = True
```
Sub-model operates on the same table as the original model.