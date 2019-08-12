# Python

## vscode settings

### language server

* https://github.com/microsoft/python-language-server/issues/1085

```json
{
    "python.jediEnabled": false,
    "python.autoComplete.extraPaths": [
        "./fluent"
    ],
}
```

### pytest

* http://doc.pytest.org/en/latest/goodpractices.html

```json
{
    "python.testing.pytestArgs": [
        "fluent"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestEnabled": true
}
```

* ```tests```
  * ```__init__.py```

### jupyter

```json
{
    "python.dataScience.notebookFileRoot": "${workspaceFolder}/fluent"
}
```
