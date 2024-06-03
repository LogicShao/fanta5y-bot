# fanta5y-bot

## ACM Helper Configuration Guide

### Setting the ACM Helper Proxy

1. Create a file named `acmhelper.env`.
2. Add the following line to the file:

```
port={Your port}
```

If this is not set, the system proxy will **not** be used.

### Configuring the Environment for ACM Helper

- To set the environment, you can either run the script:

```
python \myScript\setEnv.py
```

or directly add the following line to the `acmhelper.env` file:

```
port={Your system proxy port}
```

- If you choose to run locally, it will not link to QQ and will load a console. Otherwise, it will attempt to connect to your QQ server, which might be Lagrange.

## Using nb-cli

1. Generate a project using: `nb create`
2. Install plugins using: `nb plugin install`
3. Run your bot using: `nb run`


## Documentation

For more detailed information, please refer to the [NoneBot Documentation](https://nonebot.dev/).
