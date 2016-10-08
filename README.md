# PyConEs 2016: Taller introducción a TDD
<img src="https://pbs.twimg.com/profile_images/743356612086116355/6X4srwCV.jpg" width="250" alt="Logo PyConEs2016 Almería" />

## Información general
En este taller vamos a realizar una introducción a TDD, en concreto a través de la [kata fizzbuzz](http://www.solveet.com/exercises/Kata-FizzBuzz/11).

Para preparar el entorno adecuado y poder aprovechar mejor el tiempo durante el taller, por favor aseguraos de tener todo lo necesario correctamente instalado (más adelante se detallan los requisitos).

Tras el taller, también se facilitarán los slides de la presentación.


## Preparación del entorno

Es necesario:

* Git
* Python >= 2.7
* Virtualenv
* Tu editor favorito (vim)

### Clonar repositorio

```
git clone https://github.com/aleasoluciones/pycones2016.git
```

### Creación de un virtualenv

Instalación de virtualenv: http://rukbottoland.com/blog/tutorial-de-python-virtualenv/

Para crear el virtualenv hay dos opciones:

1. Usar directamente virtualenv:

  ```
  virtualenv fizzbuzz
  source fizzbuzz/bin/activate
  ```
2. Usar virtualenvwrapper (mkvirtualenv):

  ```
  mkvirtualenv fizzbuzz
  ```

  Si ya lo hemos creado usando `mkvirtualenv` con anterioridad, lo podemos activar de nuevo con:

  ```
  workon fizzbuzz
  ```

### Instalar los requisitos
`pip install -r requirements-dev.txt`

## Ejectuar los tests
Para verificar que todo está correctamente instalado y funcionando, ejecutar los tests:

`mamba --format=documentation fizzbuzz_spec.py`

## Soluciones
* https://github.com/jaimegildesagredo/fizzbuzz
* https://github.com/APA42/fizzbuzzkata
* https://github.com/islomar/katas/tree/master/fizzbuzz/python

