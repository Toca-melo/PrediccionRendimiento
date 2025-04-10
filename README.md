# 👩‍🏫 Predicción Rendimiento Académico
Este proyecto es una aplicación web desarrollada con Flask que permite predecir el rendimiento escolar de un estudiante teniendo en cuenta factores como el tiempo de estudio semanal, la cantidad de ausencias durante el año escolar, si asiste o no a tutorias, el nivel de apoyo parental y si realiza o no activdades extracurriculares. Si bien intentar predecir el rendimiento de un estudiante puede ser una labor desafiante ya que hay muchos factores que pueden intervenir, y que si bien tener buenos o malos hábitos de estudio no necesariamente garantizan un buen o mal desempeño, este ejercicio es útil para entender la aplicación de estrategias de clustering junto con un algoritmo de clasificación.

---
## 🗃️ Clustering y Modelo de Clasificación
El proceso de análisis de datos, selección de características, desarrollo del algoritmo de clustering y del modelo de clasificación fue realizado en **Google Colab**.
Puedes acceder al notebook completo en el siguiente enlace:

🔗 [**Notebook**](https://colab.research.google.com/drive/1ATiyDclKyiPCj1isOmM4OtnDhm07k8q0?usp=sharing)

## 🛠️ Principales Tecnologías Utilizadas

- 🔹 **Python**: Lenguaje de programación utilizado para el análisis de datos, el desarrollo del modelo de clasificación y el algoritmo de clustering.
- 🔹 **Flask**: Framework de Python empleado para desplegar una API web que permite probar el modelo de clasificación.
- 🔹 **Docker**: Plataforma de contenedores utilizada para empaquetar y desplegar la aplicación con todas sus dependencias.
- 🔹 **K-Means**: Algoritmo de aprendizaje no supervisado utilizado para el clustering.
- 🔹 **AdaBoostClassifier**: Algoritmo supervisado utilizado para realizar la predicción del rendimiento del estudiante.
- 🔹 **Google Colab**: Entorno de notebooks en la nube que facilita el desarrollo y la ejecución del código sin necesidad de configuración local.
- 🔹 **Render**: Plataforma de despliegue en la nube utilizada para alojar la API creada con Flask.

## 🗃️ Dataset
​El Students Performance Dataset de Rabie El Kharoua es un conjunto de datos sintético que recopila información detallada de 2,392 estudiantes de secundaria. Está diseñado para facilitar investigaciones educativas, análisis estadísticos y proyectos de aprendizaje automático. El dataset se encuentra en el siguiente enlace:

🔗 [**Students Performance Dataset** – Kaggle](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)

## 📊 Descripción de las Variables Utilizadas

### 🕒 StudyTimeWeekly
> **Cantidad de horas semanales** que un estudiante dedica al estudio.  
📈 Rango: `0 a 20`  
🔍 Este atributo es clave para analizar la relación entre el tiempo de estudio y el rendimiento académico.

---

### ❌ Absences
> **Número total de ausencias** durante el año escolar.  
📉 Las ausencias pueden afectar negativamente el desempeño académico, por lo que es un factor importante en los modelos predictivos.

---

### 🧑‍🏫 Tutoring
> Indica si el estudiante **recibe tutorías adicionales**.  
🔢 Tipo: Variable binaria

- `0`: No recibe tutoría  
- `1`: Sí recibe tutoría

---

### 👨‍👩‍👧 ParentalSupport
> Nivel de **apoyo parental hacia la educación** del estudiante.  
📏 Codificación:

- `0`: Ninguno  
- `1`: Bajo  
- `2`: Moderado  
- `3`: Alto  
- `4`: Muy alto

---

### 🎭 Extracurricular
> Indica si el estudiante participa en **actividades extracurriculares** como clubes, deportes o arte.  
🔢 Tipo: Variable binaria

- `0`: No participa  
- `1`: Participa

---


🧑‍💻 Autores
Valentina Beca
Brayan Zamora
