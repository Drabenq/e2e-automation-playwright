# Cómo funciona (guía para explicarlo en una entrevista)

## Page Object Model
Cada página del sitio es una clase con sus selectores y acciones (`login()`, `add_to_cart()`). Los tests solo describen lo que hace el usuario. Si cambia un selector, se arregla en un único archivo.

## Preguntas típicas
- **¿Por qué no usás `time.sleep`?** `expect(...)` de Playwright reintenta hasta que la condición se cumple o vence el tiempo. Es más rápido y menos flaky.
- **¿Cómo elegís los selectores?** Primero roles accesibles y atributos `data-test`, que el equipo de desarrollo pone para testing. Nunca rutas tipo `div > div:nth-child(3)`.
- **¿Cómo depurás un fallo en CI?** Se guarda captura y *trace* (una grabación paso a paso con DOM, red y consola) y se suben como artifact.
- **¿Por qué el test del total?** Es una validación de negocio: no solo que aparezca un número, sino que subtotal + impuestos = total.
- **¿Qué agregarías?** Ejecución en Firefox y WebKit, tests en paralelo con `pytest-xdist` y pruebas visuales.
