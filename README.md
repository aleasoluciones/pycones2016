# PyConEs 2016: Taller introducción a TDD

## Preparación del entorno

Es necesario:

* Python >= 2.7
* Virtualenv
* Tu editor favorito (vim)

### Creación de un virtualenv

#### Instalación de virtualenv
http://rukbottoland.com/blog/tutorial-de-python-virtualenv/

#### Usando virtualenv

```
virtualenv fizzbuzz
source fizzbuzz/bin/activate
```

#### Usando virtualenvwrapper (mkvirtualenv)

```
mkvirtualenv fizzbuzz
```

### Instalar los requisitos
`pip install -r requirements-dev.txt`

## Ejectuar los tests
`mamba --format=documentation fizzbuzz_spec.py`
