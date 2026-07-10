# Portfolio de Data Science & Machine Learning

## Perfil Profesional

Licenciado en Economía con formación especializada en Ciencia de Datos e Inteligencia Artificial. Mi perfil combina estadística, modelado predictivo y conocimiento de negocio para transformar datos en soluciones analíticas.

He desarrollado proyectos de Machine Learning aplicados a problemas de predicción, clasificación y toma de decisiones, utilizando Python, SQL, modelos estadísticos y herramientas de análisis de datos.

Mi principal interés se encuentra en modelos predictivos, analítica avanzada y aplicaciones de Data Science en industrias basadas en datos como fintech, banca y servicios digitales.

---

# Proyectos Destacados

# AI-Powered Predictive Customer Retention Strategy (Churn Prediction)

**Proyecto Final – GCI World 2026 Spring**  
**Matsuo-Iwasawa Laboratory – The University of Tokyo (UTokyo)**

📊 **Presentación del proyecto:**  
https://drive.google.com/file/d/18-X6A8nVYn-3PMJaWApbewK7TLMxYeoD/view?usp=sharing

💻 **Notebook:**  
https://colab.research.google.com/drive/1antTEjRSfxvb-666R7btfp35lg8GTsV6?usp=drive_link

## Descripción del Proyecto

Desarrollo de una solución completa de Machine Learning para predecir la fuga de clientes (churn) en una empresa de telecomunicaciones.

El objetivo fue construir un modelo predictivo capaz de identificar clientes con alta probabilidad de abandono y transformar esas predicciones en estrategias de retención basadas en datos.

## Problema de Negocio

La empresa contaba con un gran volumen de datos históricos de clientes, pero no disponía de una herramienta predictiva para identificar de forma eficiente aquellos usuarios con mayor riesgo de abandono.

El desafío consistió en convertir datos de comportamiento, consumo y facturación en una herramienta analítica para mejorar la toma de decisiones y optimizar campañas de retención.

## Metodología y Desarrollo Técnico

- Análisis exploratorio de datos (EDA) sobre aproximadamente 100.000 registros y múltiples variables de comportamiento.
- Identificación de patrones de clientes, valores faltantes, distribuciones y variables relevantes.
- Desarrollo de variables predictivas (Feature Engineering) basadas en conocimiento del negocio:
  - Comportamiento de consumo.
  - Estabilidad del cliente.
  - Presión de facturación.
  - Evolución del uso del servicio.
- Construcción de un enfoque de Machine Learning combinado:
  - **LightGBM** para capturar relaciones no lineales complejas.
  - **Regresión Logística con penalización Lasso** para interpretación y análisis de variables.
  - **CatBoost** como modelo comparativo.
- Validación mediante **Stratified K-Fold Cross Validation**.
- Optimización del umbral de clasificación para equilibrar Precision y Recall según objetivos de negocio.
- Implementación de técnicas de Explainable AI (XAI) mediante **SHAP Values** para interpretar los factores asociados al churn.

## Resultados Principales

- ROC-AUC: **0.704**
- KS Statistic: **0.291**
- Precision@Top10%: **81.25%**
- Recall aproximado: **77%**
- Identificación de los principales factores asociados al abandono mediante interpretabilidad del modelo.

El modelo permitió construir un enfoque predictivo orientado a priorizar acciones de retención sobre clientes con mayor probabilidad de churn.

## Stack Tecnológico

Python · Pandas · NumPy · Scikit-Learn · LightGBM · CatBoost · SHAP · Matplotlib · Seaborn · Machine Learning Classification Models

---

# Sports Analytics & Predictive Modeling: NFL Draft Classification

**GCI Competition – Machine Learning Project**

💻 **Notebook:**  
https://colab.research.google.com/drive/1Xs1PmMyelE-YiP-FN-e_EU-9bM0X36m7?usp=sharing

## Descripción del Proyecto

Desarrollo de un pipeline completo de Machine Learning para predecir la probabilidad de que atletas universitarios sean seleccionados en el Draft de la NFL.

El proyecto aplicó técnicas de clasificación, ingeniería de características y validación de modelos para identificar patrones asociados al éxito deportivo.

## Metodología

- Análisis exploratorio de datos deportivos.
- Identificación de patrones predictivos en variables físicas y de rendimiento.
- Ingeniería de características basada en conocimiento del dominio:
  - Ratio velocidad/peso.
  - Índice de explosividad.
  - Índice de fuerza.
  - Composición corporal (BMI).
- Tratamiento y análisis de valores faltantes.
- Desarrollo de modelos de clasificación utilizando:
  - Random Forest.
- Evaluación mediante:
  - ROC-AUC.
  - Stratified K-Fold Cross Validation.
- Aplicación de técnicas para reducir sobreajuste y mejorar la generalización del modelo.

## Stack Tecnológico

Python · Pandas · Scikit-Learn · Random Forest · Feature Engineering · ROC-AUC

---

# Data Analytics & Engineering Projects

## Data Engineering Pipeline & Business Analytics

Desarrollo de soluciones analíticas utilizando:

- Python para procesamiento y automatización de datos.
- SQL para transformación, consultas y análisis.
- Google BigQuery para procesamiento en Cloud.
- Herramientas de visualización para seguimiento de indicadores de negocio.

Aplicación de técnicas de análisis de datos para generar insights relacionados con comportamiento de clientes, retención y performance.
