# conan-rabbitmq-c

Conan package for [rabbitmq-c](https://github.com/alanxz/rabbitmq-c)

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/conan-community).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[![Download](https://api.bintray.com/packages/zimmerk/conan/rabbitmq-c%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/rabbitmq-c%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-rabbitmq-c.svg?branch=release%2F0.9.0)](https://travis-ci.org/AtaLuZiK/conan-rabbitmq-c)|[![Build status](https://ci.appveyor.com/api/projects/status/c4g3hkp67o3d6bjw/branch/release/0.9.0?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-rabbitmq-c/branch/release/0.9.0)|

## Reuse the packages

### Basic setup

```
conan install rabbitmq-c/0.9.0@zimmerk/stable
```

### Project setup

```
[requires]
rabbitmq-c/0.9.0@zimmerk/stable

[options]
rabbitmq-c:shared=True  # Build rabbitmq-c as a shared library
rabbitmq-c:ssl=True     # Enable SSL support

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
