# Aplicación de Mantenimiento Predictivo con Machine Learning

Este repositorio contiene el código para una aplicación de mantenimiento predictivo que utiliza el aprendizaje automático para predecir cuándo es probable que falle una máquina rotativa en función de diversas variables operativas, como temperatura, rotación, torque y más. El proyecto está orquestado mediante GitHub Actions para garantizar flujos de Integración Continua y Despliegue Continuo (CI/CD) automatizados que finalmente despliegan la aplicación en Azure para su consumo por parte de los usuarios finales.

## Resumen

La aplicación de mantenimiento predictivo consta de los siguientes componentes principales:

1. **Modelo de Aprendizaje Automático**: Se entrena un modelo de aprendizaje automático con datos históricos para predecir fallos de la máquina. La precisión del modelo se prueba continuamente con un conjunto de validación.

2. **API REST**: Se crea una API para exponer el modelo de aprendizaje automático para predicciones en tiempo real. Se realizan pruebas en esta API para garantizar su fiabilidad.

3. **Contenedorización**: La aplicación y sus dependencias se contenerizan mediante Docker. Estas imágenes de contenedor se envían a un Registro de Contenedores de Azure (ACR) para facilitar el despliegue.

4. **Azure Web App**: La aplicación se aloja como una aplicación web mediante el servicio Azure Web App. La última versión de la aplicación se despliega y se pone a disposición de los usuarios finales.

## Flujo de GitHub Actions

El flujo de CI/CD se orquesta mediante una serie de disparadores de GitHub Actions:

### Acción 1: Prueba de Precisión del Modelo
- Disparador: Evento Push en el repositorio remoto de GitHub.
- Propósito: Esta acción prueba la precisión del modelo de aprendizaje automático utilizando datos de validación. Si la precisión supera el 90%, pasa al siguiente paso.

### Acción 2: Prueba Unitaria de la API
- Disparador: Finalización exitosa de la Acción 1 (prueba de precisión del modelo).
- Propósito: Esta acción realiza pruebas unitarias en la API REST creada con el modelo de aprendizaje automático entrenado.

### Acción 3: Contenerización y Despliegue
- Disparador: Finalización exitosa de la Acción 2 (prueba unitaria de la API).
- Propósito: Esta acción conteneriza la aplicación y sus dependencias, envía las imágenes de contenedor al Registro de Contenedores de Azure y despliega la última versión de la aplicación web en el servicio Azure Web App.

## Acceso a la Aplicación

Puede acceder a la aplicación de mantenimiento predictivo desplegada utilizando la siguiente URL: [Aplicación de Mantenimiento Predictivo](https://lnkd.in/e2RP_VTq).

## Repositorio

El código fuente de este proyecto está disponible en el siguiente repositorio de GitHub: [Repositorio de GitHub de Mantenimiento Predictivo](https://lnkd.in/eSQ4M8AD).

## Empezar

Para comenzar con este proyecto, puede clonar el repositorio y seguir las instrucciones en los archivos README dentro de cada directorio de los componentes.

¡Gracias por tu interés en nuestra aplicación de mantenimiento predictivo! Si tienes alguna pregunta o comentario, no dudes en ponerte en contacto con nosotros.
