# 📦 Reto #4: Auditoría de Ventas e Inventario (E-commerce)

## 🧠 Cliente
**GadgetStore Global**

---

## 🧾 Contexto del negocio
El cliente dispone de un reporte de ventas que incluye:

- Ingreso total
- Unidades vendidas

Necesitan calcular el **precio unitario** de cada producto para detectar posibles anomalías en los datos.

👉 Problema:  
Existen filas con:
- Unidades en **0** (devoluciones)
- Valores incorrectos o no numéricos

Si no se controlan, el programa puede fallar por división entre cero o conversiones inválidas.

---

## 📝 Especificaciones Técnicas (Requerimientos)

### 🔹 1. Extracción
- Archivo de entrada: `05_Sales_Audit/data/ventas_raw.csv`
- Separador: `,`

**Formato de cada fila:**

- ID_Prod,Nombre_Prod,Ingreso_Total,Unidades


---

### 🔹 2. Transformación (Zona de entrenamiento)

#### 🧹 Limpieza de datos
- Convertir:
  - `Ingreso_Total` → `float`
  - `Unidades` → `int`

---

#### 🧮 Cálculo crítico
Calcular el precio unitario:

Precio_Unitario = Ingreso_Total / Unidades

---

#### ⚠️ Manejo de errores (doble escudo)

Debes controlar dos tipos de errores:

- `ValueError`:
  - Cuando los datos no son numéricos (ej: `"N/A"`, vacío, `"ERROR"`)

- `ZeroDivisionError`:
  - Cuando `Unidades = 0`

👉 En ambos casos:
- El `Precio_Unitario` debe ser `0.0`
- El nombre del producto debe empezar por:  
  `"⚠️ REVISAR:"`

---

#### 🧩 Estructura de la transformación
- Construir la fila completa dentro del bloque `try`
- Usar `except (ValueError, ZeroDivisionError)`
- Realizar **un único `append` final por iteración**

---

### 🔹 3. Carga (Output)
- Archivo de salida: `05_Sales_Audit/output/auditoria_precios.csv`

**Columnas finales:**
- ID  
- Producto  
- Ingreso  
- Unidades  
- Precio_Unitario  

---

## 🧪 Datos de Entrada (data/ventas_raw.csv)

- P001,Teclado Mecánico,1200.50,20
- P002,Ratón Gaming,450.00,0
- P003,Monitor 4K,ERROR,5
- P004,Auriculares BT,300.00,10
- P005,Webcam HD,150.00,


---
## 🎯 Objetivo

Construir un pipeline que:

- Lea datos de ventas
- Limpie y transforme los registros
- Calcule precios unitarios correctamente
- Maneje errores sin romper el programa
- Genere un archivo final listo para auditoría