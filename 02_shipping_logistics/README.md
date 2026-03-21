# 📦 Reto #1: Logística de E-commerce (Nivel Intermedio)

## 🧠 Contexto del negocio
Tu cliente es **FastTrack Logística**. Actualmente tienen un problema:  
su sistema de almacén genera un archivo de texto desordenado donde toda la información está mezclada.

Necesitan:
- Calcular correctamente el **costo de envío**
- Filtrar los paquetes que son **demasiado pesados** para sus furgonetas pequeñas

---

## 📝 Especificaciones Técnicas (Requerimientos)

### 🔹 Extracción
- El archivo de entrada es: `data/envios_raw.txt`
- Utiliza el separador: `|` (pipe)

---

### 🔹 Transformación

- **ID_Envio**
  - Debe empezar por `"ID-"`
  - Ejemplo: `ID-101`

- **Destino**
  - Convertir todo a **MAYÚSCULAS**

- **Peso**
  - Viene como texto con `"kg"` (ej: `"15kg"`)
  - Extraer solo el número y convertirlo a tipo `float`

- **Costo de Envío**
  - Fórmula:
  
    ```
    Costo = Peso × 2.5€
    ```

---

### ⚠️ Filtro Crítico
- Si el paquete pesa **más de 20 kg**, debe ser **excluido**
- Estos envíos pertenecen a otra ruta (camiones)

---

### 💾 Carga (Output)
- Guardar el resultado en: `output/envios_limpios.csv`

- Columnas finales:
  - `ID`
  - `Ciudad`
  - `Peso(kg)`
  - `Costo(€)`

---

## 🎯 Objetivo
Limpiar, transformar y filtrar los datos para generar un archivo estructurado listo para ser utilizado por el equipo logístico.