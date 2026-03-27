# 🏗️ Reto #5: Auditoría Multi-Almacén (LogiTrack Global)

## 🏢 Cliente: LogiTrack Global
**Contexto:** El cliente es una empresa de logística internacional que recibe diariamente reportes de envíos de tres almacenes distintos: **Madrid, Valencia y Barcelona**. 

Actualmente, el proceso de consolidación de datos es manual y propenso a errores. El sistema central de la empresa falla si recibe datos con formatos incorrectos, pesos negativos o zonas no autorizadas.

---

## 🎯 Objetivo del Proyecto
Desarrollar un pipeline ETL robusto en **Python puro** que:
1.  Automatice la lectura de múltiples archivos en un directorio.
2.  Valide cada registro según reglas de negocio estrictas.
3.  Separe los datos limpios de los corruptos, generando un reporte de errores detallado para el equipo de operaciones.

---

## 🛠️ Especificaciones Técnicas

### 1. Extracción (Multi-archivo)
- Escaneo automático de la carpeta `data/` usando la librería `os`.
- Identificación y procesamiento exclusivo de archivos con extensión `.csv`.

### 2. Transformación (Validaciones de Calidad)
Cada registro debe cumplir con las siguientes reglas para ser considerado **VÁLIDO**:
- **ID_Envio:** No puede estar vacío.
- **Peso (kg):** Debe ser un valor numérico (`float`) y estrictamente mayor a 0.
- **Zona:** Solo se aceptan los valores: `Norte`, `Sur`, `Este`, `Oeste`.
- **Costo:** Debe ser un valor numérico positivo.

### 3. Carga y Clasificación
El sistema genera dos archivos de salida en la carpeta `output/`:
- **`envios_limpios.csv`**: Registros validados con una columna extra que indica el `Origen_Archivo`.
- **`reporte_errores.csv`**: Registros fallidos con una columna descriptiva del `Motivo_Error`.

