# Python plugin

## Plugin overview

This repository provides a sample [Python](https://www.python.org/) plugin for [Tyk](https://tyk.io).

The project implements a simple middleware for header injection, using a **Pre** hook (see [Tyk custom middleware hooks](https://tyk.io/docs/tyk-api-gateway-v1-9/javascript-plugins/middleware-scripting/)). A single Python script contains the code for it, see [mymiddleware.py](mymiddleware.py).

## Requirements

See [Python Rich Plugins](https://tyk.io).

## Instructions

After checking the requirements, clone this repository:

```
$ git clone https://github.com/TykTechnologies/tyk-plugin-demo-python.git
```

Enter the plugin directory:

```
$ cd tyk-plugin-demo-python
```

## Building a bundle

Python plugins are delivered as plugin bundles. The manifest file (`manifest.json`) contains the custom middleware definition. The manifest references the files that should be part of the bundle.

```
$ tyk-cli bundle build
```

You may check the [tyk-cli documentation](https://github.com/TykTechnologies/tyk-cli) for additional options.

## Additional documentation

- [An overview of Python support in Tyk]()
