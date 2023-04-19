# apinator-secoda

[`apinator` bindings](https://pypi.org/project/apinator/) for the [Databricks API](https://docs.databricks.com/api-explorer/).

## Example

```python
from apinator_secoda.common import DatabricksContext
from apinator_secoda.unity_catalog import DatabricksUnityCatalogApi, uc_model

context = DatabricksContext(
        access_token="TOKEN",  # Will be kept secret
        account="account",
    )
api = DatabricksUnityCatalogApi(context)
shares: uc_model.ShareList = api.datashares.list()
for share in shares.shares:
    assert isinstance(share, uc_model.SharePartial)  # Not necessary, pydantic guarantees this
    ...
```
