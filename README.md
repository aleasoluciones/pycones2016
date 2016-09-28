# PyConEs 2016: Taller introducción a TDD
<img src="https://pbs.twimg.com/profile_images/743356612086116355/6X4srwCV.jpg" width="250" alt="Logo PyConEs2016 Almería" />

## Preparación del entorno

Es necesario:

* Python >= 2.7
* Virtualenv
* Tu editor favorito (vim)

### Creación de un virtualenv

Instalación de virtualenv: http://rukbottoland.com/blog/tutorial-de-python-virtualenv/

Para crear el virtualenv hay dos opciones:

1. Usar directamente virtualenv:

  ```
  virtualenv fizzbuzz
  source fizzbuzz/bin/activate
  ```
2. O usar virtualenvwrapper (mkvirtualenv):

  ```
  mkvirtualenv fizzbuzz
  ```

### Instalar los requisitos
`pip install -r requirements-dev.txt`

## Ejectuar los tests
`mamba --format=documentation fizzbuzz_spec.py`
