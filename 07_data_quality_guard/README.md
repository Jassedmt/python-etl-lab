# 🏗️ Reto #6: Integración de Ventas Multicanal (RetailSync Pro)


## 🏢 Cliente: RetailSync Pro

**Contexto:** RetailSync Pro es una empresa de retail que vende productos a través de múltiples canales:

**🛒 Tienda física**
**🌐 Ecommerce**
**📱 App móvil**

Cada canal genera archivos diarios con ventas, pero:

- Los formatos no son consistentes
- Hay duplicados
- Hay errores en precios y fechas

El equipo necesita un sistema automático para consolidar todo correctamente.

### 🎯 Objetivo del Proyecto

Construir un pipeline ETL en Python puro que:

1. Lea múltiples archivos de distintas fuentes
2. Normalice y valide los datos
3. Detecte duplicados
4. Genere datasets limpios + métricas de calidad


## 🛠️ Especificaciones Técnicas

### 1. 📥 Extracción (Multi-formato)
Leer archivos desde ``data/``
Tipos permitidos:
.csv
.json

Usar:

os → recorrer directorio
csv y json → parseo

### 2. 🔄 Transformación (Normalización + Validación)

**Cada registro debe tener esta estructura final:**

- ID_Venta
- Fecha
- Canal
- Producto
- Cantidad
- Precio_Unitario
- Total

### 🧹 Reglas de Normalización

**Canal:**

"store" → Tienda
"web" → Ecommerce
"app" → App

**Fecha:**

Convertir a formato: YYYY-MM-DD
(pueden venir como DD/MM/YYYY o YYYY/MM/DD)

**Total:**

Si no existe → calcular:

Total = Cantidad * Precio_Unitario
✅ Reglas de Validación

**Un registro es válido si:**

- ID_Venta: no vacío
- Cantidad: entero > 0
- Precio_Unitario: float > 0
- Total: coherente con cálculo
- Fecha: válida
- Canal: dentro de valores permitidos

### 🚫 Detección de Duplicados

Un registro se considera duplicado si:

- ID_Venta + Canal

ya existe.

**👉 Solo conservar el primero, los demás → errores.**

### 3. 📤 Carga y Clasificación

**Generar en output/:**

✅ ventas_limpias.csv
Datos válidos
Columnas finales normalizadas

**Añadir:**

Origen_Archivo
❌ ventas_erroneas.csv
Registros inválidos

**Añadir:**

Motivo_Error
📊 resumen_calidad.txt

**Un pequeño reporte con:**

- Total registros procesados
- Registros válidos
- Registros inválidos
- Duplicados detectados
- % calidad de datos

### 🧠 BONUS (Nivel PRO)

Si quieres hacerlo más realista:

Crear funciones separadas:
1. extract()
2. transform()
3. validate()
4. load()
5. Añadir logging con logging
6. Manejar errores con try/except
7. Permitir configuración desde un .json (zonas válidas, formatos, etc.)

### 💡 Pista de estructura
data/
    ventas_tienda.csv
    ventas_web.json
    ventas_app.csv

output/
🚀 Qué vas a practicar aquí
ETL real multi-formato
Limpieza de datos
Validación robusta
Manejo de errores
Diseño modular
Lógica de negocio (muy importante en data engineering)